<!-- markdownlint-disable MD013 -->

# Proposal: Hunting Realism — Season, Weather, Animals, and the Quarter Cycle

## Purpose

The hunting rules in Chapter 8 have not been updated to match the weather, season, and terrain framework built elsewhere in the same chapter. The result is a system where weather rolls and seasonal tables shape everything _except_ hunting. A storm has no effect on the hunter. Winter has no effect on prey. The animal table gives you a mouse as the low result and makes a deer easier to kill than a fox.

This proposal corrects four interlocked gaps:

1. Hunting has no season modifier.
2. Hunting has no weather modifier.
3. The animal table is unrealistic in species, kill difficulty, and yield.
4. The terrain table assigns the wrong HUNT modifier to Marshlands.

Two secondary improvements are also included:

5. Meat spoilage ignores temperature.
6. `MASTER OF THE HUNT` ranks 2 and 4 are generic copies of the same talent structure that appears in `HERBALIST`, `FISHER`, and `PATHFINDER`.

This is not a subsystem rebuild. Every change is a modifier addition, a table correction, or a one-sentence rule update.

---

## The Setting Context

The Forbidden Lands is pre-feudal wilderness. Three centuries under the Blood Mist killed off or scattered the old order. What remains is a patchwork of surviving villages, warchief strongholds still under construction, and land that nobody has walked in living memory. The adventurers are not peasants worrying about a lord's gamekeeper. They are people pushing into country where the nearest other human settlement may be two days' travel away and the forest past the next ridge has not been entered since before the Mist fell.

Hunting in this world is not a legal problem. It is a survival act in unmapped terrain. The woods hold animals but also things that hunt back — beasts warped by decades of demonic proximity, monsters that have colonized empty territory, the occasional sign that something worse has been through. A hunter who goes out alone for two quarters and does not return is not news. It happens.

What this means for the mechanics is that the pressure on hunting is ecological and physical, not social. The seasons still dictate when animals are fat, when they are breeding, when tracks are legible in frozen ground, and when thick summer cover makes approach nearly impossible. The weather still determines whether you can hear movement, read scent, or hold a bowstring steady. These are the constraints that matter. They always were.

---

## Current Problems

### 1. No Season Modifier for HUNT

The `SEASONS` table at the end of the `FORAGING` section gives FORAGE modifiers by season. There is no equivalent for HUNT. The table ends:

| SEASON | FORAGE |
| ------ | ------ |
| Spring | -1     |
| Summer | 0      |
| Autumn | +1     |
| Winter | -2     |

Nothing tells the GM or player that hunting in deep winter is different from hunting in autumn. It is not. In autumn, deer are rutting, ranging wide, and fat. A skilled hunter can read them. In spring, game is lean, nursing young are everywhere, and taking breeding animals strips the land of future food. Summer visibility is choked by undergrowth; animals are at peak fitness and alert. Winter opens the landscape and shows tracks in snow but shortens the viable hunting day and punishes exposure.

**Resolution:** Add a HUNT column to the SEASONS table.

| SEASON | FORAGE | HUNT |
| ------ | ------ | ---- |
| Spring | -1     | -2   |
| Summer | 0      | -1   |
| Autumn | +1     | +1   |
| Winter | -2     | 0    |

Spring -2: Game is lean from winter. Nursing animals are everywhere. Taking them strips next year's food. Even a skilled hunter finds little worth killing.

Summer -1: Thick undergrowth breaks sight lines. Animals are at peak fitness and wariness. Heat spoils meat fast. This is not a hunting season.

Autumn +1: Animals are fat. Deer and boar follow rutting patterns — predictable, preoccupied, and ranging openly. Pelts are at full quality. This is the season.

Winter 0: Snow reveals every track. Animals group together and move less. But the day is short, cold exposure is real, and fresh meat spoils slowly — which means the kill must be hauled back before dark. The advantages and penalties cancel.

---

### 2. No Weather Modifier for HUNT

The weather rules in `EXPANDED WEATHER` apply modifiers to `LEAD THE WAY`, `MAKE CAMP`, and `FORCED MARCH`. They do not touch `HUNT`. A hunter going out in a downpour gets the same odds as one in clear dawn light.

