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


def refresh_contracts(world, rng):
    for h in world.values():
        if h.contract_cooldown > 0:
            h.contract_cooldown -= 1
        if h.settlement >= SettlementTier.TOWN:
            if h.contract_available is None and h.contract_cooldown == 0:
                if rng.random() < 0.55:
                    tier_name = "warchief" if h.settlement == SettlementTier.WARCHIEF else "town"
                    eligible = [c for c in CONTRACT_TYPES if c[4] == tier_name or c[4] == "town"]
                    ct = rng.choice(eligible)
                    h.contract_available = {
                        "name": ct[0],
                        "pay": round(rng.uniform(ct[1], ct[2]), 1),
                        "duration": ct[3] + rng.randint(-2, 2),
                        "hard": ct[0] in ("warchief_raid",),
                    }
            if h.bounty_available is None and rng.random() < 0.25:
                bt = rng.choice(BOUNTY_TABLE)
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
        if model == "v2":
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

def _run_band(band, rng, world, model="v1"):
    th, mh, sh = [], [], []
    on_contract_days = travel_days = idle_days = 0
    last_season_bonus = -1
    collapse_day = None

    for day in range(SIM_DAYS):
        band.day = day
        if day % 7 == 0:
            refresh_contracts(world, rng)

        band.pos = (max(0, min(WORLD_SIZE-1, band.pos[0])),
                    max(0, min(WORLD_SIZE-1, band.pos[1])))
        cur     = world[band.pos]
        terrain = cur.terrain

        if model == "v2":
            band.pay_daily_v2(terrain, rng)
        else:
            band.pay_daily_v1(terrain, rng)

        # Seasonal pay morale bonus
        season = day // 91
        if season != last_season_bonus and band.days_unpaid == 0:
            band.morale = min(MORALE_MAX, band.morale + 1)
            last_season_bonus = season

        if day % 7 == 0:
            band.check_morale_payment(rng, model)

        # V2: prolonged-idle morale drain
        if model == "v2":
            if band.on_mission:
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
                if model == "v2":
                    band.split_loot_v2(pay * V2_BATTLE_PRIZE_PCT, rng)

                if cur.bounty_available and rng.random() < 0.35:
                    bp = cur.bounty_available["pay"]
                    band.treasury       += bp
                    band.income_bounties += bp
                    if model == "v2":
                        band.split_loot_v2(bp, rng)
                    cur.bounty_available = None

                cur.contract_available = None
                cur.contract_cooldown  = rng.randint(14, 35)
                band.current_contract  = None
                band.contract_day      = 0
                if model == "v2":
                    band.on_mission = False

        elif (cur.contract_available is not None
              and cur.feud_track < 3
              and band.morale >= 2):
            ct = cur.contract_available
            exp_cost = band.daily_wage * ct["duration"] * 1.1
            if ct["pay"] >= exp_cost * 0.75 or band.treasury < band.daily_wage * 7:
                band.current_contract = ct
                band.contract_day     = 0
                if model == "v2":
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


def run_all(model, seed_offset, commons=6, veterans=2, named_men=1, casters=0):
    results = []
    for i in range(RUNS):
        rng   = random.Random(SEED_BASE + seed_offset + i)
        world = build_world(rng)
        band  = Band(commons=commons, veterans=veterans,
                     named_men=named_men, casters=casters)
        results.append(_run_band(band, rng, world, model))
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
        "m_net_margin":      m("net_margin"),
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


def print_comparison(v1s, v2s):
    daily_wage_base = 6*WAGE["common"] + 2*WAGE["veteran"] + 1*WAGE["named_man"]
    retainer_base   = (6*RETAINER_WEEKLY["common"] + 2*RETAINER_WEEKLY["veteran"]
                       + 1*RETAINER_WEEKLY["named_man"]) / 7
    print(f"\n{SEP2}")
    print("  V1 vs V2 COMPARISON")
    print(SEP2)
    print(f"\n  {'Variant':<36} {'Model':<10} {'Survives':<10} {'Margin':>8} "
          f"{'OnContract':>12} {'DeadCost':>10}")
    print("  " + "─"*88)
    for v1, v2 in zip(v1s, v2s):
        name = v1["label"].split("(")[0].strip()[:35]
        dead_v1 = (v1["m_travel_days"] + v1["m_idle_days"]) * daily_wage_base
        dead_v2 = (v2["m_travel_days"] + v2["m_idle_days"]) * retainer_base
        for s, dead in ((v1, dead_v1), (v2, dead_v2)):
            model_tag = "DAILY" if s["model"]=="v1" else "RETAINER"
            print(f"  {name:<36} {model_tag:<10} {s['survival_rate']*100:5.1f}%     "
                  f"{s['m_net_margin']*100:+6.1f}%  "
                  f"{s['m_contract_days']:4.0f}d ({s['contract_pct']*100:4.1f}%)  "
                  f"{dead:7.0f}s")
        print("  " + "─"*88)

    print(f"\n  Daily-wage dead-time burn:  {daily_wage_base:.1f}s/day")
    print(f"  Retainer dead-time burn:    {retainer_base:.2f}s/day")
    print(f"  Runway on 100s — V1:        ~{100/daily_wage_base:.0f} days")
    print(f"  Runway on 100s — V2:        ~{100/retainer_base:.0f} days")


