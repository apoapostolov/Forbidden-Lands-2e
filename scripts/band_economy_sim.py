#!/usr/bin/env python3
"""
Mercenary Band Economy Simulator — Forbidden Lands 2E
Simulates 1 year (365 days) of operations.

Two pay models:
  v1_daily    — Full daily wages always (baseline, broken economy)
  v2_retainer — Retainer during dead weeks, mission pay when active,
                loot shares on combat outcomes

Results saved to scripts/sim_results/ as JSON.

Run:  python3 scripts/band_economy_sim.py
"""

import random
import statistics
import json
import os
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Optional, List, Tuple, Dict, Any
from collections import defaultdict
from datetime import datetime


# ─── SIMULATION PARAMETERS ──────────────────────────────────────────────────

RUNS        = 200
SIM_DAYS    = 365
SEED_BASE   = 42
WORLD_SIZE  = 12
RESULTS_DIR = "scripts/sim_results"

# ─── WAGES (silver/day) ─────────────────────────────────────────────────────

WAGE = {
    "common":          1,
    "veteran":         2,
    "elite":           3,
    "named_man":       3,
    "caster_initiate": 6,
    "caster_adept":    15,
}

# ─── V2 RETAINER (silver/week during dead weeks) ────────────────────────────

RETAINER_WEEKLY = {
    "common":          2.0,
    "veteran":         3.0,
    "named_man":       5.0,
    "caster_initiate": 8.0,
    "caster_adept":   12.0,
}

# ─── V5: MISSION PAY FRACTION ─────────────────────────────────────────────
# Mission pay = half the full daily wage, accrued only during active work days.
# Travel to the contract site stays on retainer.

MISSION_PAY_FRACTION = 0.50

# ─── V6: STRUGGLING WORLD CONTRACT PRICING ────────────────────────────────
# Base rates: −30% off V3. Captain may haggle at contract acceptance.
# Haggle roll: HAGGLE_DICE d6. One or more 6s → pay scales to −20% floor.
# With 2 dice: ~31% chance of haggle success per contract.

HAGGLE_DICE       = 2
HAGGLE_BONUS_MULT = 0.80 / 0.70   # ratio of −20% to −30% discount off V3 originals

CONTRACT_TYPES_V6 = [
    # (name, min_pay, max_pay, duration_days, employer_tier_min, garrison_mode)
    ("patrol_week",         77,  116,  7,  "town",     False),
    ("escort",              56,   98,  5,  "town",     False),
    ("clearing",           112,  182, 10,  "town",     False),
    ("protection_season",  385,  560, 91,  "town",     True ),   # garrison
    ("warchief_raid",      158,  266, 14,  "warchief", False),
    ("garrison_short",     238,  350, 21,  "warchief", False),
    ("magical_commission", 196,  294, 12,  "town",     False),   # caster only
    ("ritual_ward",        130,  210,  8,  "warchief", False),   # caster only
]

# ─── V2 LOOT SPLIT ──────────────────────────────────────────────────────────

V2_LOOT_MEN_SHARE   = 0.60   # fraction of loot pool paid to fighters
V2_LOOT_TIER = {             # fraction of men's share per tier
    "named_man": 0.50,
    "veteran":   0.30,
    "common":    0.20,
}
V2_BATTLE_PRIZE_PCT = 0.10   # fraction of contract pay treated as battle prize (loot event)

# ─── FORAGER TABLE ──────────────────────────────────────────────────────────
# Columns: 1-2 foragers | 3-5 | 6-10 | 11+

FORAGE_TABLE = {
    "forest":      [3,  8, 16, 28],
    "dark_forest": [3,  8, 16, 28],
    "hills":       [2,  7, 13, 22],
    "plains":      [2,  5, 10, 18],
    "ruins":       [1,  3,  7, 12],
    "tundra":      [0,  2,  4,  8],
    "settlement":  [0,  0,  0,  0],
}

FOOD_PER_MAN_DAY = 1
FOOD_PRICE       = 0.15   # silver per FOOD unit

# ─── CONTRACT TYPES ─────────────────────────────────────────────────────────

CONTRACT_TYPES = [
    ("patrol_week",    50,  90,   7,  "town"),
    ("escort",         60, 130,   5,  "town"),
    ("clearing",      100, 220,  10,  "town"),
    ("warchief_raid", 200, 450,  14,  "warchief"),
    ("garrison_duty",  80, 150,  21,  "warchief"),
]

BOUNTY_TABLE = [
    ("local criminal",              5,  15),
    ("named bandit",               10,  25),
    ("deserter",                    2,   5),
    ("warlord enemy",              50, 200),
    ("professional breach",        10,  30),
]

TRIBUTE_VILLAGE = [(3,12),(1,2),(1,4),(0,1),(0,3),(0,0)]
TRIBUTE_TOWN    = [(3,18),(7,21),(7,21),(2,7),(3,12),(5,30)]

# ─── V3: REPRICED CONTRACTS AND CASTER UTILITY ──────────────────────────────
# Contract floor:  band_daily_cost(13s) × duration × 1.25
# Protection season: garrison mode — band stays on retainer pay; employer
#   subsidises the dead weeks. Net: ~675s income vs ~400s retainer+food cost.
# Caster contracts: only taken by bands that have at least one caster.

CONTRACT_TYPES_V3 = [
    # (name, min_pay, max_pay, duration_days, employer_tier_min, garrison_mode)
    ("patrol_week",        110, 165,  7,  "town",     False),
    ("escort",              80, 140,  5,  "town",     False),
    ("clearing",           160, 260, 10,  "town",     False),
    ("protection_season",  550, 800, 91,  "town",     True ),   # garrison
    ("warchief_raid",      225, 380, 14,  "warchief", False),
    ("garrison_short",     340, 500, 21,  "warchief", False),
    ("magical_commission", 280, 420, 12,  "town",     False),   # caster only
    ("ritual_ward",        185, 300,  8,  "warchief", False),   # caster only
]

