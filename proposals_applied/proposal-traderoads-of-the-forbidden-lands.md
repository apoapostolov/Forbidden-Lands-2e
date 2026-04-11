<!-- markdownlint-disable MD013 -->

# Proposal: Traderoads of the Forbidden Lands — Caravan Economic Subsystem

## Purpose

The Forbidden Lands manuscript has a working economy — silver and copper prices, supply rolls (Common/Uncommon/Rare/Extremely Rare), scarcity inflation, trade goods, and crafting. It has PATH OF THE CARAVAN, a five-rank Peddler talent that manages ledgers, caches, factors, and delivery networks. It has stronghold functions (MARKETPLACE, INN, ROAD, BRIDGE, PIER, TOLL HOUSE) that shape settlement economics. And it has a journey system that tracks quarter days, terrain, weather, and random encounters.

What it does not have is a caravan subsystem: the rules for assembling a trade expedition, loading cargo, choosing a route, selling at the destination, weathering hazards on the road, and measuring whether the venture turned a profit or a loss.

This proposal builds that subsystem. The goal is a full economic layer that makes trade a playable campaign activity — not a background abstraction, not a spreadsheet exercise, but a set of decisions that fit inside the existing quarter-day journey framework and create the same kind of tension as exploration, combat, and stronghold management.

## Design Principles

- **Quarter-day native.** Caravan travel uses the same quarter-day action economy as Chapter 8 journeys. Loading, unloading, selling, and resolving hazards are quarter-day activities.
- **Silver economy.** All prices, costs, margins, and payments use the existing silver/copper system from Chapter 10. No new currency, no abstract "trade points."
- **Risk-reward loop.** Every trade route is a gamble: silver invested in cargo, time spent traveling, hazards on the road, and unknown demand at the destination. Profit is not guaranteed. The system should make players weigh whether a run is worth it.
- **Reputation-integrated.** Trade builds reputation. A caravan that delivers reliably grows its name along the route. That name translates into better prices, safer roads, and access to premium goods.
- **Compatible with PATH OF THE CARAVAN.** The talent's five ranks plug directly into this subsystem. Rank 1-2 characters handle small personal trade. Rank 3-5 characters run proper caravans with factors, heavy goods, and masterwork commissions. The subsystem gives the talent a world to operate in.
- **Compatible with Chapter 12.** Mercenary bands can escort caravans (Escort contracts). Caravans can hire protection, and the cost should align with Chapter 12 pay scales. Caravan routes can generate bounty opportunities (bandit lairs along the road, rival merchants posting recovery bounties).
- **Scalable.** A single peddler with a mule and two sacks of salt is a caravan of one. A ten-wagon train with guards, factors, and a rotation of trade goods is a caravan of scale. The same rules should cover both, with complexity gating by investment and PATH OF THE CARAVAN rank.

## Integration Points

| Existing System            | Location  | How This Proposal Connects                                                        |
| -------------------------- | --------- | --------------------------------------------------------------------------------- |
| Economy & Prices           | Ch 10     | All cargo values, costs, and margins derive from Ch 10 prices                     |
| Supply Rolls               | Ch 10     | Supply determines what is available to buy and what the destination wants         |
| Trade Goods Table          | Ch 10     | Cargo types map directly to existing trade goods                                  |
| PATH OF THE CARAVAN        | Ch 4      | Talent ranks gate caravan capabilities                                            |
| PATH OF TREASURE           | Ch 4      | Synergy with appraisal, supply manipulation, and premium sales                    |
| PATH OF WORDS              | Ch 4      | Synergy with negotiation, contract sealing, rumor evaluation                      |
| Journey Rules              | Ch 8      | Caravan travel uses the same quarter-day, terrain, and weather system             |
| Reputation & Standing      | Ch 8      | Trade builds Caravan Circle reputation; settlements recognize reliable traders    |
| Rumors                     | Ch 8      | Trade-route rumors carry economic intelligence (prices, demand, hazards)          |
| Stronghold Functions       | Ch 9      | MARKETPLACE, INN, ROAD, BRIDGE, PIER, TOLL HOUSE, STABLE shape caravan operations |
| Contracts & Bounties       | Ch 12     | Escort contracts, caravan guard pay, recovery bounties for stolen cargo           |
| Villages & Rumors proposal | Proposals | ASK AROUND for trade rumors; Notice Board for escort/delivery work                |

---

## 1. The Caravan

### What Is a Caravan?

A caravan is any organized trade expedition that moves goods between settlements for profit. It has three components:

1. **Transport** — the animals and vehicles that carry the cargo
2. **Cargo** — the goods being moved
3. **People** — the traders, guards, drovers, and factors who make it work

A single peddler with a pack mule counts. So does a six-wagon train with a mounted escort. The system scales by investment.

### Transport

Caravan capacity is measured in **load units**. One load unit equals approximately 10 Normal-weight items (100 units of weight using the existing weight system). Animals and vehicles have load capacities:

| Transport   | Load Capacity | Speed                                       | Cost       | Terrain Limits              | Notes                                                            |
| ----------- | ------------- | ------------------------------------------- | ---------- | --------------------------- | ---------------------------------------------------------------- |
| Pack mule   | 2             | Normal                                      | 25 silver  | All terrain                 | Reliable, cheap. Can go where wagons cannot.                     |
| Pack horse  | 3             | Normal                                      | 40 silver  | All terrain                 | Faster unburdened, same speed loaded                             |
| Donkey      | 1             | Slow (-1 hex/day)                           | 10 silver  | All terrain                 | Cheap, stubborn, eats less                                       |
| Ox cart     | 6             | Slow (-1 hex/day)                           | 60 silver  | Roads, plains, light forest | Cheap and strong. Cannot cross marsh, mountain, or dense forest. |
| Horse wagon | 8             | Normal                                      | 120 silver | Roads, plains, light forest | Standard trade wagon. Needs maintained road for full speed.      |
| River barge | 20            | Fast (+1 hex/day downstream, slow upstream) | 200 silver | Rivers only                 | High capacity but route-locked. Requires PIER to load/unload.    |
| Heavy wagon | 12            | Slow (-1 hex/day)                           | 200 silver | Roads only                  | Maximum land capacity. Cannot leave maintained roads.            |

**Terrain and speed.** Road-dependent transport (wagons, heavy wagons) travels at listed speed on roads and halves speed on trails. Off-road, they cannot move at all without spending a full quarter day per hex clearing path. Mules and horses handle all terrain at listed speed. River barges are route-locked but move fast downstream.

**Maintenance.** Animals require FOOD and WATER as living creatures. Vehicles require occasional repair — treat as a crafting check using Carpentry or Smithing, difficulty 1, after every 10 days of road travel or after any damage event.

### People

A caravan needs people to function:

| Role               | Function                                                          | Pay                          | Notes                                                                   |
| ------------------ | ----------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------- |
| **Caravan master** | Leads the expedition, makes route decisions, handles sales        | —                            | Usually a PC. If NPC, 2 silver/day.                                     |
| **Drover**         | Handles animals and vehicles, loads/unloads cargo, maintains gear | 5 copper/day                 | One per 2 wagons or 4 pack animals                                      |
| **Guard**          | Protects the caravan from threats                                 | 1 silver/day                 | Chapter 12 pay rates for mercenary escort apply to larger guard forces  |
| **Factor**         | Manages trade at the destination, negotiates with buyers          | 1 silver/day + 5% of profits | Requires PATH OF THE CARAVAN Rank 3 or a hired NPC with MANIPULATION 3+ |
| **Scout**          | Rides ahead, watches for hazards, finds campsites                 | 1 silver/day                 | Uses SCOUTING for advance warning of encounters                         |

A minimal caravan (one PC with a pack mule) needs no additional people. A standard trade caravan (2-4 wagons) needs 1-2 drovers and 1-2 guards. A large caravan (6+ wagons) needs a full complement: factors, scouts, multiple drovers, and a proper guard force.

**Wages.** Caravan employees are paid daily. Unpaid employees leave after 1D6 days, taking whatever they can carry. Wages come out of the caravan's operating fund, not the profit calculation. This matters: a caravan that travels slowly spends more on wages and leaves less room for profit.

---

## 2. Cargo and Loading

### Cargo Types

Cargo divides into categories based on origin, value density, and handling requirements:

| Category           | Examples                                           | Buy Price (per load unit) | Typical Margin | Weight per Load   | Notes                                                                  |
| ------------------ | -------------------------------------------------- | ------------------------- | -------------- | ----------------- | ---------------------------------------------------------------------- |
| **Bulk staples**   | Grain, salt, dried fish, firewood, raw wool        | 5-15 silver               | 20-40%         | Heavy, stable     | Low risk, low reward. Always in demand.                                |
| **Craft goods**    | Cloth, leather, iron tools, rope, candles, pottery | 15-40 silver              | 30-60%         | Normal            | Moderate value. Demand varies by settlement.                           |
| **Luxury goods**   | Wine, spices, dyes, fine cloth, glassware, incense | 40-100 silver             | 50-100%        | Light, fragile    | High value. Fragile — breakage risk on rough roads.                    |
| **Raw materials**  | Iron ore, timber, stone, pelts, tallow, herbs      | 10-30 silver              | 20-50%         | Heavy             | Demand driven by settlements with FORGE, TANNERY, etc.                 |
| **Arms and armor** | Weapons, shields, helmets, mail                    | 30-80 silver              | 40-80%         | Heavy, regulated  | Some settlements restrict arms trade. Requires PATH OF THE CARAVAN R4. |
| **Specialty**      | Medicine, alchemical ingredients, books, relics    | 50-200 silver             | 60-150%        | Light             | Extremely Rare supply. Only available in specific locations.           |
| **Livestock**      | Cattle, sheep, goats, horses, draft animals        | 20-60 silver per head     | 30-70%         | Self-transporting | Walk themselves but require feed and water. Vulnerable to predators.   |

### Loading

Loading a caravan is a quarter-day activity. One character supervises the loading and makes a CRAFTING roll (no talent required — this is basic logistics).

| ⚔️    | Outcome                                                                                                                                             |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| No ⚔️ | Loaded, but poorly secured. First rough terrain hex or hazard event causes 1D6 silver of cargo damage (shifted loads, broken goods, spilled grain). |
| 1 ⚔️  | Loaded adequately. No bonus, no penalty.                                                                                                            |
| 2 ⚔️  | Well loaded. The first cargo damage event of the journey is ignored — the lashing held.                                                             |
| 3+ ⚔️ | Expertly loaded. As above, plus available load capacity increases by 10% (rounded up) due to efficient packing.                                     |

PATH OF THE ARTISAN provides relevant bonuses to this roll. PATH OF THE CARAVAN R2+ characters automatically succeed at 1 ⚔️ and roll for better results.

### Perishability