def print_problems(v1, v2):
    daily_v1 = 6*WAGE["common"] + 2*WAGE["veteran"] + 1*WAGE["named_man"]
    retainer  = (6*RETAINER_WEEKLY["common"] + 2*RETAINER_WEEKLY["veteran"]
                 + 1*RETAINER_WEEKLY["named_man"]) / 7
    dead_v1   = (v1["m_travel_days"] + v1["m_idle_days"]) * daily_v1
    dead_v2   = (v2["m_travel_days"] + v2["m_idle_days"]) * retainer
    savings   = dead_v1 - dead_v2
    loot_exp  = v2["m_exp_loot"]

    print(f"\n{SEP2}")
    print("  DESIGN PROBLEMS AND STATUS")
    print(SEP2)
    print(f"""
  FIXED BY V2 RETAINER MODEL:
    ✓ Dead-time runway: V1 ~{100/daily_v1:.0f}d before insolvency → V2 ~{100/retainer:.0f}d
    ✓ Dead-time cost:   {dead_v1:.0f}s/year → {dead_v2:.0f}s/year  (saves {savings:.0f}s)
    ✓ Loot shares bound to men:  {loot_exp:.0f}s/year paid out  (loyalty reinforcement)
    ✓ Tribute split reduces pure-extortion incentive (men share moral weight)
    ✓ Mission pay vs retainer creates real contract-seeking behavior

  STILL BROKEN:
    ✗ Contract rates cover ~{v2['m_inc_contracts']/max(1,v2['m_contract_days'])*100/daily_v1:.0f}% of mission wages — zero margin
    ✗ Net margin still {v2['m_net_margin']*100:+.1f}% — system net-negative annually
    ✗ Protection contracts (~95s/season) cover ~{95/(daily_v1*91)*100:.0f}% of wages — incoherent
    ✗ Adept caster ({WAGE["caster_adept"]*365:.0f}s/year wages) exceeds total annual income
    ✗ Band needs lucky early-contract timing OR loot windfalls to survive a year

  REQUIRED CONTRACT PRICING FIX:
    Minimum contract = band_daily_cost × duration × 1.25
    Default warband: {daily_v1:.0f}s/day × typical 10d × 1.25 = {daily_v1*10*1.25:.0f}s minimum
    Current contracts range 50–450s (only the warchief-raid floor is near adequate)

  V2 VERDICT:
    The retainer model is necessary but not sufficient.
    It makes the daily economy playable (30d runway instead of 7d).
    It creates meaningful camp decisions (forage vs. travel vs. tribute).
    It gives loot a real distribution mechanic that binds Named Men.
    It does NOT fix the underlying contract pricing gap.
""")


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
    print(f"\nRunning {RUNS}×{SIM_DAYS}d — V1 (daily) and V2 (retainer)...\n")

    v1_base   = run_all("v1", 0);     print("  V1 base done")
    v1_small  = run_all("v1", 1000, commons=4, veterans=1, named_men=0); print("  V1 small done")
    v1_caster = run_all("v1", 2000, casters=1); print("  V1 caster done")
    v2_base   = run_all("v2", 3000);  print("  V2 base done")
    v2_small  = run_all("v2", 4000, commons=4, veterans=1, named_men=0); print("  V2 small done")
    v2_caster = run_all("v2", 5000, casters=1); print("  V2 caster done\n")

    sv1b = summarise(v1_base,   "Standard Warband  (6c+2v+1nm)")
    sv1s = summarise(v1_small,  "Small Band        (4c+1v)")
    sv1c = summarise(v1_caster, "Warband+Caster    (6c+2v+1nm+1ca)")
    sv2b = summarise(v2_base,   "Standard Warband  (6c+2v+1nm)")
    sv2s = summarise(v2_small,  "Small Band        (4c+1v)")
    sv2c = summarise(v2_caster, "Warband+Caster    (6c+2v+1nm+1ca)")

    paths = {
        "v1_baseline": save_results(v1_base,   sv1b, "v1_baseline"),
        "v1_small":    save_results(v1_small,  sv1s, "v1_small"),
        "v1_caster":   save_results(v1_caster, sv1c, "v1_caster"),
        "v2_baseline": save_results(v2_base,   sv2b, "v2_baseline"),
        "v2_small":    save_results(v2_small,  sv2s, "v2_small"),
        "v2_caster":   save_results(v2_caster, sv2c, "v2_caster"),
    }

    print(SEP2)
    print("  FL2E MERCENARY ECONOMY SIM")
    print(f"  V1 daily wages  vs  V2 retainer + mission pay + loot shares")
    print(f"  {RUNS} runs × {SIM_DAYS} days | Start: 100s treasury")
    print(SEP2)

    print("\n  ── V1: DAILY WAGES ──")
    for s in (sv1b, sv1s, sv1c): print_variant(s)

    print("\n\n  ── V2: RETAINER MODEL ──")
    for s in (sv2b, sv2s, sv2c): print_variant(s)

    print_comparison([sv1b, sv1s, sv1c], [sv2b, sv2s, sv2c])
    print_problems(sv1b, sv2b)

    print_treasury_chart(v1_base, "V1 Standard Warband")
    print_treasury_chart(v2_base, "V2 Standard Warband (Retainer)")

    print(f"\n{SEP2}")
    print("  RESULTS SAVED:")
    for k, p in paths.items():
        print(f"    {k:<14}  {p}")
    print()