CONTRACT_TYPES_V3_CASTER_ONLY = {"magical_commission", "ritual_ward"}

BOUNTY_TABLE_V3 = [
    ("local criminal",         12,  30),
    ("named bandit",           25,  60),
    ("deserter",                5,  12),
    ("warlord enemy",          80, 300),
    ("professional breach",    25,  60),
]

# Caster combat utility (all models): presence of a caster reduces casualties
CASTER_CASUALTY_REDUCTION = 0.40   # 40% reduction to base casualty rate

# V3 caster premium: bands with a caster negotiate higher pay on standard contracts
CASTER_CONTRACT_PREMIUM   = 0.35

# ─── COMBAT ─────────────────────────────────────────────────────────────────

CASUALTY_RATE_NORMAL = 0.08
CASUALTY_RATE_HARD   = 0.15
FIGHT_CHANCE_PER_CONTRACT = 0.70

# ─── MORALE ─────────────────────────────────────────────────────────────────

MORALE_START  = 4
MORALE_MIN    = 1
MORALE_MAX    = 6

NP_THRESHOLD_V1          = 7
NP_THRESHOLD_V2_RETAINER = 14
NP_THRESHOLD_V2_MISSION  = 3


def non_payment_roll(rng, diff_plus=0):
    r = rng.randint(1, 6) + diff_plus
    if r <= 1: return "desert_d3"
    if r == 2: return "equipment_stolen"
    if r <= 5: return "morale_hit"
    return "remembered"


# ─── HEX WORLD ──────────────────────────────────────────────────────────────

class SettlementTier(IntEnum):
    NONE     = 0
    VILLAGE  = 1
    TOWN     = 2
    WARCHIEF = 3


@dataclass
class Hex:
    x: int
    y: int
    terrain: str
    settlement: SettlementTier = SettlementTier.NONE
    feud_track: int = 0
    contract_available: Optional[dict] = None
    bounty_available:   Optional[dict] = None
    contract_cooldown:  int = 0
    tribute_drained:    int = 0


def build_world(rng, size=WORLD_SIZE):
    terrains = (["forest"]*30 + ["dark_forest"]*5 + ["plains"]*20 + ["hills"]*20
                + ["ruins"]*10 + ["tundra"]*5 + ["settlement"]*10)
    world = {}
    for x in range(size):
        for y in range(size):
            t = rng.choice(terrains)
            tier = SettlementTier.NONE
            if t == "settlement":
                r = rng.random()
                if r < 0.50:   tier = SettlementTier.VILLAGE
                elif r < 0.80: tier = SettlementTier.TOWN
                else:          tier = SettlementTier.WARCHIEF
            elif rng.random() < 0.08:
                tier = SettlementTier.VILLAGE
            world[(x, y)] = Hex(x, y, t, tier)
    return world


def refresh_contracts(world, rng, contracts=None, bounties=None):
    if contracts is None: contracts = CONTRACT_TYPES
    if bounties  is None: bounties  = BOUNTY_TABLE
    for h in world.values():
        if h.contract_cooldown > 0:
            h.contract_cooldown -= 1
        if h.settlement >= SettlementTier.TOWN:
            if h.contract_available is None and h.contract_cooldown == 0:
                if rng.random() < 0.55:
                    tier_name = "warchief" if h.settlement == SettlementTier.WARCHIEF else "town"
                    eligible = [c for c in contracts if c[4] == tier_name or c[4] == "town"]
                    ct = rng.choice(eligible)
                    h.contract_available = {
                        "name": ct[0],
                        "pay": round(rng.uniform(ct[1], ct[2]), 1),
                        "duration": ct[3] + rng.randint(-2, 2),
                        "hard": ct[0] in ("warchief_raid",),
                        "garrison": ct[5] if len(ct) > 5 else False,
                        "requires_caster": ct[0] in CONTRACT_TYPES_V3_CASTER_ONLY,
                    }
            if h.bounty_available is None and rng.random() < 0.25:
                bt = rng.choice(bounties)
                h.bounty_available = {"name": bt[0], "pay": rng.uniform(bt[1], bt[2])}


def distance(a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))


def nearest_employer(pos, world, min_tier=SettlementTier.TOWN):
    candidates = [(distance(pos, (h.x, h.y)), (h.x, h.y))
                  for h in world.values()
                  if h.contract_available is not None
                  and h.settlement >= min_tier
                  and h.feud_track < 3]
    return sorted(candidates)[0][1] if candidates else None


def step_toward(pos, target):
    dx, dy = target[0]-pos[0], target[1]-pos[1]
    return (pos[0]+(1 if dx>0 else -1 if dx<0 else 0),
            pos[1]+(1 if dy>0 else -1 if dy<0 else 0))


# ─── BAND ────────────────────────────────────────────────────────────────────

