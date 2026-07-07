<!-- markdownlint-disable MD013 MD024 -->

# Pursuit & Chase — The Track-Position Crew Loop

> **STATUS: WORKSHOP MODULE.** A structured chase subsystem that resolves pursuit as a multi-Round scene built on the action economy — not a single opposed roll. The crew's labor is distributed across driving, navigating, shooting, and repairing, which are *mutually exclusive*; a shared **track position** track decides who is catching whom. *Core is generic; the worked example (1920s spycraft) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic design space
   - 2a. Mechanism overview
   - 2b. NEW CONCEPTS introduced
   - 2c. Mechanical reference (tables & procedures)
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — 1920s spycraft

## 1. Origin — how this was built

- **Source primitives:** **P6 (activity menu)** is the spine — distribute the crew's labor across mutually-exclusive chase jobs. **P1 (push-and-pay)** powers each per-job roll under the engine's signature cost. **P3 (graded success ladder)** reads the roll's quality as track-position shifts, not binary pass/fail. **P5 (resource die)** models the consumables that turn a chase into a countdown — fuel, heat, ammunition, stamina.
- **Reinvention operator:** **Domain Transfer + Fusion** (Operators 1 and 4 from `18 §4`). The activity menu lives in *travel* (`06 §5`); we transfer it unchanged into *pursuit*, where the labor has the same shape — move / navigate / watch / supply / recover — but compressed into combat-length Rounds. We then **fuse** the menu with a **track-position model**: the labor's *output* becomes position shifts on a shared ladder, so the crew is not merely busy, it is *gaining or losing ground together.* The fusion produces a chase that inherits the menu's "coordination is the tactic" psychology *and* the track's "we are closing the gap" drama — neither piece alone makes a chase feel like a chase.
- **Target psychology:** **Tactical / attritional** (`17` M6) crossed with **coordination-as-play** (`17` M4, the bridge-crew row). Produces *chases that matter as scenes* — as mechanically engaging as the fight they interrupt. The point is that a car chase, a starship pursuit, or a rooftop foot-chase gets the same table-wide tactical depth combat always had, instead of collapsing to one Driving roll.
- **Problem solved:** in both source games, a chase is either a single opposed roll or a series of "did you catch up?" checks with no internal structure. That is fine for incidental pursuit, but it makes chase play *thin* — one roll where a fight would be a six-Round scene. For genres where pursuit *is* the action (heist getaway, spy thriller, monster hunt, starship combat), this is a real gap. This module closes it by treating the chase as a combat-equivalent: the same Round cadence, the same action economy, a track instead of a hit-location map.

## 2. The generic design space

### 2a. Mechanism overview

Pursuit becomes a **Chase** — a multi-Round conflict — when there are two sides in motion (a *hunter* and a *quarry*), a closing condition (a capture or escape threshold the scene is racing toward), and real consequence on the outcome (escape = freedom; capture = death or exposure). For incidental pursuit ("we tail him to the tavern"), a single Driving/Running roll (`03 §11`) is enough; reserve the chase loop for pursuits that earn the table time.

The chase is fought over a shared **position ladder** — a short ordinal track representing the gap between hunter and quarry that *both sides occupy*. The ladder replaces combat's range bands (`03 §5`) with a single dimension, because in a chase relative distance is the only position that matters. Movement along the track is the *only* win/lose state — there is no separate HP to whittle. **The hunter wants to reach Caught (0); the quarry wants to reach Out-of-sight + one gain (escape).** Each Round, every participant picks **one** job from a fixed **activity menu** (DRIVE / NAVIGATE / SHOOT / REPAIR / JOCKEY), using the engine's action economy (1 slow + 1 fast, or 2 fast). The four critical demands of a chase — *move, navigate, threaten, keep going* — are **mutually exclusive**, so a crew is always short of hands: *who does what* is the tactic. Graded rolls (P3) read as position shifts on the track.

A successful SHOOT/RAM triggers a **Hazard roll** — a typed-D66 consequence table (P4) that produces specific breakages (a shredded tire, a starred windshield): the chase's equivalent of a damage roll. Each vehicle/runner also tracks **resource dice** (P5) — Fuel, Stamina, Heat — that step down on hard use and, at depletion, force a shift against the depleted side: the countdown that makes a chase finite. The core decision each Round: *do I push for position, or repair and hold ground? Do I spend metacurrency on this DRIVE, or save it for the Hazard roll I know is coming?*

