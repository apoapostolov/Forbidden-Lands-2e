<!-- markdownlint-disable MD013 MD024 -->

# Corruption & Taint — The Doom Spiral

> **STATUS: WORKSHOP MODULE.** A power-at-a-cost subsystem: using forbidden power *refuels* you in the short term (it is tempting — you gain metacurrency, potency, or escape from a bad roll) but climbs a **doom ladder** that eventually destroys, transforms, or un-mans you. *Core is generic; the worked example (witch-hunting dark fantasy) is illustrative.*

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
8. Worked genre example — Witch-hunting dark fantasy

## 1. Origin — how this was built

- **Source primitives:** **P5** (resource die — Corruption as a die that *grows*, steps *up*, the inverse of normal depletion), **P4** (typed D66 — corruption milestone tables: what befalls you at each tier), **P2** (capped metacurrency — corruption *refuels* your pool; that is the temptation), **P10** (protected dial — the Corruption die as an inverted Pride, growing when *used* not when *avoided*).
- **Reinvention operator:** **Inversion + Fusion** (Operators 2 + 4 from `18 §4`). Invert P5 (the die grows instead of depletes) and P10 (the die escalates when the forbidden power is *used*, the exact "Doom" pattern sketched in `18 §6` Worked 4). Fuse the inverted die with P4 for the milestone/consequence tables and with P2 for the temptation that drives the climb. This is the close cousin of `18`'s Doom protected dial, extended into a full five-tier spiral.
- **Target psychology:** **Power-at-a-cost / doom** (`17`, the inverted-P10 cell). Produces *characters who are slowly becoming what they fight.* The drama is the slide, not the single catastrophe — every use is a small betrayal of the character's stated self.
- **Problem solved:** the "cost of power" in many games is either a flat penalty (boring — players just avoid the power) or a single catastrophic mishap (swingy — no slow-burn dread). This module makes the cost a *climb*: a visible ladder with named rungs, where the temptation is real (power now) and the ruin is gradual, legible, and (crucially) *choosable*. It gives the power layer (`05`) the cost its forbidden options require.

## 2. The generic design space

### 2a. Mechanism overview

Each PC who can access forbidden power has a **Corruption die**. Unlike a normal resource die (which *depletes* — steps down on use), the Corruption die *grows* — it steps **up** as you stain yourself, climbing a five-rung doom ladder (D6 → D8 → D10 → D12 → Lost). When you use forbidden power and **gain a benefit** from it, you **roll the Corruption die**: on a 1–2 the power came cheap (nothing happens *this time*); on a 3+ the die steps up one tier. At D12, the next 3+ is a **milestone** — you advance a doom tier and roll on a typed D66 Corruption Milestone table. At tier 5 the character is **Lost**: transformed, un-manned, or removed from play as the genre dictates.

The temptation that drives the climb is the inversion's secret weapon: the forbidden power **refuels your metacurrency** (P2) — and the refuel is paid out **by the Corruption die's face**, so the *more stained* you are, the *more the power pays*. A D12 casting that refuels 12 WP is far harder to forsake than a D6 refueling 6. The spiral is self-reinforcing by construction: the fall and the reward climb the same ladder. This is the engine's signature push-and-pay flipped — where the push costs to convert a fail into a success, here the forbidden power *pays you* to convert a stain into a habit. The deferral is the trap: the cost is probabilistic and future, the benefit is certain and now.

The milestones (P4) are what make corruption **specific and memorable** rather than a hidden tally. Each tier transition fires a typed D66 table split into **families** by what the corruption *is* in your genre (Flesh / Mind / Soul / Shadow / Alien). Every entry carries an *immediate effect* (the visible change), a *long-term tag* (a lasting feature), and an *atonement cost*. The `65`/`66` climax entries at each tier are the un-manning events — permanent transformations that are how the character *leaves* play at the top of the ladder.

### 2b. NEW CONCEPTS introduced

- **NEW CONCEPT — Inverted-step die (Corruption die):** P5 (resource die) normally *depletes* — it steps down on use until the resource is spent. The Corruption die applies **Operator 2 (Inversion)** to P5 and *grows* — it steps **up** on use, the polarity reversed. The step-die math inherits P5's proven curve; the inversion is genuine but small. **What is genuinely new is the doom-ladder application:** no core engine system uses a step-die that climbs toward a character-ending climax. Resource depletion ends in "you ran out"; corruption escalation ends in "you became something else." *Extends the engine by giving the step-die a terminal-transformation payload its depletion parent never carries.*
- **NEW CONCEPT — Refuel-as-temptation (the self-reinforcing trap):** The Corruption die (P5, growing) is **fused** with the metacurrency refuel (P2): casting forbidden power refuels your WP/Faith by the die's *face value*. This couples a **growing doom track** to a **growing reward** — the more stained you are, the more the power pays. No core system links a rising penalty to a rising payoff in this way. The fusion is what makes the spiral *tempting* rather than merely punishing, and it is self-reinforcing by construction: the higher the die, the larger the refuel, the harder to stop. *Extends the engine by welding a doom counter to its own incentive — the cost pays you to incur it.*
- **NEW CONCEPT — Tier-gated milestone tables:** P4 (typed D66) is normally applied **per damage type** (a crit table per weapon family; a mishap table per failure mode). Here P4 is applied **per corruption tier**: the table fires on tier transitions (T2/T3/T4), with the 65/66 climax at each tier being the *transformation moment*. The table is thus not indexed by what hit you but by *how far you have fallen* — the same family read at different tiers produces escalating ruin along a single thematic axis. *Extends P4 by gating the D66 roll on a ladder position rather than a damage source.*

