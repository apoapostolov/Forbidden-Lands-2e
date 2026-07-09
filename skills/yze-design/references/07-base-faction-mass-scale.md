<!-- markdownlint-disable MD013 -->

# Base, Faction, Mass-Combat — The Downtime Org Layer

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** The org-lifecycle pattern and the scale-escalation ladder are the spine; every base/business/band/company/faction is an instance of one genre-neutral pattern.

## Contents

1. Source provenance
2. Abstraction target
3. The shared pattern: founding → functions → upkeep → events → scale
4. Stronghold (FL)
5. Holdings and Territory
6. Riches in the Land
7. Town, Property, and Outlaw Band (West), including outlaw operating sheet
8. Mercenary Company (FL), including roster-org and host operating sheets
9. Factions, Legacies, and the Faction Turn (FL)
10. Mass combat and sieges (FL)
11. The scale-escalation ladder
12. Divergence rows (FL vs West)
13. Rule Choices and Build Recipe
14. Design intent

## Source provenance

**Forbidden Lands 2E:**
- `01-corebook/09-the-stronghold.md` (~2,470 lines) — establishing, housing/HOUSING score, stronghold sheet, base effects (rest + WP), flaws, random events, functions, hirelings, upkeep.
- `01-corebook/09-the-stronghold.md` — **Control of the Land** and **Prospecting and Resource Extraction**: territory, settlements, families, food support, claims, developed land, roads, watchtowers, outposts, control checks, prospecting, deposit dice, depletion, recovery, extraction, hauling.
- `01-corebook/12-mercenaries-of-forbidden-lands.md` (~4,890 lines) — mercenary company system: bands, size tiers, Morale, recruitment, pay/provisions, village extortion/tribute, contracts/bounties/kidnapping, campaign life (DRILL/camp/discipline), Named Men, Hired Casters, wanted men, atrocities, War Room function, Host Play, 7 premade bands.
- `01-corebook/14-traderoads-of-the-forbidden-lands.md` — caravan/traderoad economy, Warehouse function.
- `02-gamemasters-guide/11-politics-of-the-forbidden-lands.md` (~2,310 lines) — faction engine: creation/tiers/sheet, Treasury/Stores/Labor/Levy/Retainers, Pillars (Mandate/Force/Reach/Hearth) + Practices, 9 Legacies, Campaign Points, Agents & Advisors, faction rolls, Settlement bonds, Faction Turn, faction acts, fallout, burden, handoff, revenue, tribute, retainers/levy/mercenaries, armies, logistics, politics-to-war, premade factions.
- `02-gamemasters-guide/12-battles-and-sieges.md` (~1,790 lines) — mass combat: troop dice, arms/armor, battle sequence, special combat conditions, Sieges (blockade/breach/relief), supplies, campaign movement, disease, aftermath, new war talents, example units.

**Tales of the Old West 2E:**
- `01-corebook/06-life-in-the-old-west.md` — Outfits/Businesses (Business Types Table, proprietor/employee/investor, Turn of the Season Business Rolls), Property & Land (Property Status, Location Type, Features, buying/selling, auctions, Homestead Act).
- `01-corebook/08-campaigns-in-the-old-west.md` — Your Town (Aspects: Farming/Mercantile/Natural Riches/Law/Civic/Welfare/Prosperity, Amenities, Settlement Points), Turn of the Season (Business/Congregation/Personal/Town Fortune rolls), Dynasty.
- `01-corebook/11-outlaws-of-the-old-west.md` — Outlaw Band rule set: scale, leadership, cohesion, resources (refuge/fence/horsestock/provisions), Town Tags, Band Action Checks, recruitment/loyalty, shares & loot, hideout, Scores, Wanted status & pursuit, Hideout Life.

## Abstraction target

Abstract the **downtime org layer** — every "thing a player or faction owns and runs between adventures" — into one genre-neutral pattern with five beats: **founding → functions → upkeep → events → scale escalation.** FL instantiates this richly (Stronghold + Mercenary Company + Factions + Mass Combat, all interlocking); West instantiates it at the personal/small-org scale (Business/Property + Town + Outlaw Band). The deliverable is the **org lifecycle pattern** and a **scale ladder** (solo → party → band → company → faction → army → polity) with explicit guidance on which rungs to enable for which genre/campaign length.

Apply the Abstraction Ladder to: the lifecycle pattern, each build, and the scale ladder.

## 3. The shared pattern: founding → functions → upkeep → events → scale

This is the file's core abstraction. Every org in both games — a cleared dungeon converted to a castle, a bought saloon, a band of hired swords, a faction of allied settlements, a robber gang, the town the players are trying to grow — runs on the **same five-beat lifecycle.** The beats are genre-neutral; the choices on each beat are where genre is set.

### Beat 1 — Founding

**FL Stronghold:** Established by *clearing* a lair/ruin and claiming it, or by *building* on chosen ground. Building requires a **CRAFTING** roll; failure introduces a **Flaw** rolled on a D6 table (Collapsed Roof, Cramped, Dark, Defective, Haunted, Hidden Back Door). FL `09-the-stronghold.md:17-22`, `:66-77`.

**FL Mercenary Band:** Formed by naming it, naming a leader, and recruiting **3+ fighters**. The band does not exist as a tracked org until those three things are done. FL `12-mercenaries-of-forbidden-lands.md:76-83`.

**FL Faction:** Created through a 9-step sequence: seat → basis of rule → tier → four pillars → practices → legacy → holdings → resources (Treasury/Stores/Labor/Levy/Retainers) → aim → weakness. FL `11-politics-of-the-forbidden-lands.md:189-203`.

**West Business/Property:** Founded by investing **Capital** (1 Capital = $250). A proprietor starts or buys a business from the Business Types Table; a landowner buys property (Homestead Act: $14 for 160 acres). West `06-life-in-the-old-west.md:27-49`, `:157-186`, `:254-265`.

**West Outlaw Band:** Founded by a leader, a hideout, and **3+ outlaws**. The hideout is the founding asset — without it the band has no org status. West `11-outlaws-of-the-old-west.md:23-34`.

**Abstract pattern — founding:** An org is founded by satisfying a small **founding predicate** (a cleared site / spent Capital / recruited minimum headcount / a seat + a basis of rule). The predicate is a gate: the org is not tracked until it is met. The founding roll (when one is required) carries a **failure tax** that produces a *permanent embedded flaw* — the org is born marked by the conditions of its birth. **Layer:** General (the predicate gate); the founding-flaw roll is Optional (a grit choice — West does not tax business-founding this way).

### Beat 2 — Functions

**FL Stronghold:** A function is a **built improvement** (Apiary, Forge, Dungeon, Library, Marketplace, Temple, Workshop, etc. — 60+ in the table) that grants a rules effect, often staffed by a worker. Each costs raw materials, tools, time, and sometimes a prerequisite function or specialist. Functions convert downtime labor into **ongoing capability** (crafting, research, recruitment, defense, food production). FL `09-the-stronghold.md:285-355`.

**FL Mercenary Band:** The band's "functions" are its **capabilities as a force**: contracts it can take (Patrol, Escort, Clearing, Raid, Garrison, Intelligence, Caster), training upgrades (DRILL via Training Grounds), and special assets (Hired Casters). FL `12-mercenaries-of-forbidden-lands.md:965-1023`, `:1413-1433`.

**FL Faction:** The faction's functions are its **16 Practices** (grouped under four pillars) and its **9 Legacies** (talent-like drilled customs of power). Practices are what the faction *can do*; legacies are what it *does exceptionally well*. FL `11-politics-of-the-forbidden-lands.md:380-552`.

**West Business:** The business's function is its **key ability** (Bartender mixes drinks for rumor access; Blacksmith crafts/repairs; Doctor heals; Newspaper publishes). Each Business Type in the table grants a specific rules hook. FL `06-life-in-the-old-west.md:157-186`.

**West Town:** The town's functions are its **Amenities** — built improvements (General Store, Church, Saloon, Schoolhouse, Bank, Hotel, etc.) ranked by minimum Civic rank, each modifying the town's Aspects. FL `08-campaigns-in-the-old-west.md:128-253`.

**West Outlaw Band:** The band's functions are its **resources** (Refuge network, Fence access, Horsestock, Provisions die) and the operations it can run (Band Action Checks, Scores). FL `11-outlaws-of-the-old-west.md:128-276`, `:354-423`.

**Abstract pattern — functions:** Functions are **discrete, named improvements** the org acquires over time, each converting downtime resources (materials, labor, coin, stores) into a **persistent rules capability**. They are the org's "skill list." Acquiring a function has a cost ladder (materials + time + prerequisites); the function then pays out each downtime cycle. **Layer:** General.

### Beat 3 — Upkeep

**FL Stronghold:** Requires **upkeep** (food/materials/labor) per cycle; **Lacking Upkeep** triggers a D6 table (Abandonment, Decay, Mutiny, etc.). Hirelings/Residents/PCs/Slaves form the work force; **non-payment** of hirelings triggers its own D6 table (strike, theft, desertion). **Unguarded** strongholds trigger a D6 table of misfortunes. FL `09-the-stronghold.md:146-155`, `:255-272`.

**FL Mercenary Band:** Must be **paid and fed**. Pay model is Retainer (weekly) or Mission (daily). Feeding uses forager output by terrain. **Field Non-Payment** triggers a D6 table (desertion, mutiny, desertion of Named Men). FL `12-mercenaries-of-forbidden-lands.md:363-392`, `:493-526`, `:555-568`.

