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

> **The Host: Multiple Bands Under One Banner**
>
> A Host is not a single band grown large. It is several bands — each with its own leader, its own MORALE, its own Named Men — assembled under a single authority called the **Warmaster**.
>
> The Warmaster may be a PC or a Named Man elevated from the ranks. More often, they are an external figure: a warchief, a lord's marshal, a faction commander, or a wealthy employer who has retained multiple companies for a siege or campaign. The Warmaster holds the Host's banner, controls the supply line, and gives operational orders to the band captains. They do not manage individual men. They manage leaders.
>
> Full Host mechanics — band-level tracking, the Warmaster's authority and alignment, and supply across multiple bands — are in **Section 13: Host Play**.

### MORALE

MORALE is a single score from 1 to 5 tracked for the whole band. It is not a character attribute — it belongs to the band.

| MORALE | STATE    | EFFECT                                                                     |
| ------ | -------- | -------------------------------------------------------------------------- |
| 5      | Keen     | Men are eager. +1 to band MELEE rolls in first round of any engagement.    |
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

**RURAL MOB**
Farmers, woodcutters, and hunters who ran out of land or watched it burn. They know the wilderness, they are unafraid of cold and hunger, and they have no illusions about what the work is. Most started because someone raided their village and the choice was stay and die or leave and fight. The core of this band is usually a single village or hamlet — men who grew up together, buried their dead together, and trust each other the way people trust what they have tested.

- **Recruitment:** +1 to finding men at rural settlements. The captain takes anyone from the home village or hamlet who can hold a weapon and is willing. Strangers are considered on a longer timeline — they must eat with the men for several weeks and be vouched for by someone already in the band before they are treated as part of it. A new man who fits the crowd is accepted without ceremony. A new man who does not fit may never be trusted regardless of skill.
- **Strengths:** FORAGING rolls improved — treat one additional terrain type as favored when foraging. Comfortable camping in poor conditions; -1 to food cost when encamped in wilderness terrain. The band is **Trust-Held** by default (see Trust-Held Bands, Section 6).
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
- **Strengths:** DRILL time is halved — the band reaches trained status after three days of drill rather than a full week. Common fighters hold formation in the second round of an engagement without a MORALE check. Sergeants in this band promote to full authority one engagement sooner than the standard rules require. Logistics are maintained precisely; the band never accidentally runs short through poor tracking. A military band that has maintained consistent pay and kept its captain's word for a full season is **Trust-Held** (see Trust-Held Bands, Section 6). A military band that has not yet met that threshold runs on professional exchange — not fear, not trust.
- **Weakness:** Pay expectations are higher and non-negotiable. A military band at Steady MORALE expects full pay on schedule; a single late payment triggers a check at +1 difficulty rather than the standard threshold. They also have opinions about the captain's decisions and will not hide them.
- **Typical Named Men personality:** Mercenary Proud, Territorial, Quietly Violent.
- **Breaks when:** The captain shows they do not understand what a real formation is, or when the job clearly has no professional merit — atrocities, reckless assault, abandonment of standards.

**KIN BAND**
All members share blood, clan, or kin heritage. An orc warband. A wolfkin pack. Three halfling brothers who picked up stragglers of the same kin over two seasons. The loyalty structure runs through blood and old obligation rather than through coin and contract. These bands do not behave like mercenary companies in the standard sense — they behave like extended families who have become dangerous.

- **Recruitment:** Same kin only, by default. A family-based kin band (same bloodline, not just same kin type) will not accept outsiders at all without a vouch from at least one existing member and, in some cases, a formal bond or oath before the group. An outsider vouched in is treated as kin-adjacent — they have standing but not full blood standing, and the band will not extend them the same protections automatically. A man who is vouched for and then betrays the band is an example made of without debate. Use the Kin and Recruitment modifiers from Section 2.
- **Strengths:** MORALE is checked at -1 difficulty when the cause of distress is external (enemy action, contract failure, hunger). Internal grievances are handled within kin tradition — the GM should develop 1–3 kin-specific honor rules that function as additional Triggers for Named Men in this band. The band is **Trust-Held** by definition — kin bands cannot be Fear-Held except by a captain from outside the kin who takes command by force, and that condition lasts only until the kin remembers what they are (see Trust-Held Bands, Section 6).
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

> **Example:** Dain moves his company of thirty out of forest cover and into hill country on day two of a contract. He assigns six men to forage each morning. The table returns 13 FOOD. The company needs 30. The gap — 17 — comes from the provision sacks. Dain's sergeant meets him at the evening fire on day three and shows him the count: two days of stores left. They turn back toward the forest or they start losing men to a CONDITION before they reach the target.

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

> **Example:** Pell's warband of nine has been in the Stillmere hills for ten days. The employer's factor was due on day eight. Pay day comes and Pell has nothing to put on the table. He rolls D6 and gets a 4 — the sergeant Maret confronts him in front of the assembled men. Pell rolls MANIPULATION against difficulty 2: four dice, two ⚔️. He holds the line. The men accept it for now. Next pay day is not a matter of explanation.

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

> **Example:** The elder of Varbeck hands over a man called Galt — compact, a white scar below the ear, says nothing on the road north. He was not convinced. He was sold to keep the rest of the village housed through winter. His Loyalty starts at 1. He holds formation, reports accurately, eats what he is given. But when Pell fails to post a full watch on the third night, Galt counts the distance to the nearest tree line and says nothing about it to anyone.

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

### Finding Work

Public bounties and open patrol postings find the band on their own. Posted at inns, gate-keeps, and markets, they are available to anyone who asks. A MANIPULATION roll in a settlement of Reputation 3 or higher turns up current local postings. Three or more ⚔️ reaches regional postings carried by travelers who have passed through in the last week.

Private contracts — from warchiefs, trade consortium factors, fortified-settlement headmen, and similar people of actual force — do not post themselves. The employer controls the door. The band must either earn an introduction or arrive with enough standing that the employer has a reason to open it.

**Getting an audience:**

| APPROACH                                                                                  | REQUIREMENT                                                         |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| The band's Reputation is 4+                                                               | Automatic. They know who you are.                                   |
| A letter of introduction from someone the employer trusts                                 | No roll. The door opens on the introducer's Standing.               |
| Completed a contract for this employer before (Allegiance 1+)                             | No roll. The relationship already exists.                           |
| The band demonstrated visible recent capability (cleared a hex, ended a threat nearby)    | MANIPULATION difficulty 2 to convert that into an invitation.       |
| Cold approach by a band with Reputation 3                                                 | MANIPULATION difficulty 3.                                          |
| Cold approach by a band with Reputation 1–2, or OATH-BREAKER flag visible to the employer | MANIPULATION difficulty 4. Most employers decline without a reason. |

Failure does not close the door forever. The employer is occupied, not hostile. The band can return when their Reputation or recent deeds give them a better argument.

**Negotiating terms:**

Once the audience exists, the leader makes a MANIPULATION roll to settle terms. The base difficulty is set by the employer's standing:

| EMPLOYER TIER                                      | DIFFICULTY |
| -------------------------------------------------- | ---------- |
| Village or settlement elder, local headman         | 1          |
| Merchant factor, lesser warchief, consortium agent | 2          |
| Powerful warchief, regional faction representative | 3          |
| Major sovereign power, fortified city ruler        | 4          |

On a success, the leader's proposed terms are accepted, adjusted only by what the employer can supply. Each ⚔️ beyond the first earns one concession: a higher advance payment, a shorter exclusivity window, a liability clause removed. On a failure, the employer's terms stand. The band may accept them, attempt a second negotiation at the next available meeting at -1 difficulty, or withdraw.

A band at Allegiance 2 or higher with this employer reduces the terms difficulty by 1.

### Allegiance

A band that completes several contracts for the same employer becomes something more than a market hire. The employer has seen how they work. The band knows what the employer values. That history costs something and buys something.

Track **Allegiance** (0–4) per significant employer.

**Gaining Allegiance:**

- +1 after completing a contract in full, within its terms, without breach

**Losing Allegiance:**

- −1 for any breach of terms during an active contract
- −1 for abandoning an active contract
- −2 for accepting a direct competitor's contract while at Allegiance 3 or higher
- Resets to 0 if the band commits an atrocity against this employer's settlements or holdings

**Allegiance levels:**

| LEVEL | NAME     | ACCESS AND BENEFIT                                                                                                                         | CONSTRAINT                                                                                  |
| ----- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0     | Unknown  | None. Cold approach required.                                                                                                              | —                                                                                           |
| 1     | Known    | Audience automatic. The employer remembers the name. No other benefit.                                                                     | —                                                                                           |
| 2     | Favored  | Supply at employer's settlements at cost, no markup. Terms negotiation difficulty −1.                                                      | —                                                                                           |
| 3     | Retained | Above, plus Standing +1 at all settlements the employer controls. The employer's name deflects minor third-party threats against the band. | Taking a competitor's work is a breach (−2 Allegiance immediately).                         |
| 4     | Sworn    | Above, plus employer covers one advance payment per season without a posted contract. Safe passage through their territories.              | Exclusive. Any competing contract resets Allegiance to 0 and Standing behaves as GRIEVANCE. |

Allegiance 3 is a commitment the employer also carries. If they ask the band to act against the band's clear interest — destroy a settlement where the band holds Standing, contravene a Named Man's Trigger — the band may refuse and hold Allegiance 3 without penalty. The employer finds another force. Neither party calls it a breach. Allegiance 4 has no such buffer: sworn service means the employer's wars are the band's wars until the oath ends.

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

Any person, settlement, or faction with coin or goods can post a bounty. A bounty is an offer: kill this person, capture this person, return this stolen item. The bounty amount is paid on delivery. Bounties are posted at inns, gateposts, markets, and wherever men gather to sell their services.

**Posting a bounty requires:**