This is the engine's standard conflict spine (`03 §7`) re-skinned: the menu is the action economy, the track is the range ladder reduced to one dimension, the Hazard table is the crit table, the resource die is the consumables clock. The mechanics barely change; the fiction transforms completely — which is the engine's core claim (`12 §12`).

### 2b. NEW CONCEPTS introduced

- **NEW CONCEPT — Track-position ladder:** Core chases are a single opposed Driving/Running roll (`03 §11`); core combat conflict is resolved across range bands or a hit-location map (`03 §5`). This module replaces both with a *5-rung shared position track that both sides occupy simultaneously* — the two-dimensional battlefield collapses to one ordinal dimension the whole scene races along, because in a chase the only position that matters is *how far apart they are.* *Extends the engine by introducing a one-dimensional, shared, bidirectional position track that neither combat's range bands nor the single-roll chase provides.*
- **NEW CONCEPT — Chase activity menu at combat cadence:** P6's activity menu lives in *travel* at Quarter-Day cadence (`06 §5`). This module *compresses the same labor-distribution puzzle to Round cadence* — DRIVE / NAVIGATE / SHOOT / REPAIR / JOCKEY chosen every combat Round, not every Quarter-Day. The Domain Transfer of the menu is recombination of an existing primitive, but the *compression to combat speed* is a new application: no core system runs the travel menu at combat tempo. *Extends the engine by porting the coordination-puzzle menu into its fastest loop.*
- **NEW CONCEPT — Hazard as typed-D66 chase consequence:** P4's typed D66 is used for combat crits (`04 §5`) and magic mishaps (`05 §7`). No core system applies it to *chase-specific breakage families* (Collision / Mechanical, expandable to Environmental, Pursuit-stress, Pedestrian). This module does — a Hazard roll on a successful SHOOT/RAM or a forced NAVIGATE wrong-turn yields a specific, memorable breakage (a shredded tire, an engine stutter) rather than generic "lose a shift." *Extends the engine by adding a chase-specific typed-consequence table family.*
- **NEW CONCEPT — Role-reversibility:** No core conflict system lets the two sides swap mid-scene — attacker and defender, hunter and quarry are fixed for the conflict's duration. This module gates a **role flip** (hunter↔quarry) behind a crit NAVIGATE, modeling the cat-and-mouse where the hunted becomes the hunter. *Extends the engine's conflict model with a reversible-sides rule that no core conflict permits.*

### 2c. Mechanical reference (tables & procedures)

#### When it triggers

Pursuit is **not** for every "follow them." It triggers when:

1. There are **two sides** in motion — a *hunter* and a *quarry* (a chase may invert mid-scene; see Role-reversibility).
2. There is a **closing condition** — a destination, an escape threshold, or a capture threshold the scene is racing toward.
3. The scene **deserves a scene** — the outcome is consequential (escape = freedom; capture = death or exposure).

For incidental pursuit ("we tail him to the tavern"), use a single Driving/Running roll (`03 §11`). Reserve the chase loop for pursuits that earn the table time.

#### The position ladder (the track)

The chase is fought over a shared **position ladder**, a short ordinal track that represents the gap between hunter and quarry. Both sides occupy a rung. The ladder replaces combat's range bands (`03 §5`) with a single dimension — *how far apart are they* — because in a chase, relative distance is the only position that matters.

| Position | Meaning |
| --- | --- |
| **Caught** (0) | Hunter is on the quarry; scene can resolve into a fight, a grab, or a forced stop. |
| **Closing** (+1) | Within reach; one good move ends the chase. |
| **Matched** (+2) | Even — neither gaining; the default start for an even pursuit. |
| **Pulling away** (+3) | Quarry has the edge; the hunter is losing ground. |
| **Out of sight** (+4) | Quarry has broken contact; one more gain = **escape** (quarry wins). |

A **shift** is ±1 rung, awarded by a graded chase roll (P3). The track is short on purpose: most chases should resolve in 3–6 shifts in either direction. Movement along the track is the *only* win/lose state — there is no separate HP to whittle. **The hunter wants to reach Caught (0); the quarry wants to reach Out-of-sight+one (escape).**