**FL Faction:** Pays upkeep through **pillar recovery** (1 point per Season Turn, paused during Campaign), **Treasury/Stores** backing tracks (Bare/Thin/Sound/Deep) that can step *down* under strain, and **Burden** on settlements (Light/Hard/Crushing/Ruinous) that worsens Standing and Feud. FL `11-politics-of-the-forbidden-lands.md:273-291`, `:893-899`, `:1357-1366`.

**West Business:** Pays upkeep through the **season Business Roll** (key ability + help + Competition + Law + aspect modifiers), with a Business Bonus/Penalty D66 table on the line; **Going Bust** is the failure state. FL `08-campaigns-in-the-old-west.md:555-643`.

**West Town:** Pays upkeep through the **Turn of the Season** rolls; an Aspect driven to 0 means **the town fails**. FL `08-campaigns-in-the-old-west.md:522-535`, `:537-545`.

**West Outlaw Band:** Pays upkeep through the **Provisions resource die** (D6→D12, depletes), Horsestock upkeep, and the constant pressure of **Wanted** level. FL `11-outlaws-of-the-old-west.md:232-276`.

**Abstract pattern — upkeep:** Every org carries a **resource obligation** it must discharge each downtime cycle (food/wages/stores/pillar-points/aspect-tallies). **Failing upkeep triggers a degeneration table** — attrition, desertion, decay, mutiny, or collapse. Upkeep is the engine that keeps the org *alive but not free*: it converts "we own a thing" into "we must feed the thing." **Layer:** General. The degeneration table is the upkeep layer's equivalent of the core loop's bane — *latent pressure that activates when the org is starved.*

### Beat 4 — Events

**FL Stronghold:** **Random Events D6** between sessions (a monster lairs nearby, a traveler arrives, a rival eyes the site). FL `09-the-stronghold.md:79-90`.

**FL Mercenary Band:** Events arise from **MORALE triggers** (the Grievance Difficulty ladder, Argument & Escalation stages, Blood Oaths) and the **Feud Track** (0 Cold Peace → 4 Mustered War). FL `12-mercenaries-of-forbidden-lands.md:106-194`, `:801-811`.

**FL Faction:** Events are the **Faction Turn** itself — the procedural checks (Community, Development, Prosperity/Logistics, Decree, Acts, Fallout/Burden/Handoff) that fire every Season Turn or Campaign Week depending on Mode of Rule. **Fallout** has its own D66 table. FL `11-politics-of-the-forbidden-lands.md:982-1091`, `:1326-1347`.

**West Business/Town:** Events are the **Business Bonus/Penalty D66**, **Personal Fortunes D66**, and **Town Fortune** rolls at the Turn of the Season. FL `08-campaigns-in-the-old-west.md:631-643`, `:706-742`.

**West Outlaw Band:** Events arise from **Cohesion tests**, **Loyalty** breaking points, and **Wanted** pursuit. FL `11-outlaws-of-the-old-west.md:62-122`, `:508-533`.

**Abstract pattern — events:** Between downtime cycles, the org is *subject to* random/procedural events it did not choose — threats, opportunities, internal friction, or external pressure. Events are the **second agency the world has** (the first is upkeep degeneration). Together, upkeep + events make the org a *living, threatened* thing rather than a static stat block. **Layer:** General (events fire every cycle); their *source* (random table vs procedural turn vs driven by a tracked relationship like Feud/Cohesion) is a choice.

### Beat 5 — Scale escalation

**FL:** The whole point of FL's design is that an org can **climb rungs**: a Stronghold can acquire a Mercenary Company as a function (War Room, garrison); a Mercenary Company can become a Faction's retainer or its field army; a Faction's levy and mercenaries become an Army that resolves in Mass Combat. Each rung re-uses the same lifecycle beats at a larger turn scale. FL `12-mercenaries-of-forbidden-lands.md:916-943` (Allegiance 0→4), `11-politics-of-the-forbidden-lands.md:1191-1201` (Hire Mercenaries writes the band into the army roster).

**West:** West deliberately *caps* escalation — the orgs top out at the town/band scale. A Business stays a Business; a Town grows via Aspects but never becomes a faction with a turn; an Outlaw Band tops out at Outfit (16-30). There is no faction-turn layer and no mass-combat engine. FL `08-campaigns-in-the-old-west.md:69-126`, `11-outlaws-of-the-old-west.md:36-45`.

**Abstract pattern — scale escalation:** An org can be promoted to a higher rung where its lifecycle is re-set by choice (larger turn scale, bigger upkeep, wider event scope, stronger functions). The **ladder** is the explicit deliverable of §9. Crucially: **the five beats do not change between rungs** — only their *amplitude* (turn length, currency size, threat radius). This is what makes FL's interlocking rule sets one engine rather than four. **Layer:** General (the ladder exists); *which rungs are enabled* is the central genre/campaign-length choice (see §9, §11).

## 4. Stronghold (FL)

The Stronghold is FL's canonical "base" — the party's home, workshop, and the first org most campaigns acquire.

**Source instance (Abstraction Ladder):**
- **Founding:** Clear a site or build; CRAFTING roll; Flaw on failure. FL `09-the-stronghold.md:17-22`, `:66-77`.
- **Functions:** HOUSING score is the load-bearing abstraction — **100 units of wood/stone = 1 HOUSING**, capping who can live there; the Functions table (60+ improvements) is the org's expandable capability set. Building table spans Cottage (2 wood) to Palace (520 stone). A **Master Builder** auto-succeeds at construction, removing the flaw risk. FL `09-the-stronghold.md:27-47`, `:285-355`, `:228-230`.
- **Base effects (the "why you want one"):** Undisturbed rest **and** +1 WP per PC per session while the stronghold stands. The org *generates Willpower/Faith* for its owners — this is the economic reason a party wants a base at all. FL `09-the-stronghold.md:55-58`.
- **Work force:** Hirelings (paid), Residents (free, tied to the site), PCs (free, limited time), Slaves (free, reputation cost). Each function names the worker type it needs. FL `09-the-stronghold.md:157-194`.
- **Upkeep:** Per-cycle; Lacking Upkeep D6 (Abandonment/Decay/Mutiny); Non-payment D6; Unguarded D6. Three separate degeneration vectors — *resourcing, payroll, and security* are each tracked independently. FL `09-the-stronghold.md:146-155`, `:240-272`.
- **Events:** Random Events D6 between sessions. FL `09-the-stronghold.md:79-90`.

**Abstract pattern:** The Stronghold is the **rung-1 org**: a place-bound, player-owned capability hub whose entire purpose is to (a) bank downtime labor as permanent functions, (b) generate the Willpower/Faith that powers adventure, and (c) be *threatened* by three independent upkeep vectors so that "going home" is never free. The **base-effects-grant-Willpower/Faith** link is the design's keystone — it binds the downtime layer to the adventure layer economically. **Layer:** General (the rung-1 org pattern); the three-independent-upkeep-vectors model is Optional (a granularity choice — West collapses payroll and resourcing into one Business Roll).

## 5. Holdings and Territory

Holdings and Territory is the generic name for FL's Control of the Land rules. It turns the land around a base into a playable map of claims, families, workers, stores, roads, watchtowers, contested ground, and settlement support. It should be used whenever the campaign is not only about owning a base, but about **making that base matter to the surrounding world**.

The same rules can skin as a frontier holding, noble estate, ranch, gang turf, headquarters, ship network, colony, temple precinct, military base, corporate district, salvage zone, family holdings, or occult lodge. The nouns change; the loop does not.

### 5.1 The holding sheet

| Field | What to record | Examples |
| --- | --- | --- |
| Holding | the central owned place | stronghold, ranch, carrier, headquarters, lodge, colony |
| Territory | the surrounding map or social space | hexes, streets, routes, districts, moons, departments |
| Control | 0-6 rating for how firmly the holding governs nearby ground | fear, law, patrol, legitimacy, logistics, sensors |
| Claims | places the holding says are "ours" | fields, mines, routes, docks, alleys, asteroid claims |
| Families | settled households or attached dependents | families, workers, tenants, crew households, cult cells |
| Workers | people available for labor | farmers, guards, rules, staff, pilgrims, drones |
| Stores | food, materials, wages, fuel, medicine, parts | see `08` for storage/economy |
| Roads | safe links between claims | roads, patrol routes, shipping lanes, tunnels, VPN paths |
| Watchtowers | warning/control points | towers, outposts, cameras, informants, buoys, listening posts |
| Contested ground | places with rival claim or dangerous absence | feud, monster lair, cartel turf, haunted wing, enemy sensors |

### 5.2 Territory states

| State | Meaning | What players can do there | What can go wrong |
| --- | --- | --- | --- |
| Wild | unclaimed, unknown, or ungoverned | explore, survey, hunt, hide, establish first contact | hazard, ambush, rival arrives first |
| Claimed | publicly marked as yours | collect light yield, patrol, build simple post | rival contests, workers refuse, claim mocked |
| Developed | worked and supported | produce, house families, support functions, raise defense | upkeep, sabotage, depletion, taxes |
| Contested | two or more powers can enforce a claim | negotiate, fight, spy, pay, fortify | feud, raid, lawsuit, blockade |
| Ruined | cannot produce until restored | scavenge, cleanse, rebuild, abandon | disease, curse, collapse, squatters |

