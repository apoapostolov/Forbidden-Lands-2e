#!/usr/bin/env python3
"""
Mercenary Band Economy Simulator — Forbidden Lands 2E
Simulates 1 year (365 days) of operations.

Calibrated directly from proposal-mercenary-band-management.md:
  - Wages: Common 1s/day, Veteran 2s/day, Elite 3s/day
  - Food: 1 FOOD unit/man/day
  - Forager table: exact values from Section 4
  - Contract rewards: derived from settlement-tier economics in Section 5
  - Bounty floors: exact values from Section 5 bounty tables
  - Tribute: exact D6 tables from Section 4
  - Non-payment: D6 MORALE table from Section 3

Run with:  python3 scripts/band_economy_sim.py
"""

import random
import statistics
import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Tuple
from collections import defaultdict


# ─── CONFIGURATION ─────────────────────────────────────────────────────────

RUNS = 200           # Monte Carlo simulations
SIM_DAYS = 365       # Days per run
RANDOM_SEED = 42
WORLD_SIZE = 12      # 12x12 hex grid

# ─── WAGES (silver/day) — from proposal Section 2 unit table ───────────────

WAGE = {
    "common":   1,
    "veteran":  2,
    "elite":    3,
    "named_man": 3,      # sergeant tier — same as elite, distinct rules
    "caster_initiate": 6,     # midpoint of 5–8s/day
    "caster_adept":    15,    # midpoint of 12–18s/day
}

# ─── FOOD — Section 4 forager table, exact FOOD returns per column ─────────
# Columns: 1-2 foragers | 3-5 foragers | 6-10 foragers | 11+ foragers

FORAGE_TABLE = {
    "forest":     [3,  8, 16, 28],
    "dark_forest":[3,  8, 16, 28],
    "hills":      [2,  7, 13, 22],
    "plains":     [2,  5, 10, 18],
    "ruins":      [1,  3,  7, 12],
    "tundra":     [0,  2,  4,  8],
    "settlement": [0,  0,  0,  0],   # buy food in settlements; no foraging
}

FOOD_PURCHASE_PRICE = 0.15   # silver per FOOD unit (grain, rations)
FOOD_FORAGE_BRACKET = [2, 5, 10, 11]  # forager-count breakpoints (1-2, 3-5, 6-10, 11+)

# ─── CONTRACT REWARDS — derived from Section 5 employer tier economics ──────
# A warband of 10 costs ~80–105 silver/week all-in. Employer tiers:
#   Village:  surplus ~1D6 silver/week = too poor for contracts.
#   Town:     steady trade, garrison needs, 50–150 silver viable.
#   Warchief: campaigns, can pay 150–400+ silver for real work.

CONTRACT_TYPES = [
    # (name, min_pay, max_pay, duration_days, employer_tier_min)
    ("patrol_week",   50,  90,  7,  "town"),   # Weekly patrol; covers ~0.7x costs
    ("escort",        60, 130,  5,  "town"),   # Escort job
    ("clearing",     100, 220, 10,  "town"),   # Clear hex of monsters/bandits
    ("warchief_raid",200, 450, 14,  "warchief"),
    ("garrison_duty", 80, 150, 21,  "warchief"),
]

# Bounty pairs: (target description, min, max)
BOUNTY_TABLE = [
    ("local criminal",             5,  15),
    ("named bandit",              10,  25),
    ("deserter",                   2,   5),
    ("warlord's enemy",           50, 200),
    ("professional breach target", 10,  30),
]

# Tribute (forced) — D6 table from proposal Section 4, row 1-6 × settlement tier
# Using coin columns only for simplicity (FOOD tribute converted at 0.15s/unit)
TRIBUTE_VILLAGE  = [(3, 12), (1, 2), (1, 4), (0, 1), (0, 3), (0, 0)]  # (min_silver, max_silver)
TRIBUTE_TOWN     = [(3, 18), (7, 21), (7, 21), (2, 7), (3, 12), (5, 30)]

# ─── COMBAT PARAMETERS ─────────────────────────────────────────────────────

CASUALTY_RATE_PER_FIGHT = 0.08   # 8% chance any fighter becomes casualty per engagement
CASUALTY_RATE_HARD_JOB  = 0.15   # 15% for warchief-tier or "hard" contracts
FIGHT_CHANCE_PER_CONTRACT = 0.70  # 70% of contracts involve at least one engagement

# ─── MORALE — from Section 3 MORALE table ──────────────────────────────────

MORALE_START       = 4       # Fresh + first success (per proposal)
MORALE_MIN         = 1
MORALE_MAX         = 6
MORALE_VICTORY     = 1       # per successful engagement
MORALE_PAY_BONUS   = 1       # once per season if paid on time
MORALE_NONPAY      = -1      # per late-payment week
MORALE_BROKEN_CONTRACT = -2

# — Desertion probability by morale on non-payment ———
def non_payment_roll(rng: random.Random) -> str:
    """D6 field non-payment table from Section 3."""
    r = rng.randint(1, 6)
    if r == 1: return "desert_d3"    # D3 fighters desert
    if r == 2: return "equipment_stolen"
    if r == 3: return "morale_hit"   # -1 MORALE
    if r == 4: return "confrontation"
    if r == 5: return "morale_hit"
    return "remembered"              # counts double next time

# ─── HEX WORLD ─────────────────────────────────────────────────────────────