Some cargo spoils. Grain lasts indefinitely if kept dry. Fresh fish lasts 2-3 days. Wine survives anything short of breakage. Herbs lose potency after a week in heat.

The GM should track perishability only for time-sensitive goods. As a general rule:

| Cargo Type              | Shelf Life on the Road                 | Risk                                              |
| ----------------------- | -------------------------------------- | ------------------------------------------------- |
| Dry bulk staples        | Indefinite                             | Water damage (rain, river crossing)               |
| Fresh food, dairy, meat | 2-3 days, 5-7 in cold weather          | Spoilage (total loss if not sold in time)         |
| Herbs, reagents         | 5-10 days                              | Potency loss (sell price halves after shelf life) |
| Wine, oil, glassware    | Indefinite                             | Breakage (fragile — roll on rough terrain)        |
| Livestock               | Indefinite (self-feeding in grassland) | Predators, disease, stampede                      |

### Fragile Cargo

Luxury goods and glassware are fragile. When the caravan crosses rough terrain (marsh, mountain, dense forest) or suffers a hazard event, fragile cargo must pass a breakage check: roll 1D6 per load unit of fragile cargo. On a 1, that load unit takes 25% damage (round up in silver). On a 1-2 if the terrain is mountain or worse.

Good lashing (loading roll 2+ ⚔️) negates the first breakage check of the journey. PATH OF THE CARAVAN R4 allows the caravan master to designate one load unit of fragile cargo as "personally secured," exempting it from breakage checks entirely.

---

## 3. Regional Trade and Supply

### The Core Trade Mechanic

Trade profit comes from arbitrage: buying where goods are cheap (high supply, low demand) and selling where they are expensive (low supply, high demand). The Forbidden Lands' existing Supply system already contains this logic — a Common item in one settlement might be Uncommon or Rare in another.

The fundamental trade rule:

> **Buy at origin price. Sell at destination price. The difference is your margin — minus travel costs, wages, hazards, and tolls.**

### Settlement Trade Profiles

Each settlement has a trade profile — what it produces (cheap to buy) and what it needs (expensive to sell). The GM assigns or generates these profiles based on the settlement's geography, size, and stronghold functions.

| Settlement Feature   | Produces (Common supply, low price)       | Needs (Uncommon+ supply, high price)                             |
| -------------------- | ----------------------------------------- | ---------------------------------------------------------------- |
| Farmland/plains      | Grain, wool, livestock, hay               | Iron tools, weapons, salt, cloth, luxury goods                   |
| Forest settlement    | Timber, pelts, charcoal, herbs            | Grain, iron, salt, weapons, craft goods                          |
| Mining town          | Iron ore, stone, gems (rare)              | Food, cloth, timber, medicine, luxury goods                      |
| River/coastal        | Fish, rope, river trade, barge access     | Timber, iron, livestock, inland goods                            |
| Trade crossroads     | Diverse imported goods (variable)         | Nothing specific — but buys intel, services, and specialty goods |
| Temple/shrine        | Books, incense, medicine, religious goods | Food, building materials, arms (if militant order)               |
| Fortified stronghold | Arms, armor, military services            | Food, luxury goods, craft goods, raw materials                   |

**Price multipliers by supply:**

| Supply at Destination                             | Sell Price Multiplier                            |
| ------------------------------------------------- | ------------------------------------------------ |
| Common (the destination produces it too)          | x0.5 (sell at a loss — oversupply)               |
| Common (neutral — neither produces nor needs)     | x1.0 (break even on goods, lose on travel costs) |
| Uncommon (modest demand)                          | x1.5                                             |
| Rare (strong demand)                              | x2.0                                             |
| Extremely Rare (desperate demand or unique goods) | x2.5-3.0                                         |

These multipliers apply to the buy price at origin. The GM adjusts by local conditions — a famine settlement might pay x3.0 for grain even though grain is normally Common. Winter scarcity (see Chapter 12) applies to trade goods as much as to work contracts.

### Trade Rumors

When a character uses ASK AROUND (from the Villages and Rumors proposal) at a settlement with a MARKETPLACE or among caravan folk, trade rumors are available. A successful roll reveals one or more of:

- **Demand rumor:** "Ironmere is desperate for salt — their mine salt ran out last season." (Indicates Rare supply at a specific settlement, suggesting high sell price.)
- **Supply rumor:** "The elves at Green Dale are selling pelts cheap — too many and not enough takers." (Indicates Common supply at origin, suggesting low buy price.)
- **Hazard rumor:** "Bandits on the Stillmire road took a wagon last tenday." (Indicates a specific route is dangerous.)
- **Price rumor:** "Spices out of the Amber Crossing are going for double since the pass closed." (Indicates price spike at a specific location.)
- **Competition rumor:** "Three caravans already left for Hollowford this week." (Indicates the destination market may be saturated by arrival time.)

Trade rumors travel along caravan routes at the speed described in Chapter 8 (10+ hexes per season along well-traveled routes). They are only as current as the last trader who passed through.

---

## 4. Route Planning and Travel

### Choosing a Route

Before departure, the caravan master chooses a route. This is a planning decision, not a roll — the players look at the map and decide.

Key route factors:

| Factor              | Effect                                                                                                                                       |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Distance**        | More hexes = more days = more wages, feed, and exposure to hazards                                                                           |
| **Terrain**         | Road: full speed. Trail: half speed for wagons. Off-road: pack animals only.                                                                 |
| **Season**          | Winter: +50% travel time, feed costs double, hazard frequency increases. Spring thaw: rivers flood, fords close, barges run fast.            |
| **Known hazards**   | Bandit lairs, monster territories, toll stations, hostile settlements                                                                        |
| **Tolls**           | Settlements with TOLL HOUSE charge per wagon (1-3 silver) or per load unit (1 silver). Safe passage through hostile territory may cost more. |
| **Water and feed**  | River routes provide water. Grassland provides grazing. Desert and mountain require carried supplies.                                        |
| **ROAD and BRIDGE** | Stronghold-built ROAD reduces travel time by 1 quarter day per 2 hexes. BRIDGE eliminates river-crossing delays and risks.                   |

### Caravan Travel

Caravan travel follows the Chapter 8 journey rules with these modifications:

**Movement rate.** A caravan moves at the speed of its slowest transport. A wagon caravan on a road moves 2 hexes per day (one hex per hiking quarter day). Pack mule caravans may move slightly faster on good terrain but cannot exceed 3 hexes per day.

**Lead time.** A caravan with a scout can detect hazards one hex ahead. The scout spends a quarter day riding forward and returns with information. This uses the SCOUTING skill against the terrain's base difficulty (Chapter 8).

**Camp.** Caravans follow the standard Make Camp procedure. A large caravan (4+ wagons) requires extra camp setup — one quarter day instead of one action. The camp is larger, louder, and easier to find. Random encounter checks gain +1 to the hazard die while the caravan is camped.

**March order.** Before travel begins each day, the caravan master sets march order: scouts forward, cargo wagons in the middle, guards distributed. March order matters when ambush or terrain events occur. The GM uses it to determine who is exposed first.

### River Travel

A caravan with a river barge (or hired barge at 5 silver/day) can move along navigable rivers at enhanced speed. Downstream travel gains +1 hex/day. Upstream travel suffers -1 hex/day.

River travel avoids most land-based hazard encounters (no bandits, no difficult terrain, no road tolls) but introduces its own: rapids (CRAFTING or lose cargo), river piracy, grounding in low water, and portage at waterfalls or rapids.

**Loading a barge** requires a PIER function at both origin and destination, or a half-day of improvised loading at a riverbank (risk of cargo damage: roll 1D6 per load unit, cargo damage on a 1).

---

## 5. Selling Cargo — The Market Procedure

### Arrival at the Destination

When the caravan arrives at a destination settlement, the caravan master must sell the cargo. This is not automatic — it is a procedure that takes time and skill.

### The Market Roll

Selling cargo is a quarter-day activity. The caravan master (or a factor acting on their behalf) makes a MANIPULATION roll to represent the selling process: finding buyers, negotiating terms, displaying quality, and closing deals.

**Difficulty** is set by the volume and type of cargo being sold:

| Volume                                  | Difficulty |
| --------------------------------------- | ---------- |
| 1-2 load units (small trade)            | 1          |
| 3-5 load units (standard caravan)       | 2          |
| 6-10 load units (large caravan)         | 3          |
| 11+ load units (major trade expedition) | 4          |

**Modifiers:**

| Factor                                                                      | Modifier |
| --------------------------------------------------------------------------- | -------- |
| Destination has a MARKETPLACE                                               | +1       |
| Destination has an INN (buyers gather there)                                | +1       |
| Caravan master has PATH OF TREASURE R2+                                     | +1       |
| Caravan master has PATH OF WORDS R3+ (seal the bargain)                     | +1       |
| Fellowship has local Standing +2 or higher                                  | +1       |
| Cargo matches a known demand (Rare or Extremely Rare supply at destination) | +1       |
| Cargo is Common supply at destination (oversupplied)                        | -2       |
| Market recently saturated (3+ caravans arrived this season)                 | -1       |
| Winter (reduced economic activity)                                          | -1       |
| Fellowship has local Standing -1 or lower                                   | -1       |

**Results:**

| ⚔️    | Outcome                                                                                                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| No ⚔️ | Poor sale. Sell at x0.75 of the calculated destination price. Buyers sense desperation or the goods do not match local need.                                                                                             |
| 1 ⚔️  | Fair sale. Sell at x1.0 of the calculated destination price. Standard market rate.                                                                                                                                       |
| 2 ⚔️  | Good sale. Sell at x1.25. The caravan master found the right buyer or timed the pitch well.                                                                                                                              |
| 3+ ⚔️ | Excellent sale. Sell at x1.5. Premium buyer, bidding war, or perfectly timed delivery. The caravan master may also establish a **standing order** — the buyer wants the same goods next season at guaranteed x1.25 rate. |

**Standing orders.** A standing order is a guaranteed sale at the destination for a specific cargo type at x1.25 price, valid for one season. The caravan must deliver within the season or the order lapses. Standing orders reduce risk — you know what will sell — but lock the caravan into a route. PATH OF THE CARAVAN R3+ characters can hold up to 3 standing orders simultaneously across different settlements.

### Unsold Cargo

If the caravan cannot sell all its cargo (no swords, destination oversupplied, or insufficient buying power), the remainder can be:

- **Stored** at the destination (requires warehouse space — 1 silver per load unit per week, or free if the fellowship owns a stronghold with storage).
- **Carried onward** to the next destination, consuming load capacity and extending the journey.
- **Sold at loss** (x0.5 price) to a bulk buyer or barter agent.
- **Donated** to the settlement for Standing benefit (+1 Standing per 20 silver of goods donated).

---

## 6. Profit and Loss

