#!/usr/bin/env python3
"""
Forbidden Lands 2E Traderoads Economic Viability Simulation
Simulates one caravan over one year (4 seasons) across a 30x30 hex map
with 20 settlements, testing if the economic system produces viable business.
"""

import random
import math
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
from enum import Enum

# ============================================================================
# ENUMS
# ============================================================================

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

class Terrain(Enum):
    PLAINS = 1
    FOREST = 2
    MOUNTAIN = 3
    MARSH = 4
    RIVER = 5

class SettlementSize(Enum):
    HAMLET = 0
    VILLAGE = 1
    TOWN = 2
    STRONGHOLD = 3

class CargoType(Enum):
    BULK = "Bulk staples"
    CRAFT = "Craft goods"
    LUXURY = "Luxury goods"
    RAW = "Raw materials"
    ARMS = "Arms and armor"
    SPECIALTY = "Specialty"

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class CargoItem:
    cargo_type: CargoType
    quantity: int  # load units
    buy_price_per_unit: int  # silver per load unit
    sell_price_multiplier: float = 1.0  # Will be calculated per destination

@dataclass
class Settlement:
    name: str
    hex_x: int
    hex_y: int
    size: SettlementSize
    produces: CargoType  # Cheap to buy here
    needs: CargoType  # Expensive to sell here
    base_produces_price: int  # Silver per load unit
    base_needs_price: int
    has_inn: bool = False
    has_marketplace: bool = False
    has_road: bool = False

    def __hash__(self):
        return hash((self.hex_x, self.hex_y))

@dataclass
class DistanceMemo:
    """Cache for distance calculations"""
    distances: Dict[Tuple[int, int], Dict[Tuple[int, int], int]] = field(default_factory=dict)

    def get_distance(self, from_hex: Tuple[int, int], to_hex: Tuple[int, int]) -> int:
        if from_hex not in self.distances:
            self.distances[from_hex] = {}
        if to_hex not in self.distances[from_hex]:
            # Hex distance (cube coordinates converted to axial)
            dx = abs(from_hex[0] - to_hex[0])
            dy = abs(from_hex[1] - to_hex[1])
            dist = (dx + dy + abs(dx - dy)) // 2
            self.distances[from_hex][to_hex] = dist
        return self.distances[from_hex][to_hex]

@dataclass
class CaravanState:
    name: str
    cargo: List[CargoItem] = field(default_factory=list)
    silver: int = 500  # Starting capital
    current_settlement: Settlement = None
    total_profit: int = 0
    routes_completed: int = 0

    def load_capacity(self) -> int:
        """Total load units carried"""
        return sum(item.quantity for item in self.cargo)

    def cargo_value(self) -> int:
        """Current value of all cargo"""
        return sum(item.quantity * item.buy_price_per_unit for item in self.cargo)

# ============================================================================
# CONSTANTS
# ============================================================================

TRAVEL_DAYS_PER_HEX = 1  # Base: 1 day per hex for wagons on road
WAGON_CAPACITY = 6  # Load units

# Seasonal price multipliers (from proposal)
SEASONAL_MULTIPLIERS = {
    Season.SPRING: {
        CargoType.BULK: 1.5,
        CargoType.CRAFT: 1.0,
        CargoType.LUXURY: 1.0,
        CargoType.RAW: 1.0,
        CargoType.ARMS: 1.0,
        CargoType.SPECIALTY: 1.0,
    },
    Season.SUMMER: {
        CargoType.BULK: 1.0,
        CargoType.CRAFT: 1.0,
        CargoType.LUXURY: 1.0,
        CargoType.RAW: 1.0,
        CargoType.ARMS: 1.0,
        CargoType.SPECIALTY: 1.0,
    },
    Season.AUTUMN: {
        CargoType.BULK: 0.75,
        CargoType.CRAFT: 1.0,
        CargoType.LUXURY: 1.25,
        CargoType.RAW: 1.25,
        CargoType.ARMS: 1.25,
        CargoType.SPECIALTY: 1.0,
    },
    Season.WINTER: {
        CargoType.BULK: 2.0,
        CargoType.CRAFT: 1.25,
        CargoType.LUXURY: 1.5,
        CargoType.RAW: 0.75,
        CargoType.ARMS: 1.0,
        CargoType.SPECIALTY: 1.5,
    },
}

