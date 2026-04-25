# Battles & Sieges: Rules Analysis and Overhaul Proposal

**File status:** Proposal — not integrated into `02-gamemasters-guide/`
**Source chapter:** `02-gamemasters-guide/12-battles-and-sieges.md`
**Date:** 2026

---

## Part 1: Balance Analysis by Subsystem

### 1.1 Battle Line and Troop Dice

The troop dice system is well-calibrated for its purpose. Base dice scale intuitively — a line of militia behaves like 4D6 and loses cohesion at a predictable rate. The base dice cap prevents arithmetic dominance: no troop ever becomes a guaranteed winning line. This is correct.

**Problem: the advantage dice ceiling interacts awkwardly with the base dice cap.** A troop with 4 base dice and 4 advantage dice can roll 8 dice — a formidable total that a small troop with advantages cannot match except through morale. The asymmetry becomes pronounced when the Important Character die stacks on top. Against a weak troop (2D4, no advantages), an optimized troop with commander, flank, size, and an Important Character die achieves a mechanical certainty, not a dramatic tension. There is no rule that limits this compound stacking.

**Problem: the D4 troop is nearly nonfunctional.** At 2D4 against any formed resistance, the expected outcome is less than 2 successes per turn. The morale system does not compensate — morale is spent to prevent rout, not to generate results. A D4 troop that is not routed is still losing attrition three-to-one. Slave Orcs and raw levies are intended to be expendable, but the system offers no mechanism to make their expenditure meaningful.

**Problem: troop size and die type are conflated.** A "well-trained" troop (D8 die type) has the same base dice count as untrained troops of the same size. This makes the well-trained advantage directly proportional — it scales rather than adjusting the floor. Consider: an elite 4-die troop (4D8) against a raw 4-die troop (4D6) maintains a systematic advantage, but two raw 6-die troops (6D6) are typically favored. Numbers dominate training at the troop scale, which is historically correct. What is missing is a rule for well-trained troops holding a number disadvantage better through cohesion.

### 1.2 Morale System

The current morale system is a degradation track that ends in rout. Troops gain morale from Commander PERFORMANCE rolls, an Important Character die, and the General's Speech. They lose it to 1s on any die, attack results, and the Death to Cowards table. The track runs from base Morale Points (equal to die count) down to zero, at which point the troop rolls to break.

**Strength:** The morale system creates meaningful differentiation between winning and losing without making losses arbitrary. The degradation mechanic gives both sides a reason to stay engaged even while losing.

**Problem: morale repair is too easy.** A Commander Rank 1 rally roll can restore 1 morale point as a free action before the troop rolls. With a Rank 3 Commander, repositioning to a new troop restores potentially 3+ morale. This allows a single commander PC to maintain two otherwise broken lines almost indefinitely through rotation. There is no limit on how many turns this cycle can continue.

**Problem: morale and casualties interact poorly for large armies.** A 10-die troop does not break until it has lost far more morale than a 4-die troop. But the damage mechanics do not scale to troop size — both troops take 1 damage per excess enemy success. A 10-die troop is not ten times more durable than a 4-die troop; it simply starts with more points to lose. This means large armies are always preferable over smaller elite ones on a per-die basis, which removes the tactical distinction between mass levies and elite formations.

### 1.3 Siege System

The siege system is functional and structurally distinct from field battle. The wall advantage dice mechanic creates a clear defender benefit, and the supply/starvation track gives sieges a distinct pacing problem. Siege engines add a specialist resource layer the field battle lacks.

**Strength:** The blockade distinction (total vs. partial, cutting supply lines vs. starving all) is the cleanest part of the system. It creates a strategic lever for both sides without adding excess dice.

**Problem: walls scale in a one-dimensional direction.** The advantage dice system for walls (up to +4) is capped, and the repair mechanic gives a night's rest the ability to undo the entire morning's assault. In practice, a successful siege requires consistent assault pressure — the system as written makes this essentially impossible against a double wall, since overnight repair fully restores the advantage. A daily attrition mechanic for walls (partial repair only) would give attackers a realistic path without the overnight reset.

**Problem: the siege engine costs and build times are not integrated into campaign time.** A catapult takes 10 days to build. A trebuchet takes 20. In a campaign that advances at 1–2 hexes per quarter day, the army moves roughly 8–16 hexes per 10-day period. There is no rule for what happens if the army must move during construction. The engines are stranded-or-static tools, and this is never addressed.

**Problem: engineers are a single-point dependency.** Without an Engineer talent, catapults and trebuchets fire at 1/4 effectiveness. An enemy who identifies and targets the engineer PC removes most of the siege capacity in a single battle event. This is dramatic but may break a campaign where siege capability was the tactical cornerstone.