class SettlementTier(int, Enum):
    NONE       = 0
    VILLAGE    = 1   # Tiny; subsistence; tribute only
    TOWN       = 2   # Trade hub; generates contracts
    WARCHIEF   = 3   # Power center; big contracts

@dataclass
class Hex:
    x: int
    y: int
    terrain: str
    settlement: SettlementTier = SettlementTier.NONE
    feud_track: int = 0           # 0–4; higher = hostile
    standing: float = 0.0         # band's standing at this location
    contract_available: Optional[dict] = None
    bounty_available: Optional[dict] = None
    contract_cooldown: int = 0    # days until new contract posted
    tribute_drained: int = 0      # times tribute demanded this year

def build_world(rng: random.Random, size: int = WORLD_SIZE) -> dict:
    """Generate a hex world as a flat dict {(x,y): Hex}."""
    terrains = (["forest"] * 30 + ["dark_forest"] * 5 +
                ["plains"] * 20 + ["hills"] * 20 +
                ["ruins"] * 10 + ["tundra"] * 5 +
                ["settlement"] * 10)

    world = {}
    for x in range(size):
        for y in range(size):
            t = rng.choice(terrains)
            tier = SettlementTier.NONE

            # Force settlement hex to have a settlement
            if t == "settlement":
                roll = rng.random()
                if roll < 0.50:
                    tier = SettlementTier.VILLAGE
                elif roll < 0.80:
                    tier = SettlementTier.TOWN
                else:
                    tier = SettlementTier.WARCHIEF
            # Non-settlement hexes sometimes have a settlement anyway
            elif rng.random() < 0.08:
                tier = SettlementTier.VILLAGE

            world[(x, y)] = Hex(x, y, t, tier)

    return world


def refresh_contracts(world: dict, rng: random.Random):
    """Post contracts and bounties at eligible settlements."""
    for h in world.values():
        if h.contract_cooldown > 0:
            h.contract_cooldown -= 1

        if h.settlement in (SettlementTier.TOWN, SettlementTier.WARCHIEF):
            if h.contract_available is None and h.contract_cooldown == 0:
                if rng.random() < 0.55:
                    # Filter by tier
                    min_tier = "warchief" if h.settlement == SettlementTier.WARCHIEF else "town"
                    eligible = [c for c in CONTRACT_TYPES if c[4] == min_tier or
                                (min_tier == "warchief") or
                                (c[4] == "town" and h.settlement >= SettlementTier.TOWN)]
                    ct = rng.choice(eligible)
                    pay = rng.uniform(ct[1], ct[2])
                    h.contract_available = {
                        "name": ct[0],
                        "pay": round(pay, 1),
                        "duration": ct[3] + rng.randint(-2, 2),
                        "hard": (ct[0] in ("warchief_raid",)),
                    }

            if h.bounty_available is None and rng.random() < 0.25:
                bt = rng.choice(BOUNTY_TABLE)
                h.bounty_available = {
                    "name": bt[0],
                    "pay": rng.uniform(bt[1], bt[2]),
                }


def distance(a: Tuple[int,int], b: Tuple[int,int]) -> int:
    """Hex grid Manhattan distance (axial approximation)."""
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))


def nearest_employer(pos: Tuple[int,int], world: dict,
                     min_tier: SettlementTier = SettlementTier.TOWN) -> Optional[Tuple[int,int]]:
    """Find nearest hex with a contract and acceptable standing."""
    candidates = [
        (distance(pos, (h.x, h.y)), (h.x, h.y))
        for h in world.values()
        if h.contract_available is not None
        and h.settlement >= min_tier
        and h.feud_track < 3
    ]
    if not candidates:
        return None
    candidates.sort()
    return candidates[0][1]


def step_toward(pos: Tuple[int,int], target: Tuple[int,int]) -> Tuple[int,int]:
    """Move one hex toward target."""
    dx = target[0] - pos[0]
    dy = target[1] - pos[1]
    nx = pos[0] + (1 if dx > 0 else -1 if dx < 0 else 0)
    ny = pos[1] + (1 if dy > 0 else -1 if dy < 0 else 0)
    return (nx, ny)


# ─── BAND ──────────────────────────────────────────────────────────────────