- A settlement or stronghold to anchor it (the bounty lives there)
- The payment — coin, goods of agreed value, or a combination — available upfront or guaranteed by a backer who can make it good on delivery
- A description clear enough for someone to act on it

**Finding bounties:** Any PC making a MANIPULATION roll in a settlement of Reputation 3+ may ask about current bounties. One ⚔️ finds the local postings. Three ⚔️ turns up bounties from the broader region, carried by travelers.

**Accepting a bounty:** No roll required. The PC accepts the task; the coin or goods are held — coin sometimes literally in a locked box at the inn, goods under the custody of the posting settlement or a third-party guarantor — until delivery or confirmed kill.

#### Bounty Types and Reference Prices

Bounties come from grievance, necessity, or calculation. A man whose son was killed in the street posts out of grief for whatever the family can scrape together. A trade consortium posts out of commercial logic: the road needs to be clear, and hiring someone to clear it costs less than losing caravans. A warchief posts out of calculation — eliminating a named enemy is worth more than whatever is written on the notice.

Silver is the Ravenlands' working currency. Gold moves at the level of warchiefs and lords and appears occasionally in old hoards; a common farmer may have held three silver coins in his life and is unlikely to have held gold at all. All prices below are in silver. When a poster's grievance is large and their liquid coin is not, see Payment in Goods.

The prices below are floors. Below those floors, experienced collectors do not leave camp. A desperate poster goes higher. A pooled posting from multiple aggrieved parties can go considerably higher than any single contributor could manage alone.

**Grievance bounties** arise from personal offense: humiliation, theft, injury, abandonment of debt or obligation. The price reflects the harm as the poster understands it, filtered through what the poster can actually put up.

| OFFENSE                                                                       | MINIMUM PRICE | NOTES                                                                                                                                                |
| ----------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fled a small debt                                                             | 1–3 silver    | Barely above the cost of tracking. Usually posted to attach the debtor's name to a public notice rather than to recover much coin.                   |
| Theft of livestock or tools                                                   | 2–5 silver    | Typically the stolen goods' value. Doubles when the thief is identified by name and destination.                                                     |
| Desertion from a garrison or company                                          | 2–5 silver    | Corporate discipline posting. Rarely spreads past two hexes — it signals internal problems and most captains know it.                                |
| Assault resulting in lasting injury                                           | 3–8 silver    | Posted by the victim's family. Scales with the injury: a cracked rib is 3, a severed finger is 8.                                                    |
| Fled a serious debt — a season's wages or more                                | 8–20 silver   | The loss plus the insult of the escape. The number climbs if the debtor is heard to be doing well somewhere else.                                    |
| Dishonoring a kinsman — fled before settlement                                | 5–12 silver   | A family's own price on a personal offense. Poor families post what they have. Proud families post more than they can afford.                        |
| Murder of a commoner, no witnesses of standing                                | 5–15 silver   | Higher when the dead had family with resources behind them. May sit uncollected for a year and still draw interest locally.                          |
| Arson — barn, granary, workshop, or home                                      | 8–20 silver   | Posted by whoever held the thing that burned. Often pooled when a single fire touched more than one household's livelihood.                          |
| Murder of a recognized community figure — craftsman, merchant, council member | 10–25 silver  | The settlement posts it as a body, not as a family. An elder commits the settlement's formal funds. The coin is real and the settlement is watching. |

**Professional breach bounties** arise when a mercenary, escort, or contractor broke a specific obligation that involved advance payment, sworn service, or trusted access to money, cargo, or intelligence.

| BREACH                                                                        | MINIMUM PRICE        | NOTES                                                                                                                                                     |
| ----------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Abandoned a contract after taking advance pay                                 | Advance paid + 50%   | The advance plus the cost of the signal. The extra 50% is not the employer's greed. It is the market price of warning other employers what this man does. |
| Sold intelligence to an opposing party                                        | 10–30 silver         | Posted by the employer. The amount reflects how much damage the leak caused, or how much the employer thinks it did.                                      |
| Escort who abandoned cargo or left the employer to die                        | Equal to cargo value | If the cargo was lost, the posting matches the loss. If the employer survived, the posting is the insult's price.                                         |
| Named Man who turned on their own company                                     | 10–30 silver         | The captain posts it. A low number says the man was not much to begin with. A high number says the captain wants blood rather than warning.               |
| Captain who delivered a false-strength company — contracted twelve, sent five | 5–15 silver          | Low end, because the embarrassment matters as much as the silver. Posted more for the story it tells than the money it might recover.                     |

**Elimination bounties** target individuals whose removal has political, regional, or commercial value. These travel the farthest and draw the most professional interest.

| TARGET                                                       | MINIMUM PRICE | NOTES                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A known bandit working a specific road section               | 3–8 silver    | Road safety restores trade. Multiple merchants may pool the posting without coordinating.                                                                                                                                               |
| A Named Man responsible for a specific killing or attack     | 8–20 silver   | Scales with the severity of the attack. Rises when the survivors' families add to a standing pool over time.                                                                                                                            |
| A small company captain who terrorized a village             | 15–40 silver  | The village posts what it has. May run partially to goods when coin runs out. The settlement's desperation usually exceeds its liquid resources.                                                                                        |
| A company captain responsible for an atrocity                | 20–75 silver  | Regional posting, backed by multiple affected settlements naming themselves as parties. Often pooled over months.                                                                                                                       |
| A specific military officer, enforcer, or rival's right hand | 25–80 silver  | Posted by a warchief's enemies or a commercial consortium. The poster generally has the resources to back the number they write.                                                                                                        |
| A warchief's named direct enemy                              | 50–200 silver | Spreads with every caravan and rumor in the region. Professional hunters may divert active contracts for it. Always comes with political strings: the poster has a side, and delivery implicates the collector in that side's business. |

**Recovery bounties** attach to stolen or missing objects rather than persons. The price is always tied to the item's actual value. A poster who understates that value gets no takers.

| ITEM TYPE                                       | MINIMUM PRICE               | NOTES                                                                                                                                                        |
| ----------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A specific horse, ox, or breeding animal        | Equal to the animal's value | A sound horse is 8–12 silver. Post less and no one follows the tracks.                                                                                       |
| Merchant goods, tools, or locked strongbox      | Equal to the contents       | A stated estimate that proves incorrect at delivery generates a new grievance where the old one used to be.                                                  |
| Land deed, contract, or legal document          | 5–25 silver                 | The value is what the document controls. Difficult to price honestly because the poster does not want to explain their business. Most post high.             |
| Personal heirloom with no market price          | 2–10 silver                 | The poster's own valuation. A low number signals poverty, an unsentimental relationship with the thing, or both.                                             |
| Sacred or ritual object belonging to a kin band | 5–15 silver                 | Kin bands post these regardless of silver equivalence. May supplement with goods when the object's importance exceeds any coin figure and the band knows it. |

#### Payment in Goods

A village that wants a company captain dead may not have 30 silver. It may have 30 silver's worth of things: grain in the storehouse, a horse, a house standing empty since the family buried the last person who lived there, a working boat, the right to cut timber from a specific stretch of forest. Goods payment is common when the poster's grievance is serious and their liquid coin is not.

Goods payment is always negotiated before the bounty is accepted. The collector must understand what they are taking before they agree to the work. A bounty accepted on the basis of goods promised and not yet transferred is a contract built on trust rather than iron.

**What goods can constitute payment:**