### 1.4 Supply Lines

The supply line rules are the best-designed subsystem in the chapter. The stacking demoralization rules (hunger + forced march + poor sleep = results 1–4 cause demoralization) create a mechanical feedback loop that incentivizes logistical play without requiring the GM to track complex inventories.

**Strength:** Foraging depletion is elegant. A hex depletes by 1 per quarter day, recovers at 1 per week. An army that stays stationary eats the land. This creates genuine pressure to keep armies moving.

**Problem: supply costs in the chapter use two different prices without explicit reconciliation.** The Supplies section specifies 2 copper per supply unit in the field. The Stockpiling section specifies 3 copper per unit when buying from stronghold production. This difference is not explained. A player who reads both sections may assume they can exploit the cheaper field price; a GM who overlooks it may not notice the discrepancy.

**Problem: the Cooking rule (one quarter day dedicated to cooking per day) is not explicitly integrated with the March rules.** A standard day has 4 quarter days. An army that marches 2 quarter days, cooks 1, and sets up camp 0.5 + breaks down camp 0.5 has consumed all 4 quarter days with zero available for battle — unless cooking and marching overlap or camp is skipped (with the associated penalties). The time budget is too tight for a campaign that expects occasional battles.

---

## Part 2: Medieval Authenticity Gaps

### 2.1 Terrain Has No Effect

The most significant authenticity gap in the system is that terrain does not modify battle. A fight on a muddy flood plain and a fight on a dry hilltop produce identical dice — only whether the hill confers a flanking or rear-attack advantage is tracked, and even that is not explicitly addressed. Medieval commanders obsessed over ground. The choice of where to stand was often the decision that won the battle.

### 2.2 Night Attack Is Unrepresented

Night attacks were historical, decisive, and terrifying. Soldiers who could not see their line fall apart. The current system has no rule for conditions of visibility affecting battle dice or morale.

### 2.3 Weather Has No Effect

Wet conditions destroyed ranged combat. Mud neutralized cavalry. Snow and ice restricted movement. None of this affects the current dice at all. Medieval armies that fought in rain suffered specific and predictable degradations that are simply absent here.

### 2.4 Pre-Battle Rituals Are Absent

Champions' duels before battle were a recognized convention in pre-modern warfare and persist in the region's documented history. The battle sequence moves directly from General's Speech to Deployment without any pre-battle negotiation or challenge mechanics.

### 2.5 Post-Battle is a Blank

Medieval armies stripped the dead. Ransomed prisoners. Pursued routing enemies. Experienced surgeons at the field hospital. Surrendered on negotiated terms. None of this is in the current system. The battle ends when one side routs, and the next scene is whatever the GM decides.

### 2.6 Looting Does Not Feed Armies

The chapter notes that promising plunder to soldiers is how armies are paid. But there are no rules for what plunder consists of, what it is worth, or how distributing it affects cohesion and morale. The promise of plunder is mentioned only as a salary deferral mechanism.

---

## Part 3: Rules That Are Too Simple

### 3.1 Commander Rules Do Not Vary by Troop Type

The Commander talent applies uniformly to all troop types — infantry, cavalry, skirmishers. A skilled cavalry commander granting bonuses to a skirmisher line, or an infantry commander rallying cavalry, produces the same mechanical result as a tactically appropriate assignment. There is no rule that Commander effectiveness varies by the troop being led.

### 3.2 The General's Speech Is One Roll

The General's Speech is a PERFORMANCE roll made once before battle. It has three outcomes (fail/pass/push). This is mechanically light for an action the GM is expected to roleplay. A general who composes their speech carefully, invokes the right symbols, and speaks at the right time should have more mechanical levers than a straight skill check.

### 3.3 Flanking and Rear Attacks Have No Cost

Flanking grants a free advantage die. Rear attack grants a free D8. There is no description of what it requires to achieve a flank, how the enemy responds to being flanked, or whether a flanked troop gets a reaction. This turns flanking into a setup cost (positioning) without any interactive layer.

### 3.4 Battle Events Use Only Five Tables

The D66 tables cover: Monsters, Cavalry, Infantry, Attacker Sieges, Defender Sieges. There is no table for fighting elite humanoids (dwarven warriors, Redrunners), no table for fighting undead or demonic armies, no table for naval combat or river crossing under fire. Each enemy category that produces distinctive tactical situations should have its own table.

---

## Part 4: Missing Fantasy Tropes

### 4.1 Battle Magic