# Supply-based multipliers (low supply = high price)
SUPPLY_MULTIPLIERS = {
    "Common": 0.5,
    "Uncommon": 1.5,
    "Rare": 2.0,
    "Extremely Rare": 2.5,
}

# Daily costs
DROVER_WAGE = 5  # copper per day = 0.05 silver
GUARD_WAGE = 10  # copper per day = 0.1 silver
FEED_PER_ANIMAL = 1  # copper per day = 0.01 silver
ANIMAL_COUNT = 3  # Wagon team + 1 extra

# ============================================================================
# WORLD GENERATION
# ============================================================================

def generate_settlements(hex_size: int = 30, count: int = 20) -> List[Settlement]:
    """Generate random settlements across the map"""
    settlements = []
    cargo_types = [CargoType.BULK, CargoType.CRAFT, CargoType.RAW]

    for i in range(count):
        x = random.randint(0, hex_size - 1)
        y = random.randint(0, hex_size - 1)

        # Avoid duplicates
        while any(s.hex_x == x and s.hex_y == y for s in settlements):
            x = random.randint(0, hex_size - 1)
            y = random.randint(0, hex_size - 1)

        size_roll = random.randint(1, 20)
        if size_roll <= 10:
            size = SettlementSize.HAMLET
            base_buy = 10
            base_sell = 10
        elif size_roll <= 16:
            size = SettlementSize.VILLAGE
            base_buy = 15
            base_sell = 15
        elif size_roll <= 19:
            size = SettlementSize.TOWN
            base_buy = 20
            base_sell = 20
        else:
            size = SettlementSize.STRONGHOLD
            base_buy = 25
            base_sell = 25

        produces = random.choice(cargo_types)
        needs = random.choice([c for c in cargo_types if c != produces])

        settlement = Settlement(
            name=f"Settlement_{i+1}",
            hex_x=x,
            hex_y=y,
            size=size,
            produces=produces,
            needs=needs,
            base_produces_price=base_buy,
            base_needs_price=base_sell,
            has_inn=random.random() < 0.5,
            has_marketplace=random.random() < 0.4,
            has_road=random.random() < 0.3,
        )
        settlements.append(settlement)

    return settlements

# ============================================================================
# PRICE CALCULATION
# ============================================================================

def calculate_sell_price(
    cargo: CargoType,
    destination: Settlement,
    season: Season,
    distance: int,
) -> float:
    """Calculate sell price at destination settlement"""
    base_price = destination.base_needs_price

    # Is destination producing this cargo? If so, oversupply
    supply = "Common" if cargo == destination.produces else "Uncommon"
    if distance > 10:
        supply = "Rare"
    if cargo == destination.needs:
        supply = "Rare"
    if cargo == destination.needs and distance > 15:
        supply = "Extremely Rare"

    supply_mult = SUPPLY_MULTIPLIERS[supply]
    seasonal_mult = SEASONAL_MULTIPLIERS[season].get(cargo, 1.0)

    return base_price * supply_mult * seasonal_mult

def calculate_buy_price(
    cargo: CargoType,
    origin: Settlement,
) -> int:
    """Calculate buy price at origin"""
    if cargo == origin.produces:
        return origin.base_produces_price
    else:
        # Need to source from elsewhere - more expensive
        return origin.base_produces_price * 1.5

# ============================================================================
# CARAVAN OPERATIONS
# ============================================================================

def buy_cargo(
    caravan: CaravanState,
    settlement: Settlement,
    cargo_type: CargoType,
    quantity: int,
) -> bool:
    """Buy cargo at settlement. Returns True if successful"""
    price = calculate_buy_price(cargo_type, settlement)
    total_cost = price * quantity

    if caravan.silver < total_cost:
        return False

    caravan.cargo.append(CargoItem(
        cargo_type=cargo_type,
        quantity=quantity,
        buy_price_per_unit=price,
    ))
    caravan.silver -= total_cost
    return True

def sell_cargo(
    caravan: CaravanState,
    settlement: Settlement,
    season: Season,
    distance: int,
) -> int:
    """Sell all cargo at settlement. Returns silver gained"""
    total_silver = 0

    for item in caravan.cargo:
        sell_price = calculate_sell_price(item.cargo_type, settlement, season, distance)
        silver_gained = int(item.quantity * sell_price)
        total_silver += silver_gained

    caravan.silver += total_silver
    caravan.cargo = []
    return total_silver