| GOODS                                                                                                  | SILVER EQUIVALENT                         | NOTES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A riding horse, broken and sound                                                                       | 20–30 silver                              | Riding-trained and healthy. Liquid — easy to sell or ride. The most useful goods payment for a band that does not stay in one place. A green (untrained) horse moves for 12–15 silver; a war-trained horse for 60–80 silver. Verify condition and training before accepting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| A mule or pack donkey, working                                                                         | 4–8 silver                                | Carries heavy gear without the temperament or expense of a horse. Eats less, works harder on steep and broken ground, and does not bolt from blood the way a riding animal does. A band moving equipment and loot over rough terrain values a sound mule above its coin equivalent in most seasons. A donkey toward the low end; a working mule in good condition toward the high. Not fast. Worth it.                                                                                                                                                                                                                                                                                                                                                        |
| A plow ox, working and healthy                                                                         | 8–12 silver                               | High value in the right settlement. Difficult to move over rough terrain without slowing whoever is transporting it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| A breeding pair of pigs or a small sheep flock                                                         | 3–6 silver                                | Only practical if the collector has somewhere to keep them. Most often taken as part of a split payment alongside coin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| A cart with draft harness                                                                              | 10–18 silver                              | A two-wheel flatbed with single harness: 10–12 silver. A four-wheel cargo wagon with full double harness: 14–18 silver. A working cart turns the band into a mobile operation — it carries the injured, the loot, and the weight that drags on backs over long marches. The harness is useless without a draft animal; the animal loses half its utility without the cart. Offered together with an ox or mule, the combination is the most durable mobile goods payment a settled village can make.                                                                                                                                                                                                                                                          |
| A working river boat, two- to four-oarsman capacity                                                    | 12–20 silver                              | Useful to a band that moves along waterways. Requires the collection point to be accessible to water.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| A quality weapon, master-made — axe or spear                                                           | 6–18 silver                               | Immediately useful to a fighting band. Axes and spears at this tier: battleaxe or long spear, master-worked, 6–18 silver. A master-made sword runs higher: broadsword or shortsword quality, 14–22 silver; a longsword or two-handed sword, 25–50 silver. Verify the poster holds clear title before accepting. A weapon with a known dead prior owner attached to it is not payment; it is evidence.                                                                                                                                                                                                                                                                                                                                                         |
| A full suit of chainmail, fitted and intact                                                            | 20–28 silver                              | Worth taking if the band needs it and has someone who can wear it. New chainmail runs 24 silver; used but intact, assume 20–28 silver depending on wear and whether fitting is required. Dead weight if no one in the band can use it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| A winter's grain store, enough for one family                                                          | 4–8 silver                                | Useful to a stationed band. Spoils over time — poor payment for a band that moves every few weeks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| A saltbox — fifty units, dry-packed and sealed                                                         | 8–14 silver                               | Salt preserves meat, cures hide, and cleans wounds. Fifty units sealed in barrels or oilcloth runs 8–14 silver depending on how far the settlement sits from any coast. Lighter than grain, longer-keeping than most stores, and tradeable at every market that has a butcher or a tanner. Verify the seal before agreeing: wet salt is half the stated value.                                                                                                                                                                                                                                                                                                                                                                                                |
| A season's harvest yield, unharvested at time of posting                                               | 5–12 silver                               | Forward goods. The collector receives the harvest when the season turns. Requires trust that the harvest will happen and the poster will still be present and willing to honor the agreement when it does.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Timber rights to a specified forest section, one full season                                           | 8–18 silver                               | The right to cut and sell from a marked territory. Only practical for a band that has the labor to work it, or a contact who will buy the standing timber.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Hunting, trapping, and fishing rights in a defined territory, one season                               | 6–14 silver                               | The poster grants access — marked territory, agreed season, no interference from the settlement or its neighbors. A well-stocked hunting ground within a day of a trade route: 10–14 silver in meat and pelt, if the band has someone who knows how to work it. A stripped forest or depleted river stretch: 6 silver at most. Not transferable coin. A band with a hunter or trapper on its rolls treats this as a standing food supply. A band without one treats it as a gift that requires labor to unwrap.                                                                                                                                                                                                                                               |
| Local knowledge — terrain maps, danger positions, and patrol routes                                    | 8–25 silver equivalent                    | A settlement that has survived ten years in one place knows things no outsider can buy: where the bandits shelter in winter, which passes close before the first snow, how the local lord's patrol runs, where the old road still holds firm under the mud. Paid as time with the settlement's elders and scouts — one to three days of questions, listening, and sketched maps. Specific current intelligence on a hostile faction's positions and movements: 18–25 silver equivalent. Safe-route guidance to the next settlement: 8–12 silver equivalent. Worth more entering unfamiliar territory than it is to a band already working the ground.                                                                                                         |
| Letters of safe conduct and guided passage through the poster's territory                              | 5–20 silver equivalent                    | The poster writes and seals a letter declaring the band under their protection and free to pass unmolested through lands they control or have standing with. A local guide accompanies them — someone who knows the roads, the checkpoints, and the names to drop at each one. Without the guide, the letter is paper. Without the letter, the guide is goodwill. Together they open territory that coin by itself cannot buy. In settled, friendly land: 5–8 silver equivalent. In contested ground bordering a hostile power or a toll-heavy lord's roads: 15–20 silver equivalent.                                                                                                                                                                         |
| A house, outbuilding, and clear lot in a small village                                                 | 50–100 silver                             | Immovable. The materials alone for a solid wood structure run 20–40 silver; the outbuilding, cleared lot, and established claim in a living settlement add the rest. A rubble-condition structure in a dying hamlet moves for 20–30 silver and is worth what it shows. The band gains a legal presence in that settlement by accepting it. Valuable if the band wants roots; worthless if it intends to keep moving.                                                                                                                                                                                                                                                                                                                                          |
| A working smithy forge with tools and iron stock                                                       | 80–160 silver                             | The most expensive single-item payment short of a longhouse. A forge requires 60 units of iron in its construction alone — 60 silver at floor price — before the stone, the builder's labor, and the working tools. A forge with cold iron stock and a functional hearth is worth what it costs to rebuild. The band must have a smith on its rolls or someone who can hire one, or it accepts dead weight. The poster is offering part of what the settlement runs on; do not underestimate what that means when the settlement cannot rebuild one.                                                                                                                                                                                                          |
| A working craft building with tools — tanner, carpenter, cooperage, or equivalent                      | 30–70 silver                              | A tanner's shed or carpenter's workshop: 200 WOOD plus the specialist tools (scrapers, saw, chisel, planes, finishing tools), two to four days of labor. The tools alone run 5–15 silver for a complete working set. A tannery adds vat-pits and salt infrastructure. Upper range for a well-equipped cooper or wheelwright in a functioning settlement. Worth nothing to a band without a tradesman on its rolls or a buyer who will pay fair value on the purchase.                                                                                                                                                                                                                                                                                         |
| A guild house — meeting hall, locked store, and charter rights                                         | 100–200 silver                            | Not a building — a position. A guild house is the structure plus the charter rights: the recognized authority to hold meetings, set prices, exclude rivals, and enforce the trade rules within the settlement's commercial life. Those rights take years of negotiation to accumulate; they are not surrendered except under genuine collapse. The structure itself runs INN-scale or larger. The band that accepts one inherits standing, outstanding debts, and a list of rivals who want what it just acquired. A poster offering a guild house is either desperate or making someone else's problem disappear.                                                                                                                                            |
| A longhouse in a fortified settlement                                                                  | 100–250 silver                            | A significant stake. The longhouse structure itself — 400+ WOOD or equivalent stone — is only part of the cost. Space inside a fortified settlement is scarce and contested; what the poster is giving away is a position, not just a building. The band becomes a stakeholder in the settlement's politics, the settlement gains armed men inside its walls, and neither party chose the other. The lower range applies to a modest hall in a smaller palisaded camp. The upper range applies to an established longhouse with storage, a hearth, and a recognized claim in a real fortified town.                                                                                                                                                           |
| A cleared farming plot with established soil and a standing claim                                      | 50–120 silver                             | A worked field is not raw ground. Raw ground takes a month of labor with a plough — 5 IRON in materials, a smith's week in making — to break into something that grows. What the poster is selling is soil already broken, seeded, and drained, with a boundary the neighbors have acknowledged. That prior labor does not become worthless because the holder is pressed. Contested in practice: the Ravenlands run on presence and living memory, not written deeds. The band must be able to hold what it accepts.                                                                                                                                                                                                                                         |
| An herbalist or healer in attendance for an agreed term                                                | 12–20 silver equivalent per tenday        | The settlement's working healer — a HEALER talent holder, a practiced herbalist, or a senior midwife with real field knowledge — accompanies the band for the agreed term. Wound treatment after combat, daily poultice and herb preparation, and full HEALING rolls for injured band members outside normal recovery. One of the most practically valuable payments a band with an active injury rate can accept. A tenday of genuine healer attendance is worth more than coin to a band that has been using untrained hands to dress wounds in the field.                                                                                                                                                                                                  |
| Pledged skilled labor from the settlement's master craftsman                                           | 10–28 silver equivalent                   | The settlement's smith, carpenter, or builder pledges a fixed number of weeks of work, redeemable at the settlement within one year. A smith's week: equipment repair, weapon maintenance, and fabrication at no extra charge — materials drawn from band stock, labor free. A carpenter's week: structural work toward a stronghold component, or gear repair. An herbalist's week: supply preparation and wound care equivalent to full HEALER attendance. Must be claimed within the year or the pledge expires. A band building toward a permanent base treats this as direct construction credit; a traveling band treats it as a reason to return.                                                                                                      |
| Free wintering — lodging and full board with no service obligation                                     | 20–60 silver equivalent (by band size)    | The settlement grants the band winter quarters: dry beds, daily meals from communal stores, and warmth for the full winter season. Unlike a protection contract, this carries no patrol obligation — the settlement wants armed men present without bargaining for patrol schedules. Small skirmisher band (3–6 men): 20–35 silver equivalent. Full warband (7–20 men): 40–60 silver equivalent — the settlement is committing its entire winter surplus to feed twenty mouths from first frost to snowmelt. Immovable and non-transferable. Worth nothing to a band that will not stay.                                                                                                                                                                      |
| A standing protection contract — one full season, paid in provisions, shelter, and settlement standing | 50–120 silver equivalent (by band size)   | The poster hires the band rather than paying coin. Payment is ongoing: a roof, reliable food, standing among the settlement's people. Skirmisher tier (3–6 men): 50–70 silver equivalent for the season. Warband tier (7–20 men): 80–120 silver equivalent — the settlement is committing its surplus to feed twenty armed men for twelve weeks, which is as real a payment as coin. Smaller bands can still accept subsistence-and-shelter deals at lower values; the range scales with what the settlement actually consumes. Binds both parties for the season and changes the band's relationship to that settlement permanently.                                                                                                                         |
| A captive already held — transferred with ransom intelligence                                          | Market rate of captive (see Ransom table) | The poster holds a prisoner worth money to someone else and does not have the reach or patience to collect. They hand over the captive, whatever they know of the captive's connections, and all claim on what follows. The band gets the asset and the problem at once: feeding the captive, running the negotiation, and absorbing whatever arrives when the demand reaches the wrong ears. Price against the Ransom table. Verify identity and condition before accepting — a dead captive on arrival is a dead deal.                                                                                                                                                                                                                                      |
| Raw materials in bulk — iron, leather, cloth, grain, pelts, or herbs                                   | Per-unit price from Ch10 (minimum floor)  | A village rarely has coin but often has stores. Per-unit minimums: iron 1 silver, herbs 2 silver, leather 12 copper, wool cloth 8 copper, grain 3 copper, pelt 8 copper. A substantial cache — forty units of iron (40 silver), a season's tannery output in leather, or a medicinal herb store — is real settlement wealth expressed in materials rather than coin. Agree the count and condition before the contract is taken. Perishable materials (grain, meat, pelt, herbs) lose value if collection is delayed past their listed shelf life; build a condition clause in if the contract is expected to run longer than a few weeks. The collector must also consider carriage: iron is heavy, grain spoils, and a wagonload of pelts requires a wagon. |

**Three problems arise on nearly every large goods bounty.**