*Everything else in this module is pure recombination of P1–P15: the step-die ladder is P5; the refuel is P2; the milestone table is P4; the tier tags are P8; the tells are fiction (no primitive). Only the three applications above are genuine engine extensions.*

### 2c. Mechanical reference (tables & procedures)

#### The Corruption die ladder

| Tier | Die | Name (generic) | Default tell |
| --- | --- | --- | --- |
| 0 | (none) | **Clean** | — |
| 1 | D6 | **Marked** | A deniable chill; a bad dream; animals shy from you. |
| 2 | D8 | **Tainted** | A visible sign that others can notice if they look. |
| 3 | D10 | **Warped** | An unmistakable change; hard to hide; costs social friction. |
| 4 | D12 | **Lost** (on the brink) | The change is public and active; it acts without your will. |
| 5 | — | **Gone** | Transformed / un-manned / removed from play. |

#### The step-up trigger (Corruption die roll)

Roll the Corruption die **only when a forbidden use gains a benefit** (refuels you, succeeds on a dark casting, or buys off a consequence). Read the face:

| Die face | Result |
| --- | --- |
| **1–2** | **Nothing happens *this time*** — the power came cheap. Die does not step. |
| **3+** | **The die steps up one tier** (D6→D8→D10→D12). |
| **3+ while at D12** | **Milestone** — advance one doom tier and roll on the Corruption Milestone table (below). At tier 5 the character is **Gone**. |

*Note the brake:* there is no "safe ceiling" at D12 — the die cannot be parked at the top to avoid further risk, because a D12 rolling 3+ *is* the milestone. This closes the "only cast when already maxed" exploit (see §6).

#### The refuel math (P2 fusion)

> **WP (or Faith) gained = Corruption die face.**

The forbidden use refuels metacurrency by the *face value shown on the Corruption die rolled*, paid out before the step-up is resolved.

- A **D6** casting that rolls a 6 refuels **6 WP** (then steps up on 3+).
- A **D8** casting that rolls an 8 refuels **8 WP** (then steps up on 3+).
- A **D10** casting that rolls a 10 refuels **10 WP**.
- A **D12** casting that rolls a 12 refuels **12 WP** — and, being 3+, is also the milestone.

The refuel is paid **whether or not the die steps up** (the 1–2 "cheap" result still pays the face). This is the engine of temptation: the benefit is certain and now; only the step-up is probabilistic and deferred.

#### The Corruption Milestone table — Flesh family (full D66)

Roll D66 when a D12 corruption roll hits 3+ (a tier transition). The **Flesh family** is body-horror corruption — the ruin of the flesh. Build parallel families (Mind / Soul / Shadow / Alien) using the same D66 architecture; the row *structure* is identical, the *nouns* change.

Each row carries: the **immediate effect** (visible change), the **long-term tag** (a lasting P8 feature), and the **atonement cost**. Rows are grouped by the tier at which they fire. The **65/66** rows at each tier are the un-manning events.

##### T2 (D8) — the Tainted tier

The corruption becomes visible to anyone who looks. The change is uncomfortable but you remain yourself.

| D66 | Immediate effect (visible change) | Long-term tag | Atonement cost |
| --- | --- | --- | --- |
| 11 | Your wounds heal too fast, and smell of iron and old roses. | **UNSETTLING** (−1 to first-impression social rolls) | Burn a relic of a saint at a shrine. |
| 12 | Your body temperature drops; your skin is cold to the touch in any weather. | **COLD-FLESH** (animals and infants recoil from you) | Bathe in water blessed by three different priests. |
| 13 | A permanent bruise blooms under the skin of your chest, in a shape no blow made. | **MARKED-BRUISE** (the mark is recognizable to those who know it) | Have the mark excised and the wound ritually cauterized. |
| 14 | Your blood has thickened and darkened; fresh cuts ooze like tar. | **TAR-BLOOD** (bleed-out is slower, but healers find you unsettling to treat) | Let a confessor bleed you at dawn for a week. |
| 15 | Small cuts close before the eyes of anyone watching. | **MENDS-FAST** (you cannot convincingly show a wound) | Abstain from all healing — mundane or magical — for a full month. |
| 16 | Your shadow lags a half-second behind your movement. | **LAGGING-SHADOW** (noticeable to the observant) | Stand a full night vigil under open moonlight without moving. |
| 21 | Your teeth have shifted; the canines are longer, and meet wrong. | **WOLF-MOUTH** (speech is subtly altered; meat is easier) | Have a blacksmith file the teeth back and swallow the filings in holy wine. |
| 22 | Your hair has begun to fall out in patches and regrow white. | **PATCHWORK** (hard to disguise; draws stares) | Make a pilgrimage to a healing spring and bathe seven times. |
| 23 | Your wounds heal *wrong* — flesh knitting smooth and hairless where it should scar. | **SMOOTH-SCAR** (your body forgets its history) | Reopen the wounds deliberately and let them scar naturally. |
| 24 | You no longer sweat, no matter the heat; your skin runs dry. | **DRYSKIN** (you overheat in exertion; you smell of dust) | Sit in a sweat-lodge for a day and a night until the sweat returns. |
| 25 | Your fingernails have thickened and darkened to near-claws. | **CLAWING** (fine manipulation is harder; −1 to delicate tasks) | Trim them to the quick and anoint the beds with salt-water. |
| 26 | Your reflection in still water is a half-beat slow to move. | **MIRROR-LAG** (only in still water; a nervous tell) | Pour out a full wineskin of clean water at a crossroads at dusk. |

