<!-- markdownlint-disable MD013 -->

# GM Procedures — Principles, Encounters, Settlements, Solo

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the GM-facing operating manual — how a GM *runs* the engine with minimal prep. Cross-refs `00-engine-core.md` (the loop these procedures apply), `10-design-philosophy.md` (the axioms behind these procedures), `06-travel-and-downtime.md` (the journey/quarter-day frame), and `07-base-faction-mass-scale.md` (the base/faction layer these settlements and tracks feed).

## Contents

1. Source provenance
2. Abstraction target
3. GM principles (the FL seven, de-flavored)
4. The encounter engine (D66 tables, reoccurring encounters)
5. Settlement / town generators plus civic, legal, and reputation procedures
6. NPC statblock grammar
7. Solo-play engine
8. Consequence / fortune / faction tracks
9. Adventure-site structure
10. Divergence rows (FL vs West)
11. Rule Choices and Build Recipe
12. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/08-journeys.md:686-1234` — Reputation, Standing, hospitality, first impressions, rumors, villages/towns, notice boards, seek work, petitioning authority, trade, carouse, healing, rest, training.
- `01-corebook/08-journeys.md:1235-1445` — crime and punishment: offenses, detection, capture, judgment, defending, sentences, weregild, imprisonment, outlawry, sanctuary.
- `02-gamemasters-guide/02-the-gamemaster.md:25-67` — the 7 Principles of the Game; `:69-78` first session; `:93-99` handling NPCs; `:101-121` NPCs/opposition; `:123-127` consumables; `:129-135` failure (fail forward); `:137-179` stronghold events (D66 table, Reputation-weighted D66 tens roll).
- `02-gamemasters-guide/08-encounters.md:1-39` — scouting, the 9-column terrain-keyed D66 encounter matrix; `:41-48` reoccurring encounters; `:50-637` 44 numbered encounters (each: prose + statblock + terrain tags + branching outcomes).
- `02-gamemasters-guide/10-villages.md` (~980 lines) — settlement history (seed+consequence `:18-75`), size/condition/density (`:86-112`), problem/peculiarity/government (`:114-203`), locations & resource-die economy (`:205-353`), character generator (`:360-572`), situations & event generator (`:588-823`), **vicissitudes** 3D6+variables (`:825-897`), **settlement turn** 2D6 (`:899-924`), **household ledger** Need/Heat (`:926-931`), stores & shortages (`:933-936`), route links (`:938-952`), justice & retaliation (`:965-976`).
- `02-gamemasters-guide/09-adventure-sites.md:9-39` — the site-as-dungeon model (Village/Dungeon/Castle, locations+NPCs+events, no preset narrative, legends, 15-min turn).
- `03-book-of-beasts/04-solo-rules.md:1-374` — the solo/GMless layer (companions, quarter-day procedure, new-hex draw, card oracles).

**Tales of the Old West 2E (West):**
- `01-corebook/06-life-in-the-old-west.md:1379-1503` — "Folks of the Old West" generic NPC statblocks (8-column layout).
- `01-corebook/08-campaigns-in-the-old-west.md` — campaign drivers (`:13-51`), **Your Town** six-Aspect model + Prosperity (`:67-126`), amenities (`:128-442`), **Turn of the Season** fortune rolls (`:537-839`: Business, Personal Fortune, Town Fortune), campaign seeds (`:843-869`).
- `01-corebook/09-the-new-mexico-campaign.md` — territory-wide campaign framework (King of Santa Fe).
- `03-adventures/01-quiet-title.md:211-226` — four-track Faction Standing ledger; `:304-321` week-ticked Faction Clocks; `:384-436` multiple-roads-through sandbox doctrine.

## Abstraction target

Reverse-engineer the **GM-facing procedures** into a genre-neutral toolkit: a short list of **design axioms** (the FL seven, stripped of setting nouns), a **random-but-weighted encounter engine** (the D66 terrain matrix + the reoccurring-encounter rule), a **settlement-as-character model** both games share (FL's village generator with vicissitudes and household ledger; West's six-Aspect town with fortune rolls), a **minimal NPC statblock grammar**, an optional **solo/GMless layer**, and a **campaign-state tracker** pattern (West's Turn-of-the-Season fortune rolls + Quiet Title's four-track ledger; FL's stronghold-event table + faction feuds). The deliverable is the transferable procedures that let a GM *play* the engine rather than *prepare* it forever. Apply the Abstraction Ladder to each.

## 3. GM principles (the FL seven, de-flavored)

FL states seven explicit principles to "help you create the right feeling in the game and to guide you when you are unsure" (`02-the-gamemaster.md:25-27`). They are the engine's philosophy in operation — the procedural expression of the axioms in `10-design-philosophy.md`. Stripped of FL nouns, they generalize as follows. **Layer: General** (restate 5–7 for any new game; they are the GM's load-bearing judgement rules where the dice are silent).

| FL principle (source) | De-flavored axiom | What it makes the GM *do* |
| --- | --- | --- |
| **1. The World Lies Before You** (`:29-33`) — the map is open; place challenges, don't steer | **Open-table / player-driven agenda** — present a legible opportunity space; answer questions and inspire, never railroad. | Provide a map/menu of hooks; let the party set vector; inject obstacles along their chosen path. |
| **2. The Land Is Full of Legends** (`:35-39`) — deliver history through in-fiction rumor, not lecture | **Lore as player-facing rumor** — world-history is distributed as legends attached to monsters, places, NPCs; revealed by play. | Tag every site/foe/relic with a legend handout; gate lore behind contact, not GM monologue. |
| **3. The Adventurers Make Their Own Fate** (`:41-45`) — no assigned missions; build on player choices; ask questions | **Say-yes-to-player-agenda / ask-and-build** — the GM listens, asks follow-up questions, and writes challenges that answer the players' stated wants. No pure good/evil; the table decides what's right. | Mine character creation for hooks; never override a declared PC intent with plot armor. |
| **4. Nothing Is for Free** (`:47-51`) — the more they want, the more they fight; struggle for necessities; hold back rewards | **Scarcity / cost-of-safety** — desire indexes price; safety, food, water, treasure are all under pressure; "never let them feel content for more than a second." | Gate every gain behind a roll, a cost, or a risk; see `10-design-philosophy.md` §6. |
| **5. Them That's Got Shall Lose** (`:53-57`) — riches attract predators; a stronghold must be defended | **Acquisition-as-target / the tall-flower axiom** — every pile of loot or base the party builds becomes a magnet for rivals, siege, and intrigue. | Convert PC wealth into NPC motive; turn the base into a defended asset (see §8 tracks, `07-base-faction-mass-scale.md`). |
| **6. Death Is Part of the Story** (`:59-63`) — easy to break, hard to die; never kill a defenseless PC; mark the tomb and journey on | **Lethality-as-story / no execution of the helpless** — death is possible and meaningful; the GM protects *story* death over *rules* death, but does not make PCs immortal. | Allow death at real stakes; never execute a helpless PC when a more interesting fate exists; ritualize the loss (tombstone on the map). Cross-ref `04-harm-and-consequences.md`. |
| **7. The End Is Never Set** (`:65-67`) — never predetermine the finale; the climax is the *choices*, not the battle | **Emergent finale** — even scripted campaign modules offer only a *suggested* climax; the decisive moment is the players' choice, not the GM's set-piece. | Frame endings around decision points, not set battles; let the finale be what the accumulated choices make it. |

**Supporting procedures (FL, generalized):**
- **First session as prologue** (`:69-78`): mine character creation for hooks; pick one site near the start; prepare at most one random encounter; "listen more than you talk"; treat session one as tentative. **Layer: General.**
- **Failure is fail-forward** (`:129-135`): a failed roll must push the story in a new direction or deepen the danger — never grind it to a halt. In combat, a lost turn is sufficient; elsewhere, add a complication. **Layer: General** (see `00-engine-core.md` §6 on the failure-pressure layer).
- **Consumables fluctuate** (`:123-127`): let food/water/arrows/torches be sometimes easy, sometimes life-or-death, so players "can't take resources for granted" but the game isn't *all* foraging. **Layer: General** (the resource-at-risk model; `08-gear-and-economy.md`).
- **NPCs run on narrative, not full sheets** (`:93-99`): NPCs technically use PC rules, but "disregard all rule-crunching unless it directly affects a PC"; don't track NPC rations — let their food run out "at the dramatically appropriate time"; only roll for NPC actions that attack or heal a PC. **Layer: General** (this is what makes the statblock grammar in §6 minimal).
- **Important NPCs survive** (`:101-111`): avoid killing named NPCs early — a returning foe is more useful than a dead one; block paths to bosses with underlings; killing a boss has consequences (allies seek revenge, underlings defect). **Layer: General.**

## 4. The encounter engine (D66 tables, reoccurring encounters)

**The shared structure (FL; West inherits the doctrine in its campaign-seed/adventure design):** a single roll (D66 = two D6 read as tens+units) selects an encounter, but the *same roll result resolves differently by terrain/context* via a keyed matrix. FL's master table (`08-encounters.md:19-39`) maps each D66 result to a numbered encounter *per terrain column* — Plains, Forest, Dark Forest, Hills, Mountains, Lake, Marshlands, Quagmire, Ruins. So `D66 42` = encounter 1 in Plains, 35 in Mountains, 0 (no encounter) in Lake. The matrix is **terrain-weighted**: a low roll (11–36) is uniformly "no encounter" across all terrains; the dangerous terrains concentrate their signature threats at the high end. **Layer: General.**

**Scouting as the pre-encounter decision point** (`:11-15`): the lookout makes a straight SCOUTING roll (not opposed, unless the threat is actively ambushing). Success = threat spotted at safe distance → the party chooses to show themselves, ambush, or sneak away. Failure = threat is "up close and personal." This is the engine's *information-before-commitment* beat — it converts the random table from a punishment into a *choice under uncertainty*. **Layer: General.**

**The encounter entry grammar (FL, `:50-637`):** each of the 44 numbered entries is a self-contained module with a fixed shape:
1. **Atmospheric read-aloud** (evocative present-tense prose; the "you smell/see/hear" hook).
2. **The situation** — who/what, with named NPCs, motives, and a specific complication (not generic "2D6 orcs attack").
3. **Branching outcomes** keyed to player approach (fight, parley, aid, ignore) — each with consequences that ripple forward (a clan remembers, a debt is created, a witness survives).
4. **Statblock** only if combat is likely (the minimal grammar in §6).
5. **Terrain tags** — which columns the entry can appear in.

The signature trait: **encounters are situations, not statblocks.** Most can be resolved without combat; many *should* be. Slavers (`:124-143`), bandits (`:202-221`), bounty hunters (`:630-636`) each carry a named leader, a reason they are here, and a fork the party's choices determine. **Layer: General.**

**Reoccurring encounters (`:41-48`):** when the same entry is rolled again, choose one: (a) **continue** — the same people/creature return, changed by the last meeting; (b) **change** — a similar but different entity; (c) **re-roll.** This is the engine's *memory* rule — it turns a flat random table into a *growing cast*. FL's standout example is the Demon Baker (`:288-301`), whose three documented return-states (cottage → 70 loaves → march on the village) model how a reoccurring encounter *escalates on a clock of its own*. **Layer: General.**

**Abstract pattern — "the random-but-weighted table":** a D66 selector whose result is *remapped by a context column* (terrain, district, faction territory, season), plus a reoccurring rule that gives the table memory. The **choices** are: (1) the number of context columns, (2) the "no-encounter" floor (how much of the table is safe), (3) the density of named/situational entries vs. pure-combat entries, (4) whether reoccurring encounters escalate on a track. FL is the high-density, high-situation pole; a lighter game might use a D6 table with one column and pure-statblock entries.

## 5. Settlement / town generators (the settlement-as-character model)

Both games treat the home settlement as **a character with attributes, a state that changes between visits, and a balance sheet** — not a static backdrop. This is the engine's most transferable GM procedure.

**FL — the village generator (`10-villages.md`):** a settlement is built top-down through layered D66 tables:
- **History** (`:18-75`): age → number of historical events → seed-and-consequence pairs (e.g. "A feud over pasture turned bloody… …divided the households"). Each event leaves a physical mark on the place.
- **Present** (`:77-203`): size (Outpost→Town, `:86-92`), general condition (`:94-102`), population density (`:104-112`), a **problem** (`:114-147`, the active threat), a **peculiarity** (`:149-190`, what strangers remember), a **government type** (`:192-203`).
- **Locations** (`:205-353`): rolled per the size count; each has size, condition, service quality, profitability; plus a **resource-die economy** (`:322-353`) — wood/stone/iron/silver/gold/pasture each have a die size (D6–D12) that degrades on a 1 and can recover if left alone. This is the engine's scarcity model applied to *place*.
- **Characters** (`:360-572`): a full NPC generator — profession → primary skills → experience level → reputation → objective+method → wealth → gear. The generator can produce attributes up to 8 (PC max is 6) — "when one appears, let the players feel it" (`:374`).
- **Situations** (`:588-823`): a seed-and-relevance generator ("A serious crime against a noble… …is leaving bodies behind") plus a four-element event generator (circumstance + group + profession + action → interpret freely). "The table gives you bone. You give it meat" (`:601`).

**The settlement-as-character state machine (FL's signature):**
- **Vicissitudes** (`:825-897`): once per month, roll **3D6 + variables** (condition, density, unresolved problems solved/unsolved, authority challenged/firm). Result ladder runs `<3` Anarchy → `>18` Flourishing, each step modifying population, locations, and condition. Unresolved situations *become* problems; solved problems and firm authority push the roll up. **This is the settlement's "healing/damage" track.**
- **Settlement turn** (`:899-924`): the short form — 2D6 + modifiers (problems, shortages, blocked roads, weak/firm authority) → Crisis / Strain / Holding On / Recovery / Growth. "Apply the result in the fiction first" (`:924`).
- **Household ledger** (`:926-931`): name 3–5 households/power-holders; each tracks **Need** (0–3) and **Heat** (0–3). Need rises when unfed/unpaid/unprotected; Heat rises when insulted/cheated/threatened. At Need 3 the household acts from hunger (begs, steals, sells loyalty); at Heat 3 it acts from anger (boycotts, sabotages, feuds, knives). **This is the settlement's internal-faction pressure gauge.**
- **Stores & shortages** (`:933-936`): tracked stores (grain, fuel, salt, water, coin) run Bare→Thin→Adequate→Full; each seasonal turn reduces them one step unless there was a surplus; Bare produces a fitting problem (hunger, theft, poaching, sickness).
- **Route links** (`:938-952`): 1–3 roads out, each Open/Poor/Blocked/Dangerous/Taxed — for pointcrawl-style play.
- **Justice & retaliation** (`:965-976`): a 6-step Heat-escalation procedure — offense → +1 Heat (public +1, severe +1) → at Heat 2 the settlement answers with warning/fine/oath → at Heat 3 with denial of shelter, pursuit, ransom, blood price, outlawry. Repair reduces Heat by 1.

**West — Your Town (`08-campaigns-in-the-old-west.md:67-442`):** the same model, formalized and player-facing.
- **Six Aspects** (`:67-110`): Farming, Mercantile, Natural Riches, Law, Civic, Welfare — each ranked 1–6, advanced by **tally points** (`:73-84`).
- **Prosperity** (`:112-126`): the sum of aspect ranks (6–36), which sets the town's size tier (Trading Post→City) and the modifier on the Town Fortune roll.
- **Amenities** (`:128-442`): the player-driven growth rule pattern — each Turn of the Season the group chooses one amenity to build (a church, gallows, wells, saloons, railroad station…); each modifies aspect tallies, sometimes trading one aspect down to boost another (Gold Rush: Mercantile +2, Law −1). Prerequisites and min-Civic-rank gates create a tech-tree feel. Extra amenities cost **Settlement Points** (5 SP each), earned by community-spirited play (`:146-154`).
- **Failure state** (`:522-535`): if any aspect drops below rank 1, the town fails — no new amenities, all aspects decay one rank per season, people leave. "The town is finished."

**Abstract pattern — "the living settlement":** a settlement is a **character sheet for a place** with: (a) **attributes** that rate its capacity (FL: condition/locations/resources; West: six aspects), (b) a **state machine** that changes it between visits on a dice-plus-variables roll (FL vicissitudes 3D6; West fortune rolls), (c) **internal-faction pressure gauges** (FL Need/Heat; West Competition/Law modifiers), (d) a **resource economy** that degrades and recovers (FL resource dice; West tally points and aspect ranks), and (e) a **growth rule pattern driven by player investment** (FL: the party builds functions/defends the stronghold; West: the party spends SP on amenities). **Layer: General** (the settlement-as-character model); the specific attribute set and growth rule pattern are **core design choices**.

### 5.5 Civic, legal, and reputation procedures

FL's Journey chapter contains a second settlement layer beyond generation: how strangers are received, how public identity changes social odds, how work is found, how authorities are petitioned, how gossip moves, and how crime is judged. West carries the same concerns through Fame/Reputation, property Status, business Standing, town Law, and seasonal fortunes. Abstract this as the **civic procedure layer**: the rules that answer "what does the community do when the PCs enter, ask, offend, bargain, or break the law?"

#### Public identity stack

| Layer | What it answers | Mechanical expression |
| --- | --- | --- |
| Reputation / Fame | Have people heard of you? | modifies reaction, events, job offers, fear, prices |
| Standing | What do locals think of you here? | local cooperation, hospitality, authority access |
| Status / Property | What visible place do you occupy? | social modifier, lifestyle, eligibility |
| Rumor | What story is moving ahead of you? | creates clue, bias, false lead, or public pressure |
| Legal condition | Are you accused, wanted, outlawed, protected, pardoned? | gates shelter, law response, bounty, sanctuary |

**Design rule:** never use one global reputation score for everything. Use at least two layers: broad fame and local standing. Fame opens doors and attracts trouble; Standing decides whether *this* place feeds, hides, hires, or denounces you.

#### Settlement visit menu

Use this as the default civic downtime menu when PCs spend a block in a village, town, station, port, court, monastery, guildhall, starport, school, hospital, or neighborhood.

| Activity | Roll / gate | Success | Failure / complication |
| --- | --- | --- | --- |
| Ask Around | social, insight, lore, scouting | learn rumor, lead, price, person, danger | false lead, offended local, time lost, rumor about PCs |
| Seek Work | social or profession; local demand | job offer, wage, bounty, patron | bad work, trap, insult, debt, rival takes it |
| Petition Authority | Standing, Status, proof, gift | audience, permit, militia aid, judgment, commission | delay, bribe demand, public refusal, rival hearing |
| Trade | availability + price + legality | buy/sell, find specialist, special order | scarcity markup, counterfeit, legal scrutiny |
| Carouse | spend money/time | recover morale/WP/Faith, contact, gossip | debt, fight, scandal, theft, hangover |
| Hire Help | pay + reputation | hireling, guide, guard, artisan | unreliable hire, inflated wage, divided loyalty |
| Heal / Rest | clinic, healer, safe lodging | recover condition, treat injury | infection, bill, rumor, owed favor |
| Train | teacher/access/time | advancement progress | no teacher, bad teacher, institutional gate |
| Make Amends | payment, apology, service | Standing +1 or Heat −1 | rejected, costly demand, public humiliation |

**Menu validation:** at least one activity should convert money into social position, at least one should convert reputation into opportunity, and at least one should create trouble even on a success. Otherwise the settlement is only a shop.

#### Notice board / job table

Use when the GM needs work in a settlement without preplanning.

| D6 | Job family | Typical patron | Hidden pressure |
| --- | --- | --- | --- |
| 1 | Clearing | farmer, reeve, company, temple | threat has a claim or patron |
| 2 | Escort | merchant, pilgrim, prisoner, witness | passenger is wanted or lying |
| 3 | Delivery | guild, doctor, court, smuggler | package is illegal, fragile, or late |
| 4 | Recovery | family, sheriff, scholar, fence | item/person does not want return |
| 5 | Investigation | elder, paper, faction, church | culprit is protected |
| 6 | Labor / Specialist | business, stronghold, mine, ranch | underpaid, dangerous, strike brewing |

Pay can be flat, advance + bounty, share of proceeds, reputation, legal pardon, property right, or future favor. Strong jobs should state both **reward** and **who gets angry if the job succeeds**.

#### Crime and punishment procedure

Use this whenever PCs or important NPCs commit public offenses, are framed, protect criminals, violate taboo, break contract, owe blood price, or are pursued by law.

1. **Name the offense.** Theft, assault, murder, oathbreaking, trespass, poaching, smuggling, fraud, blasphemy, desertion, debt, unlawful magic, harboring, treason.
2. **Set visibility.** Secret, suspected, witnessed, public, confessed, magically/procedurally proven.
3. **Set jurisdiction.** Household, village, guild, sheriff, temple, faction, army, company, crown, occupying force, mob.
4. **Detect or accuse.** Roll scouting/investigation/social if uncertain; otherwise move directly to accusation.
5. **Capture or summon.** Decide whether law asks, fines, seizes property, arrests, posts bounty, sends posse, or attacks.
6. **Judge.** Authority rolls law/social/status vs defense, evidence, Standing, bribe, witness, champion, oath, or trial by ordeal.
7. **Sentence.** Fine, weregild/blood price, restitution, public shame, labor, imprisonment, exile, outlawry, mutilation, execution, feud, forced oath.
8. **Allow repair.** Pay, service, confession, pardon, sanctuary, duel, appeal, restitution, or a dangerous job.
9. **Track aftermath.** Standing, Heat/Wanted, faction relations, witnesses, revenge, precedent.

| Severity | Default consequence | Playable alternative |
| --- | --- | --- |
| Petty | fine, apology, restitution | service, public embarrassment, local debt |
| Serious | large fine, jail, property seizure | dangerous job, sponsor oath, exile from district |
| Blood offense | weregild, feud, outlawry, execution risk | ransom, hostage, duel, sanctuary, faction bargain |
| Political offense | bounty, treason trial, occupation response | pardon mission, propaganda trial, hostage exchange |

**Legal validation:** punishment should create playable pressure unless the campaign explicitly embraces character exit. Outlawry is a campaign mode, not a dead end: it removes ordinary civic protection and turns shelter, work, and travel into adventure problems.

## 6. NPC statblock grammar

**The minimal format (both games):** attributes (4) + relevant skills + talents + gear. The engine deliberately keeps NPC sheets thin because "NPCs run on narrative, not full sheets" (§3) — only roll for NPC actions that attack or heal a PC.

**FL — inline prose statblock** (used inside encounter entries and the village character generator):
```
SLAVERS
- STRENGTH 3, AGILITY 2, WITS 2, EMPATHY 2
- SKILLS: Melee 2
- TALENTS: –
- GEAR: Wooden club or mace, leather armor, D6 copper
```
(`08-encounters.md:137-142`; bandits `:215-220`; Teramalda `:449-456` shows the extended form with special tags like SLOW and INVULNERABLE.) The village generator (`10-villages.md:360-572`) builds these procedurally: profession → skills → experience → reputation → wealth → gear, and notes that generated attributes can reach 8 (two above PC max) for "people worth naming."

**West — 8-column table layout** (`06-life-in-the-old-west.md:1379-1503`): generic archetypes (Bounty Hunter, Card Sharp, Cattle Baron, Doctor, Outlaw, Pinkerton, Sheriff, Tracker, etc.) presented as compact reference rows:
```
BOUNTY HUNTER — GRIT 5, QUICK 4, CUNNING 3, DOCITY 2
PRESENCE 1, MOVE 1, HAWKEYE 2, INSIGHT 1
ANIMAL HANDLIN' 1
Talents: COLD BLOODED, FAST SHOOTER, MANHUNTER.
Gear: Revolver, rifle, length of rope.
```
Each entry has a one-line characterization + 3 suggested talents (Basic rank) + suggested gear. The 8 "columns" are: Name | 4 attributes | skills (grouped) | talents | gear — a glanceable roster, not a full sheet.

**Abstract pattern — "the minimal statblock":** **4 attributes + 1–4 skills (only those that matter) + 0–3 talents + gear (weapon/armor/coin).** Add **special tags** only when the NPC breaks a core rule (SLOW, INVULNERABLE, armor-as-static-rating, etc.). The **choices** are: (1) layout (FL's inline prose for embedded encounters vs. West's table-row roster for a quick-reference bestiary), (2) whether to generate procedurally (FL village generator) or hand-author (West archetypes), (3) the attribute ceiling for "named" NPCs (FL allows 8 vs. PC 6). **Layer: General.**

## 7. Solo-play engine (the GMless layer)

**FL only — full solo suite** (`03-book-of-beasts/04-solo-rules.md`). The engine runs without a GM by replacing each GM function with a procedure or oracle. **Layer: Optional** (omit if the game is GM-led only; include to enable solo/co-op/zero-prep play).

**The structural replacements:**
- **The Companion** (`:19-46`): a support PC with no Willpower (cannot push), who gives help dice rather than acting independently (except when journeying). Drawn from a complementary-profession table; given a **motivation** via card draw (Wanderlust, Fugitive, Vengeance, Greed, Orders…). If the main PC dies, the Companion "upgrades" to main.
- **The Quarter Day Procedure** (`:110-120`): the journey loop, GMless — each quarter day: shuffle deck, earn XP from yesterday's prompts, roll weather, assign/resolve tasks, perform the New Hex Procedure, consult oracles as needed, advance.
- **The New Hex draw** (`:122-134`): draw a playing card — number = random encounter (D66 on the tables); face = general encounter; Ace = random adventure site. This replaces "the GM decides whether something happens."
- **Card oracles** (`:172-316`): a standard deck (Jokers out) replaces the GM's judgement:
  - **Yes/No oracle** (`:178-192`): draw 1 (50/50), 2 take-best (Likely), or 2 take-worst (Unlikely); red = yes, black = no; Face = "…but/and a complication"; Ace = "Exceptional." Rule #1: "go with your gut" — only consult the oracle when genuinely uncertain.
  - **Helpful/Hazardous oracle** (`:194-204`): how hostile an NPC/encounter/settlement is, scaled 2–A from Neutral to Life-saving / Deadly.
  - **Theme oracle** (`:206-224`): a 4-suit × 13-value table of dramatic themes (Balance, Loss, Conflict, Failure…) to interpret ambiguous situations.
  - Plus **Wilderness** (location flavor), **Kin**, **Kin Names**, and **Traits** oracles for on-the-fly generation.

**Abstract pattern — "the GMless layer":** for each GM function (scene framing, NPC behaviour, hidden information, "does something happen," "is this NPC friendly"), substitute a **draw-and-interpret oracle** with a built-in bias choice (Likely/Unlikely draw counts). Add a **turn procedure** that structures time (the quarter-day/shift loop) and a **companion/sidekick** rule so a single PC can survive. The bias choice is what keeps solo play from feeling like coin-flips — "Likely" draws two-take-best, modeling the GM's sense that the fiction leans a certain way. **Layer: Optional.**

## 8. Consequence / fortune / faction tracks (the campaign-state tracker)

This is the engine's rule pattern for making the campaign **remember** — turning one-off choices into accumulating state. Three builds, all variations on **a tracked score that translates choices into forward-thrown consequences.**

**A. The seasonal fortune roll (West — Turn of the Season, `08-campaigns-in-the-old-west.md:537-839`):** at each season turn, three rolls resolve off-screen time:
- **Season Business Roll** (`:555-644`): the proprietor rolls their key ability + helpers (+3 max) + competition modifier (−2 to +2) + town's Law aspect + business-relevant aspect. 0 successes = business loses money (roll on the Business Penalty table); 1 = steady; 2+ = bonus (roll on the Business Bonus table, +1 to tens die per extra success). **Cannot be pushed; no Trouble** — this is a resolution roll, not a dramatic one.
- **Personal Fortune Roll** (`:706-766`): each PC rolls D66 (modified by the town's Welfare aspect) on a table of 50+ personal events — deaths, scandals, legacies, romance, new enemies, windfalls. "Jackpot" (66) and "Calamity" (11) always count regardless of modifier. This is the engine generating character-driven adventure hooks *for the GM.*
- **Town Fortune Roll** (`:768-839`): D66 (modified by Prosperity) producing town-scale events (disease, wildfires, cattle drives, boom times) that modify aspects and generate the next season's pressure.

The genius: **the settlement's attributes (§5) feed back into the fortune rolls**, so a well-developed town makes its residents richer and safer, and a neglected one makes them poorer and endangered. Player investment in the town is rewarded by the rules across seasons.

**B. The faction-standing ledger (West — Quiet Title, `03-adventures/01-quiet-title.md:211-226`):** track the party's standing with four groups on a 0+ scale — `Comunidad Trust`, `Company Pressure`, `Gold Camp Standing`, `Mountain Trust`. Each major choice moves one or more tracks ±1. Each track **throws visible consequences forward** at thresholds: high Comunidad Trust opens doors and hides witnesses; low Comunidad Trust closes the plaza and turns the acequia away. `Company Pressure` runs inverse — *high* pressure means the Company has leverage (blackmail, a warrant) over the party. This makes faction relations *rules-facing*, not just flavor.

**C. The week-ticked faction clock (West — Quiet Title, `:304-321`):** a table where each row is a week and each column is a faction; the entry in each cell is what that faction *does* that week if the party hasn't slowed the clock. Five clocks (Company, Gold Camp, Plaza, Mountain, Witness) tick simultaneously; when two fire the same week, "that is a real session." The party's choices **slow or speed** each clock (`:323-343`): burn a survey wagon to slow Company Pressure; frighten the witness to speed his flight. The hearing at week 12 is the convergence point. **This is the engine's "the world advances on its own terms" doctrine made operational.**

**D. FL's parallel tracks:**
- **Stronghold events** (`02-the-gamemaster.md:137-179`): roll D6s = highest Reputation in the group (min 1); highest die = tens of a D66; separate D6 for units. The Reputation-weighted roll means famous parties draw more (and bigger) events — a direct instance of Principle 5 ("Them That's Got Shall Lose"). The 26-entry table (Nothing → The Orc Chieftain's siege) is the base-under-siege track.
- **Household Need/Heat** (`10-villages.md:926-931`, §5): the internal-faction feud track — Heat 3 produces boycott/sabotage/feud/knives.
- **Justice & retaliation** (`:965-976`): a 6-step escalation procedure that is, in effect, a Heat track the party can raise and pay down.
- **Vicissitudes variables** (`:845-857`): each unresolved problem −1, each solved problem +1, agitator −1, firm authority +1 — the settlement's state is itself a track of the party's stewardship.

**Abstract pattern — "the campaign-state tracker":** a small number of **named scores** (faction standing, settlement aspects, household Heat, a faction clock) that (1) **move on player choices**, (2) **throw consequences forward at thresholds**, and (3) **feed back into the resolution economy** (settlement aspects modify fortune rolls; Reputation weights the event roll; faction standing gates NPC cooperation). The **choices** are: (a) granularity (West's 6 aspects × 6 ranks vs. FL's condition/locations), (b) who rolls (West's player-facing fortune rolls vs. FL's GM-rolled event tables), (c) the clock model (West's simultaneous week-tick vs. FL's monthly vicissitudes), (d) whether tracks are player-visible (West Your Town) or GM-hidden (FL stronghold events). **Layer: General** for "the campaign tracks something"; the specific model is a **core design choice**.

## 9. Adventure-site structure

**FL — the site-as-dungeon (`09-adventure-sites.md:9-39`):** three categories (Village, Dungeon, Castle), each built from random tables. The defining doctrine (`:15-17`): "An adventure site is not a scenario in the traditional sense. It has locations, NPCs and events — but it does not provide a pre-determined narrative. Instead, [players] can interact with it in many different ways, even turning it into their own stronghold." Key features: a **legend** (rumor/handout) attached to each pre-written site, discoverable by LORE roll or in-fiction hearing (`:19-21`); the **turn** (~15 min, one small room) as the exploration time unit (`:23-25`). Site creation can be done in prep or on the fly.

**West — the sandbox adventure (`03-adventures/01-quiet-title.md`):** a site/region presented as "a working country, arranged so the GM always has a live scene ready no matter where the party turns" (`:291-301`). Three rules: (1) the obvious route (the field book) is clearest, not only — list multiple roads through; (2) **factions keep their own time** (the clocks in §8C); (3) **let the party feel the weight of its own competence** — reward shortcuts with the next true trouble they create, never with a reset (`:296-301`, `:463+`).

**Abstract pattern — "the site-as-dungeon":** a location built from **locations + NPCs + events + a legend**, with **no preset narrative** — the party's approach determines the shape of play. The **turn** is the exploration clock. Cross-ref the `adventure-writing` sibling skill for prose/craft; here we capture only the *structural* pattern. **Layer: General.**

## 10. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Principles** | 7 explicit, GM-facing axioms (`02-the-gamemaster.md:25-67`) | Diffuse campaign-driver list (Ambitions, Vengeance, Justice… `08:13-51`) | Codified judgement vs. inspirational themes | FL-style when the GM wants a checklist; West-style for a looser, theme-driven table |
| **Encounter table** | 44-entry D66 matrix, 9 terrain columns, situational entries (`08-encounters.md`) | Campaign seeds + adventure-embedded encounters; no master terrain matrix | Dense random-but-weighted engine vs. authored scenario encounters | FL-style for hex-sandbox; West-style for narrative/region campaign |
| **Settlement model** | Village generator: history → present → locations → characters; **vicissitudes** 3D6+vars; **Need/Heat** ledger (`10-villages.md`) | **Your Town**: 6 Aspects (Farming/Mercantile/Natural Riches/Law/Civic/Welfare) + Prosperity; player-chosen amenities (`08:67-442`) | GM-side simulationist vs. player-facing advancement tree | FL for GM-authored living places; West for party-owned growing towns |
| **Civic/legal layer** | Reputation, Standing, hospitality, notice boards, petitioning, crime, weregild, outlawry, sanctuary | Fame/Reputation, property Status, town Law, business/community Standing | granular communal law vs broader frontier reputation | Include whenever settlements do more than sell gear |
| **Settlement state roll** | Vicissitudes 3D6 + variables (monthly) or settlement turn 2D6 (short form) | Turn of the Season: Business + Personal Fortune + Town Fortune D66 rolls (seasonal) | Gritty attrition sim vs. story-hook generator | FL for survival/decline pressure; West for character-driven hooks |
| **NPC statblock** | Inline prose (4 attr + skills + talents + gear), procedurally generatable, attr ceiling 8 | 8-column table roster, hand-authored archetypes, fixed values | Embedded-in-encounter vs. quick-reference bestiary | FL for encounters-as-stories; West for a glanceable cast |
| **Solo-play layer** | Full suite: companions, quarter-day procedure, card oracles (`04-solo-rules.md`) | Not present in core | GMless-capable vs. GM-required | Include for solo/co-op/zero-prep; omit for traditional GM-led |
| **Campaign-state tracker** | Stronghold events (Reputation-weighted D66) + household Need/Heat + vicissitude variables | Faction Standing (4-track ledger) + week-ticked Faction Clocks + Aspect/Prosperity fortune modifiers | Base-under-siege + internal feuds vs. faction-relations + region-clock | FL for base-defense/decline; West for multi-faction political sandboxes |
| **Adventure-site doctrine** | Site-as-dungeon: locations+NPCs+events, no narrative, 15-min turn, legend handouts | Sandbox country: multiple roads through, factions on their own clocks, shortcut-positive | Hexcrawl-site vs. region-sandbox | FL for pointcrawled sites; West for open political country |
| **Failure / forward motion** | Fail-forward (GM judgement) + reoccurring-encounter memory | Sandbox "country answers back" + faction clocks | GM-adjudicated vs. clock-driven | FL when GM wants authority over pace; West when the table wants the world self-driving |

## 11. Rule Choices and Build Recipe

Each choice has FL and West as two calibrated points.

1. **Principles** — codify 5–7 GM axioms (scarcity, cost-of-safety, death-as-story, emergent-finale, say-yes-to-player-agenda). *(Sets the table's operating tone.)*
2. **Encounter engine** — D66 selector + N context columns + no-encounter floor + situational-entry density + reoccurring rule (continue/change/re-roll, with optional escalation track). *(How random the world feels.)*
3. **Settlement model** — attribute set (FL condition/locations vs. West 6 aspects), state-machine roll (vicissitudes 3D6 vs. fortune D66), internal-faction gauge (Need/Heat vs. Competition/Law), growth rule pattern (stronghold functions vs. amenity SP), failure state (location collapse vs. aspect-to-zero town failure). *(How the home place lives and dies.)*
4. **NPC statblock** — layout (inline prose vs. table row), generation (procedural vs. archetype), attribute ceiling for named NPCs. *(Prep speed vs. bestiary reference value.)*
5. **Solo-play layer** — include/exclude; if included, define the turn procedure, companion rule, and oracle set (yes/no, hostile, theme). *(GMless capability.)*
6. **Campaign-state tracker** — granularity, roller (GM-hidden vs. player-facing), clock model (simultaneous tick vs. monthly), visibility (hidden vs. tracked on sheet). *(How strongly the campaign remembers.)*
7. **Adventure-site doctrine** — site-as-dungeon (locations+NPCs+events, no narrative, turn clock) vs. region-sandbox (multiple roads, faction clocks, shortcut-positive). *(Structure of a playable place.)*

**Instantiation recipe (any genre):**
1. **Write 5–7 GM principles** (choice 1) — scarcity, cost-of-safety, death-as-story at minimum. These are the judgement rules where the dice are silent; without them the procedures below become rote.
2. **Build the encounter engine** (choice 2): decide the selector (D66 or D6/D20), the context columns (terrain/district/faction/season), the no-encounter floor, and write 12–44 situational entries (not pure statblocks). Add the reoccurring rule.
3. **Pick the settlement model** (choice 3) and decide whether it's GM-authored (FL) or player-owned (West). Define its attribute set, its state-machine roll, its internal-faction gauge, and its failure state.
4. **Add the civic/legal layer** if settlements are more than shops: public identity stack, visit menu, notice-board jobs, and crime procedure.
5. **Standardize the NPC statblock** (choice 4) — 4 attributes + relevant skills + 0–3 talents + gear + special tags.
6. **Decide on the campaign-state tracker** (choice 6) — at minimum, one faction-standing or base-event track that throws consequences forward. Add more as the genre demands (political games want multiple faction tracks; survival games want a base-under-siege track).
7. **Decide on solo-play** (choice 5) — include the oracle layer if solo/co-op/zero-prep is a goal.
8. **Write one adventure site/region** (choice 7) in the chosen doctrine to validate the whole — locations+NPCs+events+legend, testable without a preset plot.

## 12. Design intent

The GM-procedures layer exists to make the engine **runnable with minimal prep and honest at the table.** Specifically:

- **The principles are the load-bearing structure.** The dice and tables handle *resolution*; the principles handle *judgement* — every moment the rules are silent, the GM falls back on "nothing is for free," "death is part of the story," "the end is never set." Without these, the procedures below collapse into rote simulation. This is why FL foregrounds them as Chapter 2's first section.
- **The encounter engine makes the world feel alive without scripted plot.** The terrain-keyed D66 matrix + the reoccurring rule turn a flat random table into a *growing, weighted cast* — the party meets the same demon baker twice and the second time he has an army. This is how a sandbox delivers story *without* a pre-written arc.
- **The settlement-as-character model makes the home place matter.** By giving the settlement attributes, a state machine, internal-faction pressure, and a growth rule pattern tied to player investment, both games make "where you live" a participating character in the campaign — one that can prosper, decline, feud, and fail. This is the engine's strongest transferable procedure.
- **The campaign-state trackers make the campaign remember.** Faction standing, household Heat, aspect ranks, and faction clocks convert one-off choices into accumulating state that *throws consequences forward.* A party that sides with the plaza in week 2 is still living with that choice in week 12. This is what separates a sandbox from a sequence of unconnected episodes.
- **The minimal statblock and the "NPCs run on narrative" rule keep prep under 30 minutes.** FL is explicit (`02-the-gamemaster.md:97`): "15–30 minutes of preparation is plenty most of the time. Trust the players and the game itself to create action and drama." The procedures exist so the GM can *play* the engine, not *prepare* it forever.
- **The principles and the settlement model are the most transferable deliverables.** A new genre can swap the encounter table, the statblock nouns, and the tracker names, but the seven axioms (de-flavored) and the settlement-as-character architecture port directly — they are the engine's GM-facing spine.