Medieval hunters knew better. Rain covered scent and sound, but also softened the ground, swelled rivers, and drove game into cover. Wind made reading sound impossible. Snow revealed everything. Storms made hunting nearly impossible — not from rule, but from the impossibility of hearing, seeing, or staying still.

**Resolution:** Add weather modifiers to the HUNT activity.

Apply these modifiers when using active weather rules:

- **Strong Wind:** HUNT -1. Animals are nervous. The hunter cannot hear movement or calls. Sent drifts unpredictably.
- **Rain or Drizzle:** HUNT -1. Game seeks shelter. Ground is soft and loud underfoot.
- **Downpour:** HUNT -2. Driving rain drowns sound, sight, and track. Most game will not move.
- **Storm:** HUNT not possible this Quarter Day.
- **Snowfall (active):** +1 to the initial SURVIVAL roll only. Tracks are visible and fresh. The kill roll is unaffected.
- **Clear skies in Winter:** HUNT +1. Hard frozen ground is quiet underfoot. Tracks from the night before are still legible.

These stack with the existing `DARKNESS` penalty and with the new season modifiers above.

---

### 3. The Animal Table Is Wrong

**Current table:**

| D6  | ANIMAL | DIFFICULTY | REQUIREMENT    | MEAT | PELTS |
| --- | ------ | ---------- | -------------- | ---- | ----- |
| 1   | Mouse  | +1         | Weapon or trap | 1    | —     |
| 2   | Crow   | 0          | Weapon         | 1    | —     |
| 3   | Rabbit | +1         | Weapon or trap | 2    | 1     |
| 4   | Fox    | -1         | Weapon or trap | 3    | 1     |
| 5   | Boar\* | -1         | Weapon         | 4    | 2     |
| 6   | Deer   | 0          | Weapon         | 5    | 3     |

Problems by row:

**Mouse (1):** Nobody hunts mice deliberately as subsistence game. Even in genuine subsistence conditions, mice represent trap-caught vermin, not hunted prey. The result is tonally wrong — a skilled hunter spending a Quarter Day to come back with a mouse reads as absurd.

**Crow (2):** The weapon-only restriction makes no sense for a bird. Crows cannot be reliably trapped because they are too wary of baited traps. Hunting one with a bow or sling is an opportunistic shot, not a Quarter Day activity. If crows appear here, the row should represent game birds broadly — partridge, pigeon, dove — which were heavily hunted in medieval Europe by exactly the methods available to poor and landless people: lime-stick, net, snare, and short-bow.

**Fox (4):** Difficulty -1 (harder than crow and rabbit) but 3 meat (more than rabbit) and available by trap. Foxes weigh roughly 5–7 kg. Dressed yield is 1–2 kg of stringy meat — the flesh was eaten in times of need but is not a primary food source. The pelt is what matters. The 3 meat is overstated; the 1 pelt is understated; the difficulty -1 is the only accurate number.

**Boar and Deer difficulty inversion:** Boar is -1, deer is 0. That makes a wounded boar in cover _the same difficulty to kill_ as a deer at medium range. Boar difficulty should reflect its lethality — more dangerous than -1. Deer should be harder to kill than the table implies — deer are notoriously difficult to approach and require a clean shot to drop.

**Resolution:** Replace the animal table.

| D6  | ANIMAL      | DIFFICULTY | REQUIREMENT    | MEAT | PELTS |
| --- | ----------- | ---------- | -------------- | ---- | ----- |
| 1   | Squirrel    | +1         | Weapon or trap | 1    | 1     |
| 2   | Game birds† | +1         | Weapon or trap | 1    | —     |
| 3   | Hare        | +1         | Weapon or trap | 2    | 1     |
| 4   | Fox         | 0          | Weapon or trap | 2    | 2     |
| 5   | Boar\*      | -2         | Weapon         | 5    | 2     |
| 6   | Deer        | -1         | Weapon         | 5    | 3     |

_\* Boar attacks you if you fail._

_† Partridge, pigeon, dove, or similar. In Marshlands or next to a lake or river, treat this result as Waterfowl (duck, coot, heron) with the same stats._

**Change notes:**