#### The activity menu (the spine — P6)

Each Round, every participant (PC or NPC) picks **one** chase job from a fixed menu. The menu is designed so that the four critical demands of a chase — *move, navigate, threaten, keep going* — are **mutually exclusive**. You cannot drive flat-out, pick the fast line, shoot, and nurse an overheating engine at the same time. This is P6's load-bearing constraint, transferred from travel (`06 §5`) to pursuit: the crew is always short of hands, so *who does what* is the tactic.

**DRIVE / RUN** is a SLOW action and the baseline offensive move — you move toward your goal, the hunter toward Caught, the quarry toward escape. Roll DRIVE, RUNNING, or PILOTING (whichever the vehicle or pursuit warrants). On a graded success, gain a position shift toward your goal — one rung closer to the threshold that ends the chase.

**NAVIGATE** is a SLOW action and the route-picking job — you choose the faster line through terrain or traffic, or force the opponent down a bad one. It is a solo job: only one navigator per vehicle per Round. Roll SURVIVAL, NAVIGATION, or STREETWISE. On a graded success, you may either grant yourself a position shift or impose a shift on the opponent — a wrong turn forced, an alley they have to back out of. A critical success can do both. This is the distinguishing tactic of a chase: the chase is won by route choice, not raw speed.

**SHOOT / RAM / FORCE** is a SLOW or FAST action (your choice, set by the fiction — a shot from the hip is fast; a deliberate ram is slow) that applies pressure degrading the opponent's next roll, or forces a Hazard roll (see below). Roll RANGED, MELEE, or DRIVE (for ramming). You cannot also DRIVE this Round — you cannot shoot and drive flat-out at the same time.

**REPAIR / BRACE** is a SLOW action and the defensive and supply move — you roll a resource die up (P5) to cool an overheating engine, patch a tire, or catch your breath, or you cancel an incoming Hazard. Roll CRAFTING, MECHANICS, or COMPOSURE. This is the action that keeps the chase going when the machine or the runner is failing — but it costs you a Round of ground, because you are not driving.

**JOCKEY** is a FAST action — the chase's mini-move: a quick feint, a block, a reroute, or a deflection. It is the chase's "dodge." Roll DRIVE or RUNNING. On a success, gain a half-shift (round down — two JOCKEYs make one full shift), or cancel an opponent's shift. This is what you do when you have already spent your SLOW action and need to defend or press a small advantage.

**The exclusions are the mechanic.** A two-person crew must split DRIVE and NAVIGATE and give up SHOOT and REPAIR. A four-person crew can cover all four jobs, but someone is still not doing something. A lone driver must pick one and accept that the others go undone — which is exactly why a lone fugitive is vulnerable and a crewed vehicle is powerful. This is the same constraint that makes travel a labor puzzle (`06 §5`), now operating at combat speed.

#### Hazards (the consequence layer — typed D66)

When a graded SHOOT/RAM/FORCE succeeds, or when NAVIGATE forces a wrong turn, the target makes a **Hazard roll** — the chase's equivalent of a damage roll. A Hazard is resolved as a **typed D66** (P4) consequence, but the *families* are chase-specific: a small table per hazard source the genre cares about. The `65`/`66` climax rows are "forced stop / catastrophic wreck" — the chase-ending outcomes that function like a Broken result. Hazards are the *cost* the track position does not already capture: you can be winning on position and still lose a tire. The family count is a density dial (`17` M3): two families for a pulp chase, four to six (add Environmental, Pursuit-stress, Pedestrian) for a tactical one.

**Sample Hazard table (two families, genre-skinnable — build parallel families for Environmental / Pursuit-stress / Pedestrian as density requires):**

| D66 | **Collision** (terrain/traffic/impact) | **Mechanical** (the machine failing) |
| --- | --- | --- |
| 11–22 | Near-miss; −1 next DRIVE | Rattle and smoke; step Heat die down |
| 23–34 | Glancing scrape; lose a shift | Tire shredded; −1 DRIVE until REPAIR |
| 35–44 | Hard impact; lose a shift + step Fuel down | Engine stutter; cannot push next Round |
| 45–54 | Spin; lose *two* shifts | Gearbox grinds; −1 DRIVE (rest of chase) |
| 55–64 | Wreck against obstacle; forced stop unless REPAIR (slow) | Overheat/leak; resource die auto-steps |
| 65 | Rollover; vehicle out, occupants roll harm (`04`) | Catastrophic failure; vehicle out |
| 66 | Fatal crash / into the river; scene ends | Engine seizes / explodes; scene ends |