**State rule:** claims do not become real because players write them down. A claim becomes real when the holding can feed it, reach it, watch it, and answer a challenge there.

### 5.3 Control score

| Control | Fiction | Mechanical posture |
| --- | --- | --- |
| 0 | no one believes the claim | cannot collect yield; rivals act freely |
| 1 | name on a post | can attempt claim checks, but all challenges are hard |
| 2 | occasional patrol or local respect | small yields; one active contested point at a time |
| 3 | ordinary control | default score for a serious holding |
| 4 | roads, watch, families, and reputation align | +1 to control checks in linked claims |
| 5 | firm rule | rivals need a plan, patron, or force to contest |
| 6 | unquestioned authority | only major event, betrayal, disaster, or army can break it |

**Control check:** roll Command, Survival, Craft, Persuasion, Lore, or another fitting skill when a claim is challenged. Add roads/watch/families/stores/help. On success, the holding keeps control. Extra successes may reduce cost, expose the rival, reassure families, or improve the claim. On failure, choose or roll trouble.

| Failed control check | Trouble |
| --- | --- |
| 1 | workers refuse, flee, strike, or demand protection |
| 2 | rival marks the claim and lowers Control by 1 until answered |
| 3 | stores are lost, spoiled, seized, or redirected |
| 4 | road/link is unsafe until patrolled or repaired |
| 5 | family loss, hostage, lawsuit, feud, scandal, or betrayal |
| 6 | claim becomes Contested or Ruined |

### 5.4 Claiming and developing

**CLAIM LAND.** To claim a place, spend one period scouting, marking, negotiating, or intimidating. Roll the fitting skill. On success, mark it Claimed and name the visible sign of ownership. Extra successes may add a contact, reduce first upkeep, find a resource, or learn a rival's weakness. On failure, the claim is known but not respected; mark a rival, hazard, or debt.

**DEVELOP LAND.** To develop a claim, assign workers/families, spend stores/materials, and spend a period. Roll Craft, Command, Survival, or the local profession skill. On success, mark it Developed and choose one yield: food, material, watch, road support, housing, reputation, market, or special resource. On failure, progress exists but gains a flaw: bad drainage, corrupt foreman, angry locals, poor soil, weak signal, hidden tunnel, legal dispute.

**BUILD A ROAD.** A road is any reliable link: trail, bridge, patrol route, rail, shipping lane, tunnel, courier line, comm relay, smuggling route. It connects two places and lets control, trade, messages, workers, and rescue move. Building requires a route survey, labor, materials, and a period. On failure, the road exists but is slow, exposed, toll-bound, seasonal, or dangerous.

**RAISE A WATCHTOWER.** A watchtower is any warning and authority post: tower, outpost, listening station, camera net, ranger cabin, shrine, beacon, buoy, informant house. It makes challenges visible sooner. On success, add +1 to control checks in nearby linked claims. On failure, it is blind in one direction, corrupt, poorly supplied, publicly hated, or easy to sabotage.

### 5.5 Families, workers, and stores

FL's families are a portable unit: not only relatives, but any attached households or dependents who make a holding real. In other genres, use workers, families, tenants, cells, crew households, pilgrims, staff, settlers, refugees, or citizens.

| Unit | What it gives | What it needs | What threatens it |
| --- | --- | --- | --- |
| Family | food production, local legitimacy, labor pool | food, protection, justice, shelter | hunger, raids, disease, grief |
| Specialist | unlocks a function or bonus | wage, workshop, status, safety | poaching, insult, better offer |
| Guard | control, watch, defense | pay, food, morale, leadership | non-payment, fear, corruption |
| Tenant/worker | production and upkeep | wage/share, tools, fair treatment | strike, flight, sabotage |
| Dependent | story gravity and moral stakes | care, medicine, shelter | hostage, illness, scandal |

**Family commitment rule:** a family or worker assigned to one claim cannot also staff another function that period. Labor allocation must bite.

### 5.6 Availability and settlement support

A holding surrounded by people can buy, hire, learn, and repair more easily. Treat settlement support as a die or score from D6 to D12, or 1-6 if the game avoids step dice.

| Support | Place | What is available |
| --- | --- | --- |
| D6 / 1-2 | hamlet, small crew, poor district | common goods, 1-2 workers, rumors |
| D8 / 3 | village, ship section, neighborhood | common goods, basic specialists, mounts/vehicles |
| D10 / 4-5 | town, station, major base | uncommon goods, tutors, mercenaries, repairs |
| D12 / 6 | city, capital, fleet hub | rare goods, masters, legal cover, large hires |

**Availability check:** when looking for goods, tutors, workers, mercenaries, legal help, rare parts, or patrons, roll the support die or rating. Success means the thing exists at ordinary cost. Failure means delay, price increase, rival claim, inferior quality, or a favor owed. Cross-load `08-gear-and-economy.md` when pricing matters.

### 5.7 Holdings and Territory turn

Run this once per month/season or whenever the holding matters.

1. **Weather the holding.** Pay upkeep: food, wages, stores, fuel, maintenance, justice, or public patience.
2. **Assign families and workers.** Each unit works one claim, function, road, watch, project, or defense.
3. **Choose one claim action.** Claim, develop, build road, raise watchtower, patrol, repair, negotiate, extract, recruit, relocate, or abandon.
4. **Check contested ground.** Each Contested claim triggers a control check or a negotiated concession.
5. **Collect yields.** Developed claims produce food, materials, coin, information, reputation, safety, recruits, or access.
6. **Roll event if pressure is high.** Trigger on low stores, unpaid workers, nearby rivals, failed checks, over-extraction, or long peace.
7. **Update the map.** Mark new states, roads, watch, families, rival moves, depleted sites, and hooks.

### 5.8 Holdings event table

| D66 | Event |
| --- | --- |
| 11-13 | A family asks for judgment between neighbors; unfair ruling costs Control. |
| 14-16 | Workers find something useful and dangerous while developing land. |
| 21-23 | A rival marks one of your claims and dares you to answer. |
| 24-26 | Stores spoil, burn, vanish, or are sold by a desperate worker. |
| 31-33 | A road fails: bridge out, patrol missing, courier killed, comms jammed. |
| 34-36 | A specialist offers service for a favor, protection, or rare tool. |
| 41-43 | Families threaten to leave unless food, justice, or safety improves. |
| 44-46 | A claim produces a windfall; choose profit now or invest in lasting growth. |
| 51-53 | Hidden occupants contest ownership: squatters, ghosts, gang, beast, old law. |
| 54-56 | The watch catches a threat early; act now for advantage or ignore at cost. |
| 61-63 | A public scandal, accident, or cruelty lowers Control by 1 until repaired. |
| 64-66 | A major power recognizes, taxes, attacks, blesses, or annexes the holding. |

### 5.9 Holdings validation

- A holding must need food/stores, labor, control, and routes; if one is missing, the system becomes free real estate.
- Claims must create both yield and responsibility.
- Roads and watchtowers must change the map, not just add passive bonuses.
- Families/workers must be useful enough to matter and vulnerable enough to protect.
- Control 6 should not mean invulnerable; it means only serious threats can move the score.
- Every non-fantasy skin must still answer: Who works here? Who believes this claim? Who contests it? What must be hauled?

## 6. Riches in the Land

Riches in the Land is the generic name for FL's prospecting and resource extraction rules. It handles veins, deposits, caches, fields, salvage, data vaults, fuel pockets, research samples, monster nests, relic sites, black-market stock, sacred groves, and any other find that can be harvested over time.

The loop is: **survey → find → size → work → yield → hauling → depletion → recovery or exhaustion.**

### 6.1 Survey procedure

**SURVEY.** Spend one travel block or downtime period searching a place for a specific kind of wealth. Roll the fitting skill: Survival for land, Lore for records/data, Craft for built materials, Scouting for surface signs, Persuasion for market rumors, Beast Handling for herds, Power skill for strange sources.

| Successes | Find |
| --- | --- |
| 0 | no useful find; mark false lead, hazard, rival, or lost time |
| 1 | common find; small deposit/cache/field, easy to work |
| 2 | significant find; useful for a holding or trade route |
| 3+ | rich find; valuable enough to attract rivals, law, monsters, claimants |

**Deep survey:** a second survey may be attempted only with new tool, better map, specialist, power, season change, or deeper access. Apply -1 unless the new method is clearly better. Failure creates attention or danger, not another blank.

### 6.2 Find types

| Find | Fantasy skin | Modern / sci-fi / other skins | Common skill |
| --- | --- | --- | --- |
| Stone/ore | quarry, iron, gems, old ruin | metals, rare earth, hull scrap | Craft / Survival |
| Fuel | coal, peat, pitch | oil, reactor fuel, batteries, oxygen | Survival / Lore |
| Food | field, herd, fishery, orchard | hydroponics, ration stock, protein vats | Survival / Beast Handling |
| Wood/fiber | forest, reeds, flax | polymers, cloth stock, ship timber | Survival / Craft |
| Relic | tomb, shrine, battlefield | alien ruin, archive, crime evidence | Lore / Scouting |
| Information | old map, witness, library | data vault, blackmail, research set | Lore / Insight |
| Influence | sacred ground, noble right | legal title, media access, patron list | Persuasion / Command |
| Living resource | monster nest, herbs, spirits | samples, organs, microbes, AI seed | Survival / Power |