### The Accounting

At the end of a trade run, the caravan master calculates profit:

```text
PROFIT = Sale Revenue - (Cargo Cost + Wages + Feed + Tolls + Repairs + Losses)
```

| Cost Category  | Calculation                                                        |
| -------------- | ------------------------------------------------------------------ |
| **Cargo cost** | Buy price × load units purchased                                   |
| **Wages**      | Daily rate × number of employees × days traveled                   |
| **Feed**       | 1 copper/day per pack animal or draft animal (waived in grassland) |
| **Tolls**      | Per wagon/load unit at each TOLL HOUSE on the route                |
| **Repairs**    | Crafting rolls and material costs for vehicle damage               |
| **Losses**     | Cargo lost to breakage, spoilage, theft, or hazard                 |

### Margin Benchmarks

Not every run needs to be profitable. Some runs build reputation, establish routes, or secure standing orders. But as a benchmark:

| Profit Margin | Verdict                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negative      | Loss. The caravan spent more than it earned. Common on first runs, long routes, or hazard-heavy trips.                                                   |
| 0-20%         | Break-even. Covered costs but barely worth the time. Acceptable for route establishment.                                                                 |
| 20-40%        | Modest profit. A living wage for the peddler and crew. The standard for short, safe routes.                                                              |
| 40-60%        | Good profit. The run was well-planned and well-sold. Enough to reinvest in a second wagon.                                                               |
| 60-100%       | Excellent profit. Rare — requires high-demand goods, low competition, or a premium sale.                                                                 |
| 100%+         | Windfall. Only possible with specialty goods sold at Extremely Rare prices, war-driven demand, or arbitrage of information the market does not yet have. |

### Reinvestment

Profit flows back into the system:

- **More transport.** Buy additional animals or wagons to increase capacity.
- **Better guards.** Hire higher-tier fighters or a proper escort.
- **Route expansion.** Explore new markets, establish new standing orders.
- **Stronghold investment.** Fund MARKETPLACE, ROAD, BRIDGE, or STABLE functions that improve future trade.
- **Reputation spending.** Use profit to buy Reputation (feast, donation, sponsorship) per the Villages and Rumors proposal.

---

## 7. Hazards on the Road

### Caravan Hazard Table

Each day of caravan travel, the GM rolls for hazards using the standard journey encounter rules (Chapter 8), with the following caravan-specific additions:

When a hazard result occurs, roll D66 on the Caravan Hazard Table:

| D66   | Hazard                       | Effect                                                                                                                                                                                            |
| ----- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 11-12 | **Road damage**              | Broken axle, washed-out ford, fallen tree. Lose one quarter day. CRAFTING roll to repair; failure adds another quarter day.                                                                       |
| 13-14 | **Spoilage**                 | Weather or road conditions damage perishable cargo. Lose 1D6 silver per load unit of perishable goods.                                                                                            |
| 15-16 | **Animal trouble**           | Lame mule, bolting horse, ox refuses a ford. Lose half a quarter day. ANIMAL HANDLING roll to resolve; failure means the animal is out for the day.                                               |
| 21-22 | **Toll dispute**             | Unexpected toll or increased rate at a crossing. Pay 1D6 silver per wagon or MANIPULATION to negotiate. Failure means double toll or denied passage.                                              |
| 23-24 | **Breakage**                 | Rough terrain damages fragile cargo. Breakage check for all fragile load units.                                                                                                                   |
| 25-26 | **Bad weather**              | Storm, fog, or downpour. Lose one quarter day. Drafts and open cargo take water damage (1D6 silver loss per unsheltered load unit).                                                               |
| 31-32 | **Theft**                    | Pilferage at camp or during a stop. Lose 2D6 silver worth of small goods unless a guard was posted (SCOUTING roll to detect the thief).                                                           |
| 33-34 | **Rival caravan**            | Another caravan is heading to the same destination with similar goods. When you arrive, the market is -1 modifier to the Market Roll.                                                             |
| 35-36 | **Bandit scouts**            | Riders observed watching the caravan from a distance. Possible ambush ahead. SCOUTING roll to detect their number and position.                                                                   |
| 41-42 | **Bandit ambush**            | Armed attack on the caravan. Use combat rules. Bandits target cargo first: if they break through the guard line, they cut loose 1D6 load units and retreat.                                       |
| 43-44 | **Predators**                | Wolves, bears, or worse. Target livestock first, then work animals. ANIMAL HANDLING to control draft animals during the attack.                                                                   |
| 45-46 | **Bridge out**               | A bridge marked on the map is damaged or gone. Detour adds 1D6 quarter days, or CRAFTING roll to improvise a crossing (failure means cargo damage).                                               |
| 51-52 | **Illness**                  | Disease hits an employee or animal. They cannot work for 1D6 days. HEALING roll to shorten recovery.                                                                                              |
| 53-54 | **Terrain obstacle**         | Rockslide, fallen tree, flooded ford, frozen pass. Choose: detour (1D6 quarter days) or clear (1 quarter day + MIGHT roll; failure is 2 quarter days).                                            |
| 55-56 | **Extortion**                | A local warlord, bandit chief, or hostile settlement demands payment for passage. 2D6 silver per wagon, or fight.                                                                                 |
| 61-62 | **Customs inspection**       | A settlement or patrol demands to inspect the cargo. Legal goods pass; restricted goods (arms in some territories, contraband) may be confiscated or fined.                                       |
| 63-64 | **Wheel or harness failure** | A vehicle breaks down in transit. CRAFTING roll to field-repair. Failure means the vehicle is immobile until a proper repair (half day + materials).                                              |
| 65-66 | **Opportunity**              | A traveler, refugee, or stranded merchant on the road. They offer goods at bargain prices, information about the route ahead, or a delivery contract worth 1D6 x 5 silver at the next settlement. |

