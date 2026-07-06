<!-- markdownlint-disable MD013 -->

# Base, Faction, Mass-Combat — The Downtime Org Layer

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** The org-lifecycle pattern and the scale-escalation ladder are the spine; every base/business/band/company/faction is an instance of one genre-neutral pattern.

## Contents

1. Source provenance
2. Abstraction target
3. The shared pattern: founding → functions → upkeep → events → scale
4. Stronghold (FL)
5. Town, Property, and Outlaw Band (West)
6. Mercenary Company (FL)
7. Factions, Legacies, and the Faction Turn (FL)
8. Mass combat and sieges (FL)
9. The scale-escalation ladder
10. Divergence rows (FL vs West)
11. Dials and instantiation recipe
12. Design intent

## Source provenance

**Forbidden Lands 2E:**
- `01-corebook/09-the-stronghold.md` (~2,470 lines) — establishing, housing/HOUSING score, stronghold sheet, base effects (rest + WP), flaws, random events, functions, hirelings, upkeep.
- `01-corebook/12-mercenaries-of-forbidden-lands.md` (~4,890 lines) — mercenary company system: bands, size tiers, Morale, recruitment, pay/provisions, village extortion/tribute, contracts/bounties/kidnapping, campaign life (DRILL/camp/discipline), Named Men, Hired Casters, wanted men, atrocities, War Room function, Host Play, 7 premade bands.
- `01-corebook/14-traderoads-of-the-forbidden-lands.md` — caravan/traderoad economy, Warehouse function.
- `02-gamemasters-guide/11-politics-of-the-forbidden-lands.md` (~2,310 lines) — faction engine: creation/tiers/sheet, Treasury/Stores/Labor/Levy/Retainers, Pillars (Mandate/Force/Reach/Hearth) + Practices, 9 Legacies, Campaign Points, Agents & Advisors, faction rolls, Settlement bonds, Faction Turn, faction acts, fallout, burden, handoff, revenue, tribute, retainers/levy/mercenaries, armies, logistics, politics-to-war, premade factions.
- `02-gamemasters-guide/12-battles-and-sieges.md` (~1,790 lines) — mass combat: troop dice, arms/armor, battle sequence, special combat conditions, Sieges (blockade/breach/relief), supplies, campaign movement, disease, aftermath, new war talents, example units.

**Tales of the Old West 2E:**
- `01-corebook/06-life-in-the-old-west.md` — Outfits/Businesses (Business Types Table, proprietor/employee/investor, Turn of the Season Business Rolls), Property & Land (Property Status, Location Type, Features, buying/selling, auctions, Homestead Act).
- `01-corebook/08-campaigns-in-the-old-west.md` — Your Town (Aspects: Farming/Mercantile/Natural Riches/Law/Civic/Welfare/Prosperity, Amenities, Settlement Points), Turn of the Season (Business/Congregation/Personal/Town Fortune rolls), Dynasty.
- `01-corebook/11-outlaws-of-the-old-west.md` — Outlaw Band subsystem: scale, leadership, cohesion, resources (refuge/fence/horsestock/provisions), Town Tags, Band Action Checks, recruitment/loyalty, shares & loot, hideout, Scores, Wanted status & pursuit, Hideout Life.

## Abstraction target

Abstract the **downtime org layer** — every "thing a player or faction owns and runs between adventures" — into one genre-neutral pattern with five beats: **founding → functions → upkeep → events → scale escalation.** FL instantiates this richly (Stronghold + Mercenary Company + Factions + Mass Combat, all interlocking); West instantiates it at the personal/small-org scale (Business/Property + Town + Outlaw Band). The deliverable is the **org lifecycle pattern** and a **scale ladder** (solo → party → band → company → faction → army → polity) with explicit guidance on which rungs to enable for which genre/campaign length.

Apply the Abstraction Ladder to: the lifecycle pattern, each instantiation, and the scale ladder.

## 3. The shared pattern: founding → functions → upkeep → events → scale

This is the file's core abstraction. Every org in both games — a cleared dungeon converted to a castle, a bought saloon, a band of hired swords, a faction of allied settlements, a robber gang, the town the players are trying to grow — runs on the **same five-beat lifecycle.** The beats are genre-neutral; the dials on each beat are where genre is set.

### Beat 1 — Founding

**FL Stronghold:** Established by *clearing* a lair/ruin and claiming it, or by *building* on chosen ground. Building requires a **CRAFTING** roll; failure introduces a **Flaw** rolled on a D6 table (Collapsed Roof, Cramped, Dark, Defective, Haunted, Hidden Back Door). FL `09-the-stronghold.md:17-22`, `:66-77`.

**FL Mercenary Band:** Formed by naming it, naming a leader, and recruiting **3+ fighters**. The band does not exist as a tracked org until those three things are done. FL `12-mercenaries-of-forbidden-lands.md:76-83`.

**FL Faction:** Created through a 9-step sequence: seat → basis of rule → tier → four pillars → practices → legacy → holdings → resources (Treasury/Stores/Labor/Levy/Retainers) → aim → weakness. FL `11-politics-of-the-forbidden-lands.md:189-203`.

**West Business/Property:** Founded by investing **Capital** (1 Capital = $250). A proprietor starts or buys a business from the Business Types Table; a landowner buys property (Homestead Act: $14 for 160 acres). FL `06-life-in-the-old-west.md:27-49`, `:157-186`, `:254-265`.

**West Outlaw Band:** Founded by a leader, a hideout, and **3+ outlaws**. The hideout is the founding asset — without it the band has no org status. FL `11-outlaws-of-the-old-west.md:23-34`.

**Generic abstraction — founding:** An org is founded by satisfying a small **founding predicate** (a cleared site / spent Capital / recruited minimum headcount / a seat + a basis of rule). The predicate is a gate: the org is not tracked until it is met. The founding roll (when one is required) carries a **failure tax** that produces a *permanent embedded flaw* — the org is born marked by the conditions of its birth. **Layer:** General (the predicate gate); the founding-flaw roll is Optional (a grit dial — West does not tax business-founding this way).