### 6.3 Deposit die

Use a deposit die to show how much a find can yield before it is exhausted.

| Deposit die | Size | Campaign meaning |
| --- | --- | --- |
| D6 | small | one job, one project, one short route |
| D8 | useful | several periods; worth guarding |
| D10 | rich | holding-scale resource; rivals notice |
| D12 | great | campaign asset; politics forms around it |

**Sizing rule:** one success gives D6, two successes D8, three successes D10, four or more D12 unless the terrain/source cannot plausibly support it. Rare finds may start one die lower but be worth more per yield.

### 6.4 Working the find

| Method | Needs | Yield | Risk |
| --- | --- | --- | --- |
| Hand gathering | 1-3 workers, simple tools | low but quick | injury, weather, theft |
| Camp | workers, shelter, guard, tools | steady | upkeep, morale, claim dispute |
| Mine/quarry/lab | specialist, function, weeks/months | high | collapse, contamination, sabotage |
| Herd/field | families/workers, season, protection | seasonal | disease, drought, predators |
| Salvage | transport, tools, guards | variable | sharp debris, old defenses, rivals |
| Data dig | access, expert, storage | information yield | trace, corruption, legal heat |
| Sacred/strange harvest | rite, power, taboo handling | potent | mishap, Blood Price, guardian |

**Work roll:** once per period, roll the fitting skill plus workers, tools, roads, watch, and specialist help. Success produces yield. Extra successes may increase yield, reduce depletion, avoid hazard, improve quality, hide the operation, or learn a new lead. Failure produces less yield and trouble.

### 6.5 Yield menu

| Yield | Use |
| --- | --- |
| Food stores | feed families/workers, heal, trade |
| Material stores | craft, build, repair, sell |
| Fuel stores | travel, machines, heat, power |
| Coin/cash | liquid profit |
| Rare part | gate Strange Devices, vehicles, powers |
| Ingredient | +1 level, required rite, medicine, poison |
| Information | clue, map, blackmail, research progress |
| Claim strength | +1 to a future control check |
| Reputation | holding becomes known for this wealth |

### 6.6 Depletion and recovery

At the end of each season or after heavy exploitation, roll the deposit die.

| Roll | Result |
| --- | --- |
| 1-2 | step the deposit die down one size |
| 3-5 | stable; no change |
| 6+ | stable and reveals a lead, quality pocket, or recovery sign |

**Heavy exploitation:** if the find was worked by double labor, unsafe methods, forced workers, magic, machines beyond local capacity, or desperate wartime extraction, roll depletion twice and keep the worse result.

**Light touch:** if the find was worked only briefly, ceremonially, sustainably, or with expert care, skip the depletion roll once or roll with +1.

**Exhausted:** when a D6 steps down, the find is exhausted. It may still leave a ruin, scar, flooded mine, empty vault, poisoned field, angry families, or valuable infrastructure.

| Resource | Recovery possibility |
| --- | --- |
| stone/ore/relic | usually none without deeper survey |
| forest/fiber/food | recovers after seasons/years if protected |
| herds/living samples | recovers if breeding grounds survive |
| data/influence | recovers only through new access or changed politics |
| strange source | recovers by rite, sacrifice, alignment, or not at all |

### 6.7 Hauling

A find is not wealth until it can be moved, guarded, stored, or used in place.

| Hauling question | If no |
| --- | --- |
| Is there a road/link? | slower transport, more mishaps, lower yield |
| Is there capacity? | yield stays on site or must be abandoned |
| Is there storage? | spoilage, theft, weather, corruption |
| Is there guard? | rivals, monsters, law, workers steal |
| Is there buyer/use? | price falls, stockpiles clog, debt rises |

**Hauling check:** roll when moving bulk through danger. Success gets the yield home. Extra successes reduce loss, avoid notice, improve price, or find return cargo. Failure costs a share of yield and creates a road, guard, vehicle, or rival problem. Cross-load `08` for transport ladders and cargo.

### 6.8 Riches event table

| D66 | Event |
| --- | --- |
| 11-13 | The find is poorer than believed; step die down or accept lower yield. |
| 14-16 | Workers discover a side chamber, witness, fossil, relic, body, or clue. |
| 21-23 | Rival claimants arrive with law, family story, gang force, or sacred right. |
| 24-26 | Accident: cave-in, fire, contamination, beast attack, equipment break. |
| 31-33 | The haul spoils, leaks, corrodes, corrupts, or attracts predators. |
| 34-36 | A worker vanishes with a sample, map, secret, or rare part. |
| 41-43 | A buyer offers a rich price with ugly conditions. |
| 44-46 | The operation reveals a road, ruin, vein, password, or hidden patron. |
| 51-53 | Heavy work damages the surrounding holding; lose Control unless repaired. |
| 54-56 | The find is taboo, illegal, cursed, classified, or owned on paper. |
| 61-63 | A rich pocket appears; increase yield now but roll depletion twice. |
| 64-66 | The find changes the campaign map; a faction, army, church, corp, or monster moves. |

### 6.9 Riches validation

- Finds must require surveying, working, hauling, and depletion; skipping any step makes free wealth.
- Rich finds must attract attention.
- Heavy exploitation must be tempting and dangerous.
- The deposit die should create uncertainty without requiring unit-count accounting.
- A find that produces rare parts, ingredients, or information should gate other systems rather than simply print money.
- If the operation out-earns adventuring safely, add rivals, depletion, storage, guards, law, disaster, or debt.

## 7. Town, Property, and Outlaw Band (West)

West runs the same five-beat lifecycle, but at personal/small-org scale and with the rungs above "town" deliberately absent.

### Business & Property (West)

**Source instance:**
- **Cash vs Capital:** Two-currency model. **$250 = 1 Capital.** Cash is adventure currency; Capital is the *illiquid investment* that founds and grows orgs. Capital is gained by starting/investing in a business, buying property, or liquidating. West `06-life-in-the-old-west.md:11-49`.
- **Founding:** Proprietor (owns/operates), Employee (works for wage + skill access), or Investor (passive capital for share of profit). Business Types Table: 24 types each with a key ability and prerequisites. West `06-life-in-the-old-west.md:133-186`.
- **Functions:** The business's **key ability** is its function. **Property Features** (Barn, Forge, Garden, Library, Oven, Stables) are built improvements — directly analogous to Stronghold functions. **Property Status** (0-8) is a reputation modifier; **Location** (8 types) sets context. West `06-life-in-the-old-west.md:230-242`, `:254-307`.
- **Upkeep:** The **season Business Roll** (key ability + help +3 + Competition + Law + relevant aspect). Failure → Business Bonus/Penalty D66; sustained failure → **Going Bust**. Wages paid to employees. West `08-campaigns-in-the-old-west.md:555-643`, `06-life-in-the-old-west.md:202-210`.
- **Events:** Business Bonus/Penalty D66, Personal Fortunes D66 at the Turn of the Season. West `08-campaigns-in-the-old-west.md:631-643`, `:706-742`.

**Abstract pattern:** West's **Capital** is the clean two-currency model of org-ownership: liquid adventure money vs illiquid org-founding money. This is the single best-expressed choice in the whole layer — FL has no equivalent (silver buys everything, functions are paid in materials/labor), which makes FL's base-building more *crafting-driven* and West's more *investment-driven*. **Layer:** General (a Capital-like illiquid currency is recommended for any West-style game); Optional for FL-style crafting-driven games.

### Your Town (West)

**Source instance:**
- **The town as a character:** Six **Aspects** — Farming, Mercantile, Natural Riches, Law, Civic, Welfare — each ranked 1-6 by tally. **Prosperity** (total, 6-36) sets Population and modifies the Town Fortune roll. An Aspect at 0 = **town failure**. FL `08-campaigns-in-the-old-west.md:69-126`.
- **Functions = Amenities:** Built improvements (General Store, Church, Saloon, Schoolhouse, Bank, Hotel) ranked by minimum Civic rank, each modifying Aspects. **Settlement Points** (5 SP = one extra amenity). FL `08-campaigns-in-the-old-west.md:128-154`.
- **Upkeep/Events = Turn of the Season:** Looking Back (apply amenities, Business/Congregation rolls) → Looking Forward (choose amenities, Lifestyle, Personal/Town Fortune rolls). The town is an org the *whole table co-owns and co-runs*. FL `08-campaigns-in-the-old-west.md:537-545`.
- **Dynasty:** Legacy XP lets a player continue as a family member after a PC's death — the town outlives the character. FL `08-campaigns-in-the-old-west.md:57-60`.

**Abstract pattern:** West's Town is the **settlement-as-character** model: the org *is* a stat block (Aspects) that the players grow, and its "death" (Aspect 0) is a campaign-ending threat on par with a TPK. This is the rung where "the org is a shared PC" becomes literal. FL has no direct equivalent — FL settlements are *objects a faction acts upon* (Ruled/Protected/Tributary), not characters the players drive. **Layer:** Situational (the settlement-as-character model is a strong fit for West/frontier/dynasty games; FL-style games treat settlements as faction assets instead).

### Outlaw Band (West)