This is P4 doing for the chase exactly what it does for combat crits (`04 §5`) and magic mishaps (`05 §7`): turning a generic "you take damage" into a *specific, memorable* breakage. A "tire shredded" is a story beat; "−1 DRIVE" alone is not.

#### Resource dice (the countdown — P5)

Each vehicle/runner tracks one or two **resource dice** for the consumables that make a chase finite: **Fuel** for vehicles, **Stamina** for runners, **Heat** for engines/guns. Each DRIVE or SHOOT that pushes the machine rolls the relevant die; on 1–2 it steps down (D12→D10→…→D6). At D6+1–2 the resource is **depleted** — out of fuel, blown engine, leg-cramp — which usually forces a position shift *against* the depleted side. This is P5 doing exactly what it does for FL food (`06 §5`): turning consumption into a gamble so the supply thinning is *felt*, not bookkept.

#### The Round structure (identical to combat)

Per Round, each participant gets **one slow + one fast, or two fast** (`03 §7`). Reactions (a JOCKEY deflection) draw from the same budget. Resolve in initiative order (the engine's existing initiative; chases often grant the *faster* side first turn — a chase-specific modifier). A chase ends when a side hits its threshold (Caught / Escape) or a Hazard forces a stop.

**Anatomy of a Round (the procedure):**
1. **Declare jobs.** Each participant names one menu job (the labor split is public — the tactic is in the choosing).
2. **Roll & read quality.** Each job rolls its core pool, read on the graded ladder (P3): fail / partial / full / crit. The *quarry's* DRIVE and the *hunter's* DRIVE oppose if both pick DRIVE — compare ⚔, higher side gains the net shift.
3. **Offer the push (P1).** Any roll may be pushed once, paying the chase's cost (self-harm, or metacurrency per the push-cost dial).
4. **Apply shifts.** Net position shifts move the track; NAVIGATE grants or imposes shifts; SHOOT/RAM triggers a Hazard roll on the target.
5. **Step resource dice (P5).** Any DRIVE/SHOOT that strained the machine rolls its Fuel/Heat die; 1–2 steps it down. REPAIR rolls a die *up* (max one rung).
6. **Check thresholds.** Caught (0) → resolve into a fight or a grab; Escape (Out-of-sight + one gain) → quarry wins. Else, next Round.

This is the engine's standard conflict spine (`03 §7`), re-skinned: the menu is the action economy, the track is the range ladder reduced to one dimension, the Hazard table is the crit table, the resource die is the consumables clock.

## 3. The pressure loop

- **Pressure:** the track is closing toward one threshold or the other every Round; resource dice step down; Hazards stack; the menu forces you to leave a job undone.
- **Decision:** *do I DRIVE for position now, or NAVIGATE to set up a bigger shift next Round? Do I SHOOT and risk the fuel die stepping, or REPAIR and give up ground? Do I spend metacurrency (P2) to push this DRIVE (P1), or save it for the Hazard roll I know is coming?*
- **Consequence:** the position ladder moves; resource dice step; Hazards land; vehicles and runners degrade.
- **State change:** the gap between hunter and quarry shifts materially — and so does each side's *ability to keep chasing.*
- **Loop shape:** **position → spend labor → roll (push?) → shift + deplete → threshold or continue.** Runs at Round cadence (faster than travel, slower than a single roll) — a 3–6 Round scene, like a real fight.

## 4. Dials

| Dial | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Track length** | 5 rungs (Caught→Escape) | 3 rungs (Caught/Matched/Escape) | Tactical depth vs quick resolve |
| **Shifts per graded roll** | 1 / 2 / 3 for partial / full / crit (P3) | 0 / 1 / 2 | Decisive rolls vs grind |
| **Menu breadth** | 5 jobs (full, above) | 3 (DRIVE / NAVIGATE / REPAIR only — no combat) | Crew-coordination puzzle vs pure race |
| **Resource dice** | Fuel + Heat (two dice) | Fuel only (one die) | Layered attrition vs single countdown |
| **Hazard model** | Typed D66 families (P4), per source | Single D6 "lose a shift" | Specific memorable outcomes vs light bookkeeping |
| **Crew size honored** | Each PC = one menu slot (full labor puzzle) | One PC rolls for whole vehicle (abstracted crew) | Everyone-at-the-table vs fast resolve |
| **Reversibility** | Roles (hunter/quarry) can flip mid-scene on a crit NAVIGATE | Fixed roles for the scene | Dynamic cat-and-mouse vs clean objective |
| **Push cost in a chase** | P1 self-harm (wear, injury) — `17` M2 attritional | P2 metacurrency spend — `17` M2 dramatic | Body-as-stakes vs belief-as-stakes |

**Calibration guidance:** start with a 5-rung track, 1/2/3 shifts, the full 5-job menu, Fuel + Heat dice, typed-D66 Hazards, full crew honored, reversible roles, push-as-self-harm. Drop to 3 rungs + the 3-job menu for a chase that should resolve in one combat-length beat; drop Hazards entirely for the lightest version. The "reversibility" dial is the one that changes the *feel* most — a reversible chase feels like cat-and-mouse; a fixed-role chase feels like a race.

## 5. Integration points

- **Hooks into:** the combat action economy (`03 §7`) — a chase *is* combat on a one-dimensional map, and a chase that hits **Caught (0)** resolves *directly into* a normal fight with the closing distance already set. Hooks into the travel menu (`06 §5`) — same labor-distribution logic, compressed to Round cadence; a pursuit through a hex is a chase layered on a hike. Hooks into the resource-die consumables (`08 §10`, `06 §5`) — Fuel/Ammo use the same dice already on the sheet.
- **Requires:** a track (5 rungs); a defined menu; a closing condition (what counts as Caught / Escape); resource dice per participant; a Hazard table (typed D66, P4) — small, 2–4 families keyed to the genre's hazard sources.
- **Replaces / extends:** the single opposed Driving/Running roll (`03 §11`) — adds the tactical layer when stakes warrant. Does *not* replace combat; it *feeds* combat when position hits Caught.
- **Cross-refs:** `03 §5,§7,§11` (positioning, action economy, single-roll conflict), `06 §5` (the activity menu, P6's home), `04 §5` (typed D66, here as Hazards), `17` M2/M4/M6 (cost type, menu breadth, success-ladder calibration), `18` Worked 5 (the starship-bridge precedent for P6→combat transfer).

## 6. Failure modes & edge cases

- **The single-roll collapse.** If the menu is trimmed to "everyone DRIVEs," the chase reverts to a series of opposed rolls with no internal tactic (`19` FE1 false choice). **Fix:** keep at least DRIVE / NAVIGATE / REPAIR on the menu so the labor split is a real decision; the menu is the mechanic, not decoration.
- **The bookkeeping drag.** A full menu + two resource dice + typed-D66 Hazards + a reversible track is a lot of state for a scene that should last ~5 Rounds. If each Round takes ten minutes, the chase outstays its welcome (`19` FE2 decision fatigue; `13` §7.3 GM burden). **Fix:** start light (3 rungs, Fuel-only, single-die Hazards) and add density only for chase-focused genres; cap chase length at the track's natural resolution.
- **The driver monopoly.** If only the wheel-character can act, the rest of the table watches (`19` FE4 agency collapse). **Fix:** honor crew size (each PC = one menu slot) so the gunner, the navigator, and the mechanic all have a turn; if the party is solo in one vehicle, use JOCKEY (fast) to give secondary PCs mini-actions.
- **The track-as-HP-bag.** If shifts are just damage on a track, the chase feels like combat-with-different-nouns. **Fix:** make NAVIGATE (the *line-picking* job) the distinguishing tactic — a good navigator shifts the track *and* imposes terrain that gates the opponent, so the chase is won by route choice, not raw speed. This is the analogue to social-combat's distance layer (`workshop/03`).
- **Resource-die inflation.** If REPAIR can step a die up at will, the Fuel/Heat countdown never bites and the chase has no clock (`13` §5.4 free-resource generation). **Fix:** REPAIR costs a full slow action (so you give up a DRIVE — you lose ground to refuel) and a resource die can step up at most one rung per Round; some damage (a blown tire) is not repairable mid-chase.
- **The GM-fiat hazard.** If Hazards land on GM whim, players feel the scene is rigged (`19` FE5). **Fix:** tie every Hazard to a defined trigger (a graded SHOOT/RAM, a forced NAVIGATE wrong-turn, a depleted resource die) and resolve it on the typed D66 in the open.
- **Reversibility whiplash.** If roles flip too easily, the objective is unstable and players stop investing in it. **Fix:** gate role-reversal behind a crit NAVIGATE (rare) or a Caught-that-doesn't-end-the-scene; a flip should be a dramatic beat, not a coin-flip.

## 7. Validation notes

- **Math (`13 §3,§4`):** track length and shifts-per-roll should be tuned so a typical chase resolves in 3–6 Rounds. At 1/2/3 shifts on a 5-rung track, an even start (Matched, +2) needs ~2 net gains for the hunter to reach Caught or ~2 net gains for the quarry to escape — which, against an opposed roll, lands in the 3–6 Round band. Resource dice (P5) should be the secondary clock: a D12 Fuel die steps on ~1/3 of DRIVE rolls, so a pure-race chase typically runs out of track before it runs out of fuel, while a combat-heavy chase (more pushes, more rolls) lets fuel bite — which is the intended feel.
- **Exploits (`13 §5`):** the REPAIR-loop is the main one (§6 above) — gated by the slow-action cost and the one-rung-per-Round cap. The "stack navigators" exploit (multiple PCs NAVIGATE to force repeated wrong-turns) is gated by the **solo job** tag, mirroring FL's "LEAD THE WAY is one PC only" (`06 §5`). Infinite-push loops (`13` §5.1) are bounded by P1's once-per-roll push limit and P2's metacurrency cap.
- **Felt experience (`19`):** the **menu** is the key psychology — it makes the chase a *coordination* scene (C5 agency ledger: everyone's labor is visible on the track), not a driver's solo performance. The **track** prevents FE3 (swinginess-as-unfairness) by making progress *visible and cumulative* — a single bad roll shifts one rung, it doesn't end the scene. The **resource die** supplies C4 (tension/payoff rhythm): the supply thinning is the rising beat that pays off when someone finally REPAIRs it or it finally depletes.
- **Pipeline (`13 §8`):** passes intent (chase-as-scene is a stated goal), math (3–6 Round band holds), exploit (REPAIR + navigator loops gated), synergy (feeds combat at Caught without doubling its rules), table (one track + 1–2 dice + small hazard table — acceptable load), verdict: **ship as a General-layer module with the menu and track as the load-bearing core; resource dice and typed Hazards as Situational density dials.**

## 8. Worked genre example — 1920s spycraft

**The setting:** Paris, 1923, three in the morning. The PCs are Sûreté-aligned agents fleeing a job gone wrong in a stolen Delage; two Bolshevik pursuers in a faster Lorraine-Dietrich are closing on the Pont de l'Alma. The PCs must cross the bridge and lose the tail before the gendarme cordon. The quarry (PCs) want **Escape**; the hunters want **Caught**.

**Dials set:** 5-rung track, start at **Matched (+2)**; 1/2/3 shifts; full 5-job menu; **Fuel + Heat** dice (both D12 for the Delage; Fuel D12 for the Lorraine); typed-D66 Hazards with two families — **Collision** (traffic, lampposts, the Seine embankment) and **Mechanical** (tire, radiator, gearbox); push cost = self-harm (wear, a grazed arm leaning out the window) — `17` M2 attritional; reversible roles (a crit NAVIGATE could flip hunter/quarry).

**The cast's labor (PC Delage, 3 crew):**
- **Marchand** (the wheel) — DRIVE.
- **Costa** (the ex-rally navigator, riding shotgun) — NAVIGATE.
- **Voss** (cover fire out the rear) — SHOOT.

A fourth job (REPAIR) goes undone this Round — the Delage's Heat die will step if they push the engine. That gap is the labor puzzle made visible.

**In use (excerpt):**

- **Round 1.** Marchand **DRIVEs** for escape: Drive 4 + the Delage's handling 1 = 5 dice; 2⚔ — a full success, +1 shift toward escape → **Pulling away (+3)**. Costa **NAVIGATEs**: Survival 3 + Streetwise 2 (Paris-born) = 5 dice; 3⚔ — a critical. She spends it to force the Lorraine down a wrong alley (the hunters take a −1 shift) *and* read the next line; the Lorraine's driver rolls Drive to absorb it, partially deflects. Net: Lorraine drops to **Closing (+1)**. Voss **SHOOTs** out the back (Ranged 3, pistol at range) = 3 dice; 1⚔ — a partial; the Lorraine must make a **Hazard roll** (Mechanical family, typed D66): rolls 22 = "windshield starred; driver −1 next Round." The Heat die is rolled for the Delage's hard driving — a 2, steps D12→D10.
- **Round 2.** The Lorraine's driver, now −1, **DRIVEs** to close: 3 dice −1 = 2; 1⚔ — barely a shift, → **Matched (+2)**. His gunner **SHOOTs** back — 2⚔, full — Voss rolls a Hazard (Collision family): 41 = "clipped a lamppost; lose a shift unless you REPAIR." Marchand cannot REPAIR *and* DRIVE, so the Delage takes the shift back down to **Closing (+1)** — they are losing the bridge. Costa **NAVIGATEs** again, 2⚔ — she routes them onto the quai where the Lorraine's extra horsepower is useless, granting the PCs a free shift next Round. Voss **JOCKEYs** (fast): a feint that cancels the hunters' upcoming NAVIGATE.
- **Round 3.** Marchand **DRIVEs** with Costa's carried shift in hand — 2⚔ +1 = enough to break to **Out of sight (+4)**. One more gain escapes. The Lorraine, down a windshield and out-horsed on the quai, **DRIVEs** desperately and **pushes** (P1) — accepting a 💀 (the gunner takes a graze, self-harm cost) — for a 2⚔ that holds them at +4, not +5. The Delage's Fuel die finally steps D10→D8 on the sprint to the bridge. Costa **NAVIGATEs** a last time — 3⚔, critical — and sends them across Pont de l'Alma into the gendarme cordon, where the Lorraine peels off. **Escape.** The Delage rolls into an alley on fumes (Fuel at D6), a starred windshield behind them and a grazed gunner — a win that *cost.*

**Why this works in 1920s spycraft:** the **menu** models the reality that a car chase is a *crew* action — the driver, the navigator reading the streets, the gunner covering the tail each have a job, and no one can do two. The **track** makes the cat-and-mouse *visible*: every Round the bridge gets closer or the tail gets tighter, and the table can see it. The **Fuel + Heat** dice give the Delage a ticking clock that matches pulp-thriller pacing — you win, but you arrive on fumes. The **typed-D66 Hazards** (Collision / Mechanical) produce the specific, memorable breakages that define the genre — a starred windshield, a clipped lamppost — not generic "you take 2 damage."

**Re-skin for your genre:**
- **Heist getaway:** menu = DRIVE / NAVIGATE / SHOOT / REPAIR / HACK-TRAFFIC-LIGHTS; Hazards = Civilian-collision / Roadblock / Pursuer-fire; resource dice = Fuel + Ammo; Caught = boxed in by police.
- **Monster hunt (the PCs are hunters):** menu = TRACK / CUT-OFF / TRAP / WATCH / REST; position rungs = Trail-gone → Scent → Close → In-sight → Cornered; Caught = the beast at bay (resolves into melee); resource dice = Stamina + Torches.
- **Starship pursuit (bridge crew):** menu = HELM / TACTICAL / ENGINEERING / COMMS / MEDICAL (the `18` Worked 5 bridge, now fused with a track); Hazards = Asteroid / Heat-spike / System-failure; resource dice = Fuel + Heat + Shields; Caught = boarding range; Escape = out of sensor range.
- **Rooftop foot-chase:** menu = RUN / PARKOUR (navigate) / TACKLE / CATCH-BREATH (repair); position = Lost → Sight → Closing → Arm's-length → Grabbed; resource dice = Stamina only; Caught = a grapple (resolves into unarmed combat).
- **Submarine/cat-and-mouse:** menu = HELM / SONAR / WEAPONS / DAMAGE-CONTROL / STEALTH; position rungs model *contact* not distance (No-contact → Bearing → Close → Weapons-solution); reversible roles on a crit SONAR — the hunted becomes the hunter.