### Hazard Frequency

Standard journey encounter rules apply. Additionally:

- **Larger caravans attract more attention.** Caravans of 4+ wagons add +1 to the encounter die. Caravans of 8+ wagons add +2.
- **Guarded caravans deter some threats.** A caravan with 3+ visible guards reduces bandit ambush and extortion results by -11 on the D66 (re-roll those results as the next entry down the table). Bandits prefer easier targets.
- **Season matters.** Winter adds +1 to weather-related hazard frequency. Summer reduces animal trouble frequency (-1 to related rolls).

---

## 8. Caravan Reputation

### Trade Circles

Chapter 8 describes Circles of Reputation — caravan folk, smiths, ferrymen, etc. — and notes they use the same system as Settlement Reputation. This proposal formalizes the **Caravan Circle** as a specific tracked circle for any fellowship that engages in regular trade.

Caravan Circle Reputation is a single score (0-11+) that represents how well known the fellowship is among traders, merchants, factors, innkeepers, toll-keepers, and caravan masters along the routes they travel.

| Caravan Rep | Meaning                                                                   |
| ----------- | ------------------------------------------------------------------------- |
| 0           | Unknown trader. No history, no name.                                      |
| 1-2         | A few factors or innkeepers have heard the name.                          |
| 3-4         | Known along one or two routes. Established among local traders.           |
| 5-6         | Reliable reputation across a region. Standing orders available.           |
| 7-8         | Strong trade name. Premium access at major markets. Factors seek you out. |
| 9-10        | Major trade presence. Your caravan's arrival is news. Markets adjust.     |
| 11+         | Legendary trader. Settlements compete for your route.                     |

### Growing Caravan Reputation

| Action                                                        | Reputation Effect                                                      |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Complete a trade run at profit                                | +1 at destination settlement (Caravan Circle)                          |
| Fulfill a standing order on time                              | +1 at that settlement (Caravan Circle)                                 |
| Deliver goods during a crisis (famine, siege, plague)         | +1 to +2 at that settlement (Caravan Circle and Settlement Reputation) |
| Protect the route (clear bandits, repair bridges, mark roads) | +1 along the route (all settlements within 2 hexes)                    |
| Donate goods or fund a MARKETPLACE or INN                     | +1 Settlement Standing and Caravan Circle                              |
| Cheat, short-change, or deliver spoiled goods                 | -1 to -2 Caravan Circle and Standing at that settlement                |
| Abandon a standing order                                      | -1 Caravan Circle at that settlement                                   |
| Cargo stolen and not recovered                                | -1 Caravan Circle (reputation for vulnerability)                       |

### Caravan Reputation Benefits

| Caravan Rep | Benefit                                                                                                                                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 3+          | Trade rumors from ASK AROUND gain +1 modifier when the character mentions their caravan name.                                                                                                                                  |
| 5+          | Standing orders are available without needing a 3+ ⚔️ Market Roll. Factors and merchants approach the caravan master with offers.                                                                                              |
| 7+          | Buy price at regular origin settlements reduced by 10% (volume discount — suppliers want to keep the account). Sell price at regular destination settlements increased by 10% (premium buyer — they trust the quality).        |
| 9+          | Safe passage. Settlements along established routes maintain the road, warn of hazards, and refuse to harbor bandits who target the caravan. Equivalent to +1 Standing at every settlement within 2 hexes of the regular route. |

---

## 9. Seasonal Economics

### The Yearly Cycle

The Forbidden Lands economy is not static. Demand, supply, risk, and profit all shift with the seasons. The caravan master who understands the cycle has an edge — and the one who ignores it pays with empty wagons and dead mules.

| Season     | Economic Character                                                                         | Effect on Trade                                                                                                                                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Spring** | Recovery and planting. Rivers flood, roads thaw, villages reopen.                          | Grain demand peaks (spring hunger). River routes reopen. Road conditions poor — muddy trails, washed fords. Fresh trade goods from winter stores commanded premium prices.                                                                        |
| **Summer** | Growth and travel. Roads dry, caravans move freely, markets active.                        | Best travel conditions. Competition highest — more caravans on the road. Prices normalize. Livestock trade peaks (grazing season).                                                                                                                |
| **Autumn** | Harvest and preparation. Grain floods the market, villages stock for winter.               | Grain prices lowest (harvest glut). Raw material demand peaks (building before winter). Luxury goods demand rises (festivals, preparation for winter isolation). Last safe window for long routes.                                                |
| **Winter** | Contraction and scarcity. Snow closes passes, rivers freeze or flood, villages shut gates. | Travel costs +50%. Food and feed costs double. Many routes impassable. Prices for all goods spike at isolated settlements. Short routes between nearby settlements are still viable. The bold or desperate trader profits most — if they survive. |

### Seasonal Price Multipliers

Apply these to the base sell price after the supply multiplier:

| Good Type      | Spring | Summer | Autumn | Winter |
| -------------- | ------ | ------ | ------ | ------ |
| Grain and food | x1.5   | x1.0   | x0.75  | x2.0   |
| Raw materials  | x1.0   | x1.0   | x1.25  | x0.75  |
| Craft goods    | x1.0   | x1.0   | x1.0   | x1.25  |
| Luxury goods   | x1.0   | x1.0   | x1.25  | x1.5   |
| Arms and armor | x1.0   | x1.0   | x1.25  | x1.0   |
| Livestock      | x1.25  | x1.0   | x0.75  | x1.5   |
| Medicine/herbs | x1.0   | x0.75  | x1.0   | x1.5   |

These stack with the supply multiplier. Grain that is Rare at a winter settlement sells at x2.0 (supply) × x2.0 (winter) = x4.0 base price. That is how fortunes are made — and why bandits patrol the winter roads.

---

## 10. Return Contracts and Passengers

### The Empty Wagon Problem

A caravan that sells its cargo at the destination faces a choice: return empty (sunk cost — wages and feed paid with no revenue), buy return cargo (investment risk — new capital required), or find a return contract (paid work for the trip home).

### Return Contracts

| Contract Type          | Description                                                                                      | Typical Pay                      | Source                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------- | ------------------------------------------------------ |
| **Freight**            | Carry goods from destination back to origin (or to a third settlement)                           | 1-3 silver per load unit per day | Merchants, factors, settlement authority               |
| **Mail and messages**  | Carry sealed letters, packages, or tokens                                                        | 1-5 silver per message           | Anyone. More valuable for distant or dangerous routes. |
| **Passengers**         | Escort a person or small group along the route                                                   | 2-5 silver per person per day    | Travelers, pilgrims, officials, refugees               |
| **Specialty delivery** | Carry a specific item that requires careful handling (fragile, perishable, dangerous, or secret) | 5-20 silver, sometimes more      | Private clients, temples, guilds                       |

Return contracts are found through ASK AROUND or SEEK WORK at the destination. A settlement with a MARKETPLACE or INN always has at least one return contract available. Smaller settlements may have none unless a specific NPC has need.

**Passenger rules.** Passengers occupy one load unit of space each (they need room for their belongings and a place to sit or ride). They bring their own food or pay the caravan 5 copper/day for meals. Passengers are non-combatants unless otherwise stated — they add mouths but not swords.

### Delivery Contracts as Hooks

Return contracts double as adventure hooks. The sealed letter is from a conspirator. The passenger is a fugitive. The specialty cargo is cursed, stolen, or alive. The freight contains hidden contraband that a customs inspection (hazard 61-62) will discover.

The GM should treat at least one return contract per season as a potential complication. The caravan master who takes every job without asking questions eventually carries something that brings trouble.

---

## 11. Integration with PATH OF THE CARAVAN