Mages are not represented as a troop type or an Important Character variant that affects the battle roll. The Battle Events table includes "a defender casts spells from the wall" and "an enemy raises an artifact" as individual events, but there are no rules for fielding a dedicated mage unit, or for a PC mage contributing to a battle outside of the Important Character die.

### 4.2 Aerial Units

Griffon riders, wyvern cavalry, and similar aerial units have no rules. They cannot be assigned a troop type. The size advantage die rule could apply (a wyvern is larger than infantry), but the aerial dimension — attacking from above, immunity to polearm attack angles, vulnerability to ranged fire — is entirely absent.

### 4.3 Undead and Demonic Armies

Undead do not flee. Demonic troops do not succumb to demoralization in the same way living soldiers do. There is no rule for commanding armies that do not use the standard morale system. A GM who needs to run an Undead assault on a walled town is working entirely by improvisation.

### 4.4 Betrayal and Defection

A unit that secretly serves the enemy — or a commander who changes sides mid-battle — has no mechanical representation. This was historically devastating and narratively rich.

### 4.5 Relief Forces Arriving Mid-Battle

An army being besieged that is relieved by an outside force creates a mid-battle addition of new troops. The current system has no rule for inserting fresh dice mid-sequence.

---

## Part 5: Exact Proposed Rules

Each overhaul below is written as final rules text. Integrate into `02-gamemasters-guide/12-battles-and-sieges.md` at the indicated location.

---

### P5.1 Terrain and High Ground

**Insert as a new subsection under `## Special Combat Conditions`.**

---

#### Terrain

The ground beneath an army's feet changes the fight. Before deployment, the GM assigns one terrain type to each section of the battlefield.

**High Ground.** A troop deployed on elevated ground — a hill, a ridge, a raised road — gains 1 advantage die. Cavalry descending from high ground at a charge gains an additional D6, but a cavalry troop charging uphill loses 1 base die.

**Muddy or Wet Ground.** Heavy rain or waterlogged soil slows cavalry significantly. Cavalry troops rolling on wet ground reduce their base dice by 1. Infantry and skirmishers are unaffected.

**Forest or Broken Ground.** Cavalry cannot enter broken ground — rocky scree, dense woodland, marsh. Any cavalry troop ordered to advance through it loses its attack for that turn. Infantry and skirmishers move freely.

**River Crossing.** A troop crossing a river or ford while under fire uses half their base dice for the attack roll on the crossing turn. Once across, they roll normally.

**Prepared Ground.** A defending general who has held ground for 24 hours may prepare it with stakes, ditches, or obstacle lines. Cavalry attacking into prepared ground loses 2 base dice on the attack roll.

---

### P5.2 Weather

**Insert as a new subsection after `### Terrain`.**

---

#### Weather

Roll D6 at the start of each battle. On a 1, the weather is adverse.

| D6 | CONDITION |
|---|---|
| 1 | Rain or snow. All ranged attacks lose 1 die. Cavalry movement reduced to infantry rate. |
| 2 | Fog. Both sides roll only half their advantage dice (round up). No flank or rear die on first turn. |
| 3 | Hard cold. Troops begin with 1 fewer morale point. Accumulated demoralization triggers on 1 and 2 immediately, even on the first turn. |
| 4 | Wind from the west. Ranged attacks with light ranged weapons lose 1 die if firing into the wind, gain 1 die if firing with it. |
| 5 | Dust cloud. As fog, but begins on the second turn and resolves on the third. |
| 6 | Unseasonably hot. After 3 battle turns, each troop loses 1 base die to exhaustion. |

Re-roll for each session day. Weather in sieges does not change mid-siege unless the GM indicates a seasonal shift.

---

### P5.3 Night Attack

**Insert as a new subsection after `### Weather`.**

---

#### Night Attack

A general may launch an attack between sundown and dawn. Night attacks are nearly always the initiative of the attacker — defenders in a prepared camp have warning time only if they maintain sentries.

**If the defending camp has no sentries:** The attacker gains a free first turn. The defending side does not roll in that turn. They are woken, not fighting. From the second turn, the battle continues normally.

**If sentries are present:** Both sides roll normally, but advantage dice are halved (rounded up) for both sides for the first 2 turns. Night is chaos for everyone.

**Torchlight.** A defending force that has lit torches removes the advantage dice penalty for themselves only. Attackers in the torchlight are easier to target — defenders regain their full advantage dice on the second turn.

A night attack requires the attacking general to have a Commanding SCOUTING roll to move troops in darkness without them becoming disorganized. Failure means the attacking force loses 1D3 base dice to confusion before the first roll.

---

### P5.4 Champion's Duel