@dataclass
class Band:
    # Roster
    commons:   int = 6
    veterans:  int = 2
    elites:    int = 0
    named_men: int = 1    # sergeant
    casters:   int = 0    # default: no caster

    # Status
    treasury:  float = 100.0
    morale:    int = MORALE_START
    days_unpaid: int = 0

    # Position
    pos: Tuple[int,int] = field(default_factory=lambda: (5, 5))

    # Tracking
    day: int = 0
    current_contract: Optional[dict] = None
    contract_day: int = 0

    # Ledger
    income_contracts:  float = 0.0
    income_bounties:   float = 0.0
    income_tribute:    float = 0.0
    expense_wages:     float = 0.0
    expense_food:      float = 0.0
    expense_recruiting: float = 0.0

    # Events log
    events: List[str] = field(default_factory=list)

    @property
    def size(self) -> int:
        return self.commons + self.veterans + self.elites + self.named_men + self.casters

    @property
    def daily_wage(self) -> float:
        return (
            self.commons   * WAGE["common"]   +
            self.veterans  * WAGE["veteran"]  +
            self.elites    * WAGE["elite"]    +
            self.named_men * WAGE["named_man"] +
            self.casters   * WAGE["caster_initiate"]
        )

    @property
    def is_alive(self) -> bool:
        return self.size >= 3 and self.morale >= MORALE_MIN and self.treasury > -50

    def forage(self, terrain: str, rng: random.Random) -> float:
        """
        Assign up to 30% of non-contract fighters as foragers.
        Returns FOOD covered (rest must be purchased).
        """
        food_needed = self.size * FOOD_PER_MAN_DAY
        # During a contract 30% forage; traveling 40%; at a settlement 0%
        if terrain == "settlement":
            return 0.0
        if self.current_contract:
            foragers = max(1, int(self.size * 0.30))
        else:
            foragers = max(1, int(self.size * 0.40))

        rates = FORAGE_TABLE.get(terrain, FORAGE_TABLE["plains"])
        if foragers <= 2:
            forage_food = rates[0]
        elif foragers <= 5:
            forage_food = rates[1]
        elif foragers <= 10:
            forage_food = rates[2]
        else:
            forage_food = rates[3]

        # Randomise ±20%
        forage_food *= rng.uniform(0.8, 1.2)
        return min(food_needed, forage_food)

    def pay_daily(self, terrain: str, rng: random.Random) -> float:
        """
        Deduct wages and food. Returns net cost (negative = expense).
        Accrue unpaid days if broke.
        """
        wages = self.daily_wage

        food_needed = self.size * FOOD_PER_MAN_DAY
        foraged = self.forage(terrain, rng)
        purchased = max(0.0, food_needed - foraged)
        food_cost = purchased * FOOD_PURCHASE_PRICE

        total = wages + food_cost

        if self.treasury >= total:
            self.treasury -= total
            self.expense_wages += wages
            self.expense_food  += food_cost
            self.days_unpaid = 0
        else:
            # Can't pay — partial if possible
            partial = max(0.0, self.treasury)
            self.treasury -= partial
            self.expense_wages += partial
            self.days_unpaid += 1

        return total

    def apply_combat(self, hard: bool, rng: random.Random):
        """Resolve an engagement. Casualties and morale."""
        rate = CASUALTY_RATE_HARD_JOB if hard else CASUALTY_RATE_PER_FIGHT
        roster = (["common"] * self.commons +
                  ["veteran"] * self.veterans +
                  ["elite"] * self.elites +
                  ["named_man"] * self.named_men)
        casualties = 0
        for member in roster:
            if rng.random() < rate:
                casualties += 1
                self._lose_fighter(member)
        if casualties == 0:
            self.morale = min(MORALE_MAX, self.morale + MORALE_VICTORY)
        else:
            self.events.append(
                f"day {self.day}: {casualties} casualty(ies) in fight "
                f"({'hard' if hard else 'normal'})"
            )
        return casualties

    def _lose_fighter(self, kind: str):
        if kind == "common"   and self.commons   > 0: self.commons   -= 1
        elif kind == "veteran" and self.veterans  > 0: self.veterans  -= 1
        elif kind == "elite"   and self.elites    > 0: self.elites    -= 1
        elif kind == "named_man" and self.named_men > 0: self.named_men -= 1

    def check_morale_payment(self, rng: random.Random):
        """Apply non-payment consequences if overdue (7+ days)."""
        if self.days_unpaid < 7:
            return
        result = non_payment_roll(rng)
        if result == "desert_d3":
            lost = rng.randint(1, 3)
            lost = min(lost, self.commons)
            self.commons -= lost
            self.morale = max(MORALE_MIN, self.morale + MORALE_NONPAY)
            self.events.append(
                f"day {self.day}: {lost} deserted (non-payment)"
            )
        elif result in ("morale_hit", "confrontation"):
            self.morale = max(MORALE_MIN, self.morale + MORALE_NONPAY)
        # "remembered" doubles next roll — tracked as extra days_unpaid nudge
        elif result == "remembered":
            self.days_unpaid += 3  # will double-trigger sooner

    def recruit_replacement(self, rng: random.Random):
        """Hire a common if band drops below starting strength with funds."""
        target = 8   # ideal warband size
        if self.size < target and self.treasury > 50:
            cost = rng.uniform(3, 8)   # one-time hiring bonus
            self.treasury -= cost
            self.expense_recruiting += cost
            self.commons += 1


FOOD_PER_MAN_DAY = 1  # FOOD units per man per day


# ─── SINGLE SIMULATION RUN ─────────────────────────────────────────────────