**Source instance:**
- **Founding:** Leader + hideout + 3+ outlaws. The hideout is the non-negotiable founding asset. FL `11-outlaws-of-the-old-west.md:23-34`.
- **Scale tiers:** Crew (3-6) / Gang (7-15) / Outfit (16-30), each adding +1 die to a different domain. **Capped at Outfit** — no faction rung above. FL `11-outlaws-of-the-old-west.md:36-45`.
- **Cohesion 1-5:** The band's morale analog (Broken → Keen), with test triggers and GM adjustment. Directly parallel to FL's Morale 1-5. FL `11-outlaws-of-the-old-west.md:62-122`.
- **Functions = resources:** Refuge (+2 to -2 per settlement), Fence access (0/1/2), Horsestock (0-4), Provisions (D6-D12 resource die). Band Action Checks (4-step procedure, ability table) are the band's "practices." FL `11-outlaws-of-the-old-west.md:128-276`, `:354-423`.
- **Upkeep:** Provisions die depletes; Horsestock must be maintained; **Wanted** level is a permanent external pressure. FL `11-outlaws-of-the-old-west.md:232-276`.
- **Members:** Notable Members have Role/Experience/**Loyalty 1-3**/Ambition/Breaking Point/Leverage — the band is a roster of NPCs with their own failure modes. FL `11-outlaws-of-the-old-west.md:449-533`.

**Abstract pattern:** The Outlaw Band is West's equivalent of FL's Mercenary Company — a **roster-and-cohesion org** where individual members are tracked and the org has a single morale stat. The structural parallel (Cohesion ↔ Morale, both 1-5; Hideout ↔ Stronghold; resources ↔ functions) is exact. The divergence is *ceiling*: West stops at Outfit, FL climbs to Host/Army/Faction. **Layer:** General (the roster-and-cohesion org is a universal rung); the cap is the genre choice.

#### Outlaw band operating sheet

Use this when creating a crime crew, rebel cell, pirate gang, smuggling ring, monster cult, resistance cadre, privateer ship, or any small illegal org.

| Field | What it records | Source abstraction |
| --- | --- | --- |
| Scale | Crew / Gang / Outfit or equivalent headcount band | size changes dice and ambition |
| Leader | who gives orders and who is blamed | founding predicate |
| Hideout | where the band can rest, store loot, and be found | founding asset |
| Cohesion | 1-5 shared morale | org health |
| Notable Members | role, experience, loyalty, ambition, breaking point, leverage | roster pressure |
| Refuge | who shelters the band and at what risk | social base |
| Fence / Market | how stolen goods become useful value | economy valve |
| Horsestock / Transport | how fast the band can move and escape | pursuit handshake |
| Provisions | resource die or upkeep stock | food/upkeep |
| Wanted / Heat | external legal pressure | consequence clock |
| Stash / Shares | loot, shares, hot goods, debt to members | payout and loyalty |

**Band action check:** when the whole band acts off-screen or above PC scale, choose one domain (raid, intimidate, smuggle, gather information, lay low, recruit, move hideout, protect turf), roll the best fitting band pool, then apply a result family:

| Result | Outcome |
| --- | --- |
| 0 successes | action fails; choose or roll trouble: Heat +1, Cohesion −1, member injured/captured, stash lost, hideout exposed |
| 1 success | action succeeds with ordinary cost: provisions step down, Heat +1, or a notable member tests Loyalty |
| 2 successes | clean success: gain the objective and one minor benefit |
| 3+ successes | strong success: gain objective, benefit, and improve position (Refuge, Fence, Cohesion, Stash, or information) |

**Score loop:** Plan target → choose approach → run PC-facing scenes for the dangerous beats → convert take into Stash/Shares → roll Heat/Wanted response → pay provisions and loyalty → choose hideout activity. If the score is resolved entirely off-screen, one band action check is enough; if PCs are present, the band sheet sets stakes and fallout rather than replacing play.

**Collapse checks:** call for a Cohesion or Loyalty check when shares are unfair, provisions run out, a leader is captured, a member is abandoned, Wanted jumps, the hideout is exposed, or a score fails publicly. On failure, choose: desertion, informant, internal challenge, reckless revenge, splinter crew, or demand for a dangerous make-good job.

## 8. Mercenary Company (FL)

The Mercenary Company is FL's **mid-scale org** and the structural bridge between the party (rung 1) and the faction (rung 5). It is also West's Outlaw Band's closest cousin.