@dataclass
class Band:
    commons:   int   = 6
    veterans:  int   = 2
    elites:    int   = 0
    named_men: int   = 1
    casters:   int   = 0

    treasury:    float = 100.0
    morale:      int   = MORALE_START
    days_unpaid: int   = 0
    on_mission:  bool  = False
    days_since_contract: int = 0

    pos:              Tuple[int,int] = field(default_factory=lambda: (5,5))
    day:              int  = 0
    current_contract: Optional[dict] = None
    contract_day:     int  = 0

    income_contracts:    float = 0.0
    income_bounties:     float = 0.0
    income_tribute:      float = 0.0
    expense_wages:       float = 0.0
    expense_food:        float = 0.0
    expense_loot:        float = 0.0
    expense_recruiting:  float = 0.0

    events: List[str] = field(default_factory=list)

    @property
    def size(self):
        return self.commons + self.veterans + self.elites + self.named_men + self.casters

    @property
    def daily_wage(self):
        return (self.commons*WAGE["common"] + self.veterans*WAGE["veteran"]
                + self.elites*WAGE["elite"] + self.named_men*WAGE["named_man"]
                + self.casters*WAGE["caster_initiate"])

    @property
    def daily_retainer(self):
        return (self.commons*RETAINER_WEEKLY["common"]
                + self.veterans*RETAINER_WEEKLY["veteran"]
                + self.named_men*RETAINER_WEEKLY["named_man"]
                + self.casters*RETAINER_WEEKLY["caster_initiate"]) / 7

    @property
    def is_alive(self):
        return self.size >= 3 and self.morale >= MORALE_MIN and self.treasury > -50

    def forage(self, terrain, rng, fraction=0.30):
        if terrain == "settlement":
            return 0.0
        n = max(1, int(self.size * fraction))
        rates = FORAGE_TABLE.get(terrain, FORAGE_TABLE["plains"])
        food = rates[0] if n<=2 else rates[1] if n<=5 else rates[2] if n<=10 else rates[3]
        return min(self.size * FOOD_PER_MAN_DAY, food * rng.uniform(0.8, 1.2))

    def pay_daily_v1(self, terrain, rng):
        wages = self.daily_wage
        foraged = self.forage(terrain, rng, 0.30)
        food_cost = max(0.0, self.size*FOOD_PER_MAN_DAY - foraged) * FOOD_PRICE
        total = wages + food_cost
        if self.treasury >= total:
            self.treasury -= total
            self.days_unpaid = 0
        else:
            self.treasury -= max(0.0, self.treasury)
            self.days_unpaid += 1
        self.expense_wages += wages
        self.expense_food  += food_cost

    def pay_daily_v2(self, terrain, rng):
        wages = self.daily_wage if self.on_mission else self.daily_retainer
        forage_frac = 0.30 if self.on_mission else 0.70
        foraged = self.forage(terrain, rng, forage_frac)
        food_cost = max(0.0, self.size*FOOD_PER_MAN_DAY - foraged) * FOOD_PRICE
        total = wages + food_cost
        if self.treasury >= total:
            self.treasury -= total
            self.days_unpaid = 0
        else:
            self.treasury -= max(0.0, self.treasury)
            self.days_unpaid += 1
        self.expense_wages += wages
        self.expense_food  += food_cost

    def pay_daily_v5(self, terrain, rng):
        wages = self.daily_wage * MISSION_PAY_FRACTION if self.on_mission else self.daily_retainer
        forage_frac = 0.30 if self.on_mission else 0.70
        foraged = self.forage(terrain, rng, forage_frac)
        food_cost = max(0.0, self.size*FOOD_PER_MAN_DAY - foraged) * FOOD_PRICE
        total = wages + food_cost
        if self.treasury >= total:
            self.treasury -= total
            self.days_unpaid = 0
        else:
            self.treasury -= max(0.0, self.treasury)
            self.days_unpaid += 1
        self.expense_wages += wages
        self.expense_food  += food_cost

    def split_loot_v2(self, loot_pool, rng):
        if loot_pool <= 0:
            return
        men_total = loot_pool * V2_LOOT_MEN_SHARE
        if self.treasury >= men_total:
            self.treasury    -= men_total
            self.expense_loot += men_total
            if rng.random() < 0.35:
                self.morale = min(MORALE_MAX, self.morale + 1)
        else:
            self.morale = max(MORALE_MIN, self.morale - 1)
            self.events.append(f"day {self.day}: loot share owed, treasury empty")

    def check_morale_payment(self, rng, model="v1"):
        if model in ("v2", "v3", "v5", "v6"):
            threshold = NP_THRESHOLD_V2_MISSION if self.on_mission else NP_THRESHOLD_V2_RETAINER
            diff_plus = 1 if self.on_mission else 0
        else:
            threshold, diff_plus = NP_THRESHOLD_V1, 0
        if self.days_unpaid < threshold:
            return
        result = non_payment_roll(rng, diff_plus)
        if result == "desert_d3":
            lost = min(rng.randint(1,3), self.commons)
            self.commons -= lost
            self.morale = max(MORALE_MIN, self.morale - 1)
            self.events.append(f"day {self.day}: {lost} deserted")
        elif result in ("morale_hit", "confrontation"):
            self.morale = max(MORALE_MIN, self.morale - 1)
        elif result == "remembered":
            self.days_unpaid += 5

    def apply_combat(self, hard, rng):
        rate = CASUALTY_RATE_HARD if hard else CASUALTY_RATE_NORMAL
        if self.casters > 0:
            rate *= (1 - CASTER_CASUALTY_REDUCTION)
        roster = (["common"]*self.commons + ["veteran"]*self.veterans
                  + ["elite"]*self.elites + ["named_man"]*self.named_men)
        casualties = 0
        for m in roster:
            if rng.random() < rate:
                casualties += 1
                if m=="common" and self.commons>0:    self.commons -= 1
                elif m=="veteran" and self.veterans>0: self.veterans -= 1
                elif m=="elite" and self.elites>0:     self.elites -= 1
                elif m=="named_man" and self.named_men>0: self.named_men -= 1
        if casualties == 0:
            self.morale = min(MORALE_MAX, self.morale + 1)
        else:
            self.events.append(f"day {self.day}: {casualties} cas ({'hard' if hard else 'norm'})")

    def recruit_replacement(self, rng):
        if self.size < 8 and self.treasury > 50:
            cost = rng.uniform(3, 8)
            self.treasury -= cost
            self.expense_recruiting += cost
            self.commons += 1