The PATH OF THE CARAVAN talent (Chapter 4, The Peddler's Talents) is designed for a world where this subsystem exists. Here is how each rank interacts:

| Rank   | Talent Ability                                                                           | Subsystem Interaction                                                                                                                                                                                                                                                                                                                  |
| ------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R1** | Spend WP to deliver trade goods worth up to 1 silver/WP from your ledger                 | Suitable for personal-scale trade. No caravan assembly needed. The "ledger" is a pre-purchased inventory that arrives by narrative means. Goods count as cargo if added to a caravan.                                                                                                                                                  |
| **R2** | Extend to weapons, 1D6 silver/WP. Establish a caravan cache.                             | The cache is the caravan's home base — a warehouse at a trading post where cargo is stored between runs. Costs 2D6×10 silver to establish (minus 2D6 per WP spent + a day of manual labor). The cache holds up to 20 load units.                                                                                                       |
| **R3** | Each WP frees 2D6 silver of goods. Assign trusted factors. Passive income. Mishap rolls. | Factors can manage a caravan leg without the PC present. The auto-trade uses the Market Roll at reduced skill (factor's MANIPULATION, typically 3 dice). Mishap rolls as described in the talent: lose 1D6 silver of goods per ☠️ per day absent. The caravan subsystem's hazard table replaces generic "mishap" with specific events. |
| **R4** | Network covers HEAVY items, armor, shields, tools, raw materials.                        | Unlocks the Arms and Armor cargo category and the Raw Materials category at full value. Pre-R4 caravans can carry these physically but cannot leverage the PATH OF THE CARAVAN talent discount or delivery network for them.                                                                                                           |
| **R5** | Masterwork designation or double purchasing power.                                       | Masterwork goods sell at +50% over standard price (specialty-tier). Double purchasing power allows WP to cover 4D6 silver per point, enabling high-value trade in luxury and specialty goods without full cash investment.                                                                                                             |

### Characters Without the Talent

A character without PATH OF THE CARAVAN can still run a caravan. The talent is not a gate — it is a force multiplier. Without it:

- No ledger deliveries (must carry everything physically)
- No caravan cache (must store goods at strongholds or rented warehouses)
- No factor management (the PC must be present for all trade)
- No arms/armor trade bonuses (can carry but not leverage the network)
- No masterwork or doubled WP purchasing

The non-talented trader makes money by the market procedure, route knowledge, and the willingness to haul cargo personally. The talented trader makes money by all of those plus supply-chain leverage.

---

## 12. Stronghold Functions and Trade

### Infrastructure Investment

Stronghold functions create lasting trade advantages. A fellowship that invests in infrastructure improves every future trade run along the routes those functions touch.

| Function                     | Trade Benefit                                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MARKETPLACE**              | +1 to all Market Rolls at this stronghold. Attracts NPC caravans (passive income: 1D6 silver per week if staffed).                                                           |
| **INN**                      | +1 to Market Rolls (buyers gather). Generates trade rumors. Attracts travelers and return contract opportunities.                                                            |
| **ROAD**                     | Reduces travel time on connected route by 1 quarter day per 2 hexes. Makes the route wagon-accessible.                                                                       |
| **BRIDGE**                   | Eliminates river-crossing hazards and delays on the route.                                                                                                                   |
| **PIER**                     | Required for barge loading/unloading. Opens river trade. Each pier connected to another pier creates a high-speed trade lane.                                                |
| **TOLL HOUSE**               | Generates passive income from NPC caravan traffic (1D6 silver per week if the road sees regular use). Provides traffic intelligence (who passed through, what they carried). |
| **STABLE**                   | Reduces animal maintenance costs by 50% at this stronghold. Provides replacement animals (buy at standard price, available Common).                                          |
| **WAREHOUSE** (new function) | Stores up to 20 load units of cargo at no weekly cost. Cargo stored here does not spoil (dry, secure storage). Required for large-scale trade operations.                    |

### Proposed New Function: WAREHOUSE

**Cost:** 200 wood, 100 stone. One HOUSING consumed.

**Effect:** Stores up to 20 load units of trade cargo. Stored goods do not spoil (dry, secure). The warehouse is the physical manifestation of PATH OF THE CARAVAN's cache — a proper one, not a muddy lean-to at a crossroads.

**Upgrade — Large Warehouse:** 400 wood, 200 stone. Two HOUSING consumed. Stores up to 50 load units.

A stronghold with a MARKETPLACE and WAREHOUSE becomes a trade hub. NPC caravans seek it out. Passive income from the marketplace increases by 50% (from 1D6 to 1D6+3 silver per week).

---

## Open Questions

1. **Complexity threshold.** The full system (cargo types, price multipliers, seasonal modifiers, hazard tables, profit calculation) is detailed by design. Should the manuscript include a "Simple Trade" shortcut for groups that want trade as background activity rather than spotlight play? The shortcut would collapse the procedure into: buy cargo → roll MANIPULATION once → GM narrates the run → check profit/loss. One roll, one outcome, five minutes.

2. **NPC caravans.** Should the system include rules for NPC-run caravans that create competition, carry goods the players want, and serve as encounter targets? A simple model: NPC caravans appear as journey encounters, carry random cargo, and either compete at the destination market or offer trade opportunities on the road.

3. **Caravan combat.** When bandits attack a caravan, how does the combat play out? The fellowship fights as usual, but the wagons, animals, cargo, and employees are at risk. Should there be a simple mass-combat shortcut (guards roll collectively, bandits target cargo, losses calculated abstractly) or should it use full tactical combat every time?

4. **Trade monopoly.** Can a fellowship with high Caravan Reputation and Standing corner a market? At Caravan Rep 9+, they could theoretically dictate terms to small settlements. Should there be a cap, a resistance mechanic, or is this an intended late-game power fantasy?

5. **WAREHOUSE function.** Is this needed as a separate stronghold function, or does existing storage (stronghold buildings with spare HOUSING) serve well enough? The proposal includes it because large-scale trade needs secure bulk storage that is mechanically distinct from living space.

6. **PATH OF THE CARAVAN Rank 3 mishaps.** The talent describes mishaps abstractly (lose 1D6 silver per ☠️ per day absent). This proposal's hazard table provides specific events. Should the talent text be revised to reference the hazard table directly, or should the two systems remain parallel (talent for quick resolution, hazard table for detailed play)?

7. **Integration with Traderoads companion.** The Villages and Rumors proposal's ASK AROUND and SEEK WORK procedures feed directly into caravan play. Should the two proposals be merged into a single chapter, or remain as separate systems that cross-reference each other?

---

## Summary of New Rules

| New Rule                                    | Type                        | Integrates With                           |
| ------------------------------------------- | --------------------------- | ----------------------------------------- |
| Caravan Assembly (transport, people, costs) | Resource system             | Ch 10 Economy, Ch 12 Pay                  |
| Cargo Categories (7 types + loading)        | Classification + roll       | Ch 10 Trade Goods                         |
| Regional Trade Profiles                     | GM tool + price framework   | Ch 10 Supply Rolls                        |
| Trade Rumors                                | Information system          | Ch 8 Rumors, Villages proposal ASK AROUND |
| Route Planning                              | Decision framework          | Ch 8 Journeys, Ch 9 ROAD/BRIDGE/PIER      |
| Caravan Travel Modifications                | Journey rules extension     | Ch 8 Movement and encounters              |
| Market Roll (selling procedure)             | Skill roll + outcome table  | Ch 10 Economy, Ch 4 Peddler talents       |
| Standing Orders                             | Persistent trade contract   | Market Roll result                        |
| Profit/Loss Accounting                      | Economic calculation        | All cost categories                       |
| Caravan Hazard Table (D66)                  | Random event table          | Ch 8 Journey encounters                   |
| Caravan Circle Reputation (0-11+)           | Reputation subsystem        | Ch 8 Circles of Reputation                |
| Seasonal Price Multipliers                  | Economic modifier table     | Ch 10 Prices                              |
| Return Contracts and Passengers             | Work-finding at destination | Villages proposal SEEK WORK               |
| PATH OF THE CARAVAN integration             | Talent-subsystem bridge     | Ch 4 Peddler talents                      |
| WAREHOUSE stronghold function               | New function                | Ch 9 Stronghold functions                 |

<!-- markdownlint-enable MD013 -->