- Squirrel replaces Mouse. Squirrels were trapped and eaten. Squirrel pelt (vair) was used for winter cloak lining. This is historically accurate and makes sense as a skill-low result.
- Game birds replace Crow. Wild birds are the medieval peasant's most reliable small-game quarry. Trap or weapon applies because snares, lime, and nets (all "traps") were the primary method. The Waterfowl note is terrain-specific: in marshes and near water, the same roll represents waterfowl instead.
- Hare replaces Rabbit. Hares are the wild animal you actually encounter in open and forested terrain. They are faster and more alert than domestic rabbits. Mechanically identical except in name; the feel is accurate.
- Fox: Difficulty adjusted from -1 to 0 (neutral). Meat reduced from 3 to 2 (accurate dressed weight). Pelts increased from 1 to 2 (fox pelt is genuinely valuable). Fox remains trap-accessible.
- Boar: Difficulty tightened from -1 to -2. The boar is the most dangerous animal a wanderer is likely to encounter outside monsters. A failed kill roll should be genuinely threatening. Meat increased to 5 (a boar is a large animal — dressed yield easily exceeds a deer for smaller breeds).
- Deer: Difficulty tightened from 0 to -1. A deer at rest is hard to approach unseen. A clean kill requires position and patience. Meat held at 5 — roe deer and larger woodland deer are similar in yield. Difficulty increase compensates for the same yield as boar with no counter-attack risk.

---

### 4. Marshlands HUNT Modifier Is Wrong

**Current terrain table (HUNT column):**

| Marshlands | -1 |

The in-text HUNT modifier list reads: "-1 in Mountains, Marshlands, or Ruins."

Mountains and Ruins being poor hunting ground is correct. Marshlands is not. Marshes are among the most productive hunting environments in medieval Europe. Waterfowl in vast numbers, otter, beaver, eel, and wading birds all concentrate in marshland. Noble hunters valued marshland hunting highly enough to build permanent blinds and maintain decoy flocks. Peasants living near marshes were better fed than their inland counterparts specifically because of marshland game.

The -1 probably represents movement difficulty. But movement difficulty is already modeled: Marshlands requires a raft. Adding -1 to HUNT double-penalizes terrain that should reward hunters.

**Resolution:** Change Marshlands HUNT from -1 to +1.

Update both the terrain table and the in-text modifier list.

Revised terrain table (affected rows only):

| TYPE       | MOVEMENT        | FORAGE | HUNT |
| ---------- | --------------- | ------ | ---- |
| Marshlands | Requires a raft | +1     | +1   |

Revised in-text list:

> - +1 in Plains, Forest, or Marshlands.
> - 0 in Dark Forest, Hills, Quagmire, or Lake/River.
> - -1 in Mountains or Ruins.

Marshlands-specific note: When hunting in Marshlands or in a hex adjacent to a lake or river, a result of 2 on the animal table (Game birds) can be treated as Waterfowl if a ranged weapon is available.

---

### 5. Meat Spoilage Ignores Temperature

**Current rule:** "You need to do this within a day, or the MEAT will be spoiled."

This applies identically in summer heat and in winter cold. In practice, a deer taken in August heat begins spoiling within hours. A deer taken in January frost will hang for days without rot.

The existing `HEAT` table tracks temperature, and the `SLEEPING GEAR` section already distinguishes hot and cold conditions. Spoilage should respect the same axis.

**Resolution:** Replace the single-sentence spoilage rule with a temperature-sensitive version.

> **MEAT AND SPOILAGE.** How long MEAT keeps before it rots depends on temperature. In summer heat (HEAT 3 or higher), raw MEAT must be eaten or cooked before the end of the current Quarter Day. In normal conditions, MEAT keeps for one day as normal. In winter cold (HEAT 0 or lower), raw MEAT keeps for D3 days before it spoils. Cooked MEAT spoils at the same rate but can be salted or smoked by a CHEF to extend its shelf life by one day — this requires TINDERBOX and SALT.

This rule applies equally to FISH and VEGETABLES. A successful CHEF roll in camp extends MEAT by one day in any temperature.

---

### 6. MASTER OF THE HUNT Talent Revision

**Current talent:**

- RANK 1: +1 to SURVIVAL when HUNT.
- RANK 2: Hunting Quarter = REST.
- RANK 3: Roll two D6 on the animal table, choose the result.
- RANK 4: Extra ⚔️ on initial roll = additional animals found.
- RANK 5: Replace +1 with D10.