# ─── SIMULATION ENGINE ───────────────────────────────────────────────────────

def _run_band(band, rng, world, model="v1", contracts=None, bounties=None):
    th, mh, sh = [], [], []
    on_contract_days = travel_days = idle_days = 0
    last_season_bonus = -1
    collapse_day = None

    for day in range(SIM_DAYS):
        band.day = day
        if day % 7 == 0:
            refresh_contracts(world, rng, contracts, bounties)

        band.pos = (max(0, min(WORLD_SIZE-1, band.pos[0])),

                    max(0, min(WORLD_SIZE-1, band.pos[1])))
        cur     = world[band.pos]
        terrain = cur.terrain

        if model in ("v2", "v3"):
            band.pay_daily_v2(terrain, rng)
        elif model in ("v5", "v6"):
            band.pay_daily_v5(terrain, rng)
        else:
            band.pay_daily_v1(terrain, rng)

        # Seasonal pay morale bonus
        season = day // 91
        if season != last_season_bonus and band.days_unpaid == 0:
            band.morale = min(MORALE_MAX, band.morale + 1)
            last_season_bonus = season

        if day % 7 == 0:
            band.check_morale_payment(rng, model)

        # V2/V3/V5/V6: prolonged-idle morale drain; garrison contracts reset the counter
        if model in ("v2", "v3", "v5", "v6"):
            if band.on_mission or band.current_contract is not None:
                band.days_since_contract = 0
            else:
                band.days_since_contract += 1
                if band.days_since_contract > 0 and band.days_since_contract % 28 == 0:
                    band.morale = max(MORALE_MIN, band.morale - 1)

        # Active contract
        if band.current_contract is not None:
            band.contract_day += 1
            on_contract_days  += 1
            ct = band.current_contract
            if rng.random() < FIGHT_CHANCE_PER_CONTRACT / ct["duration"]:
                band.apply_combat(ct.get("hard", False), rng)

            if band.contract_day >= ct["duration"]:
                pay = ct["pay"]
                band.treasury        += pay
                band.income_contracts += pay
                if model in ("v2", "v3", "v5", "v6"):
                    band.split_loot_v2(pay * V2_BATTLE_PRIZE_PCT, rng)

                if cur.bounty_available and rng.random() < 0.35:
                    bp = cur.bounty_available["pay"]
                    band.treasury       += bp
                    band.income_bounties += bp
                    if model in ("v2", "v3", "v5", "v6"):
                        band.split_loot_v2(bp, rng)
                    cur.bounty_available = None

                cur.contract_available = None
                cur.contract_cooldown  = rng.randint(14, 35)
                band.current_contract  = None
                band.contract_day      = 0
                if model in ("v2", "v3", "v5", "v6"):
                    band.on_mission = False

        elif (cur.contract_available is not None
              and cur.feud_track < 3
              and band.morale >= 2):
            ct = cur.contract_available
            # Skip caster-only contracts if band has no caster
            if ct.get("requires_caster") and band.casters == 0:
                cur.contract_available = None
                cur.contract_cooldown  = rng.randint(3, 7)
            else:
                # V3/V5/V6: bands with a caster negotiate premium on standard field deployments
                if model in ("v3", "v5", "v6") and band.casters > 0 and not ct.get("garrison") and not ct.get("requires_caster"):
                    ct = dict(ct)
                    ct["pay"] = round(ct["pay"] * (1 + CASTER_CONTRACT_PREMIUM), 1)
                # V6: captain haggles — roll HAGGLE_DICE d6, 1+ success (6) → −20% pricing
                if model == "v6":
                    ct = dict(ct)
                    dice = [rng.randint(1, 6) for _ in range(HAGGLE_DICE)]
                    if any(d == 6 for d in dice):
                        ct["pay"] = round(ct["pay"] * HAGGLE_BONUS_MULT, 1)
                # Garrison contracts: accepted on retainer-cost basis, not mission-wage basis
                if ct.get("garrison"):
                    exp_cost = band.daily_retainer * ct["duration"] * 1.1
                elif model in ("v5", "v6"):
                    exp_cost = band.daily_wage * MISSION_PAY_FRACTION * ct["duration"] * 1.1
                else:
                    exp_cost = band.daily_wage * ct["duration"] * 1.1
                if ct["pay"] >= exp_cost * 0.75 or band.treasury < band.daily_wage * 7:
                    band.current_contract = ct
                    band.contract_day     = 0
                    if model in ("v2", "v3", "v5", "v6") and not ct.get("garrison"):
                        band.on_mission = True

        else:
            target = nearest_employer(band.pos, world)
            if target is None:
                if (band.treasury < band.daily_wage * 5
                        and cur.settlement in (SettlementTier.VILLAGE, SettlementTier.TOWN)
                        and cur.tribute_drained < 3
                        and cur.feud_track < 3):
                    tbl = TRIBUTE_VILLAGE if cur.settlement == SettlementTier.VILLAGE else TRIBUTE_TOWN
                    roll = rng.choice(tbl)
                    tribute = rng.uniform(roll[0], roll[1]) if roll[1] > roll[0] else roll[0]
                    band.treasury       += tribute
                    band.income_tribute += tribute
                    if model == "v2":
                        band.split_loot_v2(tribute, rng)
                    cur.tribute_drained += 1
                    cur.feud_track = min(4, cur.feud_track + 1)
                else:
                    idle_days += 1
            else:
                if band.pos != target:
                    band.pos = step_toward(band.pos, target)
                    travel_days += 1
                    band.pos = (max(0, min(WORLD_SIZE-1, band.pos[0])),
                                max(0, min(WORLD_SIZE-1, band.pos[1])))
                    cur = world[band.pos]

        if day % 14 == 0 and cur.settlement != SettlementTier.NONE:
            band.recruit_replacement(rng)

        th.append(band.treasury)
        mh.append(band.morale)
        sh.append(band.size)

        if not band.is_alive and collapse_day is None:
            collapse_day = day
            break

    ti = band.income_contracts + band.income_bounties + band.income_tribute
    te = band.expense_wages + band.expense_food + band.expense_loot + band.expense_recruiting
    return {
        "model":             model,
        "survived":          collapse_day is None,
        "collapse_day":      collapse_day,
        "final_treasury":    band.treasury,
        "min_treasury":      min(th) if th else 0,
        "max_treasury":      max(th) if th else 0,
        "income_contracts":  band.income_contracts,
        "income_bounties":   band.income_bounties,
        "income_tribute":    band.income_tribute,
        "total_income":      ti,
        "expense_wages":     band.expense_wages,
        "expense_food":      band.expense_food,
        "expense_loot":      band.expense_loot,
        "expense_recruiting":band.expense_recruiting,
        "total_expense":     te,
        "net_margin":        (ti - te) / max(1, ti),
        "on_contract_days":  on_contract_days,
        "travel_days":       travel_days,
        "idle_days":         idle_days,
        "final_size":        band.size,
        "final_morale":      band.morale,
        "_th": th,
    }


