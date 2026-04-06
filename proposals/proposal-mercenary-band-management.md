also run a realism audit of the extorted goods as it ma# Proposal: Mercenary Band Management

**Status:** Draft
**Target chapters:** Ch09 (The Stronghold), Ch08 (Journeys — Reputation integration)
**Classification:** Major optional expansion — chapter-scale content

---

## Context

The Forbidden Lands is a post-apocalyptic wilderness where warchiefs raise palisades from nothing, villages survive on what they can take from the land, and any man with a sword and enough scars can sell his violence to whoever needs it most. The current rules cover individual guards and hirelings at the stronghold. They do not cover what happens when you ride out with a dozen armed men at your back, when you take a contract to clear a hex of bandits, when your men go unpaid for two weeks and one of them puts a knife in your bedroll, or when you burn a farmstead to make a point and the ashes follow your name for years.

This proposal defines the systems for operating a mercenary band in the field: how to form one, pay it, feed it, keep it loyal, take contracts, manage bounties on its members, and live with the consequences of the things it does.

This can stand as a late section of Ch09 or as a standalone chapter if the mercenary play loop becomes central enough to justify it.

---

## Design Goal

The mercenary band system feeds the **base-building loop** and the **pressure economy** simultaneously. A band is a resource that generates coin and power, but also obligation, hunger, and moral weight. Running one should feel like herding dangerous animals in the rain. The system uses Quarter Day structure, existing condition mechanics, Settlement Reputation and Standing, and the FOOD resource die in ways that fit the existing engine without adding independent subsystems.

---

## Section 1: The Band

A mercenary band is a named fighting force led by one or more PCs. It has a roster, a daily cost, and a MORALE score. The band's identity — its name, its banner, the stories told about it — accrues or decays through the Reputation system.

### Forming a Band

A band requires:

- A **name** (given by the PCs or earned through deeds)
- A **leader** (the PC whose Reputation and MANIPULATION anchor the group)
- A minimum of **3 fighters** beyond the fellowship

A band has no maximum size, but size has consequences. Feeding twenty men in a hex with poor hunting is a problem. Paying them while the job falls through is worse.

The band's roster is recorded separately from the stronghold hireling sheet. Men in the stronghold are guards. Men in the field under a contract are the band.

### Size Tiers

| TIER        | MEN (beyond fellowship) | CHARACTER                                                                        |
| ----------- | ----------------------- | -------------------------------------------------------------------------------- |
| Skirmishers | 3–6                     | A handful of hard men. Move fast, attract little notice.                         |
| Warband     | 7–20                    | A real force. Villages take notice. Contracts get serious.                       |
| Company     | 21–50                   | Needs dedicated logistics. A name people know or fear.                           |
| Host        | 51+                     | Requires stronghold-level supply. Two Quarter Days of logistics per day minimum. |

### MORALE

MORALE is a single score from 1 to 5 tracked for the whole band. It is not a character attribute — it belongs to the band.

| MORALE | STATE    | EFFECT                                                                     |
| ------ | -------- | -------------------------------------------------------------------------- |
| 5      | Hungry   | Men are eager. +1 to band MELEE rolls in first round of any engagement.    |
| 4      | Steady   | No modifier.                                                               |
| 3      | Shaken   | -1 to band MELEE rolls. Non-payment requires a MORALE check this week.     |
| 2      | Wavering | -2 to band MELEE rolls. Check MORALE before any dangerous assignment.      |
| 1      | Broken   | The band may scatter. Any engagement triggers a MORALE check or desertion. |

**MORALE checks:** The leader rolls MANIPULATION vs. difficulty equal to outstanding grievances (see table in Morale Triggers below). On a failure, the band loses one MORALE step. On 0 ⚔️, two steps are lost and a Named Man (see Section 7) may leave or act against the group.

**Starting MORALE:** A fresh band recruited from a single settlement begins at 3. After a successful first engagement and receiving promised pay, it rises to 4.

### MORALE TRIGGERS

These change MORALE at the end of each week.