Ranks 2 and 5 are copies of the same structure used in HERBALIST, FISHER, and PATHFINDER:

- HERBALIST rank 2: Foraging Quarter = REST.
- FISHER rank 2: Fishing Quarter = REST.
- PATHFINDER rank 2: Leading the Way Quarter = REST.
- MASTER OF THE HUNT rank 2: Hunting Quarter = REST.

All four are identical text. This is a design shortcut that makes the talents feel interchangeable and flattens the character of each.

Rank 3 (choose between two animal results) is distinctive and well-designed. Rank 4 (extra ⚔️ = extra animals) is reasonable and has no equivalent in the other talents.

The revision targets ranks 2 and 4.

**Revised talent:**

- **✦ RANK 1:** Your SURVIVAL roll is modified by +1 when you HUNT during journeys. While hiking and passing through a hex you have not hunted in, you may note animal signs and make one forward guess about what large game uses it. The GM confirms or denies. This costs no Quarter Day action.
- **✦ RANK 2:** A Quarter Day spent HUNTING counts as RESTING. In addition, traps you set work while you are absent — you do not need to stay in the hex to monitor them. A trap you set is checked when you return or at the end of the next Quarter Day, whichever comes first.
- **✦ RANK 3:** When HUNTING, you may roll two D6s on the animal table and choose which result you want to use.
- **✦ RANK 4:** You may track a missed kill. If your second roll (the kill roll) fails, you may spend one additional Quarter Day tracking the wounded animal. Roll SURVIVAL at -1. On a success, you find it and finish it — collect full MEAT and PELTS. On a failure, the animal is lost and this additional Quarter Day spent is wasted.
- **✦ RANK 5:** Replace the +1 modifier with a D10 die.

**Design notes:**

Rank 1 addition: Reading animal signs while hiking adds utility without adding power. It gives the hunter information, not success. The GM controls the confirmation, so it cannot be gamed.

Rank 2 revision: The REST equivalence is preserved. The trap addition reflects an actual hunting skill — the ability to set and leave passive traps rather than requiring active presence. This is historically accurate to peasant hunting methods and creates useful party options.

Rank 4 revision: Replacing "extra successes = extra animals" with wounded-game tracking. The tracking option is risky (costs a second Quarter Day and can still fail) but rewards persistence and represents a concrete hunter skill. The original rank 4 was fine mechanically; this version has more tactical texture.

---

## Optional Rule: Deep Woods Risk

Hunting is not just scarce in the wrong season — it is dangerous in the wrong hex. In the Forbidden Lands, pushing into unmapped terrain to hunt is the kind of decision that ends parties.

At the GM's discretion, hunting in any hex that has not been previously surveyed or explored adds a result to the HUNTING MISHAPS table in place of result 4:

> **4. Something Else Is Here.** You find tracks that are not from any game animal you recognize, or the animals in the area have gone completely silent. Roll SCOUTING. On a success, you pull back in time — no MEAT this Quarter, but no engagement. On a failure, the GM introduces an encounter appropriate to the terrain.

This replaces the existing result 4 (Trap) only in unsurveyed hexes. In known ground, result 4 remains.

For villages built around hunting — which is most of what exists in the Forbidden Lands right now — the territory within one hex of the settlement is hunted regularly and carries no extra risk. Beyond that, the GM should treat terrain as genuinely unknown until the party has surveyed it.

---

## Optional Rule: Hunting Grounds and Village Feuds

Villages in the Forbidden Lands survive on the land around them. Hunting grounds are not owned by any lord. They are held by whoever hunts them. This is not law. It is precedent, memory, and the willingness to back it with iron.

When two villages share a hex — or when one village's hunters range into a hex that another settlement depends on — the result is competition that escalates quickly.

### Hunting Grounds Claims

A village has a **claimed hex** for every hex it hunts regularly. Any hex that has been HUNTED by that settlement at least twice in the current season counts as claimed. The GM tracks this, not the players — they discover it through play.

When adventurers hunt in a claimed hex, roll D6 at the start of the Quarter Day:

| D6  | Result                                                                                                                                        |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1–3 | No encounter. Grounds are empty or the other hunters are elsewhere.                                                                           |
| 4–5 | Signs of competition. You find another party's traps, blinds, or freshly taken carcass. No confrontation yet, but the GM notes the encounter. |
| 6   | Direct encounter. You meet the other village's hunters in the same ground.                                                                    |

