<!-- markdownlint-disable MD013 -->

# 25 — Season, Downtime, and Enterprise Management

> **STATUS: CORE DESIGN TOOL.** A period-based downtime engine for businesses, factions, families, settlements, companies, and other managed entities in YZE games. Use this when downtime must run on weeks, months, seasons, years, or generations instead of only Quarter-Day / Shift activities.

## Contents

1. Source provenance and abstraction target
2. The core thesis
3. Time scales: week, month, season, year, generation
4. The Period Turn
5. The Investment Cycle
6. Enterprise sheets
7. Core Enterprise Roll
8. Activity menus
9. Bonus, penalty, and event tables
10. Enterprise archetypes
11. Family and household management
12. Faction and organization management
13. Settlement and community management
14. Winter, contraction, and hard seasons
15. Dials
16. Integration rules
17. Validation and failure modes
18. Publication templates
19. Design recipe

## 1. Source Provenance and Abstraction Target

**Primary calibration source:** Tales of the Old West 2E design material in `/mnt/c/git-public/Tales-of-the-Old-West-2e/docs/`.

- `docs/design-bible.md` — Turn of the Season; Season Business Roll; Season Congregation Roll; Personal and Town Fortune; the Investment Cycle: **Assess -> Invest -> Operate -> Reckon -> Reinvest**; the warning that each trade chapter must embody the cycle rather than merely point to it.
- `04-trials-of-the-old-west/proposals/part-ii-hearth-and-trade.md` — trade-specific enterprise procedures: saloons as crossroads, trade route ledgers, herd ledgers, mining shift menus, logging drives, traplines, market hunting, and banks as reserve-track institutions.
- `13-factions-and-standing.md` — faction Standing (-3 to +3), faction bonds, directional debts, no-cascade propagation, and once-per-season relationship events.
- `14-families-and-feuds.md` — families as long-form social entities, feud clocks, debt axes, seasonal feud moves, and rites as structured quarrels.
- `09-banking-and-the-vault.md` — bank Reserve gauge, lending postures, reserve shocks, and bank runs.
- `22-winter-and-wintering.md` — winter as a contraction turn layered over the seasonal engine: count stores, roll what winter brought, apply attrition, resolve spring thaw.

**Corebook calibration anchors:**

- `/mnt/c/git-public/Tales-of-the-Old-West-2e/01-corebook/06-life-in-the-old-west.md:15-57` — cash, Capital, liquidation, loans, collateral, seasonal interest, foreclosure.
- `/mnt/c/git-public/Tales-of-the-Old-West-2e/01-corebook/06-life-in-the-old-west.md:133-210` — outfits as season-scale businesses: proprietor, employees, investors, Capital pool, wages, Business Bonuses, losses, going bust.
- `/mnt/c/git-public/Tales-of-the-Old-West-2e/01-corebook/06-life-in-the-old-west.md:230-307` — property Status, buy/build cost, land location, property features, business-roll bonuses, seasonal feature income.
- `/mnt/c/git-public/Tales-of-the-Old-West-2e/01-corebook/08-campaigns-in-the-old-west.md:537-655` — Turn of the Season, Season Business Roll, competition, town aspect modifiers, no push/Trouble, Business Bonus/Penalty D66, covering debts.
- `/mnt/c/git-public/Tales-of-the-Old-West-2e/01-corebook/08-campaigns-in-the-old-west.md:680-705` — lifestyle as a seasonal cash and reputation pressure.
- `01-corebook/09-the-stronghold.md:15-62` — FL stronghold founding, base safety, home WP/rest payoff, attention and upkeep.
- `01-corebook/09-the-stronghold.md:106-179` — FL function construction, staff, duplicate functions, hirelings, residents, housing, food/water, recruitment.
- `01-corebook/09-the-stronghold.md:238-272` — unguarded stronghold and weekly upkeep consequences.

**Existing YZE frame:** `06-travel-and-downtime.md` owns block-scale downtime; `07-base-faction-mass-scale.md` owns the org lifecycle and scale ladder. This file fills the missing core layer between them: **period play**.

**Abstraction target:** Build a generic period engine that can run:

- a shop, saloon, clinic, mine, ranch, caravan, bank, studio, shipyard, workshop, gang, temple, campaign office, resistance cell, mercenary company, research lab, monastery, noble house, family estate, settlement, or guild;
- week/month/season/year turns;
- profit, reputation, production, welfare, risk, debts, feuds, projects, politics, reserves, and generational continuity;
- game-specific variants without becoming a board game detached from adventure.

## 2. The Core Thesis

YZE downtime is strongest when ownership creates **hungry systems**: things the players value, grow, feed, defend, and occasionally lose. A business, family, faction, or settlement should never be a passive bonus generator. It should be a living pressure loop.

The period engine has three principles:

1. **Time creates obligations.** Every period asks: what did this entity owe, who did it disappoint, what wore down, and what came due?
2. **Investment precedes payout.** Players choose risk posture before they know the result. Safety, growth, reputation, reserves, secrecy, and output compete for the same scarce capital.
3. **Every profit becomes a future pressure.** Money attracts debt; fame attracts rivals; growth attracts labor problems; secrecy creates exposure; family survival creates obligations.

The key lesson from the Old West investment cycle is that a season roll is not a flat income roll. The roll is the **reckoning** for choices made earlier. A ranch, a bank, and a saloon can all use the same period skeleton, but each must have a distinct resource, activity menu, risk family, and payout logic.

## 3. Time Scales

Use the shortest scale that still makes the decision meaningful.

| Scale | Use for | Typical procedures | What it should not do |
| --- | --- | --- | --- |
| Week | jobs, treatment, repairs, rumors, legal filings, training, route legs, project ticks | one activity per PC/org role; small event; project progress | resolve an entire institution's fate |
| Month | payroll, production, public mood, market movement, faction posture, family obligations | upkeep, one management move, one local event | replace scene play when PCs are present |
| Season | strategic business, crops, cattle, voyages, politics, long projects, faction relationships | full Investment Cycle; fortune/event roll; expansion or contraction | run every tiny errand |
| Year | legacy, construction, dynastic shifts, reputation eras, resource renewal | yearly audit; inheritance; long-term projects; settlement growth | hide major adventure consequences |
| Generation | family sagas, succession, cultural change, faction memory | inheritance, feud transformation, legacy XP, house/faction continuity | track ordinary cash flow |