def run_simulation(seed: int) -> dict:
    rng = random.Random(seed)
    world = build_world(rng)
    band = Band()

    # Daily snapshots
    treasury_history  = []
    morale_history    = []
    size_history      = []

    income_by_source  = defaultdict(float)
    expense_by_source = defaultdict(float)

    # Season tracking (for morale pay-bonus)
    last_season_pay_bonus = -1

    on_contract_days = 0
    travel_days      = 0
    idle_days        = 0

    collapse_day     = None

    for day in range(SIM_DAYS):
        band.day = day

        # Weekly refresh of contracts in the world
        if day % 7 == 0:
            refresh_contracts(world, rng)

        current_hex = world.get(band.pos)
        if current_hex is None:
            # Out of bounds; clamp
            band.pos = (
                max(0, min(WORLD_SIZE - 1, band.pos[0])),
                max(0, min(WORLD_SIZE - 1, band.pos[1])),
            )
            current_hex = world[band.pos]

        terrain = current_hex.terrain

        # ── PAY DAILY COSTS ────────────────────────────────────────────────
        daily_cost = band.pay_daily(terrain, rng)
        expense_by_source["wages"]     += band.daily_wage
        food_needed   = band.size * FOOD_PER_MAN_DAY
        foraged_today = band.forage(terrain, rng)
        purchased     = max(0.0, food_needed - foraged_today)
        expense_by_source["food"]      += purchased * FOOD_PURCHASE_PRICE

        # ── SEASON PAY MORALE BONUS ────────────────────────────────────────
        season = day // 91
        if season != last_season_pay_bonus and band.days_unpaid == 0:
            band.morale = min(MORALE_MAX, band.morale + MORALE_PAY_BONUS)
            last_season_pay_bonus = season

        # ── CHECK MORALE / NON-PAYMENT ─────────────────────────────────────
        if day % 7 == 0:
            band.check_morale_payment(rng)

        # ── ACTIVE CONTRACT RESOLUTION ─────────────────────────────────────
        if band.current_contract is not None:
            band.contract_day += 1
            on_contract_days += 1

            contract = band.current_contract
            duration = contract["duration"]

            # Combat events during the contract
            if rng.random() < FIGHT_CHANCE_PER_CONTRACT / duration:
                band.apply_combat(contract.get("hard", False), rng)

            # Contract complete
            if band.contract_day >= duration:
                pay = contract["pay"]
                band.treasury += pay
                band.income_contracts += pay
                income_by_source["contracts"] += pay

                # Bounty on the side?
                if current_hex.bounty_available and rng.random() < 0.35:
                    bp = current_hex.bounty_available["pay"]
                    band.treasury += bp
                    band.income_bounties += bp
                    income_by_source["bounties"] += bp
                    current_hex.bounty_available = None

                current_hex.contract_available = None
                current_hex.contract_cooldown = rng.randint(14, 35)
                band.current_contract = None
                band.contract_day = 0

        # ── TAKE NEW CONTRACT ──────────────────────────────────────────────
        elif (current_hex.contract_available is not None
              and current_hex.feud_track < 3
              and band.morale >= 2):
            ct = current_hex.contract_available
            # Accept if pay > 75% of projected cost (some wiggle for supply)
            expected_cost = band.daily_wage * ct["duration"] * 1.1
            if ct["pay"] >= expected_cost * 0.75:
                band.current_contract = ct
                band.contract_day = 0
            elif band.treasury < band.daily_wage * 7:
                # Desperate — take anything
                band.current_contract = ct
                band.contract_day = 0

        # ── TRAVEL ────────────────────────────────────────────────────────
        else:
            target = nearest_employer(band.pos, world)

            if target is None:
                # No work found — check if desperate enough for tribute
                if (band.treasury < band.daily_wage * 5
                        and current_hex.settlement in (SettlementTier.VILLAGE, SettlementTier.TOWN)
                        and current_hex.tribute_drained < 3
                        and current_hex.feud_track < 3):
                    # Demand tribute
                    if current_hex.settlement == SettlementTier.VILLAGE:
                        roll = rng.choice(TRIBUTE_VILLAGE)
                    else:
                        roll = rng.choice(TRIBUTE_TOWN)
                    tribute = rng.uniform(roll[0], roll[1]) if roll[1] > roll[0] else roll[0]
                    band.treasury += tribute
                    band.income_tribute += tribute
                    income_by_source["tribute"] += tribute
                    current_hex.tribute_drained += 1
                    current_hex.feud_track = min(4, current_hex.feud_track + 1)
                    band.events.append(
                        f"day {day}: tribute {tribute:.1f}s from "
                        f"{current_hex.settlement.name} @ {band.pos}, "
                        f"feud {current_hex.feud_track}"
                    )
                else:
                    idle_days += 1
            else:
                if band.pos != target:
                    band.pos = step_toward(band.pos, target)
                    travel_days += 1
                    current_hex = world[band.pos]
                    terrain = current_hex.terrain

        # ── RECRUITING ────────────────────────────────────────────────────
        if day % 14 == 0 and current_hex.settlement != SettlementTier.NONE:
            band.recruit_replacement(rng)

        # ── SNAPSHOT ──────────────────────────────────────────────────────
        treasury_history.append(band.treasury)
        morale_history.append(band.morale)
        size_history.append(band.size)

        if not band.is_alive and collapse_day is None:
            collapse_day = day
            break

    # ── FINAL METRICS ──────────────────────────────────────────────────────
    total_income  = band.income_contracts + band.income_bounties + band.income_tribute
    total_expense = band.expense_wages    + band.expense_food    + band.expense_recruiting

    return {
        "survived":          collapse_day is None,
        "collapse_day":      collapse_day,
        "final_treasury":    band.treasury,
        "min_treasury":      min(treasury_history) if treasury_history else 0,
        "max_treasury":      max(treasury_history) if treasury_history else 0,
        "income_contracts":  band.income_contracts,
        "income_bounties":   band.income_bounties,
        "income_tribute":    band.income_tribute,
        "total_income":      total_income,
        "expense_wages":     band.expense_wages,
        "expense_food":      band.expense_food,
        "expense_recruiting":band.expense_recruiting,
        "total_expense":     total_expense,
        "profit":            band.treasury - 100.0,   # vs. starting 100s
        "net_margin":        (total_income - total_expense) / max(1, total_income),
        "on_contract_days":  on_contract_days,
        "travel_days":       travel_days,
        "idle_days":         idle_days,
        "final_size":        band.size,
        "final_morale":      band.morale,
        "events_count":      len(band.events),
        "treasury_history":  treasury_history,
        "morale_history":    morale_history,
        "size_history":      size_history,
    }