**Insert as a new subsection under `### General's Speech`, before `## Deployment`.**

---

#### The Challenge

Before deployment, a commander or champion may issue a challenge to the opposing side — single combat to settle the dispute, avoid the battle, or simply demonstrate the force of will behind the line.

Both sides must agree. If the challenge is refused, the side that refused loses 1D3 morale points across all troops — seen as cowardice.

**If accepted:** The duel resolves in standard personal combat. The winner's side gains morale points equal to the victor's current Strength attribute. The loser's side loses the same number. The battle still occurs — a champion's duel is theater as much as resolution.

**PC champions:** A PC who accepts may substitute a relevant skill for MELEE at the GM's discretion — a bowmaster might request an archery duel, a diplomat might request a verbal contest decided by MANIPULATION. The opposing commander may accept or reject the alternate format. The morale stakes apply regardless of format.

---

### P5.5 Feigned Retreat

**Insert as a new subsection under `### Commander Movement`.**

---

#### Feigned Retreat

A cavalry or skirmisher troop under the command of a trained officer may execute a feigned retreat — appearing to break, drawing the enemy forward, then turning to strike.

**The roll:** The commanding Important Character or commander makes an Opposed roll: their PERFORMANCE against the opposing general's INSIGHT. If they win, the troop executes the feigned retreat and may immediately re-enter combat on the next turn with a free advantage D8 (the pursuit die). If they lose, the retreat becomes genuine — the troop must make a morale roll this turn.

A feigned retreat may be attempted once per troop per battle. It cannot be used by infantry except in exceptional circumstances at GM discretion.

---

### P5.6 Battle Magic

**Insert as a new subsection after `### The Important Character Die`, before `### Commanders and Important Characters`.**

---

#### Mages and Sorcerers in Battle

A PC or named NPC with magical abilities functions as an Important Character and rolls their advantage die as normal. However, they may choose to cast a spell directly affecting the battle instead of receiving a Battle Event.

**On any battle turn, a mage may sacrifice their advantage die roll to cast one spell.** The troop does not benefit from the advantage die this turn. The mage resolves the spell normally, but replaces the spell's roll with a number of dice equal to the troop's remaining base dice, choosing a skill as applicable (INSIGHT for Mentalism, MANIPULATION for illusions, MIGHT for Animalism, etc.). The spell's effects apply only to one adjacent troop section — it cannot alter an entire battle at once.

**Spells that deal damage:** Convert the spell's damage result to troop damage — every 2 spell damage equals 1 troop damage to the target.

**Spells that affect conditions:** Fog, fire, slowing terrain — these impose the same penalties as the corresponding Weather or Terrain conditions for 1D3 turns.

A mage who is Broken stops using their advantage die for battle rolls and may no longer cast battle spells that turn.

---

### P5.7 Aerial Units

**Insert as a new subsection after `## Notes on Mounts and Size`.**

---

#### Aerial Units

Aerial units — griffon riders, wyvern cavalry, flying creatures directed by handlers — use the cavalry troop type with the following modifications:

**Cannot be engaged.** Aerial units cannot be placed in the General Melee line unless they choose to land. Until they do, infantry and polearms cannot reach them and deal no damage. Only ranged troops and artillery engage aerial units normally.

**Charge from above.** An aerial unit that charges counts as flanking — gaining the flank advantage die. In addition, aerial attackers are immune to the polearm bonus against cavalry.

**Size advantage die.** A large aerial unit (wyvern, giant eagle) gains the size advantage die against infantry automatically.

**Vulnerability.** Aerial units take double damage from ranged critical successes — precision fire against a visible, moving target in the air is rewarded. A result of three or more successes on a ranged attack against an aerial unit deals 2 damage instead of 1.

---

### P5.8 Undead and Demonic Armies

**Insert as a new subsection after `### Aerial Units`.**

---

#### Undead and Demonic Troops

Some armies in the Ravenlands have no morale to break. Undead do not fear. Demonic entities do not surrender. These forces follow a modified rule set.

**Morale Immunity.** Undead and demonic troops do not track morale points. They cannot be affected by PERFORMANCE rolls, the General's Speech, or Death to Cowards. They never rout. Their dice are reduced only by actual damage results.

**No Supplies.** Undead troops do not require food, water, or sleep. Supply-based starvation rules do not apply to them. A siege by an undead host does not end due to the attacker's food running out.

**Commander Dependency.** Undead troops are controlled by a necromancer, lich, or dark commander. If this commander is eliminated — through an Important Character die result, a Battle Event, or direct action — all undead troops immediately lose half their remaining base dice (rounded up) as the control binding fractures. Further turns without a controller: reduce base dice by 1 per turn until they collapse or a new controller takes the field.