**Default:** one season = three months. Four seasons make a year. A campaign can rename them to quarters, patrol cycles, terms, harvests, tours, voyages, market cycles, or campaign phases.

**Period nesting:** weekly actions feed monthly upkeep; monthly results feed seasonal reckoning; seasonal consequences feed yearly legacy. Do not run every scale at full detail. Choose one **active scale** and summarize the rest.

## 4. The Period Turn

The Period Turn is the generic chassis for any week, month, season, or year.

### Looking Back

1. **Close open clocks.** Resolve any project, wound, debt call, feud move, route delay, market order, or faction undertaking whose time has arrived.
2. **Apply upkeep.** Pay wages, food, maintenance, rent, debt interest, bribes, public obligations, or relationship attention.
3. **Apply standing conditions.** Add modifiers from law/order, welfare, prosperity, weather, war, disease, shortage, market glut, faction hostility, or household strain.
4. **Resolve old trouble.** If the last period ended with an unresolved event, address it before new investment.

### Looking Forward

5. **Assess.** Read the current opportunity/risk picture.
6. **Invest.** Commit capital, stores, labor, favors, reputation, secrecy, or time into dials.
7. **Operate.** Choose the period's management moves and resolve activity rolls.
8. **Reckon.** Make the core Enterprise Roll or period check.
9. **Take fortune.** Roll or choose one event, opportunity, or fallout result.
10. **Reinvest.** Take profit, repair harm, pay debt, improve functions, expand scale, or build reserves.
11. **Seed next period.** Record one unresolved obligation or opportunity.

**Design rule:** the turn must leave the table with a new decision. If it ends with only "you gain money," it is unfinished.

## 5. The Investment Cycle

Use this cycle for season-scale businesses, organizations, holdings, and families.

### 1. ASSESS

Players gather information and decide what sort of season this is.

**ASSESS.** Spend one downtime action or assign a manager. Roll WITS + the relevant knowledge/social skill, modified by access. On success, ask one question; each extra success asks one more or grants +1 die to the Invest step. On failure, the GM answers one question truthfully and one misleadingly, or reveals the risk only after investment.

Assess questions:

| Question | Reveals |
| --- | --- |
| Where is demand rising? | best Output/Growth target |
| Who will oppose us? | rival, faction, legal, family, or market pressure |
| What will fail if neglected? | upkeep weak point |
| What resource will be scarce? | supply/cash/labor/social constraint |
| What rumor is moving? | reputation/faction event |
| What is the safe play? | low-risk strategy |
| What is the ambitious play? | high-risk strategy and reward |
| What is hidden in the books? | debt, corruption, theft, or reserve weakness |

### 2. INVEST

Players commit resources before the reckoning roll.

| Investment | Cost | Effect this period | Risk |
| --- | --- | --- | --- |
| Safety | 1 Capital / 1 Reserve / one major favor | ignore first penalty or reduce fallout severity by one step | lower profit ceiling |
| Output | 1 Capital / extra labor / supplies | +1 die to Enterprise Roll | on failure, add exhaustion, depletion, or quality flaw |
| Growth | 2 Capital / construction / recruitment | on 2+ successes, unlock improvement option | on failure, debt or unfinished project |
| Reputation | cash, feast, advertising, patronage, public rite | +1 to public-facing roll or Fortune | scandal table on failure |
| Secrecy | bribe, silence, hidden route, false books | reduce Heat/Exposure by 1 if roll succeeds | if failure, Exposure +2 |
| Reserve | profit withheld | +1 Reserve or equivalent safety gauge | no immediate payout |
| Labor | hire, conscript, family obligation, crew promise | +1 help die, can exceed ordinary help cap by +1 | morale/standing cost if unpaid |
| Quality | better stock, tools, experts, ritual purity | unlocks Bonus table high rows | more expensive upkeep next period |

**Investment timing rule:** pay costs before the roll. That is what makes the cycle feel like management rather than loot distribution.

### 3. OPERATE

The period's fiction happens: scenes, jobs, projects, weather, visits, events, disputes, and ordinary work. For light play, summarize this with one operation move. For campaign-mode play, run one scene per major enterprise.

### 4. RECKON

Make the Enterprise Roll (§7), resource-die check, faction move, family move, or project roll. Read it against the dials chosen in Invest.

### 5. REINVEST

Convert the result into future posture.

| Reinvestment | Cost | Effect |
| --- | --- | --- |
| Take payout | no reinvestment | convert profit to cash/resources now |
| Pay debt | profit or favor | remove Debt, interest, lien, blackmail, or obligation |
| Repair | profit + time | clear one damage, flaw, scandal, injury, or depleted function |
| Build reserve | profit withheld | Reserve +1, Stores +1, or resource die steps up |
| Improve function | 2+ profit / project | add or upgrade one enterprise function |
| Expand scale | 3+ profit + risk | increase reach/size; add new upkeep and event exposure |
| Reward people | profit | morale/standing +1, or prevent labor trouble |
| Buy protection | profit/favor | reduce next period's external threat |
| Lay low | forgo growth | reduce Heat/Exposure/Scandal by 1 |

## 6. Enterprise Sheets

Every managed entity needs a sheet. Keep it compact.

| Field | Meaning |
| --- | --- |
| Name | what the entity is called |
| Type | business, family, faction, settlement, crew, project, estate, route, herd, mine, bank, etc. |
| Scale | household, shop, crew, company, town, faction, region, polity |
| Key Ability | the governing skill/function used for Enterprise Rolls |
| Proprietor / Manager | who rolls and who is accountable |
| Staff / Help | who can add help dice, capped by default at +3 |
| Functions | named capabilities: bar, forge, clinic, vault, route, herd, library, chapel, spy ring |
| Gauges | 2-4 tracked values that define the enterprise's pressure |
| Capital / Reserve | illiquid investment, cash buffer, stores, or equivalent |
| Standing / Reach | public legitimacy and area of influence |
| Upkeep | wages, supplies, fuel, rent, law, feed, kin obligations, tribute |
| Risk Family | the table or fallout type used on failure |
| Bonus Table | what good periods generate |
| Penalty Table | what bad periods cost |
| Current Dials | safety/output/growth/secrecy/etc. choices this period |

### Gauge Examples