_Transfer requires presence._ Unlike coin at an inn, a house, a boat, or a grain store cannot be transferred from a distance. The collector completes the contract and must then physically appear at the collection point to receive what was posted. If the goods are far from the contract area, experienced hunters price that inconvenience into whether they take the work at all. A poster who wants serious hunters puts the goods close to where the killing is, or adds a coin supplement for the march.

_The poster must hold clear title._ A settlement elder who offers the communal grain store as payment needs the settlement's agreement — not signature, agreement. If the council disputes the elder's authority to post goods that belong to everyone, the collector arrives to claim something that no one will surrender. Before accepting goods payment, ask plainly: _whose goods are these, and who vouches for it?_ A public announcement before the settlement's council, a written agreement, or a named third-party guarantor are all acceptable answers. The absence of all three is a warning.

_Goods spoil, break, and die._ A horse sound at posting may be lame at collection. A grain store posted in autumn may be half-eaten by spring. A boat with one soft plank in summer is a boat with a serious problem by the following season. A bounty that takes months to collect against goods that deteriorate in those months has a gap in it. A collector who wants protection against this negotiates a condition clause at acceptance: the goods delivered must match the goods described at posting, or a silver supplement covers the difference. Most posters resist this. Most collectors who do not insist on it regret it.

**Third-party guarantors.** Any goods payment above 15 silver equivalent requires a guarantor to attract professional interest. A guarantor is a trusted third party who witnesses the posting, knows the condition and location of the goods, and can testify in any dispute about whether the delivery satisfied the posted terms. Common guarantors: settlement elders, innkeepers of established standing, priests of any recognized faith, captains of unrelated bands whose Reputation makes their word carry weight in the region. A guarantor who vouches falsely damages their own standing. This is usually enough.

An unguaranteed goods bounty is taken only by desperate hunters or by collectors who know the poster personally and trust them for reasons that have nothing to do with the notice. Experienced hunters discount unguaranteed goods postings by one-third in their private assessment of whether the work is worth leaving camp.

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

A captive who dies through negligence — untreated wounds, exposure, thirst, inadequate shelter — triggers a reduced consequence: Standing at the relevant settlement drops by 1, and whoever posted the bounty is an aggrieved party. The full Atrocity cascade does not apply unless the negligence was sustained and witnessed. If the band knew the captive was dying and had the means to prevent it, the GM may treat it as deliberate. The band bears responsibility for the captive's condition from capture to delivery.

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

The difference between Fear-Held and Trust-Held is not visible until it needs to be. Both bands look functional at MORALE 4. The distinction is what happens to the information when things go wrong — and where Named Men's loyalty actually sits. See **Trust-Held Bands** below.

**Tyrant Punishments**

Tyrant captains use punishments designed to leave a mark — on the body of the offender and on the memory of everyone watching. These replace or supplement the standard punishment table at the captain's choice.

**Mutilation:** Used for offenses the captain wants recorded on the body. The severity scales with the offense. A first serious offense — theft, a lie that cost blood — earns a finger from the dominant hand: MELEE and MARKSMANSHIP reduced by 1 permanently, the stub visible to anyone who looks, recognized in settlements by traders and elders who have seen it before. Repeat offenses, serious treachery, or an example the captain needs to make without killing the man outright earn the full hand: dominant hand removed, MELEE capped at 1, no two-handed weapons, no tasks requiring both hands at full capacity. The man is kept. That is the point. He is alive because the captain chose it, diminished and marked and still present in the line every morning as a reminder to the others.

**Public execution of a company member:** The captain kills a member of the band — or orders it done — in front of the assembled company. No private sentence. No quiet removal. The body stays visible until the company moves.

This always triggers:

- MORALE -1 immediately, even in a fear-held company. Fear rises, but morale costs are real.
- Every Named Man present rolls against Loyalty. A Named Man at Loyalty 1 who fails this roll begins actively planning departure or betrayal.

The exception: if the executed man was openly despised by the band — a coward whose failure cost blood, a thief who stole from multiple members — the GM may waive the MORALE cost. The execution lands differently when the men already made the same calculation.

A captain who uses public execution more than once in a season will eventually face a band in which everyone is calculating odds. Some captains understand this and use it anyway. They have made a trade: immediate obedience now for a shorter future.

#### Trust-Held Bands

Rural Peasant bands are Trust-Held by default. Kin bands are Trust-Held by definition. Military bands can become Trust-Held over a full season of consistent pay and kept word. Most bands start somewhere in the middle — professional exchange, neither fear nor trust — and drift one way or the other depending on how the captain handles the first three bad situations.

Trust-Held is not a higher MORALE ceiling. The table is the same. What changes is how failure lands, what information the captain has access to, and how long the bonds hold before they break.

**A Trust-Held band under pressure:**

- A **Trust-Held** band at MORALE 3 (Shaken) protests aloud. Named Men say what is wrong to the captain's face instead of swallowing it. This costs the captain standing. It also means the captain knows exactly what the problem is.
- A **Trust-Held** band at MORALE 2 (Wavering) demands a direct accounting from the captain — not from the sergeant. If the captain gives one that holds, the next MORALE check is at -1 difficulty. If they cannot give one, it is +1 difficulty instead.
- A **Trust-Held** band at MORALE 1 (Broken) does not pretend. The dissolution is open and the captain knows it in full. This is worse in the moment and easier to survive than the slow covert collapse of a Fear-Held band.

**Trust-Held mechanics:**

**Loyalty decay halved.** Named Men in a Trust-Held band lose Loyalty at half the standard rate when triggers are hit. The bond was built on something. It takes more sustained failure to erode it.

**The stay.** Once per season, when the captain fails a MORALE check, the GM may offer a Named Man with Loyalty 3 the chance to spend — to step forward, back the captain publicly, and hold the band together for one more day. If the Named Man does this, the MORALE cost that week is reduced by 1 step. The Named Man's Loyalty drops to 2 immediately. The bond cannot be spent again from the same Named Man until their Loyalty recovers to 3.

> **Example:** Pell fails his MORALE check after a wet week with no contract news — the band is Shaken. The GM offers Rook, Loyalty 3, the chance to spend. Rook stands by the cookfire and tells the men he has seen worse captains and worse weather, and that Pell has paid. The men finish the meal without walking. Pell records MORALE cost reduced by 1. Rook's Loyalty drops to 2. He said it because it was true. He cannot say it again from the same place until he earns it back.

**The warning.** A Trust-Held Named Man with Loyalty 1 who has reached their limit will tell the captain before they leave. Not with time to argue. Not loudly. But the captain gets one conversation — a flat statement of what is wrong and what they intend. A Fear-Held Named Man gives nothing. The captain cannot prevent either outcome. This is what trust costs and what it gives back.

**Transition out of Trust-Held.** A band that was Trust-Held and drifts into fear management — a captain who increasingly substitutes INTIMIDATION for MANIPULATION, an atrocity the Named Men were ordered to carry out, a season of broken promises — loses Trust-Held status at the end of that season. The change costs MORALE -1. The men know what the company was. That knowledge is not comfort. It is the specific grief of a thing that has become something else.

**Transition into Trust-Held.** A Fear-Held band can earn Trust-Held status. The captain must pay reliably, address Named Men's triggers when they appear, and avoid using INTIMIDATION as a substitute for MANIPULATION through a full season without a loyalty break or a public trust violation. At the end of that season, the GM confirms the transition. It is slow. It is not impossible. The men remember everything that happened before it, too — and that debt does not disappear because the band is now better.

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

**Running the optionals:** Arguments and Escalation and Death Distribution are self-contained. Enable them at the first session and they will fire when the situation calls for them. Blood Oaths requires Named Men who have worked together long enough to have a real history — at minimum a full season of shared contracts. Enabling Blood Oaths before the Named Men mean something to each other produces a mechanic that exists but never reaches the table. Add it when the Named Men have names the players would miss.

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

**Agitating actions.** Not every bystander wants the argument to stop. No roll is required to push things further. The action lands and the stage responds.

- **Naming a specific past offense** — a theft, a cowardice, a debt, a dead man whose death is still disputed — forces the argument up one stage if the target's Personality is Grudge-Holding or Mercenary Proud.
- **A physical shove**, regardless of current stage, jumps the argument to Stage 3 immediately.
- **A public insult that draws laughter** from the watching men at Stage 2 pushes to Stage 3 without a roll. Shame moves faster than anger.

If a Named Man's Trigger is spoken aloud — not implied, stated plainly in front of others — the Named Man rolls WIT difficulty 2. Failure means they enter the argument at the next stage even if they were not in it beforehand. The men know each other's Triggers. Triggers can be aimed.

**Mitigation actions.** Every stage admits intervention beyond the standard table entries.

- **Witnessed concession.** If one party names the other's grievance out loud — not an apology, an acknowledgment — the argument drops one stage without a roll. The conceding man costs something. It stays cheaper than blood.
- **INSIGHT to name the cause.** A bystander who succeeds on INSIGHT difficulty 2 names the actual grievance plainly, in front of both parties. On success, the argument drops one stage and the next intervention roll is at -1 difficulty. A wrong read changes nothing.
- **Physical interposition.** A Named Man who steps between the two parties at Stage 2 or 3 takes the argument's energy onto themselves without rolling first. They must then succeed on MANIPULATION or INTIMIDATION difficulty 2. On failure, the argument continues at the same stage and the Named Man is now in it.

**Flyting.** A man with a quick mouth and a specific grievance can turn Stage 2 or 3 into something the whole company watches rather than joins. An old tradition. It has a shape the Ravenlands recognizes — a word-fight instead of a blade-fight, formal enough that the watching men hold still.

When an argument reaches Stage 2 or Stage 3, any participant may call for flyting. The challenge is simple: _let words settle this_. The other party may accept or refuse. Refusal pushes the argument one stage forward immediately — declining the word-fight in front of witnesses reads as an admission the man's mouth is not worth hearing.