**Source instance (Abstraction Ladder):**
- **Founding:** Name + leader + 3+ fighters. FL `12-mercenaries-of-forbidden-lands.md:76-83`.
- **Scale tiers (the rung-amplifier):** Skirmishers (3-6) / Warband (7-20) / Company (21-50) / **Host (51+)**. The Host tier unlocks **Host Play** — a Warmaster and a **Ledger** (-6 to +6) that abstracts the Host as a single trackable entity rather than counting individuals. This is the engine's built-in *large-scale rule pattern*: past ~50 bodies, you stop tracking bodies and start tracking a number. FL `12-mercenaries-of-forbidden-lands.md:88-104`.
- **MORALE 1-5** (Broken → Keen): the org's single morale stat, with ±1 modifiers and a **Grievance Difficulty 1-4** ladder. MORALE Triggers table fires events when the band is mistreated. FL `12-mercenaries-of-forbidden-lands.md:106-194`.
- **Functions:** Contracts (Patrol/Escort/Clearing/Raid/Garrison/Intelligence/Caster), **DRILL** (Training Grounds → trained status → dice upgrades), Hired Casters, the **War Room** stronghold function (runs the company from the base). FL `12-mercenaries-of-forbidden-lands.md:965-1023`, `:1413-1433`.
- **Recruitment:** Settlement pool (D6/2D6/3D6 by settlement size); fighter quality tiers (Common 1s/day, Veteran 2s, Elite 3s). FL `12-mercenaries-of-forbidden-lands.md:269-337`.
- **Upkeep:** Pay (Retainer weekly vs Mission daily) + Feeding (forager output by terrain). **Field Non-Payment** D6 (desertion/mutiny). Feud Track (0 Cold → 4 Vengeance). FL `12-mercenaries-of-forbidden-lands.md:363-392`, `:493-526`, `:555-568`, `:801-811`.
- **Allegiance 0-4** (Unknown → Sworn): the choice that determines whether the band is a *free org* (the players' company) or a *faction asset* (a retainer). At Allegiance 4 the band has effectively been promoted up the ladder into another org's structure. FL `12-mercenaries-of-forbidden-lands.md:916-943`.
- **Internal life:** Discipline (Minor/Serious/Capital offenses, Flogging, Duels), Arguments & Escalation (4 stages Words→Blood), Blood Oaths (Brotherhood/Bounty/Vengeance), Atrocities (reputation consequences). The band is a *society* with its own law. FL `12-mercenaries-of-forbidden-lands.md:1447-1488`, `:1604-1647`, `:1731-1761`.

**Abstract pattern:** The Mercenary Company is the **roster-and-cohesion org at scale**: a tracked headcount, a single morale stat, a pay/feed upkeep cycle, and — critically — a **scale-tier system with a large-scale threshold** (Host Play). The large-scale rule pattern is the design's answer to "how do you scale a roster org past the point where tracking individuals is fun?" Answer: you don't; you collapse the roster into a single ledger number and a single commander. This same move recurs at the faction/army rung. **Layer:** General (roster-and-cohesion org); the large-scale threshold (Host Play) is Optional but *strongly recommended* for any game whose roster org can grow past ~30-50 members.

### Mercenary and roster-org operating sheet

Use this sheet for mercenary companies, expedition crews, guard firms, campaign staffs, ship crews, caravan guards, military squads, adventuring companies, monster-hunter chapters, and any paid roster org.

| Field | Mercenary expression | Generic expression |
| --- | --- | --- |
| Name / Captain | company name and leader | identity and command |
| Scale tier | Skirmishers / Warband / Company / Host | headcount band |
| Roster | common, veteran, elite, named men, specialists | bodies and capability |
| Morale | 1-5, with grievances | willingness to obey and endure |
| Pay model | retainer weekly vs mission daily | regular wage vs job pay |
| Provisions | food by terrain/foragers/stores | upkeep stock |
| Contract | patrol, escort, raid, garrison, intelligence, caster | purpose and payout |
| Allegiance | unknown to sworn | who ultimately owns loyalty |
| Discipline | offense ladder and punishments | internal law |
| Feud / Reputation | settlement anger, atrocities, bounties | public consequence |
| Hoard / Treasury | loot, ransom, goods, pay chest | reward and payroll |
| Stronghold link | War Room, training grounds, garrison | base handshake |

#### Contract procedure

1. **Find work.** Roll or choose employer, mission type, location, pay, advance, and hidden complication.
2. **Negotiate terms.** Set pay, duration, loot rights, ransom rights, command authority, supplies, and breach penalty.
3. **Muster roster.** Decide headcount, quality, named specialists, provisions, mounts/transport, and caster/expert support.
4. **Run the mission.** Resolve PC-facing scenes normally. Use one company roll only for off-screen or scale-mismatched work.
5. **Pay and divide.** Retainer/mission pay, loot share, ransom, and goods payment all test whether the company feels cheated.
6. **Check morale.** Apply grievances: unpaid, unfed, overworked, insulted, high casualties, bad discipline, atrocities, impossible orders.
7. **Write fallout.** Employer debt, settlement fear, feud, bounty, deserters, promotion, named member agenda, or allegiance shift.

#### Host play / large-scale

When the roster passes the table's useful tracking threshold, collapse it.

| Threshold | Keep tracking | Collapse into |
| --- | --- | --- |
| 3-10 | individuals, named roles, loyalty | roster sheet |
| 11-30 | squads, specialists, notable members | company sheet |
| 31-50 | units, payroll, morale, contracts | company + few named faces |
| 51+ | do not count every body | Host Ledger, Warmaster, Treasury, Supply, Rival Bands |

**Host procedure:** assign a Warmaster → set Ledger −6 to +6 → set Treasury and Supply posture → name 2-4 rival bands or captains → each campaign week choose one host objective → roll only when the host's order meets uncertainty → translate the result into Ledger shift, casualty posture, supply strain, diplomacy, or inter-band rivalry.

**Validation:** a roster org must never become a free army. Every increase in headcount must raise at least one of payroll, provisions, command friction, visibility, employer dependence, or atrocity risk.

## 9. Factions, Legacies, and the Faction Turn (FL)

The Faction is FL's **high-scale org** and the only place in either game where a full **board-game-style turn layer** runs *above* the players' adventure play. It is the rung where "the world moves while the PCs do."

### The faction as stat block

**Source instance:**
- **Pillars (the four core stats):** **Mandate** (legitimacy), **Force** (armed strength), **Reach** (mobility/communication), **Hearth** (sustaining base). Tier sets starting pillars: Thin (3,3,2,2) / Established (4,3,3,3) / Dominant (5,4,4,3). A pillar at 0 triggers a collapse effect (Mandate 0 = no one obeys; Force 0 = cannot muster; Reach 0 = isolated; Hearth 0 = cannot sustain). FL `11-politics-of-the-forbidden-lands.md:206-217`, `:345-377`.
- **Practices (the 16 "skills"):** grouped under pillars — Mandate (Claim, Decree, Accord, Rite), Force (Muster, Discipline, Assault, Siegecraft), Reach (Watch, Intrigue, Relay, Traffic), Hearth (Yield, Provision, Works, Relief). FL `11-politics-of-the-forbidden-lands.md:380-454`.
- **Legacies (the 9 "talent trees"):** Claimant House, Tribute Throne, Mustering Crown, Walled Seat, Toll Court, Sacred Seat, Veiled Court, Riding Lord, Dread Throne — each a 5-rank drilled custom of power. FL `11-politics-of-the-forbidden-lands.md:458-552`.
- **Resources:** Treasury & Stores (Bare/Thin/Sound/Deep backing tracks), Labor/Levy/Retainers (None→Heavy). **Basis of Rule** (Blood Right, Old Custom, Protection, Conquest, Wealth, Cult Sanction, Oath Confederacy, Dread) flavors how the faction is *legitimately held*. FL `11-politics-of-the-forbidden-lands.md:273-341`.

**Abstract pattern:** The faction is an org with a **four-stat block** (legitimacy / force / reach / sustain), a **skill list** (practices), a **talent tree** (legacies), and **backing resource tracks**. This is structurally a *character sheet at polity scale* — the same skeleton (attributes → skills → talents → resources) as a PC, re-skinned. The **basis of rule** is the unique addition: it encodes *why the org is obeyed*, which is the question that only polity-scale orgs must answer. **Layer:** General (the four-pillar stat block is the recommended polity-scale skeleton); the basis-of-rule flavor system is Optional but high-value.

### The Faction Turn

This is the central procedural engine of the high-scale rung.

**Source instance:**
- **Mode of Rule sets turn scale:** Peace/Pressure = **Season Turn**; Muster/Campaign = **Campaign Week**. The *faster the faction is spending itself, the shorter its turn*. FL `11-politics-of-the-forbidden-lands.md:988-997`.
- **The procedure (Peace, as template):** (1) Recover pillar; (2) Community roll (Mandate+Accord/Rite); (3) Development roll (Hearth+Works); (4) Prosperity roll (Hearth+Yield or Reach+Traffic); (5) Decree step; (6) Acts (one major + one minor); (7) Fallout. Pressure/Muster/Campaign variants swap the pillar+practice pairings and tighten the act economy (Muster/Campaign get one *campaign act* instead of major+minor). FL `11-politics-of-the-forbidden-lands.md:1009-1091`.
- **The roll:** **pillar + practice + one asset source + modifiers.** Asset source contributes 1-5 asset dice by rating; only the single highest asset applies (no stacking). Overwhelming advantages use an **Ascendancy Die** (D8/D10/D12) that *replaces* a d6. FL `11-politics-of-the-forbidden-lands.md:806-848`.
- **Faction Acts (the action menu):** Minor (Call Council, Collect Due, Give Safe-Conduct, Issue Decree, Send Gift, Spy), Major (Grant Protection, Hire Mercenaries, Judge/Outlaw, Negotiate Truce, Press Claim, Swear Fealty, Take Hostage), Campaign (Call Levy, Invest a Place, Raid). FL `11-politics-of-the-forbidden-lands.md:1105-1322`.
- **Fallout D66:** a failed act never means "nothing" — it always leaves a colder village, a bolder rival, a damaged road. FL `11-politics-of-the-forbidden-lands.md:1326-1347`.
- **Settlement bonds:** Ruled / Protected / Tributary / Vassal / Occupied / Allied — the status ladder the faction acts upon. **Feud Track** (0 Cold Peace → 4 Mustered War) governs when politics becomes war. **Standing** (-2 to +2) is local memory. FL `11-politics-of-the-forbidden-lands.md:907-977`.

**Abstract pattern — the faction turn:** A **procedural turn layer** that runs on its own clock (Season or Week), resolves org-vs-org and org-vs-world pressure through a **stat+skill+asset roll** identical in grammar to a PC roll, and whose turn length and act economy are *set by a Mode choice* (peaceful factions get slow turns + flexible acts; warring factions get fast turns + tight acts). The genius move is that **the same resolution grammar (attribute+skill+asset+modifiers, push, banes-damage-pillar) is reused at polity scale** — the downtime layer does not invent a new engine, it *re-scales the existing one*. **Layer:** General (the procedural turn is the defining feature of the faction rung); the Mode-based turn length is a **core design choice** (see §11). West has *no faction turn* — this is the largest single FL/West divergence in the whole layer.

### Campaign Points, Agents, and Advisors

**Source instance:**
- **Campaign Points (CP):** Awarded only when something *real changes in the world* (Minor success 1, Major 2, Significant victory 5, Great conquest 10) — never for routine success. CP heals pillars OR raises practices/pillars/legacies. FL `11-politics-of-the-forbidden-lands.md:556-624`.
- **Agents:** Named hands sent out (champion, rider, spy, a whole fellowship). Resolved as multi-roll **Undertakings** (1 roll per CP of deed-value), with Seen Steps producing a trail. **Player characters can be agents** — and when they are, the faction turn sets the field but the dangerous work plays out in ordinary adventurer time. FL `11-politics-of-the-forbidden-lands.md:628-741`.
- **Advisors:** Named hands at the seat; **Seat Work** banks bonus dice for later faction rolls. FL `11-politics-of-the-forbidden-lands.md:743-800`.

**Abstract pattern:** CP is the faction's **XP**, gated by *fictional consequence* rather than session count. Agents/Advisors are the **bridge between the faction turn and PC play** — they are the rule pattern by which "the faction wants X" becomes "the players go do X at the table." This bridge is what prevents the faction layer from becoming a dissociated board game. **Layer:** General (an XP-equivalent gated by world-change); the Agent-as-PC bridge is **essential** for any campaign that wants the faction layer to drive adventure rather than replace it.

## 10. Mass combat and sieges (FL)

Mass Combat is FL's **top rung** — the resolution engine for when org-scale conflict produces open violence. It is the only place the engine *replaces* individual conflict with an abstraction over it.

### Troop dice and the battle sequence

**Source instance:**
- **Troop Dice are a three-color pool, exactly mirroring the core loop's dice grammar:** **Base Dice** (from raw numbers — Infantry/Skirmishers 20/unit max 100 = 5 dice; Cavalry 5/unit max 25; Monster 1/unit max 5), **Advantage Dice** (from quality — well-trained, race, fervor, Important Character present, flanking +1/rear +2), **Protection Dice** (from armor — Small/Large shield, Leather/Chainmail/Plate). Veterans upgrade Advantage Dice D6→D8→D10→D12 after 3+ engagements. FL `12-battles-and-sieges.md:111-186`, `:195-234`.
- **The battle sequence:** 15-minute game turns; Army Lines (vanguard + reserves); three Battle Line Sections (left/center/right) → three rolls/side/turn. Screening/Pickets → Deployment (INSIGHT) → General's Speech (PERFORMANCE → morale points) → Challenge (duel) → Battle Turns loop → Battle Roll → Pressing the Advantage (spend 1/2/3 successes) → Damage → Morale Points → No Quarter. FL `12-battles-and-sieges.md:54-104`, `:243-450`.
- **Commander agency:** Important Characters move between troops granting advantage dice; REGROUP rolls rally fleeing troops; Ordered Retreat; Pursuit; Surrender (field/garrison). FL `12-battles-and-sieges.md:453-537`, `:563-573`.
- **Special conditions:** Ranged troops & range, skirmisher morale, terrain (High Ground +1 advantage, Mud, Forest, River Crossing half-dice, Prepared Ground, Field Works), Weather D6, Night Attack, Feigned Retreat (opposed PERFORMANCE vs INSIGHT), Ambush (SCOUTING). FL `12-battles-and-sieges.md:541-685`.

**Abstract pattern:** Mass combat **reuses the core loop's three-color dice grammar at org scale** — Base↔numbers, Advantage↔quality/training, Protection↔armor. This is the same large-scale move as Host Play: instead of rolling for each soldier, you roll a *pool that represents the unit*, and the pool's composition (how it was built) encodes everything that would matter in individual combat. **Player agency is preserved** through Important Characters who move between sections and through the General's sequence of command decisions (speech, deployment, challenge, retreat, pursuit). The mass-combat layer is thus *not* a different game — it is the same game with the dice repurposed to represent formations. **Layer:** Optional (mass combat is the top rung; many campaigns never reach it); but when enabled, reusing the core dice grammar is **strongly recommended** over inventing a new system.

### Sieges

**Source instance:**
- **The inversion:** In siege, defenders need only **10 units per base die** (vs 20 in the field) — walls compress and multiply defensive effectiveness. Walls grant **attack-first** and advantage dice by height/strength. FL `12-battles-and-sieges.md:694-714`.
- **Siege Engines** (built on-site, require an engineer at 5 silver/day): Battering Ram (7 days, siege dice, gate breaks at cumulative 3), Siege Tower (30 days, negates wall advantage at contact), Catapult (14 days, 4 attack dice/day, reduces wall advantage), Trebuchet (60 days, 8 dice/day), Tunnel (2D6 successes to complete, stability rule, collapse risk). FL `12-battles-and-sieges.md:728-768`.
- **Blockade:** Needs **3 besiegers per 1 defender**; if leaky, defenders get one supply/messenger/relief run per week (opposed SCOUTING/MANIPULATION). **Non-combatants** (D6×20) eat half-rations and can be expelled (intelligence/atrocity trade-off). FL `12-battles-and-sieges.md:771-804`.
- **Sorties, counter-mines, fire vs engines, abandoning the outer wall** — defenders are not passive. **Relief of a siege** forces the besieger to choose: Hold the Ring (−1 advantage/engaged section), Turn to Meet (garrison may sortie free), or Raise the Siege. FL `12-battles-and-sieges.md:850-895`.
- **Surrender & Parley:** once/week + after major events; opposed MANIPULATION/INSIGHT/PERFORMANCE; terms per extra success; **Bad Faith** (murdering surrendered defenders) makes all future negotiations Demanding. FL `12-battles-and-sieges.md:816-843`.

### Supplies, disease, and aftermath

**Source instance:**
- **Supply units** consumed daily (Infantry/Skirmisher 1, Cavalry 2, Monster 20). **Starving troops** suffer demoralization on 1 *and 2*, and enemies gain +2 advantage dice vs them. Desertion (1s) and death (results ≥10 after adding days-unfed) roll independently. FL `12-battles-and-sieges.md:906-946`.
- **Foraging:** roll base dice, sum *all* results ×10 = supply gathered/quarter-day; **depletion** (−1/die per quarter-day in same hex, recovers 1/week). An army that stays eats the countryside bare. FL `12-battles-and-sieges.md:952-960`.
- **Supply lines & march:** base→army line; cutting it starves the army. Camp setup/breakdown, cooking, sleep each cost quarter-days; skipping any widens the demoralization range (1→1-2→1-4 as hunger+forced-march+poor-sleep stack). FL `12-battles-and-sieges.md:962-1001`.
- **Disease:** D6 per 100 soldiers/week; on a 1, outbreak adds disease dice; each week, 1s kill 10, 6s add a die. **Siege doubles** defender disease dice unless they have a Sewer function. FL `12-battles-and-sieges.md:1030-1046`.
- **Aftermath:** Prisoners & Ransom (Common 10s → General 2000s+), prisoners without ransom value (release/forced-labor/press/execute — each with consequences), stripping the dead. FL `12-battles-and-sieges.md:1064-1117`.

**Abstract pattern:** The mass-combat layer's *true* engine is **logistics, not tactics.** The battle sequence is dramatic, but the supplies/disease/march rules are what actually decide most campaigns: an army is a *metabolism* with a daily consumption rate, a depletion-curve for foraging, a stacking demoralization penalty for every skipped maintenance quarter-day, and a disease rule set that punishes crowding. The design intent is unmistakable: **most wars are lost by arithmetic, not by the battle roll.** The siege doubling of disease, the foraging depletion, the "accumulated demoralization stacks 1→4" rule — all encode the same thesis: *the org that cannot feed and shelter itself loses before swords are drawn.* **Layer:** Situational (logistics rules only matter when the campaign sustains multi-week field operations); but when mass combat is enabled, **the logistics layer is more important than the battle sequence** — omit it and wars become board-game pieces; include it and wars become the attritional nightmares that decide real campaigns.

## 11. The scale-escalation ladder

This is the file's second core deliverable. The five-beat lifecycle is *invariant* across rungs; what changes is the **turn scale, currency size, threat radius, and which rule sets are enabled.** Each rung is defined by: **what it owns, what turn it runs on, what it costs, what it threatens, and which rule set it uses.**

| Rung | Org | Turn scale | Currency | Threatens | Rule set | FL instance | West instance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Solo** | a lone PC | scene | WP / Faith | themselves | core loop | adventurer | gunslinger |
| **Party** | the fellowship | session/adventure | shared WP, shared pride | a lair, a quest | core loop + journeys | the party | the posse |
| **Band** | a small roster org | week | pay + provisions + cohesion | a hideout, a score | roster-and-cohesion | Mercenary Band (Skirmishers) | Outlaw Crew / Business |
| **Company** | a large roster org | week/month | pay + stores + morale + feud | a settlement, a contract | roster-and-cohesion + large-scale | Mercenary Company / Host (Ledger) | Outlaw Gang/Outfit / Town |
| **Faction** | a polity-scale org | season/week | pillars + treasury + stores + levy | a region, a succession | faction turn + practices + legacies | FL Faction (pillars/practices/legacies) | *(absent)* |
| **Army** | a field force | day/quarter-day | supply units + troop dice | a campaign, a siege | mass combat + logistics | FL Army (troop dice) | *(absent)* |
| **Polity** | a ruling power | season + campaign | pillars + CP + burden | a kingdom, a dynasty | faction turn + mass combat + dynasty | FL Faction at Dominant tier + Army | *(absent)* |

### Rung rules

- **Solo → Party** is free (the core loop handles it; no new rule set).
- **Party → Band** requires the **roster-and-cohesion rule set**: a tracked headcount, a single morale stat (Morale/Cohesion 1-5), a pay/feed cycle, and a degeneration table for non-payment.
- **Band → Company** requires the **large-scale threshold** (Host Play / Ledger): past ~50 bodies, stop tracking individuals. Without this, the roster org becomes unmanageable.
- **Company → Faction** requires the **faction turn**: a procedural turn layer with a Mode choice, a stat+skill+asset roll, an act economy, settlement bonds, and a Feud track.
- **Faction → Army** requires the **mass-combat + logistics rule set**: troop dice (reusing the core grammar), the battle sequence, supply/disease/march.
- **Army → Polity** is not a new rule set — it is the *integration* of faction turn + mass combat + dynasty/CP advancement. The polity rung is where all lower rungs interlock.

### Genre / campaign-length guidance — which rungs to enable

This is the central practical output of the ladder.

- **One-shot / short campaign (3-8 sessions):** Enable **Solo → Party** only. A base may exist as color (a place to rest) without tracked functions/upkeep. *Do not* enable the band rung — there is no time to pay it off.
- **Standard campaign (1 season, ~10-20 sessions):** Enable **Solo → Band**. A Stronghold/Business with functions and upkeep gives players "something that grows." A roster org (small mercenary band or outlaw crew) is viable if the campaign is about that org. *Do not* enable the faction turn unless the campaign is explicitly political.
- **Long campaign (multi-season, 20-60 sessions):** Enable **Solo → Company**. The large-scale threshold matters now. A Mercenary Company or growing Town becomes the campaign's spine. The faction turn can be introduced in the back half as escalation.
- **Epic / dynasty campaign (60+ sessions, or generational):** Enable the **full ladder through Polity.** The faction turn runs alongside PC play; PCs serve as Agents; mass combat resolves the wars the faction turn produces. West's Dynasty rules (Legacy XP, play a family member) are the model for the generational layer. FL `08-campaigns-in-the-old-west.md:57-60`.

### The Two Classic Shapes

- **FL shape (full ladder, interlocking):** All rungs enabled. The lifecycle beats recur at each rung with amplified amplitude. The faction turn and mass combat are *expected* end-states. This is the "campaign-as-saga" shape.
- **West shape (personal/small-org, capped):** Rungs Solo → Company only. No faction turn, no mass combat. The Town is the *de facto* top org, run as a shared character. This is the "campaign-as-community" shape. The cap is a *feature*: West's genres (frontier, dynasty, outlaw) are about people and places, not polities and armies.

**The choice:** a new game chooses its *ceiling rung* first, then enables every rung up to it. The ceiling is the single most consequential campaign-design decision in the downtime layer — it determines session count viability, bookkeeping load, and whether the game is "about" individuals, communities, or power. **Layer:** General (the ladder is universal); the ceiling is a **core design choice** (see §11).

## 12. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Org density / ladder ceiling** | Full ladder through Polity | Capped at Company/Town | Saga-scale interlocking vs focused personal scale | FL-style for epic/political; West-style for community/frontier |
| **Faction turn** | Full procedural turn layer (Mode, pillars, practices, acts, fallout) | Absent | World-moves-while-PCs-do vs world-is-the-PCs'-work | Enable for political/strategic campaigns; omit for character/community games |
| **Mass combat** | Troop-dice engine + logistics + sieges | Absent | Resolves org-scale violence vs handwaves it | Enable only if the campaign sustains field operations; otherwise it's bookkeeping |
| **Org-founding currency** | Materials + labor + crafting roll | Capital (illiquid, $250=1) | Crafting-driven vs investment-driven | Capital model for economic games; materials model for survival/crafting games |
| **Town model** | Settlement = faction asset (Ruled/Protected/Tributary) | Settlement = shared character (Aspects, Prosperity, failure at 0) | Town-as-object vs town-as-PC | West model for community/dynasty; FL model for political/conquest |
| **Roster org morale** | Morale 1-5 + Grievance Difficulty + Feud Track | Cohesion 1-5 + Loyalty 1-3 + Wanted | Gritty military friction vs outlaw-crew drama | Both work; FL's is richer, West's is lighter |
| **Abstraction-collapse at scale** | Host Play (Ledger −6 to +6) | None (capped at Outfit 16-30) | Scales past 50 bodies vs never needs to | Include Host-Play-equivalent if the roster org can grow past ~30-50 |
| **Upkeep vectors** | Three independent (resourcing, payroll, security) | One (season Business/Town roll) | Granular threat vs single roll | Three-vector for survival grit; single-roll for pacing |
| **Base → Willpower/Faith link** | Stronghold grants +1 WP/PC/session | (Business grants coin/profit, not Willpower/Faith) | Base fuels adventure directly vs base fuels economy | FL link recommended — it's the economic reason to want a base |
| **Settlement relationship ladder** | Ruled/Protected/Tributary/Vassal/Occupied/Allied + Feud 0-4 | (Town Aspects + Standing) | Explicit political-status machine vs organic community stats | FL ladder for conquest/politics; West stats for community growth |
| **Generational play** | (via Faction + Dynasty-of-house legacies) | Dynasty: Legacy XP, play a family member | Polity-scale dynasties vs family-scale dynasty | West Dynasty is the cleaner model for family sagas |
| **Random-event source** | D6 tables (Stronghold, Non-Payment, Unguarded, Upkeep) + Faction Fallout D66 | Season Fortune rolls (Business, Personal, Town) | Discrete-threat tables vs seasonal-fortune rolls | D6 tables for grit; Fortune rolls for dramatic pacing |

## 13. Rule Choices and Build Recipe

Each choice has FL and West as two calibrated points. To build a new game's downtime layer, set each choice.

1. **Ladder ceiling** — Solo/Party/Band/Company/Faction/Army/Polity. *(The single most consequential decision: sets session-count viability and bookkeeping load. See §9.)*
2. **Org-founding currency** — materials+labor / Capital (illiquid) / hybrid. *(Crafting-driven vs investment-driven base-building.)*
3. **Base → Willpower/Faith link** — on (base grants WP/Faith) / off (base grants only economy). *(Whether the downtime layer directly fuels adventure.)*
4. **Upkeep vectors** — one (single roll) / three (resourcing, payroll, security) / custom. *(Granularity of "the org is threatened.")*
5. **Roster-org morale model** — single stat (Morale/Cohesion 1-5) / single stat + per-member loyalty / none. *(How much the roster's people are tracked.)*
6. **Abstraction-collapse threshold** — on (Ledger/Host Play past ~50) / off (cap the roster). *(Whether the roster org can scale indefinitely.)*
7. **Faction turn** — on / off. *(Whether the world moves procedurally while PCs act. The largest FL/West divergence.)*
8. **Faction-turn Mode choice** — on (turn length set by Mode of Rule) / off (fixed turn length). *(Whether peaceful and warring factions run at different speeds.)*
9. **Faction stat block** — four-pillar (Mandate/Force/Reach/Hearth) / custom. *(The polity-scale skeleton.)*
10. **Town model** — settlement-as-character (Aspects) / settlement-as-faction-asset (status ladder) / hybrid. *(Whether the community is a PC or an object.)*
11. **Mass combat** — on (reuse core dice grammar at unit scale) / off (handwave). *(Only enable if the campaign sustains field operations.)*
12. **Logistics layer** — on (supply/disease/march/forage-depletion) / off. *(More decisive than the battle sequence when enabled.)*
13. **Generational play** — on (Dynasty/Legacy XP) / off. *(For family-saga or multi-decade campaigns.)*

**Instantiation recipe (any genre):**

1. **Set the ladder ceiling first (choice 1).** This is determined by intended session count: <8 sessions = Party; 10-20 = Band; 20-60 = Company; 60+ = Polity. Do not enable a rung the campaign cannot sustain.
2. **Decide the faction turn (choice 7).** If the campaign is political/strategic, enable it and set the Mode choice (8). If it is character/community-focused, leave it off — this single choice saves enormous bookkeeping.
3. **Choose the org-founding currency (choice 2) and the base→Willpower/Faith link (choice 3).** These determine whether base-building feels like crafting (FL), investing (West), or both.
4. **Set the upkeep vectors (choice 4) and roster morale (choice 5).** Match grit to genre: survival/horror wants three vectors + per-member loyalty; dramatic/pulp wants one vector + a single morale stat.
5. **If the roster org can exceed ~30-50 members, enable large-scale (choice 6).** Without it, the roster becomes unmanageable.
6. **If mass combat is enabled (choice 11), reuse the core dice grammar at unit scale and include the logistics layer (choice 12).** Do not invent a new combat system, and do not omit logistics — it is what makes wars feel like wars.
7. **Choose the town model (choice 10)** to match whether the community is a protagonist (West) or a prize (FL).
8. **Validate against the adventure layer:** ensure the base→Willpower/Faith link, the Agent bridge (PCs as faction agents), and the CP/XP gate are all wired so the downtime layer *drives* adventure rather than replacing it.

**Period-engine handoff:** this file identifies what kind of org exists, what rung it occupies, and how it fits the scale ladder. When the org must be run across **weeks, months, seasons, years, or generations**, load `25-season-downtime-and-enterprises.md` for the Period Turn, Investment Cycle, Enterprise Roll, business/family/faction/settlement sheets, hard-season rules, and management validation checks. When the task is to price functions, translate stronghold construction into property/Capital, set upkeep/payback, design materials/labor/cost bands, or handle stores, warehouses, provisions, animals, wagons, and bulk materials, load `08-gear-and-economy.md`.

## 14. Design intent

The downtime org layer is engineered to turn **one-shots into campaigns** by giving players *something that grows and is threatened*. Specifically:

- **The five-beat lifecycle (founding → functions → upkeep → events → scale)** is invariant across every org type in both games. A Stronghold, a saloon, a mercenary band, a faction, and an outlaw crew are *the same pattern at different amplitudes*. This is why FL's four interlocking rule sets are one engine, not four — and why a new genre can lift the pattern wholesale and re-skin it.
- **Upkeep + events are the org's two sources of world-agency.** Without them, an org is a static stat block the players optimize. With them, the org is a *living, hungry, threatened* thing that generates session hooks every cycle ("the hirelings haven't been paid," "a monster laired in the cellar," "the Feud advanced to Armed"). The degeneration tables are the downtime layer's equivalent of the core loop's bane — *latent pressure that activates when the org is neglected.*
- **The base → Willpower/Faith link (Stronghold grants WP)** is the economic keystone that binds the downtime layer to the adventure layer. It is the reason a party *wants* a base: not for color, but because the base literally fuels their talents. Cut this link and base-building becomes a dissociated minigame.
- **The scale ladder lets a campaign escalate without changing engines.** Because each rung reuses the same lifecycle beats (and, at the top, the same dice grammar), a campaign can begin as a party clearing a lair and end as a polity fighting a war — *without ever switching systems.* The large-scale threshold (Host Play) and the grammar-reuse in mass combat are the two rules moves that make this possible.
- **The faction turn lets the world move while the PCs do.** It is the only rule set that runs on its own clock above play, and its absence in West is the largest single design difference: West's world is the community the PCs build; FL's world is the politics that happens around them. Neither is superior — they serve opposite fantasies (community vs power).
- **Logistics, not tactics, decides campaigns.** FL's mass-combat layer encodes the thesis that wars are lost by arithmetic (supply depletion, disease doubling in sieges, stacking demoralization from hunger+forced-march+poor-sleep). The battle sequence is dramatic; the supplies/disease/march rules are decisive. This is the layer's most historically honest design choice.
- **The ladder ceiling is the campaign-design choice.** Choosing how high the ladder goes is choosing what the campaign is *about*: individuals, communities, or power. West caps the ladder to stay focused on people and places; FL extends it to make the campaign a saga. A new genre's job is to find its ceiling and enable every rung up to it — and no further, because every rung above the ceiling is bookkeeping the campaign cannot repay.

The divergence between FL and West is not accidental — it is the layer's proof that **the same five-beat pattern produces opposite campaign shapes by choosing a different ceiling.** FL's full ladder makes a game where the campaign *escalates into power*; West's capped ladder makes a game where the campaign *deepens into community.* A new genre's job is to find its ceiling and let the pattern do the rest.