| Enterprise | Gauges |
| --- | --- |
| Saloon / social hub | Crossroads, Stock, Law Attention, Reputation |
| Trade route | Route Rating, Cargo, Schedule, Competition |
| Ranch / herd | Herd Die, Quality, Grass/Feed, Rustler Pressure |
| Mine | Vein Die, Depth, Dust, Timber/Safety |
| Bank | Reserve, Trust, Loan Book, Robbery Risk |
| Family | Cohesion, Holdings, Feud, Obligation |
| Faction | Standing, Reach, Debt, Heat |
| Settlement | Prosperity, Welfare, Law, Supply |
| Research lab | Project Clock, Materials, Safety, Patron Patience |

**Gauge rule:** each enterprise should have at least one profit gauge, one risk gauge, and one relationship/public gauge. Otherwise the enterprise becomes either pure accounting or pure drama.

## 7. Core Enterprise Roll

Use this for businesses, holdings, and organizations that need a period reckoning.

**Dice pool:** Key Ability + manager skill + function/tool dice + help dice (max +3) + competition modifier (-2 to +2) + settlement/faction aspect modifier + investment modifier + current condition modifiers.

**Default push rule:** season and month Enterprise Rolls cannot be pushed. They summarize too much time and should not become metacurrency farms. If the host game demands a push equivalent, use **Risky Reckoning**:

**RISKY RECKONING.** Before rolling, take Debt +1, Exposure +1, or Reserve -1 to reroll all non-success dice once. If the reroll still fails, roll twice on the Penalty table and choose the worse result.

### Result Ladder

| Successes | Result |
| --- | --- |
| 0 | Loss. Upkeep is unpaid, a gauge worsens, and roll/choose from the Penalty table. |
| 1 | Steady. Upkeep and wages are paid. No bonus, no growth. |
| 2 | Good period. Upkeep is paid and roll/choose from the Bonus table. |
| 3 | Strong period. As 2 successes, plus one Reinvestment option at -1 cost or +1 Reserve. |
| 4+ | Breakout period. As 3 successes, plus growth, scale increase, major reputation shift, or +1 Tens die modifier to a D66 Bonus roll per success beyond 2. |

### Common Modifiers

| Modifier | Dice |
| --- | --- |
| Strong demand / favorable season | +1 |
| Monopoly / rare expertise | +1 |
| Help from skilled owners, workers, kin, or allies | +1 to +3 |
| Good function or amenity | +1 |
| Investment in Output or Quality | +1 each, if paid |
| Competition | -2 to +2 |
| Bad law / hostile authority / feud pressure | -1 or -2 |
| Shortage / weather / disease / war | -1 or -2 |
| Unpaid upkeep from prior period | -1 |
| Damaged function | -1 until repaired |

**Competence calibration:** an ordinary competent enterprise should have 5-7 dice after modifiers. A desperate or new enterprise should roll 3-4 dice. A well-run, invested enterprise should roll 8-10 dice but should have more to lose.

## 8. Activity Menus

### Weekly / Monthly Management Moves

**WORK THE CORE.** Spend the period doing the enterprise's ordinary work. Roll the Key Ability. On success, gain +1 die to the next Enterprise Roll or clear one minor shortage. On failure, the work gets done but one gauge worsens: Stock -1, Morale -1, Exposure +1, or Debt +1.

**MAINTAIN.** Spend cash, stores, or labor to repair a function, heal staff, settle accounts, or restore a gauge. No roll if the cost is paid. If the resource is scarce, roll WITS + Craft/Management; failure repairs the issue but creates Debt or Delay.

**EXPAND.** Start or advance a new function, route, room, claim, herd, department, family holding, or faction cell. Pay the listed cost and roll the relevant ability. On success, mark progress; each extra success adds progress or reduces cost. On failure, mark progress but add a flaw.

**NEGOTIATE.** Treat with suppliers, creditors, patrons, rivals, workers, kin, regulators, or neighbors. Roll EMPATHY + social skill. On success, choose: improve Standing, reduce Competition, delay Debt, gain Help, or learn an opportunity. On failure, choose one but offend someone.

**PROTECT.** Guard assets, insure risk, hire muscle, strengthen law cover, consecrate boundaries, or hide records. Pay cost and roll the relevant skill. On success, ignore the next theft, raid, scandal, inspection, spoilage, or sabotage result. On failure, the protection is visible and creates a rival move.

**EXPLOIT.** Push people, land, reserves, animals, contacts, or machinery harder than is wise. Gain +2 dice to this period's Enterprise Roll. After Reckon, worsen one gauge and roll a minor fallout even on success.

**LAY LOW.** Reduce ambition to avoid attention. No growth this period. Reduce Heat, Exposure, Scandal, or Feud by 1. If creditors or enemies are active, roll; failure means they interpret quiet as weakness.

**TRAIN STAFF.** Spend time and wages to improve the people behind the enterprise. On success, add one trained helper, raise Morale/Cohesion, or unlock a function prerequisite. On failure, progress is made but the trainee wants a promise, wage, or status.

**GATHER INTEL.** Run the ASSESS move with advantage: success gives two questions instead of one. Failure gives one answer and triggers an event from the rival/authority table.

### Seasonal Strategy Moves

**SAFE SEASON.** Invest in reserves and caution. Enterprise Roll -1 die, but ignore the first Penalty result or reduce its severity. Cannot choose Growth on Reinvest unless 4+ successes.

**BUSY SEASON.** Invest in output. Enterprise Roll +1 die. If the roll fails, add Exhaustion, Quality Flaw, or Staff Trouble.

**GROWING SEASON.** Invest in expansion. Enterprise Roll unchanged. On 2+ successes, choose one extra Reinvestment option that must build or improve a function. On failure, add Debt +1.

**QUIET SEASON.** Reduce Heat, Feud, Exposure, or Scandal by 1 before rolling. Profit cap: treat 4+ successes as 3 successes.

**GAMBLING SEASON.** Take Debt +1 or Reserve -1 for +2 dice. On 0 successes, roll twice on Penalty. On 3+ successes, choose one extra Bonus.

## 9. Bonus, Penalty, and Event Tables

Use these when an enterprise does not have its own table yet. Replace them with trade-specific tables as soon as the enterprise becomes campaign-central.

### Seasonal Bonus D66

