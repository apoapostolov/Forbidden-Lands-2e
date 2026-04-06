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
| Forest      | 0        | 1            | 3            | 6             | 9            |
| Dark Forest | 0        | 1            | 3            | 6             | 9            |
| Marshlands  | +1       | 2            | 4            | 7             | 11           |
| Plains      | 0        | 1            | 2            | 4             | 6            |
| Hills       | 0        | 1            | 3            | 5             | 8            |
| Mountains   | -1       | 0            | 1            | 3             | 5            |
| Quagmire    | -1       | 0            | 1            | 3             | 5            |
| Ruins       | -1       | 0            | 1            | 3             | 5            |
| Tundra      | -2       | 0            | 0            | 1             | 3            |

Apply season modifier from Ch08 if that proposal is in use (Spring -2, Summer -1, Autumn +1, Winter 0 — add to Hunt mod column, clamp 11+ forager output minimum to 0). A fellowship member with MASTER OF THE HUNT rank 3 or above may upgrade one column to the right for the entire party.

This output fills the band's daily FOOD requirement from the bottom up. A Warband of 15 men needs 15 FOOD per day. With 5 foragers in Forest terrain they bring back 3 — the remaining 12 come from provisions. With 10 foragers they bring back 6. Running a large band in thin country burns your stores. That is intentional.

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

Before demanding anything, compare the band's effective strength to the settlement's capacity to resist. Use these rough brackets:

| SETTLEMENT SIZE        | APPROXIMATE FIGHTERS AVAILABLE | NOTES                                         |
| ---------------------- | ------------------------------ | --------------------------------------------- |
| Hamlet (1-10 people)   | 1–3                            | Almost no armed capacity. Will yield or flee. |
| Village (11-40)        | 2–6                            | A few hunters and one tough elder.            |
| Large village (41-100) | 5–12                           | Organized resistance possible.                |
| Town (101-300)         | 10–30                          | A warchief or headman with real authority.    |
| Fortified town         | 20–60+                         | As a stronghold. They will fight.             |

If the band's size tier is clearly above the settlement's available fighters, the settlement yields under duress. If the sizes are close, negotiations may fail and blood follows. If the settlement outmatches the band, there is no leverage — only risk.

### Demanding Tribute

The band arrives at a settlement and makes a demand. This is a MANIPULATION roll at difficulty set by Standing and threat imbalance:

| SITUATION                                            | DIFFICULTY                                                          |
| ---------------------------------------------------- | ------------------------------------------------------------------- |
| Band clearly larger, Standing neutral                | 1                                                                   |
| Band clearly larger, Standing positive (known)       | 0 (auto-succeed with 1 ⚔️)                                          |
| Band and village roughly matched                     | 2                                                                   |
| Village is fortified or has allies nearby            | 3                                                                   |
| Band previously extorted this settlement (same year) | +1 to difficulty                                                    |
| Settlement Standing already -3 or worse              | Roll fails automatically — they have nothing more to give willingly |

On a success, roll or choose from the **Tribute Table** based on settlement size:

| D6 | HAMLET tribute | VILLAGE tribute | LARGE VILLAGE tribute |
|----|---------------------|------------------------|-----------------------------||
| 1 | 2D6 FOOD | 1D6 silver | 3D6 silver |
| 2 | 1D3 FOOD, 1 silver | 2D6 FOOD | 1D6 silver + 5D6 FOOD |
| 3 | 1D3 silver | 3D6 FOOD | 2D6 silver + tools/gear |
| 4 | 1 pelt/hide | 1D3 silver + 1D6 FOOD | 4D6 FOOD + animals |
| 5 | 1D6 FOOD + 1 tool | 1D3 silver + equipment | 2D6 silver + a Named Man surrendered |
| 6 | Work (1 QD labor) | Animals (livestock) | A week of hosted supply (food, lodging, fodder) |

Each ⚔️ on the MANIPULATION roll allows the leader to choose freely from the tribute table result rather than rolling — or to request a specific item. With 3+ ⚔️, the settlement offers what the leader asks for without argument, up to what they actually have.

On a failure, the settlement refuses and Standing drops by 1. The band can force the issue (see Pillaging, below) or back down.

**Repeat visits:** A settlement visited a second time in the same season suffers Standing -1 on top of any roll failure. A third demand in the same season triggers automatic Feud Track +1 regardless of success. The settlement has bled out what it can give willingly.

### Tribute as Standing

A band that demands tribute and takes it is exactly the kind of force that settlements learn to either pay or destroy. Track the interaction:

- First successful tribute: Standing at this settlement drops by 1. The elder paid. They remember.
- Second tribute (same year): Standing drops by 2. They are paying tribute now, not choosing to be generous.
- Third tribute or forced payment: Standing drops to -3 or lower. This settlement is a tributary. It will accept help from anyone who offers to make the band stop.

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