If both accept, physical escalation pauses. Resolve the exchange with an opposed PERFORMANCE roll. Difficulty equals the current stage number.

| RESULT           | WINNER                                                                    | LOSER                                                                                          |
| ---------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Winner by 1–2 ⚔️ | Standing rises among the anonymous fighters; argument resolves at Stage 1 | No injury, no Loyalty roll; owes the winner a public concession in the next unrelated dispute  |
| Winner by 3+ ⚔️  | As above                                                                  | Loyalty roll (same rule as a Stage 3 fight loss); the humiliation settles longer than a bruise |
| Tie              | Argument resolves at Stage 1; the company treats both men as even         | —                                                                                              |

MORALE cost for a flyting exchange that ends without reaching Stage 4: none beyond the stage's existing cost. The company's blood stayed inside their bodies.

If either participant breaks the frame before the roll — draws steel, throws a punch, storms off — the argument jumps to Stage 4. The provocation and the broken word land at the same time.

**The compliment.** A bystander who wants neither the interposer's risk nor the orator's contest can try a third thing: publicly honor one of the men. Name a past deed, a debt the company owes them, a hard thing they did that no one has said aloud until now. Done right, it gives the man a way to step back from the argument without losing standing — the room understands that the compliment is an exit. This is PERFORMANCE difficulty 2.

On success: the honored man may end the argument at Stage 1 without standing cost. The other party may accept or push forward. Pushing forward after the honored man has stepped back costs MORALE -1 as though the argument had reached Stage 3 — the company has seen a man refuse the peace, and they remember it.

On failure: the compliment lands hollow. Wrong thing, wrong tone, a feat the honored man does not want on record in this company. Nothing changes except the bystander's credibility. They cannot attempt the compliment again in this argument.

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

### Optional: Territory Marking and the Language of Violence

_This subsystem is appropriate for Tyrant and Military bands operating in contested territory. Rural Peasant bands may use it under extreme conditions; Kin bands generally maintain territorial languages of their own that do not require it._

Territory in the Ravenlands is not owned. It is held — by whoever is present, by whoever can demonstrate the cost of challenging it, and by how recently that demonstration was made. A deed, a boundary post, a handshake with an elder: these carry weight inside settlements and nowhere else. What carries weight in the hex between settlements is what the men at the tree line believe about what happens to people who cross without invitation.

Two practices communicate this faster and more durably than any spoken threat.

**Spiked markers.** After an engagement, or after an execution, the band takes heads — or visible body parts — and posts them at the edges of claimed ground: road approaches, bridge ends, prominent trees at a hex boundary, the gate of an occupied settlement. The sergeant assigns the work. It is done without ceremony. It takes one Quarter Day to mark a full hex perimeter.

A traveler, scout, or rival band entering a marked hex who succeeds at SCOUTING (difficulty 1) reads the markers immediately. They know the ground is held, someone recent died here, and the band considers this theirs. Any band entering a marked hex must make a MORALE check (difficulty 1) before the first Quarter Day of movement — at MORALE 3 or below, the difficulty is 2. A Skirmisher-tier band that fails this check will refuse to enter without a direct order and a convincing reason.

| MARKER CONTENT                                   | STANDING            | FEUD TRACK |
| ------------------------------------------------ | ------------------- | ---------- |
| Unknown enemies                                  | -1                  | +1         |
| People the settlement recognized                 | -2                  | +2         |
| A settlement's named defender or the elder's kin | -3, D6 revolt check | +3         |

Markers degrade in two weeks without maintenance — animals, weather, rot. A band that abandons ground without clearing the markers leaves them standing for that window. Long enough to matter. Not long enough to hold the territory.

**The sack.** A severed head delivered to a specific recipient in a sack. No letter is required. The head is the message. Its meaning is the identity of the dead person: you know who this was, and now you decide what happens next.

This works only if the recipient recognizes the dead person. A captain who misjudges this — who delivers a head the recipient does not know — loses the leverage entirely. The recipient receives fear without target, which produces unpredictable responses and no compliance.

When the identity is recognized:

- No roll required. The arithmetic is already complete. The recipient knows the cost and can see it.
- The GM rolls D6: on 1–2, the recipient capitulates (offers what was demanded or withdraws); on 3–4, they negotiate (MANIPULATION difficulty 1 to hold band terms through one exchange); on 5–6, they escalate (bounty posted within a week, allies contacted, counterattack planned).
- Feud Track at the recipient settlement advances +2 regardless of outcome.

**Repeated delivery:** A second sack sent to the same settlement or faction in the same season generates automatic escalation without a roll — the recipient has counted and they know this is policy, not warning.

**Who uses this:** Tyrant captains post markers as display of ownership. Military captains may post them at a defended perimeter during a contract to mark engagement zones. Using either practice at MORALE 4 or 5 carries no additional cost. Using them at MORALE 3 or below requires the captain's justification to be visible — if the men cannot read the reason, they read it as cruelty for its own sake, and they know the difference.

A Named Man with a civilian-harm Trigger who witnesses either practice applied to non-combatants must roll against Loyalty regardless of current MORALE level.

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

### WILLPOWER

Named Men begin a mercenary engagement with a small WILLPOWER pool tied to their rank as a Named Man. This is a limited reserve — usually no more than 2–4 points.

- **Veteran Named Men** start with 2 WILLPOWER.
- **Elite Named Men** start with 3 WILLPOWER.
- Exceptional Named Men with a special status or built-in narrative role may start with 4 WILLPOWER, but 4 is the ceiling for this system.

Non-player Named Men recover **1 WILLPOWER per day** of downtime. If a Named Man is a player character, they recover WILLPOWER according to the normal player character recovery rules instead.

> **Example:** Helle is an Elite Skirmisher with 3 WILLPOWER when the night assault begins. She fails a MOVE roll crossing the spiked trench and pushes it — spending 1 WILLPOWER to succeed. The trench is cleared. Later, the captain asks her to run a message through contested ground alone. She has 2 WILLPOWER remaining. She goes. That night she sleeps in the occupied building and recovers 1. She starts tomorrow at 3 again — unless there is another assault.

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

Mercenaries are not broken men waiting to be healed. They are functional people shaped by years of violence, moral compromise, and self-preservation. Roll D66 or assign using tens-and-ones notation:

| D66   | PERSONALITY                                                                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 11-13 | **Flat** — Does not react to blood, screaming, or death. Eats during the aftermath.                                                         |
| 14-16 | **Calculating** — Counts everything: exits, weapons, faces, who is looking where. Never unprepared, never comfortable.                      |
| 21-23 | **Scornful** — Finds weakness faintly amusing. Will help, for the right price, and will say so plainly.                                     |
| 24-26 | **Cruel Practical** — Uses suffering as a tool. Not sadistic — does not enjoy it unless it serves something.                                |
| 31-33 | **Territorial** — Their gear, their cut, their space. Challenge any of it and they will not forget.                                         |
| 34-36 | **Dark Amused** — Makes jokes about things others will not name. Laughs at violence. This is just what they are.                            |
| 41-43 | **Paranoid Competent** — Assumes betrayal will come and plans for it. Usually right about the first part.                                   |
| 44-46 | **Convincing Liar** — Tells the truth when convenient. Cannot always tell the difference anymore.                                           |
| 51-53 | **Grudge-Holding** — Has a private list. Wrongs do not age out. They wait. Will say they've forgotten.                                      |
| 54-56 | **Mercenary Proud** — This is their profession and they take it seriously. They resent men who don't.                                       |
| 61-63 | **Death-Easy** — Settled their account with dying long ago. Makes them fearless in ways that look like madness.                             |
| 64-66 | **Quietly Violent** — Does not threaten. Does not argue. When the moment comes, they act before anyone else has decided the moment is here. |

### Named Man Advancement

After any engagement resulting in a clear victory, award XP to each non-player Named Man who fought.

- On a 6: award **5 XP**
- On a 5: award **3 XP**
- On a 4–3: award **2 XP**
- On a 2: award **no XP**
- On a 1: award **3 XP** and the Named Man suffers a meaningful injury. Roll on the critical injury table.

**Named Man transition to full character:** The GM may offer a Named Man a full character sheet when their player's original character is out of action and both the player and GM agree. A Named Man eligible for this transition should have at least 15 XP recorded, an Agenda that has been actively pursued, and Loyalty 3 with the fellowship. On transition, the player selects the Named Man's kin-appropriate profession from Ch02 and picks starting skills accordingly. Prior XP carries over at 2:3 conversion rate (15 Named Man XP becomes 10 PC XP). The Personality, Trigger, and Agenda survive the transition intact — they remain who they are.

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

> **Example:** Pell's men burn the granary at Salthorn because the gate foreman refused to open up and the contract was on a clock. No one is killed. Standing at each settlement within three hexes drops by 2 — four villages that have sheltered the band before. MORALE check: the men made nothing on the burn. Galt, Loyalty 2, a civilian-harm Trigger on his sheet, rolls against Loyalty and fails. He does not leave that night. He is in his bedroll calculating whether there is better work in the next town north.

### Plunder

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