| D66 | Result |
| --- | --- |
| 11 | A steady buyer, patron, or ally offers repeat work. Standing +1 with them. |
| 12 | Waste is lower than expected. Reserve +1 or Stores +1. |
| 13 | A worker, kinsperson, or junior partner proves reliable. Add one named helper. |
| 14 | A rival blunders publicly. Competition -1 next period. |
| 15 | Good weather, traffic, or timing raises demand. +1 die next period if you invest in Output. |
| 16 | An old debt is partly forgiven. Debt -1 or interest waived. |
| 21 | The enterprise's quality is noticed. Reputation +1. |
| 22 | A new supplier appears. Ignore one shortage next period. |
| 23 | A customer, client, or dependent becomes a friend. Gain a favor. |
| 24 | A small innovation improves efficiency. Upkeep -1 cost next period. |
| 25 | Staff morale rises. Morale/Cohesion +1. |
| 26 | A hidden reserve is found. Gain cash/stores equal to one minor payout. |
| 31 | A faction wants access. Gain a patron, but record their expectation. |
| 32 | Expansion site opens. Next EXPAND roll gains +1 die. |
| 33 | Local authority praises the work. Law/Legitimacy +1. |
| 34 | Rumor works in your favor. Roll twice on next public-facing Fortune and choose. |
| 35 | A loyal customer brings a problem worth an adventure. If solved, Bonus +1 next season. |
| 36 | The enterprise becomes a meeting place. Add Crossroads/Reach +1. |
| 41 | A windfall arrives with a catch. Take +1 Capital and Debt +1 to someone specific. |
| 42 | A competitor proposes cooperation. Competition -1 if you accept an obligation. |
| 43 | A worker asks for status. Grant it for Morale +1; refuse for Debt/Resentment +1. |
| 44 | A risky market opens. Next Gambling Season gains +1 die and +1 Penalty severity. |
| 45 | A public celebration is possible. Pay cost for Reputation +1 and Welfare/Cohesion +1. |
| 46 | Someone offers protection. Gain Safety next period; owe a favor. |
| 51 | A major client wants exclusivity. Profit +1 now; Competition +1 later. |
| 52 | The enterprise attracts talent. Hire a specialist if you can pay their upkeep. |
| 53 | A relative, dependent, or ally asks to be included. Add help but also obligation. |
| 54 | Your name travels. Reach +1; Heat/Exposure +1 if your work is illegal or controversial. |
| 55 | A function overperforms. Choose one function; it grants +1 die next period. |
| 56 | A feud cools through shared interest. Feud -1 if you make a concession. |
| 61 | Breakthrough. Add a new function at half cost. |
| 62 | Boom. Gain +2 Capital or equivalent, but mark Growth Pressure. |
| 63 | Public trust. Reserve +1 and Standing +1. |
| 64 | Legacy moment. Record a deed; it can justify advancement, inheritance, or renown. |
| 65 | Transformation. Increase Scale or change Type, adding one new upkeep obligation. |
| 66 | Legendary season. Choose two: +2 Capital, +2 Standing, new function, Debt -2, or major patron. Also create a powerful rival or expectation. |

### Seasonal Penalty D66

| D66 | Result |
| --- | --- |
| 11 | Spoilage, waste, or theft. Stores -1 or Reserve -1. |
| 12 | Tools, rooms, records, or assets are damaged. One function is Damaged. |
| 13 | Wages strain the books. Pay now or Morale/Cohesion -1. |
| 14 | A debtor delays payment. Debt +1 or cash shortfall. |
| 15 | Bad weather, sickness, or supply trouble. -1 die next period unless addressed. |
| 16 | A small scandal. Reputation -1 unless you pay or apologize. |
| 21 | Staff conflict. Choose a side or lose a helper. |
| 22 | A family obligation interrupts work. Pay time/cash or Family Strain +1. |
| 23 | A supplier fails. Stock/Stores -1. |
| 24 | Quality drops. Next Bonus roll is capped at 46 unless you MAINTAIN. |
| 25 | Exhaustion. Help cap reduced by 1 next period. |
| 26 | Hidden flaw. Add a tag to one function: leaky, corrupt, haunted, unsafe, unreliable, disputed. |
| 31 | Rival undercuts you. Competition worsens by 1. |
| 32 | Authority inspects, taxes, audits, or watches. Law Attention/Exposure +1. |
| 33 | A creditor calls. Pay, renegotiate, or Debt consequence escalates. |
| 34 | Theft, raid, sabotage, or robbery. Lose Reserve/Stores or run a scene. |
| 35 | Public blame. Standing -1 with one group. |
| 36 | A dangerous opportunity tempts staff or kin. If ignored, Morale -1; if pursued, run a risky scene. |
| 41 | Fire, flood, collapse, stampede, crash, panic, riot, or outbreak. Damage one function and injure someone. |
| 42 | Legal trouble. Pay fine/bribe or mark Case/Investigation clock 1. |
| 43 | Faction pressure. A faction demands access, tax, silence, or service. |
| 44 | Internal corruption. Someone skims, lies, or betrays. Find them or Reserve -1 each period. |
| 45 | Market turns. The current strategy suffers -1 die until reassessed. |
| 46 | A dependent suffers. Welfare/Cohesion -1 unless helped. |
| 51 | Debt spiral. Debt +2 or lose a function as collateral. |
| 52 | Walkout, desertion, or family split. Lose help until repaired. |
| 53 | Feud move. Advance a feud, rivalry, or legal fight by 1. |
| 54 | Reputation stain. Public rolls suffer -1 until you make restitution. |
| 55 | Reserve shock. Reserve -2; if Reserve hits 0, collapse/bust/run begins. |
| 56 | Accident with consequences. Critical injury, death, lawsuit, or haunting memory. |
| 61 | Function lost. One function is destroyed, seized, burned, foreclosed, or abandoned. |
| 62 | Patron turns. A major ally withdraws support and demands repayment. |
| 63 | Public crisis. Riot, panic, run, scandal, strike, or mob pressure. |
| 64 | Enemy opportunity. A rival gains a new function, ally, or legal claim. |
| 65 | Collapse threat. Mark Bust/Breakup/Mutiny/Succession clock 2. If already marked, trigger it. |
| 66 | Ruinous season. Choose: enterprise closes, family splits, faction schisms, settlement aspect drops to 0, or major adventure is required to avert collapse. |