# ─── VARIANT CONFIGURATIONS ────────────────────────────────────────────────

def run_variant(name: str, patch_fn, seed_offset: int = 0) -> List[dict]:
    """Run RUNS simulations with an optional Band patch applied."""
    results = []
    for i in range(RUNS):
        # Temporarily patch globals or Band defaults via closure
        result = patch_fn(i + seed_offset + RANDOM_SEED)
        result["variant"] = name
        results.append(result)
    return results


def run_baseline(seed: int) -> dict:
    return run_simulation(seed)


def run_with_adept_caster(seed: int) -> dict:
    """Band carries an Adept caster at 15s/day."""
    rng = random.Random(seed)
    world = build_world(rng)
    band = Band(casters=1)   # adds WAGE_CASTER_ADEPT to daily cost
    # Override caster wage rate
    original_wage = WAGE["caster_initiate"]
    WAGE["caster_initiate"] = WAGE["caster_adept"]  # cheat: reuse slot
    result = run_simulation(seed)
    WAGE["caster_initiate"] = original_wage
    return result


def run_small_band(seed: int) -> dict:
    """
    Skirmisher: 4 commons + 1 veteran = 5 men, lower costs, smaller contracts.
    Patch: override Band defaults via simulation modification.
    """
    rng = random.Random(seed)
    world = build_world(rng)
    band = Band(commons=4, veterans=1, named_men=0)
    # Run inline (copy-paste with band override is cleanest)
    return _run_with_band(band, rng, world)


def run_with_caster_initiate(seed: int) -> dict:
    """Band with 1 Initiate caster."""
    rng = random.Random(seed)
    world = build_world(rng)
    band = Band(casters=1)
    return _run_with_band(band, rng, world)


def _run_with_band(band: Band, rng: random.Random, world: dict) -> dict:
    """Full simulation using the provided band and world objects."""
    treasury_history = []
    morale_history   = []
    size_history     = []
    income_by_source  = defaultdict(float)
    last_season_pay_bonus = -1
    on_contract_days = 0
    travel_days      = 0
    idle_days        = 0
    collapse_day     = None

    for day in range(SIM_DAYS):
        band.day = day
        if day % 7 == 0:
            refresh_contracts(world, rng)

        current_hex = world.get(band.pos)
        if current_hex is None:
            band.pos = (
                max(0, min(WORLD_SIZE - 1, band.pos[0])),
                max(0, min(WORLD_SIZE - 1, band.pos[1])),
            )
            current_hex = world[band.pos]

        terrain = current_hex.terrain
        band.pay_daily(terrain, rng)

        season = day // 91
        if season != last_season_pay_bonus and band.days_unpaid == 0:
            band.morale = min(MORALE_MAX, band.morale + MORALE_PAY_BONUS)
            last_season_pay_bonus = season

        if day % 7 == 0:
            band.check_morale_payment(rng)

        if band.current_contract is not None:
            band.contract_day += 1
            on_contract_days += 1
            contract = band.current_contract
            duration = contract["duration"]
            if rng.random() < FIGHT_CHANCE_PER_CONTRACT / duration:
                band.apply_combat(contract.get("hard", False), rng)
            if band.contract_day >= duration:
                pay = contract["pay"]
                band.treasury += pay
                band.income_contracts += pay
                income_by_source["contracts"] += pay
                if current_hex.bounty_available and rng.random() < 0.35:
                    bp = current_hex.bounty_available["pay"]
                    band.treasury += bp
                    band.income_bounties += bp
                    income_by_source["bounties"] += bp
                    current_hex.bounty_available = None
                current_hex.contract_available = None
                current_hex.contract_cooldown = rng.randint(14, 35)
                band.current_contract = None
                band.contract_day = 0
        elif (current_hex.contract_available is not None
              and current_hex.feud_track < 3
              and band.morale >= 2):
            ct = current_hex.contract_available
            expected_cost = band.daily_wage * ct["duration"] * 1.1
            if ct["pay"] >= expected_cost * 0.75 or band.treasury < band.daily_wage * 7:
                band.current_contract = ct
                band.contract_day = 0
        else:
            target = nearest_employer(band.pos, world)
            if target is None:
                if (band.treasury < band.daily_wage * 5
                        and current_hex.settlement in (SettlementTier.VILLAGE, SettlementTier.TOWN)
                        and current_hex.tribute_drained < 3
                        and current_hex.feud_track < 3):
                    roll = rng.choice(TRIBUTE_VILLAGE
                                      if current_hex.settlement == SettlementTier.VILLAGE
                                      else TRIBUTE_TOWN)
                    tribute = rng.uniform(roll[0], roll[1]) if roll[1] > roll[0] else roll[0]
                    band.treasury += tribute
                    band.income_tribute += tribute
                    income_by_source["tribute"] += tribute
                    current_hex.tribute_drained += 1
                    current_hex.feud_track = min(4, current_hex.feud_track + 1)
                else:
                    idle_days += 1
            else:
                if band.pos != target:
                    band.pos = step_toward(band.pos, target)
                    travel_days += 1

        if day % 14 == 0 and current_hex.settlement != SettlementTier.NONE:
            band.recruit_replacement(rng)

        treasury_history.append(band.treasury)
        morale_history.append(band.morale)
        size_history.append(band.size)

        if not band.is_alive and collapse_day is None:
            collapse_day = day
            break

    total_income  = band.income_contracts + band.income_bounties + band.income_tribute
    total_expense = band.expense_wages    + band.expense_food    + band.expense_recruiting

    return {
        "survived":           collapse_day is None,
        "collapse_day":       collapse_day,
        "final_treasury":     band.treasury,
        "min_treasury":       min(treasury_history) if treasury_history else 0,
        "max_treasury":       max(treasury_history) if treasury_history else 0,
        "income_contracts":   band.income_contracts,
        "income_bounties":    band.income_bounties,
        "income_tribute":     band.income_tribute,
        "total_income":       total_income,
        "expense_wages":      band.expense_wages,
        "expense_food":       band.expense_food,
        "expense_recruiting": band.expense_recruiting,
        "total_expense":      total_expense,
        "profit":             band.treasury - 100.0,
        "net_margin":         (total_income - total_expense) / max(1, total_income),
        "on_contract_days":   on_contract_days,
        "travel_days":        travel_days,
        "idle_days":          idle_days,
        "final_size":         band.size,
        "final_morale":       band.morale,
        "events_count":       len(band.events),
        "treasury_history":   treasury_history,
        "morale_history":     morale_history,
        "size_history":       size_history,
    }