def run_all(model, seed_offset, commons=6, veterans=2, named_men=1, casters=0,
            contracts=None, bounties=None):
    results = []
    for i in range(RUNS):
        rng   = random.Random(SEED_BASE + seed_offset + i)
        world = build_world(rng)
        band  = Band(commons=commons, veterans=veterans,
                     named_men=named_men, casters=casters)
        results.append(_run_band(band, rng, world, model, contracts, bounties))
    return results


# ─── STATS ───────────────────────────────────────────────────────────────────

def pct(vals, p):
    sv = sorted(vals)
    return sv[min(int(len(sv)*p/100), len(sv)-1)]


def summarise(results, label):
    def m(k): return statistics.mean([r[k] for r in results])
    fin  = [r["final_treasury"] for r in results]
    mn   = [r["min_treasury"]   for r in results]
    surv = sum(1 for r in results if r["survived"])
    coll = [r["collapse_day"] for r in results if not r["survived"]]
    ocd  = [r["on_contract_days"] for r in results]
    return {
        "label":             label,
        "n":                 len(results),
        "model":             results[0]["model"],
        "survival_rate":     surv / len(results),
        "median_treas":      statistics.median(fin),
        "p10_treas":         pct(fin, 10),
        "p90_treas":         pct(fin, 90),
        "median_min_treas":  statistics.median(mn),
        "pct_broke":         sum(v < 0 for v in fin) / len(results),
        "m_inc_contracts":   m("income_contracts"),
        "m_inc_bounties":    m("income_bounties"),
        "m_inc_tribute":     m("income_tribute"),
        "m_total_inc":       m("total_income"),
        "m_exp_wages":       m("expense_wages"),
        "m_exp_food":        m("expense_food"),
        "m_exp_loot":        m("expense_loot"),
        "m_total_exp":       m("total_expense"),
        "m_net_margin":      (m("total_income") - m("total_expense")) / max(1, m("total_income")),
        "m_contract_days":   m("on_contract_days"),
        "m_travel_days":     m("travel_days"),
        "m_idle_days":       m("idle_days"),
        "mean_collapse_day": statistics.mean(coll) if coll else None,
        "contract_pct":      m("on_contract_days") / SIM_DAYS,
        "travel_pct":        m("travel_days")       / SIM_DAYS,
        "idle_pct":          m("idle_days")         / SIM_DAYS,
    }


# ─── JSON SAVE ────────────────────────────────────────────────────────────────

def save_results(results, summary, tag):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    compact = [{k: v for k, v in r.items() if not k.startswith("_")} for r in results]
    payload = {"tag": tag, "timestamp": ts, "runs": RUNS, "days": SIM_DAYS,
               "summary": summary, "raw": compact}
    for fname in (f"{RESULTS_DIR}/{tag}_{ts}.json",
                  f"{RESULTS_DIR}/{tag}_latest.json"):
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, default=str)
    return f"{RESULTS_DIR}/{tag}_latest.json"


# ─── REPORTING ────────────────────────────────────────────────────────────────

SEP  = "─" * 72
SEP2 = "═" * 72


def print_variant(s):
    inc = s["m_total_inc"]
    exp = s["m_total_exp"]
    print(f"\n  ▶ {s['label']}  [{s['model'].upper()}]")
    print(SEP)
    print(f"  Survival:   {s['survival_rate']*100:5.1f}%  "
          + (f"  (mean collapse day {s['mean_collapse_day']:.0f})" if s["mean_collapse_day"] else ""))
    print(f"  Treasury:   median {s['median_treas']:7.1f}s  "
          f"P10 {s['p10_treas']:7.1f}s  P90 {s['p90_treas']:7.1f}s")
    print(f"  Income:     contracts {s['m_inc_contracts']:7.1f}s  "
          f"bounties {s['m_inc_bounties']:6.1f}s  tribute {s['m_inc_tribute']:5.1f}s  "
          f"= {inc:7.1f}s")
    print(f"  Expenses:   wages {s['m_exp_wages']:7.1f}s  food {s['m_exp_food']:6.1f}s"
          + (f"  loot {s['m_exp_loot']:5.1f}s" if s["m_exp_loot"] > 0.5 else "")
          + f"  = {exp:7.1f}s")
    print(f"  Net margin: {s['m_net_margin']*100:+.1f}%  ({inc-exp:+.1f}s/year)")
    print(f"  Time:       contract {s['contract_pct']*100:.1f}%  "
          f"travel {s['travel_pct']*100:.1f}%  idle {s['idle_pct']*100:.1f}%")


