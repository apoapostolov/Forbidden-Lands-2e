<!-- markdownlint-disable MD013 -->

# Proposal — Hex Resource Subsystem

## Summary

This proposal adds a complete raw material subsystem to the player's guide: prospecting, discovery, exploitation, depletion, and recovery of natural resources within hexes. It bridges the existing gap between Chapter 8 (Journeys), which names terrain but says nothing about what lies inside it, and Chapter 9 (The Stronghold), which consumes wood, stone, iron, and ore by the hundred-unit but never explains where they come from or how they run dry.

The design draws on medieval mining, forestry, and quarrying practice. It is grounded in the action economy already established by the journey rules (Quarter Day activities, terrain modifiers, skill rolls) and keyed to the stronghold functions that already exist (Mine, Quarry, Sawmill, Lumber Camp).

## Problem Statement

The corebook has three disconnected layers:

1. **Chapter 8** defines terrain types (Plains, Forest, Hills, Mountains, etc.) and gives each a FORAGE and HUNT modifier. It says nothing about timber, stone, ore, clay, or any other material resource.

2. **Chapter 9** asks players to spend hundreds of units of wood, stone, and iron to build stronghold functions. The MINE function requires "a minable resource found in the hex." The QUARRY function references "a SURVEY THE LANDS roll." Neither mechanic is defined elsewhere in the corebook.

3. **Chapter 10** lists crafting recipes that consume raw materials (iron, wood, stone, leather, cloth) but never describes how those materials are acquired in the field.

Players building a stronghold have no rules for:
- finding out what resources exist in a hex
- how much is there
- how fast it can be extracted
- when it runs out
- whether it can recover

This proposal fills all five gaps.

## Design Principles

1. **Medieval realism over fantasy abstraction.** Real mines started with surface outcrops and prospecting. Real forests were coppiced, not clearcut. Real quarries were opened where rock showed above ground. The subsystem should feel like work, not magic.

2. **Player-facing.** Discovery and exploitation are things adventurers do. The GM sets the hex, but the players choose when to prospect, where to dig, and how hard to push. This is a player's guide subsystem, not a GM-only generator.

3. **Integrated with existing action economy.** Every activity is a Quarter Day action using existing skills (SCOUTING, SURVIVAL, CRAFTING, MIGHT). No new skills.

4. **Resource dice for depletion.** The game already uses resource dice for consumables (food, water, arrows, torches). Hex deposits should work the same way — a die that degrades on a 1.

5. **Terrain-gated.** What you can find depends on where you stand, using the terrain types already defined in Chapter 8. Mountains produce ore and stone. Forests produce timber. Plains produce clay and peat. Marshlands produce peat and bog iron.

6. **Scarcity is the default.** Most hexes contain something common (stone, clay, timber in forested land). Valuable deposits (iron, silver, gold) are rare and require real search. This matches the Forbidden Lands tone of harsh scarcity.

## Proposed Rules

### PROSPECTING

> *Before you can dig, you must find what the land is hiding. Iron does not announce itself. Stone and clay show themselves to a trained eye, but ore veins run blind beneath the surface. The old miners of Harga knew the signs — color in a streambed, a certain weight in the soil, the way a hillside sheds water after rain. You must learn the same, or pay someone who already has.*

Prospecting is the act of surveying a hex for exploitable natural resources. It is a Quarter Day activity. You must be present in the hex.

**Roll:** SCOUTING (for surface resources: timber, stone, clay, peat, sand) or SURVIVAL (for subsurface resources: iron ore, silver ore, gold, bog iron). Add terrain modifiers from the prospecting table. A character with the PATHFINDER talent adds +1. A character with the MINER hireling background or the BUILDER talent adds +1 when prospecting for stone or ore.

Each hex may be prospected once per resource category per visit. You cannot roll for iron, fail, and immediately try again. You must leave the hex and return — or spend a full day (two Quarter Days) conducting a deeper survey, which allows a second roll at -1.

#### PROSPECTING MODIFIERS

| Terrain | Surface Resources | Subsurface Resources |
| --- | ---: | ---: |
| Plains | +1 (clay, sand) | -2 |
| Forest | +2 (timber) | -2 |
| Dark Forest | +1 (timber) | -3 |
| Hills | +1 (stone) | +0 |
| Mountains | +2 (stone) | +1 (ore) |
| Marshlands | +1 (peat, bog iron) | -1 |
| Quagmire | +0 (peat) | -3 |
| Ruins | +1 (stone, salvage) | -1 |
| Lake/River | +0 (sand, clay) | -1 (alluvial ore) |