# ─── STATISTICS HELPERS ────────────────────────────────────────────────────

def pct(values: list, p: float) -> float:
    sv = sorted(values)
    idx = int(len(sv) * p / 100)
    return sv[min(idx, len(sv) - 1)]


def summarise(results: List[dict], label: str) -> dict:
    fin = [r["final_treasury"]    for r in results]
    mn  = [r["min_treasury"]      for r in results]
    ing = [r["income_contracts"]  for r in results]
    inb = [r["income_bounties"]   for r in results]
    int_= [r["income_tribute"]    for r in results]
    ew  = [r["expense_wages"]     for r in results]
    ef  = [r["expense_food"]      for r in results]
    ocd = [r["on_contract_days"]  for r in results]
    trd = [r["travel_days"]       for r in results]
    ild = [r["idle_days"]         for r in results]
    surv= sum(1 for r in results if r["survived"])
    coll= [r["collapse_day"] for r in results if not r["survived"]]

    return {
        "label":              label,
        "n":                  len(results),
        "survival_rate":      surv / len(results),
        "median_final_treas": statistics.median(fin),
        "p10_final_treas":    pct(fin, 10),
        "p90_final_treas":    pct(fin, 90),
        "median_min_treas":   statistics.median(mn),
        "pct_below_zero":     sum(1 for v in fin if v < 0) / len(results),
        "mean_contract_inc":  statistics.mean(ing),
        "mean_bounty_inc":    statistics.mean(inb),
        "mean_tribute_inc":   statistics.mean(int_),
        "mean_wage_exp":      statistics.mean(ew),
        "mean_food_exp":      statistics.mean(ef),
        "mean_total_inc":     statistics.mean([r["total_income"]  for r in results]),
        "mean_total_exp":     statistics.mean([r["total_expense"] for r in results]),
        "mean_net_margin":    statistics.mean([r["net_margin"]    for r in results]),
        "mean_on_contract_days": statistics.mean(ocd),
        "mean_travel_days":      statistics.mean(trd),
        "mean_idle_days":        statistics.mean(ild),
        "mean_collapse_day":  statistics.mean(coll) if coll else None,
        "contract_days_pct":  statistics.mean(ocd) / SIM_DAYS,
        "travel_days_pct":    statistics.mean(trd) / SIM_DAYS,
        "idle_days_pct":      statistics.mean(ild) / SIM_DAYS,
    }


# ─── REPORT ────────────────────────────────────────────────────────────────