def print_comparison(v1s, v2s, v3s=None, v5s=None, v6s=None):
    daily_wage_base = 6*WAGE["common"] + 2*WAGE["veteran"] + 1*WAGE["named_man"]
    retainer_base   = (6*RETAINER_WEEKLY["common"] + 2*RETAINER_WEEKLY["veteran"]
                       + 1*RETAINER_WEEKLY["named_man"]) / 7
    mission_v5      = daily_wage_base * MISSION_PAY_FRACTION
    print(f"\n{SEP2}")
    print("  V1 / V2 / V3 / V5 / V6 COMPARISON")
    print(SEP2)
    print(f"\n  {'Variant':<36} {'Model':<14} {'Survives':<10} {'Margin':>8} "
          f"{'OnContract':>12} {'TreasuryP50':>12}")
    print("  " + "─"*96)
    quints = zip(v1s, v2s,
                 v3s if v3s else [None]*len(v1s),
                 v5s if v5s else [None]*len(v1s),
                 v6s if v6s else [None]*len(v1s))
    for v1, v2, v3, v5, v6 in quints:
        name = v1["label"].split("(")[0].strip()[:35]
        rows = [(v1, "DAILY"), (v2, "RETAINER")]
        if v3: rows.append((v3, "RETAINER+V3"))
        if v5: rows.append((v5, "RETAINER+V5"))
        if v6: rows.append((v6, "RETAINER+V6"))
        for s, tag in rows:
            print(f"  {name:<36} {tag:<14} {s['survival_rate']*100:5.1f}%     "
                  f"{s['m_net_margin']*100:+6.1f}%  "
                  f"{s['m_contract_days']:4.0f}d ({s['contract_pct']*100:4.1f}%)  "
                  f"{s['median_treas']:>10.0f}s")
        print("  " + "─"*96)

    print(f"\n  Dead-time burn:   V1 {daily_wage_base:.1f}s/day (full wages) | V2/V3/V5/V6 retainer {retainer_base:.2f}s/day")
    print(f"  Mission pay rate: V1/V2/V3 {daily_wage_base:.1f}s/day | V5/V6 {mission_v5:.2f}s/day (half rate)")
    print(f"  Contract floor:   V3/V5 at {daily_wage_base:.0f}s/day baseline | V6 at −30% (−20% haggled)")
    print(f"  Runway on 100s:   V1 ~{100/daily_wage_base:.0f}d | V2/V3/V5/V6 ~{100/retainer_base:.0f}d")


