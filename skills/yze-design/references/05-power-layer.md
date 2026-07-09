<!-- markdownlint-disable MD013 -->

# The Power Layer — Magic, Miracles, Powers

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** The power layer is the engine's largest *optional* rule set. This file treats it as a plug-in that sits on top of `00-engine-core.md` — and proves, via West, that the engine runs at full strength with the plug-in removed.

## Contents

1. Source provenance
2. Abstraction target
3. The power families (Spells / Power Words / Rituals / Miracles)
4. Casting models (safe / chance / overcharge)
5. The Willpower/Faith as power fuel (WP + Burn)
6. Ingredients, grimoires, and power sources
7. Mishap tables
8. Power ranks and learning access
9. Epic / high-tier magic
10. Powers and Traditions
11. The on/off choice and genre-fit guidance
12. Divergence rows (FL vs West)
13. Rule Choices and Build Recipe
14. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/07-magic.md` (~5,450 lines) — the maximal instance. The full power layer: 17 disciplines, three spell **types** (Spells / Power Words / Rituals), the casting model (safe/chance/overcharge), the magic-dice table, grimoires, ingredients, **Burn** (self-harm → temporary WP), epic magic + epic ingredients, **per-discipline mishap tables** (17 families), the rarity/secrecy table, the learning/XP rules, and the entire **Forging New Spells** design appendix (rank/scope/damage/control/utility benchmarks, the spell-form template, the 10-check balance test). Discipline list (8 sorcery + 9 druidic): General, Healing, Shapeshifting, Awareness, Symbolism, Stone Song, Blood Magic, Death Magic, Elemental Magic, Ice Affinity, Nature, Swarm Magic, Magma Song, Mentalism, Oneiromancy, Magnetism, Demonic Magic. FL `07-magic.md:21-39` (rarity/secrecy), `:43-51` (learning), `:53-106` (casting), `:108-131` (grimoires/ingredients/Burn), `:137-156` (rituals/epic), `:158-184` (mishap engine + example), `:5254-5452` (forging new spells).
- `01-corebook/03-skills.md:120-138` — the Willpower (WP) Willpower/Faith that *fuels* magic, its cap (10), and its refuel trigger (1 WP per 💀 on Base Dice when pushing).

**Tales of the Old West 2E (West):**
- `01-corebook/03-rolling-the-bones.md:258-311` — **no magic system exists.** West is the engine's **zero instance**: proof the core loop, the Willpower/Faith pool, the push, the Trouble layer, and the conflict model all run without any power layer. The nearest analogue is **Faith** (a pool, not a power source) and a non-rules religious frame. This absence is itself the deliverable's anchor point.

## Abstraction target

Abstract the **power layer** as a genre-neutral *optional* system bolted onto the core engine. FL is the **maximal instance** (17 disciplines, three spell types, two casting models, a fuel economy, a self-harm override, 17 mishap families, an epic tier, and a full spell-design appendix). West is the **zero instance** — the engine's proof-by-construction that the power layer is *purely additive*: remove it and nothing in `00-engine-core.md` breaks.

The deliverables, in priority order:
1. **The on/off + density choice** (§10) — *the single most important output.* A decision table mapping genre → power-layer density (none / low / medium / high) → families subset → casting model → fuel model. West = none; FL = high; the middle is mapped for low-magic, psi, gadgets, and miracles.
2. **The power families** (§3) — a reusable three-tier effect-speed frame: Spells (slow) / Power Words (fast-reactive) / Rituals (long-dramatic), plus a possible Miracles tier.
3. **The casting-model choice** (§4) — safe (guaranteed-but-costly) vs chance (rolled-but-cheap) vs overcharge (pushed-for-scale).
4. **The fuel + cost model** (§5) — Willpower/Faith + the Burn self-harm override.
5. **The mishap-table pattern** (§7) — the failure-pressure layer *for powers*, cross-linked to the typed-table pattern in `04-harm-and-consequences.md`.

Apply the Abstraction Ladder (source instance → common pattern → design intent → choices with FL/West as two points) to each.

## 3. The power families (Spells / Power Words / Rituals / Miracles)

FL sorts every power into one of **three types** by *effect speed* and *action budget*, not by school or element. This sorting is the reusable frame — it is about *when the effect resolves in the turn structure*, which is the axis the core engine already cares about (fast vs slow action, out-of-turn reactions).

| Type | FL action budget | Role in the turn | FL source |
| --- | --- | --- | --- |
| **Spells** | **Slow action** (the default). Summon, bend, raise, twist — the bread and cloth of a caster's work. | Resolves on the caster's turn; competes with attacking/moving. | `07-magic.md:67` |
| **Power Words** | **Fast action, usable *outside your turn*** in direct response to an enemy — "just as you would answer with PARRY or DODGE." A shield of force, a binding syllable, a word that stops. | Reactive; breaks initiative order. This is the engine's *parry/dodge* slot, repurposed for magic. | `07-magic.md:69` |
| **Rituals** | **One turn (15 min) or longer** — a Quarter Day is typical; some run hours or a full watch. Binding oaths, speaking with the dead, reading the coming season, drawing power from a *place* rather than the self. | Resolves outside combat time; the dramatic, high-impact, story-shaping tier. | `07-magic.md:71, 133-135` |

The type is **tagged per spell entry**, not chosen at cast time: `✦ **RANK** 1, **POWER WORD**` / `**RITUAL**` / (unmarked = Spell). FL `07-magic.md:220, 229`. A given effect's type is a *design property* of that power, fixed when it is forged (FL `07-magic.md:5394-5397` codifies exactly this: power word = fast/narrow; spell = slow/default; ritual = long/large-scale; reaction = rare/strict).

**Common pattern — three effect-speed families:**
- **Tier 1 — Standard powers** (FL "Spells"): the slow-action default. The workhorse. Maps onto the core loop's "spend an action, resolve an effect."
- **Tier 2 — Reactive powers** (FL "Power Words"): fast, and crucially *out-of-turn / interrupting*. This tier exists so a power-user can defend like a fighter — it is the engine's defensive-reaction slot (parry/dodge) opened to magic. *This is the tier most often omitted in lighter power systems*, and its presence/absence is a real choice: without it, casters are glass cannons who must pre-cast or die.
- **Tier 3 — Dramatic powers** (FL "Rituals"): long-cast, high-impact, scene- or story-shaping. The tier that changes the world rather than the battlefield. Almost always gated by ingredients, time, or a teacher (FL `07-magic.md:51` — rituals *cannot* be reconstructed from intuition; they require a teacher or grimoire).

**A possible fourth tier — Miracles (faith-based):** FL folds divine-flavored effects (Banish Demon, Holy Ward, Resurrection, Rite of Passage) into the Healing discipline rather than a separate system. West's Faith is a *Willpower/Faith*, not a power source. A genre that wants "clerics" distinct from "wizards" can split the families along a **source axis** (arcane vs divine vs primal vs psionic) *orthogonal* to the speed axis — but FL's proof is that you need not: a single families with flavor-differentiated disciplines is enough. **Layer:** the three-tier speed families is **General** (when the layer is on); the Miracles/source-axis split is **Optional**.

**Design intent:** the families's job is to make a power-user *choose their moment*. A Spell costs your turn; a Power Word saves your life but doesn't end the fight; a Ritual reshapes the situation but demands preparation and exposure. The three tiers map onto three different dramatic registers — tactical, defensive, ceremonial — and a well-designed power layer populates all three so the caster has reasons to care about the turn structure, the reaction window, *and* the downtime clock.

## 4. Casting models (safe / chance / overcharge)

This is the engine's signature contribution to magic design: **you can never fail to cast a spell.** FL `07-magic.md:77`: "Unlike skills, you can never fail at casting a spell. Instead, you roll a number of Base Dice equal to the number of WP you spend." The roll is not a *success test* — it is a *risk-and-scale test*. ⚔ and 💀 are read as *modifiers to an effect that already fires*.

**FL's three casting models (selected per cast):**

| Model | How it works | Cost | Risk | FL source |
| --- | --- | --- | --- | --- |
| **Safe casting** | Cast the spell *below* your talent rank; you may opt to roll one fewer die per point of rank difference. At zero dice or less, **don't roll — the spell simply works as intended.** | Full WP cost (guaranteed). | Zero mishap risk; zero overcharge chance. The reliable, costly floor. | `07-magic.md:83` |
| **Chance casting** | Cast a spell *one rank above* your talent rank. | Full WP cost. | **Automatic** random mishap — no roll needed to know it goes wrong. You can never cast two ranks above. | `07-magic.md:61` |
| **Overcharge (the default roll)** | Cast at-or-below rank; roll Base Dice = WP spent (plus the magic-dice table modifiers, `07-magic.md:87-100`). Each ⚔ = +1 Power Level; each 💀 = a mishap. You **cannot push** this roll. | WP spent (cheapest in WP-per-effect once overcharge fires). | The roll is a *gamble for scale*: more ⚔ = bigger effect, more 💀 = backlash. | `07-magic.md:75-82` |

The **magic-dice table** (`07-magic.md:87-100`) folds rank difference into die count, and adds: +1 die per extra WP; −1 effective spell rank (−1 die) if cast from a grimoire; ingredients do *not* affect dice count (they add flat Power Level). This is a self-contained resolution distinct from the skill roll — it reuses the dice grammar (⚔/💀) but inverts the meaning: ⚔ no longer means "you succeeded," it means "you succeeded *harder*."

**Common pattern — the casting-risk choice (three positions):**
- **Safe (guaranteed-but-costly):** pay the fuel, skip the roll, get the baseline effect. The floor for when a caster *must* land the effect and can afford it. Removes variance at the price of ceiling.
- **Chance (rolled-but-cheap, failure-locked):** reach beyond your rank; the effect fires but a mishap is *certain*. Cheaper in access (you can attempt things above your pay grade) but the cost is paid in consequences, not fuel.
- **Overcharge (pushed-for-scale):** the default gamble — the effect always fires, but the roll decides whether it is *bigger* (⚔) or *bites back* (💀). This is the engine applying its own "push for a cost" logic *inside* the power layer: the casting roll is structurally a push that happens *before* the effect, not after a failure.

**FL-vs-West divergence:** West has no casting roll at all because it has no powers. But note the *structural kinship*: West's Faith-spend-to-push and FL's WP-spend-to-cast are the *same economy* (capped Willpower/Faith → bigger/more-reliable effect). The power layer simply adds a third thing the currency can buy (an effect that didn't exist before), plus a risk face (💀) tuned to magical backlash rather than bodily harm. **Layer:** the casting-risk choice is **General** when the layer is on; you must pick at least one position (FL uses all three).

## 5. The Willpower/Faith as power fuel (WP + Burn)

The power layer does **not** introduce a new currency. It spends the *same* Willpower/Faith the core engine already mints (see `00-engine-core.md` §7). FL's Willpower Points — capped at 10, refueled 1-per-💀-on-Base-Dice-when-pushing — are simultaneously the fuel for kin/profession talents *and* the fuel for every spell. FL `03-skills.md:120-126`; `07-magic.md:73-75`.

**This is the key coupling:** the power layer is *downstream* of the core risk loop. You cast spells with WP; you *earn* WP by taking damage on pushed rolls. A caster who never pushes never has fuel. Magic is, in the rules, *the thing you spend your suffering on.* FL `03-skills.md:124`.

**FL — Power Level = WP spent (modulated by the roll):**
- Base Power Level = WP spent on the spell. FL `07-magic.md:75`.
- Minimum 1 WP per spell, even if the description omits it. FL `07-magic.md:106`.
- Overcharge ⚔ each add +1 Power Level. FL `07-magic.md:79`.
- Ingredients add flat +1 Power Level (do *not* add dice). FL `07-magic.md:100, 5382`.
- NPCs have no WP pool — the GM simply picks a Power Level up to the caster's rank (+1 for an ingredient). FL `07-magic.md:179`.

**FL — Burn (the self-harm override):** When WP runs dry, a caster may **burn their own body to fuel a spell.** At the moment of casting, declare a burn of up to your rank in the spell's discipline; for each point burned, roll a D8 and take 1 attribute damage to the indicated attribute (1–2 Strength, 3–4 Agility, 5–6 Wits, 7–8 Empathy). Each point burned grants 1 *temporary* WP usable only on the triggering spell (vanishes otherwise). FL `07-magic.md:120-131`.

**The decisive design twist:** "You choose how much to burn, but you do not choose where the damage falls." FL `07-magic.md:131`. The *quantity* is player-controlled (a clean cost-benefit choice); the *location* is random (so burning is never a solved optimization — it might cripple the attribute you needed to survive the aftermath).

**Common pattern — fuel + the self-harm override:**
- **Fuel:** a power costs units of the core Willpower/Faith (the same pool that pays for pushing and talents). This *binds the power layer to the core loop* — you cannot spam powers without engaging the engine's risk rules, because that is where fuel comes from.
- **Self-harm override (Burn):** an optional escape valve that lets a caster cast *without* currency by paying in attribute damage instead. Two sub-choices: (a) **player-chosen quantity vs random target** — FL picks the elegant middle (chosen amount, random attribute), which preserves tension; (b) **temporary vs permanent** damage. FL uses normal (recoverable) attribute damage; epic ingredients (§9) escalate to *permanent* attribute loss.
- **Refund rules (optional):** FL's *Absorb Magical Residue* (rank 5, `07-magic.md:456-463`) and *Transfer* (rank 3, `:380`) let casters reclaim or move WP — the layer's internal recycling, gated behind high rank so it cannot trivialize the fuel economy at low levels.

**FL-vs-West divergence:** West's Faith fuels *pushing and Trouble-buyoff* — it never buys an effect that a mundane character couldn't attempt. FL's WP buys *entirely new capabilities* (flight, resurrection, demon-summoning). The Willpower/Faith is identical in shape (capped 10, spent for advantage); what differs is the *scope of what it can purchase*. This is the cleanest single proof that the power layer is an additive extension of the same economy, not a parallel system. **Layer:** fuel-from-core-Willpower/Faith is **General** (when the layer is on); Burn is **Optional** (a grit/ desperation choice — omit for lighter power systems that just gate by WP).

## 6. Ingredients, grimoires, and power sources

FL layers **material and knowledge gating** on top of the fuel cost, so that even a WP-rich caster cannot freely produce any effect. There are two independent gates:

**Gate A — Ingredients (material gating):**
- Most spells list an ingredient; once cast, it is spent (unless noted otherwise). FL `07-magic.md:116-118`.
- An ingredient adds **+1 Power Level** (flat — it does *not* add dice). FL `07-magic.md:100, 5382`.
- Three ingredient roles (forging appendix): *optional* (+1 PL, consumed), *required* (spell cannot be cast without it), *ritual* (rare/costly/dangerous — this is how Rank 4–6 effects are justified). FL `07-magic.md:5382-5384`.
- Symbolism substitutes *the symbol itself* (drawn/carved) for a physical ingredient — the inscribed rune counts as an ingredient from a rules standpoint. FL `07-magic.md:1441`.

**Gate B — Grimoires (knowledge gating):**
- You do not need spells written down to cast them — but casting *from a grimoire* treats the spell as **one rank lower** (which feeds the safe-casting die reduction and lowers mishap odds). FL `07-magic.md:108-110`.
- In combat, readying a grimoire is a **fast action**; using it is a free action requiring one hand. FL `07-magic.md:114`.
- *Writing* a spell down requires casting it once first (chance casting doesn't count), then a Quarter Day + LORE roll (two Quarter Days for a ritual). FL `07-magic.md:112`. This makes grimoires *artifacts of practiced mastery*, not free transcription.
- Learning rituals and epic spells *requires* a teacher or grimoire — "the exacting structure of a ritual cannot be reconstructed from intuition alone." FL `07-magic.md:51`.

**Gate C — Rarity & Secrecy (social gating, non-rules):** Each discipline carries a **Rarity** (Known → Strange → Disturbing → Prohibited — how the public reacts to witnessed magic) and a **Secrecy** (Initiation → Demonstration → Journey — how hard a teacher is to find). These "carry no weight in the rules" but guide GM rulings on social consequences and quest-gating. FL `07-magic.md:13-41`.

**Gate D — Inscribed Symbols (delayed-trigger gating):** Symbolism's inscribed-rune rule set lets a caster inscribe a symbol that *holds its power until triggered* by a set condition (crossing a threshold, a spoken word, a touch). FL `07-magic.md:1443`. This is the engine's "trap / contingency / ward" pattern — a power that *waits*.

**Common pattern — material and knowledge gating:** even with fuel solved, a power layer should make the caster *need the world*: stuff (ingredients), books (grimoires), teachers (secrecy), and places (ritual sites, inscribed surfaces). Each gate is a different kind of scarcity — physical, textual, social, spatial — and a designer picks which to enforce. FL enforces all four; a lighter layer might enforce only one (e.g., gadgets need only *stuff*; psi might need only *fuel*). **Layer:** ingredients and grimoires are **General** (when the layer is on); secrecy tables and inscribed-symbols are **Optional** (setting-specific flavor and rules).

## 7. Mishap tables

When casting goes wrong, FL requires that it go wrong **specifically, per discipline.** This is the power layer's failure-pressure rule, and it is structurally identical to the typed-critical-injury family pattern in `04-harm-and-consequences.md` §5.

**FL — one mishap family per discipline (17 families):** Each discipline has its own D66 mishap table, themed to that path's flavor — a Healing mishap turns septic or leaps to the wrong body; a Blood Magic mishap catches the wrong body in blood-fire; a Demonic mishap draws demon attention or pumps corruption; a Stone Song mishap is geological. FL `07-magic.md:158-166` (the rule), `:536-560` (General Spells family), `:851-875` (Healing family), `:4997-5009` + `:5228` (Demonic + corruption interaction).

**The mishap engine (shared rules across all families):**
- Trigger: any 💀 rolled on the casting dice. FL `07-magic.md:81`.
- Resolution: roll D66 on the *discipline's* table, with a modifier based on 💀 count. FL `07-magic.md:168-176`:

| 💀 rolled | D66 modifier (rollable range) |
| --- | --- |
| 1 | −10 (01–56) |
| 2 | ±0 (11–66) |
| 3–4 | +10 (22–66) |
| More | +10 per each two additional 💀 |

- **Consequence gradient:** every FL mishap table follows the same vertical structure — the low end is a *minor, flavor-rich inconvenience or small attribute damage* (lose 1 Empathy, spoil nearby reagents, a brief penalty); the high end is *catastrophic and possibly character-ending* (the 65–66 rows routinely involve demonic possession, rifts to other dimensions, "make a new character"). FL `07-magic.md:559-560, 874-875`. This gradient is what makes 💀 *escalatingly terrifying* — more skulls doesn't just mean "worse," it *shifts you up the table* toward the no-save rows.
- **Chance casting = automatic mishap:** casting above your rank *guarantees* a roll on this table (FL `07-magic.md:61`) — the cost of reaching beyond your skill is paid here, not in fuel.
- **Corruption interaction (Demonic):** a corrupted caster (corruption > Empathy) adds **+10 to Demonic mishap rolls** (FL `07-magic.md:5009`) — the table itself becomes more dangerous the further you fall, a self-reinforcing doom spiral unique to that discipline.

**Common pattern — the failure-pressure layer for powers (cross-link to `04-harm-and-consequences.md`):** this is the *same pattern* as the typed-critical-injury family. The recipe:
1. Decide which **power sources/types** in your game deserve their own failure flavor (FL: one per discipline; a lighter game might use one table for all powers, or one per source-axis).
2. Build a **D66 table** (or D% / 2d6) per family, with a **severity gradient** — low rows = recoverable/colorful, high rows = catastrophic/retiring.
3. Apply a **count-based modifier** to the roll (FL: −10/+0/+10 by 💀 count) so that "more things going wrong" in the rules pushes toward the worse rows, not just "more rolls."
4. Tie catastrophic rows to the harm system (FL mishaps routinely invoke "roll on the horror/blunt-force critical-injury table" — FL `07-magic.md:556-557, 871-872`), so the power layer's failure pressure *feeds* the harm layer rather than duplicating it.

**FL-vs-West divergence:** West has no mishaps because it has no powers — its failure-pressure layer is **Trouble** (`00-engine-core.md` §6, §10), which is *narrative* and *frame-gated*, not *roll-on-a-table*. A designer who turns the power layer ON must decide whether magical failure uses the engine's existing Trouble layer (lighter, narrative) or a dedicated mishap-table layer (heavier, specific, FL-style). **Layer:** mishap tables are **Situational** — they are the power-layer analog of the harm layer's typed tables, and are required only if you want magical failure to be *specific and memorable* rather than generic.

## 8. Power ranks and learning access

FL gates the power layer through a **rank ladder** that is taller than the normal talent ladder (talents cap at 3; magical talents run to 6) and a **learning economy** that ties advancement to the fiction.

**Ranks:** All spells are rated rank 1–3 in the main lists, with higher-rank spells existing (ranks 4–6 appear in every discipline). You can cast any spell at or below your rank in the linked talent. FL `07-magic.md:57-59, 47`. The forging appendix gives explicit **scope benchmarks per rank** (FL `07-magic.md:5286-5337`):

| Rank | Scope | Damage | Control | Utility |
| --- | --- | --- | --- | --- |
| 1 | Minor — small edge, single target, tight utility | 1 pt / 1 die, one target | brief hindrance | small resource/tool |
| 2 | Tactical — clear fight impact, small zone, brief control | 1–2 pts / 2 dice / small area | short control, deny a fast action | short-lived tools |
| 3 | Strong — shifts a battle/scene, full zone, modest summon | 2–3 pts / full zone / multi-target | zone denial, immobilize | durable tools, party aid |
| 4 | Major — large control, potent transform, place-reshaping ritual | 3–4 pts / large area / decisive hit | strong control, forced movement | major utility |
| 5 | Powerful — stronghold-scale, rare protections, major long-term change | 4–5 pts / siege-scale | area lockdown, forced outcomes | stronghold/campaign |
| 6 | Mythic — world-changing, rare and costly | lethal/catastrophic, harsh limits | commanding force, grave cost | mythic, severe limits |

**Learning economy:**
- Increase a magical talent → learn 2 spells of that rank-or-lower **for free** (the teacher's gift). FL `07-magic.md:49`.
- Any other spell at/below your rank → pay XP = spell's rank + one Quarter Day of study; **no teacher or grimoire needed** for non-rituals. FL `07-magic.md:51`.
- **Rituals and epic magic always require** a teacher *or* a grimoire — they cannot be intuited. FL `07-magic.md:51`.
- No teacher at all → XP cost **tripled**. FL `07-magic.md:45`.

**Forging new spells (the design appendix):** FL ships a complete **spell-design rule set** (FL `07-magic.md:5254-5452`). A caster at least one rank above the target spell collaborates with the GM over 5 days × rank (5 successful WITS rolls per rank). It includes:
- **Rank/scope/damage/control/utility/flavor benchmark tables** (above) — the design constraints.
- **Risky spells:** a spell that reaches too far for its rank is tagged *risky* — it can *never* be safe-cast, no matter how far below your rank. FL `07-magic.md:5278`.
- **The spell-form template** (FL `07-magic.md:5417-5426`) — Rank / Range / Duration / Ingredient + one paragraph.
- **A 10-point balance test** before acceptance (FL `07-magic.md:5430-5450`): Peer Comparison, One-Spell Problem, Risk vs Reward, Casting Pressure, Duration Stress, Stack Check, Permanence Check, Empower Check, Inscription Check, **Keeper Veto** ("if the GM cannot imagine fair counterplay, the spell is not ready").

**Common pattern — advancement within the power layer:** a tall rank ladder (so power can grow across a long campaign) with three access modes — *free-on-rank-up* (talent investment), *XP-bought* (flexible), and *quest-gated* (rituals/epics require the fiction). The forging appendix is the engine's **extensibility contract**: it tells the table how to add powers safely, with explicit benchmarks and a veto. Cross-ref `02-progression-and-xp.md` for how magical-talent ranks sit in the broader advancement model. **Layer:** the rank ladder is **General** (when the layer is on); the forging rule set and risky-spell tag are **Optional** (for tables that want player-authored powers).

## 9. Epic / high-tier magic

FL's epic tier is the engine's answer to "what does the most powerful effect in the genre look like, and how is it gated?" It is gated by a **completely different ingredient economy**, not by more WP.

**Epic magic (FL `07-magic.md:137-156, 465-535, 824-831`):** "spells and rituals that use immense powers that leave some permanent change upon the world." The defining rule: **epic ingredients do not increase Power Level — instead, you must *add* one ingredient per Power Level you want.** FL `07-magic.md:141`. You cannot throw WP at the problem; you must assemble the epic ingredient set. Examples (FL `07-magic.md:147-156`):
- **Attribute loss (+1):** permanently reduce an attribute by 1 (one free use per attribute already lost to age).
- **Monster heart (+X):** the heart of a Strength-10+ monster, used within a week; +1 level per 10 Strength.
- **Life goal (+1):** a strong emotion that fulfills a life's ambition — spent when used.
- **Elven ruby (+1/+2):** let a willing elven ruby empower an item (often killing your body) — two levels.
- **Spellcaster help (+1):** allied casters summing to magic rank ≥ 3.
- **Place of an event (+1/+2/+3):** a location where a world-shaping event occurred, used within a year.
- **Sacrifice (+1/+2, usually corrupted):** unwilling sacrifice adds corruption; sacrificing yourself counts as level 2 *without* corruption.
- **Impure motives (+1, corrupted):** power-seeking or stressed emotion sucked into the casting.

**Corrupted ingredients:** some ingredients *count* toward the requirement but add an equal level of **corruption** to the resulting spell — a permanent downside baked into the artifact or effect. FL `07-magic.md:143`.

**Epic examples:** *Create Artifact* (rank 5 ritual — forges permanent magic items with a per-Power-Level effect budget and a corruption budget; a failed/pushed crafting roll *corrupts* the artifact, FL `07-magic.md:465-501`); *God Spell* (rank 6 — triples Power Level or 5× targets, can scar the land permanently, FL `07-magic.md:503-510`); *Transcendence* (rank 6 ritual — permanently fuses you with your path, FL `07-magic.md:512-525`); *Restore Life* (rank 6 epic — true resurrection without the body, FL `07-magic.md:824-831`).

**Common pattern — the high-end ceiling:** the most powerful effects are gated not by *more fuel* (which a rich character could trivially spend) but by **irreplaceable, fiction-bound costs** — permanent attributes, unique monster parts, significant sacrifices, world-shaping locations. This is the engine's anti-trivialization design: at the ceiling, the limit is *what you are willing to lose or do*, not *what you have banked*. Corruption (a tracked, escalating downside) is the secondary brake — it lets a caster reach further at the cost of a doom spiral (Demonic: corruption > Empathy → demon whispers, demon targeting, +10 to mishap rolls; FL `07-magic.md:5009`). **Layer:** the epic tier is **Optional** — it exists only for genres whose power ceiling includes world-changing acts. A low/medium-density game stops at rank 3–4 and omits epic ingredients entirely.

## 10. Powers and Traditions

A power tradition is a taught, feared, inherited, stolen, or improvised way of doing impossible things. FL's seventeen magical disciplines are the high-density fantasy instance; the portable rule is broader: every tradition needs a source, signs, limits, rites, tools, forbidden acts, backlash, and a place in society.

Use **Powers and Traditions** whenever a game needs wizard schools, miracle paths, psychic disciplines, martial ki, alien technology, weird science, occult rites, superhero gifts, biotech procedures, songs of command, hacker daemons, or any other exceptional layer.

### 10.1 Tradition sheet

| Field | Required answer |
| --- | --- |
| Tradition | what the practice is called in the setting |
| Source | blood, oath, study, spirit, machine, drug, god, place, memory, monster, math, song |
| Signs | what witnesses see, hear, smell, feel, or fear |
| Verbs | 5-8 things the tradition does: heal, bind, reveal, move, break, summon, hide, ward |
| Limits | 3-5 things it cannot do safely |
| Ranks | what rank 1, 3, and 5/6 look like |
| Cost | Willpower/Faith, Burn, ingredient, time, debt, exposure, oath, condition |
| Tools | book, focus, weapon, lab, altar, drug, engine, animal, mask, relic |
| Forbidden acts | what grants power but stains the user |
| Backlash | the mishap family or Trouble table it uses |
| Teachers | who can teach it and what they demand |
| Public reaction | ordinary, strange, disturbing, illegal, holy, classified, fashionable |
| Adventure hooks | where its ingredients, teachers, enemies, and ruins enter play |

### 10.2 Tradition verb menu

| Verb | Rank 1 expression | Rank 3 expression | Rank 5/6 expression |
| --- | --- | --- | --- |
| Heal | restore one attribute, close a wound | cleanse poison, prevent a lasting harm | return the dying, rewrite a scar |
| Harm | deal ordinary damage | area, armor-bypass, condition | kill at range, curse a bloodline, ruin a place |
| Ward | +1 defense, block one type | protect a zone, shield a group | seal a fortress, banish a host |
| Reveal | sense nearby truth | question dead/machines/spirits, see hidden paths | read a season, expose a conspiracy |
| Bind | restrain a target | command a creature, oath, machine, crowd | bind a monster, ruler, spirit, weather |
| Move | leap, glide, pass a barrier | fly, teleport short, move cargo/crew | cross worlds, move a settlement, bend roads |
| Shape | alter material, body, emotion, signal | transform creature/object/terrain briefly | permanent change with epic cost |
| Summon | call a minor helper | call dangerous ally or tool | bargain with a great power |
| Hide | conceal signs, memories, tracks | hide a group, lair, ship, sin | erase a place from maps or minds |
| Command | bolster, frighten, rally | rule a mob or beast | sway an army, court, hive, or city |

**Design rule:** a tradition should have 3-5 strong verbs and 2-4 weak verbs. If it can do every verb equally, it is not a tradition; it is the whole power layer.

### 10.3 Rites and tools

| Rite or tool | What it buys | What it costs |
| --- | --- | --- |
| Spoken word | speed, reaction, surprise | narrow effect, obvious sign |
| Hand sign / focus | control, precision | bound hands, visible tell |
| Ingredient | +1 Power Level or special permission | consumed, rare, illegal, perishable |
| Book / pattern | lower rank or safer method | hand occupied, must be found/protected |
| Place | larger scale or lower cost | travel, exposure, enemy claim |
| Circle | shared strength | shared backlash, time, trust |
| Sacrifice | immediate reach beyond fuel | moral cost, Menace, corruption, public horror |
| Machine / apparatus | stable repeatable effect | bulk, repair, fuel, noise, theft |
| Vow | reliable access | breach consequence |

### 10.4 Blood Price

Blood Price is the broad name for sacrifice-based power. It may be literal blood magic, psychic strain, machine overheat, crew casualties, burnt memories, oath-breaking, donated years of life, illegal fuel, or killing a prepared victim. It is calibrated from FL's ritual sacrifice and epic ingredients, but it should be written in the language of the new game.

**Blood Price procedure:**

1. **Name what is paid.** Blood, years, memories, crew, reputation, innocence, oxygen, rare fuel, body parts, faith, legal safety.
2. **Name who pays.** The caster, a willing helper, an unwilling victim, a community, a machine, the land, an enemy, a bound spirit.
3. **Set the gain.** Default: +1 Power Level, double fuel, one rank permission, one extra target band, one scene of duration, or one impossible casting attempt.
4. **Set the stain.** Corruption, Menace, wanted heat, relationship loss, permanent injury, public horror, machine flaw, ghost, lawsuit, debt, omen.
5. **Resolve the act.** If the payment is unwilling, prepared, public, or taboo, add a backlash roll or raise the mishap table. If it is willing and costly, reduce the social stain but keep the loss.
6. **Record witness.** Someone or something must know: a god, ghost, camera, faction, beast, child, rival, ancestor, AI, local rumor.

| Blood Price | Gain | Stain |
| --- | --- | --- |
| Self-wound | temporary fuel or +1 level | attribute damage, scar, exhaustion |
| Willing helper | shared fuel or extra target | relationship strain, helper harm |
| Unwilling victim | doubled fuel or major level boost | Menace, corruption, law, revenge |
| Rare life | epic permission | grief, debt, impossible witness |
| Place scar | area/rank increase | haunted land, faction claim, future mishap |
| Memory | safe cast or hidden sign | lost bond, false memory, vulnerability |
| Machine burn | instant power surge | broken device, noise, fire, rare parts |
| Public taboo | fear and obedience | wanted heat, scandal, social exile |

**Blood Price validation:** this rule must never become "free power if you are cruel." The stain must be strong enough that the table hesitates. If the payment can be repeated safely, it is too cheap.

### 10.5 Circle of Power

Circle of Power is the broad name for linked casting, shared rites, psychic choirs, hacker teams, synchronized pilots, cult circles, choir miracles, machine clusters, medical teams, or any exceptional act that becomes stronger because several participants act as one.

**Circle procedure:**

1. **Gather the circle.** Set the minimum helpers, required tradition/rank, tools, place, and time.
2. **Name the leader.** One character makes the final casting or command roll.
3. **Choose helper roles.** Anchor, fuel, ward, witness, singer, surgeon, engineer, lookout, victim, scribe, pilot.
4. **Add strength.** Each qualified helper adds +1 die, +1 fuel, +1 level, one protected target, or one project tick. Pick one currency for the circle.
5. **Share danger.** If the rite mishaps, every helper suffers a lesser fallout or one chosen helper takes the leader's full fallout.
6. **Break the circle.** If a member is Broken, panics, betrays, or is removed, the circle tests for backlash.
7. **Close the rite.** Record who now knows, who is bound, what debt exists, and what mark remains on the place.

| Circle role | Adds | If it fails |
| --- | --- | --- |
| Anchor | stabilizes mishap, lowers backlash | leader takes +1 mishap severity |
| Fuel | adds Willpower/Faith or level | helper takes attribute damage or condition |
| Ward | protects circle from interruption | external threat enters the rite |
| Witness | makes effect legal, holy, binding, or public | scandal, broken oath, disputed claim |
| Scribe | preserves rite for later learning | flawed book, false formula, stolen copy |
| Singer | extends range, area, morale | panic spreads through circle |
| Engineer | keeps apparatus stable | strange device breaks or misfires |
| Lookout | prevents ambush/interruption | enemy arrives at worst moment |

**Circle of Power validation:** circles may increase scale, safety, or reach, but not all three at once. Shared casting must create shared vulnerability; otherwise the best play is always to pile on helpers.

### 10.6 Tradition examples without fantasy nouns

| Game frame | Tradition | Source | Signs | Backlash |
| --- | --- | --- | --- | --- |
| Space opera | Black Signal | alien math and forbidden relays | cold lights, delayed voices, static blood | ghosts in comms, ship systems lie |
| Medical drama | Last-Ditch Procedure | trauma medicine and experimental drugs | alarms, shaking hands, legal forms | malpractice, organ failure, addiction |
| Court intrigue | The Red Etiquette | secret oaths and noble bloodlines | silence, gloves, witnesses bowing | scandal, duel, exile |
| Mecha | Synchrony | pilot bond and machine resonance | nosebleeds, echo voices, glowing frame | feedback, cockpit fire, identity bleed |
| Crime | Saint's Luck | favors, superstition, relics, betrayal | candles, cards, old prayers | heat, debt, crew suspicion |

## 11. The on/off choice and genre-fit guidance

**This is the file's central deliverable.** The power layer is the engine's largest *optional* rule set, and the single most important genre-setting decision a designer makes is **whether to turn it on, and how dense to make it.** West proves the engine runs at full strength with it off; FL proves how far the engine scales when it is on.

**The on/off switch is binary; the density is a four-point choice.** A game either has powers (on) or does not (off). If on, density selects how much of the FL apparatus to instantiate.

### The density decision table

| Density | Power layer present? | Families tiers | Casting model | Fuel model | Mishap layer | Rank ladder | Epic tier | Genre fit | Exemplar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **None** | **No.** The engine runs on core loop + Willpower/Faith + Trouble alone. | — | — | Willpower/Faith fuels *push/talents only* | none (use core Trouble) | — | — | Historical, mundane survival, heist, western, war, sports | **West** |
| **Low** | Yes, thin. | Standard (Spells) only — often reskinned as gadgets / psi / knacks | Safe-only (guaranteed, no casting roll) or a single flat roll | Willpower/Faith; no Burn | Single generic mishap table (or core Trouble reskinned) | 1–3 | No | Low-magic fantasy, pulp gadgets, mild psi, "lucky" abilities | gadget/psi reskin |
| **Medium** | Yes, moderate. | Standard + Rituals (drop Power Words, or keep them rare) | Safe + Overcharge | Willpower/Faith + Burn (optional) | 2–4 typed mishap families (per source) | 1–5 | Optional (rank 5 cap) | Sword & sorcery, urban fantasy, superheroic, miracles+clerics | cut-down FL |
| **High** | Yes, maximal. | All three tiers (Spells + Power Words + Rituals) | Safe + Chance + Overcharge | Willpower/Faith + Burn + refunds | Full typed families (one per discipline/source) | 1–6 | Yes (epic ingredients) | High fantasy, mythic, kitchen-sink magic | **FL** |

### How to read the table

- **None (West):** the zero instance. West's Faith (`03-rolling-the-bones.md:258-311`) is a *Willpower/Faith that fuels pushing and Trouble-buyoff* — it never buys an effect a mundane character couldn't attempt. The engine's push-cost model, Trouble layer, opposed rolls, and conflict system are *completely self-sufficient.* This is not a deficiency; it is the proof that the power layer is **purely additive.** Choose None for any genre where "special abilities" would break the fiction (historical, western, war, survival, mystery, sports, social-drama).
- **Low:** turn the layer on but keep it light — usually a single tier (Standard powers), a single casting model (safe, so no one rolls a mishap), one generic failure table, and a short rank ladder. This is the natural home for **reskins**: gadgets (a "spell" is a device with charges), psi (a "spell" is a mental knack), miracles (a "spell" is a granted boon), or "lucky" pulp abilities. The power layer's *structure* (fuel, rank, ingredient-as-gizmo) is reused; the *flavor* is swapped. Crucially, **Low often drops Power Words** — without a reactive tier, power-users must rely on the core parry/dodge, keeping them grounded.
- **Medium:** the middle ground. Add the Ritual tier for dramatic/ceremonial effects, add overcharge so casting has variance, introduce Burn so desperate casting is possible, and build a few typed mishap families (typically one per *source* — arcane/divine/psi — rather than one per discipline). Rank ladder runs higher (to 5) but the epic tier is optional. This is where **low-magic fantasy, sword & sorcery, urban fantasy, and superheroic** games live, and where a Miracles/source-axis split (§3) becomes worth the complexity.
- **High (FL):** the maximal instance — all three tiers, all three casting models, Burn, per-discipline mishap families, a rank-6 ladder, and the full epic-ingredient economy. Choose High when magic is *the* point of the setting and the genre wants casters to feel like a distinct, high-variance, world-shaping class.

### The decision procedure (in order)

1. **Does the genre need powers at all?** If no → **None** (you are done; the engine is complete without this file). West is your reference.
2. **If yes — is the power *specialist* or *universal*?** If only some characters have powers (wizards in a party of fighters), you can afford **Medium/High** density because the power layer is one character's rule set. If *everyone* has a power (psi/gadgets for all), lean **Low** so the layer doesn't dominate every turn.
3. **Pick the families tiers.** Always Standard. Add Rituals if the genre has ceremonial/downtime magic. Add Power Words only if power-users need to defend like fighters (otherwise they are glass cannons).
4. **Pick the casting model(s).** Safe-only for Low; Safe+Overcharge for Medium; all three for High.
5. **Pick the fuel + cost.** Always the core Willpower/Faith (this is what binds the layer to the engine). Add Burn for Medium+ if you want desperate casting. Add refunds only at High.
6. **Pick the mishap layer.** None/trouble-reskin for Low; a few typed families for Medium; per-source-or-per-discipline families for High.
7. **Set the rank ladder and decide on the epic tier.** Low: 1–3, no epic. Medium: 1–5, epic optional. High: 1–6, epic yes.
8. **Validate against the math** (`13-balance-and-synergy.md`): expected WP economy, casting-roll variance, mishap frequency at each 💀 count, and the power-ceiling at max rank + overcharge + empower.

**Layer:** the on/off switch is **General** (a core genre decision); the density choice is **General** once on; the specific tier/model/fuel/mishap choices are the per-genre choices below.

## 12. Divergence rows (FL vs West)

This file's central divergence is the cleanest in the entire engine: **FL has the full power layer; West has none.** That *is* the row. Recording it as the canonical "magic on/off" proof:

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Power layer on/off** | **ON** — full apparatus | **OFF** — zero instance | Engine + maximal rule set vs engine alone | Off for any genre where powers break the fiction; on when powers *are* the fiction |
| **What the Willpower/Faith buys** | Pushing, talents, **and entire new capabilities** (spells) | Pushing and Trouble-buyoff **only** | Extended purchase scope vs core-scope only | Extend scope only if you turn the layer on |
| **Casting resolution** | Dedicated casting roll (⚔ = scale, 💀 = mishap); never a success test | N/A — no casting | Variance + backlash baked in | Add only with the power layer |
| **Power families** | Three tiers (Spells / Power Words / Rituals) | None | Tactical + reactive + ceremonial | Include all three for High; prune for Low/Medium |
| **Casting-risk choice** | Safe + Chance + Overcharge | None | Guaranteed-costly / rolled-cheap / pushed-scale | Pick ≥1 when the layer is on |
| **Fuel** | Core WP (capped 10, harm-refueled) | Core Faith (capped 10, action/success-refueled) | Same economy, different refuel loop | Reuse the core Willpower/Faith — do not invent a new one |
| **Self-harm override (Burn)** | Yes — chosen quantity, random attribute | None | Desperation valve | Optional; adds grit |
| **Failure pressure for powers** | 17 typed D66 mishap families, count-modified | Core Trouble (narrative, frame-gated) | Specific-and-memorable vs narrative-and-light | Mishap tables for Medium+; Trouble-reskin for Low |
| **Material gating** | Ingredients (+1 PL), consumed | None | Powers need *stuff* | Add when scarcity matters to the genre |
| **Knowledge gating** | Grimoires (−1 rank), teachers, secrecy | None | Powers need *books/teachers* | Add for scholarly/tradition-flavored magic |
| **Rank ladder** | 1–6 (taller than the 1–3 talent cap) | None | Long power-growth arc | Scale ladder to campaign length |
| **High-end ceiling** | Epic ingredients (permanent attributes, sacrifices, places); corruption spiral | None | World-changing gated by irreplaceable fiction costs | Include only at High density |
| **Player-authored powers** | Full forging appendix (benchmarks + 10-check veto) | None | Extensibility with safety rails | Include if the table wants to invent powers |

**The meta-point:** every "West option" in this table is *the absence of the rule set*, and the engine works anyway. That is the proof that the power layer is a **plug-in**, not a load-bearing wall.

## 13. Rule Choices and Build Recipe

Each choice has FL (High) and West (None) as the two calibrated endpoints; Low/Medium map the middle.

1. **On/off** — off (West) / on. *(The master switch. If off, stop here.)*
2. **Density** — none / low / medium / high. *(Sets every choice below by default; override per-genre.)*
3. **Families tiers** — {Standard} / {Standard, Rituals} / {Standard, Power Words, Rituals}. *(Effect-speed coverage.)*
4. **Casting-risk model** — safe / chance / overcharge — pick a subset. *(Variance and backlash.)*
5. **Fuel** — core Willpower/Faith (always, when on); add Burn / refunds as desperation and recycling choices. *(Binds the layer to the engine's risk loop.)*
6. **Mishap layer** — none (use core Trouble) / single generic table / typed families (per source or per discipline) / count-modified typed families. *(Failure pressure for powers.)*
7. **Material gating** — none / ingredients (+PL) / required ingredients / ritual ingredients. *(Powers need stuff.)*
8. **Knowledge gating** — none / grimoires (−rank) / teachers / secrecy tables. *(Powers need books/teachers.)*
9. **Rank ladder height** — 1–3 / 1–5 / 1–6. *(Power-growth arc.)*
10. **Epic tier** — off / on. *(World-changing effects gated by irreplaceable costs.)*
11. **Player authoring** — off / forging appendix with veto. *(Extensibility.)*
12. **Source axis** — single-source / split (arcane vs divine vs primal vs psionic). *(Optional orthogonal families — usually unnecessary.)*

**Instantiation recipe (any genre):**
1. **Decide on/off (choice 1).** If the genre's fiction is broken by special abilities, turn it off — you have West, and the engine is complete.
2. **If on, set density (choice 2)** using the §10 decision procedure (specialist vs universal power; genre's relationship to variance and backlash).
3. **Wire fuel to the core Willpower/Faith (choice 5)** — never invent a parallel currency; the layer's elegance is that it spends the *same* pool the core loop mints.
4. **Pick the casting-risk model(s) (choice 4)** consistent with density and tone (safe for grounded; overcharge for variable; chance for "reach beyond your skill").
5. **Pick the families tiers (choice 3)** — decide explicitly whether power-users get a reactive tier (Power Words); this single choice determines whether casters can defend themselves.
6. **Build the mishap layer (choice 6)** to match the failure-pressure tone — typed families for "specific and memorable," core Trouble for "light and narrative."
7. **Add gating (choices 7–8)** only for the scarcity types your genre cares about (gadgets → ingredients; scholarly magic → grimoires; forbidden magic → secrecy).
8. **Set the rank ladder (choice 9) and epic tier (choice 10)** to the campaign's power ceiling.
9. **Validate the whole** against the math (`13-balance-and-synergy.md`): WP throughput vs spell costs, mishap rate at each 💀 count, overcharge ceiling at max rank + Empower Spell, and the permanent-effect cap (forging appendix's Permanence/Empower checks, FL `07-magic.md:5444, 5446`).

## 14. Design intent

The power layer is **optional *because* the engine's pressure loop works without it** — West is the proof. The core loop (push-once-pay-a-cost, latent cost face, Willpower/Faith refueled by risk, one-chance rule) generates drama on its own; magic is not required to make a roll meaningful. When the layer *is* present, three principles govern it:

- **The layer must add *decisions*, not just power.** FL achieves this by making every cast a three-way choice — *safe* (guaranteed but full-cost, no ceiling), *overcharge* (gamble for scale, risk backlash), or *chance* (reach beyond your rank, eat a certain mishap) — and by giving the desperate caster a fourth: *burn* your own body for fuel you don't have. A power system where you always just cast the biggest spell you can afford is a *solved problem*; FL's casting-risk choice (§4) ensures it never is.
- **Fuel binds the layer to the core loop.** Powers cost the *same* WP that pushing earns. A caster who wants to cast must first *engage the engine's risk rules* — take damage on pushed rolls to bank WP. This is what keeps magic from floating free of the rest of the game: the power layer is *downstream* of the harm-and-push economy, not parallel to it (§5).
- **Mishaps keep magic from being solved.** FL's per-discipline mishap families (§7) ensure that when casting goes wrong, it goes wrong *specifically and memorably* — a Healing mishap is septic, a Stone Song mishap is geological, a Demonic mishap feeds a corruption spiral. The count-modified D66 gradient (−10 / +0 / +10 by 💀) means "more skulls" doesn't just mean "more damage," it means *sliding toward the character-ending rows.* This is the power layer's failure pressure, and it is the direct analog of the typed-critical-injury pattern in the harm layer (`04-harm-and-consequences.md` §5) — the same design pattern, applied to a different failure domain.
- **The ceiling is gated by *cost*, not by *fuel*.** Epic magic (§9) cannot be bought with banked WP; it requires irreplaceable, fiction-bound payments — permanent attributes, unique monster hearts, significant sacrifices, world-shaping locations. This is the engine's anti-trivialization core: at the top, the limit is *what you are willing to lose or become*, not *what you have saved*. Corruption extends this downward as a slow doom spiral for those who reach too far too often.

The FL-vs-West divergence is the engine's proof that **the same spine supports both a game with no magic at all and a game with seventeen magical disciplines** — and that the difference is a set of *choices*, not a different engine. A new genre's job is to set the on/off switch and the density choice, wire the fuel to the core Willpower/Faith, and then decide how much failure pressure and how high a ceiling its fiction can bear.