## 10. Enterprise Archetypes

Each archetype uses the same cycle but must have a distinct operating identity.

### Social Hub: saloon, inn, court, club, church hall, network node

- **Key gauge:** Crossroads (0-5), how many different worlds meet here.
- **Core decision:** profit vs reputation vs risk of trouble.
- **Special move:** **HOST A NIGHT.** Roll EMPATHY + social skill. On success, choose: gain rumor, gain cash, improve Standing, reduce Feud, or introduce two factions. On failure, choose one and roll a scandal/trouble event.
- **Penalty family:** brawl, scandal, law attention, unpaid tab, faction offense, staff harm.

### Route Enterprise: caravan, freight line, smuggling route, courier web, star lane

- **Key gauge:** Route Rating (D6-D12 or 1-5).
- **Core decision:** safe cargo vs profitable cargo.
- **Special move:** **MAKE THE CARGO BET.** Choose Safe, Risky, or Desperate cargo before departure. Safe: -1 profit, +1 safety. Risky: normal. Desperate: +2 profit dice, but any failure triggers route threat.
- **Penalty family:** delay, spoilage, ambush, seizure, crew fatigue, market miss.

### Herd / Stock / Fleet: ranch, stable, fishing fleet, drone swarm, mecha hangar

- **Key gauge:** Herd/Fleet Die (D6-D12) plus Quality (1-3).
- **Core decision:** breed/maintain vs sell/use hard.
- **Special move:** **CULL OR BREED.** Cull for immediate payout and step die down; Breed/Refit for no payout and a roll to step die up.
- **Penalty family:** disease, rustlers, feed shortage, quality decline, accident, predator.

### Extraction: mine, logging camp, quarry, salvage yard, data harvest

- **Key gauge:** Vein/Stand/Source Die plus Depth/Depletion.
- **Core decision:** output vs safety vs exhaustion of source.
- **Special move:** **PUSH THE SOURCE.** Gain +2 dice this period. On any failure or Trouble, increase Dust/Depletion/Danger and damage a function.
- **Penalty family:** collapse, strike, sickness, claim jump, resource depletion, pollution/curse.

### Financial Institution: bank, credit union, loan shark, treasury, patron house

- **Key gauge:** Reserve (1-5).
- **Reserve meanings:** 1 Overextended, 2 Stretched, 3 Sound, 4 Conservative, 5 Hoarding.
- **Special move:** **SET LENDING POSTURE.** Aggressive: Reserve -1, profit doubled, Penalty severity +1. Normal: no change. Tighten: Reserve +1, profit halved, public frustration +1.
- **Penalty family:** run, robbery, bad loan, panic, authority audit, debtor violence.

### Household / Family / Dynasty

- **Key gauge:** Cohesion, Holdings, Obligation, Feud.
- **Core decision:** protect kin vs pursue ambition vs settle obligations.
- **Special move:** **CALL THE HOUSE.** Gather kin and dependents. Roll EMPATHY + social skill. On success, gain help, settle Debt, or reduce Feud. On failure, get help but create a quarrel.
- **Penalty family:** inheritance dispute, marriage pressure, feud, shame, illness, debt call.

### Faction / Organization

- **Key gauge:** Standing, Reach, Debt, Heat.
- **Core decision:** act openly vs act through agents vs preserve legitimacy.
- **Special move:** **MAKE A FACTION MOVE.** Choose Pressure, Bargain, Protect, Recruit, Expand, Spy, or Settle Debt. Roll the relevant faction ability. On success, change one edge or clock. On failure, create exposure or backlash.
- **Penalty family:** rival move, debt call, schism, scandal, crackdown, betrayal.

## 11. Family and Household Management

Families are enterprises whose profit is continuity.

### Family Sheet

| Field | Meaning |
| --- | --- |
| Name / Line | the family identity |
| Elders / Heirs | who can decide and inherit |
| Holdings | land, business, office, tools, herds, title, claim |
| Cohesion | 0-5; trust and willingness to sacrifice |
| Obligation | 0-5; promises, dowries, care, debts, oaths |
| Feud | 0-6/10/12 clock; active long conflict |
| Standing | -3 to +3 with other families/factions |
| Secrets | blackmail, shame, hidden inheritance, forbidden relationship |

### Seasonal Family Procedure

1. Apply household upkeep: food, rent, care, taxes, rites, promises.
2. Resolve one obligation due this season.
3. Choose one Family Move.
4. If Feud > 0, choose or roll one Feud Move.
5. Roll Family Fortune if the family is campaign-central.
6. Reinvest: repair Cohesion, improve Holdings, settle Debt, arrange alliance, train heir, or lay groundwork for succession.

### Family Move Menu

**KEEP THE HOUSE.** Pay upkeep and roll WITS + management/craft. On success, Cohesion +1 or Holdings protected. On failure, upkeep is paid but Obligation +1.

**MAKE A MATCH.** Arrange marriage, adoption, partnership, apprenticeship, or patronage. Roll EMPATHY + social skill. On success, create an alliance edge or reduce Debt. On failure, create a quarrel or unwanted promise.

**SETTLE A QUARREL.** Name two sides and what each wants. Roll EMPATHY + Insight/Manipulation. On success, reduce Feud, Obligation, or Strain by 1. On failure, the quarrel becomes public or personal.

**CALL IN KIN.** Gain help dice up to +3 for one project/scene. Afterward, either pay them, promise them, or reduce Cohesion by 1.

**DEFEND THE NAME.** Respond to insult, scandal, lawsuit, or accusation. Roll the appropriate social/legal/combat skill. On success, Standing +1 or scandal cleared. On failure, Feud +1.

**DIVIDE THE INHERITANCE.** When an elder dies or a holding changes hands, roll WITS or EMPATHY + relevant skill. On success, choose heir and avoid split. On failure, split a holding, create Debt, or start a feud clock.

### Feud Move Menu

**RAID.** Strike property, stock, records, or reputation. Roll force or stealth. On success, damage a holding and advance Feud. On failure, suffer retaliation or public blame.

**LAWSUIT.** Move the feud into official channels. Roll social/legal. On success, freeze a holding, debt, or action. On failure, lose Standing with authority.

**SLANDER.** Attack public trust. Roll social. On success, target Standing -1. On failure, your own Reputation suffers.

