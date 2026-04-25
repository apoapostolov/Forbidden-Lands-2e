# Battles & Sieges Chapter 12 — Second-Pass Audit and Proposal

## Scope

This audit reviews `02-gamemasters-guide/12-battles-and-sieges.md` after the first overhaul pass was integrated.

The first pass solved the largest structural absences:

- terrain
- weather
- night attack
- challenge duel
- feigned retreat
- battle magic
- aerial troops
- undead and Misgrown troops
- pursuit
- aftermath scaffolding
- expanded Death to Cowards
- veterans

This second pass asks a narrower question:

What is still missing, underrepresented, procedurally weak, or too sanitized for a chapter about organized war in the Ravenlands?

## Overall verdict

Chapter 12 is now mechanically credible, but it still has a few exposed seams.

The chapter is strongest when armies are already in motion and dice are already being rolled. It is weaker when the conflict shifts into the ugly human spaces around battle:

- siege negotiation
- surrender
- hostages and bad faith
- partial blockade and smuggling
- pay failure, desertion, and mutiny
- sack, punitive violence, and the destruction of a place after storming it

It also still contains one real procedure gap:

- **morale rolls are referenced repeatedly but not explicitly defined as a reusable resolution procedure**

That is the cleanest missing system in the chapter.

## Missing or underrepresented areas

### 1. Siege diplomacy is present as flavor, not as procedure

The chapter says generous terms are offered before a breach and worse terms after one, which is correct, but it does not yet give the GM a usable procedure for:

- opening parley
- contesting terms
- determining what concessions change hands
- handling hostages, disarmament, safe conduct, or oaths
- punishing bad faith mechanically

This leaves one of the most historically important parts of siege warfare in pure GM improvisation.

### 2. Partial blockade has no live rule loop

The chapter defines what a full blockade requires, but not what happens when the besieger is short of the needed force.

Missing procedure:

- smuggling or supply runs into the fortress
- messenger traffic
- relief coordination
- interception attempts by the besieger

This matters because many Ravenlands sieges should be leaky, improvised, and badly held rather than perfect rings of steel.

### 3. Pay failure is described but not resolved

The chapter correctly states that unpaid troops desert, threaten, or turn predator. It does not yet give a turn-by-turn procedure for:

- testing a troop's loyalty when pay is late
- commander attempts to steady them
- staged escalation from grumbling to desertion to mutiny

This is the clearest missing campaign procedure after morale.

### 4. Sack and punitive occupation are too cleanly implied

The chapter discusses stripping dead, ransom, starvation, and village over-extraction. It still stops short of a direct rule for what happens when a place is stormed and the victors choose between:

- mercy
- controlled sack
- open sack

That omission matters both mechanically and tonally. Medieval war did not end when a gate fell. Very often, that was when the worst part began.

### 5. Ransom has value bands but not negotiation procedure

The chapter gives strong ransom values, but no actual method for resolving:

- hard bargaining
- exchanged hostages
- oaths of non-aggression
- surrender of named captives or standards

This is a smaller issue than pay or parley, but still a real procedural hole.

## Missing procedural systems or undefined checks

### 1. Morale roll is undefined

The chapter repeatedly says troops make a morale roll or morale check, but it never states the reusable procedure.

That should be fixed first.

### 2. No check for leaky blockade events

A partial blockade currently has no roll loop.

### 3. No check for missed pay

Unpaid troops are described narratively, but there is no trigger -> roll -> consequence structure.

### 4. No check for surrender negotiations

The chapter contains the historical truth but not the game procedure.

## Tone areas still too clean

The chapter is already harsher than before, but some passages still stop one step before the thing itself.

### 1. Aftermath is still restrained where it should sometimes be ugly

This is mostly a matter of omission, not weak prose. The chapter names ransom and stripping the dead, but not:

- women and boys carried off
- captives maimed for terror
- false surrender terms
- commanders preserving order at the cost of denying their own men expected plunder
- the fact that sack destroys future tax ground as surely as starvation does

These should not be written graphically. They should be written plainly.

### 2. Salaries describes the logic of mutiny but not its smell

The present text explains failed pay well, but it stays in summary voice. A war chapter benefits from one or two sharper truths:

- men drift away at dawn with stolen tack and unpaid anger
- officers are seized in their sleep
- hungry soldiers loot those they were sent to protect

Again: plain, not theatrical.

### 3. Siege terms need more medieval hardness

The current siege section knows that pre-breach terms are better. It does not yet state the older truth plainly enough:

- a place that forces an assault often forfeits mercy
- a commander who lies under truce may win once and then never be believed again
- hostages, standards, named men, and relics are bargaining matter, not noble scenery

## Proposed second-pass additions

### P6.1 — Define the morale roll

Add a short reusable procedure under `#### Morale Points`.

**Rule goal:** give every later morale check a common engine.

**Proposed procedure:**

- roll a number of D6 equal to the troop's current morale points
- any success means the troop holds
- no success means the morale roll failed
- the calling rule determines what success and failure do

This is the cleanest fix in the whole pass.

### P6.2 — Add leaky blockade and supply-run procedure

Insert under `#### Blockade`.

**Rule goal:** make incomplete sieges active rather than binary.

**Procedure:**

- once per week, if blockade is incomplete, the defenders may attempt one run
- defender rolls `SCOUTING` or `MANIPULATION`
- besieger rolls `SCOUTING` or `INSIGHT`
- defender win: messenger, supplies, or small reinforcements get through
- besieger win: run is broken, goods or messenger are taken, and the defender learns the ring is tighter than hoped

### P6.3 — Add surrender, parley, and bad-faith procedure

Insert after `#### Blockade` or as a new siege subsection before `#### Repairing Defenses`.

**Rule goal:** make siege diplomacy playable.

**Procedure:**

- both commanders choose whether to parley
- opposed roll using `MANIPULATION`, `INSIGHT`, or `PERFORMANCE` as appropriate
- extra successes buy or deny terms:
  - safe conduct
  - sidearms retained
  - hostages given
  - stores surrendered
  - named prisoners released
  - oath not to return for a season
- if sworn terms are broken, future surrender offers from that commander become harder because word spreads

### P6.4 — Add missed pay procedure

Insert under `### Salaries`, after `#### When Payment Fails`.

**Rule goal:** turn late pay into an actual campaign pressure track.

**Procedure:**

- before affected troops roll, the general or a commander may attempt `PERFORMANCE` or `MANIPULATION`
- each success steadies one troop for that week
- each affected troop then makes a morale roll
- on success, it loses morale but stays in hand
- on failure, it loses morale and sheds men or begins mutiny
- repeated unpaid weeks escalate the outcome

### P6.5 — Add storm, sack, and mercy procedure

Insert under `### Aftermath`.

**Rule goal:** make the fall of a place feel materially and morally different depending on how it was taken.

**Procedure:**

After a breached place falls, the victor chooses one:

- **Mercy** — little immediate plunder, but future order remains possible
- **Ordered Sack** — gains plunder and supply, but discipline frays and morale suffers
- **Open Sack** — gains the most immediate wealth and terror value, but destroys prisoners, spreads disease, hardens future resistance, and makes later surrender negotiations harder

This is the strongest missing tone-and-system addition in the chapter.

### P6.6 — Add coercive collection and occupation procedure

Insert under `#### Village Contributions` and `### Aftermath`.

**Rule goal:** make wartime rule over people and places feel immediate, ugly, and mechanically consequential rather than implied off-page.

**Procedure:**

- when a village refuses contribution, the commander chooses hostages, quartering, or exemplary punishment
- each choice yields immediate compliance in a different way but worsens Standing, burden, or feud
- when a place is taken and meant to be held, the victor must leave a troop behind and choose whether occupation rests on oaths and hostages, ordinary garrison rule, or terror

This is the key bridge between Chapter 12 conquest and Chapter 11 political aftermath.

## Recommended implementation order

1. `P6.1 Morale roll`
2. `P6.2 Leaky blockade`
3. `P6.3 Parley and bad faith`
4. `P6.4 Missed pay`
5. `P6.5 Storm, sack, and mercy`
6. `P6.6 Coercive collection and occupation`

That order fixes the cleanest procedure gap first, then the biggest strategic hole, then the most important human-war omissions.

## Immediate implementation target

For this pass, the highest-value first implementation set is:

- define morale rolls
- add leaky blockade
- add surrender/parley/bad-faith rules
- add missed pay procedure
- add storm/sack/mercy rules
- add coercive collection and occupation rules

Those changes are all small enough to fit the current chapter structure without redesigning the battle engine.

## Final recommendation

Do not rewrite the whole chapter.

The battle engine is already strong. What it needs now is not another total overhaul. It needs the ugly connective tissue that makes armies feel like collections of hungry, frightened, acquisitive human beings rather than only colored dice on a field.