def calculate_journey_cost(distance: int, season: Season) -> int:
    """Calculate wages and feed costs for a journey"""
    base_days = distance * TRAVEL_DAYS_PER_HEX

    # Winter adds 50% to travel time
    if season == Season.WINTER:
        base_days = int(base_days * 1.5)

    # 1 drover + 1 guard
    drover_cost = DROVER_WAGE * base_days * 0.01  # Convert copper to silver
    guard_cost = GUARD_WAGE * base_days * 0.01
    feed_cost = FEED_PER_ANIMAL * ANIMAL_COUNT * base_days * 0.01

    return int(drover_cost + guard_cost + feed_cost)

def apply_hazards(cargo_value: int) -> float:
    """Randomly apply hazard loss. Returns loss percentage"""
    roll = random.randint(1, 20)

    if roll <= 2:  # Significant loss (bandit, spoilage, etc)
        return 0.15
    elif roll <= 5:  # Moderate loss
        return 0.05
    elif roll <= 8:  # Minor loss
        return 0.02
    else:  # No loss
        return 0.0

# ============================================================================
# SIMULATION
# ============================================================================

def run_trade_cycle(
    caravan: CaravanState,
    settlements: List[Settlement],
    season: Season,
    distance_cache: DistanceMemo,
) -> Tuple[int, bool]:
    """
    Run one full trade cycle: pick route, buy cargo, travel, sell.
    Returns (profit, success)
    """
    # Pick destination (not too close, not too far)
    valid_destinations = [
        s for s in settlements
        if s != caravan.current_settlement
        and 3 <= distance_cache.get_distance(
            (caravan.current_settlement.hex_x, caravan.current_settlement.hex_y),
            (s.hex_x, s.hex_y)
        ) <= 20
    ]

    if not valid_destinations:
        return 0, False

    destination = random.choice(valid_destinations)
    distance = distance_cache.get_distance(
        (caravan.current_settlement.hex_x, caravan.current_settlement.hex_y),
        (destination.hex_x, destination.hex_y)
    )

    # Buy cargo (greedy: buy whatever is cheapest to sell at destination)
    cargo_to_buy = caravan.current_settlement.produces
    quantity = min(WAGON_CAPACITY, caravan.silver // calculate_buy_price(cargo_to_buy, caravan.current_settlement))

    if quantity == 0:
        return 0, False

    buy_cost = calculate_buy_price(cargo_to_buy, caravan.current_settlement) * quantity
    caravan.silver -= buy_cost
    caravan.cargo = [CargoItem(
        cargo_type=cargo_to_buy,
        quantity=quantity,
        buy_price_per_unit=calculate_buy_price(cargo_to_buy, caravan.current_settlement),
    )]

    # Travel
    journey_cost = calculate_journey_cost(distance, season)
    caravan.silver -= journey_cost

    if caravan.silver < 0:
        caravan.silver = 0
        return -buy_cost - journey_cost, False

    # Apply hazards
    loss_pct = apply_hazards(sum(item.quantity * item.buy_price_per_unit for item in caravan.cargo))
    hazard_loss = int(sum(item.quantity * item.buy_price_per_unit for item in caravan.cargo) * loss_pct)
    caravan.silver -= hazard_loss

    if hazard_loss > 0:
        # Reduce cargo quantity to reflect loss
        for item in caravan.cargo:
            lost_units = int(item.quantity * loss_pct)
            item.quantity -= lost_units

    # Sell cargo
    sell_value = sell_cargo(caravan, destination, season, distance)

    # Calculate profit
    profit = sell_value - buy_cost - journey_cost - hazard_loss

    caravan.current_settlement = destination
    caravan.total_profit += profit
    caravan.routes_completed += 1

    return profit, profit > 0

# ============================================================================
# MAIN SIMULATION
# ============================================================================

def run_year_simulation():
    """Run full year simulation"""
    print("=" * 80)
    print("FORBIDDEN LANDS TRADEROADS ECONOMIC VIABILITY SIMULATION")
    print("30x30 hex map, 20 settlements, 1 year (4 seasons)")
    print("=" * 80)
    print()

    # Setup
    random.seed(42)
    settlements = generate_settlements(30, 20)
    distance_cache = DistanceMemo()

    # Print settlement summary
    print(f"Generated {len(settlements)} settlements:")
    for s in settlements[:5]:
        print(f"  {s.name}: {s.size.name} at ({s.hex_x}, {s.hex_y}), "
              f"produces {s.produces.value}, needs {s.needs.value}")
    print(f"  ... and {len(settlements) - 5} more")
    print()

    # Initialize caravan
    caravan = CaravanState(
        name="The Wanderer's Trade Company",
        silver=500,
        current_settlement=random.choice(settlements),
    )

    print(f"Caravan: {caravan.name}")
    print(f"Starting settlement: {caravan.current_settlement.name}")
    print(f"Starting capital: {caravan.silver} silver")
    print()

    # Run year
    season_profits = {}

    for season in [Season.SPRING, Season.SUMMER, Season.AUTUMN, Season.WINTER]:
        print(f"\n{'='*80}")
        print(f"SEASON: {season.name}")
        print(f"{'='*80}")

        season_silver_start = caravan.silver
        season_routes = 0
        season_profit = 0
        successful_routes = 0

        # Each season: run ~3-4 trade cycles
        trades_per_season = random.randint(3, 4)

        for route in range(trades_per_season):
            if caravan.silver < 10:
                print(f"  Route {route+1}: FAILED - insufficie capital ({caravan.silver} silver)")
                break

            profit, success = run_trade_cycle(caravan, settlements, season, distance_cache)
            season_routes += 1
            season_profit += profit

            if success:
                successful_routes += 1
                status = "SUCCESS"
            else:
                status = "LOSS  "

            print(f"  Route {route+1}: {status} | Profit: {profit:+6d} silver | "
                  f"Capital: {caravan.silver:4d} | Destination: {caravan.current_settlement.name}")

        print(f"\nSeason summary: {successful_routes}/{season_routes} successful | "
              f"Profit: {season_profit:+6d} | Capital: {caravan.silver}")
        season_profits[season.name] = season_profit

    # Final report
    print(f"\n{'='*80}")
    print("ANNUAL SUMMARY")
    print(f"{'='*80}")
    print(f"Starting capital:     500 silver")
    print(f"Final capital:        {caravan.silver} silver")
    print(f"Total profit:         {caravan.total_profit:+d} silver ({(caravan.total_profit/500)*100:+.1f}%)")
    print(f"Routes completed:     {caravan.routes_completed}")
    print(f"Avg profit per route: {caravan.total_profit / max(caravan.routes_completed, 1):.0f} silver")
    print()
    print("Seasonal breakdown:")
    for season_name, profit in season_profits.items():
        print(f"  {season_name:10s}: {profit:+6d} silver")
    print()

    # Viability analysis
    print(f"{'='*80}")
    print("VIABILITY ANALYSIS")
    print(f"{'='*80}")

    # Benchmark: 20% annual return on capital is considered viable
    annual_return_pct = (caravan.total_profit / 500) * 100

    print(f"Annual ROI: {annual_return_pct:.1f}%")

    if annual_return_pct >= 20:
        print("✓ VIABLE: System produces sustainable profit margins")
    elif annual_return_pct >= 0:
        print("~ MARGINAL: System breaks even or barely profitable")
    else:
        print("✗ BROKEN: System produces losses")

    print()
    print(f"Per-route analysis:")
    avg_per_route = caravan.total_profit / max(caravan.routes_completed, 1)
    print(f"  Average profit per route: {avg_per_route:.0f} silver")
    print(f"  Route success rate: {(successful_routes/season_routes)*100:.0f}%" if season_routes > 0 else "  Route success rate: 0%")

    # Player-facing interpretation
    print()
    print(f"{'='*80}")
    print("PLAYER EXPERIENCE INTERPRETATION")
    print(f"{'='*80}")
    print(f"A player running caravans would:")
    if annual_return_pct >= 50:
        print("  → Become wealthy rapidly (viable as main income source)")
        print("  → Should take 2-3 months to fund a major stronghold upgrade")
    elif annual_return_pct >= 20:
        print("  → Build wealth steadily (viable as supplementary income)")
        print("  → Should take 4-6 months to fund a stronghold upgrade")
    elif annual_return_pct >= 0:
        print("  → Break even on trading (not worth doing unless story-required)")
        print("  → Would need to supplement with adventuring work")
    else:
        print("  → Lose money (trading is a money sink, not a business)")
        print("  → Would need major balance fixes to be worthwhile")

    return caravan

if __name__ == "__main__":
    run_year_simulation()