### Beat 2 — Functions

**FL Stronghold:** A function is a **built improvement** (Apiary, Forge, Dungeon, Library, Marketplace, Temple, Workshop, etc. — 60+ in the table) that grants a mechanical effect, often staffed by a worker. Each costs raw materials, tools, time, and sometimes a prerequisite function or specialist. Functions convert downtime labor into **ongoing capability** (crafting, research, recruitment, defense, food production). FL `09-the-stronghold.md:285-355`.

**FL Mercenary Band:** The band's "functions" are its **capabilities as a force**: contracts it can take (Patrol, Escort, Clearing, Raid, Garrison, Intelligence, Caster), training upgrades (DRILL via Training Grounds), and special assets (Hired Casters). FL `12-mercenaries-of-forbidden-lands.md:965-1023`, `:1413-1433`.

**FL Faction:** The faction's functions are its **16 Practices** (grouped under four pillars) and its **9 Legacies** (talent-like drilled customs of power). Practices are what the faction *can do*; legacies are what it *does exceptionally well*. FL `11-politics-of-the-forbidden-lands.md:380-552`.

**West Business:** The business's function is its **key ability** (Bartender mixes drinks for rumor access; Blacksmith crafts/repairs; Doctor heals; Newspaper publishes). Each Business Type in the table grants a specific mechanical hook. FL `06-life-in-the-old-west.md:157-186`.

**West Town:** The town's functions are its **Amenities** — built improvements (General Store, Church, Saloon, Schoolhouse, Bank, Hotel, etc.) ranked by minimum Civic rank, each modifying the town's Aspects. FL `08-campaigns-in-the-old-west.md:128-253`.

**West Outlaw Band:** The band's functions are its **resources** (Refuge network, Fence access, Horsestock, Provisions die) and the operations it can run (Band Action Checks, Scores). FL `11-outlaws-of-the-old-west.md:128-276`, `:354-423`.

**Generic abstraction — functions:** Functions are **discrete, named improvements** the org acquires over time, each converting downtime resources (materials, labor, coin, stores) into a **persistent mechanical capability**. They are the org's "skill list." Acquiring a function has a cost ladder (materials + time + prerequisites); the function then pays out each downtime cycle. **Layer:** General.

### Beat 3 — Upkeep

**FL Stronghold:** Requires **upkeep** (food/materials/labor) per cycle; **Lacking Upkeep** triggers a D6 table (Abandonment, Decay, Mutiny, etc.). Hirelings/Residents/PCs/Slaves form the work force; **non-payment** of hirelings triggers its own D6 table (strike, theft, desertion). **Unguarded** strongholds trigger a D6 table of misfortunes. FL `09-the-stronghold.md:146-155`, `:255-272`.

**FL Mercenary Band:** Must be **paid and fed**. Pay model is Retainer (weekly) or Mission (daily). Feeding uses forager output by terrain. **Field Non-Payment** triggers a D6 table (desertion, mutiny, desertion of Named Men). FL `12-mercenaries-of-forbidden-lands.md:363-392`, `:493-526`, `:555-568`.

**FL Faction:** Pays upkeep through **pillar recovery** (1 point per Season Turn, paused during Campaign), **Treasury/Stores** backing tracks (Bare/Thin/Sound/Deep) that can step *down* under strain, and **Burden** on settlements (Light/Hard/Crushing/Ruinous) that worsens Standing and Feud. FL `11-politics-of-the-forbidden-lands.md:273-291`, `:893-899`, `:1357-1366`.

**West Business:** Pays upkeep through the **season Business Roll** (key ability + help + Competition + Law + aspect modifiers), with a Business Bonus/Penalty D66 table on the line; **Going Bust** is the failure state. FL `08-campaigns-in-the-old-west.md:555-643`.

**West Town:** Pays upkeep through the **Turn of the Season** rolls; an Aspect driven to 0 means **the town fails**. FL `08-campaigns-in-the-old-west.md:522-535`, `:537-545`.

**West Outlaw Band:** Pays upkeep through the **Provisions resource die** (D6→D12, depletes), Horsestock upkeep, and the constant pressure of **Wanted** level. FL `11-outlaws-of-the-old-west.md:232-276`.

**Generic abstraction — upkeep:** Every org carries a **resource obligation** it must discharge each downtime cycle (food/wages/stores/pillar-points/aspect-tallies). **Failing upkeep triggers a degeneration table** — attrition, desertion, decay, mutiny, or collapse. Upkeep is the engine that keeps the org *alive but not free*: it converts "we own a thing" into "we must feed the thing." **Layer:** General. The degeneration table is the upkeep layer's equivalent of the core loop's bane — *latent pressure that activates when the org is starved.*

### Beat 4 — Events

**FL Stronghold:** **Random Events D6** between sessions (a monster lairs nearby, a traveler arrives, a rival eyes the site). FL `09-the-stronghold.md:79-90`.

**FL Mercenary Band:** Events arise from **MORALE triggers** (the Grievance Difficulty ladder, Argument & Escalation stages, Blood Oaths) and the **Feud Track** (0 Cold Peace → 4 Mustered War). FL `12-mercenaries-of-forbidden-lands.md:106-194`, `:801-811`.

**FL Faction:** Events are the **Faction Turn** itself — the procedural checks (Community, Development, Prosperity/Logistics, Decree, Acts, Fallout/Burden/Handoff) that fire every Season Turn or Campaign Week depending on Mode of Rule. **Fallout** has its own D66 table. FL `11-politics-of-the-forbidden-lands.md:982-1091`, `:1326-1347`.

**West Business/Town:** Events are the **Business Bonus/Penalty D66**, **Personal Fortunes D66**, and **Town Fortune** rolls at the Turn of the Season. FL `08-campaigns-in-the-old-west.md:631-643`, `:706-742`.

**West Outlaw Band:** Events arise from **Cohesion tests**, **Loyalty** breaking points, and **Wanted** pursuit. FL `11-outlaws-of-the-old-west.md:62-122`, `:508-533`.