#### PROSPECTING RESULTS

| Successes | Result |
| ---: | --- |
| 0 | Nothing found. The hex may still contain resources — you simply failed to find them. |
| 1 | **Common deposit found.** The GM reveals one common resource present in the hex (stone, clay, sand, peat, timber — whichever fits the terrain). Roll the deposit die on the Deposit Size table. |
| 2 | **Significant deposit found.** As above, but the GM may reveal a less common resource (iron ore, bog iron, salt). Roll the deposit die with +1. |
| 3+ | **Rich deposit found.** As above, plus the GM may reveal a rare resource (silver ore, gold, gemstone, marble, limestone). Roll the deposit die with +2. |

A hex can contain multiple deposits of different types. Each prospecting roll can reveal at most one. The GM decides which deposits exist based on terrain and setting logic — this table gives the player's roll a mechanical gateway, but the GM is never forced to place silver in a plains hex just because the player rolled three sixes.

### DEPOSIT SIZE

When a deposit is found, roll on this table to determine its scale. The deposit die represents the total extractable material. The die is not rolled during extraction — it is **degraded** over time by exploitation (see Depletion below).

| D6 + Modifier | Deposit Size | Deposit Die | Approximate Total Yield |
| ---: | --- | --- | --- |
| 1-2 | **Pocket.** A surface scatter, an exposed seam, a single fallen trunk. Enough for a few days of work. | D6 | 50–100 units |
| 3-4 | **Seam.** A workable deposit. Enough to support a season of digging or cutting. | D8 | 100–300 units |
| 5-6 | **Vein.** A substantial find. Enough to justify building a proper mine, quarry, or lumber camp. | D10 | 300–600 units |
| 7+ | **Lode.** A major deposit. Rare, valuable, and worth defending. Worth building a stronghold around. | D12 | 600–1200 units |

The "approximate total yield" is a guideline for the GM, not a tracked number. The deposit die handles depletion abstractly.

### WHAT EACH TERRAIN HOLDS

This table defines the default resource possibilities per terrain type. The GM may add or remove entries based on local hex fiction, but this is the baseline. A resource marked **Common** can be found on a single prospecting success. One marked **Uncommon** requires two successes. One marked **Rare** requires three or more.

| Terrain | Common | Uncommon | Rare |
| --- | --- | --- | --- |
| Plains | Clay, sand | Peat, limestone | — |
| Forest | Timber, firewood | Resin, charcoal wood | Bog iron (if wet) |
| Dark Forest | Timber, firewood | Banewood, charcoal wood | — |
| Hills | Stone, clay | Iron ore, limestone | Silver ore |
| Mountains | Stone | Iron ore, marble | Silver ore, gold |
| Marshlands | Peat, reeds | Bog iron | — |
| Quagmire | Peat | Clay | — |
| Ruins | Salvage stone, salvage iron | Worked stone, old bronze | Artifacts (GM-placed) |
| Lake/River | Sand, clay | Alluvial iron, salt (coast) | Alluvial gold |

**Salvage** resources from Ruins are reclaimed, not mined. They count as half-weight for transport because they come pre-shaped but damaged.

### EXPLOITATION

> *A mine is not a hole. It is a throat driven into the earth, propped with beams that want to bow, drained of water that wants to rise, and fed with men who want to leave. Every unit of ore costs sweat, timber, and risk. If you think you can dig wealth from the ground the way you pick flowers from a meadow, the mountain will teach you otherwise.*

Once a deposit is found, it can be exploited. Exploitation methods depend on the resource type:

| Resource | Method | Skill | Tool Required | Yield Per Quarter Day | Notes |
| --- | --- | --- | --- | ---: | --- |
| Timber | Felling | MIGHT | Timber axe | 4 units wood | Forest or Dark Forest only. |
| Firewood | Gathering | SURVIVAL | Hand axe or saw | 2 units firewood | Any hex with trees. No prospecting needed. |
| Stone | Quarrying | MIGHT | Sledgehammer, pickaxe | 2 units stone | Open quarry; no tunnel risk. |
| Clay/Sand/Peat | Digging | SURVIVAL | Shovel | 3 units | Open-air extraction. |
| Iron Ore | Mining | MIGHT | Pickaxe, sledgehammer | 2 units ore | Requires tunnel supports (1 wood per QD). Collapse risk. |
| Silver Ore | Mining | MIGHT | Pickaxe, sledgehammer | 1 unit ore | As iron, but slower. |
| Gold | Panning/Mining | SURVIVAL or MIGHT | Pan or pickaxe | 1 unit per day | Panning (rivers) uses SURVIVAL. Mining uses MIGHT. |
| Bog Iron | Gathering | SURVIVAL | Shovel | 1 unit per QD | Seasonal: available Spring and Fall only. |
| Resin/Charcoal | Processing | CRAFTING | Hand axe, kiln or fire | 2 units per QD | Requires existing timber supply. |
| Salvage (Ruins) | Scavenging | SCOUTING | Crowbar or hammer | 2 units per QD | Mixed materials; GM determines type. |

**Yield assumes one worker.** Multiple workers in the same deposit multiply yield linearly, up to the capacity of the operation (see the MINE and QUARRY functions in Chapter 9 for the stronghold-scale version — up to twelve workers).

**Casual extraction vs. stronghold operation.** A lone adventurer with a pickaxe can dig ore from a found deposit at the field rate above. Building a proper MINE or QUARRY function (Chapter 9) increases throughput, adds hireling capacity, and unlocks seasonal batch yields. The field rates exist so that a party on the road can extract material from a found deposit without building permanent infrastructure.

#### COLLAPSE RISK (MINING)

Underground mining carries the same collapse risk described in the MINE function (Chapter 9). For each week of underground mining, roll one Gear Die. On a 💀, a tunnel section collapses. Each worker inside rolls a second Gear Die — another 💀 means that worker is trapped. Trapped NPCs are killed. A trapped PC suffers an attack of ten Base Dice (Weapon Damage 1, blunt force). If the PC survives, they must make a MIGHT roll to dig free or wait for rescue.

Surface quarrying, timber felling, panning, and open-air digging do not carry collapse risk — but they carry weather risk. Work in rain, storm, or cold imposes the same penalties as hiking in those conditions (see Weather, Chapter 8).

### DEPLETION

> *The dwarves of Moldena speak of a mine's life the way a druid speaks of a tree's. It is born when the first pick breaks stone. It grows when the veins branch. It sickens when the ore thins to dust and the water rises. And it dies when the last man walks out and the mountain closes behind him. Every mine dies. The question is how much it gives before it does.*

Every deposit has a **deposit die** assigned when it is discovered. The deposit die is not rolled to produce ore — it is rolled to check whether exploitation has begun to exhaust the source.

**Depletion roll:** At the end of each **Season** (three months) of active exploitation, roll the deposit die once. On a **1**, the deposit die degrades one step:

D12 → D10 → D8 → D6 → **Exhausted**

When a D6 deposit rolls a 1, the deposit is exhausted. No further material can be extracted.

**Heavy exploitation** accelerates depletion. If more than six workers operated in the deposit during the season, roll the depletion die **twice** and apply the worse result.

**Intermittent use** slows depletion. If the deposit was worked for fewer than four weeks of the season, skip the depletion roll entirely for that season. This rewards careful, seasonal extraction — the medieval pattern of working a mine in summer and leaving it to drain in winter.

### RECOVERY

Mineral deposits (stone, ore, silver, gold) do not recover. Once exhausted, they are gone. The mountain gave what it had.

**Timber** recovers. If a forested hex is not logged for two full seasons (six months), roll a D6. On a 5-6, the deposit die recovers one step (minimum D6). Coppiced woodland — timber cut above the root so the stump resprouts — recovers on a 4-6 instead. A character with the HERBALIST talent or a DRUID can supervise coppicing.

**Peat** recovers very slowly. If a peat deposit is not cut for one full year, roll a D6. On a 6 only, the deposit die recovers one step.

**Bog iron** recovers seasonally. Bog iron forms in waterlogged soil through natural chemical processes. A depleted bog iron deposit may recover one die step per year automatically, without a roll, as long as the marshland hex is not drained or built over.