def print_report(summaries: List[dict]):
    sep  = "─" * 72
    sep2 = "═" * 72

    print()
    print(sep2)
    print("  FORBIDDEN LANDS 2E — MERCENARY BAND ECONOMY SIMULATION")
    print(f"  {RUNS} runs × {SIM_DAYS} days  |  Starting treasury: 100 silver")
    print(sep2)

    for s in summaries:
        print()
        print(f"  ▶ VARIANT: {s['label']}")
        print(sep)

        print(f"  Survival rate:          {s['survival_rate']*100:6.1f}%")
        if s["mean_collapse_day"] is not None:
            print(f"  Mean collapse day:      {s['mean_collapse_day']:6.1f}")
        print(f"  % runs ending broke:    {s['pct_below_zero']*100:6.1f}%")
        print()

        print(f"  TREASURY (final, silver)")
        print(f"    Median:               {s['median_final_treas']:8.1f}")
        print(f"    10th percentile:      {s['p10_final_treas']:8.1f}")
        print(f"    90th percentile:      {s['p90_final_treas']:8.1f}")
        print(f"    Median minimum:       {s['median_min_treas']:8.1f}")
        print()

        print(f"  INCOME (annual mean, silver)")
        print(f"    Contracts:            {s['mean_contract_inc']:8.1f}"
              f"  ({s['mean_contract_inc']/max(1,s['mean_total_inc'])*100:4.1f}%)")
        print(f"    Bounties:             {s['mean_bounty_inc']:8.1f}"
              f"  ({s['mean_bounty_inc']/max(1,s['mean_total_inc'])*100:4.1f}%)")
        print(f"    Tribute (coerced):    {s['mean_tribute_inc']:8.1f}"
              f"  ({s['mean_tribute_inc']/max(1,s['mean_total_inc'])*100:4.1f}%)")
        print(f"    ─── TOTAL:            {s['mean_total_inc']:8.1f}")
        print()

        print(f"  EXPENSES (annual mean, silver)")
        print(f"    Wages:                {s['mean_wage_exp']:8.1f}"
              f"  ({s['mean_wage_exp']/max(1,s['mean_total_exp'])*100:4.1f}%)")
        print(f"    Food:                 {s['mean_food_exp']:8.1f}"
              f"  ({s['mean_food_exp']/max(1,s['mean_total_exp'])*100:4.1f}%)")
        print(f"    ─── TOTAL:            {s['mean_total_exp']:8.1f}")
        print()

        inc = s["mean_total_inc"]
        exp = s["mean_total_exp"]
        margin = s["mean_net_margin"] * 100
        surplus_deficit = inc - exp
        print(f"  Net margin:             {margin:+6.1f}%  "
              f"(income − expense = {surplus_deficit:+.1f}s/year)")
        print()

        print(f"  TIME ALLOCATION (% of {SIM_DAYS} days)")
        print(f"    On contract:          {s['contract_days_pct']*100:6.1f}%  "
              f"({s['mean_on_contract_days']:.0f} days)")
        print(f"    Traveling to work:    {s['travel_days_pct']*100:6.1f}%  "
              f"({s['mean_travel_days']:.0f} days)")
        print(f"    Idle / no work:       {s['idle_days_pct']*100:6.1f}%  "
              f"({s['mean_idle_days']:.0f} days)")
        print()

    # ── PROBLEM SUMMARY ──────────────────────────────────────────────────

    print(sep2)
    print("  IDENTIFIED ECONOMY PROBLEMS")
    print(sep2)

    baseline = summaries[0]
    daily_cost_approx = (
        6 * WAGE["common"] +
        2 * WAGE["veteran"] +
        1 * WAGE["named_man"] +
        (9 * FOOD_PER_MAN_DAY * FOOD_PURCHASE_PRICE)   # ~half purchased
    )
    weekly_cost = daily_cost_approx * 7

    print()
    print(f"  BASE WARBAND (6 common + 2 veteran + 1 named man = 9 men)")
    print(f"  Daily wage cost:    {daily_cost_approx:.1f}s")
    print(f"  Weekly wage cost:   {weekly_cost:.1f}s")
    annual_wage = daily_cost_approx * 365
    print(f"  Annual wage cost:   {annual_wage:.0f}s  (wages alone, no food)")
    print()

    # Contract coverage ratio
    if baseline["mean_on_contract_days"] > 0:
        contract_daily_rate = (baseline["mean_contract_inc"] /
                               max(1, baseline["mean_on_contract_days"]))
    else:
        contract_daily_rate = 0
    print(f"  Daily income when on contract: ~{contract_daily_rate:.1f}s/day")
    print(f"  Daily total cost:              ~{daily_cost_approx:.1f}s/day")
    coverage = contract_daily_rate / max(0.01, daily_cost_approx)
    print(f"  Contract coverage of costs:    {coverage*100:.1f}%")
    print()

    # Dead time cost
    dead_days = baseline["mean_travel_days"] + baseline["mean_idle_days"]
    dead_cost = dead_days * daily_cost_approx
    print(f"  Dead time (travel + idle):     {dead_days:.0f} days/year")
    print(f"  Cost during dead time:         {dead_cost:.0f}s/year")
    print(f"    (band burns money at full rate with zero income)")
    print()

    # Tribute pressure
    trib = baseline["mean_tribute_inc"]
    if trib > baseline["mean_contract_inc"] * 0.30:
        print(f"  ⚠ Tribute income ({trib:.0f}s) = "
              f"{trib/max(1,baseline['mean_total_inc'])*100:.1f}% of total.")
        print(f"    Bands are economically pressured into extortion.")
    else:
        print(f"  Tribute income: {trib:.0f}s  "
              f"({trib/max(1,baseline['mean_total_inc'])*100:.1f}% of total)")
    print()

    # Protection contract check
    protection_season_pay  = 95    # midpoint of 80–120 silver equivalent
    band_season_wages      = daily_cost_approx * 91
    print(f"  PROTECTION CONTRACT PROBLEM (Section 5, settlement tier):")
    print(f"    A protection contract, 1 season, pays ~{protection_season_pay}s equivalent.")
    print(f"    Band wages alone for 1 season:  ~{band_season_wages:.0f}s")
    shortfall = band_season_wages - protection_season_pay
    print(f"    Shortfall:                      ~{shortfall:.0f}s  "
          f"(contract covers {protection_season_pay/band_season_wages*100:.1f}% of wages)")
    print()

    # Caster ROI
    caster_annual_cost = WAGE["caster_adept"] * 365
    caster_annual_cost_init = WAGE["caster_initiate"] * 365
    print(f"  CASTER COST ANALYSIS:")
    print(f"    Initiate caster:  {caster_annual_cost_init}s/year in wages")
    print(f"    Adept caster:     {caster_annual_cost}s/year in wages")
    print(f"    (No contract type provides a specific caster premium.)")
    print(f"    Band must earn this extra from the same contract pool.")
    print()

    # Gap analysis — what contract rate would be break-even
    annual_expense_target = annual_wage + (9 * 0.15 * 365 * 0.5)  # wages + ~half food
    contract_days_typical = baseline["mean_on_contract_days"]
    breakeven_daily = annual_expense_target / max(1, contract_days_typical)
    print(f"  BREAK-EVEN ANALYSIS:")
    print(f"    Annual expenses (est.):        {annual_expense_target:.0f}s")
    print(f"    Days on contract (mean):       {contract_days_typical:.0f}")
    print(f"    Required daily contract rate:  {breakeven_daily:.1f}s/day")
    print(f"    Actual daily contract rate:    {contract_daily_rate:.1f}s/day")
    gap = breakeven_daily - contract_daily_rate
    if gap > 0:
        print(f"    GAP:  {gap:.1f}s/day under break-even")
        print(f"          Contracts need to pay ~{gap/max(0.01,contract_daily_rate)*100:.0f}% more")
        print(f"          OR contract availability needs to increase")
    else:
        print(f"    System is above break-even by {-gap:.1f}s/day on contract")
    print()

    print(sep)
    print("  DESIGN RECOMMENDATIONS — PROBLEMS FOUND")
    print(sep)

    problems = []
    if baseline["pct_below_zero"] > 0.20:
        problems.append(
            f"• {baseline['pct_below_zero']*100:.0f}% of runs go bankrupt. "
            f"The economy is not self-sustaining at current contract rates."
        )
    if dead_days > 90:
        problems.append(
            f"• Dead time averages {dead_days:.0f} days/year ({dead_days/365*100:.0f}% of the year). "
            f"Wages burn at full rate with zero income during transit."
        )
    if coverage < 1.20:
        problems.append(
            f"• Contracts pay ~{coverage*100:.0f}% of daily costs when active. "
            f"There is no buffer for bad luck, casualties, or downtime upgrades."
        )
    if trib > baseline["mean_contract_inc"] * 0.20:
        problems.append(
            f"• Tribute accounts for {trib/max(1,baseline['mean_total_inc'])*100:.1f}% of income. "
            f"The math nudges captains toward extortion regardless of morality."
        )
    if protection_season_pay < band_season_wages * 0.60:
        problems.append(
            f"• Protection contracts (80–120s/season equivalent) cover only "
            f"{protection_season_pay/band_season_wages*100:.0f}% of wages. "
            f"These contracts are economically inviable unless food/shelter savings are substantial."
        )
    if caster_annual_cost_init > baseline["mean_contract_inc"] * 0.15:
        problems.append(
            f"• An Initiate caster costs {caster_annual_cost_init}s/year. "
            f"With no contract premium for caster bands, adding one erodes margin further."
        )

    if problems:
        print()
        for p in problems:
            print(f"  {p}")
    else:
        print("  No major problems detected at these parameter settings.")

    print()
    print(sep2)
    print()


