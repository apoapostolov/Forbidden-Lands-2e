#!/usr/bin/env python3
"""
Sensitivity analysis: Traderoads with different starting capitals and caravan sizes
"""

import random
from traderoads_simulation import (
    run_trade_cycle, generate_settlements, CaravanState, Season, DistanceMemo
)

def run_sensitivity_analysis():
    """Test viability with different starting capitals and caravan sizes"""
    print("\n" + "=" * 80)
    print("TRADEROADS SENSITIVITY ANALYSIS")
    print("Testing different starting capitals and caravan sizes")
    print("=" * 80)
    print()

    # Reuse the same settlement map for consistency
    random.seed(42)
    settlements = generate_settlements(30, 20)
    distance_cache = DistanceMemo()

    starting_capitals = [250, 500, 1000, 2000]

    for start_capital in starting_capitals:
        print(f"\n{'-' * 80}")
        print(f"STARTING CAPITAL: {start_capital} silver")
        print(f"{'-' * 80}")

        caravan = CaravanState(
            name="Test Caravan",
            silver=start_capital,
            current_settlement=random.choice(settlements),
        )

        season_results = {}

        for season in [Season.SPRING, Season.SUMMER, Season.AUTUMN, Season.WINTER]:
            season_profit = 0
            season_routes = 0
            successful_routes = 0

            trades_per_season = 3

            for _ in range(trades_per_season):
                if caravan.silver < 10:
                    break

                profit, success = run_trade_cycle(caravan, settlements, season, distance_cache)
                season_routes += 1
                season_profit += profit

                if success:
                    successful_routes += 1

            if season_routes > 0:
                success_rate = (successful_routes / season_routes) * 100
                season_results[season.name] = (season_profit, season_routes, success_rate)

        # Results
        annual_return_pct = (caravan.total_profit / start_capital) * 100 if start_capital > 0 else 0

        print(f"Final capital:       {caravan.silver:4d} silver")
        print(f"Total profit:        {caravan.total_profit:+6d} silver")
        print(f"Annual ROI:          {annual_return_pct:6.1f}%")
        print(f"Routes completed:    {caravan.routes_completed}")

        print(f"\nSeasonal performance:")
        for season_name, (profit, routes, success_rate) in season_results.items():
            print(f"  {season_name:10s}: {profit:+6d} silver ({routes} routes, {success_rate:.0f}% success)")

        # Viability
        if annual_return_pct >= 50:
            viability = "EXCELLENT"
        elif annual_return_pct >= 20:
            viability = "GOOD"
        elif annual_return_pct >= 0:
            viability = "MINIMAL"
        else:
            viability = "FAILED"

        print(f"\nViability: {viability}")

        # Risk interpretation
        print(f"\nRisk profile:")
        if caravan.silver < 50:
            print(f"  ✗ BANKRUPT RISK: Capital depleted during year")
        elif caravan.silver < start_capital * 0.75:
            print(f"  ~ MODERATE RISK: Significant drawdowns possible")
        else:
            print(f"  ✓ LOW RISK: Steady capital growth")

if __name__ == "__main__":
    run_sensitivity_analysis()