---

## Section 7: Named Men

Named men are veteran fighters with individual stats, names, personalities, and loyalty scores. They are not anonymous soldiers. They have opinions, histories, and lines they won't cross. They are also the band's most dangerous problem when things go wrong.

### Creating a Named Man

Use the SERVANT PERSONALITIES table (Ch09) for name and personality. Then assign each of the following:

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

## Acceptance Summary

These changes are interdependent. Sections 1–6 (band formation, morale, pay, provisions, extortion and tribute, contracts) are the core and should be accepted together. Section 4 (village extortion) can be deferred if the campaign does not involve coercive play against settlements, but it ties the band economy to the Feud Track and should not be omitted from a full implementation. Sections 7–8 (Named Men, wanted status) layer onto the core and can be added separately. Section 9 (atrocities) is self-contained and adds the moral accounting layer. Section 10 requires no changes — it documents integration with existing systems. Section 11 is a new stronghold function and requires only the War Room text.

| #   | CHANGE                             | LOCATION                     | DEPENDENCY        |
| --- | ---------------------------------- | ---------------------------- | ----------------- |
| 1   | Band formation + size tiers        | Ch09 (new section)           | None              |
| 2   | Morale system                      | Ch09                         | 1                 |
| 3   | Fighter tiers + recruitment        | Ch09                         | 1                 |
| 4   | Pay, provisions, field non-payment | Ch09                         | 1, 2              |
| 5   | Village extortion and tribute      | Ch09 + Ch08 cross-reference  | 1, 2, 3, 4        |
| 6   | Contracts and bounties             | Ch09                         | 1                 |
| 7   | Campaign life (QD activities)      | Ch09                         | 1, 2              |
| 8   | Named Men system                   | Ch09                         | 1, 2, 3           |
| 9   | Wanted status                      | Ch09 + Ch08 cross-reference  | 6                 |
| 10  | Atrocities                         | Ch09 + Ch08 cross-reference  | None (standalone) |
| 11  | Integration section                | No text changes — notes only | All above         |
| 12  | War Room function                  | Ch09 functions table         | Independent       |

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

## Open Questions

**✅ 1. COMMAND talent:** Resolved. PATH OF THE COMMANDER (Ch04) is the existing hook. Section 10 now defines how PC leaders with any rank in that talent substitute PERFORMANCE for MANIPULATION on MORALE checks, and how the higher ranks extend into Named Man coordination. No separate COMMAND talent is needed.

**⏸️ 2. Large-scale warfare:** Deferred. This proposal handles bands up to ~50 men. Armies, sieges, and coordinated multi-stronghold campaigns require a separate system. The Host tier (51+ men) flags the boundary but does not solve it. That system, if built, should treat this proposal's output as its atomic unit: a Host is several Warbands, not a different kind of thing.

**✅ 3. Mercenary archetypes by kin:** Resolved. Kin recruitment modifiers are now in Section 2 (Recruitment and Quality) as a table. Elf, Dwarf, Halfling, Wolfkin, Orc, and Goblin each carry specific mechanical note. Notes were kept narrow — modifier to the settlement roll only, not permanent stat effects.

**New open questions from this pass:**

4. **Named Man promotion track:** Can a Named Man with sufficient advancement be promoted to a PC-adjacent role — given a name, a full character sheet, and played as a temporary PC if their original character is out of action? The current advancement rules touch this but don't resolve the full transition. A named man who gains multiple stat increases, develops a clear personality, and completes their Agenda may deserve a more formal path into the fellowship if both player and GM agree.

5. **Band reputation vs. fellowship reputation:** The proposal currently uses the fellowship's Reputation as the band's. This works for small bands but breaks down if the band operates independently for a season while the PCs are elsewhere. A band that commits atrocities while the PCs are absent should not automatically collapse the fellowship's Reputation. Consider a secondary **Band Notoriety** track that runs parallel to fellowship Reputation and can diverge — linked by the fellowship's name but capable of accruing its own consequences.

6. **Named Man death and inheritance:** When a Named Man with high Loyalty and a developed Agenda dies, what happens to the Agenda? If it was close to resolution, other Named Men may carry it forward, or the loss may generate a narrative consequence. No rule covers succession of an Agenda or what Named Men do with a dead comrade's debt or oath.

7. **Band downtime at the stronghold:** The proposal handles field operations but does not define what a Named Man does when the band is home between contracts. Do they count as Guards for the stronghold's Defense Rating? Can they be put to work on a function? Do they require separate housing, or does the BARRACKS cover them? The field-to-garrison transition is mentioned in Section 10 but not mechanized.

8. **Morale cap at 5 (Hungry):** The label "Hungry" for MORALE 5 — meaning eager and dangerous — may confuse tables who read HUNGRY as the resource condition. Rename before integration to avoid collision with the HUNGRY condition in Ch05.