def print_problems(v1, v2, v3=None, v5=None, v6=None):
    daily_v1   = 6*WAGE["common"] + 2*WAGE["veteran"] + 1*WAGE["named_man"]
    retainer   = (6*RETAINER_WEEKLY["common"] + 2*RETAINER_WEEKLY["veteran"]
                  + 1*RETAINER_WEEKLY["named_man"]) / 7
    mission_v5 = daily_v1 * MISSION_PAY_FRACTION
    dead_v1    = (v1["m_travel_days"] + v1["m_idle_days"]) * daily_v1
    dead_v2    = (v2["m_travel_days"] + v2["m_idle_days"]) * retainer

    print(f"\n{SEP2}")
    print("  DESIGN PROBLEMS AND STATUS")
    print(SEP2)
    print(f"""
  MODEL SCORECARD (standard 9-man warband):
    V1 daily wages:         survival {v1['survival_rate']*100:.1f}%  margin {v1['m_net_margin']*100:+.1f}%  treasury {v1['median_treas']:.0f}s median
    V2 retainer model:      survival {v2['survival_rate']*100:.1f}%  margin {v2['m_net_margin']*100:+.1f}%  treasury {v2['median_treas']:.0f}s median""")
    if v3:
        print(f"    V3 repriced+casters:    survival {v3['survival_rate']*100:.1f}%  margin {v3['m_net_margin']*100:+.1f}%  treasury {v3['median_treas']:.0f}s median")
    if v5:
        print(f"    V5 half mission pay:    survival {v5['survival_rate']*100:.1f}%  margin {v5['m_net_margin']*100:+.1f}%  treasury {v5['median_treas']:.0f}s median")
    if v6:
        print(f"    V6 struggling world:    survival {v6['survival_rate']*100:.1f}%  margin {v6['m_net_margin']*100:+.1f}%  treasury {v6['median_treas']:.0f}s median")
    print(f"""
  V2 FIXED:
    ✓ Dead-time runway: ~{100/daily_v1:.0f}d → ~{100/retainer:.0f}d
    ✓ Dead-time cost:   {dead_v1:.0f}s → {dead_v2:.0f}s/year  (−{dead_v1-dead_v2:.0f}s)
    ✓ Loot shares paid to men: {v2['m_exp_loot']:.0f}s/year  (loyalty loop)
    ✓ Dead-week decisions matter: terrain, foraging, tribute all real""")
    if v3:
        prot_avg  = (550 + 800) / 2
        prot_cost = retainer * 91 + 91 * FOOD_PRICE
        v3_daily_ct = v3["m_inc_contracts"] / max(1, v3["m_contract_days"])
        print(f"""
  V3 FIXED:
    ✓ Contract floor: {daily_v1:.0f}s/day × duration × 1.25  (patrol 7d → {int(daily_v1*7*1.25)}s min)
    ✓ Protection season pays {int(prot_avg):.0f}s vs ~{prot_cost:.0f}s cost → net +{int(prot_avg-prot_cost):.0f}s
    ✓ Casters reduce casualty rate by {CASTER_CASUALTY_REDUCTION*100:.0f}% across all engagements
    ✓ Caster bands negotiate +{CASTER_CONTRACT_PREMIUM*100:.0f}% on standard contracts
    ✓ Caster-specific contracts exist (magical commission, ritual ward)
    ✓ Bounties repriced: ~2× V1/V2 rates (systematic, not anecdotal)

  V3 RESIDUAL:
    Contract income/day on mission: {v3_daily_ct:.1f}s vs {daily_v1:.1f}s cost ({v3_daily_ct/daily_v1*100:.0f}% coverage)
    Net margin: {v3['m_net_margin']*100:+.1f}%  ({v3['m_total_inc']-v3['m_total_exp']:+.0f}s/year)
    Adept caster wages ({WAGE['caster_adept']*365:.0f}s/year) still need explicit magic-contract pipeline
    Bands with strong loot luck and garrison access can reach profitability""")
    if v5 and v3:
        v5_daily_ct = v5["m_inc_contracts"] / max(1, v5["m_contract_days"])
        dead_v5     = (v5["m_travel_days"] + v5["m_idle_days"]) * retainer
        print(f"""
  V5 CHANGES (half mission pay, retainer during travel):
    Mission pay: {daily_v1:.0f}s/day × 50% = {mission_v5:.1f}s/day (active work only — not travel)
    Travel to site stays on retainer ({retainer:.2f}s/day)

  V5 RESULT:
    Contract income/day: {v5_daily_ct:.1f}s  | mission pay cost/day: {mission_v5:.1f}s  | gross/day on mission: +{v5_daily_ct-mission_v5:.1f}s
    Net margin: {v5['m_net_margin']*100:+.1f}%  ({v5['m_total_inc']-v5['m_total_exp']:+.0f}s/year)
    Wage expenditure: {v5['m_exp_wages']:.0f}s vs V3 {v3['m_exp_wages']:.0f}s (−{v3['m_exp_wages']-v5['m_exp_wages']:.0f}s)""")
    if v6 and v5:
        v6_daily_ct  = v6["m_inc_contracts"] / max(1, v6["m_contract_days"])
        haggle_pct   = round(1 - (1/6)**HAGGLE_DICE, 3) * 100
        floor_30     = CONTRACT_TYPES_V6[0][1]   # patrol_week min as proxy
        print(f"""
  V6 CHANGES (struggling world — −30% contract floor + haggling):
    Contract base: −30% off V3 rates ({floor_30}s min for patrol week)
    Haggle roll:   {HAGGLE_DICE}d6, 1+ success (6) → −20% pricing (~{haggle_pct:.0f}% of contracts)
    Mission pay:   same as V5 (half rate, active work only)

  V6 RESULT:
    Contract income/day: {v6_daily_ct:.1f}s  | mission pay cost/day: {mission_v5:.1f}s  | gross/day on mission: +{v6_daily_ct-mission_v5:.1f}s
    Net margin: {v6['m_net_margin']*100:+.1f}%  ({v6['m_total_inc']-v6['m_total_exp']:+.0f}s/year)
    Wage expenditure: {v6['m_exp_wages']:.0f}s vs V5 {v5['m_exp_wages']:.0f}s | contract income: {v6['m_inc_contracts']:.0f}s vs V5 {v5['m_inc_contracts']:.0f}s""")
    elif not v3:
        print(f"""
  V3 NOT YET RUN — contract pricing gap remains:
    ✗ Rate covers ~{v2['m_inc_contracts']/max(1,v2['m_contract_days'])*100/daily_v1:.0f}% of mission wages
    ✗ Protection contracts (~95s/season) cover ~{95/(daily_v1*91)*100:.0f}% of wages""")


def print_treasury_chart(results, label):
    print(f"\n  TREASURY — {label}")
    print(f"  {'Day':>4}  {'Mean':>7}  {'P10':>7}  {'P90':>7}  Bar (÷10s)")
    print("  " + "─"*52)
    for d in range(0, SIM_DAYS+1, 25):
        vals = [r["_th"][d] for r in results if d < len(r["_th"])]
        if not vals: continue
        m = statistics.mean(vals)
        bar = "█" * max(0, int(m/10))
        sign = "▼" if m < 0 else ""
        print(f"  {d:>4}  {m:>7.1f}  {pct(vals,10):>7.1f}  {pct(vals,90):>7.1f}  {bar}{sign}")