**Clay and sand** do not deplete under normal use. A clay or sand deposit is effectively inexhaustible at the scale of play. Do not track a deposit die for these resources unless the GM has a specific fiction reason (a flood buries the clay pit, a landslide covers the sand bank).

### TRANSPORT

Raw materials are heavy. Moving them from the hex where they were found to the stronghold where they are needed is a logistical problem, not a footnote.

| Material | Weight Per Unit | Notes |
| --- | --- | --- |
| Timber (logs) | 2 | Requires a cart or dragging. Cannot be carried in a backpack. |
| Firewood | 1 | Can be bundled and carried. |
| Stone | 3 | Requires a cart. Wagons cannot enter difficult terrain. |
| Iron Ore | 2 | Heavy, dirty, and awkward. |
| Silver/Gold Ore | 2 | As iron ore. Attracts attention. |
| Clay/Sand/Peat | 1 | Bulky but light. Sacks or barrels. |
| Planks | 1 | Lighter than raw timber; requires a Sawmill to produce. |
| Charcoal | 1/2 | Very light. Fragile. Crumbles if dropped or rained on. |

**Cart capacity:** A cart drawn by one horse carries 50 weight-units of material. A wagon drawn by two horses carries 100. Neither can enter difficult terrain unless a ROAD exists.

**River transport:** If the source hex connects to the stronghold hex by river, timber can be floated downstream at no cart cost. One worker per 20 units of timber manages the float. Stone and ore cannot be floated.

**Road bonus:** If a ROAD function (Chapter 9) connects the two hexes, transport time is halved and wagon capacity doubles for that route.

The distance in hexes between deposit and stronghold determines transport time: one Quarter Day per hex of open terrain, two per hex of difficult terrain. A round trip doubles the time. Building infrastructure (roads, bridges, river piers) is the medieval answer to transport cost — and the game's answer too.

### PROSPECTING DURING JOURNEYS

Prospecting integrates with the existing journey framework. During a journey, each Quarter Day is allocated to an activity: HIKE, FORAGE, HUNT, KEEP WATCH, REST, SLEEP, or MAKE CAMP. **PROSPECT** is added as a new Quarter Day activity.

**PROSPECT:** Spend one Quarter Day surveying the current hex for exploitable natural resources. Roll as described under Prospecting above. You cannot hike and prospect in the same Quarter Day. You must remain stationary in the hex.

A party that wants to prospect a hex typically arrives by hiking in one Quarter Day, prospects in the second, and either rests or camps in the third and fourth. This means prospecting costs a full travel day — you sacrifice forward movement to learn what the land holds. That trade-off is intentional.

If the party is already camped in a hex (at a stronghold, resting after a fight, waiting out weather), prospecting costs only the Quarter Day, with no travel penalty.

### LINKING DEPOSITS TO STRONGHOLD FUNCTIONS

The existing stronghold functions already reference the resources this subsystem provides:

| Stronghold Function | Resource Required | How This Subsystem Connects |
| --- | --- | --- |
| MINE (Ch9) | "A minable resource must be found in the hex" | A prospecting roll for subsurface resources with 2+ successes reveals iron or silver ore, satisfying this prerequisite. |
| QUARRY (Ch9) | A quarry resource or a SURVEY THE LANDS roll | A prospecting roll for surface resources with 1+ success reveals stone, clay, sand, or peat. This replaces the undefined "SURVEY THE LANDS" reference. |
| SAWMILL (Ch9) | Timber supply | A prospecting roll confirms timber availability in a Forest or Dark Forest hex. Timber is always Common in these terrains. |
| LUMBER CAMP (Ch9 Hex Improvements) | Forest/Dark Forest only | As Sawmill. The deposit die tracks how long the forest can sustain logging before thinning. |
| FORGE (Ch9) | 60 Iron | Iron must be mined from a found iron ore deposit and smelted at the forge. |
| SALT WORKS (Ch9) | Adjacent ocean | Salt is not prospected — it is produced from seawater. No change. |
| FIELD / GARDEN (Ch9) | "A hex that can be foraged" | The forage modifier from the terrain types table (Ch8) already governs this. No change. |

#### REPLACING "SURVEY THE LANDS"