# ─── MAIN ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    print(f"\nRunning {RUNS} simulations × {SIM_DAYS} days each...")
    print("This takes ~20–30 seconds.\n")

    # ── Baseline: 6 common + 2 veteran + 1 named man ──────────────────────
    BASE_RESULTS = []
    for i in range(RUNS):
        r = run_simulation(RANDOM_SEED + i)
        r["variant"] = "baseline"
        BASE_RESULTS.append(r)
    print(f"  Baseline done ({RUNS} runs)")

    # ── Variant: small band (4 common + 1 veteran, no named man) ──────────
    SMALL_RESULTS = []
    for i in range(RUNS):
        r = run_small_band(RANDOM_SEED + i + 1000)
        r["variant"] = "small_band"
        SMALL_RESULTS.append(r)
    print(f"  Small band done ({RUNS} runs)")

    # ── Variant: band with Initiate caster ────────────────────────────────
    CASTER_RESULTS = []
    for i in range(RUNS):
        r = run_with_caster_initiate(RANDOM_SEED + i + 2000)
        r["variant"] = "caster_initiate"
        CASTER_RESULTS.append(r)
    print(f"  Caster (Initiate) done ({RUNS} runs)")

    summaries = [
        summarise(BASE_RESULTS,   "Standard Warband  (6×common + 2×veteran + 1×named man)"),
        summarise(SMALL_RESULTS,  "Small Band        (4×common + 1×veteran, no named man)"),
        summarise(CASTER_RESULTS, "Warband + Caster  (adds Initiate at 6s/day)"),
    ]

    print()
    print_report(summaries)

    # ── Per-day treasury percentile chart (baseline only) ─────────────────
    print("  TREASURY OVER TIME — BASELINE (mean ± 1 stdev, 100-day intervals)")
    print()
    print(f"  {'Day':>4}  {'Mean':>7}  {'Stdev':>7}  {'P10':>7}  {'P90':>7}  BAR")
    print("  " + "─" * 60)

    for checkpoint in range(0, SIM_DAYS + 1, 25):
        vals = []
        for r in BASE_RESULTS:
            hist = r["treasury_history"]
            if checkpoint < len(hist):
                vals.append(hist[checkpoint])
        if not vals:
            continue
        m  = statistics.mean(vals)
        sd = statistics.stdev(vals) if len(vals) > 1 else 0
        p10 = pct(vals, 10)
        p90 = pct(vals, 90)
        bar_len = max(0, int((m / 300) * 30))
        bar = "█" * bar_len + ("▓" if m < 0 else "")
        bar_color = "" if m >= 0 else ""
        print(f"  {checkpoint:>4}  {m:>7.1f}  {sd:>7.1f}  {p10:>7.1f}  {p90:>7.1f}  {bar}")

    print()
    print("  (mean treasury at each checkpoint; bar scaled to 300s max)")
    print()