##### T3 (D10) — the Warped tier

The change is unmistakable, hard to hide, and begins to *cost* you mechanically. You are no longer fully what you were.

| D66 | Immediate effect (visible change) | Long-term tag | Atonement cost |
| --- | --- | --- | --- |
| 31 | A borrowed hunger: you must eat raw meat weekly or take a harm. | **HUNGER** (weekly raw-meat requirement or −1 attribute) | A three-day fast under a confessor's watch. |
| 32 | Your eyes have gone the color of spoiled milk; you see best in the dark. | **NIGHT-EYES** (+1 sight in darkness; −1 in bright light) | Stare into a noon sun in a rite of reclaiming the day. |
| 33 | Your bones ache and shift; you are an inch taller, and jointed wrong. | **RESHAPEN** (armor must be refit; you move with an alien gait) | Submit to a bone-setting ritual by a guild surgeon-priest. |
| 34 | Your blood, spilled, moves on its own for a moment before it stills. | **LIVING-BLOOD** (spilled blood seeks its source; unsettling to foes and allies) | Bleed into running water and let it carry the taint away. |
| 35 | You have stopped aging — frozen at the moment of the stain. | **UNAGING** (you will outlive those you love; a slow curse) | None known; the change is fixed. (Counts toward tier-5 inevitability.) |
| 36 | Your pulse has slowed to a thrum; you breathe half as often. | **SLOW-PULSE** (feign death easily; hard to rouse from sleep) | Undergo a symbolic deathwatch and be "reborn" at dawn. |
| 41 | A second row of teeth is emerging behind the first. | **DOUBLE-TEETH** (your bite is a weapon; your speech is a horror) | Have them pulled one by one over a season, with no healing between. |
| 42 | Your skin has taken on the texture and grey hue of old parchment. | **PARCHMENT-SKIN** (cuts tear deep; fire is your terror) | Be wrapped in fresh linen anointed with chrism for a full day. |
| 43 | You no longer cast a reflection in *any* surface, only a smear. | **REFLECTIONLESS** (mirrors show nothing where you stand) | Catch your reflection in a silvered mirror and *name* it back. |
| 44 | Small vermin — flies, rats — are drawn to you and will not flee. | **VERMIN-Drawn** (−1 to stealth in infested places; a creeping tell) | Spend a night in a sealed room with the vermin and do not flinch. |
| 45 | A wound you took long ago reopens and will not close; it weeps black. | **WEEPING-WOUND** (constant low pain; the wound is a mouth) | Find the one who dealt the wound and forgive them, truly. |
| 46 | Your hands have begun to move on their own when you sleep — gestures, signs. | **SOMNAMBUL-HANDS** (sleep is no longer safe; you wake to strangeness) | Bind your hands each night for a month and a day. |

##### T4 (D12) — the Lost tier (on the brink)

The change is public and *active* — it acts without your will. The next milestone (or refusal to climb down) is tier 5: you are gone.

