<!-- markdownlint-disable MD013 -->

# Travel and Downtime — The Journey Engine

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** Travel is where YZE turns *logistics* into play. This file assumes `00-engine-core.md` (resolution, success ladders, pushing) and ties to `04-harm-and-consequences.md` (conditions: COLD/THIRSTY/HUNGRY/SLEEPY) and `02-progression-and-xp.md` (TRAIN/CRAFT).

## Contents

1. Source provenance
2. Abstraction target
3. Travel model: hex (FL) vs pointcrawl (West) — the central dial
4. The time block: Quarter-day / Shift
5. The activity menu — the load-bearing structure
6. Movement, navigation, and the forced-march pressure valve
7. Weather and environmental pressure
8. Forage, hunt, fish — the food layer
9. Making camp, watch, and the failed-camp liability
10. Rest, sleep, recovery shifts, and downtime
11. Divergence rows (FL vs West)
12. Dials and instantiation recipe
13. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/08-journeys.md` (~1,470 lines) — hex map (10 km hexes, 10 terrain types), Quarter Days (Morning/Day/Evening/Night), daily checklist, Weather (Wind/Rainfall/Temperature) + Expanded Weather (HEAT/TEMP, seasonal, clothes, sleeping gear), full activity menu (HIKE/LEAD THE WAY/KEEP WATCH/FORAGE/HUNT/FISH/SURVEY/MAKE CAMP/REST/TRAIN/CRAFT/REPAIR/SLEEP/EXPLORE), forced march, mounts, darkness, sea travel, settlement-visit downtime menu (ASK AROUND/SEEK WORK/PETITION/TRADE/CAROUSE/HEAL/REST/TRAIN), reputation system.
- `03-book-of-beasts/03-gamemaster-tools.md:138-345` (journey location/campsite random tables by terrain), `:347-379` (weather, mirrors core), `:380-422` (stronghold random events/servants), `:422-477` (forage for herbs, potions & poisons).

**Tales of the Old West 2E (West):**
- `01-corebook/06-life-in-the-old-west.md:1261-1345` — **pointcrawl** travel: Traveling Table (miles per **Shift** by method × terrain), pushing travel (+50%, MOVE/Animal Handlin' roll, Trouble halts progress), Making Camp (Nature roll, extra ⚔ = −1 to pursuers' HAWKEYE), Wildlife statblocks (bear/bison/wolf/snake/spider, Toughness), Animal Critical Effect Table, Traps (snares/bear trap/pit trap).
- `02-the-1870s/11-frontier-survival-and-hunt.md:13-187` — water (daily need, sources, bad water, purification), weather as regional killers (blue norther/chinook/drought/haboob), fire, navigation, travel-speed table (miles/day by mode), regional terrain, "the country as antagonist."
- `02-the-1870s/11-frontier-survival-and-hunt.md:191-470` — the Hunt as **professions** (buffalo hide hunter, market hunter, wolfer, sporting guide, contract hunter, trapper).
- `02-the-1870s/15-competence-and-procedures.md:126-211` — camp & trail procedures (fire in wind/rain/snow; beans/biscuit/bacon/coffee; pitching & striking camp; picketing; night watches), survival procedures (finding/conserving water, river crossing, reading weather, blizzard, rattlesnake, shelter, tracking, snare, field-dressing).

## Abstraction target

Reverse-engineer the **journey engine** as a genre-neutral travel/survival loop. The two games instantiate the *same spine* — a **time block** (Quarter-day / Shift), an **activity menu** (each PC takes one travel job per block), a **weather-pressure layer**, a **food layer**, and a **camp/recovery layer** — but diverge sharply on the **spatial model**: FL is a maximal **hex-crawl** (10 km tiles, terrain types, per-tile procedures, tile-by-tile mishaps); West is a **pointcrawl** (mileage-between-points, lighter, with depth pushed into survival reference prose and the Trouble system).

The deliverable is the **activity-menu architecture** — the most transferable artifact: *distribute the party's labor across a fixed menu so every PC has a travel job* — and the **hex-vs-pointcrawl trade-off** recorded as the engine's central spatial dial.

## 3. Travel model: hex (FL) vs pointcrawl (West) — the central dial

**FL — hex-crawl (granular, exploratory):** The map is divided into hexagons, **one hexagon = 10 kilometers**. Each hex has a terrain type that governs movement difficulty and encounter tables. FL `08-journeys.md:7-42`. Movement is *tile-by-tile*: you enter a new hex, the pathfinder rolls to **LEAD THE WAY** (a Survival roll *per hex entered*), failure still moves you in but triggers a mishap roll. FL `08-journeys.md:175-198, 229-258`. Ten terrain types (Plains, Forest, Dark Forest, Hills, Mountains, High Mountains [impassable], Lake/River [boat], Marshlands [raft], Quagmire, Ruins) each tag movement (Open/Difficult/Impassable) *and* forage/hunt modifiers. FL `08-journeys.md:31-42`. The hex is the unit of exploration: unexplored hexes are the prize, terrain features are discovered hex-by-hex, and the GM rolls a random encounter **once per Quarter Day while HIKING, once per day if you stay put**. FL `08-journeys.md:281-284`.

**West — pointcrawl (mileage-between-points, lighter):** Travel is resolved by a **Traveling Table**: miles covered per **Shift**, cross-indexed by *method of travel* (on foot / horseback / cart / stagecoach) × *terrain class* (Road or trail / Easy / Hard). West `06-life-in-the-old-west.md:1283-1290`. There is no grid; distance is a number between two named points. Speeding up is a single decision — push for **+50% distance** with a MOVE roll (foot) or Animal Handlin' roll (mount/wagon); failure adds a cumulative −1, *Trouble* on the roll halts you at half distance (sprained ankle, lame horse, thrown wheel). West `06-life-in-the-old-west.md:1263-1267`. The country between points is rendered as **procedural reference and attrition** rather than tiles: water spacing ("sixty miles to the next water"), regional weather killers, and terrain types are *setting facts that set difficulty and survival rolls*, not a map you crawl. West `11-frontier-survival-and-hunt.md:135-187`.

**The trade-off (record this as the core decision):**

| | **FL — hex-crawl** | **West — pointcrawl** |
| --- | --- | --- |
| **Spatial unit** | Hexagon tile (10 km). | Distance number between points. |
| **Exploration feel** | *Discovery of unknown space* — fog-of-war, terrain features revealed per tile, the map *is* play. | *Traversal of known route* — the points matter; the between is attrition. |
| **Navigation cost** | A Survival roll **per hex entered**; failure = mishap (lost, blocked, sprained ankle). FL `08-journeys.md:229-258`. | A single decision to rush (+50%); navigation is folded into travel speed + survival reference. West `06:1263-1267`. |
| **Prep weight** | Heavy — terrain table, mishap tables, encounter tables, per-tile features. | Light — one mileage table + Trouble on the rush roll. |
| **Best for** | Sandbox exploration, hex-crawl campaigns, "draw your own map." | Linear/point-to-point drama, trail and pursuit stories, faster pacing. |

**Generic abstraction — "the spatial model":** a function that turns *intended movement* into *progress + pressure*. Two canonical points:
- **Tile-crawl** (FL): the world is a grid of unknown tiles; each tile entered is a procedure (enter → navigate → possibly mishap → possibly encounter). Favors exploration depth, fog-of-war, and "the map as treasure." Cost: prep and table-time per tile.
- **Point-hop** (West): the world is a graph of named points with edge weights (miles × terrain class); a travel block advances you N miles along an edge, with pressure on the rush decision. Favors speed, pursuit/drama, and survival-as-attrition. Cost: less discovery, the "between" is flavor not play.

**Layer:** the spatial model is a **core design dial** (see §12). Within either model, the **terrain-class tagging** (Open/Easy/Hard/Difficult/Impassable × forage/hunt modifiers) is **General** — both games attach movement and food modifiers to terrain type. FL `08-journeys.md:31-42`; West `06:1285-1290`. The per-tile mishap tables (FL) and the rush/Trouble gate (West) are the *pressure layer* and are **Situational** to the chosen spatial model.

## 4. The time block: Quarter-day / Shift

**The shared rule (both):** Travel is measured in **fixed blocks of the day**, not continuous time. During a journey, each character spends *one block* on *one activity*; the block is the budget over which the party distributes its labor.

**FL — the Quarter Day:** The day is divided into **four Quarter Days: Morning, Day, Evening, Night.** FL `08-journeys.md:149-157`. "At the start of every Quarter Day, each adventurer must choose one activity for the Quarter Day. No more than one activity can be performed at the same time, unless specified otherwise." FL `08-journeys.md:158`. The Quarter Day is also the unit for weather effects, forced-march rolls, encounter rolls, and spoilage timers. A **daily checklist** opens the day: roll resource dice (water/food/hygiene), roll weather, update calendar, check time-sensitive effects. FL `08-journeys.md:44-49`.

**West — the Shift:** Travel speed is given as **miles per Shift**, cross-indexed by method and terrain. West `06-life-in-the-old-west.md:1283-1290`. Making Camp, watch, and rest occur over Shifts; pushing travel and the Trouble gate are per-Shift decisions. West `06:1263-1267, 1277-1281`. The Shift carries the same load as FL's Quarter Day — it is the travel-time budget — but West does not hard-codify a four-block day or a daily-roll checklist in the core travel section; its daily structure is implied by the travel table and camp sequence.

**Generic abstraction — "the travel time unit":** a discrete block (¼-day / Shift / watch) that is the resolution unit for *all* travel procedures: movement, activities, weather, encounters, recovery, spoilage. Two knobs: (1) **blocks per day** (FL = 4 explicit Quarter Days; West = Shift, count loose), and (2) **whether the day opens with a deterministic checklist** (FL yes — resource dice, weather, calendar; West no formal checklist). **Layer:** the time block is **General**; the daily-roll checklist is **Optional** (a pacing/attrition dial — it makes the day feel like a series of costs, but it adds bookkeeping).

## 5. The activity menu — the load-bearing structure

> This is the most transferable artifact of the journey engine: **distribute the party's labor across a fixed menu so every PC has a travel job.**

**FL — the full formal menu (14 activities).** At the start of every Quarter Day each PC picks **one** activity from a fixed list; most can be done by several PCs at once, a few are single-PC-only: FL `08-journeys.md:158-173`.

| Activity | Solo or shared | Can stack with HIKE? | Core roll |
| --- | --- | --- | --- |
| **HIKE** | *All* must do it to move on the map | (is the move action) | Endurance (forced march) |
| **LEAD THE WAY** (pathfinder) | One PC only; no helping | Yes (pathfinder also HIKES) | Survival, per hex |
| **KEEP WATCH** (lookout) | One PC only; no helping | Yes | Scouting (on encounter) |
| **FORAGE** | Several; helping allowed | No (must stop) | Survival |
| **HUNT** | Several; helping allowed | No | Survival (find) + Marksman/Survival (kill) |
| **FISH** | Several (needs water hex) | No (foot); yes (from boat) | Survival |
| **SURVEY THE LANDS** | Several | No | Scouting |
| **MAKE CAMP** | One rolls; helping allowed | No | Survival |
| **REST** | Several (auto when you SLEEP) | — | Resource-die restore |
| **SLEEP** | Several (≥1 Quarter Day/day or SLEEPY) | — | (enables REST) |
| **TRAIN** | Several (needs XP + teacher) | — | Wits (if no teacher) |
| **CRAFT** | Several | — | Crafting |
| **REPAIR** | Several (≤3 items/Quarter) | — | Crafting |
| **EXPLORE** | Several (at an adventure site) | No (journey pauses) | site-specific |

The exclusions encode the labor trade-off: to **move** you spend HIKE; to **navigate safely** you spend LEAD THE WAY; to **spot threats** you spend KEEP WATCH; to **eat** you spend FORAGE/HUNT/FISH and *stop moving*. A lone traveler is allowed to LEAD THE WAY and KEEP WATCH at once — an explicit exception that proves the rule that the menu is a *constraint on the party*. FL `08-journeys.md:297-299`.

**West — a lighter, spirit-equivalent menu.** West does not publish a 14-row formal menu, but the same labor-distribution logic runs its travel: someone must **ride/drive** (the travel action, resolved by the Traveling Table), someone must **make camp** (Nature roll), someone must **stand watch** (night watches, two-hour turns), and the party makes **rush vs. safe** and **forage/hunt** decisions within the Shift budget. West `06:1263-1281`; camp/trail procedures in `15-competence-and-procedures.md:126-160` (pitching camp, picketing horses, night herders riding two-hour watches). The depth West *does* formalize that FL does not is **mounted/animal labor** and **trail procedure** (catching, saddling, hobbling, picketing, watering, shoeing, pacing a horse so it doesn't founder) — a travel-job layer tuned to its genre. West `15:24-82, 152-155`.

**Generic abstraction — "the activity menu":** A fixed list of travel jobs; each block, each PC picks one; the menu is balanced so that *movement, navigation, security, and supply are mutually exclusive demands* — you cannot move, navigate, watch, and forage with the same character in the same block. The menu is what makes travel a **resource-allocation puzzle** rather than narration: the party is perpetually short of hands, so "do we push on or stop to forage?" is a real decision every block.

Three design knobs: (1) **menu breadth** (FL = 14; West ≈ 6–8 implicit; trim to a mounted/survival/urban set as the genre demands); (2) **solo-vs-shared** tagging (which jobs one character monopolizes — pathfinder, lookout — which forces role assignment); (3) **what stacks with movement** (FL lets LEAD THE WAY and KEEP WATCH stack with HIKE; FORAGE/HUNT cannot — this is the key constraint that makes *stopping* costly). **Layer:** the menu architecture is **General**; the specific activity roster is **Situational** (genre-dependent); the daily-roll checklist that opens the day is **Optional**.

## 6. Movement, navigation, and the forced-march pressure valve

**FL movement (per tile):** Two hexes/Quarter Day in Open terrain, one in Difficult, +1 (to three) Open on horseback; a road raises all travel to 3/Quarter; vehicles, rowing, and sailing have their own speeds. FL `08-journeys.md:175-198`. **Navigation = LEAD THE WAY:** a Survival roll *per hex entered*; success finds a viable path, failure still moves you in but rolls a mishap (Lost, Blocked Terrain, Quicksand, Fog, Downpour, Sprained Ankle, Savage Animal…). FL `08-journeys.md:229-258`. Modifiers stack from conditions: −1 in Darkness/Fog/Snowfall, −1 per Strong Wind at sea, +1 in clear Sun/Moon/Stars. FL `08-journeys.md:235-242`. **Darkness** adds a Scouting roll per unexplored hex entered (fail = fall, 1 Strength), with a season-by-season light/dark table (winter = only Daytime is light). FL `08-journeys.md:260-271`.

**The forced-march valve (FL):** You can HIK E two Quarter Days freely. A **third** Quarter Day of hiking requires an Endurance roll; fail = 1 Agility damage and you can't hike (must rest/sleep). A **fourth** is another Endurance roll at **−2** and makes you SLEEPY (you miss sleep). Gear/loadout and mounts shift the threshold (drawn large weapon/shield −1 hike before rolling; mounted +1). Cumulative −2 per consecutive forced march; snowfall −1. FL `08-journeys.md:200-217`. Mounts force-march on Animal Handling + the animal's Strength; fail = the animal goes lame. FL `08-journeys.md:219-227`.

**West movement (per edge):** Miles per Shift by method × terrain class (foot/horse/cart/stagecoach × road/easy/hard). West `06:1283-1290`. **Navigation/rush = a single roll:** push for +50% with a MOVE (foot) or Animal Handlin' (mount/wagon) roll; failure = no extra progress + cumulative −1 to further rushes; **Trouble on the roll halts you at half distance** (sprained ankle, lame horse, thrown wheel). West `06:1263-1267`. Travel in heat/cold risks Freezing/Heatstroke. West `06:1269`.

**Generic abstraction — "movement + the over-exertion valve":** A base speed (tiles/block or miles/block) tagged by terrain class, plus a **navigation/rush procedure** that converts *wanting to go faster/farther* into a roll that can fail. The two instantiations sit at opposite ends of a dial:
- **Per-tile navigation** (FL): every tile of unknown space costs a roll; failure = a mishap that costs progress or harm. High granularity, exploration-driven.
- **Per-edge rush** (FL): one decision per block to over-exert; the cost is gated by Trouble (a narrative tax) rather than a tile mishap (a mechanical tax). Light, drama-driven.

The **over-exertion valve** — a roll you take to exceed the safe daily travel — is shared and **General**: FL's forced-march (Endurance, damage on fail, sleep loss) and West's rush (MOVE/Animal Handlin', Trouble halts progress) are the same mechanic at two calibrations. The valve is what makes "push on or camp" a real decision: extra distance costs body/beasts/time. **Layer:** base speed + terrain tags = **General**; per-tile navigation = **Situational** (tile-crawl only); the over-exertion valve = **General**.

## 7. Weather and environmental pressure

**FL — weather as a mechanical system ("attrition by table"):** Optional, but when on, the GM rolls **three D6 each morning** — Wind, Rainfall, Temperature — and each result hands out modifiers to travel activities and triggers Endurance rolls. FL `08-journeys.md:51-79`, mirrored at `03-gamemaster-tools.md:347-379`.

- **Wind** (None/Breeze/Gales/Storm): modifies MAKE CAMP (−0/−1/−2); Storm forces an Endurance roll from everyone to keep moving for a Quarter Day. FL `08:55-62`.
- **Rainfall** (Clear/None/Drizzle/Downpour): modifies LEAD THE WAY (+1 clear to −2 downpour); Downpour forces a group Endurance roll to keep moving. FL `08:64-71`.
- **Temperature** (Hot/Pleasant/Cool): Hot forces each HIKING PC to roll Endurance/Quarter Day or become THIRSTY; Cool forces everyone outside camp to roll Endurance/Quarter Day or become COLD. FL `08:74-79`.

**FL Expanded Weather (HEAT/TEMP, seasonal, clothes):** A deeper optional layer. **HEAT** is *felt* temperature (skin), **TEMP** is *actual* temperature; convert between them. Start from a **seasonal base** (Summer 2 / Spring·Fall 1 / Winter 0 / Mountains −1). HEAT on a ladder (−2 to +4) sets *how often* you must roll Endurance to avoid COLD: at HEAT 0 it's every Quarter Day; at −1 every hour; at −2 every 15 minutes — i.e., cold scales from "unpleasant" to "you die in an hour." FL `08-journeys.md:81-108`. **Clothes** (Soaked −2 / Bare minimum −1 / Normal 0 / Winter +1) and **sleeping gear** (campfire up to +2; tent +2 MAKE CAMP and rain protection; no blanket −1; sleeping fur +1) convert TEMP→HEAT and gate whether sleeping on bare ground makes you COLD. FL `08:127-147`. Snowfall at ≤0 HEAT modifies LEAD THE WAY and FORCED MARCH; rain at positive HEAT drops HEAT by 1 and can ruin moisture-sensitive gear (roll item dice, ⚔ = damage). FL `08:121-125`.

**West — weather as setting + attrition reference ("the country as antagonist"):** West does not give a morning weather table in the core travel rules; instead it renders weather as **regional killers** — concrete, lethal, prose-grounded: the *blue norther* (temp drops 50°F in two hours), the *chinook*, hailstorm, tornado, lightning, drought, the Hard Winter of 1886–87; desert *heat*, *cold nights* (50°F drop after sundown), *haboob*, *flash flood*, *sandstorm*; mountain snow/avalanche/altitude sickness/hypothermia. West `11-frontier-survival-and-hunt.md:39-82`. The mechanical pressure enters through the **Trouble system** and through explicit conditions: rushing travel in hot/cold weather risks **Freezing / Heatstroke**. West `06:1269`. The procedural layer (`15:177-185`) gives *reading the weather* (mares' tails = front in 12 h; halo around the moon = rain inside a day) and *surviving a blizzard/thunderstorm* as concrete procedures. The fiction load is enormous: "The land in the West does not care. It is the central fact and the central terror." West `11:185-187`.

**Generic abstraction — "weather as attrition":** A pressure layer that converts *the environment* into *condition damage and lost actions*. Two calibrated points:
- **Mechanical/weather-table** (FL): a deterministic morning roll produces modifiers to travel activities and triggers Endurance rolls that inflict conditions (THIRSTY/COLD). Predictable, table-driven, integrates with gear (clothes/sleeping gear as HEAT modifiers) and the food/water economy. Produces a *grind* — every day the weather taxes you.
- **Reference/Trouble-gated** (West): weather is a *setting fact* that sets scene stakes and enters mechanics through the Trouble system + condition triggers (Freezing/Heatstroke) when you over-exert. Produces *dramatic* weather — storms are scenes, not die rolls.

**Design knobs:** (1) **random-table vs GM-discretion** weather generation; (2) **felt-vs-actual temperature split** (FL's HEAT/TEMP) — adds realism, costs bookkeeping; (3) **gear-as-weather-modifier** (clothes, sleeping gear, fire, tent) — makes equipment loadout a survival decision; (4) **condition currency** — does weather deal attribute damage, conditions, or Trouble? **Layer:** a weather-pressure layer is **General** (the engine expects attrition from the environment); the morning-roll table is **Optional**; the HEAT/TEMP expanded system is **Optional** (a depth dial).

## 8. Forage, hunt, fish — the food layer

**FL — formalized food-supply subsystem.** Food and water are **tracked resources** (Resource Dice) consumed daily; the daily checklist rolls them down. FL `08-journeys.md:44-49`. When supplies run low, three travel activities replenish them, all gated by **Survival** and modified by **terrain + season**:

- **FORAGE** (stop; Survival; food *or* water): success = X units of VEGETABLES (X = ⚔ rolled) or a full waterskin refill to D12; failure = a mishap (Poisonous, Leeches, Sprained Ankle, Torn Clothes, Savage/Persistent Animal). Terrain mods (+1 Forest/Marshland; −1 Plains/Dark Forest/Quagmire; −2 Mountains/Ruins) and season mods (+1 Spring/Autumn; −2 Winter, for food). FL `08-journeys.md:307-352`.
- **HUNT** (stop; Survival find + Marksman/Survival kill): small game (1 Quarter) or large (2 Quarters); an animal table (Squirrel→Deer/Boar) with difficulty, meat, and pelts; failure = mishap (Sprained Ankle, Lost gear, Trap, Savage Animal, Sick Prey). Weather/season/terrain mods **stack** (e.g., autumn-rain-forest = +1; spring-downpour-mountains = −5, "almost certainly a failure, which is the point — nobody hunts in a spring mountain storm"). FL `08-journeys.md:354-413`. **Spoilage** ties food to weather: raw MEAT/FISH spoils within the Quarter Day at HEAT 3+, one day normal, D3 days at HEAT 0 or below; a Chef roll during MAKE CAMP extends it a day. FL `08:386`.
- **FISH** (needs water hex; Survival): X = ⚔ FISH caught; failure = mishap (Snagged Hook, Hook in Finger, Broken Gear, Mosquito Swarm, Splash!, Attacked). FL `08-journeys.md:414-430`.

The food layer is wired into the **recovery economy** too: during a short break you restore Strength by rolling the *food* resource die, Agility by *water*, etc. — so food is not just "don't starve," it is *the currency of healing on the road*. FL `08-journeys.md:555-573`. Herbs (forage variant for Herbalists) feed the potions/poisons subsystem. FL `03-gamemaster-tools.md:424-427`.

**West — food as profession + survival reference.** West's food layer is lighter in the *core travel* rules (no daily Resource Die checklist in the travel section) but far deeper as **setting**: an entire chapter on the **Hunt as professions** — buffalo hide hunter (the "stand," the Sharps, the skinners, the economics), market hunter, wolfer (strychnine bait), sporting guide, contract hunter, trapper. West `11-frontier-survival-and-hunt.md:191-470`. Trapping is mechanically formalized: lay a trap with a Nature roll; traps have Strength (attack dice), Concealment (HAWKEYE penalty), and method (snare/bear trap/pit); extra ⚔ boost Strength or Concealment. West `06-life-in-the-old-west.md:1347-1377`. Cooking/field-dressing is *procedural reference* (beans, sourdough biscuit, bacon/beef, coffee; field-dressing a deer, butchering a beef). West `15:140-145, 207-211`.

**Generic abstraction — "the food layer":** A supply subsystem where **food/water are consumed daily and replenished by travel activities gated by Survival/Nature rolls, modified by terrain and season, with spoilage tying perishables to weather.** Two calibrations:
- **Resource-die + activity-roll** (FL): food/water are dice you roll down daily and restore via FORAGE/HUNT/FISH; spoilage + the recovery tie-in make food *the healing currency*. Tight, mechanical, attritional.
- **Profession + trap/procedure** (West): hunting is a *vocation* with gear, economics, and consequence; trapping is a roll-built trap subsystem; cooking/processing is procedural reference. Color-rich, drama-driven.

**Design knobs:** (1) **food tracking** — Resource Die (FL) vs scene-level scarcity (West) vs none; (2) **season/terrain modifiers** on the supply roll (both have these — General); (3) **spoilage tied to weather** (FL) — Optional depth; (4) **food-as-healing-currency** (FL's short-break restore) — a strong dial that makes supply *load-bearing* for survival. **Layer:** a daily-consumption pressure is **General**; the FORAGE/HUNT/FISH activity trio is **General** (the menu needs a supply row); season/terrain modifiers = **General**; the Resource-Die economy and spoilage = **Optional**.

## 9. Making camp, watch, and the failed-camp liability

**FL — MAKE CAMP as a rich roll with a success ladder, improvements, *and* a hidden failure table.** Making camp takes a Quarter Day (usually Evening); one PC rolls Survival (others help), modified by terrain/weather. FL `08-journeys.md:495-553`.

- **1 ⚔** = a basic camp (crude fire, rough bedding, gear gathered): you may REST/SLEEP without the bare-ground penalties.
- **Each extra ⚔** buys: +1 attribute recovered on REST/SLEEP; concealment (enemies must match/exceed the camp's ⚔ on Scouting to find it); or one **camp improvement** (Banked Fire, Dry Shelter, Raised Beds, Cooking Place, Watch Post, Quiet Camp, Animal Picket). FL `08:503-529`. *This is the canonical instance of the engine-level **Success Menu** (`00 §4`): each surplus ⚔ on a downtime/long-process roll buys one player-declared quality of the output.*
- **Failure** = you still set up camp, but the GM makes a **hidden roll on the Failed Camp Liability table** (Exposed, Smoky, Wet, Disordered, Poor Fire, Bad Ground, Bad Hygiene, Vermin, Noisy) — a weakness that bites when the night is tested by cold, weather, watch, or danger; a 66 escalates to **Trouble at Camp** (Savage Animal, Lost/Broken Gear, Fire!). FL `08:531-553`.
- **Watches:** the Night divides into up to three watches; standing watch without sleeping in the last six Quarter Days makes you SLEEPY; a campfire gives full fire/light the first watch, half thereafter unless banked/tended. FL `08:511-515`.

**West — Making Camp as a single Nature roll with a pursuit-evasion use.** To find a sheltered, safe, hidden camp takes a **Nature roll** (can be a Group roll with help). Extra ⚔ beyond the first give **−1 to pursuers' HAWKEYE** to find the camp — but **a fire (for warmth/cooking) gives pursuers +3 to HAWKEYE**, a sharp trade-off. Failure means anyone relying on the camp for rest suffers: no sleep → **Exhausted**, or too cold → **Freezing**, or both (GM's call). West `06-life-in-the-old-west.md:1277-1281`. Watch is procedural: night herders ride two-hour watches, singing to keep stock calm, listening for the wrong sound. West `15:152-155`.

**Generic abstraction — "the camp procedure":** The recovery point of the day, gated by a Survival/Nature roll, with a **success ladder** (basic camp → bonus recovery/concealment/improvements) and a **failure cost** (bad camp = lost recovery or hidden liability). Three shared elements: (1) camp as the *healing gate* — you recover here, not on the march; (2) camp as *concealment* — a good camp hides you; a fire exposes you (West's +3 HAWKEYE, FL's enemy-Scouting-vs-camp-⚔); (3) camp as *watch obligation* — someone must trade sleep for security.

**Design knobs:** (1) **failure model** — FL's hidden-liability table (mechanical, produces bad-camp *flaws*) vs West's condition-on-fail (Exhausted/Freezing) vs a simple "no recovery"; (2) **camp improvements** (FL's pick-list) — Optional depth that rewards a high roll; (3) **fire-vs-concealment trade-off** — both encode it (General for stealth-heavy games). **Layer:** a camp-as-recovery-gate roll is **General**; the improvement pick-list and the hidden-liability table are **Optional** (depth dials).

## 10. Rest, sleep, recovery shifts, and downtime

**FL — REST, SLEEP, and the resource-die recovery loop.** REST recovers damage; SLEEP (≥1 Quarter Day/day or you become SLEEPY) automatically counts as REST. Interrupting REST/SLEEP by combat voids it. FL `08-journeys.md:555-634`. Recovery is **resource-driven**: once per Quarter Day take a 15-minute **short break** (allowed even mid-activity) and roll a resource die to restore an attribute — **Strength ← food/alcohol; Agility ← water; Empathy ← liquor/chef-food; Wits ← tobacco; Willpower ← narcotics** (capped by potency). FL `08:559-573`. So the road's healing economy *is* its supply economy. Sleeping on **bare ground** skips MAKE CAMP: each PC rolls Survival to find a spot (fail = no sleep → SLEEPY) and suffers COLD with no fire; at HEAT ≤0, bare-ground Endurance rolls auto-fail. FL `08:630-634`. **TRAIN** (needs XP + teacher, or a Wits roll), **CRAFT** (full day = 2 Quarter Days), **REPAIR** (≤3 items/Quarter), and **EXPLORE** (journey pauses at a site; can't REST/SLEEP the same Quarter) round out the non-combat block. FL `08:614-620, 665-667`.

**FL — settlement downtime menu.** Inside a settlement, the *same* Quarter-Day-pick-one-activity architecture runs a downtime menu: **ASK AROUND** (info; Manipulation/Insight/Lore/Scouting, difficulty ladder by target), **SEEK WORK** (two Quarter Days: find + do; a D6 Available-Work table, pay by ⚔), **PETITION** authority (access/militia/commissions, gated by Standing), **TRADE**, **REPAIR AND CRAFT**, **CAROUSE** (spend silver → recover WP + contacts + gossip), **HEAL**, **REST**, **TRAIN**. FL `08-journeys.md:1022-1234`. The notice board (D6 notices by settlement size; categories Clearing/Escort/Delivery/Recovery/Investigation/Labor; flat/advance+bounty pay structures) and the Reputation/Standing/Hospitality system make settlements a *downtime economy* parallel to the travel economy. FL `08:686-1009`.

**West — rest and the downtime rhythm.** West's rest is lighter in the core travel rules (Making Camp failure → Exhausted/Freezing; a decent camp enables a night's rest), and its downtime weight sits in **procedural reference** (the order of camp work: fire, beans/biscuit/bacon/coffee, pitching/striking camp, picketing, watch) and in the **competence** framing — a working hand *does* these things every day, and the procedure is the texture. West `15:126-160`. Hunting-as-profession (Chapter 11) functions as a downtime/economic activity: the hide hunter's season, the market hunter's weekly take, the trapper's line — these are *campaign-scale* downtime with economics rather than per-block rolls. West `11:199-308, 393-453`.

**Generic abstraction — "recovery + downtime":** Two layers:
- **Recovery (per block):** REST/SLEEP as the healing gate; the **currency of recovery** is the design choice — FL makes it *supply* (food/water restore attributes via resource dice), West makes it *conditions/competence* (a good camp clears Exhausted/Freezing). The over-exertion valve (§6) and the recovery loop are mirror images: pushing costs body; resting + supply restores it.
- **Downtime (per settlement/season):** a *second* activity-menu architecture for "not on the road" — info, work, trade, craft, carouse, train, petition. FL formalizes this as a Quarter-Day menu identical in structure to the travel menu; West leans on profession/economics and procedure.

**Design knobs:** (1) **recovery currency** — supply-dice (FL) vs condition-clear (West) vs attribute-regen; (2) **bare-ground / no-camp penalty** — Optional pressure; (3) **formal downtime menu** (FL's settlement menu) — a strong, transferable structure that mirrors the travel menu; (4) **profession-scale downtime** (West's hunt economics) — for games where the character's *job* is the campaign. **Layer:** REST/SLEEP as recovery gate = **General**; the resource-die recovery loop = **Optional**; the settlement downtime menu = **General** (highly transferable); TRAIN/CRAFT/REPAIR = **General** menu rows.

## 11. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Spatial model** (central dial) | Hex-crawl (10 km tiles, per-tile navigation + mishaps) | Pointcrawl (miles/Shift between points, rush roll) | Exploration depth vs prep/speed | Hex for sandbox exploration & fog-of-war; pointcrawl for trail/pursuit drama & fast pacing |
| **Time block** | 4 Quarter Days (Morning/Day/Evening/Night) + daily checklist | Shift (count loose) | Structured attritional day vs flexible block | Quarter Day when the *day* should feel like a series of costs; Shift for lighter pacing |
| **Activity-menu formality** | 14-row formal menu, solo/shared tagged | ~6–8 implicit jobs + mounted/animal labor | Tight labor puzzle vs genre-textured jobs | Formal menu when travel is the game; implicit when travel is connective tissue |
| **Navigation cost** | Survival roll **per hex entered**; fail = mishap table | One rush roll/block; Trouble halts progress | Mechanical per-tile tax vs narrative per-block tax | Per-tile for exploration; per-block for drama |
| **Over-exertion valve** | Forced march: Endurance, Agility damage + SLEEPY | Rush: MOVE/Animal Handlin', +50% or Trouble halt | Body-tax vs progress-tax | Match the harm model (FL body, West Trouble) |
| **Weather system** | Morning D6 table (Wind/Rain/Temp) + HEAT/TEMP expanded + clothes/gear | Regional-killer reference + Trouble/condition triggers | Mechanical grind vs dramatic scenes | Table for attritional survival; reference for dramatic, GM-discretion weather |
| **Felt-vs-actual temperature** | HEAT/TEMP split + seasonal base + clothes/sleeping-gear modifiers | Implicit (heat/cold → Freezing/Heatstroke) | Realism + bookkeeping vs simplicity | HEAT/TEMP only for survival-focused games; omit otherwise |
| **Food tracking** | Resource Dice, daily roll-down, spoilage-by-HEAT | Scene-level scarcity + profession/trap subsystem | Mechanical attrition vs color + mechanics | Resource Die when supply is load-bearing; profession when the hunt is the story |
| **Food-as-healing-currency** | Yes — short break restores attributes via food/water/etc. | No (recovery via camp clearing conditions) | Supply = survival vs supply = flavor | Wire food to healing for hard-survival games |
| **Camp failure model** | Hidden Failed-Camp-Liability table (flaws) + Trouble at Camp | Condition on fail (Exhausted/Freezing) | Mechanical flaws vs condition tax | Liability table for rich camp play; condition for speed |
| **Camp improvements** | Pick-list (Banked Fire, Dry Shelter, Watch Post…) | (none formal) | Rewards high roll / adds prep | Include for survival-craft depth; omit for lean play |
| **Fire-vs-concealment** | Enemy Scouting must beat camp ⚔ | Fire = +3 to pursuers' HAWKEYE | Both encode the stealth/camp trade-off | General for any stealth-relevant game |
| **Downtime architecture** | Formal settlement menu (Ask/Work/Petition/Trade/Carouse/Heal/Train) + notice board + Reputation | Profession/economics + procedural reference | Quarter-Day downtime economy vs job-as-campaign | Formal menu when settlement play matters; profession when the job is the campaign |
| **Mishap model** | Extensive D6/D66 mishap tables per activity | Trouble system (narrative) | Mechanical tax vs narrative tax | Mishap tables for granularity; Trouble for speed (consistent with `00-engine-core.md` §6) |

## 12. Dials and instantiation recipe

Each dial has FL and West as two calibrated points. To build a new game's journey engine, set each dial.

1. **Spatial model** — hex-crawl / pointcrawl / hybrid (named points on a hex map). *(Sets exploration depth vs pacing. The single most consequential travel decision.)*
2. **Time block** — Quarter-day (4/day + checklist) / Shift (loose) / watch. *(Sets how granular the attritional day feels.)*
3. **Activity-menu breadth** — full 14-row / lean ~6 / genre set (add mounted labor, urban jobs, ship stations…). *(Sets the labor-puzzle complexity.)*
4. **Solo-vs-shared tagging** — which jobs one PC monopolizes (pathfinder, lookout, skipper). *(Forces role assignment each block.)*
5. **Navigation cost** — per-tile roll+mishap / per-edge rush+Trouble / none (known route). *(Match to the spatial model.)*
6. **Over-exertion valve** — forced-march (Endurance, damage, sleep loss) / rush (MOVE/Animal Handlin', Trouble halt) / none. *(Makes "push on or camp" a real decision.)*
7. **Weather generation** — morning D6 table / GM-discretion + reference / none. *(Deterministic grind vs dramatic scenes.)*
8. **Weather depth** — base table only / HEAT-TEMP felt-vs-actual + seasonal + clothes+gear / condition-only. *(Realism vs bookkeeping.)*
9. **Food tracking** — Resource Die (daily roll-down) / scene scarcity / profession economics / none. *(How load-bearing is supply?)*
10. **Food-as-healing-currency** — on (resource-die restore on short break) / off (recovery via rest/conditions). *(On = survival; off = supply is flavor.)*
11. **Camp failure model** — hidden liability table / condition-on-fail / no-recovery / none. *(Rich camp play vs speed.)*
12. **Camp improvements** — pick-list (fire/shelter/beds/watch post…) / none. *(Rewards high MAKE CAMP rolls.)*
13. **Fire-vs-concealment trade-off** — on (fire exposes camp) / off. *(For any stealth-relevant game.)*
14. **Downtime architecture** — formal settlement menu + notice board / profession-scale economics / none. *(A second activity-menu for "not on the road.")*
15. **Mishap model** — D6/D66 mishap tables per activity / Trouble system / hybrid. *(Mechanical vs narrative failure tax — keep consistent with the core loop's push-cost model, `00-engine-core.md` §6.)*

**Instantiation recipe (any genre):**
1. **Pick the spatial model (dial 1)** — this single choice does more to set the feel of travel than any other. Hex-crawl = exploration is the game; pointcrawl = traversal is connective tissue.
2. **Set the time block (dial 2) and build the activity menu (dials 3–4)** — the menu is the load-bearing structure; define movement, navigation, security, supply, and recovery jobs, and tag which are solo. Ensure movement, navigation, watch, and forage are *mutually exclusive* so the party is always short of hands.
3. **Choose the over-exertion valve (dial 6)** consistent with the core loop's cost model — body-tax (FL-style) pairs with bane-self-harm; progress-tax/Trouble (West-style) pairs with currency-spend. (`00-engine-core.md` §6.)
4. **Set weather depth (dials 7–8)** to your survival emphasis — full weather table + HEAT/TEMP for hard-survival; reference + Trouble for dramatic.
5. **Decide food tracking (dials 9–10)** — if survival is the genre, wire food to healing (FL); otherwise keep supply as scene pressure.
6. **Set camp (dials 11–13)** and the **downtime architecture (dial 14)** — a downtime menu mirroring the travel menu turns settlements into a parallel economy.
7. **Keep the mishap model (dial 15) consistent** with the failure-pressure layer of the core loop.
8. **Validate** the labor puzzle: in a typical block, can a 3–4 PC party move, navigate, watch, *and* forage? If yes, the menu is too generous; tighten the solo tags or the stacks-with-HIKE list.

## 13. Design intent

The journey engine exists to make **logistics a form of play.** Specifically:

- **The activity menu distributes the party's labor** so that *every PC has a travel job* and the party is perpetually short of hands. Because movement, navigation, watch, and supply are mutually exclusive demands, "do we push on or stop to forage?" is not flavor — it is a resource-allocation decision made every block. This is the most transferable artifact: a fixed menu of jobs, one per PC per block, balanced so the party can never do everything at once.
- **The over-exertion valve + the recovery loop are mirror images** — pushing on costs body/beasts/time, and resting restores it (in FL, *via the supply you foraged*). This is what keeps travel from being a death spiral: you can always trade distance for recovery, and recovery is gated by supply, which is gated by the forage/hunt activities you sacrificed movement to take.
- **Weather + food turn movement into attrition**, which makes "do we push on or camp" a real decision rather than narration. The environment, not just enemies, is a source of pressure — FL by a morning table that taxes every activity; West by rendering the country as an indifferent antagonist whose weather kills.
- **The spatial model is the central dial** because it determines *what travel is about*: in a hex-crawl, travel is the *discovery of unknown space* (the map is treasure); in a pointcrawl, travel is the *traversal of a known route under attrition* (the points are the story). Same spine, opposite feel — the engine's proof, again, that **the same loop produces opposite tones by swapping one dial.** FL's hex-crawl makes a game where *the wilderness itself* is the dungeon; West's pointcrawl makes a game where *the distance between waters* is the antagonist.
- **Don't roll for trivial travel** (both books, by structure): the engine only earns its attrition when the journey has stakes — when cold, hunger, pursuit, or the unknown make each block matter. A journey with no pressure should be summarized, not crawled, or the activity menu and weather table flood the session with bookkeeping without drama.
- **The downtime menu mirrors the travel menu** — settlements get their own pick-one-activity-per-block architecture (info, work, trade, craft, carouse, train, petition), so "not on the road" is still structured play, not a cut-scene. This parallel is what lets a campaign breathe between expeditions without losing the engine's rhythm.