**Generic abstraction — events:** Between downtime cycles, the org is *subject to* random/procedural events it did not choose — threats, opportunities, internal friction, or external pressure. Events are the **second agency the world has** (the first is upkeep degeneration). Together, upkeep + events make the org a *living, threatened* thing rather than a static stat block. **Layer:** General (events fire every cycle); their *source* (random table vs procedural turn vs driven by a tracked relationship like Feud/Cohesion) is a dial.

### Beat 5 — Scale escalation

**FL:** The whole point of FL's design is that an org can **climb rungs**: a Stronghold can acquire a Mercenary Company as a function (War Room, garrison); a Mercenary Company can become a Faction's retainer or its field army; a Faction's levy and mercenaries become an Army that resolves in Mass Combat. Each rung re-uses the same lifecycle beats at a larger turn scale. FL `12-mercenaries-of-forbidden-lands.md:916-943` (Allegiance 0→4), `11-politics-of-the-forbidden-lands.md:1191-1201` (Hire Mercenaries writes the band into the army roster).

**West:** West deliberately *caps* escalation — the orgs top out at the town/band scale. A Business stays a Business; a Town grows via Aspects but never becomes a faction with a turn; an Outlaw Band tops out at Outfit (16-30). There is no faction-turn layer and no mass-combat engine. FL `08-campaigns-in-the-old-west.md:69-126`, `11-outlaws-of-the-old-west.md:36-45`.

**Generic abstraction — scale escalation:** An org can be promoted to a higher rung where its lifecycle is re-parameterized (larger turn scale, bigger upkeep, wider event scope, stronger functions). The **ladder** is the explicit deliverable of §9. Crucially: **the five beats do not change between rungs** — only their *amplitude* (turn length, currency size, threat radius). This is what makes FL's interlocking subsystems one engine rather than four. **Layer:** General (the ladder exists); *which rungs are enabled* is the central genre/campaign-length dial (see §9, §11).

## 4. Stronghold (FL)

The Stronghold is FL's canonical "base" — the party's home, workshop, and the first org most campaigns acquire.

**Source instance (Abstraction Ladder):**
- **Founding:** Clear a site or build; CRAFTING roll; Flaw on failure. FL `09-the-stronghold.md:17-22`, `:66-77`.
- **Functions:** HOUSING score is the load-bearing abstraction — **100 units of wood/stone = 1 HOUSING**, capping who can live there; the Functions table (60+ improvements) is the org's expandable capability set. Building table spans Cottage (2 wood) to Palace (520 stone). A **Master Builder** auto-succeeds at construction, removing the flaw risk. FL `09-the-stronghold.md:27-47`, `:285-355`, `:228-230`.
- **Base effects (the "why you want one"):** Undisturbed rest **and** +1 WP per PC per session while the stronghold stands. The org *generates metacurrency* for its owners — this is the economic reason a party wants a base at all. FL `09-the-stronghold.md:55-58`.
- **Work force:** Hirelings (paid), Residents (free, tied to the site), PCs (free, limited time), Slaves (free, reputation cost). Each function names the worker type it needs. FL `09-the-stronghold.md:157-194`.
- **Upkeep:** Per-cycle; Lacking Upkeep D6 (Abandonment/Decay/Mutiny); Non-payment D6; Unguarded D6. Three separate degeneration vectors — *resourcing, payroll, and security* are each tracked independently. FL `09-the-stronghold.md:146-155`, `:240-272`.
- **Events:** Random Events D6 between sessions. FL `09-the-stronghold.md:79-90`.

**Generic abstraction:** The Stronghold is the **rung-1 org**: a place-bound, player-owned capability hub whose entire purpose is to (a) bank downtime labor as permanent functions, (b) generate the metacurrency that powers adventure, and (c) be *threatened* by three independent upkeep vectors so that "going home" is never free. The **base-effects-grant-metacurrency** link is the design's keystone — it binds the downtime layer to the adventure layer economically. **Layer:** General (the rung-1 org pattern); the three-independent-upkeep-vectors model is Optional (a granularity dial — West collapses payroll and resourcing into one Business Roll).

## 5. Town, Property, and Outlaw Band (West)

West runs the same five-beat lifecycle, but at personal/small-org scale and with the rungs above "town" deliberately absent.

### Business & Property (West)

**Source instance:**
- **Cash vs Capital:** Two-currency model. **$250 = 1 Capital.** Cash is adventure currency; Capital is the *illiquid investment* that founds and grows orgs. Capital is gained by starting/investing in a business, buying property, or liquidating. FL `06-life-in-the-old-west.md:11-49`.
- **Founding:** Proprietor (owns/operates), Employee (works for wage + skill access), or Investor (passive capital for share of profit). Business Types Table: 24 types each with a key ability and prerequisites. FL `06-life-in-the-old-west.md:133-186`.
- **Functions:** The business's **key ability** is its function. **Property Features** (Barn, Forge, Garden, Library, Oven, Stables) are built improvements — directly analogous to Stronghold functions. **Property Status** (0-8) is a reputation modifier; **Location** (8 types) sets context. FL `06-life-in-the-old-west.md:230-242`, `:254-307`.
- **Upkeep:** The **season Business Roll** (key ability + help +3 + Competition + Law + relevant aspect). Failure → Business Bonus/Penalty D66; sustained failure → **Going Bust**. Wages paid to employees. FL `08-campaigns-in-the-old-west.md:555-643`, `06-life-in-the-old-west.md:202-210`.
- **Events:** Business Bonus/Penalty D66, Personal Fortunes D66 at the Turn of the Season. FL `08-campaigns-in-the-old-west.md:631-643`, `:706-742`.

**Generic abstraction:** West's **Capital** is the clean two-currency model of org-ownership: liquid adventure money vs illiquid org-founding money. This is the single best-expressed dial in the whole layer — FL has no equivalent (silver buys everything, functions are paid in materials/labor), which makes FL's base-building more *crafting-driven* and West's more *investment-driven*. **Layer:** General (a Capital-like illiquid currency is recommended for any West-style game); Optional for FL-style crafting-driven games.

