<!-- markdownlint-disable MD013 -->

# Design Philosophy — Pressure, Loops, Lethality, Layering

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the conceptual backbone. Every other reference file's "Design intent" section and the validation pipeline in `13-balance-and-synergy.md` draw from this file. If a rule cannot be defended against the principles here, it does not belong in a YZE-family game.

## Contents

1. Source provenance
2. Abstraction target
3. Core design identity (the engine's thesis)
4. The pressure economy
5. The five primary gameplay loops
6. "Nothing Is for Free" — and the cost-of-safety axiom
7. Lethality and attrition as feature, not bug
8. Tone and the authenticity lens
9. The general / situational / optional layering principle
10. Warning signs (inherited anti-patterns, generalized)
11. Divergence rows (FL vs West)
12. Dials and instantiation recipe
13. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `skills/forbidden-lands-design/references/system-design-map.md:16-30` — Core Design Identity, "ties ambition to exposure," the five tensions.
- `skills/forbidden-lands-design/references/system-design-map.md:32-130` — Primary Gameplay Loops (Expedition/Conflict/Recovery/Willpower/Base), Pressure Economy, Chapter Map.
- `skills/forbidden-lands-design/references/system-design-map.md:310-351` — Proposal Integration Method, **Warning Signs** (subsystem inflation, silent talent invalidation, false realism, vague enforcement, misleading survivability).
- `02-gamemasters-guide/02-the-gamemaster.md:25-67` — the 7 Principles of the Game.
- `02-gamemasters-guide/02-the-gamemaster.md:131` — "fail forward."
- `skills/forbidden-lands-design/references/realism-audit-synergy-and-change-scenarios.md:26-72` — realism vs playability, the practical realism test, the synergy-risk catalog.

**Tales of the Old West 2E (West):**
- `skills/western-rpg-design/SKILL.md:31-52` — the four-layer design method (rule loop, design purpose, integration map, table behavior).
- `skills/western-rpg-design/SKILL.md:78-85` — Standards For Good Design.
- `skills/western-rpg-design/SKILL.md:122-128` — Proposal Review Checklist.
- `skills/western-writing/SKILL.md:402-465` — the 12 non-negotiable prose rules (the parallel *voice* philosophy — the prose-level expression of the same pressure-toward-authenticity stance).
- `02-the-1870s/00-introduction.md:5,13` — "built from the cold facts of the ledger, not the painted backdrops of a theater"; "The land does not care. That indifference is the story."
- `02-the-1870s/12-availability.md:5` — "the wrong-decade object is the most reliable way to lose the West"; "the bias should always be toward *not yet*."

## Abstraction target

Abstract the **design philosophy** that makes YZE *work* — the reason both books, despite different genres, feel like the same engine. The thesis: **the engine ties ambition to exposure.** Every loop turns a resource (time, body, gear, metacurrency, safety) into pressure, and pressure into decision. The deliverable is the **pressure-economy** model, the **five core loops** (Expedition / Conflict / Recovery / Metacurrency / Base) restated genre-neutrally, the **cost-of-safety axiom**, the **lethality-as-feature** stance, the **authenticity lens**, the **general/situational/optional layering principle**, and — most critically — the **anti-pattern catalog** that the validation pipeline in `13-balance-and-synergy.md` checks against.

Apply the Abstraction Ladder to: identity, pressure, loops, axioms, lethality, tone, layering, anti-patterns.

## 3. Core design identity (the engine's thesis)

**The thesis (FL, stated outright):** "Forbidden Lands works because it ties ambition to exposure." `system-design-map.md:18`.

Abstracted, genre-neutrally: **the engine ties ambition to exposure.** Characters are not protected heroes with narrative armor. They are hungry, driven agents operating in a landscape that exacts a price for every step, every swing, every claim of safety. The design identity rests on five tensions, all inherited from FL `system-design-map.md:24-28` and present (if differently costumed) in West:

- **risk versus reward** — the larger the prize, the larger the bet.
- **speed versus safety** — moving fast exposes you; hunkering costs time.
- **power versus mishap** — leverage (magic, gunfire, gear) is unstable; it backfires on the user.
- **scarcity versus preparation** — everything finite can be exhausted; preparedness is itself a resource.
- **survivability versus long-term cost** — you can live through this, but what does living cost?

**The governing warning (FL):** "Any new rule that ignores those tensions may function locally while still breaking the larger game." `system-design-map.md:30`. This is the single sentence every other file's design intent inherits.

**FL — frontier survival:** The expression is *exposure to the land itself.* The Blood Mist has lifted and the adventurers are "hungry, driven opportunists moving through a hard landscape where travel, wounds, scarcity, weather, and magic all exact a price" `system-design-map.md:20`. Ambition = loot and legend; exposure = cold, hunger, the hex, the monster. The costumed currency is *the body and the supply.*

**West — Old West grit:** The expression is *exposure to the indifference of a real country.* "The American West of the 1870s was a country built on iron, horse sweat, and staggering distance" `02-the-1870s/00-introduction.md:3`. Ambition = pay, a name, a stake, survival past the next winter; exposure = the gun, the distance, the fever, the debt, the law. The thesis is rendered in a single line: "The land does not care. That indifference is the story." `02-the-1870s/00-introduction.md:13`. The costumed currency is *grit and belief (Faith).*

**Generic abstraction:** State the thesis once for any new game — *what does ambition look like here, and what does exposure look like here?* The two answers name the game's currency and its adversary. FL's adversary is the landscape; West's adversary is the country's indifference. Both answers must be **physical and credible**, not abstract — a thesis the player can feel as pressure, not read as flavor.

## 4. The pressure economy

**FL's own framing:** "The game is built on layered pressure rather than single-axis balance." `system-design-map.md:113`. There is no single hit-point bar to drain; there are *many* pressure sources acting simultaneously, and a rule is never evaluated in isolation. `system-design-map.md:129-130`.

**The engine's pressure sources (generalized from FL `system-design-map.md:117-125` + the West design space `SKILL.md:54-66`):**

| Pressure source | FL expression | West expression | Generic (engine-level) |
| --- | --- | --- | --- |
| **Time** | Quarter Day spent on travel/actions | Shift spent on the trail / the job | The unit that travel, recovery, and scarcity are measured in |
| **Body** | Attribute scores reduced by 💀 damage | Attribute reduced by Trouble/wounds | The live dice pool that is also your health |
| **Gear** | Gear dice degrading on 💀; resource dice | Consumables as Resource Dice (Optional) | Finite equipment that wears toward broken/empty |
| **Metacurrency** | Willpower (cap 10, harm-refueled) | Faith (cap 10, 4/scenario, action-refueled) | The capped pool that converts risk into future agency |
| **Safety** | Scarcity of food/water/shelter/expert tools | Scarcity of water, ammunition, a warm bed | The absence of a safe baseline that other systems assume |
| **Overreach** | Mishaps from pushing too hard / bad magic | Desperate Trouble tables | The tax for grabbing more than your position allows |

**The resource-at-risk model (the engine's core abstraction):** Every meaningful interaction follows the same four-beat shape — **pressure → decision → consequence → state change.**

1. **Pressure:** a resource is put at risk (a Quarter Day is spent, dice are rolled with banes latent, a pool sits near its cap, a long march is begun without supplies).
2. **Decision:** the player (or GM) chooses how to respond — push or accept, fight or flee, press on or make camp, spend the metacurrency or hoard it.
3. **Consequence:** the choice resolves into a mechanical outcome — damage, degradation, a Trouble escalation, a depleted die, a gained/lost WP or Faith.
4. **State change:** a durable change lands on the character sheet — lower attribute, broken gear, a condition, a new pressure to carry forward.

If an interaction does not run all four beats, it is **decorative** — it produces narration without stakes. The engine treats narration-without-stakes as a bug: it floods the economy (every trivial roll generates metacurrency in FL) and flattens the drama. See `00-engine-core.md:205` ("don't roll too often").

**The evaluation rule (FL, verbatim sense):** When judging any rule, "Ask which pressure it relieves, which pressure it adds, and whether it accidentally cancels a core source of tension elsewhere." `system-design-map.md:129-130`. A rule that *relieves* pressure must relieve the *right* pressure and *cost* something to do it; a rule that *adds* pressure must add pressure the game actually wants. **Layer:** General — the resource-at-risk model is the engine's analytical spine, not an optional toggle.

## 5. The five primary gameplay loops

FL names five loops `system-design-map.md:32-109`. Both games run all five; the genres costume them differently. Restated genre-neutrally:

### 1. The Expedition loop

**Sequence (FL `system-design-map.md:36-44`):** prepare → travel → spend resources → face encounters and environmental pressure → reach site → risk injury or gain treasure → retreat, recover, rearm.

**Generic:** a journey through hostile space where the *act of getting there* is itself a resource drain and a series of exposure events. The destination is the prize; the road is the tax.

**Design purpose (FL `system-design-map.md:46-49`):** survival pressure makes exploration meaningful; logistics and risk assessment are *part of play, not prep outside play.* FL = hex-crawl with Quarter Days and foraging; West = the trail drive, the ride, the march, measured in Shifts and water. The loop must not be skippable for free — cheap travel hollows out the pressure spine (see Warning §10e).

### 2. The Conflict loop

**Sequence (FL `system-design-map.md:54-60`):** initiative → action choice → roll → push or accept → immediate consequence → injury, positioning, or loss of tempo.

**Generic:** a violent or high-stakes contest where each exchange costs tempo, position, or body. Combat is dangerous enough that *choosing it* is itself a decision.

**Design purpose (FL `system-design-map.md:62-65`):** "combat is dangerous enough that choosing it matters; tactical decisions are simple but costly." West's Trouble system (Safe/Risky/Desperate exposure) `00-engine-core.md:99-101` is the same stance from the position-advantage angle. The loop rewards avoidance, flanking, and escalation — never routine violence.

### 3. The Recovery loop

**Sequence (FL `system-design-map.md:70-76`):** become damaged, Broken, or conditioned → survive the immediate crisis → rest, heal, use talents or magic → recover partially or completely → carry lasting consequences where rules specify.

**Generic:** getting hurt is not the end of the beat — *surviving the hurt* is its own loop, and surviving has a price.

**Design purpose (FL `system-design-map.md:78-81`):** "the game does not only ask whether you survive the fight. It asks what surviving costs." Recovery consumes the *time* pressure source; anything that compresses recovery too cheaply (Care, healing magic) is a high-impact rule even when it looks small. See `realism-audit...md:346-361` (Care halves recovery time — one of the strongest tempo effects). Cross-link: `04-harm-and-consequences.md`.

### 4. The Metacurrency loop

**Sequence (FL `system-design-map.md:86-92`):** attempt difficult action → push → accept risk from banes → gain the metacurrency → spend it on talents, spells, or pressure relief.

**Generic:** a closed loop where **risk refuels agency and agency is spent on bigger risk.** FL: damage-on-push earns WP; spend WP on talents/spells. West: action/success earns Faith; spend Faith on pushing and buying off Trouble.

**Design purpose (FL `system-design-map.md:94-95`):** "desperation feeds power; players are rewarded for risk-taking, but never for free." This loop is the engine's anti-death-spiral — it is what stops attrition from becoming hopeless, because getting hurt *stocks your comeback.* It is also the engine's most fragile coupling: any rule that eases refuel, adds refunds, or permits extra pushes "becomes much more dangerous than it looks in isolation" `realism-audit...md:275-281`. Cross-link: `00-engine-core.md:116-134`, `13-balance-and-synergy.md`.

### 5. The Base loop

**Sequence (FL `system-design-map.md:101-105`):** gather wealth and materials → establish or improve stronghold → gain functions, safety, and status → attract new obligations and vulnerabilities.

**Generic:** long-term success is converted into infrastructure, and infrastructure **trades mobility for rooted value** while *generating new threats.* FL = the Stronghold and its weekly event table `02-the-gamemaster.md:137-179`. West = the ranch, the stake, the claim, the saloon — the rooted investment that draws rustlers, tax collectors, and vendettas.

**Design purpose (FL `system-design-map.md:107-109`):** "long-term success alters campaign shape; security becomes another asset to defend." This is the loop where Principle 5 ("Them That's Got Shall Lose," `02-the-gamemaster.md:53-57`) lands: success does not buy safety, it buys *a bigger target.* The Base loop must never collapse into pure upside — every function gained must arrive with an obligation or vulnerability, or the pressure economy breaks.

**Layer:** all five loops are **General** — a YZE-family game is incomplete without all five operating, though a given genre may weight one or two as primary (FL weights Expedition + Base; West weights Conflict + Recovery). Which loop dominates is a dial — see §12.

## 6. "Nothing Is for Free" — and the cost-of-safety axiom

**The master axiom (FL Principle 4):** "Nothing Is for Free." `02-the-gamemaster.md:47`. "The fact that the players are free to make their own decisions and go wherever they please doesn't mean that they should get whatever they want. The more they want something, the more they should be ready to fight for it." `02-the-gamemaster.md:48-49`.

**The cost-of-safety corollary:** Safety is the most expensive thing in the game. FL: "Hold back on the treasures and rewards. Never allow the adventurers to feel content for more than a second." `02-the-gamemaster.md:51`. West's design space names the same thing directly: "scarcity, survival, and the cost of safety in the frontier" is a mandatory check surface `SKILL.md:65`. The metacurrency itself encodes this — FL's WP refuels from harm, so the *safest* path (never push, never get hurt) is also the path that *starves you of agency.*

**Principle 5 ("Them That's Got Shall Lose"):** The axiom's long-term expression. Acquired wealth/power does not retire you; it *exposes* you. "They will most likely attract greedy stares... Let the player characters fight to keep what they have." `02-the-gamemaster.md:53-56`. The Stronghold is the textbook case: "the stronghold will attract wanderers and fortunehunters... the adventurers will eventually have to fight to defend their stronghold" `02-the-gamemaster.md:56-57`.

**Generic abstraction — the axiom as a design test:** For any proposed rule, ask: *what does this give the character, and what does it cost?* If the answer to the second question is "nothing" or "flavor," the rule violates the axiom. Concretely:
- A talent that grants an edge must cost a slot, a WP, an action, or a tradeoff.
- A gear item that solves a problem must displace a tool, a talent, or stronghold function, or deplete toward broken. FL: "is the item solving a real gap" `system-design-map.md:241`.
- A safe option (safe casting, lossless travel, full healing) must either not exist, be ruinously expensive, or carry a hidden cost that bites later. "Does it introduce safe casting by accident?" `system-design-map.md:206` is the canonical version of this test.

**Layer:** General — the axiom governs all rules. It is not a toggle; violating it is a Warning Sign (§10).

## 7. Lethality and attrition as feature, not bug

**FL's stance (Principle 6, "Death Is Part of the Story"):** "The rules are written so that it's relatively easy to become Broken, but rather difficult for a player character to die. As GM, you should basically never kill a defenseless player character — there are always more interesting ways to use the situation. Yet, sooner or later, player characters will still die. Allow it to happen — the players need to be reminded now and then that their adventurers aren't immortal." `02-the-gamemaster.md:61`.

**The lethality calibration:** The engine is built on a deliberate two-stage model — *Broken is easy, death is hard, but death is real.* This is not a survival-simulator's permadeath, nor a heroic game's plot armor. It is a **threat that makes avoidance a strategy and survival a story.** "That a player character dies is not a failure, it is a part of your shared story." `02-the-gamemaster.md:63`.

**Attrition is the operating mechanism, death is the boundary:** Lethality is felt mostly through *attrition* — the slow accumulation of reduced attributes, conditions, gear wear, depleted resources, and spent metacurrency that makes the *next* encounter more dangerous than the last. The Pressure Economy (§4) is what makes attrition bite. Death is the consequence that arrives when attrition is ignored past the breaking point. West sharpens the attrition edge with infection, fever, and the medical limits of the 1870s — "the 1870s doctor cannot cure diphtheria, scarlet fever, cholera, typhoid, or tuberculosis" `02-the-1870s/12-availability.md:37` — so a wound that is survivable today can still kill next week.

**Generic abstraction:** Lethality is a **dial**, not an on/off. The two calibrated points:
- **FL:** Broken-easy / death-hard, but death real; the GM is told never to kill a *defenseless* PC (use the situation instead) `02-the-gamemaster.md:61`. Attrition is the body and the supply.
- **West:** attrition is grit and circumstance — a gutshot is survivable but the fever is not guaranteed; the medical technology *will not save you.* Lethality is historically bounded, which makes it feel inevitable rather than arbitrary.

**Why this is a feature:** Without the threat of real loss, the Pressure Economy has no teeth — players would simply push until they succeed, never retreat, never spend resources on avoidance. Lethality is what makes "do we fight or do we flee" a real question, what makes recovery matter, what makes the metacurrency loop dramatic rather than mechanical. **Layer:** General (attrition always on); the death/Broken calibration is a dial — see §11, §12. Cross-link: `04-harm-and-consequences.md`.

## 8. Tone and the authenticity lens

Both games share a stance on realism that is more disciplined than "realistic." The engine is **not a simulator** — it "is a harsh adventure game that uses realism selectively to intensify pressure" `realism-audit...md:34-35`. Realism earns its place only when it sharpens a decision; it is a tool, not a goal.

### The authenticity lens (genre-neutral)

Every system — combat, gear, economy, travel, social — should pass a **realism sniff-test without sacrificing playability.** The test, generalized from FL's "practical realism test" `realism-audit...md:64-72` and West's evidence base, asks in order:

1. **What decision does this make sharper?** (If nothing — the realism is decorative weight `realism-audit...md:72`.)
2. **What existing abstraction is it replacing or clarifying?** (Realism that merely duplicates an existing pressure channel with new bookkeeping is bad realism `realism-audit...md:58`.)
3. **What is the new table burden?** (Procedure without decision is stall `realism-audit...md:57`.)
4. **Does it preserve campaign movement, or stall it?**
5. **If it cripples a character, is that honestly labeled — playable, retirement-default, or fatal?** `realism-audit...md:70`.

### Good realism / bad realism (FL's boundary, generalized)

**Good realism** does at least one of `realism-audit...md:39-43`: creates a meaningful choice; reinforces the material reality of the world; gives an existing pressure a cleaner rule hook; makes outcomes more believable without slowing play. FL's own examples: cold *blocking recovery* instead of only dealing damage; critical injuries carrying distinct lasting effects; travel consuming Quarter Days rather than handwaving logistics `realism-audit...md:46-52`.

**Bad realism** does one or more of `realism-audit...md:57-60`: adds procedure without adding decisions; creates "you are technically alive but functionally unusable" states without saying so; duplicates an existing pressure channel with new bookkeeping; relies on GM mercy to remain playable. These map directly onto the Warning Signs in §10 (false realism, misleading survivability, vague enforcement).

### How each game holds the lens

**FL — grim medieval frontier:** authenticity is *material and ecological.* The cold, the hunger, the weight of gear, the rarity of steel — these are the realism hooks. The audit lesson is explicit: "catastrophic injury is more interesting as survivable consequence than as flat instant death, but 'survivable' must not be used dishonestly for states that effectively end active adventuring" `realism-audit...md:79-82`. Survival-with-cost is good; hidden non-playability is bad `realism-audit...md:84-86`.

**West — 1870s historical authenticity:** authenticity is *documentary and evidentiary.* The skill ships a 26-chapter evidence base (`02-the-1870s/`) so that "nothing on the page is from the wrong decade" `western-writing/SKILL.md:48-49`. The governing rule: "The wrong-decade object is the most reliable way to lose the West... The bias should always be toward *not yet*" `02-the-1870s/12-availability.md:5`. The stakes are stated flatly: "It is built from the cold facts of the ledger, not the painted backdrops of a theater" `02-the-1870s/00-introduction.md:5`. West is the *stricter* authenticity point — where FL can invent a monster, West must verify a cartridge.

### The parallel voice philosophy

The prose-level expression of the same stance is West's 12 non-negotiable rules `western-writing/SKILL.md:402-465`: "no mood without object" (every atmospheric line carries a physical noun), "end on weight" (land on concrete consequence, not qualifier), "no clean violence" (the body is meat), "no anachronism of mind." These are not stylistic preferences — they are the *prose enforcement* of the authenticity lens. A rule whose flavor text violates them feels imported, the same way a wrong-decade revolver breaks the spell. **Generic:** whatever the genre, the prose must be as physically grounded as the mechanics; tone and rules are the same pressure applied at two layers. **Layer:** the lens is General; its *strictness* is a dial (West harder than FL) — see §11.

## 9. The general / situational / optional layering principle

Both books manage complexity the same way: a three-tier layering that keeps the **core lean** and pushes variance to the edges. This is the engine's complexity-management strategy.

**The three tiers (engine-level):**

- **General** — the core resolution and economy, always on, every table. The dice grammar (6 = success), pushing, the success ladder, the metacurrency pool, the five loops. A player who knows only the General layer can play the game.
- **Situational** — rules that apply only in a specific context (combat actions, journey phases, stronghold events, specific Trouble exposures). They extend the core without replacing it; they activate when the fiction calls them and are silent otherwise.
- **Optional** — mode-switching or variant rules a table adopts or drops as a whole. FL's Appendix (heroic campaigns, Legendary gear), Surge of Willpower (1 XP → 1 WP, once/session) `00-engine-core.md:134`; West's Fast Initiative, Consumables as Resource Dice.

**Why the layering exists:** The General layer must stay small enough to hold in working memory during live play. FL's design logic is explicit that good rules "preserve the simple dice grammar," "avoid nested exceptions," and "stay legible in live play" `system-design-map.md:266-269, 276-277`. Every exception, variant, and edge case that is allowed to seep into the General layer makes the core slower and the synergy risks worse (a talent that interacts with an optional rule that interacts with a situational rule is three-deep, and "many local balance problems are actually talent interaction problems" `system-design-map.md:163`).

**The layering discipline (design rule):** When proposing a new rule, first ask which tier it belongs in. A rule that *could* be Situational or Optional but is written as General is a Warning Sign (subsystem inflation, §10a). A rule that is General but reads as an exception to another General rule is almost always mis-layered. **Layer:** the layering principle itself is General; the assignment of any given rule to a tier is a design decision that must be stated explicitly, not left implicit.

## 10. Warning signs (inherited anti-patterns, generalized)

> This is the engine's anti-pattern catalog. **Directly inherited from FL's `system-design-map.md:331-351`, de-flavored to genre-neutral vocabulary, with two additions (f, g) the skill adds.** The validation pipeline in `13-balance-and-synergy.md` checks every proposal against this list. A proposal that trips a warning sign is not auto-rejected — it is flagged for deeper integration review.

### a. Subsystem inflation

**FL:** "The proposal adds a new category, die, or track where an existing rule could carry the load." `system-design-map.md:334-336`.

**Generic:** The proposal introduces a new resource track, die type, condition, or sub-system that duplicates a job an existing rule already does. Before adding, ask: *which existing rule could carry this load if it were extended?* FL's own guidance — "does the rule create new roll logic that should instead reuse the base grammar" `system-design-map.md:155` — is the canonical test. **Layer test:** if the rule belongs in Optional and is written as General, it inflates.

### b. Silent invalidation

**FL:** "A new general rule makes a talent, spell, or item special ability feel redundant." `system-design-map.md:338-340`.

**Generic:** A new rule erases the niche of an existing rule (talent, ability, spell, gear function) without acknowledging it. "Does it invalidate a talent's niche" `system-design-map.md:168`; "does a new rule privilege one kin or profession too strongly" `system-design-map.md:143`. The danger is invisible at proposal time and surfaces only when a player finds their character's signature ability is now something anyone can do for free.

### c. False realism

**FL:** "The rule sounds harsher or more authentic, but only produces stalled play, bookkeeping, or GM mercy." `system-design-map.md:342-344`.

**Generic:** "Realistic" rules that do not actually model reality or sharpen decisions — they add drag. This is FL's bad-realism category restated `realism-audit...md:57-60`: procedure without decision, bookkeeping without tension. The test is the realism sniff-test (§8): if it cannot answer "what decision does this make sharper?" `realism-audit...md:72`, it is false realism.

### d. Vague enforcement

**FL:** "The effect relies on loose phrases like 'harder to act' or 'reduced travel ability' without direct game hooks." `system-design-map.md:346-348`.

**Generic:** A rule whose effect depends on GM interpretation to function — "harder to act," "at a disadvantage," "reduced ability" — with no mechanical hook (no die modifier, no condition, no defined consequence). West's standard is the inverse and explicit: a rule "must produce a clear table behavior, not just evocative text" `SKILL.md:80` and "can rules text be run at the table without interpretation drift?" `western-writing/SKILL.md:499`. If a rule cannot be run without the GM inventing its effect each time, it is vague enforcement.

### e. Misleading survivability

**FL:** "The text presents an outcome as playable when it is functionally retirement or dependence without agency." `system-design-map.md:350-351`.

**Generic:** Numbers or text that look survivable but aren't — or that *hide* non-playability behind a "survivable" label. The FL audit's sharpest line: "survivable must not be used dishonestly for states that effectively end active adventuring" `realism-audit...md:81`. The proposal checklist demands the verdict be stated: "whether catastrophic outcomes are playable, retirement-default, or dead ends" `SKILL.md:127`. A permanently blinded, limbless, or dementia-bound character who is technically alive is misleading survivability if the text calls the state "recoverable."

### f. Setting-laden generic language (skill addition)

**Generic (the skill's own contribution):** A rule written in engine-agnostic space that still carries the *flavor* of one specific setting — "the Blood Mist," "Quarter Day," "Willpower," "the Stronghold" — when the abstraction should be vocabulary-neutral ("the travel unit," "the metacurrency," "the Base"). This is the prose-level version of subsystem inflation: a concept that should be abstracted is left costumed, so readers of one book cannot recognize it in another. Every term in this file should pass the test: *would a reader of either source book, or neither, recognize this as the same concept?*

### g. Sibling-skill duplication (skill addition)

**Generic (the skill's own contribution):** Two design skills (here: `forbidden-lands-design` and `western-rpg-design`) independently reinvent the same engine-level rule, audit method, or warning sign in their own vocabulary, producing drift between sibling games. The YZE-design skill exists *precisely* to prevent this: the engine-level rule should be stated once here, and each sibling skill should cite it rather than re-derive it. A proposal that re-derives an engine rule in setting-specific language, rather than instantiating the abstract one, is sibling-skill duplication. (This warning sign is meta — it governs the *skills*, not the *rulebooks* — but it is what keeps the two books recognizably the same engine.)

### The catalog as a checklist

When reviewing any proposal, run it against a–g in order. FL's proposal method already supplies the structural frame: state the problem, find the owning chapter, trace adjacent systems, check existing terms and procedures, check table playability, decide the voice `system-design-map.md:312-320`. The warning signs are what that method *catches* when it is applied honestly. **Layer:** General — the warning-sign catalog applies to all proposals in all tiers; an Optional rule can be a warning sign just as easily as a General one.

## 11. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Thesis costume** | Frontier survival (body/supply as currency) | Old West grit (grit/belief as currency) | Ecological exposure vs documentary indifference | Match the genre's adversary (land vs country) |
| **Lethality calibration** | Broken-easy / death-hard, never kill the defenseless | Attrition-and-circumstance (the fever decides); historically bounded medical ceiling | Mechanical breakpoint vs slow inevitability | FL-style when you want a clear "Broken" state; West-style when you want time-and-infection to do the work |
| **Authenticity strictness** | Material/ecological realism (cold, hunger, steel) — inventive within tone | Documentary/evidentiary realism (the 1870s ledger) — verify, never invent the anachronism | Invention-permitted vs invention-forbidden | West's strictness for any historical genre; FL's for any invented-but-grounded genre |
| **Optional-rule surface** | Larger (heroic campaigns, artifact/Pride dice, Surge of Willpower, stronghold) | Leaner (Fast Initiative, Consumables as Resource Dice) | More dials vs leaner core | Larger surface for high-fantasy/pulp; leaner for grounded/low-power |
| **Primary loop weighting** | Expedition + Base | Conflict + Recovery | Journey-and-investment vs violence-and-aftermath | Weight the loop the genre's stories are *about* |
| **Failure-pressure idiom** | Mechanical (banes on dice, always on push) | Narrative (Trouble tables, exposure-gated) | Tax on the roll vs tax on the frame | See `00-engine-core.md:172` — both work; match the push-cost model |

## 12. Dials and instantiation recipe

To build a new YZE-family game, set these philosophy dials (each has FL and West as two calibrated points):

1. **State the thesis** — name the genre's *ambition* and its *exposure.* The two answers name the currency and the adversary. *(Sets the whole game's tone.)*
2. **Pick the primary loops** — weight 2 of the 5 as dominant (FL: Expedition + Base; West: Conflict + Recovery). All 5 must still function; 2 carry the campaign. *(Sets what play is *about*.)*
3. **Set the lethality** — Broken-easy/death-hard (FL) vs attrition-and-circumstance (West). *(Sets the threat the Pressure Economy leans on.)*
4. **Pick the authenticity strictness** — inventive-within-tone (FL) vs documentary-verify (West). *(Sets whether you can invent a monster or must verify a cartridge.)*
5. **Decide the optional-rule surface** — large dial set (FL) vs lean core (West). *(Sets how many variant levers the table gets.)*
6. **Wire the resource-at-risk model** — confirm each pressure source (time/body/gear/metacurrency/safety/overreach) has a four-beat loop (pressure→decision→consequence→state change). If any source lacks one, it is decorative. *(Validates the Pressure Economy.)*
7. **Run the axiom test** — for every General rule, confirm it costs something and that safety is expensive. *(Enforces "Nothing Is for Free.")*

**Instantiation recipe (any genre):**
1. Write the thesis sentence (dial 1) — ambition = ___, exposure = ___. If you cannot fill both blanks with physical, credible nouns, the genre is not ready for the engine.
2. Set the lethality (dial 3) and the authenticity strictness (dial 4) *together* — they must agree (a documentary genre wants attrition-and-circumstance; an inventive genre can afford a cleaner breakpoint).
3. Weight the loops (dial 2) to match the genre's stories.
4. Wire the push-cost model and failure-pressure idiom to the thesis (see `00-engine-core.md:174-196` — this is where philosophy meets mechanics).
5. Decide the optional surface (dial 5) from the table's complexity tolerance.
6. Validate the whole against the Warning Signs (§10) and the synergy risks in `13-balance-and-synergy.md`.

## 13. Design intent

The philosophy exists so that **any rule, in either book or any new genre, can be tested against it.** A rule belongs in a YZE-family game if and only if it can answer *yes* to all of these:

- **Does it tie ambition to exposure?** Does it put a resource at risk in service of the thesis? (§3)
- **Does it run the four-beat pressure loop** — pressure → decision → consequence → state change? If a beat is missing, the rule is decorative. (§4)
- **Does it cost something?** Does it honor "Nothing Is for Free," and does it keep safety expensive? (§6)
- **Does it make lethality and attrition *meaningful*** — does the threat of loss make a real decision sharper (fight vs flee, push vs accept, press on vs camp)? (§7)
- **Does it pass the authenticity lens** — does its realism sharpen a decision without sacrificing playability or hiding non-playability? (§8)
- **Is it in the right layer** — General only if it must be always-on; Situational if context-gated; Optional if mode-switched? (§9)
- **Does it avoid all seven Warning Signs** — no subsystem inflation, no silent invalidation, no false realism, no vague enforcement, no misleading survivability, no setting-laden generic language, no sibling-skill duplication? (§10)

If a rule fails any of these, it does not belong in a YZE game — no matter how evocative its text, how historically accurate its detail, or how much it pleases the GM who proposed it. The philosophy is the gate; the mechanics in the other reference files are the mechanisms that pass through it.