On a result of 6, the encounter begins as a stand-off. Neither side attacks immediately. Open with an opposed INSIGHT roll — the character who speaks first versus the opposing hunter's leader. Success reads their intent; failure leaves you reading tension wrong.

**Possible outcomes of a stand-off:**

- Negotiate passage (MANIPULATION roll — difficulty 2, or 3 if you took game from their ground already this season).
- Back down — you lose the Quarter Day but avoid escalation.
- Hold your ground — both parties hunt the hex. Roll HUNT normally, but both sides compete: the other village takes D3 MEAT from the same pool on a success, and the GM advances the feud track by one step.
- Fight — treat as a normal encounter. The other hunters fight as a NPC group at the GM's discretion.

### The Feud Track

Feuds between villages escalate in steps. The GM keeps a simple counter per village-pair.

| Step | State      | What It Means                                                                                            |
| ---- | ---------- | -------------------------------------------------------------------------------------------------------- |
| 0    | Cold       | Mutual wariness. No active hostility.                                                                    |
| 1    | Disputed   | Contested hexes are watched. Meetings are tense.                                                         |
| 2    | Hot        | Traps set in each other's grounds. Ambushes are possible.                                                |
| 3    | Open feud  | Raiders hit the weaker party's camps. MAKE CAMP in a disputed hex triggers a SCOUTING roll or ambush.    |
| 4    | Blood feud | Active killing. Hunters from either village in a disputed hex roll an encounter check every Quarter Day. |

A feud advances one step when:

- A party takes game from the other's claimed ground without negotiation.
- A stand-off ends in a fight.
- One party steals or destroys the other's set traps.

A feud retreats one step when:

- A MANIPULATION roll succeeds during a formal meeting between village representatives (requires travel to the other village).
- One side pays compensation in MEAT, PELTS, or SILVER equal to 5 × the current step.
- A season passes without incident in any disputed hex.

#### Feud Track and Reputation

The feud track is a village-pair relationship. Reputation (Chapter 8) is the fellowship's individual relationship with each settlement. The two interact but are not the same score.

**How the feud affects the fellowship's Reputation:**

When the fellowship is involved in an incident that advances the feud track — taking game without negotiation, fighting in a stand-off, destroying traps — each village involved in that feud rolls its awareness of the event. The GM rolls the relevant Settlement Reputation of the fellowship at that village (or treats it as 1 if the fellowship is unknown there). Each ⚔️ means the village heard what happened.

At villages that heard:

- If the fellowship sided with or was seen as aligned with that village's rival: **Standing -1** at that village.
- If the fellowship sided with or helped that village's position: **Standing +1** at that village.
- If the fellowship acted in their own interest with no clear alignment: no Standing change, but the GM notes the event.

The fellowship does not control the story. Hunters talk. By the time the adventurers reach either village, the version of events that arrived first has already shaped opinion.

**Feud step effects on Recognition:**

At a village already hostile in a feud, the GM may apply the feud step as a penalty to the first impression roll when the fellowship arrives — but only if the village associates the adventurers with the rival. This is a social consequence, not a fixed rule. The GM judges whether the association is established.

| Feud Step      | Possible Standing effect on arrival (if associated with rival)                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1 (Disputed)   | No mechanical effect; tensions are noted in conversation.                                                          |
| 2 (Hot)        | Standing treated as 1 lower than recorded for this visit.                                                          |
| 3 (Open feud)  | MANIPULATION difficulty +1 for any request unrelated to fighting.                                                  |
| 4 (Blood feud) | The village will not deal with known allies of the rival at all without a successful MANIPULATION at difficulty 3. |

**De-escalation and Standing:**

Successfully dropping the feud track through negotiation or compensation also yields Standing gains. If the fellowship brokers a settlement between two villages:

- Each village gains **Reputation +1** for the fellowship at both settlements (they are now known as someone who handled a hard thing).
- If the negotiation required the fellowship to present itself in person and succeeded on 2+ ⚔️: **Standing +1** at both settlements.

This is one of the few ways to rapidly build Standing at a village the fellowship has not previously done anything for. Resolving a feud is exactly the kind of deed that gets talked about.