### Your Town (West)

**Source instance:**
- **The town as a character:** Six **Aspects** — Farming, Mercantile, Natural Riches, Law, Civic, Welfare — each ranked 1-6 by tally. **Prosperity** (total, 6-36) sets Population and modifies the Town Fortune roll. An Aspect at 0 = **town failure**. FL `08-campaigns-in-the-old-west.md:69-126`.
- **Functions = Amenities:** Built improvements (General Store, Church, Saloon, Schoolhouse, Bank, Hotel) ranked by minimum Civic rank, each modifying Aspects. **Settlement Points** (5 SP = one extra amenity). FL `08-campaigns-in-the-old-west.md:128-154`.
- **Upkeep/Events = Turn of the Season:** Looking Back (apply amenities, Business/Congregation rolls) → Looking Forward (choose amenities, Lifestyle, Personal/Town Fortune rolls). The town is an org the *whole table co-owns and co-runs*. FL `08-campaigns-in-the-old-west.md:537-545`.
- **Dynasty:** Legacy XP lets a player continue as a family member after a PC's death — the town outlives the character. FL `08-campaigns-in-the-old-west.md:57-60`.

**Generic abstraction:** West's Town is the **settlement-as-character** model: the org *is* a stat block (Aspects) that the players grow, and its "death" (Aspect 0) is a campaign-ending threat on par with a TPK. This is the rung where "the org is a shared PC" becomes literal. FL has no direct equivalent — FL settlements are *objects a faction acts upon* (Ruled/Protected/Tributary), not characters the players drive. **Layer:** Situational (the settlement-as-character model is a strong fit for West/frontier/dynasty games; FL-style games treat settlements as faction assets instead).

### Outlaw Band (West)

**Source instance:**
- **Founding:** Leader + hideout + 3+ outlaws. The hideout is the non-negotiable founding asset. FL `11-outlaws-of-the-old-west.md:23-34`.
- **Scale tiers:** Crew (3-6) / Gang (7-15) / Outfit (16-30), each adding +1 die to a different domain. **Capped at Outfit** — no faction rung above. FL `11-outlaws-of-the-old-west.md:36-45`.
- **Cohesion 1-5:** The band's morale analog (Broken → Keen), with test triggers and GM adjustment. Directly parallel to FL's Morale 1-5. FL `11-outlaws-of-the-old-west.md:62-122`.
- **Functions = resources:** Refuge (+2 to -2 per settlement), Fence access (0/1/2), Horsestock (0-4), Provisions (D6-D12 resource die). Band Action Checks (4-step procedure, ability table) are the band's "practices." FL `11-outlaws-of-the-old-west.md:128-276`, `:354-423`.
- **Upkeep:** Provisions die depletes; Horsestock must be maintained; **Wanted** level is a permanent external pressure. FL `11-outlaws-of-the-old-west.md:232-276`.
- **Members:** Notable Members have Role/Experience/**Loyalty 1-3**/Ambition/Breaking Point/Leverage — the band is a roster of NPCs with their own failure modes. FL `11-outlaws-of-the-old-west.md:449-533`.

**Generic abstraction:** The Outlaw Band is West's equivalent of FL's Mercenary Company — a **roster-and-cohesion org** where individual members are tracked and the org has a single morale stat. The structural parallel (Cohesion ↔ Morale, both 1-5; Hideout ↔ Stronghold; resources ↔ functions) is exact. The divergence is *ceiling*: West stops at Outfit, FL climbs to Host/Army/Faction. **Layer:** General (the roster-and-cohesion org is a universal rung); the cap is the genre dial.

## 6. Mercenary Company (FL)

The Mercenary Company is FL's **mid-scale org** and the structural bridge between the party (rung 1) and the faction (rung 5). It is also West's Outlaw Band's closest cousin.