The term "SURVEY THE LANDS" appears twice in Chapter 9 without definition. This subsystem replaces it: any reference to "a SURVEY THE LANDS roll" should be read as "a successful prospecting roll in the hex." The next editorial pass should update those two references.

### WORKED EXAMPLE

> Torvin's band has claimed a ruined castle in a Hills hex as their stronghold. They need stone for RAMPARTS (600 stone) and iron for a FORGE (60 iron, which means 60 units of ore smelted into bars). The nearest forest is two hexes south.
>
> **Season 1 — Spring.** Torvin prospects the castle hex for surface resources. He rolls SCOUTING with the +1 Hills modifier and scores one success. The GM reveals a **stone deposit** — a limestone shelf exposed by the old castle's collapsed foundations. The deposit die is rolled: 4 + 1 (Hills bonus) = 5, a **Vein** (D10). Plenty of stone.
>
> Torvin then prospects for subsurface resources. He rolls SURVIVAL with +0 (Hills). Two successes. The GM reveals an **iron ore seam** running under the eastern slope. Deposit die: 3 = **Seam** (D8). Enough ore for a few seasons if they are careful.
>
> **Season 2 — Summer.** Two hired quarry workers begin extracting stone. At 2 units per QD per worker, working two QDs per day for twelve weeks, they produce roughly 288 units of stone this season. The deposit depletion die is rolled at season's end: the D10 shows a 4. No degradation.
>
> Meanwhile, Torvin and the dwarf Tyrgar begin mining iron ore by hand. No MINE function yet — just picks and tunnel supports. At 2 units of ore per QD, Torvin works 48 QDs over twelve weeks and produces 96 units of ore. But he also spends 48 units of wood on tunnel supports. The party's hunter spends two days felling timber in the forest hex to the south (4 units per QD × 4 QDs = 16 units, hauled back by cart over two days). The rest of the wood is bought from a nearby village.
>
> At season's end, the iron deposit's D8 is rolled: a 1. The die degrades to D6. The seam is thinning faster than expected — they should build a proper MINE to increase efficiency before pushing harder.
>
> **Season 3 — Fall.** The MINE function is built (60 wood for supports, one month build time). Now up to twelve workers can operate. Four hired miners work the deposit: 300 ore per season per miner at stronghold scale = 1,200 ore total. But this is heavy exploitation (more than six workers total), so two depletion dice are rolled. The D6 shows 3 and 2. No degradation this time — but the deposit is already fragile. Torvin decides to reduce to two miners next season and let the mine rest.

## Integration Notes

- **Chapter 8:** Add PROSPECT as a Quarter Day activity in the journey activity list, alongside HIKE, FORAGE, HUNT, KEEP WATCH, REST, SLEEP, and MAKE CAMP.
- **Chapter 9:** Replace the two "SURVEY THE LANDS" references with "a successful prospecting roll" and cross-reference the new subsystem. Add a short note under MINE and QUARRY pointing to this section.
- **Chapter 10:** No changes needed. Crafting recipes already consume the right material units.
- **Chapter 3 (Skills):** No new skills. SCOUTING and SURVIVAL already cover the rolls. Consider adding a one-line note under SCOUTING ("You can also prospect a hex for surface resources") and SURVIVAL ("You can also prospect for subsurface deposits like ore veins").

## What This Proposal Does Not Cover

- **Hex ownership, territory control, and political consequences of claiming resources.** Those are GM-facing systems. Chapter 9 already has hex improvement rules and a territorial framework. This proposal provides the resource layer those systems consume.
- **NPC settlement generation.** That is a Gamemaster's Guide topic (and the domain of supplements like *Towns & Villagers*).
- **Trade prices for raw materials.** Chapter 10 already defines prices for finished goods. Raw material prices should follow the same supply/rarity framework: common resources are cheap, rare ores command a premium. A price table can be added to Chapter 10 if needed, but it is not part of this proposal.
- **Magical resources.** Demon iron, elf-forged glass, cursed ore, and similar supernatural materials are GM-placed fiction elements, not prospectable deposits. This subsystem handles the mundane economy of stone, wood, and metal.

## Voice Check

The proposal uses the manuscript's existing voice: direct, physical, unsentimental, with medieval-weight imagery. Flavor text is embedded in the rules, not bolted on. Numbers are spare and functional. The worked example reads like play, not theory.

<!-- markdownlint-enable MD013 -->