### Herd Stealing

Animals move. A skilled hunter does not just take prey from the ground — he drives prey toward it.

**HERD STEALING** is a HUNT action that requires two Quarter Days instead of one. On the first Quarter, instead of hunting, the character spends the time driving game animals — making noise, setting fire to brush, using a hunting dog — to push animals from one hex into another.

Roll SURVIVAL at -1. Success means D3 animals are displaced from the source hex into the target hex. The source hex's HUNT modifier drops by 1 until next season. The target hex's HUNT modifier gains +1 until next season.

This can be used offensively: depleting a rival village's hunting grounds while fattening your own. It is also how villages actually manage territory over years — slowly tilting the land in their favor.

If the source hex is a rival's claimed ground, advancing the feud track by one step when the rival eventually notices (which they will — the GM rolls after one full season whether they discover it).

A village that loses two hexes to herd stealing in the same season is in genuine food pressure. The GM should treat this as a stronghold event: the settlement may send raiders, sue for peace, or fracture internally.

### Trap Theft

A hunter with rank 2 MASTER OF THE HUNT sets traps that work while absent. Those traps can be stolen.

Any character who succeeds on a SCOUTING roll in a hex with set traps finds them. They may then:

- **Leave them.** The original hunter collects their catch normally.
- **Empty them.** Steal the catch. Roll SURVIVAL; each success yields 1 MEAT or PELT from whatever was caught. Advances feud track by 1 if the trap belongs to a rival village's hunter.
- **Destroy them.** The trap is wrecked. The original hunter rolls the hunting mishap table instead of collecting. Advances feud track by 2.

---

## Integration Notes

### Skills and Gear

- `MASTER OF THE HUNT` revisions alter one talent in Chapter 4. No other talents require changes.
- `HERBALIST`, `FISHER`, and `PATHFINDER` could be revised in the same spirit but that is not part of this proposal. The `MASTER OF THE HUNT` revision is narrow to this proposal and should not be held waiting on a broader talent rewrite.
- The `CHEF` extended-spoilage rule requires `SALT` to exist as an item in Chapter 10. Salt is not currently listed as a gear item. Either add it as a minor item (similar to TINDERBOX) or simplify the spoilage extension to "a CHEF can preserve MEAT for one extra day with a successful CRAFTING roll during MAKE CAMP, requiring a TINDERBOX."

### Chapter 8 Layout

The season modifier table currently appears after the FORAGING section. Once the HUNT column is added, the table logically applies to both activities. It should either move to appear immediately before both sections or be referenced explicitly in both.

### Terrain Table

The terrain table appears twice: once as a standalone table in the TYPES OF TERRAIN section and once as an in-text modifier list inside the HUNT section. Both must be updated for the Marshlands change.

---

## Acceptance Summary

The following is the list of changes suitable for direct integration into Chapter 8 (and Chapter 4 for the talent).

| #   | Change                                       | Location                                    |
| --- | -------------------------------------------- | ------------------------------------------- |
| 1   | Add HUNT column to the SEASONS table         | Ch08 Foraging › Seasons table               |
| 2   | Add weather modifiers for HUNT               | Ch08 Hunt section (modifier list)           |
| 3   | Replace animal table                         | Ch08 Hunt section                           |
| 4   | Change Marshlands HUNT from -1 to +1         | Ch08 Terrain table + Hunt modifier list     |
| 5   | Add temperature-sensitive meat spoilage rule | Ch08 Hunt (and Fish, Foraging by reference) |
| 6   | Revise MASTER OF THE HUNT ranks 2 and 4      | Ch04 General Talents                        |
| 7   | Hunting Grounds Claims + Feud Track          | Ch08 Optional Rules sidebar                 |
| 8   | Herd Stealing subsystem                      | Ch08 Optional Rules sidebar                 |
| 9   | Trap Theft rules                             | Ch08 Optional Rules sidebar                 |

Changes 1–4 are directly connected and should be applied in a single pass. Change 5 (spoilage) is independent and can be deferred if Salt is not yet an item. Change 6 (talent) is independent and can be applied separately. Changes 7–9 are optional rules and can be added as a single sidebar; they depend on Change 6's trap-while-absent clause in MASTER OF THE HUNT rank 2.