# ─── MAIN ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"\nRunning {RUNS}×{SIM_DAYS}d — V1 / V2 / V3 models...\n")

    v1_base   = run_all("v1", 0);     print("  V1 base done")
    v1_small  = run_all("v1", 1000, commons=4, veterans=1, named_men=0); print("  V1 small done")
    v1_caster = run_all("v1", 2000, casters=1); print("  V1 caster done")
    v2_base   = run_all("v2", 3000);  print("  V2 base done")
    v2_small  = run_all("v2", 4000, commons=4, veterans=1, named_men=0); print("  V2 small done")
    v2_caster = run_all("v2", 5000, casters=1); print("  V2 caster done")
    v3_base   = run_all("v3", 6000, contracts=CONTRACT_TYPES_V3, bounties=BOUNTY_TABLE_V3)
    print("  V3 base done")
    v3_small  = run_all("v3", 7000, commons=4, veterans=1, named_men=0,
                        contracts=CONTRACT_TYPES_V3, bounties=BOUNTY_TABLE_V3)
    print("  V3 small done")
    v3_caster = run_all("v3", 8000, casters=1,
                        contracts=CONTRACT_TYPES_V3, bounties=BOUNTY_TABLE_V3)
    print("  V3 caster done")
    v5_base   = run_all("v5", 9000,  contracts=CONTRACT_TYPES_V3, bounties=BOUNTY_TABLE_V3)
    print("  V5 base done")
    v5_small  = run_all("v5", 10000, commons=4, veterans=1, named_men=0,
                        contracts=CONTRACT_TYPES_V3, bounties=BOUNTY_TABLE_V3)
    print("  V5 small done")
    v5_caster = run_all("v5", 11000, casters=1,
                        contracts=CONTRACT_TYPES_V3, bounties=BOUNTY_TABLE_V3)
    print("  V5 caster done")
    v6_base   = run_all("v6", 12000, contracts=CONTRACT_TYPES_V6, bounties=BOUNTY_TABLE_V3)
    print("  V6 base done")
    v6_small  = run_all("v6", 13000, commons=4, veterans=1, named_men=0,
                        contracts=CONTRACT_TYPES_V6, bounties=BOUNTY_TABLE_V3)
    print("  V6 small done")
    v6_caster = run_all("v6", 14000, casters=1,
                        contracts=CONTRACT_TYPES_V6, bounties=BOUNTY_TABLE_V3)
    print("  V6 caster done\n")

    sv1b = summarise(v1_base,   "Standard Warband  (6c+2v+1nm)")
    sv1s = summarise(v1_small,  "Small Band        (4c+1v)")
    sv1c = summarise(v1_caster, "Warband+Caster    (6c+2v+1nm+1ca)")
    sv2b = summarise(v2_base,   "Standard Warband  (6c+2v+1nm)")
    sv2s = summarise(v2_small,  "Small Band        (4c+1v)")
    sv2c = summarise(v2_caster, "Warband+Caster    (6c+2v+1nm+1ca)")
    sv3b = summarise(v3_base,   "Standard Warband  (6c+2v+1nm)")
    sv3s = summarise(v3_small,  "Small Band        (4c+1v)")
    sv3c = summarise(v3_caster, "Warband+Caster    (6c+2v+1nm+1ca)")
    sv5b = summarise(v5_base,   "Standard Warband  (6c+2v+1nm)")
    sv5s = summarise(v5_small,  "Small Band        (4c+1v)")
    sv5c = summarise(v5_caster, "Warband+Caster    (6c+2v+1nm+1ca)")
    sv6b = summarise(v6_base,   "Standard Warband  (6c+2v+1nm)")
    sv6s = summarise(v6_small,  "Small Band        (4c+1v)")
    sv6c = summarise(v6_caster, "Warband+Caster    (6c+2v+1nm+1ca)")

    paths = {
        "v1_baseline": save_results(v1_base,   sv1b, "v1_baseline"),
        "v1_small":    save_results(v1_small,  sv1s, "v1_small"),
        "v1_caster":   save_results(v1_caster, sv1c, "v1_caster"),
        "v2_baseline": save_results(v2_base,   sv2b, "v2_baseline"),
        "v2_small":    save_results(v2_small,  sv2s, "v2_small"),
        "v2_caster":   save_results(v2_caster, sv2c, "v2_caster"),
        "v3_baseline": save_results(v3_base,   sv3b, "v3_baseline"),
        "v3_small":    save_results(v3_small,  sv3s, "v3_small"),
        "v3_caster":   save_results(v3_caster, sv3c, "v3_caster"),
        "v5_baseline": save_results(v5_base,   sv5b, "v5_baseline"),
        "v5_small":    save_results(v5_small,  sv5s, "v5_small"),
        "v5_caster":   save_results(v5_caster, sv5c, "v5_caster"),
        "v6_baseline": save_results(v6_base,   sv6b, "v6_baseline"),
        "v6_small":    save_results(v6_small,  sv6s, "v6_small"),
        "v6_caster":   save_results(v6_caster, sv6c, "v6_caster"),
    }

    print(SEP2)
    print("  FL2E MERCENARY ECONOMY SIM")
    print(f"  V1 daily  |  V2 retainer  |  V3 retainer+repriced+caster  |  V5 half mission pay  |  V6 struggling world")
    print(f"  {RUNS} runs × {SIM_DAYS} days | Start: 100s treasury")
    print(SEP2)

    print("\n  ── V1: DAILY WAGES ──")
    for s in (sv1b, sv1s, sv1c): print_variant(s)

    print("\n\n  ── V2: RETAINER MODEL ──")
    for s in (sv2b, sv2s, sv2c): print_variant(s)

    print("\n\n  ── V3: RETAINER + REPRICED CONTRACTS + CASTER UTILITY ──")
    for s in (sv3b, sv3s, sv3c): print_variant(s)

    print("\n\n  ── V5: RETAINER + REPRICED + HALF MISSION PAY ──")
    for s in (sv5b, sv5s, sv5c): print_variant(s)

    print("\n\n  ── V6: STRUGGLING WORLD (−30% CONTRACTS + HAGGLING + HALF MISSION PAY) ──")
    for s in (sv6b, sv6s, sv6c): print_variant(s)

    print_comparison([sv1b, sv1s, sv1c], [sv2b, sv2s, sv2c], [sv3b, sv3s, sv3c], [sv5b, sv5s, sv5c], [sv6b, sv6s, sv6c])
    print_problems(sv1b, sv2b, sv3b, sv5b, sv6b)

    print_treasury_chart(v1_base, "V1 Standard Warband")
    print_treasury_chart(v2_base, "V2 Standard Warband (Retainer)")
    print_treasury_chart(v3_base, "V3 Standard Warband (Retainer+Repriced)")
    print_treasury_chart(v5_base, "V5 Standard Warband (Half Mission Pay)")
    print_treasury_chart(v6_base, "V6 Standard Warband (Struggling World)")

    print(f"\n{SEP2}")
    print("  RESULTS SAVED:")
    for k, p in paths.items():
        print(f"    {k:<14}  {p}")
    print()
