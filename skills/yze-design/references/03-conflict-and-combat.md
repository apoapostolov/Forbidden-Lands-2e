<!-- markdownlint-disable MD013 -->

# Conflict and Combat — The Action Economy

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the conflict/combat spine — the action economy that makes combat a *decision* rather than a slog. Assumes the resolution, pushing, and damage material in `00-engine-core.md`.

## Contents

1. Source provenance
2. Abstraction target
3. Time units (Round / Turn / Shift)
4. Initiative models (segment vs card draw)
5. Range and zones
6. Reach bands and positioning
7. Slow / fast action economy
8. Reactive actions (dodge / parry / block)
9. Melee conflict
10. Ranged conflict
11. Social conflict
12. The Duel / Face-Off special-conflict pattern
13. Morale and rout
14. Mounted combat
15. Divergence rows (FL vs West)
16. Dials and instantiation recipe
17. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/05-combat-and-damage.md` — Round/Turn/Shift (lines 29-34), rolling initiative as AGILITY+WITS ⚔ segments (7-23), optional Fast Skill Roll Initiative (19-23), surprise (25-27), slow/fast action lists (39-101), zones & range + zone features Cramped/Rough/Open/Dark-Foggy + borders Blocked/Obscured (115-162), movement (151-153), mounted combat (165-167), fleeing (171-185), Morale & Rout optional (191-212), ambushes/sneak attacks (214-233), close combat reach bands + CUT IN/BRACE/INTERCEPT/LOCK SHIELDS/FEINT (235-339), reactive dodge/parry (271-277, 299-313), ranged combat + Aim/Shoot/Ready/Load (353-395), social conflict Manipulation vs Insight + negotiating position + Reputation (397-443), weapon features (449-540), cover (686-699).

**Tales of the Old West 2E (West):**
- `01-corebook/05-conflict-and-damage.md` — Round/Turn/Shift table (18-31), six range categories Arm's Length→Distant (34-42), card-draw initiative + suit seniority (44-50), Fast Initiative via Quick roll (52-54), exchanging initiative cards (60-62), two-actions-per-Round (64-73), slow/fast action tables (76-119), surprise/sneak/ambush (121-127), fighting modifiers + All-Out Attack + Called Strikes (129-160), blocking & dodging with counterattack (162-172), protecting another (174-176), grappling (178-192), retreating (194-196), shoving/disarming (198-207), brace (209-211), morale & rout (213-229), lasso (231-237), ranged conflict + single/double/lever actions (239-251), aiming/called shots/quick shots/target size/cover/range modifiers (249-265), resolution stunts (267-274), duels Face Off→Go for Your Guns→Shoot-off (276-326), fanning (327-348), overwatch (350-366), sneak attacks/ambushes + undetected +3 (367-373), cover ratings (375-379), reload economy (381-385), bows & slingshots (404-406), social conflict Presence/Performin' vs Insight + negotiating position + Social Conflict by Mail (408-438).

## Abstraction target

Reverse-engineer **conflict** as a genre-neutral *action-economy engine*: a time unit, an initiative method, a positioning model (zones + range bands), a strict slow/fast action budget, a reactive-defense layer, and a small set of conflict *modes* (melee / ranged / social) plus an optional *ceremonial* mode (the Duel/Face-Off). FL and West share the spine almost completely — the differences are flavor and calibration: FL builds a rich *reach-band* and *zone-feature* positioning system and resolves initiative as a rolled segment; West builds a deep *firearm-action* and *cover* system and resolves initiative by random card draw. Capture the **two-actions-per-Round budget** as the engine's load-bearing structure and the **Duel/Face-Off** as a reusable "high-stakes scripted conflict" pattern.

Apply the Abstraction Ladder (source instance → generic mechanism → design intent → dials) to every section.

## 3. Time units (Round / Turn / Shift)

**Both games converge on the same three-scale time ladder.** FL:

> "A round can represent any period from ten seconds up to a minute, depending on circumstances and the skills used. … A turn is about 15 minutes long, and it is used primarily when exploring adventure sites." FL `05-combat-and-damage.md:31-34`.

West states it as a fixed table:

| Unit | Duration | Primary use |
| --- | --- | --- |
| Round | 5–10 seconds | Combat |
| Turn | 5–10 minutes | Exploration |
| Shift | 6 hours | Recovery |

West `05-conflict-and-damage.md:18-31`. West adds the **four Shifts in a day** (Morning/Afternoon/Evening/Night) and tasks the GM with tracking time across all three scales. West `05-conflict-and-damage.md:29-31`.

**Generic mechanism — the three-scale time ladder:** three nested units where each step is roughly an order of magnitude larger and maps to a different mode of play. *Round* = tactical combat (seconds) — the unit over which the action budget and initiative cycle. *Turn* = exploration/procedure (minutes) — the unit for journey actions, scouting, healing attempts, per-Turn recovery. *Shift* = recovery/downtime (hours) — the unit for rest, attrition timers (starvation/disease rolls), and the day's quarters.

**Design intent:** the ladder keeps each play-mode on a clock that matches its stakes. Combat matters because a Round is seconds, so a single action budget is genuinely scarce; exploration matters because a Turn is long enough that a failed roll *costs time* and advances the world; recovery matters because a Shift is long enough that attrition and rest interlock. Without the three scales, you either get combat that sprawls (turns too long) or exploration that has no cost (turns too short to matter). **Layer:** General throughout.

**Dials & instantiation recipe:**
1. **Round length** — 5–10 s (both) is the calibrated point. Shorten toward "a single heartbeat" for hyper-lethal genres; lengthen toward a minute for abstract mass combat. The exact value matters less than the *scarcity feeling* it produces.
2. **Turn length** — 5–10 min (West) / ~15 min (FL). Dial tunes how costly exploration failure is.
3. **Shift length + day structure** — 6 h / 4-per-day (West) is the explicit point; FL implies Quarter Days. Add named quarters (West's Morning/Afternoon/Evening/Night) when you want downtime beats to feel real.
4. **Which scale governs recovery** — both use Shift-level rest + Turn-level field-medicine; the dial is whether a single rest restores *all* attribute points (town/stronghold comfort) or only *one per attribute* (wilds). FL `05-combat-and-damage.md:791-798`.

## 4. Initiative models (segment vs card draw)

The two games resolve "who acts first" with opposite mechanisms — one **deterministic-from-roll**, the other **purely random**.

**FL — the "initiative segment" (rolled, sticky-within-round):** At the start of each Round, every participant rolls **AGILITY + WITS** together; add the ⚔ rolled to *unmodified AGILITY* to get a numeric **segment**. Higher segments act before lower; you may **delay** to any lower segment but once you act you stay there. Participants in the same segment act *simultaneously*, with damage/conditions applying at the end of the segment. FL `05-combat-and-damage.md:7-23`. **Surprise:** the surprising side adds +3 to initiative in Round 1; the surprised side uses only unmodified AGILITY (no roll). FL `05-combat-and-damage.md:25-27`. **Optional Fast Skill Roll Initiative:** every player rolls AGILITY; if each gets ≥1 ⚔ the whole party acts before enemies, else after. The side that started combat adds +2 in Round 1. Enemies never roll. FL `05-combat-and-damage.md:19-23`.

**West — the card draw (random, redrawn each Round):** A full deck (jokers removed); each participant draws one card; **Aces high act first, descending through King.** Ties broken by suit seniority: **spades > hearts > diamonds > clubs**. Everyone redraws each Round; the deck is reshuffled at conflict's end. West `05-conflict-and-damage.md:44-50`. **Optional Fast Initiative:** side initiative via a single `Quick` roll — if ≥ half the PCs succeed, the party side acts first; else enemies do. Within a side, order is table-negotiated. West `05-conflict-and-damage.md:52-54`. **Swapping cards:** once per scene, two PCs who can communicate may exchange initiative cards at the start of a Round (a small tactical-cooperation valve). West `05-conflict-and-damage.md:60-62`. **NPCs:** the GM draws one card per NPC, or one for a group. West `05-conflict-and-damage.md:56-58`.

**Generic mechanism — three initiative archetypes on one dial:**
- **Rolled-and-sticky (FL):** a roll produces a numeric order that holds within the Round; re-rolled next Round. Predictable, stat-coupled (fast/agile characters reliably go first), supports *delay* and *simultaneous-segment* resolution.
- **Random-and-redrawn (West):** a deck produces a fresh random order every Round; decouples initiative from stats. Produces volatility and drama; anyone can suddenly be first or last.
- **Side-based (both games' Optional/Fast variants):** collapse the order to "our side / their side," decided by a single roll. Fastest to run; sacrifices per-character granularity.

**Design intent:** initiative decides *who pays the action-economy tax first*. FL's rolled model makes agility a real combat stat and lets smart play (delay, simultaneous resolution, segment-swap via FEINT) matter. West's card model makes combat *unpredictable* — thematically right for a genre where a gunfight is chaos and anyone can get unlucky. The Optional/Fast variants exist in both books because *exact order rarely matters as much as overall momentum* in skirmishes, and both designers want a way to skip the bookkeeping. Without a per-Round initiative method, the action budget has no sequence and combat devolves into "everyone declares, then resolve." **Layer:** General (some initiative method is mandatory); the archetype is a core design dial.

**Dials & instantiation recipe:**
1. **Initiative archetype** — rolled-sticky / random-redrawn / side-based / fixed. *(Sets the volatility and stat-coupling of combat order.)*
2. **Stat coupling** — couple to a speed/agility stat (FL: AGILITY+WITS) vs decouple entirely (West: cards). FL's stat-coupling rewards character build; West's randomness rewards tactical adaptability.
3. **Resolution granularity** — per-segment with simultaneous ties (FL) vs strict linear order (West). FL's simultaneous-segment rule is a feature, not a bug — it lets two fast fighters genuinely clash.
4. **In-round malleability** — allow delay (FL), card-swap between allies (West), or neither. More malleability = more tactical cooperation; less = more ruthlessness.
5. **Surprise bonus** — both give the surprising side a Round-1 edge (+3 dice FL; the ambusher wins the opening). The dial is the *size* of the edge and whether the surprised side acts at all that Round.

## 5. Range and zones

**Both games use named range bands rather than measured distances** — this is the engine's signature positioning abstraction. The bands are nearly identical; West adds a sixth band (Medium).

| Band | FL | West |
| --- | --- | --- |
| Arm's Length | Right next to you | Hand-to-hand range |
| Near | A few steps, same zone | Within a few meters |
| Short | Up to ~25 m, bordering zone | Up to ~25 m |
| (Medium) | — | Up to ~50 m (West only) |
| Long | Up to ~100 m | Up to ~150 m |
| Distant | As far as the eye can see | 150 m–1000 m |

FL `05-combat-and-damage.md:155-161`; West `05-conflict-and-damage.md:34-42`.

**FL layers a *zone* model on top of the bands** — the battlefield is divided into **zones** (a room or patch of ground, a few steps to ~25 m across); moving between neighboring zones is one **segment** of distance. FL `05-combat-and-damage.md:115-118`. Zones carry **features** that modify actions inside them:
- **CRAMPED** — heavy weapons −2; cannot SWING before an attack. FL `05-combat-and-damage.md:131`.
- **ROUGH** — RUNning in requires a MOVE roll or you fall. FL `05-combat-and-damage.md:133`.
- **OPEN** — ideal for mounted combat. FL `05-combat-and-damage.md:135`.
- **DARK/FOGGY** −2 to ranged attacks into the zone; attacks can't pass through. FL `05-combat-and-damage.md:137`.

And **borders** between zones carry their own tags:
- **BLOCKED** — wall/abyss; cannot pass. FL `05-combat-and-damage.md:143`.
- **OBSCURED** — blocks line of sight (doorway, shrubbery) but not movement; no ranged attacks across it. FL `05-combat-and-damage.md:145`.

**West layers a *cover* model instead** — position is GM-discretion distance, but cover is a graded, mechanical defense:
- **Partial Cover** (low fence/wall): attacker −1. West `05-conflict-and-damage.md:263`.
- **Good Cover** (≥ half obscured): attacker −2.
- **Heavy Cover** (only a small part visible): attacker must make a Called Shot.
Cover additionally acts as **protection dice** rolled against incoming damage (a Cover Rating: bush 1, wicker fence 2, furniture 3, wooden door 4, wooden wall 5, adobe wall 8). West `05-conflict-and-damage.md:375-379`. FL has the same *cover-as-armor* mechanic (Armor Rating: furniture 3, wooden door 4, tree trunk 5, wooden wall 6, stone wall 8) but no attacker-side to-hit penalty grades. FL `05-combat-and-damage.md:688-699`.

**Generic mechanism — the positioning model:** two layers — (a) **range bands** (named, non-measured, both games) that gate which weapons/actions are legal and apply distance modifiers, and (b) a **terrain/cover layer** that the genre dresses differently. FL's terrain layer is *zone features + borders* (terrain-as-movement-and-line-of-sight); West's is *cover ratings + to-hit penalty grades* (terrain-as-defense). The two are the same abstraction seen from opposite ends: FL asks "what does the ground do to you when you move/attack?"; West asks "what does the ground do for you when you're shot at?"

**Design intent:** named bands replace a grid with a *conversation*. You never measure feet; you describe position ("they're at Short range, behind a wooden door") and the fiction carries the tactics. This is what makes the engine playable at a table without a battlemat. The terrain layer is where each genre injects its signature pressure: FL's zones make *movement and line-of-sight* the scarce resource (good for dungeons and ruins); West's cover makes *concealment* the scarce resource (good for gunfights). Without the bands, positioning becomes hand-wavy and tactics collapse; without a terrain layer, all ground is featureless and combat loses spatial interest. **Layer:** General (range bands); the terrain-layer dialect is a design dial.

**Dials & instantiation recipe:**
1. **Band count** — 5 (FL) or 6 (West's Medium). Add bands when you need finer ranged granularity (firearms); use fewer for melee-centric games.
2. **Terrain layer** — zone-features-and-borders (FL) / cover-ratings-and-to-hit-grades (West) / hybrid / none. *(What kind of spatial pressure the genre wants.)*
3. **Cover-as-armor** — on (both, with Cover Rating) / off. When on, decide whether cover also imposes an attacker to-hit penalty (West) or only soaks damage (FL).
4. **Movement resolution** — FL zones + segment-of-distance + Rough-requires-roll; West pure GM discretion. Zone-movement gives tactical legibility; discretion gives speed.

## 6. Reach bands and positioning

**FL only — a deep reach-band subsystem** that makes *weapon length* a form of positioning pressure, layered on the range bands.

> "Weapons fall into three length bands. They decide who must close, who keeps space, and who can strike from the next zone over." FL `05-combat-and-damage.md:249-253, 602-608`.

- **SHORT-REACH** — knives, fists; can only attack if already inside the opponent's reach.
- **NORMAL REACH** — swords, axes; fight at Arm's Length.
- **LONG-REACH** — spears, polearms; fight from **Near** range, keep enemies out, apply −1 to the enemy's MOVE. If an enemy gets inside Arm's Length, the weapon is "badly awkward" (haft use at −2, 0 damage). FL `05-combat-and-damage.md:251-253, 502, 518`.

The reach dance is resolved by a set of **positioning fast actions**:
- **CUT IN / BACK** — a FAST action rolling MOVE to close inside the opponent's reach (or step back to your own). Against a LONG-REACH weapon the CUT IN is at −1; fail and you stay outside. FL `05-combat-and-damage.md:327, 610-614`.
- **BRACE** — set a pointed polearm/long-reach weapon; the first enemy moving into reach triggers an immediate STAB (counts as your one immediate attack). FL `05-combat-and-damage.md:329`.
- **INTERCEPT** — spend both actions to hold a reactive stance; make one ATTACK/SHOOT before an enemy's action resolves. FL `05-combat-and-damage.md:331`.
- **LOCK SHIELDS** — shield + allied shield-bearer in the same zone; ranged attacks −1 vs all of you, +1 ⚔ needed to SHOVE. FL `05-combat-and-damage.md:337`.
- **FEINT** — swap initiative segments with an opponent at Arm's Length; takes effect next Round. FL `05-combat-and-damage.md:339`.
- **HALF-HAND** (weapon feature) — shorten grip to shift reach one band inward (FAST action). FL `05-combat-and-damage.md:496`.

The first fighter to successfully close and engage *sets the distance band*; mismatch your reach and you must CUT IN before you can attack. Surprise/sneak-attack bypasses this — you start inside your preferred distance. FL `05-combat-and-damage.md:255-258, 616`.

**West's nearest analogue** is much lighter: the **Brace** fast action gives +1 (or +2 for mounted/charging/narrow-opening targets) to your first covered-lane shot — a positional hold for *ranged* weapons, not a melee-reach system. West `05-conflict-and-damage.md:209-211`. West treats weapon reach as implicit (fists/clubs/tomahawks at Arm's Length; lasso as a special ANIMAL HANDLIN'-based grapple at Near/Short). West `05-conflict-and-damage.md:231-237`.

**Generic mechanism — "reach as positioning pressure":** a subsystem that converts *weapon length* into a *distance-control contest*. Long weapons own the outer band and tax entry; short weapons must win a close-in roll to engage; once closed, the long weapon is penalized. This creates a rock-paper-scissors of reach (long keeps short out; short punishes long once inside) that gives melee tactical depth without a grid. The pattern generalizes to any weapon-as-positioning axis (range brackets for firearms, engagement radius for mounts).

**Design intent:** reach bands make *which weapon you drew* a load-bearing tactical choice — a dagger is genuinely dangerous only if you close, a spear is genuinely dangerous only if you keep them out. Without it, all melee weapons are just different damage numbers and the only question is "who hits harder." The CUT IN roll is the engine's way of making *getting inside* cost something (a fast action and a MOVE roll), so reach advantage is earned, not free. **Layer:** Situational — a reach subsystem only pays for itself in melee-heavy genres; West's lighter model proves you can run the engine without it. **Layer of each action:** CUT IN/BRACE/INTERCEPT/LOCK SHIELDS/FEINT are Situational (require the reach subsystem to exist); FL lists them as General within its own book.

**Dials & instantiation recipe:**
1. **Reach subsystem presence** — on (FL) / off (West). Turn on for melee-centric or historical genres; leave off for ranged-centric genres.
2. **Band count for reach** — three (FL's Short/Normal/Long) is the calibrated point. More bands = more granular but more bookkeeping.
3. **Entry cost** — a MOVE roll at −1 vs Long-Reach (FL). The penalty size tunes how dominant long weapons are.
4. **Inside-the-reach penalty** — −2/0 damage haft-use (FL). Decides how badly a closed-on polearm is neutralized.
5. **Positional hold actions** — BRACE/INTERCEPT (FL) / ranged Brace (West). Decide whether holds are melee-only, ranged-only, or both.

## 7. Slow / fast action economy

**This is the load-bearing rule of the whole conflict engine.** Both books state it almost identically:

> "When it is your turn to act, you can perform *one slow action and one fast action, or two fast actions*." FL `05-combat-and-damage.md:41`; West `05-conflict-and-damage.md:66` (near-verbatim).

A **slow action** usually requires a skill roll (attack, cast, flee, treat). A **fast action** is quicker and may or may not roll (dodge, parry, draw, run, retreat). Actions **refresh at the start of each Round** and cannot be banked. FL `05-combat-and-damage.md:99-101`.

**The two action menus (representative, not exhaustive):**

| Slow actions (FL) | Slow actions (West) |
| --- | --- |
| Slash, Stab, Punch/Kick, Grapple, Break Free, Shoot, Persuade, Taunt, Cast Spell, Flee, Crawl, Charge, Treat Wounded, Dragging | Crawl, Melee attack, Shoot, First Aid, Persuade, Horse/Mount, Wagon, Start engine Vehicle |

| Fast actions (FL) | Fast actions (West) |
| --- | --- |
| Dodge, Parry, Draw Weapon, Swing Weapon, Get Up, Hold Fast, Shove, Disarm, Brace, Intercept, Lock Shields, Feint, Run, Retreat, Grapple Attack, Ready Weapon, Aim, Power Word, Draw Grimoire, Use Item | Run, Get Up, Draw weapon, Prepare a weapon, Quick shot, Aim, All-Out Attack, Block, Dodge, Initiate/Maintain Grapple, Retreat, Seek Cover, Brace, Protect Another, Shove, Disarm, Ride Horse, Drive Wagon, Use Item, Reload Firearm |

FL `05-combat-and-damage.md:47-87`; West `05-conflict-and-damage.md:76-113`.

**Key shared rules around the budget:**
- **Helping others** costs you one action of the same type and breaks initiative order. FL `05-combat-and-damage.md:95-97`; West `05-conflict-and-damage.md:70`.
- **Reactive actions count against the budget** — dodging/parrying out of turn subtracts from your later turn (see §8).
- **Immediate attacks are capped at one per Round** outside your turn (FL's BRACE/INTERCEPT/RIPOSTE all share this single slot). FL `05-combat-and-damage.md:275-277`.
- **Prone** requires a GET UP fast action before melee; prone targets suffer +2 to be hit. FL `05-combat-and-damage.md:243`; West `05-conflict-and-damage.md:137`.

**Genre-specific action entries** dress the same skeleton: FL has Cast Spell / Power Word / Draw Grimoire (magic economy); West has Prepare-a-single/lever-action-weapon (cocking/chambering), Quick Shot (fast shot at −2), Reload Firearm (ammo economy), Ride Horse / Drive Wagon, Seek Cover, Protect Another. FL `05-combat-and-damage.md:57, 73, 85`; West `05-conflict-and-damage.md:68, 97-98, 105-107, 113`.

**Generic mechanism — the two-action budget:** every combatant gets exactly **2 actions per Round**, drawn from a slow-pool and a fast-pool, spendable as (1 slow + 1 fast) or (2 fast). Slow = "the thing that decides the fight" (the attack, the spell); fast = "the things that shape the fight" (movement, defense, readiness). The budget is the scarcity that makes combat a *sequence of trade-offs*: you cannot attack *and* defend fully *and* reposition in one Round. Reactive defense spends *future* actions, so defending now taxes your next turn — this is what makes "do I attack or do I defend?" a real question.

**Design intent:** the slow/fast split is the single most important combat rule in the engine. It does three jobs at once: (1) **scarcity** — only one decisive roll per Round means every attack is a commitment; (2) **tempo** — fast actions let you do *two* small things, so a pure-movement or pure-defense Round is viable, which makes disengage/reposition real tactics; (3) **compatibility with reactions** — because reactions cost from the same budget, the engine avoids the "free infinite defenses" problem that bloats other d6 systems. Without the budget, combat is a slugfest of "I attack, I attack"; with it, every Round is a hand of two cards and you choose how to play them. **Layer:** General — mandatory, load-bearing.

**Dials & instantiation recipe:**
1. **Action count per Round** — 2 (both, the canonical point). Raise to 3 only for high-action pulp; the engine's balance assumes 2.
2. **Slow/fast split** — the (1 slow + 1 fast) ∨ (2 fast) rule (both). Alternative: allow 2 slow (more lethal/faster), or 3 fast (more mobile). Both books chose the middle.
3. **Reaction cost** — reactions draw from the same budget (both). This is the dial that prevents defense-bloat; never make reactions free without rebalancing damage.
4. **Immediate-attack cap** — one per Round outside your turn (FL). Caps combo abuse from positional holds.
5. **Genre action entries** — add slow/fast entries for the genre's signature verbs (magic, vehicles, mounts, reload). The skeleton is stable; the menu is the flavor.

## 8. Reactive actions (dodge / parry / block)

**Both games let a defender act out of turn to avoid an attack, paying from the shared action budget.** The trigger, cost, and effect differ in detail but share the spine.

**FL — dodge (MOVE) and parry (MELEE + gear):** When attacked by an aware opponent, the defender declares DODGE or PARRY *before* the attack roll. Each is a fast reactive action that breaks initiative order and **counts toward the defender's two actions that Round** — once both are spent, no more reactions. FL `05-combat-and-damage.md:271-273`.
- **DODGE** — roll MOVE; every ⚔ cancels one attacker ⚔; you fall **prone** (or stay standing at −2). Slash gives you +2 to dodge; stab gives −2. FL `05-combat-and-damage.md:299`.
- **PARRY** — roll MELEE + shield/weapon Gear Bonus; every ⚔ cancels one attacker ⚔. Parrying without the *parrying* feature is −2; a shield parries a stab at +2. FL `05-combat-and-damage.md:301`. Ranged attacks count as stabs when parrying and require a shield/parrying weapon. FL `05-combat-and-damage.md:387`.

FL's attack-vs-defense matrix (the "rule of thumb: slash is line and movement, stab is line and guard, a shield is the safest answer to a point"):

| Action | SLASH | STAB | PUNCH/KICK |
| --- | --- | --- | --- |
| Parry with weapon | — | −1 | — |
| Parry with shield | — | +2 | +2 |
| Dodge | +2 | −2 | — |
| Parry w/o parrying weapon | −2 | −2 | — |
| Dodge w/o going prone | −2 | −2 | — |

FL `05-combat-and-damage.md:306-312`.

**West — block (FIGHTIN') and dodge (MOVE), with a counterattack option:** Declare Block or Dodge before the attack roll; it costs a fast action; you can't react if you've spent your actions. Roll the relevant ability; **for each success choose an effect** — cancel one of the attacker's damage, *or* perform a **counterattack** dealing weapon damage (no extra damage from additional successes). West `05-conflict-and-damage.md:162-170`. Blocking unarmed against armed/dangerous attacks is impossible without a sturdy weapon. West `05-conflict-and-damage.md:172`. West also has **Protect Another** — a fast reaction to become the target instead of an ally, or grant the ally +1 to their own Block/Dodge. West `05-conflict-and-damage.md:174-176`.

**Generic mechanism — the reactive-defense layer:** a class of *out-of-turn* actions that (a) are declared before the attack resolves, (b) cost from the defender's shared action budget (preventing infinite defense), and (c) cancel attacker successes/damage on a 1:1 basis (or convert to a counterattack). The two games diverge on the *economy of effect*: FL reads the reaction as success-cancellation (your ⚔ erase attacker ⚔), with weapon-type interaction modifiers; West reads it as a success-*menu* (each ⚔ buys a cancel *or* a counterattack).

**Design intent:** reactions are what make combat *not a foregone conclusion*. Without them, whoever wins initiative and attacks simply deals damage — the defender is a passive target. With them, every attack is a *question* ("will they spend an action to stop this?") and the defender has agency. The budget-coupling is essential: it means defending has an *opportunity cost* (you'll have fewer actions on your turn), so you can't turtle forever — eventually you must act, and that's when you're vulnerable. The slash/stab/shield matrix (FL) and the cancel-vs-counterattack choice (West) add weapon-specific texture so defense isn't a single optimal move. **Layer:** General (some reactive defense is mandatory); the cancel-vs-menu economy is a design dial.

**Dials & instantiation recipe:**
1. **Defense verbs** — dodge-only / dodge+parry / dodge+block+protect (West's three). More verbs = more tactical texture but more rules.
2. **Effect economy** — pure success-cancellation (FL) / success-menu with counterattack (West). FL's model is faster; West's makes defense *aggressive* (you can hurt them while defending).
3. **Prone penalty on dodge** — FL drops you prone (or −2 to stay up); West doesn't. Adds a positional cost to dodging.
4. **Weapon-type interaction** — FL's slash/stab/shield matrix. Add when you want weapon choice to matter defensively; omit for speed.
5. **Protect/intercept an ally** — West's Protect Another (Optional in spirit). Add when you want bodyguard play.

## 9. Melee conflict

**The melee mode** uses the action budget (§7) + reach (§6) + reactions (§8) + the resolution spine (`00-engine-core.md`). Both games resolve a melee attack as: roll the melee ability + weapon bonus; on a hit, deal the weapon's damage; extra ⚔ increase damage and/or buy stunts.

**FL — Slash / Stab / Punch as the three melee verbs**, each with a weapon-feature prerequisite and a distinct defense profile:
- **SLASH** (edged/blunt): dodge +2, weapon-parry −2 unless *parrying*. FL `05-combat-and-damage.md:289`.
- **STAB** (pointed): dodge −2, shield-parry +2. FL `05-combat-and-damage.md:291`.
- **PUNCH/KICK/BITE** (unarmed): parry +2; 1 damage; uses blunt table (or slash if fanged). FL `05-combat-and-damage.md:293`.
Plus **GRAPPLE** (unarmed; both fall prone, opponent drops weapon, only BREAK FREE / grapple-attack allowed), **SHOVE** (knock prone; HOOK/shield), **DISARM** (vs 1H = 1⚔, 2H = 2⚔; opponent may take the ⚔ as AGILITY damage to keep the weapon), **HOLD FAST** (+1 parry or +1 dodge; +1 ⚔ needed to shove/disarm/grapple you), **SWING WEAPON** (heavy only; +1 damage on the following slash/stab). FL `05-combat-and-damage.md:295, 315-325, 319`.

**West — a single Melee attack verb with a stunt menu and modifier options:**
- Roll FIGHTIN' (+ weapon gear mod); hit = weapon Damage as Shakes/Hurts (first point Shakes, then alternate). West `05-conflict-and-damage.md:148-149`.
- **Stunts** per extra ⚔: +1 damage (repeatable) / knockdown-or-pushback / hold-in-Grapple / inflict a critical injury (if enough ⚔ to meet the weapon's Crit Rating) / **bank a Carry-Forward Bonus** (+1 on a normal success, +2 on a critical of 3+ net ⚔, to your next attack — see `00 §4`). West `05-conflict-and-damage.md:151-156`.
- **All-Out Attack** — fast Prepare + slow attack for +2 (reduced to +1 with a Called Strike). West `05-conflict-and-damage.md:139`.
- **Called Strikes** — −3 to target a location or cause a specific effect (disarm, trip); All-Out + Called = +1 not +2. West `05-conflict-and-damage.md:141-145`.
- **Grappling** — initiated as a stunt; once locked, the key ability becomes **LABOR** not FIGHTIN'; instigator gets +2; both count as Prone vs others; resolve via opposed LABOR (subdue / break free / fight-over-weapon). West `05-conflict-and-damage.md:178-192`.
- **Shove / Disarm** — fast FIGHTIN' roll; on success choose the declared effect; extra ⚔ as normal stunts. West `05-conflict-and-damage.md:198-207`.

**Generic mechanism — the melee move menu:** a small set of attack verbs (FL: slash/stab/punch/grapple; West: melee-attack + All-Out/Called modifiers) layered on the action budget, each with a weapon prerequisite, a damage expression, and a defense-interaction profile. The genre decides whether melee is *verb-rich* (FL's slash/stab/punch each feel different and interact with defense differently) or *modifier-rich* (West's single verb tuned by All-Out/Called/Stunt). Both converge on grapple as a state-change (prone + restricted action set + opposed strength to resolve).

**Design intent:** melee is where the action budget, reach, and reaction layers all intersect, so the move menu is what makes that intersection *legible*. FL's three verbs make weapon choice and defense choice a paired tactical puzzle (a stab beats a dodge, a shield beats a stab). West's stunt menu makes *extra successes* meaningful in melee (otherwise surplus ⚔ are wasted) and gives the player narrative authorship over the hit. **Layer:** General (melee exists in any combat game); verb-richness is a design dial.

**Dials & instantiation recipe:**
1. **Melee verb count** — 3 (FL's slash/stab/punch) / 1 + modifiers (West). More verbs = more weapon-tactical depth; fewer = faster resolution.
2. **Defense-interaction matrix** — FL's slash/stab/shield table / none. Add when weapon-vs-weapon dueling is the genre's heart.
3. **Extra-success economy** — FL's "+1 damage per extra ⚔" / West's stunt menu (damage, movement, grapple, crit). West's menu gives players more authorship; FL's is faster.
4. **Modifier stack** — All-Out (+2) / Called (−3) / Prone-target (+2). West's table is the calibrated point; FL folds most of these into the action menu.
5. **Grapple model** — both converge on prone + opposed strength + restricted actions. This is the canonical grapple dial; reuse as-is.

## 10. Ranged conflict

**Both games resolve ranged attacks with the SHOOTIN'/MARKSMANSHIP ability + range modifiers; the genre divergence is in the *weapon-action economy*.**

**FL — bow/crossbow/throw with a READY/LOAD economy and weapon features:**
- **READY WEAPON** (fast) before each bow/sling shot; once readied you can only SHOOT or AIM. Crossbows skip READY but require LOAD (slow) before each shot. FL `05-combat-and-damage.md:373-375`.
- **AIM** (fast) — +1 die vs moving target, +2 vs a target that didn't MOVE last Round; must AIM and SHOOT same Round; can't AIM an aware Arm's-Length opponent. FL `05-combat-and-damage.md:379`.
- **SHOOT** (slow) — MARKSMANSHIP + weapon Gear Bonus; can be dodged; parry requires shield/parrying weapon (counts as stab). FL `05-combat-and-damage.md:383`.
- **Range mods:** Arm's Length −3 (or +3 vs oblivious), Near 0, Short −1, Long −2, Distant −3 (requires Aim). FL `05-combat-and-damage.md:359-367`.
- **Weapon features** (LOAD, LOAD X2, READY, WINDLASS, PIERCE ARMOR, HIGH-VELOCITY, MISFIRE, etc.) encode the firearm/crossbow behavior in the gear tag rather than a separate action economy. FL `05-combat-and-damage.md:498-536`.

**West — a deep firearm-action economy + cover + signature tricks:**
- **The weapon's "action"** determines the prepare step: **single-action** pistols and **lever-action** rifles need a fast Prepare (cock/chamber) before each shot; **double-action** and **breech** weapons don't. Bows need Prepare to nock. West `05-conflict-and-damage.md:68, 243-251`.
- **AIM** (fast) +2; lost if you do anything else or get hurt. **QUICK SHOT** (fast, −2) lets you shoot as a fast action. West `05-conflict-and-damage.md:253, 259`.
- **CALLED SHOTS** −3 to hit a location or cause an effect (shoot a gun from their hand, wing them prone); Aim + Called = +1 not +2. West `05-conflict-and-damage.md:255-257`.
- **Range mods:** Near +1, Short 0, Medium −1, Long −2, Distant −3, Arm's Length −3 (or +3 vs inactive); target size +2/−2; partial/good/heavy cover −1/−2/Called-only. West `05-conflict-and-damage.md:261-265`.
- **Stunts** per extra ⚔: +1 damage / pin-down (1 Doubts) / knockback / crit (if ⚔ ≥ Crit Rating) / **bank a Carry-Forward Bonus** (+1 normal / +2 critical of 3+ net ⚔, to your next shot — see `00 §4`). West `05-combat-and-damage.md:269-274`.
- **FANNING** (single-action pistol, ≥4 bullets, two hands, whole Round): −2 (−1/extra target up to 3); first success = two bullet-hits; further successes add a third target or stunts; crit rolls twice take lesser; gun emptied. West `05-conflict-and-damage.md:327-348`.
- **OVERWATCH** (fast, ranged weapon, no enemy at Arm's Length): cover a direction; between now and your next Round you may fire at a target in that lane, resolved before all other declared actions. Lost if you do anything but shoot that direction, are melee-attacked, or take damage. West `05-conflict-and-damage.md:350-366`.
- **RELOAD** — 2 cartridges per fast action; a revolver takes 3 actions to fully reload, a double-barrel 1, a 15-round magazine 4 Rounds. West `05-conflict-and-damage.md:381-385`.
- **COVER** as both to-hit penalty (above) and protection dice (Cover Rating). West `05-conflict-and-damage.md:375-379`.

**Generic mechanism — "ranged = positioning + reload economy":** ranged conflict is the action budget applied to a *prepare-shoot-reload* loop, tuned by range/cover/size modifiers. The genre decides how much of the weapon's behavior lives in (a) a **prepare/reload action economy** (West's cock/chamber/reload, FL's READY/LOAD), (b) **weapon-feature tags** (FL's gear features), and (c) **signature tricks** (West's Fanning, Overwatch, Quick Shot). Both games use AIM as the "+bonus fast action before the shot" and converge on the Arm's-Length-is-hard / oblivious-is-easy range polarity.

**Design intent:** ranged conflict is where the engine proves it can model a *weapon technology* rather than just a damage number. The prepare/reload economy is the scarcity that makes ammunition and weapon choice matter — a single-action revolver *feels* different from a double-action because of the cocking tax, not because of a damage delta. Cover is the ranged-defense layer (since you can't parry a bullet), and West's dual cover model (to-hit penalty + protection dice) is the genre's signature. FL pushes the same depth into *weapon features* (PIERCE ARMOR, HIGH-VELOCITY, MISFIRE) so a crossbow and a longbow behave differently. Without the reload/prepare economy, ranged combat is just "I shoot, damage"; with it, every shot is a logistics decision. **Layer:** General (ranged exists); the reload/feature/trick depth is a design dial calibrated by genre.

**Dials & instantiation recipe:**
1. **Reload/prepare economy depth** — none (throw-only) / READY-before-shot (FL bows, West single/lever) / LOAD-per-shot (FL crossbows) / cartridge-count + reload-actions (West firearms). Depth scales with the genre's weapon technology.
2. **Weapon-behavior encoding** — feature tags (FL) / action-type tags (West's single/double/lever). FL's tags are more composable; West's are more legible.
3. **Signature tricks** — Fanning / Overwatch / Quick Shot (West) / Aim + High-Velocity (FL). Add the ones that match the genre's iconography; these are the *cinematic* verbs.
4. **Cover model** — to-hit-only / protection-only (FL) / both (West). West's dual model is the gold standard for firearm genres.
5. **Range polarity** — both use Near=easy, extremes=hard, Arm's-Length-vs-aware=hardest, Arm's-Length-vs-oblivious=easiest. Reuse this polarity; it's genre-neutral.
6. **Extra-success economy** — FL's +1 damage/⚔ / West's stunt menu (damage, pin-down-as-mental-damage, knockback, crit). West's pin-down stunt is notable: ranged attacks can inflict *mental* pressure, not just physical.

## 11. Social conflict

**Both games treat social conflict as a parallel mode to physical combat** — same opposed-roll spine, a "negotiating position" modifier table, and the rule that you can't make an NPC do anything wholly against their interest no matter how well you roll.

**FL — Manipulation vs Insight + local Reputation:**
- Make an opposed roll of **MANIPULATION** vs the opponent's **INSIGHT**; it's a slow action *only for you*. FL `05-combat-and-damage.md:405-407`.
- On success, the opponent must **do what you want OR immediately attack you with violence**; even compliance may come with a counter-demand. FL `05-combat-and-damage.md:409`.
- **Negotiating position** modifies your roll: +1 each for more people on your side / the ask costs them nothing / they're damaged / you've helped them before / you present well; −1 each for their side having more people / you ask for something valuable or dangerous / they've nothing to gain / communication trouble / range is Short+. FL `05-combat-and-damage.md:413-427`.
- **Reputation** — use the fellowship's local Reputation; higher than opponent = +1, more than double = +2 (symmetric). FL `05-combat-and-damage.md:429-431`.
- Range usually Near; can extend to Short/Long at GM discretion with negative mods. Group manipulation targets the leader/spokesperson (−1 if they outnumber you). FL `05-combat-and-damage.md:433-439`.

**West — Presence/Performin' vs Insight + Social Conflict by Mail:**
- Opposed **PRESENCE** *or* **PERFORMIN'** (circumstance-chosen) vs **INSIGHT** (GM sets crowd INSIGHT). If in Rounds, a slow action. West `05-conflict-and-damage.md:418-420`.
- Win by *N* successes: the loser must comply, or suffer **N points of Vexes or Doubts** (mental damage). Symmetric — if they out-roll you, *you* back down or take the damage. A character can be **Broken** by social damage. West `05-conflict-and-damage.md:422`.
- If neither yields, the conflict continues until one gives in or is Broken; a Doubts-Broken loser "hides in confusion and despair," a Vexes-Broken loser "flies into an angry rage." West `05-conflict-and-damage.md:424`.
- **Negotiating position** (+1: more people / ask costs nothing / helped before / presented well; −1: their side bigger / ask is valuable-dangerous / nothing to gain). West `05-conflict-and-damage.md:426-437`.
- Usually no initiative draw — social conflict plays as back-and-forth narrative over a longer timeframe, no further than Short range. West `05-conflict-and-damage.md:410`.
- **Social Conflict by Mail** — a letter or telegram uses **BOOKLEARNIN'** instead of Presence/Performin'. West `05-conflict-and-damage.md:414-416`.

**Generic mechanism — "social conflict as parallel to physical":** social conflict reuses the opposed-roll + modifier-table + can't-compel-self-harm spine of combat, but maps onto *mental/social attributes* and resolves via a different currency. The two games diverge on the *resolution currency*: FL resolves social conflict as a binary compel-or-provoke-violence (the stakes escalate to physical on failure); West resolves it as a *damage-dealing* contest (surplus successes become Vexes/Doubts that can Break a character), making social conflict genuinely attritional and able to end a scene without a punch thrown.

**Design intent:** making social conflict mechanically parallel to physical means the *face* character is as load-bearing as the *fighter* — you can win scenes with words, and the rules take that seriously rather than hand-waving it to roleplay. FL's "comply or attack" rule is brilliant because it makes a failed persuasion *dramatically escalate* (now it's a fight), so social conflict is never wasted screen time. West's damage model is brilliant because it lets a social conflict *end* a character (Broken by Doubts/Vexes) without anyone drawing a weapon, which is true to a genre where reputation and nerve are the real currency. The "negotiating position" table (near-identical in both) is what makes the fiction *load-bearing* on the roll — your leverage, your numbers, your history all become dice. **Layer:** General (social conflict as a mode); the resolution currency (binary-escalate vs damage-attrition) is a design dial.

**Dials & instantiation recipe:**
1. **Resolution currency** — binary compel-or-escalate (FL) / damage-attrition that can Break (West) / hybrid. FL's model keeps scenes short and punchy; West's lets social conflict *be* the combat.
2. **Attribute mapping** — FL: Manipulation vs Insight; West: Presence/Performin' vs Insight (+ Booklearnin' for mail). Map to whatever your attribute array calls "social offense/defense."
3. **Leverage modifier table** — both converge on the same +1/−1 factors (numbers, cost, history, presentation). Reuse this table near-verbatim; it's genre-neutral.
4. **Reputation/standing integration** — FL's local Reputation (Optional in spirit, ties to the Stronghold system); West folds reputation into the genre's core. Add when the genre runs on social standing.
5. **Medium expansion** — West's Social Conflict by Mail (BOOKLEARNIN'). Add telegraph/letter/radio variants for any genre with written communication.
6. **Initiative** — usually none (narrative back-and-forth); both permit Round-structuring if needed. Default to no-initiative for speed.

## 12. The Duel / Face-Off special-conflict pattern

**West's Duel is the engine's most structured conflict — a three-phase scripted mini-scene** that resolves a signature genre moment *outside* the normal action budget. FL has a different special-conflict pattern (the ambush/sneak-attack). Both are instances of a reusable abstraction: the *ceremonial scripted conflict*.

**West — the Duel (Face Off → Go for Your Guns → Shoot-off):** "All the actions of the duel play out within the space of one Round, and effectively take place simultaneously. During the duel we do not break down the characters' actions into fast and slow actions." West `05-conflict-and-damage.md:280`.

1. **THE FACE OFF** — opposed **PRESENCE** roll; the winner gets **+1 Draw bonus per success over the opponent** (psyche them out, read their eyes, get the drop). West `05-conflict-and-damage.md:282`.
2. **GO FOR YOUR GUNS** — opposed **LIGHT-FINGERED** roll to draw, modified by: the weapon's Draw modifier, gear bonuses (quick-draw holster), talent bonuses, and the Face Off bonus. Winner draws first; a tie = simultaneous fire. West `05-conflict-and-damage.md:312-319`.
3. **THE SHOOT-OFF** — the Draw winner shoots first with **bonus SHOOTIN' dice = successes won on the Draw**; if the loser is still standing, their return shot resolves. West `05-conflict-and-damage.md:321`.
4. **IS IT OVER…?** — keep fighting or declare honor satisfied; if it continues, draw initiative cards and resume normal slow/fast action combat. West `05-conflict-and-damage.md:323`.
5. **Trouble in a duel** — Trouble that would cost an action instead inflicts −1 to the next duel roll. West `05-conflict-and-damage.md:325`.

Crucially, West *generalizes* the pattern: "Many situations…lend themselves to using the dueling rules, even those that are not formal duels. Any situation where iron has not yet been drawn but two characters make eye contact, knowing they are about to come into conflict, can be resolved using these rules." West `05-conflict-and-damage.md:284-286`. (You cannot FAN during the duel — only after the first shot, when normal combat resumes. West `05-conflict-and-damage.md:348`.)

**FL's special-conflict pattern — the ambush/sneak-attack:** a structured opening that grants a free pre-initiative action and denies reactions.
- **SNEAK ATTACK** — opposed SNEAK vs the target's scout/awareness, modified by range (Arm's Length −2 … Long +1); on success, you get **one free action (slow *or* fast, not both) before initiative**; the target **cannot DODGE or PARRY**. FL `05-combat-and-damage.md:218-220, 222-227`.
- **AMBUSH** — a group-vs-group sneak where the attacker waits; +2 because the *target* is moving; resolved by lowest-SNEAK attacker vs highest-scout target. FL `05-combat-and-damage.md:229-231`.
- **Stealth mods** — −1 for heavy armor or large shield, −1 per negative MOVE mod, +1 if both hands free or only tiny/light items. FL `05-combat-and-damage.md:233`.

West's sneak/ambush converges on the same structure: opposed **MOVE vs HAWKEYE**, range mods, success = one free opening action before initiative, target **cannot Block or Dodge**, plus a flat **+3 to the attack pool for any undetected attacker**. West `05-conflict-and-damage.md:121-127, 367-373`.

**Generic mechanism — the "ceremonial scripted conflict":** a *special conflict mode* that (a) suspends or replaces the normal action budget, (b) resolves a high-stakes genre-iconic moment as a *sequence of phased opposed rolls* whose margins carry forward as bonuses, and (c) returns to normal combat if unresolved. The Duel is the *simultaneous-phased* variant (Face Off bonus → Draw bonus → Shoot-off bonus, all in one Round). The Ambush is the *opening-advantage* variant (win a stealth roll → free unreactionable action → normal combat). Both are reusable templates: any genre has signature moments (the standoff, the ambush, the formal challenge, the duel-by-champion) that deserve a scripted mini-scene rather than a single attack roll.

**Design intent:** ceremonial conflict exists to *dramatize the genre's signature beat* with mechanical weight. A Western gunfight-to-first-draw is the emotional climax of the genre; collapsing it to "roll SHOOTIN', damage" would waste it. The phased structure makes *each prior roll feed the next* (your nerve feeds your draw feeds your shot), so the whole duel is one escalating stake-chain that a single die-roll can't capture. FL's ambush serves a different intent: it rewards *preparation and stealth* with a decisive opening, making "scout and set up" a real tactic rather than flavor. Both patterns share the principle that *some conflicts deserve more structure than the action budget allows*. **Layer:** Optional — a game need not have a ceremonial mode, but every genre benefits from one for its iconic moment.

**Dials & instantiation recipe:**
1. **Ceremonial mode presence** — Duel (West) / Ambush (both) / formal-challenge (genre-custom) / none. Include at least one for the genre's signature beat.
2. **Phase structure** — West's 3-phase carry-forward (Presence → Light-Fingered → Shootin') is the canonical "escalating bonus chain" template. Generalize as: *phase-1 social/mental* → *phase-2 speed/technique* → *phase-3 resolution*, with each margin becoming the next bonus.
3. **Action-budget handling** — suspend entirely (West duel) / grant one free pre-initiative action (both ambush) / operate within the budget. Suspension is for truly ceremonial moments; the free-action model is for opening advantages that flow into normal combat.
4. **Reaction denial** — both ambush variants deny the target's defense on the opening blow. This is what makes the ambush *decisive*; use sparingly.
5. **Generality** — West explicitly opens the Duel to any eye-contact-before-iron moment. Build your ceremonial mode to trigger on a *fictional condition*, not a formal declaration, so it sees use.

## 13. Morale and rout

**Both games mark Morale & Rout as optional** — a disengagement layer for NPC groups only (players judge their own fear).

**FL — morale rating in dice, triggered by combat turning-points:** Check at end of Round when: the leader is Broken/killed; half the fighters are Broken/dead/fled; a monstrous/demonic display shakes the side; a fear attack lands ≥3 ⚔ with an escape route; the side is plainly outmatched. Each side has a **morale rating in dice** (hardened enemies ~6; add for veterans/fanatics/upper-hand; subtract for rabble/beasts/pressed men, −1 die per factor after the first). Roll the rating; success = hold (no recheck for 2 Rounds); failure = choose: fall back and flee / surrender if mercy seems possible / cower-scatter-bargain-break-formation / fight on in fear at −2. Undead/demons/monsters/fanatics usually immune. FL `05-combat-and-damage.md:191-212`.

**West — flat dice by troop quality, triggered similarly:** Check when: leader Broken/captured/killed; half down/fleeing/out; plainly outmatched; terrifying display/slaughter/failed charge breaks nerve. Roll **2 dice** (rabble/green/drunks) / **4** (deputies/ranch hands/hired muscle) / **6** (hard cases/veterans/still-think-they-can-win); success = hold, failure = flee / surrender / scatter for cover / freeze and fight at −2. Religious fanatics, cornered killers, disciplined troops may ignore at GM discretion. West `05-conflict-and-damage.md:213-229`.

**Generic mechanism — "the disengagement layer":** an *optional* rule that lets NPC groups break and run when the fight turns, resolving combat *without* total annihilation. Triggered by named combat turning-points (leader down, half-down, terrifying display, plain outmatch); resolved by a single morale-dice roll against a troop-quality rating; failure yields a fiction-appropriate rout outcome (flee/surrender/scatter/fight-in-fear). The dial is the *rating model* (FL's per-side dice rating with add/subtract factors vs West's flat three-tier ladder).

**Design intent:** morale exists so that *not every fight is to the death*. Without it, every NPC fight ends in slaughter, which is both unrealistic and exhausting. With it, the GM can resolve a turning fight with a single roll and the world feels alive — enemies break, surrender, scatter. The "players don't roll morale for themselves" rule is essential: it preserves PC agency (you decide when *you* retreat) while letting the world react believably. The troop-quality rating (both games) encodes *who these fighters are* in a single number. **Layer:** Optional in both books; recommended for any game where combat is frequent and total-annihilation would be tedious or implausible.

**Dials & instantiation recipe:**
1. **Presence** — on/off. Default on for any game with frequent NPC combat.
2. **Trigger list** — both converge on (leader down / half-down / terrifying display / plain outmatch). Reuse this list; it's genre-neutral.
3. **Rating model** — per-side dice with add/subtract factors (FL) / flat 3-tier ladder by troop quality (West). FL's is more tunable per-enemy; West's is faster at the table.
4. **Failure outcomes** — both converge on (flee / surrender / scatter-cover / fight-in-fear-at-−2). Reuse.
5. **Immunity list** — undead/demons/fanatics (FL) / fanatics/cornered-killers/disciplined-troops (West). Tune to the genre's fearless archetypes.

## 14. Mounted combat

**Both games treat a mount as an extension of positioning and a combat modifier**, with West doing far more (horses as a subsystem).

**FL — mounted combat as a flat modifier + reach interaction:** Attacking a mounted opponent suffers **−1**; **polearms ignore this** and may add their item bonus when **SHOVING** a mounted opponent. **OPEN** zones are "ideal for mounted combatants." FL `05-combat-and-damage.md:135, 167, 518`. (FL's mounted model is light — the mount is a tactical condition, not a statted participant.)

**West — horses as a full subsystem (riding, breeds/qualities/flaws, Spooked Horse):** West's mounted model is far deeper — **Ride Horse** is a fast ANIMAL HANDLIN' action (West `05-conflict-and-damage.md:110`); the lasso (ANIMAL HANDLIN' to snare, then opposed ANIMAL HANDLIN' vs LABOR to grapple) is a signature mounted/rope tactic (West `05-conflict-and-damage.md:231-237`); **falling from a bucking/fast/jumping horse** is an 8-dice attack (damage 1, Crit 2) halved by a MOVE roll (West, in the harm file). The horse is a statted entity with **breeds, qualities, and flaws**, and a **Spooked Horse** state that can unseat or endanger the rider.

**Generic mechanism — "mount as extension of positioning":** a mount does three things in the conflict engine: (1) it modifies to-hit (FL's −1 vs mounted) and movement (mounts cover ground faster, often ignoring zone/rough penalties); (2) it carries a **fall/dismount risk** (West's 8-dice fall); (3) in deeper implementations it is a **statted entity** with its own abilities (ANIMAL HANDLIN' to control) and its own failure states (Spooked). The genre decides how much of the mount is *condition* (FL) vs *participant* (West).

**Design intent:** a mount should change *how you fight*, not just how fast you move. FL's light model keeps mounted combat from bogging down in a second character sheet — it's a tactical edge (height, reach-polearm synergy, open-zone advantage) and a small to-hit tax. West's deep model makes the *horse* a character with agency (it can spook, fall, be lassoed) because the genre's iconography is men-on-horses; the horse *must* be a participant for cattle drives, cavalry, and horseback gunfights to feel right. **Layer:** Situational (mounted rules only matter when mounts are in play); the depth (condition vs participant) is a design dial calibrated by how central mounts are to the genre.

**Dials & instantiation recipe:**
1. **Mount depth** — condition (FL's −1 and reach synergy) / participant (West's statted horse + ANIMAL HANDLIN' + Spooked). Condition-depth for low-mount genres; participant-depth for mounted genres.
2. **To-hit modifier vs mounted** — −1 (FL). Small enough to matter, large enough to feel like an advantage.
3. **Reach/mount synergy** — polearms ignore the mounted penalty and SHOVE with bonus (FL). Generalizes to "long weapons are the answer to a mount."
4. **Dismount/fall risk** — West's 8-dice fall attack (halved by MOVE). Include whenever mounts move at speed; the dial is the damage and the mitigation roll.
5. **Mount-as-statted-entity** — off (FL) / on with abilities + states (West). Turn on only if the mount is a recurring character or the genre runs on horsemanship.
6. **Signature mounted tactic** — West's lasso (ANIMAL HANDLIN' snare → opposed grapple). Generalize to "a genre-specific ranged-grapple tool."

## 15. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Initiative archetype** | Rolled segment (AGILITY+WITS ⚔), sticky in-Round, simultaneous ties | Random card draw, redrawn each Round, suit-breaks-ties | Stat-coupled & predictable vs volatile & dramatic | FL-style for tactical/character-build games; West-style for chaotic/genre-iconic games |
| **Optional/Fast initiative** | Fast Skill Roll (party-before-enemies if each PC gets ≥1 ⚔; +2 to side that started combat) | Fast Initiative (Quick roll; party-first if ≥half succeed) | Both collapse to side-initiative | Use either for skirmishes; both exist to skip bookkeeping |
| **In-Round order malleability** | Delay to lower segment; FEINT swaps segments | Once-per-scene ally card-swap | Solo-tactical vs cooperative-tactical | FL for duel-style play; West for party-coordination play |
| **Range band count** | 5 (no Medium) | 6 (adds Medium) | Coarser vs finer ranged granularity | West's 6 for firearm genres; FL's 5 for melee/bow genres |
| **Terrain layer** | Zone features (Cramped/Rough/Open/Dark) + borders (Blocked/Obscured) | Cover ratings + to-hit penalty grades (Partial/Good/Heavy) | Movement/line-of-sight pressure vs concealment/defense pressure | FL-zones for dungeons/ruins; West-cover for gunfights; hybrid possible |
| **Cover as armor** | On (Cover Rating table, no to-hit penalty) | On (Cover Rating table + to-hit penalty grades) | Soak-only vs soak + to-hit | West's dual model for firearm genres; FL's soak-only for lower-tech |
| **Reach subsystem** | Deep (Short/Normal/Long + CUT IN/BRACE/INTERCEPT/LOCK SHIELDS/FEINT/HALF-HAND) | Light (Brace for ranged only; melee reach implicit) | Melee tactical depth vs simplicity | FL-reach for melee/historical genres; omit for ranged-centric genres |
| **Melee verb model** | Verb-rich (Slash/Stab/Punch, each with defense profile) | Verb-single + modifiers (Melee attack + All-Out/Called/Stunt menu) | Weapon-as-puzzle vs success-as-authorship | FL for weapon-dueling genres; West for cinematic narrative combat |
| **Defense verbs** | Dodge (MOVE) + Parry (MELEE+gear) | Dodge (MOVE) + Block (FIGHTIN') + Protect Another | Two-verb vs three-verb | Add Protect Another for bodyguard/team play |
| **Defense economy** | Pure success-cancellation with weapon-type matrix | Success-menu: cancel damage *or* counterattack | Fast/resolved vs aggressive/choice-laden | FL for speed; West for "defense can hurt" |
| **Ranged weapon model** | Bow/crossbow/throw + READY/LOAD + gear-feature tags (PIERCE/HIGH-VEL/MISFIRE) | Firearm-action economy (single/double/lever) + Fanning + Overwatch + Quick Shot + reload-count | Feature-tag depth vs action-economy depth | FL-features for fantasy; West-actions for firearm genres |
| **Signature ranged tricks** | Aim, High-Velocity, Pierce Armor (via tags) | Fanning, Overwatch, Quick Shot, Called Shots | Tag-composable vs named-cinematic | West's named tricks for genre iconography |
| **Social conflict currency** | Binary: comply *or* escalate to violence | Damage-attrition: surplus ⚔ as Vexes/Doubts, can Break | Short/punchy vs attritional/scene-ending | FL for escalation-prone games; West for reputation-as-combat games |
| **Social attribute mapping** | Manipulation vs Insight | Presence/Performin' vs Insight (+ Booklearnin' by mail) | Single-ability vs circumstance-chosen | Map to your attribute array; West's medium-expansion is reusable |
| **Reputation in social** | Local Reputation mod (+1/+2, symmetric) | (folded into genre core, not a separate table) | Explicit-table vs implicit | FL-table when reputation is a tracked subsystem |
| **Ceremonial conflict** | Ambush/sneak-attack (free pre-initiative action, no reactions) | Duel: Face Off → Go for Your Guns → Shoot-off (phased bonus chain) | Opening-advantage vs escalating-script | Include the genre's signature beat; both patterns are reusable |
| **Morale rating model** | Per-side dice with add/subtract factors (veterans +, rabble −) | Flat 3-tier (2/4/6 dice by troop quality) | Tunable-per-enemy vs fast-at-table | FL for bespoke foes; West for quick resolution |
| **Mount depth** | Condition (−1 vs mounted; polearm synergy) | Participant (statted horse, ANIMAL HANDLIN', Spooked, lasso, fall-risk) | Tactical-edge vs full-subsystem | FL for low-mount genres; West for mounted genres |
| **Time-unit explicitness** | Round/Turn/Shift in prose (Round ~10s–1min; Turn ~15min) | Round/Turn/Shift as a fixed table (Round 5–10s; Turn 5–10min; Shift 6h; 4 Shifts/day) | Loose vs calendrical | West's table when downtime beats matter |

## 16. Dials and instantiation recipe

Each dial has FL and West as two calibrated points. To build a new game's conflict system, set each dial.

1. **Time-unit ladder** — Round/Turn/Shift with explicit durations + day structure. *(Sets the clock for each play-mode.)*
2. **Initiative archetype** — rolled-sticky / random-redrawn / side-based / fixed. *(Sets combat-order volatility and stat-coupling.)*
3. **Stat coupling of initiative** — couple to a speed stat (FL) / decouple via cards (West). *(Whether agility is a combat stat.)*
4. **Range band count** — 5 (FL) / 6 with Medium (West). *(Ranged granularity.)*
5. **Terrain layer** — zone-features-and-borders (FL) / cover-ratings-and-to-hit-grades (West) / hybrid / none. *(What kind of spatial pressure.)*
6. **Cover model** — soak-only (FL) / soak + to-hit penalty (West) / none. *(Ranged-defense depth.)*
7. **Reach subsystem** — on with full verb set (FL) / light-ranged-only (West) / off. *(Melee tactical depth.)*
8. **Action budget** — 2 actions/Round = (1 slow + 1 fast) ∨ (2 fast). *(The load-bearing constant — keep at 2.)*
9. **Reaction economy** — draws from shared budget (both) / separate pool / free. *(Never free without rebalancing damage.)*
10. **Defense verbs & economy** — dodge+parry, success-cancellation (FL) / dodge+block+protect, success-menu with counterattack (West). *(Defense texture and aggression.)*
11. **Melee verb model** — verb-rich with defense matrix (FL) / verb-single + stunt menu (West). *(Weapon-puzzle vs narrative-authorship.)*
12. **Ranged weapon-behavior encoding** — gear-feature tags (FL) / action-type economy (West). *(Where the weapon's behavior lives.)*
13. **Reload/prepare depth** — none / READY-per-shot / LOAD-per-shot / cartridge-count. *(Scales with weapon technology.)*
14. **Signature ranged tricks** — Aim-only / +Fanning+Overwatch+Quick Shot (West) / genre-custom. *(The cinematic verbs.)*
15. **Social conflict currency** — binary comply-or-escalate (FL) / damage-attrition-can-Break (West). *(Whether social conflict can end a character.)*
16. **Social attribute mapping + medium** — single ability vs circumstance-chosen; add mail/telegram/radio variants. *(Range of social scenes.)*
17. **Reputation integration** — explicit local-Reputation table (FL) / folded-into-core (West) / none. *(When reputation is a tracked subsystem.)*
18. **Ceremonial conflict mode** — Duel phased-bonus-chain (West) / Ambush opening-advantage (both) / genre-custom / none. *(Dramatize the signature beat.)*
19. **Morale & rout** — on/off; rating model per-side-dice (FL) or flat-3-tier (West). *(Whether fights end without annihilation.)*
20. **Mount depth** — condition (FL) / participant (West). *(How central mounts are.)*

**Instantiation recipe (any genre):**
1. **Start with the action budget** (dial 8) — keep the 2-actions/Round rule. Everything else hangs off it; changing it breaks the engine's balance.
2. **Wire reactions to the budget** (dial 9) — this single coupling prevents defense-bloat and is non-negotiable for the engine to function.
3. **Pick the initiative archetype** (dial 2) to match the genre's volatility (rolled for tactical, cards for chaotic, side-based for fast).
4. **Choose the terrain layer** (dial 5) and **cover model** (dial 6) to match where the genre's spatial pressure lives (movement/LOS for dungeons, concealment for gunfights).
5. **Decide reach subsystem presence** (dial 7) based on how central melee weapon-choice is; turn off for ranged-centric genres.
6. **Set the ranged weapon-behavior encoding** (dial 12) and **reload depth** (dial 13) to match the genre's weapon technology; add **signature tricks** (dial 14) for the genre's iconography.
7. **Choose the social-conflict currency** (dial 15) — binary-escalate for short scenes, damage-attrition for reputation-as-combat.
8. **Build one ceremonial conflict mode** (dial 18) for the genre's signature beat (the standoff, the ambush, the formal challenge).
9. **Turn on morale & rout** (dial 19) if NPC combat is frequent; pick the rating model by table-preference.
10. **Validate the whole against the action-economy math**: with 2 actions/Round and reactions drawn from the budget, a combatant can do at most one decisive thing per Round while defending — confirm that damage, armor, and HP produce fights that last 3–6 Rounds (long enough for tactics, short enough to stay tense).

## 17. Design intent

The conflict engine is engineered to make **combat a sequence of trade-offs, not a slugfest.** Specifically:

- **The two-actions-per-Round budget is the load-bearing rule.** It guarantees scarcity: you cannot attack, defend, *and* reposition in one Round, so every turn is a hand of two cards you must choose how to play. This is what makes the difference between "I hit it again" and a real tactical decision.
- **Reactive defense draws from the same budget**, which is the engine's defense against defense-bloat. Because dodging now costs you an action later, you can't turtle — eventually you must act, and that's when you're vulnerable. Other d6 systems that make reactions free end up with combat that never ends.
- **Named range bands replace a grid with a conversation.** You never measure feet; you describe position and the fiction carries the tactics. This is what makes the engine playable without a battlemat and keeps the focus on the fiction.
- **The terrain layer is where each genre injects its signature pressure** — FL's zones make *movement and line-of-sight* scarce (dungeons, ruins); West's cover makes *concealment* scarce (gunfights). Same abstraction, opposite ends: "what does the ground do to you?" vs "what does the ground do for you?"
- **The slow/fast split creates tempo.** Fast actions let you do two small things (move + draw, dodge + reposition), so a Round of pure movement or pure defense is viable — which makes disengagement, repositioning, and readiness real tactics rather than wasted turns.
- **The ceremonial conflict mode dramatizes the genre's signature beat.** A Western gunfight-to-first-draw or a dungeon ambush deserves more structure than a single attack roll; the phased bonus-chain (West's Duel) and the opening-advantage (both games' Ambush) are reusable templates for giving iconic moments mechanical weight.
- **Social conflict is mechanically parallel to physical**, so the *face* character is as load-bearing as the *fighter*. FL's comply-or-escalate makes a failed persuasion dramatically *become* a fight; West's damage-attrition lets a social conflict *end* a character without a punch. Both take "winning with words" seriously rather than offloading it to roleplay.

The FL-vs-West divergence is the engine's proof that **the same action-economy spine produces opposite combat feels by swapping the flavor layers.** FL builds a *reach-and-zone* tactical puzzle for a melee-centric dungeon-crawler; West builds a *firearm-and-cover* volatility engine for a ranged-centric Western. A new genre's job is to identify *its* signature spatial pressure (zones? cover? altitude? formation?) and *its* signature ceremonial beat (the standoff? the dogfight? the chase?), then wire them onto the same 2-actions-per-Round budget.