**Named Men during downtime:** Named Men assigned to GUARD duty at the stronghold count toward Defense Rating the same way common soldiers do. During a downtime period, a Named Man may additionally be assigned to one of the following stronghold functions per Quarter Day: TRAINING (they drill the common guards, +1 to the COMMAND roll for next season's drill if a Named Man ran it), SCOUTING (a Named Man dispatched as a ranger counts as a standing patrol, satisfying one week of patrol contract terms without the band deploying), or LOGISTICS (reduces the weekly provision cost for garrison fighters by 1 unit per Named Man assigned, to a minimum of half normal cost). A Named Man assigned to stronghold duty does not advance — no XP awards during home-station periods. Loyalty does not decay during downtime as long as pay is current; if pay lapses, standard non-payment rules apply.

### Reputation Cascade

The band's deeds — contracts completed, atrocities committed, bounties earned — all travel through the Ch08 Reputation system. The band does not have its own Reputation score separate from the fellowship's. Their name is the fellowship's name. Every deed adds to or subtracts from the same pool of stories people carry across hexes.

A stronghold's Reputation radiates outward via hire relationships. If the band was hired by a settlement, that settlement knows the fellowship's name and passes it forward. If the band burned that settlement, neighboring settlements know that too.

If the band operates independently for a full season while the PCs are elsewhere — sent on contract without fellowship oversight — atrocities the band commits in that period still attach to the fellowship's name. This is the cost of the name being shared. A future subsystem may introduce a separate Band Notoriety track that can diverge from fellowship Reputation in extreme cases; for now, the band's name is the fellowship's name without exception.

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

| RANK        | ENTRY CONDITION                                                                | PAY/DAY    | AUTHORITY AND USE                                                                                                          |
| ----------- | ------------------------------------------------------------------------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------- |
| FRESH       | First contract, no record                                                      | 1 silver   | None. Takes every order from anyone ranked BLADE or higher.                                                                |
| BLADE       | Fought through at least two engagements and returned. The company has seen it. | 1 silver   | May speak at company council. May be assigned a single task detachment.                                                    |
| CALLED      | Carries a call name (see below).                                               | 2 silver   | May lead scouting, flanking, or small detachments of 3–5 men. Assigned own unit.                                           |
| TENSMAN     | Commands a unit of ten through a full contract.                                | 3\* silver | MANIPULATION rolls for their unit's minor discipline. Handles the unit's daily assignments.                                |
| SERGEANT    | Commanded a section through hard fighting and kept it together.                | 4\* silver | May substitute their own MANIPULATION for the captain's on section-level MORALE checks.                                    |
| FIRST BLADE | The captain's right hand. There is only one at a time.                         | 8\* silver | Full authority short of overriding an active contract. Leads the company if the captain is absent, incapacitated, or dead. |

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

## Section 13: Host Play

A Host is the top tier of this system — multiple bands operating under a shared authority. It is not a warfare system for armies and sieges; those remain outside scope. It is the framework for tables that want the mechanics and politics of meta-band play: the fellowship's band serving inside a larger force, dealing with other captains, navigating a Warmaster's orders, and holding their independence inside someone else's campaign.

### Running a Host at the Table

Each band within the Host is tracked separately. Its own roster, its own MORALE score, its own Named Men, its own daily pay requirement. The Host does not merge into a single unit — it is a collection of units operating under shared authority.

If the PCs lead one of those bands, run their band with the full mechanics of this system. The other bands exist at summary level: the GM tracks their strength die, current MORALE, and standing obligations, but does not roll for every Named Man's agenda. Their captains are supporting NPCs — available for scene work, capable of acting against band interests if the Warmaster's authority is contested.

### The Warmaster's Authority

A Warmaster gives operational orders. Band captains follow them — or don't. The chain of authority is real but fragile. It runs on reputation, past payment, and the belief that the Warmaster can deliver what was promised.

When the PCs' band receives a Warmaster order they want to refuse or modify, the captain makes a MANIPULATION roll at difficulty equal to the Warmaster's REPUTATION divided by 2 (round up, minimum 1). On success, the objection is heard and a compromise is negotiated. On failure, the order stands as given. Openly defying a Warmaster order without even attempting the roll costs MORALE −1 and is noted.

A Warmaster who fails to pay, fails to supply, or gives orders that result in serious band casualties without acknowledged cause may be challenged. A band captain with REPUTATION 3+ may formally contest the Warmaster's leadership: one MANIPULATION roll opposed by the Warmaster's. If the PC wins, their band detaches from the Host under the GRIEVANCE mechanic without triggering a full Atrocity. If they lose, the Warmaster may demand a loyalty demonstration.

### The Warmaster's Alignment

A Warmaster is either independent — running the Host as their own enterprise, personally responsible for all obligations — or sworn to a faction.

An **independent Warmaster** negotiates contracts the same way a band captain does. They retain all bands within the Host on a contract basis, paying each band out of the overall contract fee. If the contract falls through, the Warmaster absorbs the loss or passes it down to the individual bands. If they pass it down, every band's MORALE is at risk simultaneously.

A **faction Warmaster** represents an employer with institutional backing — a warchief's army, a noble's levies, a religious military order, a trade guild's private force. The faction supplies, funds, and controls the strategic objective. The Warmaster executes it. Individual band captains deal primarily with the Warmaster, not the faction directly. What the faction wants and what the Warmaster tells the captains may not be the same thing; the gap between them is where political pressure operates.

**Faction alignment and individual bands:** A band serving under a faction Warmaster is treated as Allegiance 1 toward that faction by default, regardless of what the individual band captain believes about the relationship. The faction knows the band's name and what they did. If the Host achieves the campaign objective, the band gains Allegiance +1 with that faction once before the Host disperses. If the Host fails badly, the faction may redirect blame — and a named band makes an easier target than a dispersed force.

### Supply at Host Scale

Individual bands within a Host do not forage independently by default. The Host has a combined supply requirement — add every band's daily FOOD total. The Warmaster or a designated logistics officer handles provisioning. Each band receives its share at the end of each Quarter Day.

If the supply line is disrupted, each individual band rolls against its own provisions. A band with enough stores sustains itself. A band without stores falls into the standard unpaid/unfed MORALE trigger chain immediately — the Host's shared logistics do not protect a band that ran its own stores dry.


### Host Treasury

The Warmaster holds the Host's coin. Not as a personal fund — as a working account the entire force runs on. Every contract payment, every advance from a faction employer, every fee wrested from a settlement that wanted the Host gone, flows into the treasury first. The Warmaster pays out, the bands draw down, and the difference between what is promised and what is left is the number that determines how long the Host stays together.

**How the treasury works:**

The treasury is divided into three parts:

- **Operating reserve:** The coin allocated to cover the next two weeks of full Host pay. If this drops below one week's total cost, the Warmaster is in distress.
- **Band advances:** Coin pre-allocated to individual bands for their local expenses — food supplements, gear repair, informants, bribes. Drawn against a written order.
- **Strategic reserve:** Held back from all operating allocations. Emergencies only: a contract collapses mid-run, a band needs emergency resupply, a rival makes an offer to one of the captains that needs buying off.

A Host without a strategic reserve is a Host one bad week from collapse. Experienced Warmasters keep their strategic reserve at two weeks of full Host pay and do not touch it except to prevent something worse than the cost of keeping it.

**Tracking the treasury at the table:**

The GM holds the treasury total. The PCs either manage it (if they are the Warmaster or hold a financial role) or observe its effects (if they are a band captain dealing with the Warmaster). The Warmaster shares treasury information at their discretion — a captain asking about pay security makes a MANIPULATION roll at difficulty 1 to get a straight answer. On a failure, they get a version of the truth.

### Band Budgets and the Purser

Each band within a Host draws from the Host treasury at a fixed rate. Not coin handed over — a budget allocation, tracked by a purser. The purser is a Named Man or trusted NPC appointed by the Warmaster. The purser knows what each band is drawing, what they are spending it on, and how the ledger sits.

**Standard allocation per band per week:**

| BAND SIZE | PAY ALLOCATION | LOCAL EXPENSES BUDGET |
| --------- | -------------- | --------------------- |
| Skirmishers (3–6) | 21–42 silver | 5 silver |
| Warband (7–20) | 49–140 silver | 10–15 silver |
| Company (21–50) | 147–350 silver | 20–30 silver |

Local expenses cover informants, small bribes, gear repairs the band cannot defer, emergency food, and similar costs. They do not cover Named Man bonuses, specialized equipment, or anything requiring a direct order from the Warmaster.

A band that exceeds its local budget without Warmaster authorization draws against the next week's allocation. Two consecutive overruns trigger a purser review. What comes out of a purser review depends on what went into the excess — legitimate combat costs are absorbed; personal expenditure comes out of the captain's own share; unexplained excess is a problem.

**Deferred pay:**

When the treasury is short, the Warmaster may declare a deferral: pay is not cut, it is delayed. Each week of deferred pay is a formal obligation recorded in the purser's ledger and carries interest in goodwill — the delayed band's MORALE check this week is made at the standard trigger threshold, but the Warmaster takes a −1 to their authority roll at the next Host Council if deferred pay is still outstanding. A deferred debt that goes three weeks unpaid becomes a Grievance on the standard GRIEVANCE table.

**What the PCs can do with this:**

If the fellowship runs one band, they receive their allocation and manage it. A week where they need more than their budget requires going to the purser with a justification or the Warmaster with a request. If the fellowship runs the purser's function (trusted Named Man or direct Warmaster role), they see everything — the treasury position, the other bands' draws, the strategic reserve — and can act on that information, including selectively reporting it.

### Dispatch and Messengers

A Host does not fight in one place at once. Bands may be one hex apart, twenty hexes apart, or on separate sides of a contested river. Orders written at the Warmaster's table take time to arrive. By the time they do, the situation at the receiving end may no longer match the situation the orders were written for.

Information lag is real and has mechanical teeth.

**Dispatch rules:**

A rider on a sound horse covers roughly six hexes per day on clear roads, four in difficult terrain. The Warmaster's order leaves the table on day 0. The band receives it on day 0 + travel time. Until then, the band operates on last known orders.

| DISTANCE | CLEAR ROAD | DIFFICULT TERRAIN | WINTER/MUD SEASON |
| -------- | ---------- | ----------------- | ----------------- |
| 1–2 hexes | Same day | Next morning | Next morning |
| 3–6 hexes | 1 day | 2 days | 3 days |
| 7–12 hexes | 2 days | 3–4 days | 5–6 days |
| 13+ hexes | 3+ days | 5+ days | 8+ days |

**Standing orders:** Every band within a Host operates under a set of standing orders — what to do if contact is lost, what threshold justifies independent action, how long to wait for a rider before assuming the Warmaster's situation has changed. The Warmaster issues standing orders at Host formation and may update them via dispatch. A band following standing orders in good faith is not in breach of Warmaster authority, even if the action taken looks wrong from the outside.

Standing orders cover at minimum:
- Withdrawal threshold (when to pull back without orders)
- Contact protocol (how to signal the Warmaster's relay point)
- Emergency action authority (what the band captain may decide alone)

**Lost riders:** A dispatch rider who does not arrive is a problem. The Warmaster does not know the message failed. The receiving band does not know the order exists. The GM rolls secretly when a rider enters dangerous territory: SCOUTING at difficulty 1 in contested hexes, difficulty 2 in actively hostile territory. On a failure, the rider is delayed (re-roll arrival by 1D3 days), captured, or killed (GM decides based on what is in the hostile territory). A captured rider means the enemy has the Warmaster's orders.

**Urgent riders:** A Warmaster who needs a message delivered fast may send a relay — two or three riders, each carrying a copy, taking different routes. Cost: 2–5 silver per rider depending on distance and season. Increases delivery odds, does not eliminate the delay.

**The reply problem:** A band captain sending a report back to the Warmaster faces the same delay. A response to a question asked on day 1 arrives on day 4 at best. Plans that depend on real-time communication between the Warmaster and a remote band will fail. The Host that functions well under information lag has Warmasters who write orders that do not depend on perfect relay, and captains who can execute against the intent rather than the letter.

> **Example:** Pell's warband holds the east flank at the Ashriver crossing. The Warmaster sends orders on day three to pull back to the tree line before dawn — the enemy has reinforced the far bank. The rider hits mud season on the ridge road. The orders arrive at midday on day five. Pell has already held the crossing through a probe and taken two wounded. He reads the order. It says pull back before dawn. Dawn was nine hours ago. He does what the standing orders say: hold position, report status, wait for the next rider.

### Host Diplomacy

A Host deals with parties the individual bands cannot. A faction that will not meet a single captain will meet a Warmaster. A rival Host that has a reason to fight has a reason to talk first. A settlement that would shut its gates at a warband of twelve may open them when a Host of two hundred is a day's march away.

Diplomacy at Host scale has three forms.

**Faction negotiation:**

The Warmaster speaks for the Host. They use their own MANIPULATION, not any band captain's. Difficulty scales with the faction's power:

| FACTION TIER | DIFFICULTY | EXAMPLES |
| ------------ | ---------- | -------- |
| Local | 1 | Village council, small cult, minor trader |
| Regional | 2 | Warchief with a territory, guild with several towns, armed religious order |
| Major | 3 | A lord with military force, a large faction with institutional standing |
| Great | 4 | A power that controls borders, a major faith's military arm, a warlord with multiple Hosts |

Success: the faction treats with the Host. Negotiated terms (contract, passage, non-aggression) become binding under the GRIEVANCE mechanic at the Host level — a broken agreement costs the Warmaster's REPUTATION, not an individual band's Standing.

Failure: the faction refuses terms. The Warmaster may try again next quarter after a significant change in circumstances (a Host victory, a shift in the faction's position, a third party's pressure on the faction). Not before.

**Rival Host parley:**

Two Hosts that could fight are often better served talking — at least until one of them has a clear advantage. A Warmaster who wants to parley sends a rider under flag of truce. The rival Warmaster may accept or refuse. Refusing is not an atrocity. Executing the rider under truce is.

Parley terms a Warmaster may propose:
- Non-aggression for a stated period (one week to one season)
- Passage rights through each other's territory
- Division of a contract between both Hosts (split pay, split zone, split obligations)
- One Host standing aside while the other operates (paid standoff)
- Full alliance: both Hosts under a shared campaign objective, shared command, shared pay pool

Each proposal requires opposed MANIPULATION: the proposer rolls, the opposing Warmaster rolls, the higher result determines whose terms anchor the negotiation. A tie reopens discussion. A defection offer made privately to a band captain during parley — bypassing the Warmaster — is noted in the GRIEVANCE mechanic if the offering Warmaster is ever identified.

**Third-party arbitration:**

Disputes between Hosts, broken truces, or contested claims over a contract payment may be submitted to a third-party arbitrator both Warmasters recognize. Common arbitrators: priests of standing, prominent merchants, elders of a sufficiently neutral settlement, the patron faction of one Host if the other accepts their authority.

The arbitrator's ruling is not enforceable by law — the Ravenlands has no court. It is enforced by the same mechanism all Host obligations run on: REPUTATION damage to the party that defies it. Both Warmasters agree before arbitration begins that defying the ruling removes their right to dispute the other's response. That agreement is what gives arbitration teeth.

### Inter-Band Rivalry

Bands within the same Host compete. The competition is usually quiet — which band gets the better billet, which captain gets mentioned in the Warmaster's dispatches, whose men come out of a contract cycle with the most loot, whose Named Men get elevated first. When the Host has enough work for everyone, this stays manageable. When resources tighten, it sharpens into something with edges.

**Favorable status:** The Warmaster may designate one band as currently favored — first pick of new contract assignments, first draw on fresh supplies, their captain's word carries more weight at council. Favorable status is noted. The other captains note it too.

**Rival bands:** Two bands in direct competition note each other. Track a Rivalry score (0–3) between any two bands. It starts at 0 and rises through specific triggers:

| TRIGGER | RIVALRY INCREASE |
|---------|-----------------|
| One band receives favorable status while the other does not | +1 |
| One band's action causes the other band to take casualties | +1 |
| One band takes contract credit for work the other band started | +1 |
| A Named Man from one band defects to the other | +1 |
| Both bands bid for the same billet/territory/contract assignment | +1 |

**What Rivalry costs:**

- Rivalry 1: captains are cold. MANIPULATION rolls between the two captains are at +1 difficulty.
- Rivalry 2: men are hostile. If both bands occupy the same camp, one random Minor Offense incident per week (see Section 6: Discipline).
- Rivalry 3: it is personal. Any joint operation requires a MANIPULATION roll from both captains (difficulty 2) before the operation begins. On a failure, the failing captain's band performs at −1 MORALE for the operation. On a double failure, neither band acts in support of the other.

**Reducing Rivalry:**

The Warmaster may spend one council action and REPUTATION 1 to formally broker a ceasefire between two rival bands. This drops Rivalry by 1. The alternative is letting it run — which teaches the Warmaster something about their own command, because Rivalry 3 between two of your bands means you created a condition and ignored it long enough for it to get there.

Rivalry does not reset at Host dissolution. If the two bands encounter each other again in a future Host or neutral territory, their prior Rivalry carries forward at −1 (minimum 0).

### The Host Council

The Warmaster convenes the council. Band captains attend — in person if the Host is concentrated, by trusted representative if bands are dispersed. A council costs one full Quarter Day for all bands involved, paid in lost patrol time, reduced foraging, and the social currency of the Warmaster's attention divided equally among every captain who showed up.

**What a council decides:**

- Operational changes: new march routes, target assignments, contract amendments
- Resource allocation: which bands get provisioning priority, which draw on the local goods budget
- Grievance hearing: a captain may name a Grievance against another captain or against the Warmaster; the council rules on the response
- Status designations: favorable status granted or revoked, Rivalry formally acknowledged, captains elevated or demoted

**What the Warmaster can force through:**

Everything with difficulty 0 and nothing with the word "takes." The Warmaster assigns targets, allocates budgets, and sets the march. They cannot force a captain to accept reduced pay without a MANIPULATION roll. They cannot force a captain to take an operation their band cannot sustain without a MANIPULATION roll at difficulty equal to the captain's REPUTATION divided by 2 (round up). They cannot revoke a captain's command in front of the assembled council without creating a Rivalry, a Grievance, or both — unless the revocation comes with clear evidence the captain has broken standing orders.

**Captains calling council:**

A band captain with REPUTATION 3+ may call an emergency council without Warmaster authorization if they can get two other captains to co-sign the call. The Warmaster must attend or formally refuse. A refusal costs the Warmaster −1 REPUTATION. A captain who calls council and cannot get co-signers marks a Grievance against the Warmaster in their own ledger — private, unspoken, building.

**Council vote:**

On contested decisions where the Warmaster has not issued a direct order, captains vote. Each captain has one vote. The Warmaster has two votes. A tied vote goes to the Warmaster. A vote that goes against the Warmaster two-to-one is a result they may comply with or override — overriding it costs REPUTATION −1 and starts a Rivalry entry.

### The Warmaster's Ledger

The Warmaster's authority is not permanent. It is a stock account that grows with victories, clean pay, and honored promises — and drains with losses, deferred coin, and broken commitments.

Track the Warmaster's Ledger as a separate score from their personal REPUTATION. The Ledger starts at 0 and runs from −6 to +6.

**The Ledger rises (+1 per event):**

- Contract completed and all bands paid in full on schedule
- A battle won with low band casualties
- A faction negotiation that improved conditions for two or more bands
- The Warmaster absorbs a personal loss to protect the bands' pay
- Standing orders that proved accurate in an unexpected situation

**The Ledger falls (−1 per event):**

- Deferred pay not resolved within two weeks
- Band casualties caused by a Warmaster order that captains disputed before the operation
- A parley or negotiation that failed and put the Host in a worse position
- A rider lost and an operation that failed because of it
- A council vote overridden by the Warmaster without later justification

**Ledger consequences by score:**

| LEDGER | EFFECT ON WARMASTER |
| ------ | ------------------- |
| +4 to +6 | Authority calls cost no MANIPULATION — captains follow without rolls |
| +1 to +3 | Standard authority. MANIPULATION at difficulty equal to REPUTATION ÷ 2. |
| 0 | Neutral. Captains comply but observe. No modifier, no bonus. |
| −1 to −3 | Every Warmaster order except direct operationals requires MANIPULATION at difficulty +1 above standard. |
| −4 to −6 | The Host is fracturing. Any captain with REPUTATION 2+ may call an emergency council without co-signers. The Warmaster's two council votes reduce to one. |

A Ledger that hits −6 triggers automatic Host dissolution (see below) unless the Warmaster resigns command voluntarily before a council vote removes them.

### Host Dissolution

Hosts end. Some cleanly. Most do not.

**Clean dissolution** happens when the campaign objective is complete and all obligations are honored. The Warmaster announces dissolution at a final council. Each band receives their full outstanding pay from the treasury reserve, any equipment drawn on Host allocation is either returned or purchased at a negotiated price, and the bands separate with their prior standing intact. The Warmaster retains credit for the Host's accomplishments. Each captain walks away with whatever Allegiance they earned.

**Contractual dissolution** happens when the employer discharges the Host before the objective is complete. If the contract specified an early-termination fee, the Warmaster collects it and distributes proportionally. If it did not, the Warmaster negotiates — MANIPULATION at the faction's standard difficulty. Bands receive a pro-rated share of whatever was collected. Captains who signed directly with the employer (not through the Warmaster) may press their own claims.

**Collapse** is messy. Triggered by: treasury empty with no recovery path, Ledger at −6, Warmaster killed or fled, major military defeat that breaks two or more bands simultaneously. When collapse happens, each band defaults to its last known contract obligations and operates independently. There is no formal dissolution. The Warmaster's outstanding obligations do not transfer — they simply become unpaid debts that follow whatever name was attached to the Host. If that name was the fellowship's name, the fellowship holds the debt.

**After dissolution:**

Individual bands keep their MORALE score, their Named Men, their gear, and their accumulated Allegiance with any factions they dealt with directly. The Host's shared REPUTATION is distributed unevenly: each captain's account with the factions and settlements the Host dealt with is based on what they personally did and witnessed. A band captain who honorably completed every assignment walks away with real settlement standing. A band captain who was present for an atrocity committed by a rival band under the same banner walks away with whatever the witnesses remember and whoever survived to tell it.

This is the price of shared banners: the bad ones follow everyone.

Sieges, territorial control, and pitched battle between Hosts remain outside scope. The Host tier defines where this proposal ends and where a future large-scale warfare system begins. Each band within this proposal is the atomic unit of that future system — a Host is several companies, not a different kind of thing.

---

## Acceptance Summary

These changes are interdependent. Sections 1–6 (band formation, morale, pay, provisions, extortion and tribute, contracts) are the core and should be accepted together. Section 4 (village extortion) can be deferred if the campaign does not involve coercive play against settlements, but it ties the band economy to the Feud Track and should not be omitted from a full implementation. Sections 7–8 (Named Men, wanted status) layer onto the core and can be added separately. Section 9 (atrocities) is self-contained and adds the moral accounting layer. Section 10 requires no changes — it documents integration with existing systems. Section 11 is a new stronghold function and requires only the War Room text. Section 12 (Serving in Another's Company) is standalone — it can be accepted or omitted entirely independent of all other sections. Section 13 (Host Play) is the full meta-band system; it expands independently of all prior sections and is only meaningful for tables intending multi-band campaigns.

| #   | CHANGE                                                                                         | LOCATION                     | DEPENDENCY        |
| --- | ---------------------------------------------------------------------------------------------- | ---------------------------- | ----------------- |
| 1   | Band formation + size tiers                                                                    | Ch09 (new section)           | None              |
| 2   | Morale system                                                                                  | Ch09                         | 1                 |
| 3   | Fighter tiers + recruitment                                                                    | Ch09                         | 1                 |
| 4   | Pay, provisions, expanded forager table, field non-payment                                     | Ch09                         | 1, 2              |
| 5   | Village extortion and tribute                                                                  | Ch09 + Ch08 cross-reference  | 1, 2, 3, 4        |
| 6   | Finding Work, Allegiance Track, Contracts and Bounties, Kidnapping, Mercenary Hoards           | Ch09                         | 1                 |
| 7   | Campaign life (QD activities)                                                                  | Ch09                         | 1, 2              |
| 8   | Named Men system                                                                               | Ch09                         | 1, 2, 3           |
| 9   | Wanted status                                                                                  | Ch09 + Ch08 cross-reference  | 6                 |
| 10  | Atrocities                                                                                     | Ch09 + Ch08 cross-reference  | None (standalone) |
| 11  | Integration section                                                                            | No text changes — notes only | All above         |
| 12  | War Room function                                                                              | Ch09 functions table         | Independent       |
| 13  | Serving in Another's Company (Section 12)                                                      | Ch09 (new optional section)  | Independent       |
| 14  | Section 6 optionals: Arguments and Escalation, Blood Oaths, Death of a Member — Distribution   | Ch09                         | 8                 |
| 15  | Host Play (Section 13): treasury, budgets, dispatch, diplomacy, rivalry, council, ledger, dissolution | Ch09 (new optional section)  | Independent       |

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

**✅ 2. Large-scale warfare:** Resolved at the Host tier boundary. A brief Host sidebar in Section 1 (after the Size Tiers table) introduces the Warmaster concept. Full Host mechanics — band-level tracking, Warmaster authority and alignment, supply at scale, and scope boundary — are in **Section 13: Host Play**.

**✅ 3. Mercenary archetypes by kin:** Resolved. Kin recruitment modifiers are now in Section 2 (Recruitment and Quality) as a table. Elf, Dwarf, Halfling, Wolfkin, Orc, and Goblin each carry specific mechanical note. Notes were kept narrow — modifier to the settlement roll only, not permanent stat effects.

**✅ 4. Named Man death and gear distribution:** Resolved. The Death of a Member — Distribution of Effects optional subsystem (Section 6) covers gear, pay, disputed items, gambling debts voided, and MORALE consequences. The process for anonymous fighters and Named Men is differentiated. What remains open: if a Named Man dies close to completing their Agenda, no rule specifies what happens to that Agenda — whether another Named Man can inherit it, whether it generates a narrative debt, or whether it simply closes. Flag for integration pass.

**Open questions:**

1. ✅ **Named Man promotion to PC-adjacent role:** Resolved. Section 7 (Named Man Advancement) now includes a ruling: a Named Man with 15+ XP recorded, an active Agenda, and Loyalty 3 may be granted a full character sheet by the GM when a player's original character is out of action. Prior XP carries over at 2:3 conversion. Personality, Trigger, and Agenda survive the transition.

2. ⏸️ **Band reputation vs. fellowship reputation:** Acknowledged and noted as a deferred design gap. Section 10 (Reputation Cascade) now includes a stated deferral: the band's name is the fellowship's name without exception until a Band Notoriety track is built. Future work, not blocking integration.

3. ✅ **Band downtime at the stronghold:** Resolved. Section 10 (Stronghold Defense Rating) now includes a Named Man downtime ruling: Named Men may be assigned to GUARD, TRAINING, SCOUTING, or LOGISTICS functions. BARRACKS covers Named Men and common guards alike. Loyalty does not decay during downtime if pay is current.

4. ✅ **MORALE 5 label collision:** Resolved. The label "Hungry" is renamed to **Keen** throughout the proposal.

5. ✅ **Acceptance table is out of date:** Resolved. The Acceptance Summary table now includes rows for: the expanded forager table (row 4), the full Section 5 additions including kidnapping and mercenary hoards (row 6), and the three Section 6 optional subsystems (row 14).

6. ✅ **Optional subsystem grouping:** Resolved. A guidance note now precedes the Optional subsystems in Section 6: Arguments and Escalation and Death Distribution are session-one ready; Blood Oaths should wait until the Named Men have shared history.

7. ✅ **Brotherhood oath bonus magnitude:** Resolved. The text already reads +2. The open question reflected a stale draft. No change needed.

8. ✅ **Unintentional captive death:** Resolved. The kidnapping section now distinguishes deliberate execution from negligent death. Negligent death triggers a reduced consequence: Standing −1 at the relevant settlement, the poster is a grieved party, and the full Atrocity cascade does not apply unless the negligence was sustained and visible. GM may treat it as deliberate if the band had means to prevent it and did not.

9. ✅ **Mercenary diplomacy and allegiances:** Resolved. Section 5 now opens with **Finding Work** (audience requirements and terms negotiation mechanic) and **Allegiance** (0–4 track per employer, with access tiers and exclusivity costs). The contract-vs.-bounty distinction is preserved: bounties are public, contracts are private, and conflicting obligations default to the employer's terms under the existing GRIEVANCE mechanic. The approach roll uses MANIPULATION at difficulty set by employer tier (1–4). Retained bands (Allegiance 3) carry exclusivity obligations; sworn bands (Allegiance 4) carry full exclusivity.
10. ✅ **Host diplomacy layer:** Resolved in Section 13 expansion. The full Host system now covers: the treasury and band budget allocation (Host Treasury, Band Budgets and the Purser), information lag and rider mechanics (Dispatch and Messengers), faction negotiation and rival Host parley including flag-of-truce and arbitration procedures (Host Diplomacy), resource competition between bands with a tracked Rivalry score (Inter-Band Rivalry), the council mechanic including captain-called emergency councils and vote rules (The Host Council), the Warmaster's Ledger as a persistent authority track (The Warmaster's Ledger), and clean, contractual, and collapse dissolution paths with per-band ownership of reputation consequences (Host Dissolution). Open: high-level political intrigue and multi-faction campaign dynamics at the level of a great power using the Host as a strategic instrument — this would be a campaign design question beyond the scope of a rules proposal.