**MEDIATION.** Bring a respected third party. Roll EMPATHY + social. On success, Feud -1 and Debt is named. On failure, both sides harden.

**RETALIATION.** Answer a recent harm. Gain +1 die if the harm was public. On success, restore face. On failure, Feud advances twice.

**TRUCE.** Offer terms. Pay concession; roll. On success, freeze Feud for one season. On failure, the concession is taken and the feud continues.

## 12. Faction and Organization Management

Use this when an organization matters relationally but does not need the full FL faction-turn machinery.

### Light Faction Sheet

| Field | Meaning |
| --- | --- |
| Purpose | what the faction wants |
| Means | what it can do |
| Reach | neighborhood / town / region / realm / sector |
| Standing with PCs | -3 enemy to +3 sworn ally |
| Bonds | edges to other factions, -3 to +3 |
| Debts | directional promises owed |
| Heat | public/authority pressure |
| Current Move | what it will do this period |

### Seasonal Faction Procedure

1. For each campaign-central faction, choose one Move.
2. Resolve only moves that touch PCs, shared assets, or active fronts.
3. If PC Standing with a faction changed by 2+ this season, propagate once through strong Bonds: allied factions shift +1, enemy factions shift -1. Do not cascade.
4. Each season, call at most one Debt per faction. The target may Pay, Refuse, or Renegotiate.
5. Roll one Relationship Event for the whole web, not one per faction.

### Faction Move Menu

**PRESSURE.** Threaten, tax, expose, blockade, sue, raid, or intimidate. On success, target loses resource or gains Heat. On failure, the faction loses Standing.

**BARGAIN.** Offer aid with terms. On success, create directional Debt. On failure, the offer offends or reveals weakness.

**PROTECT.** Guard a place, person, right, secret, or route. On success, reduce Heat/Feud/Threat. On failure, the protection costs more than expected.

**RECRUIT.** Grow membership, labor, troops, voters, believers, or informants. On success, Reach or Help improves. On failure, infiltrators, zealots, or opportunists enter.

**EXPAND.** Claim turf, market, office, settlement, route, or institution. On success, Reach +1 or new function. On failure, rival gets a free move.

**SPY.** Learn secret, weakness, route, account, or plan. On success, ask two questions. On failure, Heat +1 or false information.

**SETTLE DEBT.** Pay, forgive, transfer, or call a Debt. On success, Debt changes as intended. On failure, Debt becomes public or personal.

## 13. Settlement and Community Management

A settlement is an enterprise whose output is livability.

### Settlement Sheet

Use 4-6 aspects. West-style calibration often uses Farming, Mercantile, Natural Riches, Law, Civic, Welfare, Prosperity. Generic games can rename them:

| Aspect | Generic meaning |
| --- | --- |
| Supply | food, water, energy, logistics |
| Trade | market, craft, wealth, exchange |
| Safety | law, defense, order, trust |
| Care | health, welfare, education, mutual aid |
| Spirit | faith, culture, identity, morale |
| Reach | roads, politics, communication, allies |

### Community Season Procedure

1. Apply amenity/function modifiers.
2. Resolve enterprise/faction/family rolls that depend on the settlement.
3. Choose one new amenity, improvement, policy, or public project.
4. Pay lifestyle/upkeep if the game tracks it.
5. Roll personal/community Fortune with modifiers from Welfare/Prosperity or equivalent.
6. Apply a public event and seed next season's pressure.

### Community Moves

**BUILD AMENITY.** Pay cost and assign labor. On success, add a function or aspect modifier. On failure, project is half-built and creates Debt/Scandal.

**HOLD COUNCIL.** Let factions, families, guilds, or crews contest a public decision. Roll social. On success, choose policy and reduce Feud/Heat. On failure, choose policy but offend a group.

**RAISE RELIEF.** Spend stores/cash/favors to improve Care/Welfare or prevent collapse. On success, clear hardship. On failure, help reaches some and not others; create resentment.

**ENFORCE ORDER.** Use law, guards, custom, militia, or public shame. On success, Safety +1 or Heat -1. On failure, authority overreaches.

**OPEN MARKET.** Invite trade, festival, caravan, fair, pilgrims, investors, or smugglers. On success, Trade/Prosperity +1. On failure, Heat, disease, crime, or scandal enters.

## 14. Winter, Contraction, and Hard Seasons

Not every season should offer growth. Winter, war, plague, drought, siege, recession, famine, monsoon, or occupation can replace normal business with contraction play.

### Hard Season Procedure

1. **Count stores:** food, fuel, feed, medicine, ammunition, cash, social goodwill, repair parts, or spiritual strength.
2. **Name what the season brought:** roll or choose from the Hard Season table.
3. **Apply attrition:** reduce stores, gauges, morale, animals, staff, functions, or health.
4. **Choose survival moves:** ration, shelter, borrow, raid, migrate, sacrifice, consolidate, pray, hide, negotiate.
5. **Resolve thaw/reset:** what survived, what was lost, what changed permanently, and what opportunity appears.

### Hard Season D12

| D12 | Result |
| --- | --- |
| 1 | Deep isolation: travel and trade are blocked. |
| 2 | Long cold / hard scarcity: stores deplete twice. |
| 3 | Illness: Care/Medicine becomes the key gauge. |
| 4 | Predators or raiders: protection is tested. |
| 5 | Cabin fever: Cohesion/Morale suffers. |
| 6 | Fuel/feed failure: choose people, animals, machines, or comfort. |
| 7 | A stranger arrives with need and danger. |
| 8 | A debt comes due when payment is hardest. |
| 9 | A rival suffers and can be helped or exploited. |
| 10 | Hidden rot: one function shows a flaw. |
| 11 | Early thaw / relief: a chance to move first. |
| 12 | The season did not end: repeat one attrition, then grant a hard-won boon. |

**Design rule:** contraction must be playable. The point is not to punish ownership; it is to reveal what the players will sacrifice to preserve it.

## 15. Dials