**Source instance (Abstraction Ladder):**
- **Founding:** Name + leader + 3+ fighters. FL `12-mercenaries-of-forbidden-lands.md:76-83`.
- **Scale tiers (the rung-amplifier):** Skirmishers (3-6) / Warband (7-20) / Company (21-50) / **Host (51+)**. The Host tier unlocks **Host Play** — a Warmaster and a **Ledger** (-6 to +6) that abstracts the Host as a single trackable entity rather than counting individuals. This is the engine's built-in *abstraction-collapse mechanism*: past ~50 bodies, you stop tracking bodies and start tracking a number. FL `12-mercenaries-of-forbidden-lands.md:88-104`.
- **MORALE 1-5** (Broken → Keen): the org's single morale stat, with ±1 modifiers and a **Grievance Difficulty 1-4** ladder. MORALE Triggers table fires events when the band is mistreated. FL `12-mercenaries-of-forbidden-lands.md:106-194`.
- **Functions:** Contracts (Patrol/Escort/Clearing/Raid/Garrison/Intelligence/Caster), **DRILL** (Training Grounds → trained status → dice upgrades), Hired Casters, the **War Room** stronghold function (runs the company from the base). FL `12-mercenaries-of-forbidden-lands.md:965-1023`, `:1413-1433`.
- **Recruitment:** Settlement pool (D6/2D6/3D6 by settlement size); fighter quality tiers (Common 1s/day, Veteran 2s, Elite 3s). FL `12-mercenaries-of-forbidden-lands.md:269-337`.
- **Upkeep:** Pay (Retainer weekly vs Mission daily) + Feeding (forager output by terrain). **Field Non-Payment** D6 (desertion/mutiny). Feud Track (0 Cold → 4 Vengeance). FL `12-mercenaries-of-forbidden-lands.md:363-392`, `:493-526`, `:555-568`, `:801-811`.
- **Allegiance 0-4** (Unknown → Sworn): the dial that determines whether the band is a *free org* (the players' company) or a *faction asset* (a retainer). At Allegiance 4 the band has effectively been promoted up the ladder into another org's structure. FL `12-mercenaries-of-forbidden-lands.md:916-943`.
- **Internal life:** Discipline (Minor/Serious/Capital offenses, Flogging, Duels), Arguments & Escalation (4 stages Words→Blood), Blood Oaths (Brotherhood/Bounty/Vengeance), Atrocities (reputation consequences). The band is a *society* with its own law. FL `12-mercenaries-of-forbidden-lands.md:1447-1488`, `:1604-1647`, `:1731-1761`.

**Generic abstraction:** The Mercenary Company is the **roster-and-cohesion org at scale**: a tracked headcount, a single morale stat, a pay/feed upkeep cycle, and — critically — a **scale-tier system with an abstraction-collapse threshold** (Host Play). The abstraction-collapse mechanism is the design's answer to "how do you scale a roster org past the point where tracking individuals is fun?" Answer: you don't; you collapse the roster into a single ledger number and a single commander. This same move recurs at the faction/army rung. **Layer:** General (roster-and-cohesion org); the abstraction-collapse threshold (Host Play) is Optional but *strongly recommended* for any game whose roster org can grow past ~30-50 members.

## 7. Factions, Legacies, and the Faction Turn (FL)

The Faction is FL's **high-scale org** and the only place in either game where a full **board-game-style turn layer** runs *above* the players' adventure play. It is the rung where "the world moves while the PCs do."

### The faction as stat block

**Source instance:**
- **Pillars (the four core stats):** **Mandate** (legitimacy), **Force** (armed strength), **Reach** (mobility/communication), **Hearth** (sustaining base). Tier sets starting pillars: Thin (3,3,2,2) / Established (4,3,3,3) / Dominant (5,4,4,3). A pillar at 0 triggers a collapse effect (Mandate 0 = no one obeys; Force 0 = cannot muster; Reach 0 = isolated; Hearth 0 = cannot sustain). FL `11-politics-of-the-forbidden-lands.md:206-217`, `:345-377`.
- **Practices (the 16 "skills"):** grouped under pillars — Mandate (Claim, Decree, Accord, Rite), Force (Muster, Discipline, Assault, Siegecraft), Reach (Watch, Intrigue, Relay, Traffic), Hearth (Yield, Provision, Works, Relief). FL `11-politics-of-the-forbidden-lands.md:380-454`.
- **Legacies (the 9 "talent trees"):** Claimant House, Tribute Throne, Mustering Crown, Walled Seat, Toll Court, Sacred Seat, Veiled Court, Riding Lord, Dread Throne — each a 5-rank drilled custom of power. FL `11-politics-of-the-forbidden-lands.md:458-552`.
- **Resources:** Treasury & Stores (Bare/Thin/Sound/Deep backing tracks), Labor/Levy/Retainers (None→Heavy). **Basis of Rule** (Blood Right, Old Custom, Protection, Conquest, Wealth, Cult Sanction, Oath Confederacy, Dread) flavors how the faction is *legitimately held*. FL `11-politics-of-the-forbidden-lands.md:273-341`.

**Generic abstraction:** The faction is an org with a **four-stat block** (legitimacy / force / reach / sustain), a **skill list** (practices), a **talent tree** (legacies), and **backing resource tracks**. This is structurally a *character sheet at polity scale* — the same skeleton (attributes → skills → talents → resources) as a PC, re-skinned. The **basis of rule** is the unique addition: it encodes *why the org is obeyed*, which is the question that only polity-scale orgs must answer. **Layer:** General (the four-pillar stat block is the recommended polity-scale skeleton); the basis-of-rule flavor system is Optional but high-value.

### The Faction Turn

This is the central procedural engine of the high-scale rung.

**Source instance:**
- **Mode of Rule sets turn scale:** Peace/Pressure = **Season Turn**; Muster/Campaign = **Campaign Week**. The *faster the faction is spending itself, the shorter its turn*. FL `11-politics-of-the-forbidden-lands.md:988-997`.
- **The procedure (Peace, as template):** (1) Recover pillar; (2) Community roll (Mandate+Accord/Rite); (3) Development roll (Hearth+Works); (4) Prosperity roll (Hearth+Yield or Reach+Traffic); (5) Decree step; (6) Acts (one major + one minor); (7) Fallout. Pressure/Muster/Campaign variants swap the pillar+practice pairings and tighten the act economy (Muster/Campaign get one *campaign act* instead of major+minor). FL `11-politics-of-the-forbidden-lands.md:1009-1091`.
- **The roll:** **pillar + practice + one asset source + modifiers.** Asset source contributes 1-5 asset dice by rating; only the single highest asset applies (no stacking). Overwhelming advantages use an **Ascendancy Die** (D8/D10/D12) that *replaces* a d6. FL `11-politics-of-the-forbidden-lands.md:806-848`.
- **Faction Acts (the action menu):** Minor (Call Council, Collect Due, Give Safe-Conduct, Issue Decree, Send Gift, Spy), Major (Grant Protection, Hire Mercenaries, Judge/Outlaw, Negotiate Truce, Press Claim, Swear Fealty, Take Hostage), Campaign (Call Levy, Invest a Place, Raid). FL `11-politics-of-the-forbidden-lands.md:1105-1322`.
- **Fallout D66:** a failed act never means "nothing" — it always leaves a colder village, a bolder rival, a damaged road. FL `11-politics-of-the-forbidden-lands.md:1326-1347`.
- **Settlement bonds:** Ruled / Protected / Tributary / Vassal / Occupied / Allied — the status ladder the faction acts upon. **Feud Track** (0 Cold Peace → 4 Mustered War) governs when politics becomes war. **Standing** (-2 to +2) is local memory. FL `11-politics-of-the-forbidden-lands.md:907-977`.

**Generic abstraction — the faction turn:** A **procedural turn layer** that runs on its own clock (Season or Week), resolves org-vs-org and org-vs-world pressure through a **stat+skill+asset roll** identical in grammar to a PC roll, and whose turn length and act economy are *parameterized by a Mode dial* (peaceful factions get slow turns + flexible acts; warring factions get fast turns + tight acts). The genius move is that **the same resolution grammar (attribute+skill+asset+modifiers, push, banes-damage-pillar) is reused at polity scale** — the downtime layer does not invent a new engine, it *re-scales the existing one*. **Layer:** General (the procedural turn is the defining feature of the faction rung); the Mode-parameterized turn length is a **core design dial** (see §11). West has *no faction turn* — this is the largest single FL/West divergence in the whole layer.

### Campaign Points, Agents, and Advisors

**Source instance:**
- **Campaign Points (CP):** Awarded only when something *real changes in the world* (Minor success 1, Major 2, Significant victory 5, Great conquest 10) — never for routine success. CP heals pillars OR raises practices/pillars/legacies. FL `11-politics-of-the-forbidden-lands.md:556-624`.
- **Agents:** Named hands sent out (champion, rider, spy, a whole fellowship). Resolved as multi-roll **Undertakings** (1 roll per CP of deed-value), with Seen Steps producing a trail. **Player characters can be agents** — and when they are, the faction turn sets the field but the dangerous work plays out in ordinary adventurer time. FL `11-politics-of-the-forbidden-lands.md:628-741`.
- **Advisors:** Named hands at the seat; **Seat Work** banks bonus dice for later faction rolls. FL `11-politics-of-the-forbidden-lands.md:743-800`.

**Generic abstraction:** CP is the faction's **XP**, gated by *fictional consequence* rather than session count. Agents/Advisors are the **bridge between the faction turn and PC play** — they are the mechanism by which "the faction wants X" becomes "the players go do X at the table." This bridge is what prevents the faction layer from becoming a dissociated board game. **Layer:** General (an XP-equivalent gated by world-change); the Agent-as-PC bridge is **essential** for any campaign that wants the faction layer to drive adventure rather than replace it.

## 8. Mass combat and sieges (FL)

Mass Combat is FL's **top rung** — the resolution engine for when org-scale conflict produces open violence. It is the only place the engine *replaces* individual conflict with an abstraction over it.

### Troop dice and the battle sequence

**Source instance:**
- **Troop Dice are a three-color pool, exactly mirroring the core loop's dice grammar:** **Base Dice** (from raw numbers — Infantry/Skirmishers 20/unit max 100 = 5 dice; Cavalry 5/unit max 25; Monster 1/unit max 5), **Advantage Dice** (from quality — well-trained, race, fervor, Important Character present, flanking +1/rear +2), **Protection Dice** (from armor — Small/Large shield, Leather/Chainmail/Plate). Veterans upgrade Advantage Dice D6→D8→D10→D12 after 3+ engagements. FL `12-battles-and-sieges.md:111-186`, `:195-234`.
- **The battle sequence:** 15-minute game turns; Army Lines (vanguard + reserves); three Battle Line Sections (left/center/right) → three rolls/side/turn. Screening/Pickets → Deployment (INSIGHT) → General's Speech (PERFORMANCE → morale points) → Challenge (duel) → Battle Turns loop → Battle Roll → Pressing the Advantage (spend 1/2/3 successes) → Damage → Morale Points → No Quarter. FL `12-battles-and-sieges.md:54-104`, `:243-450`.
- **Commander agency:** Important Characters move between troops granting advantage dice; REGROUP rolls rally fleeing troops; Ordered Retreat; Pursuit; Surrender (field/garrison). FL `12-battles-and-sieges.md:453-537`, `:563-573`.
- **Special conditions:** Ranged troops & range, skirmisher morale, terrain (High Ground +1 advantage, Mud, Forest, River Crossing half-dice, Prepared Ground, Field Works), Weather D6, Night Attack, Feigned Retreat (opposed PERFORMANCE vs INSIGHT), Ambush (SCOUTING). FL `12-battles-and-sieges.md:541-685`.

**Generic abstraction:** Mass combat **reuses the core loop's three-color dice grammar at org scale** — Base↔numbers, Advantage↔quality/training, Protection↔armor. This is the same abstraction-collapse move as Host Play: instead of rolling for each soldier, you roll a *pool that represents the unit*, and the pool's composition (how it was built) encodes everything that would matter in individual combat. **Player agency is preserved** through Important Characters who move between sections and through the General's sequence of command decisions (speech, deployment, challenge, retreat, pursuit). The mass-combat layer is thus *not* a different game — it is the same game with the dice repurposed to represent formations. **Layer:** Optional (mass combat is the top rung; many campaigns never reach it); but when enabled, reusing the core dice grammar is **strongly recommended** over inventing a new system.

### Sieges

**Source instance:**
- **The inversion:** In siege, defenders need only **10 units per base die** (vs 20 in the field) — walls compress and multiply defensive effectiveness. Walls grant **attack-first** and advantage dice by height/strength. FL `12-battles-and-sieges.md:694-714`.
- **Siege Engines** (built on-site, require an engineer at 5 silver/day): Battering Ram (7 days, siege dice, gate breaks at cumulative 3), Siege Tower (30 days, negates wall advantage at contact), Catapult (14 days, 4 attack dice/day, reduces wall advantage), Trebuchet (60 days, 8 dice/day), Tunnel (2D6 successes to complete, stability mechanic, collapse risk). FL `12-battles-and-sieges.md:728-768`.
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

**Generic abstraction:** The mass-combat layer's *true* engine is **logistics, not tactics.** The battle sequence is dramatic, but the supplies/disease/march rules are what actually decide most campaigns: an army is a *metabolism* with a daily consumption rate, a depletion-curve for foraging, a stacking demoralization penalty for every skipped maintenance quarter-day, and a disease subsystem that punishes crowding. The design intent is unmistakable: **most wars are lost by arithmetic, not by the battle roll.** The siege doubling of disease, the foraging depletion, the "accumulated demoralization stacks 1→4" rule — all encode the same thesis: *the org that cannot feed and shelter itself loses before swords are drawn.* **Layer:** Situational (logistics rules only matter when the campaign sustains multi-week field operations); but when mass combat is enabled, **the logistics layer is more important than the battle sequence** — omit it and wars become board-game pieces; include it and wars become the attritional nightmares that decide real campaigns.

## 9. The scale-escalation ladder

This is the file's second core deliverable. The five-beat lifecycle is *invariant* across rungs; what changes is the **turn scale, currency size, threat radius, and which subsystems are enabled.** Each rung is defined by: **what it owns, what turn it runs on, what it costs, what it threatens, and which subsystem it uses.**

| Rung | Org | Turn scale | Currency | Threatens | Subsystem | FL instance | West instance |
| --- | --- | --- | --- | --- | --- | --- | — |
| **Solo** | a lone PC | scene | WP / Faith | themselves | core loop | adventurer | gunslinger |
| **Party** | the fellowship | session/adventure | shared WP, shared pride | a lair, a quest | core loop + journeys | the party | the posse |
| **Band** | a small roster org | week | pay + provisions + cohesion | a hideout, a score | roster-and-cohesion | Mercenary Band (Skirmishers) | Outlaw Crew / Business |
| **Company** | a large roster org | week/month | pay + stores + morale + feud | a settlement, a contract | roster-and-cohesion + abstraction-collapse | Mercenary Company / Host (Ledger) | Outlaw Gang/Outfit / Town |
| **Faction** | a polity-scale org | season/week | pillars + treasury + stores + levy | a region, a succession | faction turn + practices + legacies | FL Faction (pillars/practices/legacies) | *(absent)* |
| **Army** | a field force | day/quarter-day | supply units + troop dice | a campaign, a siege | mass combat + logistics | FL Army (troop dice) | *(absent)* |
| **Polity** | a ruling power | season + campaign | pillars + CP + burden | a kingdom, a dynasty | faction turn + mass combat + dynasty | FL Faction at Dominant tier + Army | *(absent)* |

### Rung mechanics

- **Solo → Party** is free (the core loop handles it; no new subsystem).
- **Party → Band** requires the **roster-and-cohesion subsystem**: a tracked headcount, a single morale stat (Morale/Cohesion 1-5), a pay/feed cycle, and a degeneration table for non-payment.
- **Band → Company** requires the **abstraction-collapse threshold** (Host Play / Ledger): past ~50 bodies, stop tracking individuals. Without this, the roster org becomes unmanageable.
- **Company → Faction** requires the **faction turn**: a procedural turn layer with a Mode dial, a stat+skill+asset roll, an act economy, settlement bonds, and a Feud track.
- **Faction → Army** requires the **mass-combat + logistics subsystem**: troop dice (reusing the core grammar), the battle sequence, supply/disease/march.
- **Army → Polity** is not a new subsystem — it is the *integration* of faction turn + mass combat + dynasty/CP advancement. The polity rung is where all lower rungs interlock.

### Genre / campaign-length guidance — which rungs to enable

This is the central practical output of the ladder.

- **One-shot / short campaign (3-8 sessions):** Enable **Solo → Party** only. A base may exist as color (a place to rest) without tracked functions/upkeep. *Do not* enable the band rung — there is no time to pay it off.
- **Standard campaign (1 season, ~10-20 sessions):** Enable **Solo → Band**. A Stronghold/Business with functions and upkeep gives players "something that grows." A roster org (small mercenary band or outlaw crew) is viable if the campaign is about that org. *Do not* enable the faction turn unless the campaign is explicitly political.
- **Long campaign (multi-season, 20-60 sessions):** Enable **Solo → Company**. The abstraction-collapse threshold matters now. A Mercenary Company or growing Town becomes the campaign's spine. The faction turn can be introduced in the back half as escalation.
- **Epic / dynasty campaign (60+ sessions, or generational):** Enable the **full ladder through Polity.** The faction turn runs alongside PC play; PCs serve as Agents; mass combat resolves the wars the faction turn produces. West's Dynasty rules (Legacy XP, play a family member) are the model for the generational layer. FL `08-campaigns-in-the-old-west.md:57-60`.

### The two canonical configurations

- **FL configuration (full ladder, interlocking):** All rungs enabled. The lifecycle beats recur at each rung with amplified amplitude. The faction turn and mass combat are *expected* end-states. This is the "campaign-as-saga" configuration.
- **West configuration (personal/small-org, capped):** Rungs Solo → Company only. No faction turn, no mass combat. The Town is the *de facto* top org, run as a shared character. This is the "campaign-as-community" configuration. The cap is a *feature*: West's genres (frontier, dynasty, outlaw) are about people and places, not polities and armies.

**The dial:** a new game chooses its *ceiling rung* first, then enables every rung up to it. The ceiling is the single most consequential campaign-design decision in the downtime layer — it determines session count viability, bookkeeping load, and whether the game is "about" individuals, communities, or power. **Layer:** General (the ladder is universal); the ceiling is a **core design dial** (see §11).

## 10. Divergence rows (FL vs West)

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
| **Base → metacurrency link** | Stronghold grants +1 WP/PC/session | (Business grants coin/profit, not metacurrency) | Base fuels adventure directly vs base fuels economy | FL link recommended — it's the economic reason to want a base |
| **Settlement relationship ladder** | Ruled/Protected/Tributary/Vassal/Occupied/Allied + Feud 0-4 | (Town Aspects + Standing) | Explicit political-status machine vs organic community stats | FL ladder for conquest/politics; West stats for community growth |
| **Generational play** | (via Faction + Dynasty-of-house legacies) | Dynasty: Legacy XP, play a family member | Polity-scale dynasties vs family-scale dynasty | West Dynasty is the cleaner model for family sagas |
| **Random-event source** | D6 tables (Stronghold, Non-Payment, Unguarded, Upkeep) + Faction Fallout D66 | Season Fortune rolls (Business, Personal, Town) | Discrete-threat tables vs seasonal-fortune rolls | D6 tables for grit; Fortune rolls for dramatic pacing |

## 11. Dials and instantiation recipe

Each dial has FL and West as two calibrated points. To build a new game's downtime layer, set each dial.

1. **Ladder ceiling** — Solo/Party/Band/Company/Faction/Army/Polity. *(The single most consequential decision: sets session-count viability and bookkeeping load. See §9.)*
2. **Org-founding currency** — materials+labor / Capital (illiquid) / hybrid. *(Crafting-driven vs investment-driven base-building.)*
3. **Base → metacurrency link** — on (base grants WP/Faith) / off (base grants only economy). *(Whether the downtime layer directly fuels adventure.)*
4. **Upkeep vectors** — one (single roll) / three (resourcing, payroll, security) / custom. *(Granularity of "the org is threatened.")*
5. **Roster-org morale model** — single stat (Morale/Cohesion 1-5) / single stat + per-member loyalty / none. *(How much the roster's people are tracked.)*
6. **Abstraction-collapse threshold** — on (Ledger/Host Play past ~50) / off (cap the roster). *(Whether the roster org can scale indefinitely.)*
7. **Faction turn** — on / off. *(Whether the world moves procedurally while PCs act. The largest FL/West divergence.)*
8. **Faction-turn Mode dial** — on (turn length parameterized by Mode of Rule) / off (fixed turn length). *(Whether peaceful and warring factions run at different speeds.)*
9. **Faction stat block** — four-pillar (Mandate/Force/Reach/Hearth) / custom. *(The polity-scale skeleton.)*
10. **Town model** — settlement-as-character (Aspects) / settlement-as-faction-asset (status ladder) / hybrid. *(Whether the community is a PC or an object.)*
11. **Mass combat** — on (reuse core dice grammar at unit scale) / off (handwave). *(Only enable if the campaign sustains field operations.)*
12. **Logistics layer** — on (supply/disease/march/forage-depletion) / off. *(More decisive than the battle sequence when enabled.)*
13. **Generational play** — on (Dynasty/Legacy XP) / off. *(For family-saga or multi-decade campaigns.)*

**Instantiation recipe (any genre):**

1. **Set the ladder ceiling first (dial 1).** This is determined by intended session count: <8 sessions = Party; 10-20 = Band; 20-60 = Company; 60+ = Polity. Do not enable a rung the campaign cannot sustain.
2. **Decide the faction turn (dial 7).** If the campaign is political/strategic, enable it and set the Mode dial (8). If it is character/community-focused, leave it off — this single choice saves enormous bookkeeping.
3. **Choose the org-founding currency (dial 2) and the base→metacurrency link (dial 3).** These determine whether base-building feels like crafting (FL), investing (West), or both.
4. **Set the upkeep vectors (dial 4) and roster morale (dial 5).** Match grit to genre: survival/horror wants three vectors + per-member loyalty; dramatic/pulp wants one vector + a single morale stat.
5. **If the roster org can exceed ~30-50 members, enable abstraction-collapse (dial 6).** Without it, the roster becomes unmanageable.
6. **If mass combat is enabled (dial 11), reuse the core dice grammar at unit scale and include the logistics layer (dial 12).** Do not invent a new combat system, and do not omit logistics — it is what makes wars feel like wars.
7. **Choose the town model (dial 10)** to match whether the community is a protagonist (West) or a prize (FL).
8. **Validate against the adventure layer:** ensure the base→metacurrency link, the Agent bridge (PCs as faction agents), and the CP/XP gate are all wired so the downtime layer *drives* adventure rather than replacing it.

## 12. Design intent

The downtime org layer is engineered to turn **one-shots into campaigns** by giving players *something that grows and is threatened*. Specifically:

- **The five-beat lifecycle (founding → functions → upkeep → events → scale)** is invariant across every org type in both games. A Stronghold, a saloon, a mercenary band, a faction, and an outlaw crew are *the same pattern at different amplitudes*. This is why FL's four interlocking subsystems are one engine, not four — and why a new genre can lift the pattern wholesale and re-skin it.
- **Upkeep + events are the org's two sources of world-agency.** Without them, an org is a static stat block the players optimize. With them, the org is a *living, hungry, threatened* thing that generates session hooks every cycle ("the hirelings haven't been paid," "a monster laired in the cellar," "the Feud advanced to Armed"). The degeneration tables are the downtime layer's equivalent of the core loop's bane — *latent pressure that activates when the org is neglected.*
- **The base → metacurrency link (Stronghold grants WP)** is the economic keystone that binds the downtime layer to the adventure layer. It is the reason a party *wants* a base: not for color, but because the base literally fuels their talents. Cut this link and base-building becomes a dissociated minigame.
- **The scale ladder lets a campaign escalate without changing engines.** Because each rung reuses the same lifecycle beats (and, at the top, the same dice grammar), a campaign can begin as a party clearing a lair and end as a polity fighting a war — *without ever switching systems.* The abstraction-collapse threshold (Host Play) and the grammar-reuse in mass combat are the two mechanical moves that make this possible.
- **The faction turn lets the world move while the PCs do.** It is the only subsystem that runs on its own clock above play, and its absence in West is the largest single design difference: West's world is the community the PCs build; FL's world is the politics that happens around them. Neither is superior — they serve opposite fantasies (community vs power).
- **Logistics, not tactics, decides campaigns.** FL's mass-combat layer encodes the thesis that wars are lost by arithmetic (supply depletion, disease doubling in sieges, stacking demoralization from hunger+forced-march+poor-sleep). The battle sequence is dramatic; the supplies/disease/march rules are decisive. This is the layer's most historically honest design choice.
- **The ladder ceiling is the campaign-design dial.** Choosing how high the ladder goes is choosing what the campaign is *about*: individuals, communities, or power. West caps the ladder to stay focused on people and places; FL extends it to make the campaign a saga. A new genre's job is to find its ceiling and enable every rung up to it — and no further, because every rung above the ceiling is bookkeeping the campaign cannot repay.

The divergence between FL and West is not accidental — it is the layer's proof that **the same five-beat pattern produces opposite campaign shapes by choosing a different ceiling.** FL's full ladder makes a game where the campaign *escalates into power*; West's capped ladder makes a game where the campaign *deepens into community.* A new genre's job is to find its ceiling and let the pattern do the rest.