| D66 | Immediate effect (visible change) | Long-term tag | Atonement cost |
| --- | --- | --- | --- |
| 51 | Your shadow has detached. It acts on its own — whispering, pointing — and obeys the GM during scenes you aren't watching. | **SHADOW-TWIN** (a second agent that is you, but isn't) | Track and bind the shadow in a set-piece rite — a full session. |
| 52 | Your reflection has begun moving when you are still, and smiling when you aren't. | **SMILING-REFLECTION** (it knows things; it may betray you) | Trap the reflection in a silvered mirror and seal it in lead. |
| 53 | Your body no longer casts warmth; you freeze the air around you. Frost rims your clothes. | **HEART-WINTER** (allies take harm from prolonged contact; plants wither near you) | Walk into a great fire and choose to stay until the warmth returns or you do not. |
| 54 | The dead recognize you. Crows speak your name; stray dogs bow. | **DEATH-KIN** (the dead and beasts treat you as one of theirs; the living grow uneasy) | Spend a wake and a vigil in a crypt and refuse the dead's welcome. |
| 55 | Your wounds close by *pulling in* nearby flesh — a fly, a mouse, a hand on your skin. | **FLESH-EATER** (you heal only by consuming living things) | Starve a wound open for a week and let it heal by nothing but your own will. |
| 56 | You have a second heartbeat — slower, deeper, somewhere behind the first. | **TWIN-PULSE** (something is growing in you; it is patient) | Surgically locate and destroy the second heart with a blessed blade. |
| 61 | Your skin splits along old scars and something pale shows beneath, just for a moment. | **SOMETHING-BENEATH** (you are a shell over a tenant) | Confront what is beneath, in a rite of naming and refusal. |
| 62 | Your voice has layered: two tones now, one yours, one not, speaking in unison. | **DOUBLE-VOICE** (your words carry twice their weight; the second voice lies) | Take a vow of total silence for a season until only one voice remains. |
| 63 | Your eyes no longer blink unless you will them to; they have gone dry and bright. | **UNBLINKING** (a predator's stare; animals flee; men go quiet) | Weep a true tear — for something real — and bathe the eyes in it. |
| 64 | You bleed black and your blood *moves toward* the wounded of others, offering itself. | **BLACK-MERCY** (your blood wants to enter others; a contagion and a gift) | Let yourself be bled dry and transfused with the clean blood of another. |
| **65** | **Un-manning — the flesh remakes itself.** You undergo a permanent, visible transformation: a limb lengthens wrong, your face rearranges, you become something those who knew you cannot name. The GM and player agree the shape. You remain *you*, but no longer human-shaped. | **REMADE** (permanent; cannot be hidden; the body is no longer your original) | A great working: a saint's intercession, a god's direct touch, or a quest to find the *original* flesh (a season-long arc). Failure to complete it confirms the change. |
| **66** | **Un-manning — the tenant wakes.** The thing beneath the skin takes a turn at the wheel: for a scene, *you are not the one driving.* The player surrenders control to the GM for that scene; the body does something the character would never do. When you return, you remember it all. This is the warning shot for tier 5. | **TENANT-AWAKE** (it can happen again; the GM may invoke it under defined triggers) | Bind the tenant in a set-piece rite spanning a full session and a sacrifice the player chooses. A partial binding holds it; a failed binding advances you to tier 5. |

*Tier 5 (Gone) is not a table roll — it is the resolution of the ladder. The character becomes what they hunted, ascends as something inhuman, or breaks beyond repair, and leaves play as the genre dictates. By the time a PC reaches tier 5, the tells have made the approach unmistakable (§6); the player chose the final stain.*

*Other families use the same D66 architecture with re-skinned rows: **Mind** (obsessions → compulsions → lost memories → a second self), **Soul** (estrangement → failed prayers → barred from holy ground → the divine turns away), **Shadow** (the shadow lags → the shadow whispers → the shadow acts → you become the shadow), **Alien** (a wrongness → an adaptation → a symbiont → you are no longer the host). The 65/66 rows at each tier in every family are the transformation events — the genre's signature ruin.*

#### The atonement procedure (stepping the die down)

Atonement is the rope ladder back — the only way to reduce the Corruption die. Run it as five numbered steps:

1. **When it can be attempted.** Atonement can be attempted whenever the character is at **tier 1 or higher** and the GM agrees an atonement opportunity exists in the fiction (a shrine to reach, a confessor to find, a relic to burn). It is never automatic — the opportunity must be *present*, and the GM is the arbiter of when one is.
2. **What it costs.** Atonement is a **quest or ritual**, not a rest. It costs fiction: a pilgrimage (a journey), a confession (a vulnerability), a burned grimoire (a sacrifice of power), a vigil (time and risk). The cost is set by the milestone tag's *atonement cost* column (above) or, for a generic descent, by the table below. It must cost something real — time, risk, or a story beat — never nothing.
3. **The effect.** A completed atonement **steps the Corruption die down one tier** (D12→D10→D8→D6→Clean). The doom ladder recedes one rung. The character is less stained than they were.
4. **The limit.** Atonement may be performed **at most once per tier** per character. You cannot farm redemption between castings: having atoned from T4→T3, you cannot atone again until you have climbed back to at least T4. The GM gates *whether* an opportunity exists; the once-per-tier rule gates *how often*.
5. **Whether tags persist.** **Yes — tags persist.** Atonement steps the *die*, not the *tags*. The HUNGER tag, the SHADOW-TWIN, the SMOOTH-SCAR: these are permanent marks of the fall and remain after the die steps down. This is deliberate: it keeps the spiral from being trivially reversible, gives the player a reason to climb slowly (fewer tags), and means even a redeemed character carries the *history* of what they were. (A *separate*, harder rite — a "purification" — may remove a single tag at the GM's discretion, but it is not atonement and is rarer still.)

**Generic atonement costs by tier** (use when a milestone tag doesn't specify its own):

| Die tier you are atoning *from* | Atonement cost (fiction) |
| --- | --- |
| T1 (D6) → Clean | A small rite: a confession, a donated relic, a day's vigil at a shrine. |
| T2 (D8) → T1 | A pilgrimage to a specific holy site, or a quest to undo one specific harm done while tainted. |
| T3 (D10) → T2 | A season-long undertaking: a sworn vow kept, a debt to the divine paid, a monster of the same taint slain. |
| T4 (D12) → T3 | A major set-piece arc: a quest for a relic of genuine power, a descent to confront the source of the corruption, a sacrifice the player chooses. |

#### Engine fit (why this isn't a parallel system)

A common failure of "corruption" subsystems is that they bolt on a parallel tracker — a separate tally, a separate roll, a separate economy — that lives beside the engine without touching it (`10 §10` subsystem inflation). This module avoids that by routing through primitives the engine already runs:

- The Corruption die **is** P5/P10 — the same step-die logic as food (FL) and Pride (FL), only inverted. No new die type, no new roll procedure.
- The temptation **is** P2 — it refuels the same WP/Faith pool the rest of the game uses. The forbidden power enters the engine's own economy, not a side-economy.
- The milestones **are** P4 — the same typed-D66 architecture as crits and mishaps. No new table grammar.
- The tier tags **are** P8 — they land in the same feature-grammar as weapons and talents.

The result is a subsystem that *feels* like the core loop because it *is* the core loop, inverted and fused — which is the engine's own trick for producing novelty (`12 §12`, `16 §6`). A designer installing this needs no new dice, no new currency, no new resolution mechanic — only the inversion (die grows), the fusion (refuel + milestone table), and the atonement rule (a quest to step back down).

#### The tells (corruption as public fiction)

A Corruption die on a character sheet is necessary but not sufficient — the doom ladder must also be *legible in the fiction* so the table (and the world) can react. Each tier carries a **tell**: a visible, narratable sign that grows more pronounced as the die steps up (see the ladder table above). Tier 1's tell is deniable (a chill, a bad dream); tier 4's is unmistakable (the shadow moves on its own). Tells matter for three reasons:

1. **They make the spiral shared drama.** Other PCs can see the stained character changing and must decide whether to intervene — confront, report, aid the atonement, or look away. This converts a solo tracker into party fiction.
2. **They create social consequence.** NPCs react to tells — a witch-hunter's Order may investigate its own; a village may shun or fear the tainted; a patron may withdraw support. The corruption thus ripples into the social and faction layers.
3. **They make tier 5 a visible approach, not a surprise.** A tier-4 character *looks* nearly lost; no one at the table can claim the end came without warning. This is the antidote to the "un-manning cliff" failure mode (§6).

Tells are fiction, not mechanics — they cost no dice and add no rolls. They are the GM's and table's job to voice. A milestone table entry can specify a tell (the Flesh-family UNSETTLING tag carries one), but the tier itself should always carry *some* narratable sign by default.

#### Why inversion changes the math (a warning)

A normal resource die (P5) steps *down* — you have a long way to fall (D12→D6) and depletion is the slow crisis. The Corruption die steps *up* — and there are only four steps to the top (D6→D8→D10→D12→Lost). This is `18 §7`'s "inverting without re-balancing" anti-pattern in miniature: an inverted mechanic hits its climax *faster* than its parent hits empty. The cheapest-use range (1–2 = no step) and the benefit-only trigger are the brakes that keep the spiral at campaign cadence. Tighten either and the spiral accelerates dramatically — see Dials and Failure modes.

## 3. The pressure loop

- **Pressure:** the forbidden power is *useful* — it refuels your metacurrency (P2), boosts a roll, or buys off a consequence you couldn't otherwise escape. The pressure is the *need* the power answers (a fight going badly, a resource depleted, a failure that costs everything). Crucially, the need must be *real and recurring* — if legitimate options are always sufficient, the spiral never opens (see Failure modes).
- **Decision:** *do I use the forbidden power now — refueling myself, winning this moment — and roll the Corruption die? Or do I pay the legitimate cost (harm, retreat, accept the failure) and stay clean?* This is the engine's signature push-and-pay, flipped: the push *pays you*, the cost comes later. The deferral is the trap — the cost is probabilistic and future, the benefit is certain and now.
- **Consequence:** the Corruption die may step up; at milestones, a permanent tag lands; the character inches up the doom ladder. Every tier makes the *next* temptation harder to resist for two reasons: (a) the character has more sunk cost invested in the forbidden power, and (b) the higher die *pays more* on a refuel — a D12 casting that refuels 12 WP is far harder to foreswear than a D6 refueling 6. The spiral is self-reinforcing by construction.
- **State change:** the character's standing on the doom ladder changes — a visible, fiction-loaded state, not a hidden tally. Each tier also adds a *tell* (a fiction tag others can notice), so the party and the world begin to react to the stained character. At tier 5, the character leaves play.
- **Loop shape:** **need → yield (refuel) → stain → milestone → climb.** Runs at casting-cadence (faster than an org lifecycle; slower than a single roll). The spiral is *slow* by design — see Failure modes for the pacing trap. The loop closes only via atonement (stepping back down) or abandonment (tier 5).

## 4. Dials

| Dial | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Die ladder** | D6→D8→D10→D12 (5 tiers) | D6→D8→D10 (4 tiers, tighter) | Slow burn vs fast ruin |
| **Step-up trigger** | 3+ on the Corruption die | 4+ (rarer) | Stains often vs stains sting |
| **Cheapest-use range** | 1–2 = no step (power came cheap) | Always steps (no cheap outs) | Forgiving vs inexorable |
| **What triggers a roll** | Only *gaining a benefit* from forbidden power | *Any* use, including failed castings | Temptation-driven vs contact-driven |
| **The temptation (P2)** | Forbidden use refuels metacurrency (WP/Faith) by the die's face value | Forbidden use grants +1 die to the roll or a free push | Fuel-loop vs peak-power |
| **Tier effects** | Cosmetic at T1, mechanical tags at T2–3, climax at T4–5 | Mechanical from T1 (sterner) | Slow dread vs immediate bite |
| **Milestone table families** | 3–5 typed families (physical/mental/social/spiritual/alien) | 1 master table | Rich flavor vs simple |
| **Atonement (step down)** | A **quest** or ritual steps the die down one tier | Cannot step down — only forward | Redeemable vs one-way |
| **Atonement availability** | Always available if you can secure the quest | Once per tier, GM-gated | Hopeful vs tragic |
| **Tier 5 resolution** | Character Lost (becomes NPC / monster / departs) | Player may sacrifice the power source to reset to T3 | Hard floor vs costly reprieve |
| **Corruption visibility** | Die shown on sheet; tier is public fiction | Hidden tracker revealed only at milestones | Tension-on-display vs slow reveal |

**Calibration guidance:** start with the 5-tier ladder (D6→D12), 3+ step trigger, 1–2 cheapest-use, benefit-only triggers, metacurrency refuel temptation, cosmetic-then-mechanical tiers, 3–5 milestone families, **quest-based atonement** (the redeemable dial). This is the classic doom spiral with a rope ladder back. Reserve the one-way (irredeemable) dial for grimdark genres where the slide *is* the tragedy.

## 5. Integration points

- **Hooks into the power layer (`05`):** this is the **cost the power layer needs.** Any forbidden spell, pact, alien implant, or psychic overchannel in `05` routes its cost through this subsystem instead of (or in addition to) the standard mana/mishap cost. The power layer defines *what counts as forbidden*; this module defines *what using it costs over time.* Without this, forbidden options are either free (broken) or flat-penalized (avoided).
- **Hooks into harm (`04`):** the Corruption die is a **parallel harm track.** Where `04` tracks wounds to the body, this tracks wounds to the *self.* A Corruption milestone can also deal a real condition (a Warped-tier mental corruption may impose a permanent phobia tag) — the two tracks intersect at the fiction but do not share a pool.
- **Hooks into metacurrency (`00 §7`):** the temptation fuse. Forbidden use refuels WP/Faith (P2). This is what makes the spiral *tempting* rather than punishing — the player feels the power working, *now*, and the cost is deferred and probabilistic. Wire the refuel amount to the Corruption die's face so the *riskier* (higher) die also *pays more* — a self-reinforcing trap.
- **Hooks into talents/identity (`01 §5`, `08 §6`):** Corruption milestones land **tags** (P8) on the character — permanent features (a tell, a weakness, a forbidden knack). These interact with the talent/feature grammar already in the game. At high tiers, corruption tags can *replace* benign talents (the character's identity is being overwritten).
- **Requires:** a defined list of what counts as *forbidden* in the genre; a Corruption die per qualifying PC; the milestone table(s); an atonement rule if redemption is in scope.
- **Replaces / extends:** any flat "corruption point" tally — replaces it with a step-die that inherits P5's proven curve and P10's escalation logic.
- **Cross-refs:** `05 §7` (magic mishaps — a sibling one-shot cost; this is the *chronic* cost), `04 §5` (typed D66, here as Corruption Milestones), `18 §6` Worked 4 (the Doom dial this extends), `16` P5/P10/P4/P2.

## 6. Failure modes & edge cases

- **"Players never use the forbidden power" (the wasted-subsystem failure).** If the temptation isn't real, players rationally stay clean and the whole module never triggers — the designer built a spiral no one enters. **Fix:** the *refuel* (P2) must be substantial and must answer a *real* need — make legitimate alternatives scarce or costly in the genre's pressure loops (a fight you can't win cleanly; a metacurrency pool that runs dry). The corruption must be the *easy* answer to a *hard* problem, not a marginal option. Tune the refuel amount up if the power goes unused.
- **"Players spiral to doom too fast" (the pacing failure).** An inverted depletion mechanic (Operator 2) hits its climax *faster* than a normal one depletes — `18 §7`'s anti-pattern warns of this. If the die steps up on every use, a player can hit tier 5 in a session. **Fix:** (a) widen the cheapest-use range (1–2 = no step), so ~33% of uses are "free" and the climb is probabilistic; (b) gate step-ups to *beneficial* uses only, not every casting; (c) raise the step trigger to 4+ for slower burn; (d) make atonement *available* — the rope ladder back. Recompute the breakpoints (`13 §4`) so a typical character sees tier 3–4 across a *campaign arc*, not an evening.
- **The atonement exploit.** If stepping the die back down is too easy, players farm redemption between uses and the spiral never advances — the cost is vaporized. **Fix:** atonement is a **quest or ritual**, not a rest — it costs fiction (time, risk, a story beat), never nothing. Gate it to once per tier and make the GM the arbiter of when an atonement opportunity even *exists* in the fiction.
- **Milestone-table fatigue.** If every minor casting prompts a D66 roll and a tag, the table becomes bookkeeping (`19` FE2). **Fix:** the milestone table fires only on **tier transitions**, not every use. Day-to-day corruption is just the die stepping; the table is the *climax* beat, like a critical injury — rare and loaded.
- **The un-manning cliff.** Tier 5 removing a character from play can feel punitive if it arrives without warning. **Fix:** the doom ladder is **public fiction** — the player can see tier 4 (D12) coming and *chooses* the final stain. Tier 5 is always a player decision, never a surprise ambush. Offer the "sacrifice the power source to reset to T3" dial for genres where the floor should be costly, not terminal.
- **Inconsistent cost model.** `18 §5` warns against mixing cost types. If the game's master cost is *harm* and corruption costs *metacurrency* (or vice versa), the subsystem feels incoherent. **Fix:** align corruption's cost type with the game's master cost model (`12` degree-of-freedom 1), or justify the exception explicitly. In most dark-fantasy calibrations corruption is its *own* cost type — which is fine, because it is the *dedicated* cost for the forbidden-power layer.
- **The lone-edgelord monopoly.** If only one PC has forbidden power, the corruption spiral is a solo mini-game the table watches. **Fix:** either give every PC a corruption vector (different sources — one's a pact, one's an implant, one's a bloodline), or wire corruption milestones to *party* fiction (your stain marks an ally; your transformation endangers the group) so the spiral is shared drama, not a sidebar.

## 7. Validation notes

- **Math (`13 §3`/`§4`):** with a 3+ step trigger and 1–2 cheapest-use, the expected steps-to-climb from Clean to tier 5 is roughly 4–5 *beneficial uses per tier* × 5 tiers ≈ 20–25 beneficial uses — a campaign's worth, not a session's. If playtesting shows faster spirals, widen the cheapest-use range or raise the trigger to 4+. Recompute after any dial change; inverted mechanics are sensitive to trigger width (`18 §7`).
- **Exploits (`13 §5`):** the atonement-farm exploit (above) is the primary one; gated by quest-cost and once-per-tier. A secondary exploit: "use the forbidden power only when the Corruption die is already D12" (no further step risk) — **fix** by ruling that a D12 rolling 3+ is the *milestone* itself, so there is no safe ceiling.
- **Synergy (`13 §6`):** the subsystem *should* synergize with the power layer (`05`) — it is the cost that makes forbidden options balanced. Check that forbidden power is *not* also gated by a separate heavy cost (double-charging makes it unused; see failure mode 1).
- **Felt experience (`19`):** the doom ladder must be **visible** (public die + tier fiction + tells) to produce dread rather than anxiety — `19` C5 agency ledger: the player must see the slide to *choose* it, and the table must see it to react to it. The temptation must **pay well** enough to be genuinely tempting (FE1 false choice avoided) — a refuel too small to matter is the same as no subsystem. Tier 5 must be a **player-chosen** outcome, never a GM ambush (FE5 fairness); the tells guarantee the approach is visible. The milestone table carries the *memorable-specific* psychology of P4 — "your reflection has been smiling when you aren't" is the point, not "−1 to a stat." The self-reinforcing trap (higher die pays more) is *intended* felt experience: the player should feel the power getting harder to forsake as they fall, which is the dramatic engine of the genre.
- **Table load (`13 §7`):** one extra die roll on each *beneficial* forbidden use (light — same cadence as a damage roll). The milestone D66 fires only on tier transitions (~4–5 times across a campaign per character), so the heavy table is rare. The Corruption die itself is a single step-die on the sheet — less bookkeeping than a point tally. Net: low ongoing load, occasional loaded beats. Acceptable.
- **Pipeline verdict (`13 §8`):** passes intent (clear power-at-a-cost drama), math (tunable spiral length, ~20–25 beneficial uses to tier 5), exploit (atonement gated; no safe ceiling at D12), synergy (feeds the power layer rather than duplicating its cost), table (one extra roll per beneficial use; milestone table only on tier transitions — acceptable load). Ship with the redeemable dial as default; the one-way dial is a genre variant, not the baseline.

## 8. Worked genre example — Witch-hunting dark fantasy

**The setting:** A grim theocracy where the Inquisition hunts witches — but the only reliable weapon against the dark is the dark itself. The PCs are inquisitors licensed to use the forbidden arts (maleficia) in the hunt. Every casting stains them; the Order's oldest members are no longer entirely human. The dramatic question is not *whether* the PCs will fall, but *how far* and *whether they can come back.*

**What counts as forbidden:** casting any maleficia spell from `05` (the inquisitor's necessary evil), or channeling a captured witch's power through yourself. Legitimate alternatives (steel, prayer, fire) exist but are often insufficient against true horrors — which is why the temptation is real.

**Dials set:** 5-tier ladder (D6→D8→D10→D12→Lost); 3+ step trigger, 1–2 cheapest-use; benefit-only triggers; **the temptation = casting maleficia refuels Willpower (WP) by the Corruption die's face** (a D8 casting that rolls an 8 refuels 8 WP — a desperate inquisitor's lifeline); cosmetic-then-mechanical tiers; **4 milestone families** (Flesh / Mind / Soul / Shadow); **quest-based atonement** (a pilgrimage, a confession, a burned grimoire) stepping the die down one tier, once per tier.

**In use (excerpt):**

- **The fight going badly.** Inquisitor Marta is cornered by a coven-bred horror; her steel is useless and she's at 2 WP. She invokes *Tongue-of-Ash* (a maleficia), succeeds, and **gains the benefit** — escape + the spell refuels her WP by her Corruption die's face. She is at **tier 1 (D6)**, rolls it: a **5** (3+, steps up). She is now **tier 2 (D8), Marked → Tainted.** She rolls the Flesh milestone table (§2c): a **23** — her wounds now heal wrong, and she carries the **SMOOTH-SCAR** tag. She escapes, richer in WP, poorer in self. The other players *see* the die step up on the sheet — the dread is public.
- **The refuel making it worse.** Later, desperate again and now at tier 3 (D10), Marta casts: the D10 refuels **10 WP** — a fortune. The player feels the trap: the more stained she is, the more the power *pays*, and the harder it is to stop. She rolls the die: **3+**, stepping to tier 4 (D12). The player *sees the cliff.*
- **Three sessions later.** Marta is **tier 3 again** — between sessions she undertook a **pilgrimage** (atonement quest, a session of play, real fiction cost) and stepped back from tier 4 to tier 3. The spiral breathes. But the SMOOTH-SCAR tag persists (atonement steps the *die*, not the tags — another reason to climb slowly).
- **The campaign's end.** Marta reaches **tier 4 (D12)** again, with no time for another pilgrimage. The final horror can only be stopped by a great working. The player **chooses** the last stain: rolls the D12, gets **3+**, hits tier 5. She becomes the thing that stops the horror — and then must be stopped in turn. The player rolls a new inquisitor. The Order continues.

**Why this works in dark fantasy:** the *refuel* temptation maps exactly onto the genre's core tension — the inquisitor *needs* the dark to fight the dark, and the power genuinely works (the WP refuel is real, the escape is real). The doom ladder makes the slide *legible* — the player always knows how close to the edge they are, and every tier transition is a story beat (P4's specific-and-memorable psychology). Atonement as pilgrimage fits the theocratic setting and keeps the spiral from feeling like a trap. Tier 5 as "become the monster" delivers the genre's signature tragedy: the hunter who becomes the hunted. The self-reinforcing trap (a higher die pays more WP, so the most-corrupted inquisitor is also the most desperate to keep casting) is *the* dramatic engine of witch-hunter fiction — the veteran who has fallen too far to climb back, and knows it.

**Calibration note for this genre:** dark fantasy wants the redeemable dial *on* (pilgrimages exist) but atonement to be *scarce* (a pilgrimage is a session of play, and the GM need not always offer one). The result is a spiral that breathes — advances and retreats — rather than a one-way slide, which matches the genre's moral texture (hope and ruin in tension, ruin usually winning). For a *grimdark* variant where the slide is inexorable, switch atonement off entirely: the spiral becomes a countdown, and tier 5 becomes the campaign's planned endpoint for every inquisitor.

**Re-skin for your genre:**
- **Cosmic horror (alien tech / psychic overexposure):** forbidden = alien artifacts or overchanneling psi; tiers = biological mutation / sanity erosion; tier 5 = ghoul-hood or ego-death; atonement = rare suppressants that are themselves dwindling (P5, non-inverted).
- **Cyberpunk (black ICE / untested cyberware):** forbidden = unregulated implants or daemon-summoning; tiers = cyber-psychosis / humanity loss; tier 5 = flatline or goon-hood; atonement = expensive therapy / firmware rollback.
- **Superhero (dark bargain / radioactive origin):** forbidden = the power that also poisons you; tiers = the power mutating you; tier 5 = villain-turn; atonement = the loved one who pulls you back (once).
- **Necromancy / death magic:** forbidden = animating the dead; tiers = the dead *recognizing* you, then *following* you, then *replacing* you; tier 5 = you join your own court of the unburied.