| EVENT                                            | MORALE CHANGE                                |
| ------------------------------------------------ | -------------------------------------------- |
| Won an engagement with few casualties            | +1                                           |
| Paid on time, in full                            | +1 (once/season, does not stack per payment) |
| Band proved decisive value — took something real | +1                                           |
| Suffered significant loss (20%+ casualties)      | -1                                           |
| Late payment by 3+ days                          | -1                                           |
| Broken contract (leader's fault)                 | -2                                           |
| Atrocity ordered by leader, no plunder gained    | -1                                           |
| Atrocity ordered, men got plunder                | +1 (but see Atrocities)                      |
| Fellowship abandoned the band in danger          | -2                                           |
| Named Man killed                                 | -1                                           |

### Band Archetypes

A band's origin shapes how it recruits, how it holds together, and what breaks it. The following archetypes describe the most common formations in the Ravenlands. They are not mutually exclusive — a band may start as one type and drift into another — but each carries distinct mechanical defaults.

**RURAL PEASANT BAND**
Farmers, woodcutters, and hunters who ran out of land or watched it burn. They know the wilderness, they are unafraid of cold and hunger, and they have no illusions about what the work is. Most started because someone raided their village and the choice was stay and die or leave and fight. The core of this band is usually a single village or hamlet — men who grew up together, buried their dead together, and trust each other the way people trust what they have tested.

- **Recruitment:** +1 to finding men at rural settlements. The captain takes anyone from the home village or hamlet who can hold a weapon and is willing. Strangers are considered on a longer timeline — they must eat with the men for several weeks and be vouched for by someone already in the band before they are treated as part of it. A new man who fits the crowd is accepted without ceremony. A new man who does not fit may never be trusted regardless of skill.
- **Strengths:** FORAGING rolls improved — treat one additional terrain type as favored when foraging. Comfortable camping in poor conditions; -1 to food cost when encamped in wilderness terrain.
- **Weakness:** Loyalty is local. If a contract takes the band far from the region they know, MORALE checks are at +1 difficulty until the band has been abroad a full season. They also tend to carry the politics of the home village with them — old grudges, family debts, a face someone punched ten years ago.
- **Typical Named Men personality:** Flat, Death-Easy, Mercenary Proud.
- **Breaks when:** The captain starts acting like a lord. Some of these men left a lord. They know the shape of it.

**TYRANT BAND**
Built around one captain who holds the company by force of threat and selective violence. The men stay because leaving has a cost, because the captain wins enough, and because the alternative is starting over with nothing. Some of these companies are the most effective in the field. Some are charnel houses in slow motion.

- **Recruitment:** Tyrant captains prefer men who are already broken to something. Criminals, former convicts, men with debts or prices on their heads, men who have no settlement to return to. The initiation is a test of submission: new men are given the worst tasks, subjected to directed cruelty from the senior members, and watched to see if they break, run, or go quiet and adapt. Men who go quiet and adapt are the ones the captain wants. Men who fight back are allowed to stay only if they fight well enough to be worth the trouble — and only if the captain can hurt them in a way that settles the question of who is in charge. A criminal background is not required but is treated as a qualification: a man with a past is a man who cannot afford to leave.
- **Strengths:** May use INTIMIDATION in place of MANIPULATION on all internal discipline and MORALE checks (see Tyrant Punishments above). Common fighters do not check morale in the first round of any engagement — fear of the captain outweighs fear of the enemy.
- **Weakness:** The band is Fear-Held (see Tyrant Companies, Section 6). Named Men Loyalty decay is doubled. When the captain is absent, removed, or visibly weakened, MORALE drops by 1 immediately and all Named Men re-evaluate their position.
- **Typical Named Men personality:** Calculating, Paranoid Competent, Grudge-Holding.
- **Breaks when:** The captain loses once — badly, visibly, in front of men who have been storing the calculation for months.

**MILITARY BAND**
Veterans of a larger force: soldiers who served under a warchief, garrison troops who got left behind when the campaign ended, or units whose commander died and whose pay stopped. They drill, they hold formation, and they have a professional relationship to violence that peasant bands do not.

- **Recruitment:** The captain requires demonstrated prior service before accepting a new man — a verifiable record of engagements, a recognizable military background, or sponsorship from a current member who can attest to capability. Useless men are not taken on as projects. A man who cannot name his role, maintain his own equipment, and perform a specific function in the line is turned away regardless of need. Roles must be filled — the captain recruits to gaps, not to headcount. Without a SCOUT, they recruit a scout. Without a MEDIC, they find a healer. When all roles are covered, they stop recruiting until something breaks. -1 to finding men at rural settlements. +1 at town-scale settlements and at other military encampments.
- **Strengths:** DRILL time is halved — the band reaches trained status after three days of drill rather than a full week. Common fighters hold formation in the second round of an engagement without a MORALE check. Sergeants in this band promote to full authority one engagement sooner than the standard rules require. Logistics are maintained precisely; the band never accidentally runs short through poor tracking.
- **Weakness:** Pay expectations are higher and non-negotiable. A military band at Steady MORALE expects full pay on schedule; a single late payment triggers a check at +1 difficulty rather than the standard threshold. They also have opinions about the captain's decisions and will not hide them.
- **Typical Named Men personality:** Mercenary Proud, Territorial, Quietly Violent.
- **Breaks when:** The captain shows they do not understand what a real formation is, or when the job clearly has no professional merit — atrocities, reckless assault, abandonment of standards.

**KIN BAND**
All members share blood, clan, or kin heritage. An orc warband. A wolfkin pack. Three halfling brothers who picked up stragglers of the same kin over two seasons. The loyalty structure runs through blood and old obligation rather than through coin and contract. These bands do not behave like mercenary companies in the standard sense — they behave like extended families who have become dangerous.

- **Recruitment:** Same kin only, by default. A family-based kin band (same bloodline, not just same kin type) will not accept outsiders at all without a vouch from at least one existing member and, in some cases, a formal bond or oath before the group. An outsider vouched in is treated as kin-adjacent — they have standing but not full blood standing, and the band will not extend them the same protections automatically. A man who is vouched for and then betrays the band is an example made of without debate. Use the Kin and Recruitment modifiers from Section 2.
- **Strengths:** MORALE is checked at -1 difficulty when the cause of distress is external (enemy action, contract failure, hunger). Internal grievances are handled within kin tradition — the GM should develop 1–3 kin-specific honor rules that function as additional Triggers for Named Men in this band.
- **Weakness:** An atrocity against a member of the same kin — a company member of the shared kin harmed by the captain's order — triggers automatic MORALE -2 and a loyalty roll for all Named Men, regardless of current MORALE level. Blood obligations can also pull Named Men away from the band for personal reasons that have nothing to do with the contract.
- **Typical Named Men personality:** Grudge-Holding, Territorial, Flat.
- **Breaks when:** The captain does something that violates the kin's internal code — betrayal of a blood member, dishonoring a bloodline, exposing a family weakness to outsiders.

---

## Section 2: Recruitment and Quality

### Finding Men

Fighters are recruited the same way as the GUARD hireling: visit a settlement, make a MANIPULATION roll. Use settlement size and the stronghold's Reputation to modify the roll. A settlement that has heard of the band through Reputation may provide candidates without a roll.

In the field, recruitment can happen in:

- Villages: D6 potential recruits, roll supply as Common
- Inns and crossroads: 1D3, MANIPULATION to find willing fighters
- Former bandits, defeated enemies: MANIPULATION difficulty 2 to bring in; they begin at loyalty 1 (see Named Men)

A SHELTER/BARRACKS at your stronghold adds the existing bonus for finding hirelings. It does not help recruiting in the field.

**Settlement tapped:** Once the band has recruited from a settlement, that settlement is tapped for one year. No further recruitment rolls there until that time has passed. The band stripped out the men willing to fight. What remains are the ones who did not want to go, and pushing harder only damages Standing. The one exception: if the band has done something notable for that settlement since the last recruitment — defended it, returned a captive, brought significant wealth — the GM can allow a second draw within the year.

This applies even if the band has changed hands. The men are gone regardless of who is leading now.

### Fighter Tiers

| TIER    | SALARY/DAY | SUPPLY   | STATS                                      | NOTES                                                                           |
| ------- | ---------- | -------- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| Common  | 1 silver   | Common   | STR 3, AGL 3, MELEE 1, Armor 3 (leather)   | Standard soldier. The existing GUARD hireling.                                  |
| Veteran | 2 silver   | Uncommon | STR 4, AGL 3, MELEE 2, Armor 4 (chainmail) | Has seen blood and did not run. Requires TRAINING GROUNDS to hire.              |
| Elite   | 3 silver   | Rare     | STR 5, AGL 4, MELEE 3, Armor 5 (plate)     | A named fighter in their own right. Requires TRAINING GROUNDS + SHOOTING RANGE. |

A band need not be uniform. A warband of 10 might include 6 Commons, 3 Veterans, and 1 Elite who serves as the sergeant.

The stats above are for anonymous fighters. Any Veteran or Elite who becomes a Named Man uses the full character build in Section 7, which adds WIT, EMP, individual skill distribution, and talents.

### Kin and Recruitment

Most fighters in the Ravenlands are human. The others are not impossible to find, but they come with different expectations, different reasons for hiring out, and different problems when things go wrong.

| KIN      | RECRUITMENT MODIFIER | NOTES                                                                                                                                                                          |
| -------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Human    | None                 | Standard.                                                                                                                                                                      |
| Half-Elf | None                 | Found near trade crossroads and mixed settlements. Slightly more likely to negotiate terms before signing.                                                                     |
| Elf      | -2 to roll           | Rare as hired fighters. Those available are usually exiled, disgraced, or carrying something they can't name. When found, they fight at Elite tier by default.                 |
| Dwarf    | -1 to roll           | Slow trust. Once hired, their Loyalty floor is 2 — they will not start at 1. They do not desert quietly; if they go, you know about it.                                        |
| Halfling | -2 to assault rolls  | Hard to find for frontal assault contracts. Excellent scouts and skirmishers. A halfling Named Man hired for scout or stealth work has no recruitment penalty.                 |
| Wolfkin  | Special              | Pack-oriented. When you recruit a wolfkin, roll D3. That many additional wolfkin may accompany them as Common fighters at the same terms, with no additional recruitment roll. |
| Orc      | None                 | No penalty for orders involving violence, including atrocity-adjacent work. Some carry old grudges that may complicate contracts against specific kin or settlements.          |
| Goblin   | Common Only          | Available at Common tier only. Half the standard salary. Useful as scouts and flankers; will not hold a palisade under direct assault.                                         |

These modifiers apply to the settlement recruitment roll only — the MANIPULATION roll. They are not permanent attribute adjustments.

### Advance Payment

When hired for field work away from the stronghold, fighters expect advance pay for the projected duration. Pay one week in advance. If the job runs long, pay again before the week expires or roll on the FIELD NON-PAYMENT table (see Section 3).

---

## Section 3: Pay, Provisions, and Consequences

### Daily Costs

The band eats. Budget 1 FOOD unit per man per day. For a warband of 10, that is 70 FOOD per week — a genuine resource pressure. This does not include the fellowship themselves.

Add daily wages. A warband of 10 commons costs 10 silver per day, 70 silver per week. A mixed warband (6 common, 3 veteran, 1 elite) costs 15 silver per day, 105 silver per week. These numbers are before any stronghold upkeep.

This pressure is intentional. It motivates contract-taking and resource risk.

### Feeding the Band

The band forages when possible. Rather than rolling dice for each forager individually, use the **daily field ration table** below. Assign a number of men to foraging each Morning Quarter — they are not available for other duties that Quarter Day. The result tells you how many FOOD units the forager party brings back by Evening, before provisions are drawn.

**Daily forager output by terrain and party size:**

| TERRAIN     | Hunt mod | 1–2 foragers | 3–5 foragers | 6–10 foragers | 11+ foragers |
| ----------- | -------- | ------------ | ------------ | ------------- | ------------ |
| Forest      | 0        | 3            | 8            | 16            | 28           |
| Dark Forest | 0        | 3            | 8            | 16            | 28           |
| Marshlands  | +1       | 4            | 10           | 20            | 34           |
| Plains      | 0        | 2            | 5            | 10            | 18           |
| Hills       | 0        | 2            | 7            | 13            | 22           |
| Mountains   | -1       | 1            | 3            | 7             | 12           |
| Quagmire    | -1       | 1            | 3            | 7             | 12           |
| Ruins       | -1       | 1            | 3            | 7             | 12           |
| Tundra      | -2       | 0            | 2            | 4             | 8            |

Apply season modifier from Ch08 if that proposal is in use (Spring -2, Summer -1, Autumn +1, Winter 0 — add to Hunt mod column, clamp 11+ forager output minimum to 0). A fellowship member with MASTER OF THE HUNT rank 3 or above may upgrade one column to the right for the entire party.

This output fills the band's daily FOOD requirement from the bottom up. A Warband of 15 men needs 15 FOOD per day. With 5 foragers in Forest terrain they bring back 8 — the remaining 7 come from provisions. With 10 foragers they bring back 16, covering the full band. A Company of 35 in the same forest needs 35 FOOD; 15 foragers return 28, leaving 7 from provisions. Good terrain with enough foragers sustains a band. Plains sustain about half. Mountains and Ruins sustain a fraction — enough to slow the drain, not enough to stop it. Tundra is a death march against the stores.

Running a large band in thin country burns your provisions. That is intentional.

If a band goes unfed for a full day, every fighter suffers a CONDITION. A second day without food, they begin to break or desert independently of MORALE.

### FIELD NON-PAYMENT

When the leader fails to pay the band on time, roll D6. This replaces the standard NON-PAYMENT table for armed men away from a stronghold, because armed men unpaid in the field are more dangerous than a handyman who hasn't been paid.

| D6  | EFFECT                                                                                                                                       |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | One D3 of the unhappiest fighters desert overnight. They may sell information about the band's position, contracts, or crimes to any buyer.  |
| 2   | A Named Man (if any) demands written acknowledgment of the debt. If refused, they leave and their loyalty shifts to whoever hires them next. |
| 3   | The men keep working but slow down. Band counts as SHAKEN (MORALE -1 step) for the week, regardless of current MORALE.                       |
| 4   | The sergeant or most senior fighter confronts the leader publicly. MANIPULATION difficulty 2 to hold the command. Failure costs 1 MORALE.    |
| 5   | Quiet muttering only. The leader loses any +1 MORALE bonus they would have gained this week.                                                 |
| 6   | The men accept it for now, but every man remembers. Next non-payment rolls twice on this table.                                              |

If the band has a BARRACKS/SHELTER back at the stronghold, apply the standard improved non-payment rule (roll twice, take the higher result) to that table only while fighters are at the stronghold. In the field, this table always applies.

---

## Section 4: Village Extortion and Tribute

A band with enough swords and enough hunger does not need a contract. It can ride into a village, state its size, and let the arithmetic do the talking. This section covers what happens when the band uses its presence as leverage — demanding tribute, occupying a settlement, or taking what it needs by force or threat.

This system connects directly to Settlement Standing, the Feud Track (Ch08), and the Atrocity rules in Section 9.

### The Balance of Force

Before demanding anything, compare the band's effective fighting strength to the settlement's available fighters — its guards, hunters, and able-bodied men who will stand — not its full population. Use these rough brackets:

| SETTLEMENT SIZE        | APPROXIMATE FIGHTERS AVAILABLE | NOTES                                                                                                                                                                                                                 |
| ---------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hamlet (1-10 people)   | 1–3                            | Almost no armed capacity. Will yield or flee.                                                                                                                                                                         |
| Village (11-40)        | 2–6                            | A few hunters and one tough elder.                                                                                                                                                                                    |
| Large village (41-100) | 5–12                           | Organized resistance possible.                                                                                                                                                                                        |
| Town (101-300)         | 10–30                          | A warchief or headman with force behind him. A Warband cannot hold 2:1 here — a full Company of 40+ is the minimum. Towns are rare in the Ravenlands; most bands will never have the numbers to threaten one cleanly. |
| Fortified town         | 20–60+                         | As a stronghold. They will fight, and they have walls.                                                                                                                                                                |

**Clearly larger** means the band's fighting men number at least twice the settlement's available fighters — a 2:1 advantage. Against an unfortified settlement at that ratio the arithmetic is plain to everyone: resistance costs more than the tribute. Below 2:1, the settlement may calculate that fighting is worth it. Village men who watch their elder hand over the harvest without any blood drawn have a long memory and a short limit.

If the band and the settlement are roughly matched, negotiations may fail and blood follows. If the settlement outmatches the band, there is no leverage — only risk.

### Demanding Tribute

The band arrives at a settlement and makes a demand. The leader chooses whether to negotiate or threaten — use MANIPULATION or INTIMIDATION. The difficulty table is the same either way. The consequences are not.

**MANIPULATION** treats the demand as one professional to another. The leader lays out the arithmetic and lets the settlement do the math on its own. A capable MANIPULATION roll leaves the settlement poorer but not enraged.

**INTIMIDATION** skips the calculation and goes straight to the fear. It is faster and works when the leader lacks the social skill to negotiate. It carries three built-in costs:

- Standing drops 1 extra on any success, beyond the normal tribute hit. Fear is compliance, not goodwill.
- Feud Track advances +1 on any success. The settlement was not persuaded — it was broken. It is already thinking about who it can call for help.
- On a failed INTIMIDATION roll, the settlement does not merely refuse. Roll D6: 1–2, they draw weapons immediately — treat as combat, and Pillaging consequences apply regardless of how the fight ends; 3–6, they refuse and the band must eat the loss or escalate.

**Pushing an INTIMIDATION roll** carries additional risk: if the push still fails, the band must either attack (Pillaging) or retreat with Standing -2 and Feud Track +1. The bluff has been called and everyone in the settlement saw it.

Settlements that reach Feud Track 3 or 4 after INTIMIDATION tribute post better-paid bounties. The band is feared rather than merely resented, which makes killing or capturing its leaders worth more to rivals and warchiefs looking for reputation. Treat any bounty posted against an INTIMIDATION-tribute band as worth +50% over the standard rate.

| SITUATION                                            | DIFFICULTY                                                          |
| ---------------------------------------------------- | ------------------------------------------------------------------- |
| Band ≥2× settlement's fighters, Standing neutral     | 1                                                                   |
| Band ≥2× settlement's fighters, Standing positive    | 0 (auto-succeed with 1 ⚔️)                                          |
| Band and village roughly matched                     | 2                                                                   |
| Village is fortified or has allies nearby            | 3                                                                   |
| Band previously extorted this settlement (same year) | +1 to difficulty                                                    |
| Settlement Standing already -3 or worse              | Roll fails automatically — they have nothing more to give willingly |

On a success, roll or choose from the **Tribute Table** based on settlement size:

| D6  | HAMLET             | VILLAGE                | LARGE VILLAGE                                   | TOWN                                    |
| --- | ------------------ | ---------------------- | ----------------------------------------------- | --------------------------------------- |
| 1   | 2D6 FOOD           | 1D6 silver             | 3D6 silver                                      | 5D6 silver                              |
| 2   | 1D3 FOOD, 1 silver | 2D6 FOOD               | 1D6 silver + 5D6 FOOD                           | 3D6 silver + 2D6 FOOD                   |
| 3   | 1D3 silver         | 3D6 FOOD               | 2D6 silver + tools/gear                         | 4D6 silver + quality gear               |
| 4   | 1 pelt or hide     | 1D3 silver + 1D6 FOOD  | 4D6 FOOD + animals                              | 3D6 silver + animals                    |
| 5   | 1D6 FOOD + 1 tool  | 1D3 silver + equipment | 2D6 silver + a Named Man surrendered            | A Named Man surrendered + 2D6 silver    |
| 6   | Work (1 QD labor)  | Animals (livestock)    | A week of hosted supply (food, lodging, fodder) | Two weeks of hosted supply + 2D6 silver |

**Named Man surrendered:** The settlement hands over its most capable fighter — a hunter-warrior, a returned soldier, a young man the elder would rather lose now than watch die in a fight the village cannot win. This person joins the band's roster at Veteran tier. If the elder convinced them it was better than the alternative, they start at loyalty 3 and will do the work. If handed over against their will, loyalty starts at 1 — they came because the elder sold them, and they will desert or inform against the band at the first credible opportunity unless the leader wins them over personally. Either way, the settlement loses that fighter permanently. The village is now weaker than it was when the band arrived.

Each ⚔️ on a **MANIPULATION** roll allows the leader to choose freely from the tribute table rather than rolling, or to name a specific item. With 3+ ⚔️, the settlement complies without argument, up to what it actually has.

Each ⚔️ on an **INTIMIDATION** roll suppresses one revolt trigger. The first ⚔️ earned before a push cancels the D6 combat roll on a failed push — the crowd backs down rather than drawing steel. The Standing and Feud Track consequences still apply.

On a failure with MANIPULATION, the settlement refuses and Standing drops by 1. The band can force the issue (see Pillaging, below) or back down.

**Repeat visits and depletion:** Each settlement can be successfully tribute-stripped a limited number of times in a single year before it has nothing left to give. Track successful tribute demand attempts (forced or willing) against each settlement separately.

| SETTLEMENT SIZE | ANNUAL TRIBUTE LIMIT | DEPLETION NOTE                                                      |
| --------------- | -------------------- | ------------------------------------------------------------------- |
| Hamlet          | 1                    | One round strips a hamlet bare. It has seed grain and that is it.   |
| Village         | 2                    | Two rounds in a year leaves the village eating roots by winter.     |
| Large village   | 3                    | Three rounds is manageable once; brutal twice in consecutive years. |
| Town            | 4                    | A town has reserves. Fourth demand empties them.                    |

Once the annual limit is hit, the settlement's roll fails automatically regardless of force applied — there is nothing to take. The band can still pillage (destroy what remains) or occupy, but no tribute payment is possible until the next year.

Each repeat visit before the limit is hit costs Standing and Feud Track as follows:

- First demand: Standing -1 on success, Feud Track +1
- Second demand (same year): Standing -1 on any result, Feud Track +1
- Third demand (same year): Standing -2, Feud Track +1, and all adjacent settlements within 1 hex hear about it (Standing -1 there as well)
- Fourth demand or beyond: Feud Track +2 per demand. The settlement's neighbors are already organizing.

### Tribute as Standing

A band that demands tribute and takes it is exactly the kind of force that settlements learn to either pay or destroy. Track the interaction:

- First successful tribute: Standing at this settlement drops by 1. The elder paid. They remember.
- Second tribute (same year): Standing drops by 2. They are paying tribute now, not choosing to be generous.
- Third tribute or forced payment: Standing drops to -3 or lower. This settlement is a tributary. It will accept help from anyone who offers to make the band stop.

### Settlement Decay

A settlement bled past its annual tribute limit, pillaged more than once, or occupied for more than a season begins to fail. People leave or die. The settlement shrinks.

**Decay trigger:** Any of the following in a single year causes a size drop at year's end:

- Annual tribute limit exceeded (any amount beyond the cap)
- Two or more pillages in the same year
- Occupation lasting more than one full season
- Annual tribute limit hit two years in a row, even without exceeding it

**Decay cascade:**

| CURRENT SIZE  | DROPS TO      | EFFECT                                                                                                   |
| ------------- | ------------- | -------------------------------------------------------------------------------------------------------- |
| Town          | Large village | The warchief or headman leaves with his household. Fighters drop proportionally. Trade halts.            |
| Large village | Village       | Half the families scatter. Available fighters halved. Forager output reduced one bracket.                |
| Village       | Hamlet        | Most adults gone. Only the stubborn or the trapped remain. Tribute capacity: 1 per year.                 |
| Hamlet        | Deserted      | The last families leave or die. No triggers, no hirelings, no trade. The hex functions as Ruins terrain. |

A **deserted settlement** is a ruin. The buildings stand, or most of them do. You can camp in the shells. Foraging and hunting use Ruins modifiers. No one is there to pay tribute, offer work, or sell information — but someone may come back someday, or something may move in.

Decay is permanent unless the GM runs active resettlement as part of play. A settlement that drops to Hamlet can recover to Village over 2+ years if left completely alone and the band never returns. A deserted settlement requires an active colonization effort to rebuild — treat that as stronghold founding rules from Ch09.

The GM should track the current size of any settlement the band has touched. A map that shows villages the band turned into ruins is working as intended.

### Pillaging

If the band takes what it wants without asking — or forces collection after a refused demand — this counts as an Atrocity (see Section 9, Burning/Massacre categories as applicable). The Standing hit is immediate (-3 minimum at this settlement, -1 at settlements within rumor range). The Feud Track advances by 2 steps.

Food and goods taken this way cost nothing in coin but generate the Atrocity consequences. They do feed the band and fill the stores.

### Occupation

The band can occupy a settlement — plant its banner and stay, asserting authority over the village's labor and production. This is distinct from tribute: the band is not passing through and demanding; it is setting up a power structure.

**To occupy:**

- The band must be physically present (or leave a detachment behind)
- MANIPULATION roll difficulty 2 (3 if any Standing -2 or worse already in place)
- On success: the settlement becomes an _occupied_ tributary

**Occupied tributary rules:**

- Produces 1D6 silver worth of goods per week, drawn from what the settlement generates
- Counts as a SHELTER/BARRACKS equivalent for finding hirelings (the band has a home here)
- The band can draw on the settlement's HUNT/FORAGE output directly: reduce daily FOOD cost by the settlement's hex forager output (treat as 3–5 foragers of the hex's terrain)
- The occupation requires at least 2 fighters left behind per 10 settlement adults, or it collapses within a week

**Occupation costs:**

- Standing at this settlement: -1 per week of occupation (minimum floor -5)
- Neighboring settlements within 2 hexes: Standing -1 once (when occupation is established and word travels)
- Feud Track advances +1 at occupation start

**Ending an occupation:**

- The band leaves: occupation ends. No settlement will forgive cleanly; Standing does not recover automatically. Treat as resolved Feud Track step for recovery purposes.
- The settlement revolts: if Standing hits -5 and the detachment is fewer than required, the settlers attack. They use ANGRY MOB rules at full settlement adult strength.
- A rival force drives the band out: the rival inherits whatever goodwill the band destroyed, at GM discretion.

### Feud and Resolution

Extortion, tribute, and occupation all interact with the Feud Track. Use the extended track:

| STEP | STATE        | EFFECT                                                                                                    |
| ---- | ------------ | --------------------------------------------------------------------------------------------------------- |
| 0    | Cold         | Settlement has paid or complied. Tension exists.                                                          |
| 1    | Resentful    | Settlement talks to its neighbors. Standing -1 at adjacent settlements within 1 hex.                      |
| 2    | Coordinating | Settlement seeks outside help. Any warchief or band within 3 hexes may hear the appeal.                   |
| 3    | Armed        | Settlement has hired or allied with another force. That force will actively seek the band's eviction.     |
| 4    | Vengeance    | Settlement has committed to destroying the band regardless of cost. Bounty posted. Standing -3 area-wide. |

**Advancing the track:**

- First tribute demand (same year): +1
- Forced tribute after refusal: +2
- Pillage or atrocity: +2
- Occupation established: +1
- Killing a defender: +2

**Retreating the track:**

- One season passes with no contact: -1 step
- Compensation paid (≥ 5× weekly tribute in coin, food, or equivalent goods): -2 steps
- Compensation paid publicly with a Named Man witnessing the oath not to return: -3 steps
- A genuine service to the settlement (clearing a threat, returning a captive, defending against a third party): GM may reduce 1–2 steps at discretion

At Feud Track 3 or 4, the opposing force becomes an active NPC faction. The GM names them, gives them a size tier, and they begin hunting the band or hiring against it. This is the machinery of consequence: the band has made itself an enemy of the land it is eating.

---

## Section 5: Contracts and Bounties

### Contracts

A contract is a job with defined terms, a named employer, and a coin figure. Contracts can be:

- **Patrol** — Keep a hex clear of monsters or bandits for a season. Pay: weekly.
- **Escort** — Bring a person or cargo from point A to point B. Pay: on arrival.
- **Assault** — Take a stronghold, clear a ruin, kill a target. Pay: advance + completion.
- **Intimidation** — Occupy a settlement or demonstrate force until a demand is met. Pay: as agreed.
- **Revenge** — A private party wants something destroyed. Pay: based on what they can afford.

**Terms always specify:**

- The target or task
- Duration or completion condition
- Full amount and payment schedule (advance / balance / expenses)
- Exclusivity (can the band take other work meanwhile?)
- Liability for incidental damage (burning a farmstead on purpose vs. by accident matters)

**Breach:** If the leader breaks the contract, the employer can post a GRIEVANCE. A grievance becomes a Standing hit at every settlement the employer has Standing in, equal to the breach's severity. Repeated breaches accrue reputation as oath-breakers, which is tracked separately (see Atrocities).

**Written vs. spoken:** Spoken contracts are common; anyone who witnesses the oath can testify. Written contracts require a SCRIBE or a literate PC, but they carry more legal weight in contested settlements and can be sold or transferred.

### Posting a Bounty

Any person, settlement, or faction with coin can post a bounty. A bounty is an offer: kill this person, capture this person, return this stolen item. The bounty amount is paid on delivery. Bounties are posted at inns, gateposts, markets, and wherever men gather to sell their services.

**Posting a bounty requires:**

- A settlement or stronghold to anchor it (the bounty lives there)
- The coin available upfront or guaranteed by a wealthy backer
- A description clear enough for someone to act on it

**Finding bounties:** Any PC making a MANIPULATION roll in a settlement of Reputation 3+ may ask about current bounties. One ⚔️ finds the local postings. Three ⚔️ turns up bounties from the broader region, carried by travelers.

**Accepting a bounty:** No roll required. The PC accepts the task; the coin is held — sometimes literally in a locked box at the inn.

**Bounties on the fellowship:** If the PCs have done something worth targeting, any aggrieved party can post a bounty on them. The bounty amount travels via the Reputation and rumor system (Ch08). At each settlement within rumor range of the posting, the GM may have NPCs react with recognition. The fellowship's Reputation makes this faster: a well-known band is easier to identify and report on.

**Clearing a bounty:**

- Pay restitution acceptable to the grantor — typically double the stated harm plus public acknowledgment
- Eliminate the grantor (this rarely ends the matter: heirs inherit grievances)
- Outlast it — a bounty not pursued for a full year fades from active memory; reduce its effective Reputation spread by 1 step each season after the first
- Negotiate — MANIPULATION difficulty 3 to argue the grantor down; they must have reason to be persuadable

### Kidnapping

Kidnapping is a contract or a crime depending on who ordered it and who got taken. The mechanics are the same either way. The money changes.

**As a contract:** An employer pays to have a specific person captured and delivered alive. The band executes the grab, handles transit, and collects on delivery. Payment is split — advance on acceptance, balance on successful delivery. Terms always specify condition: alive means breathing and able to stand and answer questions. A dead or permanently broken delivery earns partial payment at best, and an employer who wanted the person alive is now an aggrieved party.

**As a ransom operation:** The band captures someone worth money to someone — a merchant's son, a warchief's wife, a named creditor — and holds them while sending word. The value of the ransom depends on who was taken and what they mean to the payer. The band collects nothing until someone decides to pay.

**Executing the grab:** A capture attempt works like a standard MELEE exchange, but the attacker's goal is BROKEN condition, not dead. Once a target is Broken, they can be restrained without a roll. An unbroken target who is outnumbered 3:1 may surrender on a MANIPULATION roll by the leader (difficulty 2). On a failure, the target fights until Broken or dead.

Taking a well-guarded target requires a full combat, which costs time, noise, and clean hands. Most kidnappings happen at night, on the road, or in the moment when the target is outside their walls.

**Holding a captive:**

- Each captive consumes 1 FOOD per day, same as a fighter.
- A captive with STR 4 or higher, or who holds any military or wilderness skill, attempts escape once every 3 days. Roll opposed SCOUTING (captive vs. the band's watch). A failed escape attempt costs the captive 1 STRENGTH from restraint. Success: the captive is gone.
- Shackling a captive removes escape attempts but requires chains or rope (1 silver). A shackled captive cannot walk under their own power without assistance.
- A captive who is starved, tortured, or treated as a slave rather than a prisoner arrives at delivery in a state the employer or family may find unacceptable. A consistently mistreated captive may die before the negotiation closes.

**Ransom negotiation:** Send word first. The demand is a message — carried by a neutral party or left at a known location. State the amount, the delivery point, and the deadline. The GM determines whether the target's connections can pay the stated amount.

If the payer counters, the leader makes a MANIPULATION roll (difficulty 1 if the band holds clear leverage, difficulty 2 if the payer is stalling). Success holds the negotiation on band terms. Failure means the payer's number creeps forward, or the negotiation breaks.

A deadline passed without payment: execute the captive, extend at cost, or release and absorb the loss. Executing a captive who was not yet paid for is an Atrocity (see Section 9). Releasing them generates no coin but avoids the Atrocity consequence.

**Ransom rates by captive value:**

| CAPTIVE TYPE                         | RANSOM          | NOTES                                                                                     |
| ------------------------------------ | --------------- | ----------------------------------------------------------------------------------------- |
| Common civilian, no connections      | 1D6 silver      | Barely worth holding. Better as leverage on their settlement.                             |
| Skilled craftsman or merchant factor | 2D6 silver      | Employer wants them back working. Condition matters.                                      |
| Merchant or settlement elder         | 3D6 silver      | Real money, real family. Will have connections who ask questions.                         |
| Named Man from another company       | 4D6 silver      | Their captain may pay to recover the asset — or may write them off.                       |
| Warchief's kin or equivalent         | 6D6 silver      | The payer has resources. The payer also has reach. This purchase comes with enemies.      |
| Fellowship member (PC)               | GM's discretion | The PC's connections, assets, and debts determine what the band can realistically demand. |

**Recovery bounties:** Anyone with coin and a kidnapped person they want back can post a bounty for the captive's safe return. Recovery bounties always specify condition — alive, unharmed, or alive and able to testify. Dead delivery is worth nothing. Partial condition earns partial payment or earns an enemy.

A recovery bounty travels through the rumor system like any other bounty. If the band holding the captive has a name and that name is known, other bands will hear that there is a bounty in play. That creates competition. The kidnapping band now has enemies from the payer and from any freelancer who wants the coin.

**Condition on delivery:** Always settled before handoff. A captive promised unharmed who arrives with broken fingers generates a grievance regardless of payment. A captive promised alive who dies in transit earns nothing. The band bears responsibility for the captive's condition from the moment of capture to the moment of delivery.

### Mercenary Hoards

Coin moved in a band does not travel safely. Inns hold it until someone drinks it. Strongholds hold it until someone attacks the stronghold. Banks do not exist in the Ravenlands. The answer most experienced captains reach is the same: bury it.

A mercenary hoard is a hidden cache of valuables — coin, pelts, a good sword, whatever survives the years. It is not a bank. It has no lock and no ledger. The only security is that no one knows where it is.

**Establishing a hoard:** Choose a hex and a specific terrain feature — a hollow root, a marked stone, a particular river bend with a distinctive fork. Make a SURVIVAL roll. Each ⚔️ indicates how difficult the cache is to find by someone who does not know the exact location:

| ⚔️  | CONCEALMENT                                                                   | FINDER'S ROLL DIFFICULTY |
| --- | ----------------------------------------------------------------------------- | ------------------------ |
| 0   | Poor. An obvious disturbed patch of earth or a too-neat arrangement of stone. | 1                        |
| 1   | Adequate. Requires deliberate searching in the right hex.                     | 2                        |
| 2   | Well hidden. Requires knowing the terrain feature specifically.               | 3                        |
| 3+  | Expert. Requires the marker, or weeks of systematic searching.                | 4                        |

The leader records the hoard location and marker privately. If the leader dies or deserts without disclosing it, the hoard is lost as a practical matter — though it stays in the ground.

**Hoard contents by band size and duration:**

| BAND SIZE AND DURATION    | TYPICAL VALUE              | LIKELY CONTENTS                                                                                      |
| ------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------- |
| Patrol, one season        | 3D6 silver                 | Coin only. Maybe a spare knife.                                                                      |
| Warband, one season       | 5D6 silver                 | Coin, one quality item (weapon or armor piece), D3 pelts.                                            |
| Warband, one year         | 4D6 silver + 1D6×10 copper | Coin, 1–2 quality items, one trophy or curiosity.                                                    |
| Company, one season       | 3D6×5 silver               | Coin, 2–3 quality items, provisions for 1 week, captive goods held for sale.                         |
| Company, one year or more | 3D6×10 silver              | Significant coin, quality weapons and armor, trade goods, possibly a map or deed, one artifact item. |

On arriving at an old hoard site not touched in a year, roll D6: on a 1, something disturbed the cache — water, animals, a structural collapse. Reduce contents by half. On a 6, conditions preserved everything exactly.

**Multiple caches:** Experienced captains split reserves across two or three hides in different hexes. No single capture or betrayal empties the full reserve. Record each location separately. Some captains forget one. Some captains leave one behind deliberately when they leave a region permanently. Those are the ones hunters find.

> **Finding a Dead Band's Hoard**
>
> Old bands leave things behind. A company broken by plague, ambushed and scattered, dissolved after a bad winter — the captain buried the surplus before things went wrong, or sometimes after. The captain died. The sergeant who knew the location died a week later. The hoard sits.
>
> Word reaches the fellowship by several routes: a survivor who knows the hex but not the exact spot, a partial map taken from a dead man's boot, a captive who mentions it under pressure, an old letter in a ruined stronghold. The information is always incomplete. The hoard is always real.
>
> **Finding it requires:**
>
> - Knowing or narrowing the hex — a survivor's account, a landmark, a marking on a map fragment
> - A SCOUTING roll at the establishment difficulty (see table above)
> - Time: searching a hex takes one full Quarter Day per attempt
>
> The band that finds the hoard owns it. There is no inheritance in the Ravenlands.
>
> What a dead band's hoard contains is up to the GM. Some captains buried coin and weapons. Some buried things they wanted no one to trace back to them — goods that explain a massacre, documents that implicate a warchief, a bound and preserved head. Sometimes the hoard explains why the band died. A locked strongbox at the bottom of a cache tells a story if someone takes the time to open it.

---

## Section 6: Campaign Life

### Quarter Day Activities for the Band

The band uses the fellowship's Quarter Day structure. Each Quarter Day, the leader must account for:

- **March** — movement through the hex. Standard travel rules.
- **HUNT/FORAGE** — assign foragers to reduce food cost.
- **MAKE CAMP** — one Quarter Day per day required for a proper camp with a perimeter.
- **DRILL** — see below.
- **PATROL** — satisfies patrol contract terms for the day.
- **REST** — the band can rest one Quarter Day while encamped.

A _Skirmisher_ band (3-6 men) needs no dedicated logistics Quarter Day. A _Warband_ (7-20 men) needs one Quarter Day of logistics per day — provisioning, equipment maintenance, camp discipline. A _Company_ (21-50 men) needs two Quarter Days of logistics unless a STEWARD or a senior sergeant handles them; the PC-facing requirement drops to one check per day.

### DRILL

Spending a full day (two Quarter Days) in DRILL improves the band's readiness. After a week of consistent drilling, the leader may make a COMMAND roll (MANIPULATION, difficulty 2). On success, Common fighters count as trained for one full engagement sequence — they do not have to roll morale when casualties mount. After three successful full weeks of drilling, Veteran fighters gain +1 to their MELEE for the season.

Drilling requires a TRAINING GROUNDS (at the stronghold) or a dedicated drill field established during camp (one Quarter Day of labor, requires at least 40 WOOD, lasts the season).

### Camp Setup and Security

When the band makes camp, one person must STAND GUARD each Night Quarter (standard rule). With a Warband or larger force, two people must stand guard — one front perimeter, one back. If only one guards, the GM rolls SCOUTING at difficulty 2 for any threat that passes through.

**Fortified Camp:** Spending two Quarter Days with materials (50 WOOD minimum) establishes a fortified camp at this position. The camp functions as a Palisade (Defense Rating +1) for one week, after which it degrades unless maintained. A fortified camp allows the band to hold a hex as a temporary stronghold and reduces the effective threat from ambushes.

### Discipline and Punishment

Every company has rules. The printed ones go in a contract. The real ones live in what the captain will and will not take — and in what the sergeant does before the captain has to hear about it.

When a member of the band breaks a rule, commits a crime against another member, or refuses a direct order in the field, the captain or sergeant decides the response. There is no formal court. There is no appeal. This is not a kingdom with a magistrate. What justice exists in a mercenary company is the justice the captain is willing to enforce and the band is willing to accept.

**Offenses are weighted as follows. The GM determines whether a given act constitutes a Minor, Serious, or Capital offense based on circumstances.**

| SEVERITY | EXAMPLES                                                                                                                                                                                                                         | TYPICAL PUNISHMENT                                                                                          |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Minor    | Insubordination, skipping watch, petty theft from another member, starting a fight that ends without injury                                                                                                                      | Reduced share of next contract payment (half-pay for a week), or public reprimand before the assembled band |
| Serious  | Stealing a significant sum from another member, habitual lying that put others at risk, cowardice that cost the band blood, assault within the company, sexual violation against a member or civilian in a controlled occupation | Flogging (1D6 wounds, armor does not apply), demotion in rank, or expulsion                                 |
| Capital  | Betraying the contract or selling intelligence to an enemy, killing a fellow company member outside sanctioned duel, abandoning a position during active combat and causing deaths that follow                                   | Death, or permanent expulsion with a bounty posted under the company's name                                 |

**Carrying out sentence** requires the captain or sergeant — someone with standing in the company — to make the call, state it plainly in front of whoever is present, and follow through. A sentence stated and not carried out costs MORALE -1. Men will note that the rules have teeth only when it is convenient.

**Flogging** is the standard enforcement instrument for Serious offenses that the captain wants to punish without losing the man. The sentenced person takes 1D6 damage to STRENGTH with no armor reduction. They are not BROKEN by this unless the result equals or exceeds their remaining STRENGTH — but a close call is noticed, especially in front of others. Recovery follows standard wound rules.

**Duels** are a controlled alternative to informal violence. Two company members with a formal grievance may request a duel before the captain. The captain may permit it or forbid it. Duels are first blood by default. Both combatants fight to one BROKEN condition and stop — unless the captain rules differently. A man killed in an unsanctioned duel counts as a company murder.

**Expulsion** removes the man from the rolls, voids his pay claim, and forfeits any share of an active contract. The captain may additionally post a WANTED notice (see Section 8) if the offense was severe enough. Other companies may or may not honor it.

#### Tyrant Companies

Some captains run a company the way a man runs a dog — through pain and fear rather than coin and respect. MORALE in a tyrant company is held together by threat rather than by trust. The MORALE mechanics function the same way, but the interpretation changes.

A tyrant captain may substitute INTIMIDATION for MANIPULATION on all internal MORALE checks and discipline rolls. This works — until it doesn't. Track separately whether the band's MORALE is **Fear-Held** or **Trust-Held**:

- A **Fear-Held** band at MORALE 3 (Shaken) does not protest. It goes quiet. Individual Named Men begin pursuing private agendas and concealing information from the captain.
- A **Fear-Held** band at MORALE 2 (Wavering) will not break openly. It will leak — men leaving in the night, minor sabotage, no warning given when the situation turns.
- A **Fear-Held** band at MORALE 1 (Broken) does not dissolve in front of the captain. It dissolves behind them.

In a tyrant company, loyalty scores for Named Men decay at double normal rate when triggers are hit. Named Men with Loyalty 1 in a fear-held company will sell information and act against the captain's interest the moment they calculate it is safe. The calculation usually arrives before the captain expects it.

**Tyrant Punishments**

Tyrant captains use punishments designed to leave a mark — on the body of the offender and on the memory of everyone watching. These replace or supplement the standard punishment table at the captain's choice.

**Mutilation:** Used for offenses the captain wants recorded on the body. The severity scales with the offense. A first serious offense — theft, a lie that cost blood — earns a finger from the dominant hand: MELEE and MARKSMANSHIP reduced by 1 permanently, the stub visible to anyone who looks, recognized in settlements by traders and elders who have seen it before. Repeat offenses, serious treachery, or an example the captain needs to make without killing the man outright earn the full hand: dominant hand removed, MELEE capped at 1, no two-handed weapons, no tasks requiring both hands at full capacity. The man is kept. That is the point. He is alive because the captain chose it, diminished and marked and still present in the line every morning as a reminder to the others.

**Public execution of a company member:** The captain kills a member of the band — or orders it done — in front of the assembled company. No private sentence. No quiet removal. The body stays visible until the company moves.

This always triggers:

- MORALE -1 immediately, even in a fear-held company. Fear rises, but morale costs are real.
- Every Named Man present rolls against Loyalty. A Named Man at Loyalty 1 who fails this roll begins actively planning departure or betrayal.

The exception: if the executed man was openly despised by the band — a coward whose failure cost blood, a thief who stole from multiple members — the GM may waive the MORALE cost. The execution lands differently when the men already made the same calculation.

A captain who uses public execution more than once in a season will eventually face a band in which everyone is calculating odds. Some captains understand this and use it anyway. They have made a trade: immediate obedience now for a shorter future.

---

> **The Unofficial Rules**
>
> Every company has rules no one writes down. They are older than the captain, older than most of the men, and enforced by pressure and habit rather than stated expectation. Here is what companies actually deal with and how rough companies actually deal with it.
>
> **Theft between members** is the worst offense on the inside of a company. Worse than a fight, worse than lying to the sergeant, worse than sleeping through watch. A man who steals from the man who is going to stand next to him in a shield line has made a calculation about his own skin versus everyone else's, and that calculation does not have a good outcome for anyone. In most companies, a first offense earns a flogging and a reputation that follows the man until he leaves. A second offense earns expulsion. A third offense — if someone is still operating a third offense — earns whatever the men decide, and the captain looks the other way. This is not a policy. It is weather.
>
> **Lying that cost blood** — telling the sergeant the left flank was clear when it wasn't, claiming to have been on watch, swearing a civilian was hostile to justify a killing — is handled faster than most things. There is no standard punishment. There is a standard outcome: the captain and the sergeant hear what happened, from everyone who was there. After that, the liar's word does not travel well. What follows depends on what the lie cost.
>
> **Violence against a civilian in an occupation zone** is an atrocity under Section 9, but within the company it is also a problem of management. Men who commit it once and understand why it was wrong are men the company can keep. Men who commit it and do not understand why it was wrong are a liability that will eventually cost the company a contract, a settlement's standing, or a night ambush from twenty relatives. The sergeant handles the distinction.
>
> **Sexual violence against a civilian** triggers automatic atrocity consequences regardless of Standing. Within the company, the captain's response determines whether the company is the kind of company that can hold a contract in settled areas. Most captains who want repeat work from employers know this and respond accordingly. Some do not. Their companies have a type of reputation, and the work that finds that reputation is the work that deserves it.
>
> **Initiation** in rough companies is not formal. There is no ceremony. What happens is that new men are given the worst watch, the heaviest carry, the coldest corner of any camp, and the hardest assignments for the first two or three weeks. They are tested for the things that matter — do they hold, do they complain past the point where complaining is useful, do they lie about weakness to avoid work that will then fall on someone else. Men who pass are not told they passed. Other men start treating them differently. That is all.
>
> The hazing that exists beyond that boundary — targeted cruelty, sustained humiliation, deliberate injury — happens when the sergeant is weak or absent or complicit. It is not tradition. It is what bad management produces. A smart captain kills it fast, not because it is kind, but because a man who is being eaten alive by the men around him is not available to perform when it counts, and the man doing the eating is building habits that will cause a worse problem later.
>
> Every company has someone who thinks cruelty is a teaching method. Usually they have done it so long they cannot account for it. The sergeant who handles them early saves the captain a larger problem later.

---

### Optional: Arguments and Escalation

Use this subsystem when the band is under sustained pressure — unpaid, hungry, tired, or carrying fresh grief. Arguments happen. Most die in the air before they reach blood. Some drench in blood.

**Triggers — the GM may call for an argument when:**

- MORALE is 3 (Shaken) or lower at the end of a day
- Two Named Men share a Loyalty trigger overlap or directly competing Agendas
- The band has gone two or more days without pay, food, or rest
- A member died today and no one has spoken about it
- A direct order produced a bad outcome and the man who gave it is still giving orders

When a trigger fires, the GM picks or rolls for two participants. If one is a Named Man, use their personality to color the opening. If both are anonymous fighters, the argument starts below them — in the ranks — and may pull Named Men in.

**The escalation ladder:** Arguments move through stages in order. Each stage ends when someone intervenes, or when the next stage begins.

| STAGE | STATE         | WHAT HAPPENS                                                                                                             | INTERVENTION                                                     |
| ----- | ------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| 1     | Words         | Raised voices, accusations, old debts aired in front of the company.                                                     | MANIPULATION difficulty 1. A cool word or a hard look is enough. |
| 2     | Confrontation | One man stands up. Hands are on belts. Others are watching.                                                              | MANIPULATION difficulty 2. Or INSIGHT to find the real cause.    |
| 3     | Drawn Weapons | Steel is out. Everyone in camp has stopped what they were doing.                                                         | INTIMIDATION difficulty 2, or physical interposition (grapple).  |
| 4     | Blood         | Combat begins. First blood or BROKEN condition ends the fight — unless no one intervenes and rage runs ahead of caution. | No intervention roll. Stop the fight physically or let it end.   |

If the argument reaches Stage 4 without intervention, roll D6 after the fight ends. On a 1, one participant is dead — the blow landed wrong, someone's blade slipped. On a 2–6, the loser is Broken and the winner is standing over him. The captain now has a body or a badly broken man, neither of which is good for what comes next.

**MORALE cost by outcome:**

- Argument stayed at Stage 1–2, resolved: no cost
- Argument reached Stage 3, resolved without blood: MORALE -1 (the men saw it, they're thinking about it)
- Stage 4 with a Broken loser: MORALE -1, and both participants are unavailable that Quarter Day
- Stage 4 with a dead participant: MORALE -1, and apply the Death of a Member rules (see below)

**Named Men and arguments:** A Named Man involved in a Stage 3 or 4 argument who loses rolls against their Loyalty. On a failure, their Loyalty drops by 1 — whatever broke the surface is still working. A Named Man who wins a Stage 4 argument gains no mechanical benefit, but their standing in the company rises: the GM should treat them as more respected by anonymous fighters for the remainder of the season.

**Deliberate provocation:** A leader or Named Man may deliberately provoke an argument to draw out a rival's true loyalties or break a standoff between two factions in the band. This is MANIPULATION difficulty 3 — the difficulty of starting a fire without being seen as the one who dropped the torch.

---

### Optional: Blood Oaths

A blood oath is not a contract. Contracts can be breached for the right price. A blood oath is a spoken commitment made with open cuts, in front of witnesses, in a tradition that men in the Ravenlands understand is older than any warchief and older than most laws. Most men in the Ravenlands have never taken one. Most men in the Ravenlands would not break one.

Three kinds of blood oath are common in mercenary life:

**Brotherhood oath.** Two Named Men bind themselves to each other — not to a captain, not to a company, to each other specifically. They bleed into soil or water or fire. The oath is witnessed by whoever is present; the company does not need to be assembled, but usually is. The oath states plainly: I will not leave you behind, I will not lie to you in a matter of life, and I will stand over your body before I walk away from it.

Mechanics: If the oathbound partner is Broken in combat in the Named Man's presence, lied to by someone within earshot, insulted publicly, betrayed, or struck — the witnessing Named Man gains +2 to their next single roll made in direct response. This is typically MELEE against the offender, but it extends to INTIMIDATION if the response is a threat rather than a blade. It does not stack, it does not last beyond the response action, and it does not apply to anything other than the direct accountability for what was done. The men around them will recognize what it means when the bonus fires. It is not a combat advantage. It is evidence of what the oath cost.

A Named Man who has sworn brotherhood will not abandon their oathbound partner voluntarily. If a captain orders one to leave the other behind, the Named Man rolls against Loyalty. Any result means they hesitate one Round before following the order — that hesitation may be the thing that saves the partner or the thing that gets both killed, depending on the situation.

**Bounty oath.** The captain cuts their hand and swears before the band that this contract will be completed. It is done when the employer wants more than a handshake, when the target is dangerous enough that backing out would shame the band, or when the captain wants to communicate to their own men that this is not optional.

Mechanics: the band's Reputation in the employer's settlement increases by 1 for the duration of the contract — they are known to have sworn. If the band abandons the contract after swearing, Standing at that settlement drops by 3 and word travels. Other employers will hear that this band swore and walked. A captain who breaks a bounty oath more than once loses the ability to post or accept bounties in settlements where that reputation has arrived.

**Vengeance oath.** Sworn against a person or faction. Requires a wound, a name spoken aloud, and a reason. The oath states: this person — named, described, identified — has done a thing that cannot be paid for in coin, and I will see them dead. Witnesses are not required but are common.

Mechanics: the oathed party (individual or whole band if sworn collectively) gains a permanent +1 MANIPULATION when attempting to gather information specifically about the oath target. They will ask anyone. Men who have sworn a vengeance oath will not agree to a contract that requires protecting or allying with the target, regardless of pay. A Named Man who holds a vengeance oath and is ordered to stand down by a captain must roll against Loyalty to comply. On a failure, they comply for now and find another time.

**Breaking a blood oath** is not acceptable by tradition — yet some low men do it nonetheless. The cost is as follows:

- Any Named Man who witnesses the oath broken loses 1 Loyalty immediately.
- The oath-breaker's Reputation (Ch08) drops by 1 in any settlement that hears of it.
- A captain who breaks a brotherhood oath will find that no Named Man of quality will swear one with them again. The word travels slowly, but it travels.

No oath can be dissolved by agreement. That is the point of it. A man who wants out of a blood oath can only wait for the other half to die, or be released publicly by a witnessed statement from the other party. Some men choose to die rather than break an oath. Some captains consider that a waste. It depends on the company.

---

### Optional: Death of a Member — Distribution of Effects

When a company member dies — fighter, Named Man, or someone the band was traveling with — the company has to decide what happens to them before the day is done. A company that lets it sit past a day is a company with a brewing argument.

**Anonymous fighters:** Personal effects are pooled. The sergeant or whoever runs logistics divides usable gear back into company stores — armor, weapons, tools. Personal items with no tactical value (a carving, a letter, a child's tooth on a cord) are burned or buried with the body in most companies. What fits the stores goes to the stores. What doesn't goes in the ground.

Pay owed through the end of the current contract is distributed equally among the surviving members. This is traditional and expected. A captain who pockets a dead man's owed pay will find out how quickly that travels.

**Named Men:** The process is more deliberate. Before anything is touched:

1. Ask if the dead man named a recipient before the job. If he did, that person receives the primary weapon and any personal item of significance. No one argues with last words spoken in front of the company.
2. If no name was given, the primary weapon is offered first to whoever fought alongside them most — their partner in line, their regular watch-mate. Refusing the offer does not disqualify from receiving other effects. It means the weapon goes to the next in seniority.
3. Armor and secondary weapons go to the stores. A Named Man's personal weapon is not a company asset. His armor is.
4. Personal items with no combat value are assembled and burned or buried according to whatever practice the dead man held, if it was known. If not known, the company custom applies.

**Disputed items:** If two men both claim the same item and neither has a clearly stronger case, the sergeant makes the call. If no sergeant is present, MANIPULATION roll between the two claimants. The loser accepts it publicly or becomes a Stage 1 argument by the next Quarter Day. Or this becomes an Argument.

**Gambling debts to company members** die with the man. What he owed inside the company is voided. What he owed to outsiders is his family's problem, not the company's — unless the captain decides to honor them for reputation reasons.

**MORALE:** A company that settles effects quietly and fairly within the same day the man died suffers no additional MORALE penalty beyond the standard death cost. A company that bickers, delays, or allows a dispute to fester past a day costs MORALE -1 on top of any death-related loss already applied. Men can absorb death. They cannot absorb the ugliness that follows it.

**Named Man's recorded effects:** If the GM has been tracking a Named Man's specific gear — a weapon with a name, an artifact, an unusual item — those should be noted at creation, not improvised at death. A Named Man who has carried a particular blade for two seasons and dies in the third should have an accounting ready. It makes the death land harder and the distribution matter more.

---

## Section 7: Named Men

Named men are veteran fighters with individual stats, names, personalities, and loyalty scores. They are not anonymous soldiers. They have opinions, histories, and lines they won't cross. They are also the band's most dangerous problem when things go wrong.

### Creating a Named Man

Assign each of the following. For personality, roll or choose from **Named Man Personalities** below.

- **Tier:** Veteran or Elite (determines stats, see below)
- **Role:** Their fighting specialty (Line, Skirmisher, or Brute — shapes attributes and skill emphasis)
- **Loyalty:** 1, 2, or 3
- **Trigger:** The thing that will break their loyalty
- **Agenda:** What they want beyond pay

Named Men are tracked individually. Record their stats on a separate NPC sheet. They are not anonymous soldiers — they can be Broken, recover, advance, and die in ways that matter to the story.

### Attributes

Each tier provides a base attribute array. Pick the role that fits the character or roll D6.

**VETERAN** (D6: 1–2 Line, 3–4 Skirmisher, 5–6 Brute)

| ROLE       | STR | AGL | WIT | EMP | NOTES                                |
| ---------- | --- | --- | --- | --- | ------------------------------------ |
| Line       | 4   | 3   | 3   | 2   | Standard soldier. Holds a position.  |
| Skirmisher | 3   | 4   | 3   | 2   | Fast. Harasses flanks, scouts ahead. |
| Brute      | 5   | 3   | 2   | 2   | Hard to kill. Carries heavy weapons. |

**ELITE** (D6: 1–2 Line, 3–4 Skirmisher, 5–6 Brute)

| ROLE       | STR | AGL | WIT | EMP | NOTES                                     |
| ---------- | --- | --- | --- | --- | ----------------------------------------- |
| Line       | 5   | 3   | 3   | 3   | Tested veteran. Reads a fight quickly.    |
| Skirmisher | 4   | 5   | 3   | 2   | Dangerous alone. Hard to corner.          |
| Brute      | 6   | 3   | 3   | 2   | Uncommonly powerful. Other men give room. |

WIT and EMP matter. Named Men can be manipulated, persuaded, rattled by FEAR attacks, and may recover from WITS damage in ways anonymous soldiers cannot. Use these stats whenever a Named Man is directly confronted, interrogated, or targeted by social pressure.

### Skills

All Named Men begin with their tier's MELEE. Then choose additional skills from the Field Skills Pool below.

**MELEE** — Veteran 2, Elite 3. Not optional. This is why they are worth naming.

**Field Skills Pool** — choose from these only:

| SKILL           | ATTRIBUTE | TYPICAL ROLE          |
| --------------- | --------- | --------------------- |
| ENDURANCE       | STR       | Any — marching, cold  |
| MIGHT           | STR       | Brute, Line           |
| MARKSMANSHIP    | AGL       | Skirmisher            |
| MOVE            | AGL       | Skirmisher, quick men |
| STEALTH         | AGL       | Skirmisher, Scout     |
| SCOUTING        | WIT       | Patrol work           |
| SURVIVAL        | WIT       | Field craft           |
| INSIGHT         | WIT       | Sergeant material     |
| MANIPULATION    | EMP       | Sergeant material     |
| HEALING         | EMP       | Band medic            |
| ANIMAL HANDLING | EMP       | Mounted, beast work   |

**How many additional skills:**

- Veteran: choose 2 from pool, each at skill level 1
- Elite: choose 3 from pool; may raise one to skill level 2

**Role guidance:** A Skirmisher who carries a ranged weapon must take MARKSMANSHIP from the pool — a high AGL score does not substitute for the skill when using bows or crossbows. Without MARKSMANSHIP, the Named Man can only make base attribute rolls for ranged attacks, which is insufficient at Veteran tier and unacceptable at Elite. A Skirmisher without MARKSMANSHIP is a scout or flanker, not a shooter; adjust their equipment accordingly.

### Talents

Named Men carry only general talents. They do not have profession paths or kin paths unless the GM has a specific reason. Assign from the **Mercenary Talent Pool** below.

- Veteran: 1 talent, rank 1–2
- Elite: 2 talents, rank 1–3 each

**Mercenary Talent Pool**

These are the talents common among hired fighters of the Ravenlands. Talents not on this list require the GM to have a clear rationale — a Named Man who once served a mage's guard might carry COLD-BLOODED; a Named Man who grew up raiding from horseback might carry HORSEBACK FIGHTER. The list is not a hard wall, but it is the expected range.

_Close combat — weapon style_

| TALENT               | MAXIMUM RANK FOR NAMED MEN | NOTES                   |
| -------------------- | -------------------------- | ----------------------- |
| AXE FIGHTER          | Veteran 2, Elite 3         |                         |
| HAMMER FIGHTER       | Veteran 2, Elite 3         |                         |
| SWORD FIGHTER        | Veteran 2, Elite 3         |                         |
| HEAVY WEAPON FIGHTER | Veteran 2, Elite 3         | Brute role only         |
| KNIFE FIGHTER        | Veteran 2, Elite 3         | Common secondary talent |
| SHIELD FIGHTER       | Veteran 2, Elite 3         | Line only               |
| INSIDE THE GUARD     | Veteran 1, Elite 2         | Skirmisher only         |

_Combat style_

| TALENT         | MAXIMUM RANK FOR NAMED MEN | NOTES                                                            |
| -------------- | -------------------------- | ---------------------------------------------------------------- |
| BERSERKER      | Veteran 1, Elite 2         | Requires a rage- or fury-based personality                       |
| BRAWLER        | Veteran 1, Elite 2         | Preferred by men who grew up fighting without weapons            |
| COLD-BLOODED   | Veteran 1, Elite 2         | Executioner types; will not coexist with a Civilian Harm trigger |
| DIRTY FIGHTING | Veteran 1, Elite 2         | Street-origin fighters                                           |
| EXECUTIONER    | Veteran 1, Elite 2         | Requires willingness to end surrendered foes                     |
| FIRM GRIP      | Veteran 1, Elite 2         | Grapplers, those who disarm well                                 |
| PAIN RESISTANT | Veteran 2, Elite 3         | Common. The ones who stayed when others broke.                   |

_Combat support_

| TALENT             | MAXIMUM RANK FOR NAMED MEN | NOTES                                       |
| ------------------ | -------------------------- | ------------------------------------------- |
| COMBAT EXPERIENCED | Veteran 1, Elite 2         |                                             |
| DEFENDER           | Veteran 1, Elite 2         | Shield bearer or rear-guard type            |
| FEARLESS           | Veteran 2, Elite 3         | The man the others look at when it gets bad |
| LIGHTNING FAST     | Veteran 1, Elite 2         | Skirmisher role only                        |

_Ranged and mounted_

| TALENT            | MAXIMUM RANK FOR NAMED MEN | NOTES                            |
| ----------------- | -------------------------- | -------------------------------- |
| FAST SHOOTER      | Veteran 1, Elite 2         | Crossbow or bow only             |
| HORSEBACK FIGHTER | Veteran 1, Elite 2         | Only if the Named Man is mounted |

_Command (sergeant only)_

| TALENT | MAXIMUM RANK FOR NAMED MEN | NOTES                                           |
| ------ | -------------------------- | ----------------------------------------------- |
| LEADER | Elite 1                    | Named Men with Loyalty 3 and Sergeant rank only |

### Equipment

Equipment determines a Named Man's fighting reach and silhouette in play. It follows from role.

| TIER    | ROLE       | PRIMARY WEAPON                   | SECONDARY       | ARMOR                     |
| ------- | ---------- | -------------------------------- | --------------- | ------------------------- |
| Veteran | Line       | Sword or spear + shield          | Knife           | Chainmail (Armor 4)       |
| Veteran | Skirmisher | Short bow or crossbow            | Short sword     | Leather (Armor 3)         |
| Veteran | Brute      | Two-handed axe or heavy club     | —               | Chainmail (Armor 4)       |
| Elite   | Line       | Sword + shield, or war axe       | Knife, dagger   | Chainmail (Armor 4)       |
| Elite   | Skirmisher | Crossbow + short sword and knife | Throwing knives | Leather or light mail (3) |
| Elite   | Brute      | Great sword, great axe, or maul  | Short sword     | Chainmail (Armor 4)       |

An Elite in a leadership role (Sergeant) may wear plate if the band is prosperous (Armor 5). This is a mark of achievement — the men will note it.

### Sergeant

A Named Man elevated to Sergeant is the leader's operational right hand. Designation requires:

- Loyalty 3
- Veteran or Elite tier
- Recognized by at least half the band (no formal roll required; the GM determines when this condition is clearly met)

A Sergeant gets one additional benefit:

- When the leader is absent, the Sergeant makes MANIPULATION rolls on behalf of the band for routine discipline and protest resolution. Use the Sergeant's own MANIPULATION, not the leader's.
- When the leader is present, a Sergeant with LEADER rank 1 may spend WP as per that talent to support MORALE checks.
- A Sergeant's death always triggers a MORALE check, regardless of current MORALE level.

### Three Quick-Builds

These are ready-to-play Named Men for GMs who do not want to build from scratch. Adjust names and personalities freely.

---

**THE LINE MAN** _(Veteran, Loyalty 2)_
STR 4, AGL 3, WIT 3, EMP 2
Skills: MELEE 2, ENDURANCE 1, SURVIVAL 1
Talent: PAIN RESISTANT rank 1
Armor: Chainmail (4) | Weapon: Sword + shield
Trigger: Left behind when wounded
Agenda: Enough coin for a small house somewhere quiet
_Appearance: Short, broad, no expression left. Has stopped explaining himself._

---

**THE SKIRMISHER** _(Veteran, Loyalty 2)_
STR 3, AGL 4, WIT 3, EMP 2
Skills: MELEE 2, MARKSMANSHIP 1, STEALTH 1
Talent: KNIFE FIGHTER rank 1
Armor: Leather (3) | Weapon: Crossbow + short sword
Trigger: Ordered to harm civilians
Agenda: A private enemy they want dead — they'll do it themselves if the band gets close
_Appearance: Moves quietly. Always has a second knife no one sees until they need it._

---

**THE BRUTE** _(Veteran, Loyalty 1)_
STR 5, AGL 3, WIT 2, EMP 2
Skills: MELEE 2, MIGHT 1, ENDURANCE 1
Talent: BERSERKER rank 1
Armor: Chainmail (4) | Weapon: Great axe
Trigger: Consistently spoken of as ignorant or beneath notice
Agenda: To build a name worthy of being remembered
_Appearance: Large. Wears an old scar across the chin like it won an argument. Usually did._

---

**THE SERGEANT** _(Elite, Loyalty 3)_
STR 5, AGL 3, WIT 3, EMP 3
Skills: MELEE 3, MANIPULATION 1, INSIGHT 1, ENDURANCE 1
Talents: FEARLESS rank 2, LEADER rank 1
Armor: Chainmail (4) | Weapon: War axe + shield
Trigger: Not elevated in rank when clearly more capable
Agenda: Respect — not coin, not land, but to be seen as the kind of man others follow
_Appearance: Not the biggest. Just the one standing when the others aren't._

### Loyalty Score

| LOYALTY | MEANING                                                                                     |
| ------- | ------------------------------------------------------------------------------------------- |
| 3       | Trusted. Will not betray the band short of a direct command to do something they refuse.    |
| 2       | Reliable. Will leave or act out if their trigger is hit; will not actively harm the band.   |
| 1       | Self-interested. Will take coin elsewhere, sell information, or remain neutral in a crisis. |

Loyalty changes over time:

- +1 if the leader demonstrates genuine regard for the named man's wellbeing (healing their wounds, honoring their victory publicly, clearing a debt for them)
- -1 if their Trigger is triggered and the leader does nothing to address it
- -1 per MORALE step the band falls below 3, each week

### Named Man Triggers

Roll D6 or assign:

| D6  | TRIGGER                                                                  |
| --- | ------------------------------------------------------------------------ |
| 1   | Ordered to harm civilians, especially children or the defenseless        |
| 2   | Not elevated in rank when clearly more capable than the current sergeant |
| 3   | A specific kin or people they will not raise arms against                |
| 4   | Left behind or abandoned when wounded                                    |
| 5   | Consistently spoken of as ignorant or beneath notice                     |
| 6   | Witness to the leader taking more than their promised share of plunder   |

### Named Man Agendas

Every Named Man wants something beyond pay. Roll D6 or pick:

| D6  | AGENDA                                                                        |
| --- | ----------------------------------------------------------------------------- |
| 1   | Enough coin to buy back a family member who was enslaved or ransomed          |
| 2   | A particular enemy killed — their own private war                             |
| 3   | To learn a craft skill or talent from someone in the fellowship               |
| 4   | To build a name worthy of being remembered when they die                      |
| 5   | Land or a house — a place of their own                                        |
| 6   | Something they lost: an heirloom, a title, a piece of truth they need to hear |

The leader can invest in an agenda — helping a named man pursue it — and in return gain a bonus to MORALE (+1) when it succeeds and a bond that raises loyalty.

### Named Man Personalities

Mercenaries are not broken men waiting to be healed. They are functional people shaped by years of violence, moral compromise, and self-preservation. Roll D12 or assign:

| D12 | PERSONALITY                                                                                                                                 |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Flat** — Does not react to blood, screaming, or death. Eats during the aftermath.                                                         |
| 2   | **Calculating** — Counts everything: exits, weapons, faces, who is looking where. Never unprepared, never comfortable.                      |
| 3   | **Scornful** — Finds weakness faintly amusing. Will help, for the right price, and will say so plainly.                                     |
| 4   | **Cruel Practical** — Uses suffering as a tool. Not sadistic — does not enjoy it unless it serves something.                                |
| 5   | **Territorial** — Their gear, their cut, their space. Challenge any of it and they will not forget.                                         |
| 6   | **Dark Amused** — Makes jokes about things others will not name. Laughs at violence. This is just what they are.                            |
| 7   | **Paranoid Competent** — Assumes betrayal will come and plans for it. Usually right about the first part.                                   |
| 8   | **Convincing Liar** — Tells the truth when convenient. Cannot always tell the difference anymore.                                           |
| 9   | **Grudge-Holding** — Has a private list. Wrongs do not age out. They wait. Will say they've forgotten.                                      |
| 10  | **Mercenary Proud** — This is their profession and they take it seriously. They resent men who don't.                                       |
| 11  | **Death-Easy** — Settled their account with dying long ago. Makes them fearless in ways that look like madness.                             |
| 12  | **Quietly Violent** — Does not threaten. Does not argue. When the moment comes, they act before anyone else has decided the moment is here. |

### Named Man Advancement

After any engagement resulting in a clear victory, roll D6 for each Named Man who fought:

- On a 6: they gain +1 to one stat (player's choice, within reason — MELEE or STRENGTH)
- On a 5: they develop a new habit or trait (add to personality)
- On a 1: they took a wound that matters. Roll on the critical injury table.

---

## Section 8: Wanted Men

### Acquiring a Price on Your Head

Any member of the band — PC or Named Man — can become wanted. Common sources:

- A posted bounty after a crime or contract breach
- A surviving enemy with resources and a grudge
- A settlement whose Standing was destroyed
- A warchief whose stronghold was burned

**Wanted rating:** Track the coin amount of any bounty. Higher amounts travel further via rumor and reach more opportunistic ears.

| BOUNTY          | SPREAD                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| Under 5 silver  | Local only. Known in the posting settlement and two hexes out.                                               |
| 5–20 silver     | Regional. Reaches any settlement connected by trade road or river within 5 hexes. Hunters may take interest. |
| 20–100 silver   | Wide. Mercenaries and bounty seekers anywhere with Reputation access may hear it within a season.            |
| Over 100 silver | Famous. The name travels with every caravan and rumor for a year. Even allies may be tempted.                |

### Effect of Being Wanted

At any settlement within spread range, the GM may have one or more of the following happen:

- Gate guards ask pointed questions about identity
- An innkeeper sends word to whoever posted the bounty
- A competing band takes a contract to bring in the wanted person
- A Named Man with Loyalty 1 considers whether they are safer selling the information

Having a high enough personal Reputation can counteract this: people who know and respect the fellowship are less likely to turn them in. Standing at the specific settlement matters most.

### Sheltering Wanted Men

If the fellowship shelters a wanted band member, they absorb reputational exposure. Anyone helping a wanted man stands to inherit the bounty's scrutiny. A settlement that discovers this may demand surrender of the wanted person or penalize Standing by -1 to -2.

If the leader publicly harbors the wanted person and the settlement knows it, the bounty's spread now includes that stronghold in its circle.

### Clearing Wanted Status

Same as clearing a contract grievance:

1. **Restitution** acceptable to the grantor — and the grantor must still be alive and reachable
2. **Killing or discrediting the grantor** — eliminates the legal basis. Does not stop private revenge.
3. **Time** — reduce effective spread by 1 tier per season the bounty goes uncollected
4. **Outliving your pursuers** — if no collection attempt is made in one year and the grantor has not renewed interest, the bounty is considered cold. It exists but does not actively spread.

---

## Section 9: Atrocities

An atrocity is an act that crosses a visible line — visible enough that it defines what the band is known for. The Forbidden Lands is harsh and life is cheap, but even in this setting, some acts rupture something. Villages burn. Captives die begging. People who should have been ransomed are killed for the fun of it. Children disappear. These acts leave marks that gold does not scrub off.

### Defined Atrocities

| ACT              | DESCRIPTION                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| Massacre         | Killing non-combatants — workers, villagers, the wounded, the surrendered                |
| Burning          | Destroying a settlement's means of survival: homes, granaries, livestock                 |
| Ransom killing   | Executing a captive who had been accepted for ransom, or who surrendered expecting mercy |
| Slave-taking     | Taking free people by force and selling or keeping them                                  |
| Breaking an oath | Violating a sworn agreement before witnesses, especially one made before the gods        |
| Treachery        | Killing an ally, turning on a contract employer, betraying inside knowledge              |

### Immediate Consequences

When an atrocity occurs:

1. **Standing crash:** Every settlement within rumor range of the act loses 2 Standing with the band, or drops to -3 if they were allies. Settlements with direct survivors drop to -4 or -5.

2. **Reputation spread:** The act travels through the rumor system as a recognized fact, not hearsay. GMs may treat it as a piece of the band's Reputation that precedes them wherever they go. This does not require a roll — it happens.

3. **MORALE check:** Unless the men benefited materially (see below), the band must check MORALE. Ordered massacres with no apparent gain reduce MORALE by -1. A Named Man with Loyalty 2 or 3 may state they will not repeat it. A Named Man with a civilian-harm Trigger must be tested.

4. **Bounty:** Anyone with standing and motive can post a bounty within a season of the act. Villages destroyed in an atrocity can be assumed to have survivors in neighboring hexes who will spend years carrying the story forward.

### Plunder and the Dark Arithmetic

If the atrocity came with material gain — livestock taken, valuables looted, labor captured — MORALE may rise rather than fall, at least in the short term. This is the design's honest acknowledgment of how those situations work. However:

- Short-term MORALE gain from atrocity plunder does not offset the Reputation consequences
- Named Men with humanity-based Triggers still check loyalty regardless of plunder
- The long-term Standing damage compounds across settlements. What paid for one good week creates obstacles for the next year.

Tracking both effects simultaneously is the design intent. The system does not moralize. It accounts.

### Oath-Breaker Status

Repeat contract breaches, betrayals, and broken oaths accumulate into an OATH-BREAKER flag. Once a band has broken three oaths on record (as heard through Reputation), any MANIPULATION roll to negotiate a new contract takes -2 difficulty. Any settlement elder or warchief who knows the flag will not hire them without extraordinary assurance, usually collateral.

The flag can be reversed by publicly honoring a particularly costly obligation — one where keeping the oath demonstrably hurt the band. This is the only mechanism.

---

## Section 10: Integration Points

### Stronghold Defense Rating

GUARDS hired at the stronghold continue to function as described in Ch09. Merges can happen: when the band returns home, their fighters may be assigned to GUARD duty at the stronghold, contributing to its Defense Rating under the unit points formula (Strength × 3 + MELEE + talent rank sum ± armor delta from 7; average common soldier ≈ 15 points). This transition — field band to stronghold garrison and back — is how strongholds grow into real military forces.

### Reputation Cascade

The band's deeds — contracts completed, atrocities committed, bounties earned — all travel through the Ch08 Reputation system. The band does not have its own Reputation score separate from the fellowship's. Their name is the fellowship's name. Every deed adds to or subtracts from the same pool of stories people carry across hexes.

A stronghold's Reputation radiates outward via hire relationships. If the band was hired by a settlement, that settlement knows the fellowship's name and passes it forward. If the band burned that settlement, neighboring settlements know that too.

### Feud Track

If the band operates in contested hunting ground, the FEUD TRACK rules (Ch08 optional rules) apply to any hex they operate in belonging to a village. A mercenary band hunting in a claimed hex without negotiation advances the track as if it were a rival hunting party, because it is. Armed men eating game belonging to a village is not a neutral act.

### Talent Integration

**PATH OF THE COMMANDER (Ch04):** This is the existing answer to the band leadership problem. A PC who has taken PATH OF THE COMMANDER at any rank may substitute PERFORMANCE for MANIPULATION on band MORALE checks. At rank 3, when they grant an immediate melee attack to allies per the talent, Named Men may be included as eligible targets if they are within the command radius and the leader has direct line of sight and voice. At rank 5, the Sergeant need not be present to relay orders — the conditioning carries on the men's own initiative for that round.

A band leader without PATH OF THE COMMANDER uses MANIPULATION as written. PATH OF THE COMMANDER adds depth, not replaces. A PC need not have it to lead a band.

**MASTER OF THE HUNT:** A fellowship member with this talent can reduce the band's daily food cost by assigning themselves as head forager. Their special trap clause (from proposal-hunting-season-weather-realism) allows traps to work while the band drills in camp.

**COLD-BLOODED:** Fellowship members with COLD-BLOODED do not trigger MORALE penalties from ordered atrocities. Named Men are unaffected — their loyalty is independent.

---

## Section 11: New Stronghold Function Suggestion

### WAR ROOM

A dedicated space for planning field operations — maps, intelligence reports, messenger routes.

✦ **REQUIREMENT:** TOWN HALL, SCRIPTORIUM
✦ **RAW MATERIALS:** 200 STONE, 100 WOOD
✦ **TOOLS:** Saw, hammer
✦ **TIME:** 2 weeks
✦ **REPUTATION:** +1
✦ **EFFECT:** When planning a field contract from this location, the leader may make one LORE roll (at difficulty 2) to learn one piece of material information about the target hex or NPC — troop strength, patrol timing, material value — before the job begins. A SCRIBE automatically succeeds with one ⚔️. Also allows the band leader to leave standing orders with a STEWARD that trigger under named conditions (enemy of specific type arrives / payment from specific party — act accordingly).

---

## Section 12: Serving in Another's Company

Most fellowships come to mercenary life as commanders. They form a band, name it, take contracts, carry the weight of keeping it fed and paid. Some start from below.

A fellowship without coin or reputation, newly arrived in a contested hex, or looking for work that teaches before it kills, may sign on under an existing captain. They eat the company's food. They sleep where the sergeant points. They fight when ordered and hold their opinions until asked.

This section governs that arrangement. It is not a lesser version of mercenary play. The view from the bottom of a company is different — the politics are smaller and more immediate, the dangers are the same, and the captain makes decisions the fellowship must live with. The rules that follow handle how the fellowship earns rank, what rank costs and grants, and how they leave when the time comes.

The mode works best as a bridge. Three or four sessions under another captain's orders gives scope for a richer transition to leading a band of their own. It also builds history: the fellowship will know what a working company looks like, what breaks one, and who, in the company, they actually want to keep.

### Terms of Service

A company takes on new men at the captain's discretion. The fellowship makes contact through an inn, a gatepost posting, a referral from a settlement that knows the company's name, or direct approach at the company's camp. If the captain is selective, the GM may call for a MANIPULATION roll (difficulty 1–2, based on how badly the company needs hands) before any terms are offered.

Signing terms:

- **Daily wage** (see rank table below)
- **Duration:** season, named contract, or open-ended
- **Exclusivity:** the company's contracts take priority over fellowship-owned contracts while the term runs
- **Standing orders** (see table below) — these predate the fellowship and apply from the first day

**Standing Orders**

Every company has rules that settled before you arrived. Roll D6 or choose:

| D6  | STANDING ORDER                                                                                                                 |
| --- | ------------------------------------------------------------------------------------------------------------------------------ |
| 1   | No killing prisoners without the captain's word. Ransoms belong to the company, split by the purser.                           |
| 2   | What you take in the field you keep. What a contract employer pays is split by rank and time served.                           |
| 3   | No drinking the night before a march. The sergeant enforces this.                                                              |
| 4   | Every man sleeps with something sharp within reach.                                                                            |
| 5   | Disputes between members settle by agreement or by the sergeant's word. No blood between company members on pain of expulsion. |
| 6   | Two men through any door, first and last. Never one alone.                                                                     |

The fellowship is subject to standing orders immediately. Breaking one is not grounds for punishment the first time. The captain notes it. The second time, the sergeant speaks to them directly.

### Rank in the Company

Entry rank depends on demonstrated history. A fellowship with no known record enters at FRESH. A fellowship that presents a credible history of engagements may enter at BLADE. The GM decides; the fellowship makes the case.

| RANK        | ENTRY CONDITION                                                                | PAY/DAY  | AUTHORITY AND USE                                                                                                          |
| ----------- | ------------------------------------------------------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| FRESH       | First contract, no record                                                      | 1 silver | None. Takes every order from anyone ranked BLADE or higher.                                                                |
| BLADE       | Fought through at least two engagements and returned. The company has seen it. | 1 silver | May speak at company council. May be assigned a single task detachment.                                                    |
| NAMED       | Carries a call name (see below).                                               | 2 silver | May lead scouting, flanking, or small detachments of 3–5 men. Assigned own unit.                                           |
| TENSMAN     | Commands a unit of ten through a full contract.                                | 3 silver | MANIPULATION rolls for their unit's minor discipline. Handles the unit's daily assignments.                                |
| SERGEANT    | Commanded a section through hard fighting and kept it together.                | 4 silver | May substitute their own MANIPULATION for the captain's on section-level MORALE checks.                                    |
| FIRST BLADE | The captain's right hand. There is only one at a time.                         | 8 silver | Full authority short of overriding an active contract. Leads the company if the captain is absent, incapacitated, or dead. |

**Advancing in Rank**

Rank advances when the fellowship demonstrates the thing that rank requires — leading when the leader is down, keeping a section together when it falls apart, seeing what others miss and acting on it. The captain makes the call. The fellowship may request promotion with a MANIPULATION roll at difficulty 1; if the captain believes the demonstration was genuine, they agree. If not, they say so plainly.

Rank given under pressure or by extraction feels like neither rank nor respect. Player characters who want to matter in the company earn it.

### The Call Name

Companies rename their men. The name in the ledger is for counting the dead and split the purse. The name used on a march, across a burning position, or when someone needs to move — that one gets earned.

A call name is granted when two conditions are both met:

1. A deed was witnessed by at least three company members and is agreed to be worth remembering.
2. At least one Named Man or higher sponsors the name — vouches for it in front of whoever is present.

The name that sticks is not always the one the person would choose. It comes from what they did, how they look, where they came from, something they said once, or something they survived. The player proposes a name after the deed; the GM shapes it based on what actually happened in play.

A call name travels. Settlements that know the company may know the name before they know the face. Reputation rolls involving the company carry the call name as well as the fellowship's own.

**Call Name Table** — for reference or direct use at the table:

| D20 | CALL NAME      |
| --- | -------------- |
| 1   | Twice          |
| 2   | Old Rook       |
| 3   | Coldhand       |
| 4   | Boot           |
| 5   | Shepherd       |
| 6   | The Questioner |
| 7   | Saltmarch      |
| 8   | Ironback       |
| 9   | One-Ear        |
| 10  | Cutter         |
| 11  | Pale           |
| 12  | Ember          |
| 13  | The Nail       |
| 14  | Dust           |
| 15  | Long Bone      |
| 16  | Winter         |
| 17  | The Teacher    |
| 18  | Ghost          |
| 19  | Goat           |
| 20  | The Lamp       |

The GM may adapt: Twice-Broken, Cold-Eye, The Half, Long-Shepherd, Pale Winter. The words are raw material, not fixed names.

---

> **GM Advice — Running the Captain**
>
> Make the captain someone who is often right. Not a tyrant waiting to be removed. Not a mentor waiting to validate the fellowship.
>
> The captain leads this company because they have done it longer than anyone here and most of them are still alive. Their orders look wrong when they are given. They tend to look correct when the fighting starts. Build at least two decisions that work this way — where the fellowship's objection was reasonable but the captain knew something they didn't — before you put the captain in a position where the fellowship can justifiably go against them.
>
> Give the captain one thing they want that is not the contract. A debt they are working down. A person inside the company they are protecting. A war they are steering quietly around the edge of. When the fellowship discovers what that is, the entire relationship changes.
>
> Use the Named Men from Section 7 for the captain's inner circle. Give each one a Loyalty score and a Trigger. When Named Men trust the fellowship enough to speak privately, they will say things about the captain that no one says out loud. Those conversations are the company's real history, and they are more interesting than any contract.
>
> If the captain dies or is removed, do not hand command to the fellowship automatically. The succession of a captaincy is the most dangerous moment in a company's life. The First Blade has prior claim. What they do with it — and whether the Named Men follow — is the scenario.

---

> **Player Advice — Finding the Game at the Bottom**
>
> You are not in charge. You carry your gear, you eat what the cook makes, and you sleep where the sergeant indicates. That is not a limitation on the session. It is the opening condition of a different kind of play.
>
> The game here is in the people. You have time to learn who is in this company — the sergeant who gives harsh assignments because it is the only way to keep fresh men alive, the First Blade who says less than anyone and moves decisions in ways you cannot track until you have been here long enough to watch, the cook who is older than the captain and knows things neither of them will say. Push into that web. Ask the wrong questions. Make small alliances before you understand why they matter.
>
> Your call name is a rumor engine. Before you had one, you were new blood in someone else's company. After it, you are a story. Named Men will have opinions about that story before they have formed an opinion about you. Use the gap.
>
> Rank is satisfying to earn here precisely because no one gives it to you. The captain does not hand out promotions. You do the thing, someone witnesses it, and later the sergeant states your new rank the way they would state a weather condition — flat, permanent, done. That is how it feels in a real company, and it should feel that way at the table.

---

### Disagreeing with Orders

The captain gives orders. The fellowship may find those orders wrong, dangerous, against what they will do. The game does not flatten this.

**Options when an order is received:**

- **Comply** — no roll. Whatever follows is the company's consequence and the fellowship shares it.
- **Object** — MANIPULATION roll, difficulty 1. On success, the captain listens and explains their reasoning; they may not change the order, but they will not hold the objection against the fellowship. On failure, the captain notes it. Two failed objections from the same person earns a warning.
- **Refuse openly** — no roll. The company records the refusal. The fellowship member is treated as insubordinate until they leave or the captain releases the obligation. Other Named Men may adjust their behavior toward them.
- **Act against the order** — the fellowship does the opposite. If the outcome clearly benefits the company, they may roll MANIPULATION difficulty 2 afterward to explain it; the captain may reconsider or, in rare cases, promote. If the outcome costs the company, this is contract breach under Section 5. The captain does not forget it.

### Leaving the Company

At the end of a contracted term, the fellowship departs cleanly. No roll. The captain may offer new terms; the fellowship declines or negotiates as they choose.

Departing in the middle of an active contract is breach. Section 5 covers breach consequences. The captain's Standing at nearby settlements determines how far the grievance travels.

**Mutiny** is forced succession. It requires:

1. Three or more Named Men — including at least two PCs — willing to publicly challenge the captain
2. A witnessed triggering event: an atrocity, a catastrophic failure, a clear oath-break by the captain
3. A MANIPULATION roll by the senior mutineer at difficulty 3, opposed by the captain's own MANIPULATION

On success: the captain is removed — imprisoned, exiled, or killed, as the company decides. The senior mutineer assumes command. If that is a PC, the company transitions to the PC-led model from Sections 1–6. The previous captain's active contracts, their known grievances, and their Standing at settlements — all of it transfers to the new leadership, positive and negative alike.

On failure: the mutiny collapses. Each Named Man who participated rolls Loyalty immediately. The captain will purge the ringleaders. A PC who was the senior mutineer faces expulsion, a bounty, or worse, depending on what blood was shed in the attempt.

---

## Acceptance Summary

These changes are interdependent. Sections 1–6 (band formation, morale, pay, provisions, extortion and tribute, contracts) are the core and should be accepted together. Section 4 (village extortion) can be deferred if the campaign does not involve coercive play against settlements, but it ties the band economy to the Feud Track and should not be omitted from a full implementation. Sections 7–8 (Named Men, wanted status) layer onto the core and can be added separately. Section 9 (atrocities) is self-contained and adds the moral accounting layer. Section 10 requires no changes — it documents integration with existing systems. Section 11 is a new stronghold function and requires only the War Room text. Section 12 (Serving in Another's Company) is standalone — it can be accepted or omitted entirely independent of all other sections.

| #   | CHANGE                                    | LOCATION                     | DEPENDENCY        |
| --- | ----------------------------------------- | ---------------------------- | ----------------- |
| 1   | Band formation + size tiers               | Ch09 (new section)           | None              |
| 2   | Morale system                             | Ch09                         | 1                 |
| 3   | Fighter tiers + recruitment               | Ch09                         | 1                 |
| 4   | Pay, provisions, field non-payment        | Ch09                         | 1, 2              |
| 5   | Village extortion and tribute             | Ch09 + Ch08 cross-reference  | 1, 2, 3, 4        |
| 6   | Contracts and bounties                    | Ch09                         | 1                 |
| 7   | Campaign life (QD activities)             | Ch09                         | 1, 2              |
| 8   | Named Men system                          | Ch09                         | 1, 2, 3           |
| 9   | Wanted status                             | Ch09 + Ch08 cross-reference  | 6                 |
| 10  | Atrocities                                | Ch09 + Ch08 cross-reference  | None (standalone) |
| 11  | Integration section                       | No text changes — notes only | All above         |
| 12  | War Room function                         | Ch09 functions table         | Independent       |
| 13  | Serving in Another's Company (Section 12) | Ch09 (new optional section)  | Independent       |

Changes 1–7 together form the minimum viable play loop. Without morale and pay pressure, mercenary management is just hirelings with extra paperwork. The atrocity rules (10) are standalone and can be brought in at any time.

---

## Fiction Preview

The following is a prose sample for the chapter opening or a sidebar. It is in the manuscript voice and subject to the writing standard from `WRITING_GUIDE.md`.

---

> _"The problem with twenty armed men," said the woman who later became known as the Torch Carrier, though not as a compliment, "is that they need to eat every day. The problem with twenty hungry armed men is your problem."_

Mercenaries are not hirelings. A hireling tends to what you own. A mercenary is a force you direct toward a problem and hope comes back pointed the right way. Give him shelter and coin and the job stays simple. Miss a payment, let the job go wrong, give him a reason to look at you like a problem — and the calculation changes.

The Ravenlands has no lack of men who would rather fight than farm. The wars that broke the world threw them up like silt. They are real fighters, most of them, scarred and practical and capable of the things fighters do. They will hold a position or clear a hex or ride hard to a burning village if that is what the contract asks. They will eat their share and sleep in what shelter they find and complain about both.

But they are not loyal to a cause. They are loyal to what the cause pays, and to the man who stands in front of them when things go badly, and to the kind of work that lets them come back alive.

Earn that, and you have a band. Lose it, and you have twenty men deciding whether to walk off or do something worse.

---

### Band Life — Extended Fiction

The band eats first. Before the captain decides the march route, before the sergeant counts the watch rotation, before anyone puts a coin on a contract table — the band eats. Sixteen men need a full quarter-day's worth of food every morning, and sixteen hungry men are not sixteen men. They are sixteen separate calculations happening in sixteen heads, and every one of those calculations ends the same way. This is what a new captain learns in the first week.

The next thing they learn is the march. Twenty miles in fair conditions. Fourteen in rain. Half that in the mud season, when the tracks between villages turn to brown channels and the men's boots rot through from inside. The Ravenlands does not have roads. It has the memory of roads — raised lines, old stone courses, paths that pre-Cataclysm carts used and that feet still find by instinct. Walk one long enough and you will find where it was cut by something that came up through the ground, or where the forest closed back in over twenty years, or where the bridge is now a rotten tangle three feet downstream from where it was built.

---

They camp inside daylight margins. Not from discipline — from arithmetic. The Mist still pools in low places after dark, thicker than air, heavier than fog, and men caught walking in it do not come back. The band has old soldiers who will tell you the worst of it lifted with the demon lords, that a man can walk two miles in it on a clear night and come through fine. Those are the same men who sleep with a knife across their chest and one boot on. Old habits from before they knew better, they say. Then they pull their fingers tight around the hilt and say nothing more.

So the camp goes up before the light goes red. Fire first, then perimeter. A guard on the tree-line who lasts two hours before the cold makes him useless, then another guard, until dawn. Not because the captain orders it every night. After the third week, the men do it without being told. Fear is a better instructor than command, and the Ravenlands has never run short of fear.

---

A village sees them from half a mile. A hamlet will have someone up a tree before the band clears the wood-line. By the time the captain reaches the palisade gate or the elder's door, the goats have been moved twice and three men with iron are standing somewhere they can be seen. This is not hostility. It is memory.

The villages that survive in the Ravenlands are the ones that learned to count strangers before the strangers counted them. Sixteen swords is larger than most villages can answer, and every elder between here and the Stillmist knows that the coin minted before the Cataclysm goes further in a mercenary's hand than in any other. Their silver is old. The faces stamped on it are kings who died before the grandfathers of these elders were born. The men carrying it have needs that a village cannot fill and places to spend it that a village farmer will never see, and when the captain speaks at the door the elder standing opposite them is calculating how much the village can give before winter becomes a problem worse than the band is.

Most bands do not start with extortion. Most start with an honest demand and a reasonable number. But the arithmetic of sixteen hungry men against an elder who cannot feed them for three days without gutting the stores — that arithmetic closes fast. The captain who has not thought through what happens when it closes is the captain who finds out the hard way.

---

Inside the band, the social weight runs separate from rank. The sergeant holds authority. The captain holds coin and contract. But there is a third thing — harder to name — that lives in the man others look at when the situation turns bad. He is not always the sergeant. He is not always the biggest man. He is the one whose face does not change when the calculation gets ugly. The others do not discuss him. They do not vote for him. Over time, when trouble starts, they face the same direction he does. After a season, that direction is the one they trust.

Bands that lose that man — to injury, to a clean desertion, to a contract that went wrong — feel the loss before they understand it. The morale holds until the first test. Then it does not hold.

---

The ones who last in this work are not the strongest or the fastest. They are the ones who never needed anyone to tell them that sleeping rough is fine, that cold food is fine, that the reward for doing the job correctly is getting to do the job again. They came from farms that burned or families that starved out or villages that could not feed one more mouth through the white months. They are practical in every way except the one that counts: they keep coming back.

They are not unlike the first settlers who pushed into the Stillwood or up through the Blight Marshes when the Mist was still thick and no one had reason to believe any of them would return. Those men and women went because staying was also a kind of dying, and because the land beyond the hills did not ask them what they had done before they arrived. The band offers the same thing. Whatever you were before you signed — the empty field, the dead village, the name that now means nothing in a settlement that burned six years ago — the band does not care. You can march. You can hold a position. You eat when the food is there and you do not complain when it isn't. That is enough.

Ask one of the old ones why they stay. They will name a figure — enough coin to get somewhere, enough to clear a debt, enough to buy land if the price stays honest. Push harder and the figure gets vague. Push harder still and they stop answering. The truth is that most of them could not say what they are marching back toward. They know how to do this. They know who the men around them are, which ones hold and which ones don't, where the next meal is and how far to the next village. That is a kind of certainty. Out there — beyond the contract, beyond the march, in the life they are supposedly saving toward — there is none.

The Ravenlands does not reward the man who stops.

---

## Open Questions

**✅ 1. COMMAND talent:** Resolved. PATH OF THE COMMANDER (Ch04) is the existing hook. Section 10 now defines how PC leaders with any rank in that talent substitute PERFORMANCE for MANIPULATION on MORALE checks, and how the higher ranks extend into Named Man coordination. No separate COMMAND talent is needed.

**⏸️ 2. Large-scale warfare:** Deferred. This proposal handles bands up to ~50 men. Armies, sieges, and coordinated multi-stronghold campaigns require a separate system. The Host tier (51+ men) flags the boundary but does not solve it. That system, if built, should treat this proposal's output as its atomic unit: a Host is several Warbands, not a different kind of thing.

**✅ 3. Mercenary archetypes by kin:** Resolved. Kin recruitment modifiers are now in Section 2 (Recruitment and Quality) as a table. Elf, Dwarf, Halfling, Wolfkin, Orc, and Goblin each carry specific mechanical note. Notes were kept narrow — modifier to the settlement roll only, not permanent stat effects.

**✅ 4. Named Man death and gear distribution:** Resolved. The Death of a Member — Distribution of Effects optional subsystem (Section 6) covers gear, pay, disputed items, gambling debts voided, and MORALE consequences. The process for anonymous fighters and Named Men is differentiated. What remains open: if a Named Man dies close to completing their Agenda, no rule specifies what happens to that Agenda — whether another Named Man can inherit it, whether it generates a narrative debt, or whether it simply closes. Flag for integration pass.

**Open questions:**

1. **Named Man promotion to PC-adjacent role:** Can a Named Man with sufficient advancement be given a full character sheet and played as a temporary PC if their original character is out of action? The current advancement rules (Section 7) touch this but do not resolve the full transition. A Named Man who has gained multiple stat increases, developed a clear personality, and completed their Agenda may deserve a more formal path into the fellowship if both player and GM agree. Low priority — this is a GM call in practice — but a one-paragraph ruling would prevent table confusion.

2. **Band reputation vs. fellowship reputation:** The proposal uses the fellowship's Reputation as the band's. This works for small bands but breaks down if the band operates independently for a season while the PCs are elsewhere. A band that commits atrocities while the PCs are absent should not automatically collapse the fellowship's Reputation. Consider a secondary **Band Notoriety** track that runs parallel to fellowship Reputation and can diverge — linked by the fellowship's name but capable of accruing its own consequences. Defer unless Band Notoriety is needed in play.

3. **Band downtime at the stronghold:** The proposal handles field operations but does not define what a Named Man does when the band is home between contracts. Section 10 notes that field fighters can be assigned to GUARD duty (Defense Rating contribution), but the transition is not mechanized. Specifically: does the BARRACKS cover Named Men as well as common guards? Can Named Men be assigned to stronghold functions during downtime? Requires a brief ruling before integration.

4. **MORALE 5 label collision:** The label "Hungry" for MORALE 5 — meaning eager and dangerous — collides with the HUNGRY condition in Ch05. Rename before integration. Candidates: **Keen**, **Sharp**, **Primed**. Pick one and propagate through the MORALE table, MORALE TRIGGERS table, and any section that references the state by name.

5. **Acceptance table is out of date:** The table in the Acceptance Summary reflects the original section structure. The following have been added and are not yet listed: kidnapping rules (Section 5), mercenary hoards + dead band sidebar (Section 5), expanded forager table with coverage math (Section 3), and the three optional subsystems in Section 6 (Arguments and Escalation, Blood Oaths, Death of a Member — Distribution). Update before integration review.

6. **Optional subsystem grouping:** The three Section 6 optionals are individually marked "Optional" but carry no guidance on running them together vs. separately. Blood Oaths requires a campaign long enough for Named Men to form meaningful bonds — a short campaign gains little from it. Arguments and Escalation and Death Distribution are self-contained and work from the first session. A brief note in the section header recommending which optionals to enable in which campaign contexts would prevent tables enabling Blood Oaths in session one and wondering why it never fires.

7. **Brotherhood oath bonus magnitude:** The current text grants +1 to the reactive roll. Confirm this is correct before integration — in a single-die-pool system, +1 is meaningful but not dominant. If the design intent was higher, update before final text lock.

8. **Unintentional captive death:** The kidnapping rules specify that executing a captive after accepting ransom is an Atrocity. A captive who dies through neglect — starvation, untreated wounds, exposure — is not addressed. Clarify whether unintentional death triggers the Atrocity consequence (probably yes, on a reduced scale) or requires deliberate intent. The distinction has contract and MORALE implications.