| Dial | Low | Standard | High |
| --- | --- | --- | --- |
| Active scale | season only | month + season | week + month + season |
| Enterprise count | one shared entity | 2-4 central entities | full web of entities |
| Roll cadence | only at season end | monthly activity + season roll | weekly moves + season roll |
| Profit detail | abstract bonus | cash/capital/reserve | ledgers, debt, function costs |
| Risk severity | delay/cost | damaged function/debt | collapse, foreclosure, schism |
| Public web | Standing only | Standing + Debt | Standing + Debt + Bonds + propagation |
| Family depth | obligation tags | Cohesion/Obligation/Feud | inheritance, rites, generations |
| Faction depth | light moves | seasonal web | full faction turn |
| Winter/hard season | event only | contraction procedure | replaces ordinary season |
| Pushing | no push | Risky Reckoning optional | push allowed with severe debt/exposure |

**Recommended defaults:** one active scale, one shared enterprise, 2-3 gauges, one season roll, one event table, one reinvest choice. Add more only when management is the campaign premise.

### 15.1 Calibrated Downtime Profiles

Use these profiles to avoid vague "downtime exists" designs. Each one chooses an active scale, roll cadence, investment posture, and consequence family.

| Profile | Active scale | Core entity | Required gauges | Roll cadence | Default investment menu | Failure family |
| --- | --- | --- | --- | --- | --- | --- |
| Survival base | week + season | stronghold, camp, haven, ship | Stores, Shelter, Watch, Morale | weekly upkeep; seasonal event | Maintain, Protect, Store, Repair, Recruit | spoilage, unguarded event, unpaid workers, damaged function |
| Frontier business | season | outfit, shop, ranch, mine, saloon | Capital, Competition, Standing, Debt | one Season Business Roll | Output, Quality, Labor, Reputation, Reserve | debts, employee trouble, reputation loss, competition shift |
| Family/household | season + year | family, household, dynasty | Cohesion, Obligation, Holdings, Feud | one seasonal household move; yearly inheritance | Duty, Marriage/Alliance, Estate, Education, Reconciliation | feud escalation, compadre/family crisis, contested property |
| Faction/political | season | faction, party, guild, clan | Standing, Reach, Debt, Heat | one faction move per central faction | Patronage, Pressure, Secrecy, Recruitment, Public Works | betrayal, backlash, debt call, enemy move |
| Criminal/outlaw | month + season | gang, crew, cell | Heat, Provisions, Loyalty, Stash | monthly job/fallout; seasonal upkeep | Lay Low, Score, Bribe, Muscle, Safehouse | wanted pressure, betrayal, provisions loss, hideout exposed |
| Civic/community | season | town, settlement, neighborhood | Welfare, Law, Prosperity, Civic | one amenity and fortune per season | Amenity, Welfare, Law, Trade, Reserve | aspect loss, no new amenities, migration, town decline |
| Research/project | week + season | lab, ritual, expedition project | Clock, Materials, Safety, Patron | weekly ticks; season reckoning if large | Materials, Expertise, Safety, Secrecy, Breakthrough | accident, flawed result, patron anger, materials loss |
| Domain/war | season + year | estate, army, province | Supply, Legitimacy, Force, Threat | season campaign turn; yearly audit | Levy, Fortify, Diplomacy, Tax, Campaign | unrest, supply crash, desertion, invasion |
| Cozy/community | month + season | home, shop, community circle | Comfort, Bonds, Supplies, Reputation | monthly scenes; gentle seasonal turn | Host, Help, Improve, Trade, Rest | obligation, disappointment, shortage, festival trouble |

### 15.2 Profile Procedures

**Survival base.** Each week, pay or roll upkeep for Watch, Stores, and Shelter. If the base is unguarded, roll an intrusion/spoilage event. Each season, choose one improvement or stockpiling goal. This is FL-leaning: stronghold safety, storage functions, hireling pay, weekly upkeep, and unguarded-event pressure are the spine.

**Frontier business.** Each season, apply wages, competition, Law, and the relevant community aspect; then make the Enterprise Roll. No push. At 0 successes, wages and running costs are not covered and a Penalty result creates immediate debt or social trouble. At 2+ successes, a Bonus result creates dividends or position. This is West-leaning: Capital, proprietors, employees, town aspects, and Business Bonus/Penalty tables are the spine.

**Family/household.** Each season, choose one household priority: provide, reconcile, arrange, defend, educate, marry, inherit, or answer a feud. Roll using the caretaker's social/management skill plus help from involved kin. On success, raise Cohesion, Holdings, or Standing. On failure, Obligation or Feud rises and one named relationship demands a scene. Yearly turns handle succession, inheritance, and children aging into new roles.

**Faction/political.** Each season, every central faction chooses one move: recruit, pressure, bargain, expose, expand, fortify, or repair. Standing modifies social access; Heat/Threat triggers authorities or enemies. Use no-cascade propagation: one relationship change may create one neighbor reaction, not a whole-web avalanche.

**Criminal/outlaw.** Each month, the crew chooses Score, Lay Low, Resupply, Bribe, Recruit, or Move Safehouse. Scores create Stash and Heat. Lay Low reduces Heat but risks Loyalty. Each season, pay provisions/upkeep; unpaid crews create betrayal or splintering rather than a clean accounting penalty.

**Civic/community.** Each season, finish last season's amenity, apply aspect changes, choose the next amenity, roll fortunes, then give the players one civic problem to answer in play. If any essential aspect falls below the floor, the settlement enters decline and can no longer grow until the campaign deals with the cause.

**Research/project.** Each week, assign labor to Clock, Materials, Safety, or Patron. Breakthroughs require clock completion and a reckoning roll. Safety neglected means a failure produces harm, flawed invention, corruption, scandal, or a destroyed function.

**Domain/war.** Each season, count Supply and Force, choose diplomacy/tax/levy/fortify/campaign, then roll Legitimacy or command. Failure should produce unrest, supply failure, desertion, enemy breakthrough, or debt. Yearly audit changes borders, titles, law, and succession.

**Cozy/community.** Each month, pick one relationship/community scene and one improvement. Failure does not usually destroy the entity; it creates obligation, disappointment, shortage, embarrassment, or a chance to make amends. Keep the same YZE pressure loop, but lower catastrophic severity.

### 15.3 Calibration Gates

Before shipping a period system, answer:

1. **What source pole is it closest to?** FL weekly stronghold upkeep, West season business, West town amenity, or a hybrid.
2. **What is the active scale?** If you choose more than one, name which scale gets full procedure and which is summarized.
3. **What does investment buy?** Dice, safety, growth, output, reputation, secrecy, reserve, or labor.
4. **What is paid before the roll?** Cash, Capital, materials, stores, favors, time, obligations, or exposure.
5. **What can go bust?** Business, function, relationship, faction standing, settlement aspect, base safety, or project clock.
6. **What creates scenes?** Debt call, repair, rival, worker dispute, family obligation, shortage, theft, inspection, raid, ceremony, illness, or opportunity.

## 16. Integration Rules

- **With `06-travel-and-downtime`:** block-scale activities feed period play. A week of CRAFT/REPAIR/TRAIN can become +1 die, one project tick, or one cleared flaw.
- **With `07-base-faction-mass-scale`:** this file supplies the period clock and investment cycle; `07` supplies the scale ladder and org types.
- **With economy (`08`):** use cash for immediate spending, Capital/Reserve for enterprise posture, and resource dice for stores that deplete unpredictably.
- **With inventory/transport/storage (`26`):** use personal rows for carried gear, transport ladders for group stores, and storage functions for stockpiles; do not let an enterprise hold bulk materials without transport or a place to keep them.
- **With crafting/construction/investment economics (`27`):** use the cost/value translator for function prices, property Status, town amenities, investment payback, salaries, upkeep, loans, and persistent-bonus pricing.
- **With metacurrency:** do not let passive businesses generate metacurrency without a risk loop. If a base fuels powers/talents, require upkeep or a vulnerable function.
- **With factions:** if the full faction turn is active, do not also resolve every minor organization with full Enterprise Rolls. Use light moves for lesser factions.
- **With family play:** family obligations should create adventure hooks, not only penalties. Every obligation should have at least one scene-facing way to resolve it.
- **With existing host games:** classify each period system as General, Situational, Optional, or Campaign Mode. Most businesses are Optional; a settlement-as-PC is Campaign Mode.

## 17. Validation and Failure Modes

### Exploit Checks

| Risk | Test | Fix |
| --- | --- | --- |
| Passive profit | can players gain money without upkeep, risk, or time? | add upkeep, event, cap, or active period |
| Investment snowball | does profit buy dice that guarantee more profit? | cap investment dice, increase upkeep with scale |
| Help inflation | can a large group add unlimited dice? | cap help at +3 by default |
| Push farming | can long-period rolls generate metacurrency safely? | no push, or Risky Reckoning with debt/exposure |
| Reserve immunity | can Reserve cancel every bad result? | one cancellation per period; rebuild reserve slowly |
| Event spam | does every entity roll every table? | one event per shared web or central enterprise |
| Board-game drift | do period turns replace adventure? | every period must seed scenes, NPCs, obligations |

### Felt-Experience Checks

- **Stewardship:** players should feel they can care for the enterprise, not just watch it decay.
- **Ambition:** growth should be tempting and frightening.
- **Continuity:** consequences should carry forward, especially relationships and flaws.
- **Playability:** a bad season should create a rescue problem, not only declare ruin.
- **Distinctiveness:** a bank, ranch, and family must not all feel like "roll business; gain/lose money."

### Math Checks

- 5 dice succeeds at least once about 60% of the time; 7 dice about 72%; 9 dice about 81%.
- A standard enterprise roll should live in the 5-8 dice band after ordinary modifiers.
- +1 die is meaningful; +2 dice is a posture shift; +3 dice should require risk, cost, or rare advantage.
- Broad persistent +1 dice from functions should cost upkeep or be narrow.
- 0 successes must hurt, but should not usually erase the enterprise in one roll unless a collapse clock was already primed.

## 18. Publication Templates

### Player-Facing Rule

At the turn of each season, your enterprise reckons with the choices you made. First, pay its upkeep and resolve old trouble. Then choose how you invest: safety, output, growth, reputation, secrecy, reserves, or labor. After the season's work is done, roll the enterprise's Key Ability. One success keeps it steady. Two or more bring profit or opportunity. No successes mean loss, debt, damage, or public trouble.

### GM Procedure

Run the season in two halves. Looking back, collect upkeep, apply standing conditions, and resolve old trouble. Looking forward, let the players assess, invest, operate, reckon, and reinvest. Do not roll for every minor shop in the world. Roll only for enterprises the players own, depend on, oppose, or might lose.

### Quick Reference

1. Apply upkeep and old trouble.
2. Assess risk/opportunity.
3. Choose investment dials.
4. Resolve one operation move if needed.
5. Roll Key Ability + skill + functions + help (max +3) + modifiers.
6. 0 = Penalty; 1 = steady; 2 = Bonus; 3+ = Bonus plus reinvestment/growth.
7. Reinvest and seed next period.

### Sheet Fields

Enterprise Name; Type; Scale; Key Ability; Manager; Staff/Help; Functions; Gauges; Capital/Reserve; Standing/Reach; Upkeep; Risk Family; Current Dials; Debts; Events; Improvements.

## 19. Design Recipe

Use this when creating a downtime system for a new YZE game.

1. **Pick the active scale.** Week, month, season, year, or generation.
2. **Name the managed entity.** Business, family, faction, settlement, route, ship, company, lab, cult, school, estate, troupe, squadron.
3. **Define the output.** Profit, safety, knowledge, influence, welfare, production, legitimacy, continuity, secrets, faith, readiness.
4. **Choose 2-4 gauges.** Include one profit/output gauge, one risk gauge, and one relationship/public gauge.
5. **Write the sheet.** Key Ability, manager, functions, upkeep, standing, reserve, risk family.
6. **Build the activity menu.** At minimum: work, maintain, expand, negotiate, protect, exploit, lay low.
7. **Build the investment menu.** At minimum: safety, output, growth, reputation/secrecy, reserve/labor.
8. **Write the Enterprise Roll.** Include exact dice formula, modifiers, push rule, result ladder.
9. **Create Bonus and Penalty tables.** Use the generic D66 tables until the entity becomes central, then write trade-specific tables.
10. **Create one hard-season/contraction rule.** Every long-form enterprise needs a bad-period mode.
11. **Wire adventure hooks.** Each period must produce scenes: debt calls, rival moves, family obligations, repairs, escorts, investigations, negotiations, raids, ceremonies.
12. **Validate.** Check passive profit, snowballing, help cap, push farming, event spam, and distinctiveness.

**Final acceptance test:** after one season, the players should know what they gained, what it cost, who noticed, what worsened, and what they must decide next.
