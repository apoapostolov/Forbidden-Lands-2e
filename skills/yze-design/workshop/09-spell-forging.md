<!-- markdownlint-disable MD013 MD024 -->

# Spell Forging — Designing New Powers in Play

> **STATUS: WORKSHOP MODULE.** A downtime rule set that lets a player and the GM **collaboratively design a new power** through a sequence of rolls, rather than picking from a fixed list. It converts spell invention into a *long-process roll* whose surplus successes buy the spell's qualities from a player-authored menu — the engine's **Success Menu** (`00 §4`) applied to the power layer (`05`). This module sits *below* `08-spell-systems.md` — pick your magic system there, then design individual spells here. *Core is generic; the worked example (high fantasy) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic design space
   - 2a. Rule overview
   - 2b. NEW CONCEPTS introduced
   - 2c. Rules reference (tables & procedures)
   - 2d. Forging across the magic-system archetypes (`08`)
3. The pressure loop
4. Choices
5. Integration points
6. Failure modes & edge cases
7. Check notes
8. Worked genre example — High fantasy (forbidden sorcery)

## 1. Origin — how this was built

- **Source pattern(s):** the **Success Menu** (`00 §4`, just added — each surplus ⚔ on a downtime roll buys one player-declared quality of the output) is the spine of the forging roll; **P3** (graded success ladder + threshold-raise — the forging roll is read on the success ladder, and the caster may raise the threshold to aim higher); **P8** (feature grammar — a forged power is a bundle of composable tags, exactly as weapons are in `references/08-gear-and-economy.md §6`); **P1** (push-and-pay — each forging day's WITS roll can be pushed at the usual cost, binding invention to the body); **P4** (typed D66 — the backlash table when a forging goes wrong). The whole module sits *inside* the power layer (`05`); it does not work without a power layer turned on.
- **Reinvention operator:** **Domain Transfer + Fusion** (Operators 1 + 4 from `18 §4`). Domain-transfer the Success Menu — canonically a *camp/craft/build* rule pattern (`06 §9`) — to *power design*: the "output" you are building is not a shelter or a weapon but a *spell*. Fuse it with P8 (feature grammar): each menu entry a surplus ⚔ buys becomes a **feature tag** on the new power, exactly as a weapon's tags gate its actions (`03 §9`, `references/08-gear-and-economy.md §6`). The fusion is what makes a forged spell a *designed artifact* with load-bearing tags, not a free-form wish.
- **Target psychology:** **Investment / authorship** (`17`, the agency-ledger column). Produces *powers that feel personally crafted* — the player named what they wanted, the dice decided how much of it they got, and the GM ratified the result against the engine's benchmarks. This is the engine's MAKE CAMP pleasure (`06 §9`) scaled up to a multi-session project: a high roll buys a richer spell; a weak roll yields a narrower one that must be reforged later.
- **Problem solved:** most RPGs either (a) offer a fixed spell list the player picks from (no authorship; the caster is a shopper, not a designer), or (b) allow free-form spell invention with GM-veto-only balance (inconsistent; the GM becomes the entire balance team with no rubric). FL ships a *third way* — a structured forging process with explicit benchmark tables, a 10-point balance test, and a veto — but documents it as FL-specific prose. This module abstracts that third way into an engine-agnostic rule set any YZE-family game can drop in, and wires it to the **Success Menu** so the *roll itself* distributes the spell's qualities, not just GM judgement.

## 2. The generic design space

### 2a. Rule overview

Spell forging is a **downtime project** that produces one new power. The project has two phases: a **design phase** where the player and GM agree on what the spell *is* (its intent, its rank, its desired qualities), and a **forging phase** where the caster rolls repeatedly over time and the dice decide how much of the design *takes*. The output is a finished spell written in the engine's standard spell-form template (§2c), ready to be learned and cast through the power layer's normal rules (`05 §4`).

The **design phase** is the Success Menu made explicit. Before any dice are rolled, the player states the spell's **major effect** (what it fundamentally does — heal, bind, burn, reveal, transform) and then **names the qualities they want** it to have: longer duration, a wider area, a second target, a built-in resistance roll, freedom from an ingredient. The GM listens, consults the rank/scope benchmarks (§2c) to set the spell's **rank**, and writes down the **menu** — the list of qualities surplus successes can buy. Some entries the player named may cost more than one ⚔ (especially potent ones the GM judges above the rank's normal scope); some may be rejected entirely as belonging to a higher rank. The menu is **player-authored within GM constraints**, ratified against the benchmark tables — this is the same authority split as MAKE CAMP's improvement list (`06 §9`), scaled to magical authorship.

The **forging phase** is the long-process roll. Creating a spell takes a number of **forging days** (each one Shift or Quarter Day of dedicated work), and on each forging day the caster rolls a **knowledge attribute** (WITS or equivalent). Each success banked is one ⚔ toward the spell. When the project's ⚔ total reaches the spell's **forging cost** (set by rank — §2c), the spell is **learned at its baseline**: the major effect works, the rank is fixed, the type tag (STANDARD / REACTIVE / RITUAL) is set, but *none of the menu qualities are purchased yet*. Each surplus ⚔ beyond the forging cost is spent, at the moment of completion, on the **Success Menu** — buying the spell its qualities one by one. A strong forging run produces a rich, flexible spell; a marginal one produces a narrow spell the caster may later **reforge** (below) to expand. This is the Success Menu applied to a *multi-roll* project rather than a single downtime roll: the menu is built up front, the ⚔ accumulate across days, and the spend happens at completion.

The whole process is **bounded by the Risk principle** (`05`, FL's forging appendix): a spell that pushes beyond its rank's scope is tagged **RISKY** — it can never be safe-cast, no matter how far below the caster's rank. This is the forging's anti-trivialization valve, parallel to the corruption spiral in `workshop/07`: power that runs ahead of its limits carries a permanent cost. A forged spell that is too strong for its rank is either *raised in rank* (costing more to learn and cast) or *tagged RISKY* (forever unstable). The GM decides which, using the 10-check balance test (§2c) as the rubric.

### 2b. NEW CONCEPTS introduced

- **NEW CONCEPT — Success Menu applied to power design:** The Success Menu (`00 §4`, just added) is canonically a *camp/craft/build* rule pattern — surplus ⚔ on MAKE CAMP buy camp improvements (`06 §9`). Here it is **domain-transferred to the power layer** (`05`): the "output" is a spell, and the menu entries are the spell's *feature tags* (duration, area, targets, resistance, ingredient-freedom). The rule is recombination; the **application** — a power's qualities distributed by a forging roll, not chosen freely — is new: no core system gates *what a power does* behind a downtime roll. FL's forging appendix assigns qualities by GM judgement alone; this module makes the dice arbitrate. *Extends the Success Menu from physical outputs (camps, items) to designed capabilities (spells, rituals).*
- **NEW CONCEPT — Multi-roll accumulation into a Success Menu spend:** The Success Menu fires on a *single* downtime roll (MAKE CAMP is one Survival roll). Forging is a *multi-day project*: the caster rolls once per forging day, banks successes, and spends the accumulated surplus on the menu at completion. This fuses the Success Menu with **P6** (the activity-menu / labor-distribution spine): each forging day is one "activity," the project is the time block, and the menu is the output's feature list. No core system accumulates ⚔ across multiple rolls into a single menu spend. *Extends the Success Menu from instant resolution to project-scale resolution.*
- **NEW CONCEPT — Reforging (iterative authorship):** FL's forging is one-shot — you forge a spell once, it is learned, done. This module adds **reforging**: a learned spell can be re-forged later (a new forging project, same spell) to *add menu qualities the original roll could not afford*. The reforging cost is lower (the baseline already exists), but each reforging **raises the spell's RISKY threshold** (it gets harder to safe-cast as it accumulates tags). This gives casters a growth path for signature spells across a long campaign — a power that starts narrow and is enriched over time, mirroring how a stronghold (`07 §4`) grows functions. *Extends the power layer with an iterative-authorship valve FL's one-shot forging lacks.*
- **NEW CONCEPT — Quality-cost table for menu entries:** FL's forging benchmarks tell the GM *what a rank can do* (scope/damage/control/utility) but not *what each quality costs in ⚔*. This module ships an explicit **quality-cost table** (§2c) — a menu entry's ⚔ price is set by how far it reaches beyond the spell's rank-baseline. This makes the Success Menu spend *rules* rather than judgement-call: "extend duration one step" = 1 ⚔; "add a second target" = 1 ⚔; "add a second *major effect*" = 3 ⚔ and raises the rank. *Extends the forging appendix with a pricing layer the original leaves to GM fiat.*

*Everything else is pure recombination of P1–P15: the forging roll is P1 (+ P3 ladder); the spell's tags are P8 (feature grammar); the forging days are P6 (activity menu); the RISKY tag is P12 (layering) + the cost-of-safety axiom (`10 §6`); the mishap-on-failure is P4 (typed D66). Only the four applications above are genuine engine extensions.*

### 2c. Rules reference (tables & procedures)

This section is the **runnable content** — a designer should be able to run a forging project from this alone. Everything is generic; swap the nouns (WITS → your knowledge attribute, WP → your Willpower or Faith, etc.) per `15`.

#### The spell-form template (the output format)

Every forged spell is written in this template — the engine's standard power-entry format (FL `07-magic.md:5413-5426`, generalized). The type tag goes on the RANK line; the qualities purchased via the Success Menu are woven into the descriptive paragraph as feature tags.

```
#### SPELL NAME

✦ RANK X [, TYPE TAG(S)]
✦ RANGE: [see vocabulary below]
✦ DURATION: [see vocabulary below]
✦ INGREDIENT: [none / optional (+1 PL, consumed) / required / ritual-rare]

[One paragraph: the major effect, how Power Level scales it, how targets resist
(if applicable), and any qualities purchased via the forging Success Menu.]
```

**Type tags** (on the RANK line): `STANDARD` (slow action — the default, omitted), `REACTIVE` (fast action, usable out-of-turn in the parry/dodge slot — the power-user's defense tier, `05 §3`), `RITUAL` (one Turn / Quarter Day or longer — the dramatic, story-shaping tier), `REACTION` (rare; strict limits required), `EPIC` (uses the epic-ingredient economy, `05 §9` — each PL requires its own irreplaceable ingredient), `RISKY` (never safe-castable, regardless of rank difference), `METAMAGIC` (cast layered onto another spell — e.g. EXTEND, HOLD).

#### The design phase — building the menu (numbered procedure)

Before any forging roll, the player and GM run this procedure. The output is a written **forging brief**: the spell's rank, type, baseline effect, and the Success Menu of qualities surplus ⚔ can buy.

1. **State the major effect.** The player says, in one sentence, what the spell fundamentally does (heal, bind, burn, reveal, transform, summon, ward, move, sense). The GM notes it. This is the spell's identity — everything else is elaboration.
2. **Consult the scope benchmark** (table below) and **set the rank.** The GM judges which rank's "scope" row the major effect fits. A heal is rank 1 (minor — single target, tight utility); a zone-wide fireball is rank 3 (strong — shifts a battle, full zone); a stronghold-scale ward is rank 5 (powerful). The rank is the spell's home; the caster must be *at least one rank above* it to forge it (FL `07-magic.md:5262`). If the effect spans two ranks' scopes, pick the higher — the spell reaches, and will likely be tagged RISKY (step 7).
3. **Set the type tag.** Standard (slow) by default. REACTIVE only if the effect is narrow and immediate (a shield, a countersyllable — the defense tier). RITUAL if the effect is lasting, large-scale, or world-shaping. REACTION only with strict limits and clear counterplay (rare). EPIC if the effect is rank 5-6 and gated by irreplaceable fiction costs (`05 §9`).
4. **Player names the desired qualities.** The player lists what they want beyond the baseline: longer duration, wider area, more targets, a resistance roll, no ingredient, a second minor effect, a delayed trigger (the "trap/ward" pattern, `05 §6` Gate D). The GM writes them all down — none are rejected yet.
5. **GM prices each quality** against the **quality-cost table** (below). Each menu entry gets a ⚔ cost: 1 for a one-step extension (duration up a rung, +1 target, +1 die of damage); 2 for a two-step extension or a second minor effect; 3 for a second *major* effect (this usually raises the rank — step 7). Entries the GM judges above the rank's scope are either rejected or accepted *with a RISKY tag consequence* (step 7).
6. **GM sets the forging cost** (the ⚔ threshold to learn the spell at baseline) from the rank-cost table below. This is what the caster must bank before any menu spend happens.
7. **Apply the Risk principle.** If the spell stacks too many minor effects, pushes the limits of its rank, or does more than one thing at full strength, tag it **RISKY** (never safe-castable) OR raise its rank one (costing more to learn and cast). The GM decides using the 10-check balance test (below) as the rubric. "Magic is strong because it is risky; a safe spell spreads, and a spread spell rots a world" (FL `07-magic.md:5272`).
8. **Write the forging brief.** Rank, type, major effect, forging cost, and the priced Success Menu. This is the contract for the forging phase.

#### Rank / scope benchmark table (sets the spell's home rank)

The spell's rank is set by what its major effect *does*, judged against these scopes. FL `07-magic.md:5286-5337`, generalized. Each rank also carries damage / control / utility sub-benchmarks the GM uses to price menu entries.

| Rank | Scope (overall ceiling) | Damage benchmark | Control benchmark | Utility benchmark |
| --- | --- | --- | --- | --- |
| **1** | Minor — small edge, single target, tight utility | 1 pt or 1 die, one target | brief hindrance | small resource / minor tool |
| **2** | Tactical — clear fight impact, small zone, brief control | 1–2 pts / 2 dice / small area | short control, deny a FAST action | short-lived tools, travel aid |
| **3** | Strong — shifts a battle/scene, full zone, modest summon | 2–3 pts / full zone / multi-target | zone denial, immobilize briefly | durable tools, party aid |
| **4** | Major — large control, potent transform, place-reshaping ritual | 3–4 pts / large area / decisive hit | strong control, forced movement | major utility, ritual shaping |
| **5** | Powerful — stronghold-scale, rare protections, major long-term change | 4–5 pts / siege-scale | area lockdown, forced outcomes | stronghold / campaign utility |
| **6** | Mythic — world-changing, rare and costly | lethal / catastrophic, harsh limits | commanding force, grave cost | mythic, severe limits |

#### Forging cost by rank (the ⚔ threshold to learn the spell at baseline)

The forging cost is the number of banked ⚔ required to learn the spell *before* any Success Menu spend. Surplus ⚔ beyond this go to the menu.

| Rank | Forging cost (⚔) | Forging days | Notes |
| --- | --- | --- | --- |
| **1** | 5 | 5 | Each day: one knowledge-attribute roll; bank ⚔. |
| **2** | 10 | 10 | |
| **3** | 15 | 15 | |
| **4** | 20 | 20 | Rituals typically; often requires a teacher. |
| **5** | 25 | 25 | Stronghold-scale; epic ingredients begin to apply. |
| **6** | 30 | 30 | Mythic; epic-ingredient economy governs (each PL needs its own ingredient, `05 §9`). |

*A forging day is one Shift (or Quarter Day) of dedicated work. The caster may do other things that day, but the forging roll consumes that time block. Days need not be consecutive, but a project abandoned for a full season loses its banked ⚔ (the insight fades) — the GM may waive this for a signature spell the caster is actively researching.*

#### The quality-cost table (prices each Success Menu entry)

Each quality the player wants costs ⚔ from the surplus. This table makes the spend rules. "Step" means one rung on the range/duration vocabulary (below).

| Quality | ⚔ cost | Notes |
| --- | --- | --- |
| Extend **duration** one step | 1 | e.g. Immediate → One round per PL. See duration vocabulary. |
| Extend **duration** two steps | 2 | e.g. Immediate → One turn per PL. |
| Widen **range** one step | 1 | See range vocabulary. Often cheaper to lock range and spend on effect. |
| Add **+1 target** | 1 | +1 target per 2 PL for stronger effects (GM judgement). |
| Add **+1 die / +1 pt** of damage scaling | 1 | Per the damage benchmark for the rank. |
| Add a **resistance roll** for targets | 1 | If the spell removes choice, it must allow resistance (`05`, FL `07-magic.md:5398`). Often *required*, not optional. |
| Remove the **ingredient** requirement | 2 | The spell is cast from WP alone. Tempting but removes a scarcity gate. |
| Make the ingredient **reusable** (not consumed) | 2 | The item is a focus, not fuel. |
| Add a **delayed trigger** (trap / ward / contingency) | 2 | The spell waits for a condition (`05 §6` Gate D). Triggers the Inscription Check (10-check). |
| Add a **second minor effect** | 2 | A secondary capability at less-than-full strength. |
| Add a **second major effect** | 3 | Almost always raises the rank by 1 (step 7). This is "two spells in one" — the classic RISKY trigger. |
| Make the effect **permanent** | 3 + RISKY | Permanent effects trigger the Permanence Check (10-check). Usually reserved for rank 4+ rituals. |

*The GM is the final arbiter of cost. If a quality is not on this table, price it by analogy to the closest entry and note the ruling. The 10-check balance test (below) is the backstop — if a spell passes design but fails balance, the cost was too low.*

#### Range and duration vocabulary (the spell's spatial and temporal tags)

Forged spells use the engine's standard range and duration terms. "Keep distances short and time brief unless the spell is restrained by ritual or rare ingredients. Long durations should feel like commitments, not conveniences" (FL `07-magic.md:5339`).

**Range (in increasing order):** `PERSONAL` (self only) · `ARM'S LENGTH` (touch) · `NEAR` (one target or small group, same zone) · `SHORT` (a full zone, or a visible target in another zone) · `LONG` (a distant zone, battlefield-wide) · `DISTANT` (ritual distance, map-scale).

**Duration (in increasing order):** `IMMEDIATE` (instantaneous) · `ONE ROUND` / `ONE ROUND PER PL` (combat control) · `ONE TURN` (15 min) / `ONE TURN PER PL` (strong effects with a visible sustain cost) · `QUARTER DAY` (travel, recovery, extended protection) · `ONE DAY OR LONGER` (rituals, shaping, long-term change) · `PERMANENT` (lasting changes — always flagged for the Permanence Check).

#### The forging roll (P1 + P3 — numbered procedure)

Each forging day, the caster rolls. The roll is a normal skill roll, not a casting roll — it uses the engine's core resolution (`00 §3`), not the power layer's casting-risk choice (`05 §4`).

1. **Roll the knowledge attribute** (WITS or equivalent) + the relevant **skill** (LORE, the casting discipline's talent, or a dedicated FORGING/CRAFT skill if the game has one). Difficulty is set by the GM (Average 0 by default; raise for spells above the caster's comfort, lower with a teacher or grimoire). Read on the success ladder (`00 §4`): 0 ⚔ = no progress that day; 1 ⚔ = bank 1; 2 ⚔ = bank 2; 3+ ⚔ = bank 3 (the critical surplus can be pushed for more, see step 3).
2. **Bank the ⚔** toward the forging cost. The project's running total is tracked on the forging brief. When the total reaches the forging cost, the spell is **learned at baseline** — the major effect works, the rank and type are fixed. Any further ⚔ banked (or any surplus at the moment of completion) goes to the Success Menu.
3. **The caster may push** the forging roll (P1, `00 §6`), paying the normal cost (attribute damage, Willpower/Faith, or Trouble per the game's push-cost model). A pushed forging roll can bank extra ⚔ — but a pushed failure banks nothing and the cost is paid. *This binds invention to the body*, exactly as casting does: a caster who forges aggressively takes damage, and that damage refuels the core pool they will spend casting the spell later (`00 §7`). The loop is intentional.
4. **Failure is not catastrophe.** A day that rolls 0 ⚔ banks nothing, but the project is not lost — the caster tries again next forging day. The project is only lost if abandoned for a full season (the banked ⚔ fade) or if the GM invokes a **forging mishap** (see below) on a dramatically bad roll.
5. **A teacher or grimoire halves the time.** With a teacher (who knows the spell's discipline at rank ≥ the spell's rank + 1) or a grimoire (a written treatise on the effect), each forging day banks **double** ⚔ (a success banks 2/4/6 instead of 1/2/3). This mirrors FL's learning economy (`05 §8`): rituals and high-rank spells effectively *require* a teacher or grimoire — "the exacting structure cannot be reconstructed from intuition alone."

#### Forging mishap (P4 — when invention goes wrong)

Optionally, the GM may call for a **forging mishap roll** when a forging day's pushed roll produces 3+ 💀 (the engine's "severe setback" threshold, `00 §6`), or when the project is abandoned and restarted badly. Roll on the forging-mishap table — a typed D66 family themed to *invention gone wrong* (analogous to a discipline's mishap table, `05 §7`). The 65/66 rows are character-ending (the spell consumes the caster, the insight breaks their mind, a permanent Corruption tag is gained per `workshop/07`).

**Generic forging-mishap family (Procedural — narrative cost):** build the 36 rows on the spine of *what went wrong in the lab* — wasted materials, a flawed insight that must be unlearned (lose banked ⚔), a backlash that wounds the caster (roll on the harm layer's crit table, `04 §5`), a summoned instability that escapes (a free encounter), a Corruption stain (`workshop/07`) for spells that reach into forbidden domains, up through the 65/66 climax (the spell takes on a life of its own — it becomes a sentient hazard, or the caster is permanently transformed). *This is P4 applied to the design process itself, not to casting — a sibling of the discipline mishap tables, tuned to invention.*

#### The 10-check balance test (run before the spell enters play)

Before a forged spell is accepted into the game, run these ten checks in order. If the spell fails one, fix it before moving on. FL `07-magic.md:5430-5452`, generalized. This is the **backstop** that makes player-authored powers safe — the Success Menu distributes qualities, but the 10-check decides whether the *result* is balanced.

**1. PEER COMPARISON.** Pick three existing powers of the same rank and discipline. If the forged spell beats all three on two or more axes (damage, control, duration, range, action budget, flexibility), it is too strong — remove a menu quality or raise the rank.

**2. ONE-SPELL PROBLEM.** Ask whether this spell replaces other choices. If it answers too many situations alone, it needs a hard limit, a narrower target, or a higher rank. A spell that is always the right answer is a spell that makes every other spell wrong.

**3. RISK VS REWARD.** If the effect is bold, the risk must be bold. Add a ritual, a rare ingredient, a harsh limit, or a clear downside. If it is still safer than its peers, it is too cheap. This is where the RISKY tag is applied — the spell that runs ahead of its rank pays forever.

**4. CASTING PRESSURE.** Cast it at minimum Power Level. If it is still a strong answer, reduce it. Then cast it at a typical PL for its rank; if it feels like a rank +1 spell, it is too strong. The baseline (no menu qualities) should be *narrow*; the menu is what makes it rich.

**5. DURATION STRESS.** If the spell lasts longer than one turn, ask what it blocks or deletes. If it prevents meaningful counterplay for a full fight, shorten the duration or add a resistance roll each round.

**6. STACK CHECK.** Consider the best-case combo (talents, rituals, ingredients, allies). If the ceiling feels abusive, add a cap or remove a scaling axis. "Never scale everything at once — if you do, it is no longer one spell, but a bundle of several spells" (FL `07-magic.md:5374`).

**7. PERMANENCE CHECK.** For permanent changes (attribute bonuses, armor reduction, body modification, persistent summons), ask how many times it can be cast on the same target. If no cap, add one. "Permanent effects that stack without limit will break any system given enough sessions."

**8. EMPOWER CHECK.** Cast the spell at doubled Power Level (as if empowered by a metamagic effect). If the empowered version produces an effect belonging at a higher rank, cap the spell's PL scaling or declare it cannot benefit from external PL amplifiers.

**9. INSCRIPTION CHECK.** Ask whether the spell could be inscribed as a symbol/ward that triggers autonomously without the caster present. If so, does it remain balanced? Area damage, Corruption generation, and permanent effects should not be eligible for inscription unless the GM adds severe limits.

**10. KEEPER VETO.** If the GM cannot imagine fair counterplay or a meaningful consequence, the spell is not ready. Rework it until it *invites play* instead of shutting it down. This is the final authority — the benchmarks and the menu pricing serve the veto, not the other way around.

#### Reforging (iterative authorship — extending a learned spell)

A learned spell can be **reforged** to add menu qualities the original forging roll could not afford. This is a new forging project on the same spell.

1. **The reforging cost** is **half the original forging cost** (round up), because the baseline already exists — the caster is enriching, not inventing.
2. **The reforging days** are half the original (round up). A teacher or grimoire still doubles banked ⚔.
3. **Each reforging raises the spell's RISKY threshold by one step.** A spell reforged once is RISKY if it was not already; a spell reforged twice cannot be safe-cast even one rank below the caster. This is the cost of accumulation — a signature spell that grows across a campaign becomes correspondingly unstable, mirroring the corruption spiral (`workshop/07`) at a slower cadence.
4. **Reforging cannot change the major effect or the rank.** It adds menu qualities only. To change what the spell *does*, forge a new spell.

*Reforging gives a long-campaign caster a growth path for a signature power — the spell that defines them — without handing out free power. The RISKY escalation is the brake: a spell enriched too often becomes too unstable to rely on, forcing the caster to diversify rather than über-tool one effect.*

### 2d. Forging across the magic-system archetypes (`08`)

The forging procedure above assumes the **Path/Talent archetype** (`08` #3, FL's own model) — a discipline talent gates rank, the spell is learned into the tree. But `08-spell-systems.md` catalogs twelve archetypes, and forging adapts to each. The core procedure (design → roll over days → spend surplus on the Success Menu → 10-check) is unchanged; what differs is **what is being forged** and **where the finished spell goes**. This subsection is the bridge between the two modules — read it after choosing your archetype in `08`.

**Vancian / Book (#1):** forging produces a **new spell entry in the caster's grimoire**. The "forging days" are days spent *writing and testing* the spell in the book; the knowledge roll is WITS + LORE. The finished spell must still be **prepared** (memorized into a slot) to be cast — forging creates the recipe, preparation cooks it. A forged Vancian spell's slot is a resource die (D6–D12 by rank) per `08` #1's NEW CONCEPT. Reforging a Vancian spell means rewriting the grimoire entry to add qualities — the old recipe is lost (replaced).

**Spell-as-Skill (#2):** forging produces a **new skill** the caster gains at rank 1. The forging roll uses whatever attribute the skill will use (PRESENCE for Pyromancy, EMPATHY for Enchantment). The "forging days" are practice — the caster is training the new skill, not researching a formula. Reforging is simply **advancing the skill** (spending XP to raise its rank, per `02 §3`), which unlocks richer effects at higher ranks — no separate RISKY rule, because the skill rank itself gates power. The Success Menu here maps to "what the skill can do at rank 1 vs rank 3 vs rank 5" — the menu is the skill's growth ladder.

**Psionic (#4):** forging produces a **new innate power** — the psion is *awakening* a latent ability, not learning one. The forging roll is WITS (or the psionic attribute); the "forging days" are meditation/trance. There is no grimoire and no teacher — a psion forges alone (the teacher/grimoire benefit does not apply). Reforging deepens the awakened power (more menu qualities). Because psionics is innate, a forged power cannot be taught — it is the psion's alone.

**Folk / Hedge (#5):** forging is **slower and lower-powered** — a folk spell is forged over a season of practice, not days, and the menu is capped at low-rank qualities (no epic-tier entries). The forging roll uses the folk-craft skill (Survival, LORE, a tradition skill) **modified by community Standing** (`08` #5): forging *for* the community (a charm to ward the village) grants a bonus; forging *against* the community's values (a curse) inflicts a Standing penalty and risks the folk-mage being shunned. A forged folk spell is taught by demonstration within the community (the teacher benefit is replaced by "apprentice in the village").

**Pact / Summoning (#6):** forging a new pact-boon requires **the patron's involvement** — the forging days are ritual invocations, and each forging roll is made at a penalty if the **Pact Debt** (`08` #6) is high (the patron is wroth). The finished spell is a new boon the patron grants — but it raises the Debt by its rank (the bargain deepens). A forged pact-boon can be **revoked** by the patron (on breach or a called debt refused) — unlike other archetypes, the forged spell is not permanently the caster's; it is *on loan*. Reforging a pact-boon deepens the Debt further still.

**Divine / Faith (#7):** forging a new divine spell requires **Devotion ≥ the spell's rank + 1** (`08` #7) — the caster must be *especially* faithful to be entrusted with a new gift. The forging days are prayer and acts of devotion; the forging roll is the faith attribute + the religious skill. The finished spell is granted by the deity and gated by Devotion thereafter (castable only while Devotion ≥ rank). A forged divine spell can be **lost** if Devotion drops below its rank and is not restored — atonement restores access, not the spell itself (the spell remains, but is withheld).

**Verb-Noun / Free-form (#8):** forging does not produce a *spell* — it produces a **new verb or noun rating**, or a new **rote** (a pre-statted combination). Forging a new verb/noun is forging a *technique*, not an effect: the caster spends the forging project to gain "Create 2" or "Fire 3" as a rated art. The Success Menu here buys the art's scope (what combinations it enables). Alternatively, forging a **rote** codifies a common verb+noun combination into a quick-cast spell (so the mage doesn't re-improvise it each time) — the rote's menu qualities are its fixed choices. The 10-check for a rote is lighter (it's a shortcut, not a new power); for a new verb/noun it is full.

**Item / Relic (#9):** forging is **attunement** — the caster is unlocking a new tag on an advancing relic (`08` #9), not creating a standalone spell. The forging days are rituals of investment in the relic; the forging roll uses the attunement skill + the relic's bond rating. The finished "spell" is a new relic function (a tag). Reforging a relic adds more tags — and raises the relic's **upkeep** cost (it demands more to maintain, like an org growing functions, `07 §3`). A relic-tag forged via this procedure is subject to the full 10-check (relics that do too much are the "über-item" failure mode).

**Blood / Sacrifice (#10):** forging a blood-magic spell means **paying the forging cost in blood**, not just time — each forging day deals 1 attribute damage to the caster (the research itself bleeds them). The forging roll is WITS, but pushed rolls cost *double* damage (blood magic is hungry). A forged blood-spell's menu can include a **sacrifice-scaling** quality (the spell reaches further when fed a greater sacrifice). Forging a blood-spell risks **Corruption** (`workshop/07`) — each forging project may step the Corruption die.

**Rune / Glyph (#11):** forging produces a **new rune design** (a codified inscription), not a cast spell. The forging days are spent *inscribing and testing* the rune on practice surfaces; the forging roll is the inscription craft skill. The finished rune is a design the caster can thereafter *inscribe* (in downtime, per `08` #11) and *trigger* (in combat). The Success Menu buys the rune's qualities (trigger condition, area, duration, reusability). The **Inscription Check** (10-check #9) is non-negotiable for runes — a rune is, by definition, an autonomous trigger, so it must pass that check or be rejected.

**Channeling / Possession (#12):** forging is **negotiating a new pact-term with the rider** — the caster is expanding what a channeled spirit is permitted to do while riding. The forging days are trance-sessions with the rider; the "forging roll" is rolled *by the GM* (the rider's will, per `08` #12), not the caster. The finished "spell" is a new clause in the channeling pact (the rider may now also heal, or also speak in tongues). Reforging deepens the pact — and raises the **possession risk** (the rider is more entrenched, harder to exorcise). The 10-check's Keeper Veto is especially load-bearing here: if the rider's new permission has no fair counterplay, the forging fails — the rider demands too much.

*Across all twelve: the Success Menu (spend surplus ⚔ on qualities), the forging-cost-by-rank table, and the 10-check are constant. What varies is the fiction of the forging (study vs. trance vs. bleeding), the roll's attribute/skill, and where the finished spell lives (tree, book, skill list, relic, pact, rune-design). This is the module's claim: **forging is archetype-agnostic** — the design procedure transplants to any of `08`'s systems.*

## 3. The pressure loop

- **Pressure:** forging consumes downtime (forging days the caster could spend on other projects, training, or recovery); pushing the forging roll costs body, Willpower, or Faith; a RISKY spell cannot be safe-cast; reforging escalates instability.
- **Decision:** *do I push this forging roll for more ⚔ (risk harm now) or accept a slower project? do I spend surplus on the qualities I want, or bank them via reforging for later? do I accept the RISKY tag to fit one more quality, or keep the spell safe-castable?*
- **Consequence:** a strong forging yields a rich spell; a weak one yields a narrow spell; a pushed-failed day costs body for no progress; a RISKY spell is forever unstable.
- **State change:** the caster's spellbook gains (or enriches) a power — a permanent, authored artifact of their downtime investment.
- **Loop shape:** **design (build menu) → forge (roll over days) → spend surplus (Success Menu) → balance-test → learn → (optionally) reforge later.** Runs at project cadence (days to weeks), not Round or session cadence — a *strategic-authorship* resource, parallel to the base-building loop (`07 §4`).

## 4. Choices

| Choice | Setting A | Setting B | Psychology produced |
| --- | --- | --- | --- |
| **Who sets the rank** | GM alone (FL default) | Player proposes, GM ratifies | Authority vs collaboration |
| **Menu pricing** | Fixed quality-cost table (this module) | GM judgement per spell (FL default) | Rules consistency vs bespoke nuance |
| **Forging roll** | Knowledge attribute + skill (P1 core roll) | Dedicated FORGING skill or talent | Integrated vs specialized |
| **Pushing the forging roll** | Allowed (binds invention to body) | Disallowed (forging is safe, just slow) | Gritty attrition vs relaxed authorship |
| **Surplus ⚔ spend timing** | At completion (accumulate, then spend) | Per-day (each day's surplus buys immediately) | Project-scale vs incremental authorship |
| **Reforging** | On (iterative authorship, RISKY escalates) | Off (one-shot forging, FL default) | Growth path vs fixed spells |
| **Teacher/grimoire benefit** | Double banked ⚔ | Halve forging days | Knowledge-economy emphasis |
| **Mishap layer** | On (P4 forging-mishap table on bad pushes) | Off (failure just banks nothing) | Specific-and-memorable failure vs forgiving |
| **RISKY tag availability** | GM may invoke freely | Player may opt-in (for a richer spell) | GM-controlled danger vs player-tempted danger |
| **Epic-tier forging** | Rank 5-6 uses epic-ingredient economy (`05 §9`) | Rank 5-6 just costs more forging days | World-changing gated by fiction vs by time |

**Calibration guidance:** start with GM-sets-rank, fixed quality-cost table, knowledge-attribute roll, pushing allowed, surplus-spend-at-completion, reforging **on** (it is this module's signature contribution), teacher-doubles-⚔, mishap **on** for gritty games / **off** for lighter ones. The RISKY tag and the 10-check are **non-negotiable** — they are the entire balance backstop. A game that drops them has lost the safety rails and should not allow player-authored spells at all.

## 5. Integration points

- **Hooks into:** `08-spell-systems.md` — this module sits *below* it: pick the archetype there, then forge spells here. The forging procedure is archetype-agnostic (§2d), but the finished spell's home (tree, book, skill, relic, pact, rune) depends on the chosen system. Hooks into the power layer (`05`) — a forged spell is cast through the normal casting-risk choice (safe/chance/overcharge), fueled by the core Willpower/Faith, and subject to the discipline's mishap table when cast. Hooks into progression (`02`) — learning a forged spell costs XP (rank + one Quarter Day of study, per `05 §8`) *after* the forging project completes; the forging produces the spell, the XP learns it. Hooks into travel/downtime (`06`) — a forging day is a Shift/Quarter Day and competes with other downtime activities (TRAIN, CRAFT, REST). Hooks into the harm layer (`04`) — pushed forging rolls damage attributes; forging mishaps roll on crit tables. Hooks into Corruption (`workshop/07`) — forbidden-domain spells gain Corruption tags, and reforging a forbidden spell can step the Corruption die.
- **Requires:** a power layer turned **on** (`05 §10`). Without powers, there is nothing to forge. Requires a defined knowledge attribute and (ideally) a LORE/casting skill. Requires the GM to run the 10-check.
- **Replaces / extends:** FL's forging appendix — this module generalizes it and wires it to the Success Menu. A game using FL's forging verbatim does not need this module; a game building its own power layer from `05` uses this to add player-authored spells safely.
- **Cross-refs:** `00 §4` (Success Menu — the spine); `05` (power layer — the host system); `16` P1/P3/P4/P6/P8 (the composed patterns); `17` (investment/authorship psychology); `13 §8` (review path); `19` FE1/FE4 (false-choice and agency-collapse — the two failures the menu + reforging are engineered against).

## 5a. Handshake

- **Prerequisites:** power layer, rank/scope scale, downtime cadence.
- **Inputs:** forging skill, project cadence, quality menu, mishap trigger, learning cost.
- **Outputs:** forged spell template, banked successes, quality costs, RISKY tag, reforging procedure.
- **Touched systems:** powers, progression, downtime, harm, corruption, crafting.
- **Replaces or stacks:** replaces freeform spell invention; stacks with `13-rituals-projects-and-research.md` only by treating spells as this module's special case.
- **Incompatibilities:** do not allow reforging plus uncapped empowerment plus no mishap; that creates signature-spell dominance.

## 6. Failure modes & edge cases

- **"The spell solves everything" (the One-Spell Problem, check 2).** If a forged spell is always the right answer, it makes every other spell wrong — the caster's loadout collapses to one über-tool. **Fix:** the 10-check's One-Spell Problem check is the explicit gate; if the spell answers too many situations, narrow its target, add a hard limit, or raise its rank. The quality-cost table's high prices for "second major effect" (3 ⚔ + rank raise) and "permanent" (3 ⚔ + RISKY) are the upfront brakes. (`19` FE1 — false choice: a spell that is always right is not a choice.)
- **"The spell is uncounterable" (the Keeper Veto, check 10).** A spell with no fair counterplay shuts down play — it does not *invite* a response, it ends the scene. **Fix:** the Keeper Veto is absolute — if the GM cannot imagine counterplay, the spell is not ready, full stop. This is the one check that cannot be bargained over. (`19` FE4 — agency collapse: a rule that removes the opponent from meaningful play.)
- **"Reforging makes an über-spell."** A caster who reforges the same spell every downtime accumulates qualities until it dominates. **Fix:** each reforging raises the RISKY threshold — a spell reforged 2-3 times cannot be safe-cast even well below rank, making it unreliable precisely when the caster needs it most. The RISKY escalation is the brake that forces diversification. (Cross-ref `13 §5.5` — action-budget abuse variant; `workshop/07` — the doom-spiral pattern applied to accumulation.)
- **"The player out-argues the GM on rank/menu pricing."** If the GM is the sole balance authority with no rubric, forging becomes a social negotiation the player can win. **Fix:** the quality-cost table and the benchmark tables make pricing *rules* — the GM points at the table, not at their own judgement. The 10-check is the backstop; the Keeper Veto is final. (`19` FE5 — "too unfair" — but here the unfairness is *prevented* by the rubric.)
- **"Forging is too slow to ever matter."** At 5-30 forging days, a spell can take a season to design — too slow for a fast-paced campaign. **Fix:** the teacher/grimoire benefit (double banked ⚔) halves effective time; a dedicated FORGING talent can add dice; the GM may compress forging days to "one per session" rather than one per Shift. The choice is explicit (§4). Do *not* solve this by lowering the forging cost — that breaks the investment psychology.
- **"A RISKY spell is just better."** If RISKY only removes safe-casting (one of three casting models), a caster who never safe-casts anyway pays nothing. **Fix:** RISKY should also *raise the effective mishap rate* — treat a RISKY spell as one rank higher for mishap-table modifier purposes (more 💀 push the roll further up the table, `05 §7`). This makes RISKY a real cost for overcharge-casters, not just safe-casters.
- **"Permanent effects stack infinitely."** A permanent-buff spell cast on every ally, every session, breaks the game. **Fix:** the Permanence Check (check 7) requires a hard cap on recasting — "once per target, ever" is the default. Permanent effects are also gated by the 3-⚔ menu cost + RISKY tag, making them rare by construction.
- **"Inscription makes the spell autonomous."** A forged spell inscribed as a ward (delayed-trigger quality) fires without the caster present — potentially abuseable (area damage on a tripwire, permanent effects on a threshold). **Fix:** the Inscription Check (check 9) — area damage, Corruption generation, and permanent effects are *not eligible* for inscription unless the GM adds severe limits. The delayed-trigger quality costs 2 ⚔ *and* must pass check 9.

## 7. Check notes

- **Math (`13 §3` / `§8` Stage 1):** a rank-3 spell costs 15 ⚔ over 15 forging days. A caster rolling WITS 4 + LORE 3 = 7 dice expects ~1.17 ⚔/day (7/6), so ~13 days to bank 15 — roughly on schedule, with variance. A teacher doubles this to ~6-7 days. Pushing adds ~0.2-0.5 ⚔/day at the cost of attribute damage. The forging-cost table is calibrated so a rank-appropriate caster finishes a same-rank spell in roughly the FL-benchmarked time (5 days × rank). If spells forge too fast, raise the cost or the difficulty; if too slow, add the teacher benefit or a FORGING talent.
- **Abuses (`13 §5` / Stage 2):** the One-Spell Problem (check 2) and the Stack Check (check 6) are the main abuse gates — both are explicit in the 10-check. The reforging-RISKY escalation gates accumulation. The Permanence Check gates infinite stacking. The Inscription Check gates autonomous triggers. Verify a forged spell cannot be empowered (check 8) into a higher-rank effect without a cap.
- **Synergy (`13 §7` / Stage 3):** the module hooks cleanly because it reuses P1/P3/P4/P6/P8 and the Success Menu — no new dice type, no parallel economy. The one synergy to watch: a forged spell that interacts with the Corruption spiral (`workshop/07`) can gain a Corruption tag that refuels the caster on cast — recompute the doom curve if a forbidden-domain forged spell is also a frequent-cast workhorse.
- **Felt experience (`19` §7 Stage C):** the **Success Menu** is the key psychology — it converts "the GM gives me a spell" into "the dice decided how much of *my* spell I got," which defeats FE1 (false choice) and FE4 (agency collapse) simultaneously: the player authored the intent, the dice arbitrated the result, the GM ratified it. The **reforging** valve preserves C3 (flow channel) — a weak first forging is not a dead end; the caster can enrich the spell later. The **RISKY tag** and the **10-check** are the anti-FE5 ("too unfair") backstop — they ensure player-authored power does not break the table's trust. The forging-mishap table should be telegraphed (C2 perceived randomness): the GM foreshadows that a push is risky before the roll, so a mishap feels *earned*, not random.

## 8. Worked genre example — High fantasy (forbidden sorcery)

**The setting:** a high-fantasy kingdom where the approved spell lists are curated by the Arcane Collegium, but a caster with a teacher (or a stolen grimoire) can forge their own. The power layer is at **High density** (`05 §10`): all three tiers (Spells / Power Words / Rituals), all three casting models, Burn, per-discipline mishap families, a rank-6 ladder, and the epic-ingredient economy. Corruption (`workshop/07`) is in play for forbidden disciplines.

**Settings chosen:** GM-sets-rank (player proposes); fixed quality-cost table; WITS + the discipline's talent for the forging roll; pushing allowed (binds invention to body); surplus-spend-at-completion; reforging **on**; teacher/grimoire doubles banked ⚔; forging-mishap **on** (P4, Procedural family); RISKY tag available (GM-invoked and player-opt-in); epic-tier forging uses epic ingredients at rank 5-6.

**The caster:** Rowan, a sorcerer with the Elemental Fire discipline at rank 3. She wants a signature spell the Collegium never approved — a precision flame that burns *only what she names*, leaving allies and surroundings untouched. She has a teacher (her mentor, exiled for heretical research) and a grimoire (the mentor's notes).

**The design phase:**

1. **Major effect:** a ranged flame that damages a single named target, ignoring all others in the area.
2. **Scope benchmark:** single-target damage at range with a control twist (the "ignore others" is a control feature). Rank 3 (strong — "shifts a battle, multi-target strikes" inverted: a *precise* strike). GM sets **rank 3**.
3. **Type tag:** STANDARD (slow action) — this is a workhorse attack spell, not a reactive defense or a ritual.
4. **Player's desired qualities:** (a) ignore non-targets in the area (the signature feature — this is *the point* of the spell); (b) +1 die of damage per PL; (c) no ingredient (cast from WP alone); (d) burns hotter on a critical (extra damage on 3+ net ⚔).
5. **GM prices each quality:** (a) "ignore non-targets" = 2 ⚔ (a strong control feature — effectively selective area damage, above the rank-3 single-target baseline); (b) "+1 die/PL damage" = 1 ⚔ (standard damage scaling); (c) "no ingredient" = 2 ⚔ (removes a scarcity gate); (d) "critical burns hotter" = 1 ⚔ (a narrow conditional bonus). Total menu cost: **6 ⚔** of surplus beyond the forging cost.
6. **Forging cost:** rank 3 = **15 ⚔**. So Rowan needs to bank 15 to learn the spell at baseline, then 6 more to buy all four qualities = **21 ⚔ total** for the full spell.
7. **Risk principle:** the "ignore non-targets" feature is bold for rank 3 (it is effectively a free selective-area tag). The GM judges it within scope *if* the spell is single-target only (no area scaling). The "no ingredient" quality (c) removes a gate. Together, these push the spell toward RISKY — the GM tags it **RISKY**: it can never be safe-cast, no matter how far below Rowan's rank. Rowan accepts (she never safe-casts anyway — she overcharges for scale). The spell is *not* raised to rank 4 because the major effect (single-target precision flame) fits rank 3's scope.
8. **Forging brief written:** rank 3, STANDARD, RISKY. Major effect: precision flame, single named target. Forging cost 15; menu (6 ⚔): selective (2) + damage scaling (1) + no ingredient (2) + critical-burns-hotter (1).

**The forging phase:**

- Rowan has a teacher and a grimoire, so each forging day banks **double** ⚔. She rolls WITS 4 + Elemental Fire 3 = 7 dice, difficulty Average (0). Over 11 forging days (she needs ~21 ⚔; at ~1.17 ⚔/day doubled to ~2.34/day, that is ~9 days; she takes 11 with variance), she banks the 15 baseline + 6 surplus = **21 ⚔**. She pushes two of those rolls for extra ⚔, taking 2 Strength damage total (which she heals at MAKE CAMP) — binding the invention to her body, as the loop intends.
- **At completion:** the 15 ⚔ learns the spell at baseline (precision flame, single target, rank 3, RISKY). The 6 surplus ⚔ are spent on the menu: selective (2) + damage scaling (1) + no ingredient (2) + critical-burns-hotter (1). All four qualities purchased.

**The 10-check (run before play):**

1. **Peer Comparison:** compared to FIREBALL (rank 3, area, ignores no one) and other rank-3 Elemental spells, Rowan's spell trades area for precision — it is stronger on one axis (selectivity) but weaker on another (no zone damage). Passes.
2. **One-Spell Problem:** it is a single-target attack spell — it does not replace healing, movement, defense, or utility. Passes.
3. **Risk vs Reward:** the RISKY tag is the cost — it can never be safe-cast. Passes.
4. **Casting Pressure:** at minimum PL (1), it deals 1 damage to one target, selectively. Narrow but useful. At typical PL (3), it deals 3 damage to one target ignoring allies — strong but not rank-4 (no zone, no transform). Passes.
5. **Duration Stress:** Immediate. Passes (no duration to stress).
6. **Stack Check:** best case = overcharge to 5-6 PL + Empower Spell (metamagic) doubling to 10+ PL → 10 damage to one target. High, but single-target only — checked against the Empower check below.
7. **Permanence Check:** not permanent. Passes.
8. **Empower Check:** at doubled PL, the spell deals double damage to one target — lethal, but still single-target. The GM caps PL scaling at 6 (no external amplifiers beyond Empower Spell's single application) to prevent rank-4-level single-target damage. Noted in the spell entry.
9. **Inscription Check:** the spell has no delayed-trigger quality — it cannot be inscribed as a ward. Passes.
10. **Keeper Veto:** the GM can imagine counterplay (cover, range, resistance rolls, counterspelling, killing the caster before she casts). Passes.

**The finished spell (written in the template):**

```
#### ROWAN'S NAMED FLAME

✦ RANK 3, RISKY
✦ RANGE: Long
✦ DURATION: Immediate
✦ INGREDIENT: None

You hurl a thread of flame that burns only the target you name. The
target suffers damage equal to the Power Level; for each additional PL,
add one die of damage. No other creature or object in the area is
harmed — the flame knows its name. On a critical casting (3+ net ⚔),
the flame burns hotter: +2 damage. This spell is RISKY and can never
be safe-cast. Its Power Level cannot be amplified by more than one
external effect (e.g. Empower Spell, once).
```

**Later — reforging:** at rank 4, Rowan reforges NAMED FLAME to add a second target (1 ⚔ on the menu, reforging cost = half of 15 = 8 ⚔, ~4 forging days with her teacher). The reforging raises the RISKY threshold — NAMED FLAME is now RISKY *and* treated as rank 4 for mishap-table purposes (more 💀 push the mishap roll further up the table). She has a richer signature spell, but it is correspondingly more unstable — the trade the module is designed to force.

**Why this works in high fantasy:** the Success Menu makes Rowan a *designer* of her magic, not a shopper — the spell is hers because she named its qualities and the dice decided how many she got. The RISKY tag and the 10-check make her authorship *safe for the table* — the GM ratified the result against benchmarks, not by fiat. The reforging valve lets NAMED FLAME grow with Rowan across the campaign, becoming her signature without ever being free. And because forging binds to the body (pushed rolls damage attributes) and to the risk loop (a RISKY spell cannot be safe-cast), the invented power sits *inside* the engine's pressure economy — it is not a free gift, it is an investment paid for in downtime, body, and permanent instability.

**Re-skin for your genre:**

- **Sword & sorcery (medium density):** drop the epic tier; forging caps at rank 5; reforging is rarer (requires a master teacher). The RISKY tag carries social weight — a RISKY spell is marked as heretical.
- **Psi / gadgets (low density):** a "spell" is a psionic knack or a prototype device; the "teacher" is a lab or a mentor; the "ingredient" is a component or a focus; reforging is "iterating the prototype." The 10-check becomes a usability/safety test.
- **Cosmic horror:** forging a new ritual *always* gains a Corruption tag (`workshop/07`); the forging-mishap table's 65/66 rows feed the doom spiral. Invention of forbidden rites is the surest path to transformation.
- **Urban fantasy / modern occult:** the Collegium is a secret society or a corporate R&D division; the grimoire is a leaked manuscript or a dark-web archive; the forging days are late nights in the lab/library. The RISKY tag means the spell is unstable tech the authorities would confiscate.