**Demonic troops** do not collapse without a commander, but they do not coordinate — each troop rolls as though it has no flanking or rear advantage, regardless of positioning. The fear they generate, however, imposes an automatic -1 morale point per turn for any troop engaged with them for the first three turns.

---

### P5.9 Pursuit of Routing Troops

**Insert as a new subsection after `### Troop Regrouping`.**

---

#### Pursuit

When a troop routes, the victorious side may pursue. A pursuing troop must have cavalry or skirmishing cavalry available; infantry cannot effectively pursue a routing force.

**The pursuit roll:** The pursuing cavalry troop rolls their full dice against the routing troop's remaining base dice. Results are applied as damage, removing fleeing soldiers from the field entirely.

**The cost of pursuit:** A cavalry troop that pursues leaves the main battle line. They cannot participate in that battle turn's main roll. If the main battle line suffers a reversal while the cavalry pursues, they cannot reinforce.

A general who orders pursuit risks winning the flank and losing the center. This is a conscious choice.

---

### P5.10 Ransom and Post-Battle Aftermath

**Insert as a new section `## Aftermath` before the final attribution note.**

---

## Aftermath

When the last troop routes or surrenders, the dice stop. The battle is over. What happens next is not abstracted.

### Prisoners and Ransom

Important Characters captured in battle — those whose last base die was eliminated — are held alive unless the victor explicitly kills them. In the Ravenlands, a live prisoner with rank or talent is worth money.

**Ransom negotiations** use MANIPULATION or INSIGHT against the captor's standing. The values below reflect rough market expectations:

| CAPTURED CHARACTER | RANSOM VALUE |
|---|---|
| Common soldier | 5–10 copper |
| Troop commander (no important character) | 25–100 copper |
| Important Character, no title | 100–500 copper |
| Named noble or general | 500–2,000 copper |
| PC | Negotiated by the table |

Captors who kill prisoners forgo ransom. Captors who treat prisoners poorly risk the same treatment for their own soldiers when captured in turn.

### Stripping the Dead

An army that controls the field after the battle may loot the bodies of the fallen. For every 10 base dice worth of destroyed enemy troops, the victors may roll 2D6:

- A result of 10+ yields a usable weapon or piece of armor.
- A result of 5–9 yields D6 × 10 copper in salvage value.
- A result of 1–4 yields nothing salvageable.

Stripping takes one quarter day. An army that strips the dead cannot begin marching or foraging during that time.

### Wounded

After any battle in which a troop was eliminated, roll D6 for each important character who was in that troop and was not confirmed killed. On a 5+, the character survived with wounds — they are Broken and must be treated with HEALING before the next battle or they die.

---

### P5.11 Expanded Death to Cowards

**Replace the existing `Death to Cowards` paragraph with the following.**

---

#### Death to Cowards

When a troop routs in the presence of their own general, the general may order the execution of those who fled. This is the ancient right of commanders and the oldest method of making the fear of retreat worse than the fear of the enemy.

**Executing cowards:** The general selects up to 1D6 soldiers from the routing troop. Those soldiers die. The troop loses those base dice permanently.

**Effect on the army:** All other troops that witnessed the execution must each roll a morale check. On success: the troop gains 1 morale point — the lesson was understood. On failure: the troop loses 1 morale point — the lesson inspired the wrong emotion.

**Post-battle morale check.** In the rest period following any battle in which Death to Cowards was used, all surviving troops make a MORALE roll at the start of the next session. Troops that fail begin the next engagement with 1 fewer morale point than their starting total.

The general who uses this tool has borrowed the loyalty of their army against the loan of its fear. Interest is charged in the battles that follow.

---

### P5.12 Veterans: A Tier Above Well-Trained

**Insert as a new row in the Advantage Dice table and add the following subsection.**

---

#### Veterans

A troop that has survived three or more battles without being destroyed may be designated **Veterans** at the GM's discretion. Veterans gain the following:

- Their die type increases by one step (D6 → D8, D8 → D10, D10 → D12). This stacks with Well-trained.
- They do not make morale checks unless their morale is reduced to zero — the first morale check is waived each engagement.
- When their commander is killed or captured, they roll their morale at Formidable difficulty instead of Normal.

Veterans cannot be recruited. They can only be earned. An army that has no veterans has never fought together long enough to trust each other in the dark.

---

*Proposal prepared for Forbidden Lands 2E revision. These rules are staged for review and integration. None of the above is canonical until explicitly merged into* `02-gamemasters-guide/12-battles-and-sieges.md` *and the chapter changelog updated.*
