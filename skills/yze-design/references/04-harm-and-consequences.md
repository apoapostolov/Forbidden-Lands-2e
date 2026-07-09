<!-- markdownlint-disable MD013 MD024 MD041 MD060 -->

# Harm and Consequences — Damage, Injury, Environment

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the consequences layer — it assumes the damage-generation side of conflict (`03-conflict-and-combat.md`) and the Willpower/Faith/push loop (`00-engine-core.md`). The central deliverable is the **Critical-Injury Table Engine** (§5), a reusable D66 architecture that recurs in magic mishaps (`05-power-layer.md`).

## Contents

1. Source provenance
2. Abstraction target
3. Attribute damage and Broken
4. Coup de grâce and the merciful-killing test
5. The Critical-Injury table engine (D66 location × severity) — **the central reusable artifact**
6. Conditions (starve / dehydrate / exhaust / freeze / heat / addicted)
7. Environmental harm (fire / blast / fall / drown / poison / disease / darkness)
8. Stabilization and death rolls
9. Healing and recovery
10. Permanent injury and retirement ("When the Road Ends")
11. Divergence rows (FL vs West)
12. Rule Choices and Build Recipe
13. Design intent

## 1. Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/06-critical-injuries.md:1-523` — Critical Injuries overview, Death, Healing, Permanent Injuries (`65`/`66` resolution), Non-Typical Damage routing, "When the Road Ends" (retirement), Broken, Broken NPCs, Pushed Damage (no crit on self-break), Conditions (Hungry/Thirsty/Sleepy/Cold/Addicted), Fear, Darkness, Falling, Drowning, Poison (Potency by opposed roll; Lethal/Paralyzing/Sleeping/Hallucinogenic; weapon-coating), Disease (Virulence; daily sickness rolls; cumulative −1; medical aid), Riding Animals; seven critical-injury table families: **Slash** (`:188-233`), **Blunt Force** (`:235-280`), **Stab** (`:282-325`), **Burn** (`:327-382`), **Acid/Corrosion** (`:384-415`), **Cold/Freeze** (`:417-448`), **Swallow** (`:450-481`), plus **Horror** (`:483-523`) — each physical family carries a temporary table *and* a Permanent Injuries table.

**Tales of the Old West 2E (West):**
- `01-corebook/05-conflict-and-damage.md:439-688` — Getting Hurt and Getting Broken (Hurts→Grit, Shakes→Quick, Doubts→Docity, Vexes→Cunning; split-damage rule), Coup de Grace (Docity test, 1 Doubts cost), Recovering Lost Attribute Points (1/Turn), Getting Back Up (Doctorin'), Critical Injuries (Crit-Rating-via-stunts *and* Broken-takes-damage triggers), the single master **Critical Injury Table** (`:521-560`, D66, Tens=location, Units=severity), Stunned, Stabilization & Death Rolls (Fatal injuries; un-pushable RESILIENCE Death roll; Instant Death), Healing Critical Injuries, Conditions (Starving/Dehydrated/Exhausted/Freezing/Heatstroke), Fire (Intensity), Dynamite and Explosions (Blast Power; Desperate handling), Falling, Falling from your Horse, Drowning, Venom and Poison (Potency 1–3; Lethal/Paralyzing/Sleeping/Hallucinogenic), Disease (Virulence 1–3; named diseases), Darkness.

## 2. Abstraction target

Abstract **harm** as a genre-neutral *layered cascade*. Damage is not a single HP pool — it flows through discrete layers, each of which is a separable design choice:

1. **Attribute damage → Broken** (the immediate-crisis layer): harm maps to a named attribute; at 0 the actor is Broken.
2. **Critical-Injury Table Engine** (the lasting-consequence layer): a D66 lookup producing location × severity, immediate + long-term effects, healing time, and lethality. **This is the engine's signature reusable artifact** — identical architecture in both games.
3. **Conditions** (the attrition layer): deprivation states that block recovery and deal slow damage.
4. **Environmental hazards** (the world-pressure layer): fire/fall/drown/poison/disease/darkness, each a *rated* pressure (Intensity/Potency/Virulence/Blast Power).
5. **Stabilization & death rolls** (the threshold layer): what stands between Broken and dead.
6. **Healing & recovery** (the bounce-back layer): how attributes and injuries regenerate.
7. **Permanent injury & retirement** (the long-arc layer): the graceful exit when a PC becomes unplayable.

Both books converge remarkably across all seven layers. The one structural divergence is the *shape* of the critical-injury layer: FL generalizes it into a **family of typed tables** (one D66 family per damage *type* the genre cares about), while West uses a **single master table** indexed by body location. Generalizing "typed critical-injury families" is this file's key deliverable (§5), and the same pattern recurs in magic mishaps (`05-power-layer.md` §5).

## 3. Attribute damage and Broken

**Source instance (FL):** Damage is dealt in **🩸** to a specific attribute. The damage source names the attribute it hits (a sword cuts Strength; a fear attack drains Wits; horror drains Empathy). When an attribute reaches **0**, the character is **Broken** — helpless and out of action until they recover ≥1 point. FL `06-critical-injuries.md:5, 41-57`. Strength-Broken or Wits-Broken is especially dangerous because it routes to the lethal critical-injury tables (`:5`). FL is explicit that **pushing yourself into Broken does NOT trigger a critical injury** — you can never kill yourself by pushing a roll. FL `06-critical-injuries.md:47-49`.

**Source instance (West):** Damage is *split* across a paired attribute, point-for-point, with a fixed alternation: physical damage is **Hurts→Grit then Shakes→Quick, Shakes first**; mental damage is **Doubts→Docity then Vexes→Cunning, Doubts first**. West `05-conflict-and-damage.md:443`. When any attribute hits 0 you are Broken, with a *flavored* helplessness per attribute: Grit-Broken = collapse/unconscious; Quick-Broken = too drained to act; Cunning-Broken = violent outburst or sullen withdrawal; Docity-Broken = panic/despair/meek compliance (can only flee or follow). West `:445-451`.

**Common pattern:** Harm reduces a **named attribute**; reaching zero in that attribute produces a state of **helplessness** (Broken) whose *fiction* is keyed to which attribute fell. There is no separate "HP" — the attribute *is* the HP for the kind of harm it absorbs. **Layer:** General.

**Health Tracks — the third mapping (engine-family pattern, not in FL or West core).** FL and West both use *small* attribute-tracks (typical 2–5 points each), which makes harm swingy: one or two good hits can Break an attribute, ending a fight fast. Other YZE-family games — notably **Coriolis** — use a different mapping that produces **larger, less swingy health pools** for heroic or pulp genres. Two constructions, combinable:

- **Combined-attribute track:** the health pool is the **sum of two attributes** (e.g. Strength + Agility). This roughly doubles the pool and smooths variance — a character is Broken only when the *combined* track hits zero, not when either attribute does. Coriolis applies this to its general damage track.
- **Flat-value bonus:** add a fixed number to an attribute to form the track (e.g. **5 + Strength**). The flat portion absorbs the swinginess of a low attribute, guaranteeing a survivable floor; the attribute portion still rewards high stats. This shifts the genre toward heroic survivability — the average pool roughly doubles, and a starting character cannot be one-shot by a single strong hit.

A health track may use **both** (combined + flat bonus) for the most heroic feel, or be an **external track not tied to an attribute at all** (a fixed pool per character, like D&D HP) — the extreme of the "less swingy" choice, at the cost of losing attribute-as-HP's *specificity* (a Strength hit and a Wits hit become fungible). **Layer:** Optional — adopt when the genre wants survivability and longer conflicts; omit (use pure attribute-as-HP) for gritty, swingy, lethal tone.

**Design intent:** Attribute-as-HP makes harm *specific* rather than abstract. A blow that Breaks your Strength tells a different story (you're bleeding out) than one that Breaks your Wits (you're mad with fear). This lets the damage type *select its own consequences* (see §5) and means different harm vectors threaten different parts of the character — a fear attack can't be "healed" with a bandage. The Health Track variant *trades specificity for survivability* — it is the choice a designer reaches for when the genre needs longer, less swingy conflicts (social combat, pulp action, boss fights) more than it needs the "which attribute fell?" story beat.

**Rule Choices & Build Recipe:**
- **Damage-to-attribute mapping** — *single-attribute-per-source* (FL: each source names its target attribute) / *paired-attribute split* (West: physical damage alternates Grit/Quick, mental alternates Docity/Cunning) / *combined-attribute health track* (Coriolis: sum of two attributes, e.g. Strength+Agility) / *flat-value track* (e.g. 5+Strength) / *external fixed pool* (attribute-agnostic HP). FL `06-critical-injuries.md`; West `:443`; Coriolis (engine-family). *Choose paired-split for two-axis attrition; choose single for clean consequence routing; choose combined/flat/external for larger, less swingy, more heroic pools. The further down this list, the longer a conflict takes to resolve and the lower the lethality.*
- **Broken flavor** — *one generic helplessness* (FL) vs *per-attribute helplessness fiction* (West `:445-451`). *The per-attribute flavor makes Broken a story beat, not just a number reaching zero. Note: combined/flat/external tracks lose per-attribute flavor by construction — if you adopt a health track, Broken becomes a single generic state unless you track which attribute the *last* point came from.*
- **Self-Broken safety** — FL exempts self-push-Broken from critical injury (`06-critical-injuries.md:47-49`); West has no equivalent carve-out because Broken routes through the master table on *subsequent* damage, not on the break itself. *Include the FL carve-out if you want pushing to be risky but not suicidal.*

## 4. Coup de grâce and the merciful-killing test

**Source instance (West):** A character Broken on Grit or Quick is defenseless and can be **finished with a coup de grâce** — but killing in cold blood costs something. To go through with it, the killer must **fail a Docity test**: roll dice equal to current Docity, *no ability applies, cannot be pushed*, and they must get **zero successes**. Any success means their conscience stops them. Regardless of outcome, the attempt inflicts **1 Doubts** just for trying. West `05-conflict-and-damage.md:453-455`.

**Source instance (FL):** No parallel "moral-cost test" for finishing a helpless foe in the harm chapter; a Broken foe is simply killable. The moral weight is instead distributed — the Horror table's `32 Honorable` result (FL `06-critical-injuries.md:500`) *removes* the willingness to perform a coup de grace as a lasting psychological injury, and the Cold-blooded talent is the opposite (the capacity to do it cleanly). So FL models mercy-cost as a *character trait / injury outcome*, not a per-act test.

**Common pattern:** A rule that **finishing a helpless foe is gated by a cost** — either a per-act moral test (must *fail* a conscience roll) or a character-capacity trait (you can't, unless trained/tainted). **Layer:** Optional (present in West as a test; in FL only as a trait/injury). Strongly recommended for any genre where killing should feel like it *costs the killer something*.

**Design intent:** The coup-de-grâce test prevents Broken from being a trivial "loot the body" state. It makes mercy and ruthlessness *asymmetric in the rules*: the merciful character keeps their Docity, the ruthless one pays Doubts each time. It also gives the *victim's* allies a reason to reach a Broken companion before the enemy resolves the kill.

**Rule Choices & Build Recipe:**
- **Gate type** — *per-act conscience test* (West: fail a no-ability, no-push roll) / *character trait* (FL: Cold-blooded talent allows it; Honorable injury forbids it) / *automatic* (no gate; Broken = dead on demand). West `:453-455`; FL `06-critical-injuries.md:500`.
- **Cost on attempt** — *always 1 Doubts whether or not you go through* (West `:455`) / *cost only on success* / *no cost*. *Always-pay makes even the attempt morally taxing.*
- **Test direction** — West's "must *fail* (zero successes)" is unusual and deliberate: high Docity makes you *less* able to kill, inverting the usual "good stat = good outcome." *Use the inverted test when conscience should be a brake, not a skill.*

## 5. The Critical-Injury table engine (D66 location × severity) — **the central reusable artifact**

This is the engine's signature consequence rule and the most directly portable artifact in the whole system. Both games use **the same D66 architecture**; they diverge only on *how many tables* and *how they're indexed*.

### 5.1 The shared D66 architecture

**Source instance (both):** When a critical injury is triggered, roll **D66** (two D6, one Tens, one Units). The result is read against a table whose rows are the 36 outcomes `11`–`66`. Each row carries a fixed column write-up:

| Column | Meaning |
| --- | --- |
| **D66** | The roll (`11`–`66`). |
| **Location / Injury name** | Where on the body and what it is. |
| **Lethal (Fatal)?** | Whether the injury can kill. |
| **Time limit** | How long until death if untreated (D6 rounds/Turns/hours/days). |
| **Immediate effect** | Penalty/condition suffered *now and until healed*. |
| **Long-term / permanent effect** | What lingers *after* healing time (often preventable by a healing roll). |
| **Healing time** | D6/2D6/3D6 days or weeks; or "Permanent." |

FL `06-critical-injuries.md:188-211` (Slash, canonical write-up); West `05-conflict-and-damage.md:521-560` (master table, columns: Roll / Location / Injury / Fatal / Healing Time / Immediate Effect / Long-term Effect).

**The Tens/Units encoding — the core trick:** In West the **Tens die = body location** (1=Lower Leg, 2=Upper Leg, 3=Arm, 4=Gut, 5=Chest, 6=Head) and the **Units die = severity** (low = minor, high = catastrophic), so the table is literally a *6×6 location×severity grid* read top-to-bottom, left-to-right. West `:476`. FL uses the same Tens/Units geometry but indexes by *wound kind* within each typed family rather than a single location axis. A **Called Shot** that produces a critical fixes the Tens (location) die and rolls only the Units die for severity — West `:478`; FL has no called-shot variant in the harm chapter.

**The `65` / `66` climax row:** Both engines reserve the top of the table for the worst outcomes. FL's rule is explicit and elegant: a **`65`** = "should kill you, but if someone saves you in time, roll on the matching **Permanent Injuries** table instead" — so `65` is the *maiming* threshold, survivable but scarring. A **`66`** = final, body destroyed beyond rescue ("Decapitation," "Crushed skull," "Burnt to a crisp"). FL `06-critical-injuries.md:22-27, 209-210, 256-257, 358-359`. West's master table has `66` as instant death ("Terrible hit to the head — You are very dead") and `65` as a survivable-but-grim throat wound; West `:559-560`. The `65`/`66` split is a **reusable lethality choice** (see §5.4).

**Two trigger paths (both):**
1. **Surplus-success / Crit-Rating path:** spend enough stunts/extra successes to buy a crit (West: each weapon has a **Crit Rating** = stunts needed; FL `03-skills.md` Stunts). West `:469`.
2. **Broken-takes-more-damage path:** a character already Broken who takes more damage to the Broken attribute auto-triggers a critical injury. West `:470`; FL routes Strength/Wits-Broken to the relevant table (`06-critical-injuries.md:5`).

**Common pattern:** a **D66 lookup** that converts "a really bad hit" into a *specific, named, narratively-loaded consequence* with a lethal flag, a countdown, an immediate penalty, a healing time, and a possible permanent effect. The table is the engine's *memory of harm* — it replaces generic HP loss with injury that *means something*. **Layer:** General (the architecture); the table *contents* are genre work (§5.4).

### 5.2 FL's innovation — the family of typed tables

**Source instance (FL):** FL does not have *a* critical-injury table. It has **eight**: Slash, Blunt Force, Stab, Burn, Acid/Corrosion, Cold/Freeze, Swallow, and Horror — one per *damage type the genre cares about*. When you're Broken, you roll on **the table matching the latest form of damage you suffered**: sword = Slash, club = Blunt Force, fire = Burn, acid = Acid, frostbite = Cold, swallowed by a beast = Swallow, fear/horror attack = Horror. FL `06-critical-injuries.md:5, 29-31, 188-523`. Each *physical* family is actually **two tables**: a temporary Critical Injuries table (the wound you're dying from) **and** a Permanent Injuries table (the scar you carry if you survive a `65`). FL `:212-233, 259-280, 304-325, 361-382, 402-415, 435-448, 468-481`. Horror is single-table (mental wounds scar differently — they *are* the permanent effect, with a healing time). FL `:483-523`.

**Why this is the key insight:** A *family of typed tables* makes the **set of damage types** a first-class design object. The genre *declares what kinds of harm matter* by giving each its own table. FL cares about edged weapons (Slash), piercing (Stab), blunt trauma (Blunt Force), fire (Burn), acid (Acid), cold (Cold), being eaten (Swallow), and madness (Horror) — that list *is* a portrait of the game's threats. A genre that doesn't care about being swallowed alive simply has no Swallow table; a genre that cares about radiation adds a Rad table. **The table family is a genre-commitment device.**

### 5.3 West's alternative — one master table indexed by location

**Source instance (West):** West uses a **single 36-row master table** indexed by body location (Tens) × severity (Units): 1x=Lower Leg, 2x=Upper Leg, 3x=Arm, 4x=Gut, 5x=Chest, 6x=Head. West `:521-560`. Special damage types (fire, cold, starvation) are *not* routed through this table at all — they bypass it and use their own dedicated rules ("For some special types of physical damage... the Critical Injury Table is not used"). West `:507`. So West's genre-commitment is encoded *differently*: weapon crits all hit the same anatomical table, while environmental harm gets bespoke mini-systems.

### 5.4 Generalizing "typed critical-injury families" — the recipe

> **This is the file's central reusable deliverable.** The recipe: *for each damage type your genre cares about, build a D66 family.* The architecture is fixed; the *set of families* is the genre choice.

**The fixed architecture (port as-is):**
1. **Roll D66.** Tens = one axis (location, or wound-site); Units = severity (low→high).
2. **36 rows, `11`–`66`.** Severity escalates down-and-right.
3. **Each row = name + lethal flag + time-limit + immediate effect + healing time + (optional) long-term effect.**
4. **Reserve `65` = maiming threshold** (survivable only via timely rescue → roll on Permanent table) and **`66` = final death** (body destroyed). This `65`/`66` split is the engine's reusable *lethality climax*.
5. **`11`–`~25` = cosmetic/minor** (no penalty or trivial); **`~31`–`~46` = debilitating but survivable** (penalties, slowed); **`51`+ = lethal** (countdown to death).

**The genre choice — choosing the family set:**
| Genre | Recommended typed families |
| --- | --- |
| **Dark fantasy / survival** (FL) | Slash, Stab, Blunt Force, Burn, Acid, Cold, Swallow, Horror — *8 families.* |
| **Historical Western** (West) | One master anatomical table + bespoke environmental rules — *1 family + environment bypass.* |
| **Sci-fi** | Ballistic, Energy, Vacuum/Cold, Radiation, Toxic/Chemical, Cyber-psych, Grav-Fall. |
| **Modern horror** | Slash, Bite, Burn, Toxic, Psychic/Horror, Disease. |
| **Pulp action** | Single master table (low lethality, fast resolution); reserve typed families for signature threats. |

**Building one family (work recipe):**
1. Name the damage type and the attribute it threatens (e.g., *Radiation → Vitality*).
2. Decide the table's *flavor*: what does this harm *look like* at minor, moderate, severe, lethal? Write 6 minor rows, ~12 moderate, ~12 severe, ~6 lethal.
3. Set healing times on a scale that matches the genre's pace (D6 days for gritty; D6 hours for pulp).
4. Populate the immediate effects with *specific, memorable* penalties (not "−1 to stuff") — "two-handed weapons cannot be used," "to RUN becomes a slow action," "disease with Virulence 6." FL's tables are the gold standard: every row is a *vignette*. FL `:188-233`.
5. Build the matching Permanent Injuries table (for survivors of `65`) if the genre wants lasting scars; omit it for pulp.
6. Decide the `66`: make it *final and evocative* ("Decapitation," "Burnt to a crisp," "Your head leaves your body").

**Cross-link — this pattern recurs in magic mishaps:** FL's per-discipline spell mishap tables use the identical "one typed table per thing that can go wrong" architecture. See `05-power-layer.md` §5 (mishaps). **Treat "typed D66 family" as a cross-cutting engine pattern:** anywhere the game needs *specific, memorable, genre-flavored* consequences for a *category* of bad outcome (combat harm, magic failure, social ruin, vehicle crash), build a typed D66 family. Flag in `14-recipes-new-game-new-rule.md`.

**Layer:** General (the D66 architecture + the `65`/`66` climax + the typed-family *pattern*); Situational (each specific family's contents are genre work); Optional (the Permanent Injuries sub-table — omit for low-lethality games).

## 6. Conditions (starve / dehydrate / exhaust / freeze / heat / addicted)

**Source instance (FL):** Five conditions — **Hungry, Thirsty, Sleepy, Cold, Addicted** — each a deprivation/addiction state that (a) **blocks recovery** of a specific attribute and (b) deals **slow attrition damage** to it. FL `06-critical-injuries.md:59-103`. Pattern: skip a daily need → after one day you gain the condition → you can't recover the tied attribute (except by magic) → you take periodic damage → if that attribute Breaks, you die after one more interval. Clearing the need clears the condition. FL also notes a condition can **Break** you directly (e.g. Thirsty-Broken), and in that case you do **not** roll a critical injury — the condition *is* the crisis. FL `:41-45`.

**Source instance (West):** Five conditions — **Starving, Dehydrated, Exhausted, Freezing, Heatstroke** — structurally identical to FL's, mapped onto the paired attributes (Starving→Grit, Dehydrated→all attributes, Exhausted→Docity/Cunning, Freezing→Grit/Cunning, Heatstroke→all). West `05-conflict-and-damage.md:509-597`. West adds the Freezing *interval ladder* (above freezing = roll/day; sub-zero = roll/Shift; extreme = roll/Turn) and a Heatstroke rule that **imposes Trouble on all rolls** (not just pushed) — tying conditions to the failure-pressure layer. West `:589, 594`.

**Common pattern — the deprivation layer:** a set of states, each defined by (1) a **trigger** (skip a need for one interval), (2) a **recovery block** (can't heal attribute X), (3) an **attrition tick** (lose N to attribute X per interval), (4) a **lethal breakpoint** (if X Breaks, death after one more interval), and (5) a **clear condition** (resume the need). **Layer:** General (the pattern); the *specific conditions* are genre work (FL's Addicted has no West equivalent; West's Heatstroke has no FL equivalent). Tie to `06-travel-and-downtime.md` (conditions are primarily a *travel* pressure).

**Design intent:** Conditions are the engine's **slow clock**. Where combat damage is acute, conditions are *chronic* — they make the passage of time itself a threat. They also make **basic survival logistics** (food, water, sleep, shelter, warmth) load-bearing in the rules, which is why they cluster in the travel chapter. The recovery-block is the cruel part: you can't heal *while* starving, so deprivation compounds rather than merely wounds.

**Rule Choices & Build Recipe:**
| Choice | FL | West | Choice |
| --- | --- | --- | --- |
| **Condition set** | Hungry, Thirsty, Sleepy, Cold, Addicted | Starving, Dehydrated, Exhausted, Freezing, Heatstroke | Pick the 4–6 deprivations your setting's *travel* threatens. |
| **Recovery block scope** | One attribute each (Strength / all / Wits / Str+Wits / Empathy) | Mapped to paired attrs (Grit / all / Docity+Cunning / Grit+Cunning / all) | Single-attr = clean routing to crit tables; paired = attritional spread. |
| **Lethal breakpoint** | Die after one more interval when tied attr Breaks | Make a Death roll, then repeat per interval | FL = deterministic grimness; West = a fighting chance each interval. |
| **Interaction with failure layer** | (none direct) | Heatstroke imposes Trouble on *all* rolls | Borrow the West trick to make a condition *feel* debilitating at the dice. |
| **Interval granularity** | Endurance rolls at GM-set frequency (winter = hourly) | Ladder: day/Shift/Turn by severity | Use a ladder when you want cold/heat to *escalate in the rules. |

## 7. Environmental harm (fire / blast / fall / drown / poison / disease / darkness)

Both games treat environmental hazards as **rated pressures** — each hazard has a single numeric rating that drives an opposed or flat roll, and damage scales with successes. The *rating* is the reusable abstraction; the specific hazard is genre build.

### 7.1 Fire — Intensity
**FL:** not given a standalone Intensity rule in the harm chapter; fire routes through the **Burn critical-injury table** when Broken. FL `06-critical-injuries.md:29, 327-359`.
**West:** Fire is measured in **Intensity** (typical bonfire = 8). Exposed: roll Intensity dice, each success = 1 damage. If damaged, you **catch fire**: another Intensity attack each Round, Intensity +1/round, until an attack deals 0 damage (fire out) or a MOVE roll (slow action) puts it out. Fire-Broken = Death roll every Round until saved. West `:599-603`.
**Generic:** a hazard with an **Intensity rating** = dice pool; successes = damage; an *escalating* feedback loop (catches → recurs → grows) until actively extinguished. **Layer:** General (the rated-pressure model); the escalation loop is Optional (omit for one-shot hazards).

### 7.2 Explosions — Blast Power (West only)
**West:** Explosions measured in **Blast Power** (1 stick dynamite = 8; 2–3 = 12; bundle = 16). For each victim in Short range, roll Blast Power dice; success = 1 damage (Arm's-Length = 2/success). Cannot push. Blast Power ≥7 reaches Medium range at −6. Dynamite *handling* is always **Desperate** (Trouble even un-pushed) unless you have the miner talent. West `:605-615`.
**Generic:** a **Blast Power** rating = pool rolled *per victim*; point-blank doubles; falloff with range; handling the device carries its own failure pressure. **Layer:** Situational (genre-dependent — only where explosions exist).

### 7.3 Falling
**FL:** 0.5 damage/meter (round up). Reduce by MOVE successes, −1 more for a controlled jump (fast action). May take −2 on MOVE to try to land standing (only if no crit). Metal armor gives no protection. FL `:118-119`.
**West:** damage = height(m) ÷ 2 (round down). Controlled jump: MOVE roll, each success −1 damage. GM may call a crit. Falling from a horse = 8-dice attack (damage 1, Crit 2), halved by a MOVE roll. West `:617-623`.
**Generic:** fall damage = **linear in height**; mitigated by a movement/agility roll; optional crit trigger. **Layer:** General. Both converge on height÷2; the horse-fall-as-attack is a nice West build of "animal throws you = an attack."

### 7.4 Drowning
**FL:** Swim assumed. In water: ENDURANCE/Turn to stay afloat; if sunk, ENDURANCE/round to hold breath; fail = drown, 1 Strength damage/round; Broken-while-drowning = die in D6 minutes. FL `:115, 121-123`.
**West:** Swim assumed. LABOR/Turn to stay afloat (every Round in heavy clothes); fail = sink; RESILIENCE/round to hold breath; fail = drown, 1 Hurt/round; Broken = Death roll, then every 5 rounds, until DOCTORIN' revives. West `:625-627`.
**Generic:** three-stage pressure — **afloat check (per Turn) → breath-hold check (per round) → damage per round**, with a Broken-drowning death clock. **Layer:** General. The escalation from Turn→round cadence is the engine's "time is running out" tempo trick.

### 7.5 Poison / Venom — Potency
**FL:** Potency as an **opposed roll** — GM rolls Potency Base Dice vs your ENDURANCE. Win = full effect, lose = limited effect. Four types: **Lethal (Str), Paralyzing (Agi), Sleeping (Wits), Hallucinogenic (Emp)** — each deals 1 damage/round to its attribute until Broken (antidote halts). FL `:125-151`.
**West:** Potency **1–3** (rarely 4+). You roll RESILIENCE; need successes ≥ Potency. Fail = full, pass = limited. Same four types mapped to West's pairs: **Lethal (Hurts), Paralyzing (Shakes), Sleeping (Vexes), Hallucinogenic (Doubts)**. West `:629-665`.
**Generic — poison as a rated opposed/threshold pressure:** a poison has (1) a **Potency rating** (the dice or the threshold), (2) a **speed** (Round/Turn/Shift), (3) a **target attribute** per type, (4) **full vs limited effect** gated by a resist roll, (5) an **antidote/healing halt**. The *four-type families* (lethal/paralyzing/sleeping/hallucinogenic → body/agility/mind/soul) is itself reusable. **Layer:** General (the model + the four-type families).

### 7.6 Disease — Virulence
**FL:** Virulence (typical 3, higher exists). Opposed ENDURANCE vs Virulence to resist; fail = Sick. Next day: 1 damage to the disease's attribute (Str or Agi by nature); can't recover it while sick; daily sickness roll, each fail = +1 damage; recover after successes = Virulence (non-consecutive); each failed roll = cumulative −1 (min 1 die). Str-Broken-sick = die next day; Agi-Broken-sick = bedridden, fail = die. FL `:153-170`.
**West:** Virulence **1–3** (rarely 4+). Roll RESILIENCE, need successes ≥ Virulence. Fail = Sick: next day 1 Hurts + 1 Shakes; can't recover Grit/Quick; daily roll, fail = +1 each; Broken-on-Grit = immediate Death roll, then per day. Single success ends it. Named diseases (Cholera V2, Consumption V1/weekly, Smallpox V3, etc.). West `:667-680`.
**Generic — disease as a recovery race:** a disease has (1) **Virulence** (threshold or opposed pool), (2) a **primary attribute burden** (or paired, in West), (3) **daily sickness rolls** that deal damage on fail and need N cumulative successes to cure, (4) an optional **escalating penalty** (FL's cumulative −1) to model a worsening case, (5) a **lethal breakpoint** when the tied attribute Breaks. **Layer:** General. FL's cumulative-penalty is the more punishing model (death spiral); West's single-success-cures is more forgiving.

### 7.7 Darkness
**FL:** (rule truncated in source) — operating blind without light imposes penalties/limits actions. FL `:113-114`.
**West:** In total darkness, MOVE to run (fail ≥1 damage). Melee at Arm's Length OK but must HAWKEYE (free action) to locate first. Ranged: HAWKEYE to attempt, then −3, and range mods doubled. West `:682-688`.
**Generic — darkness as a sensory-deprivation pressure:** running/moving blind = damage risk; attacking blind = locate-first gate + severe penalty + range compression. **Layer:** Situational (only where light scarcity matters).

**Design intent (environmental harm, overall):** Every environmental hazard is a **number you can choice** (Intensity, Blast Power, Potency, Virulence, height, depth, darkness-level). This makes hazards *scalable and combinable* — a "Potency 6 venom in a Freezing storm" is two rated pressures stacking. The opposed/threshold resist roll means hazard damage is *earned through the dice*, not just declared, which keeps players engaged with the threat rather than passively taking damage. **Layer:** General (the rated-pressure model); specific hazards Situational.

## 8. Stabilization and death rolls

**Source instance (FL):** If a critical injury is **lethal**, someone must make a successful **healing** roll before the listed time limit or you die. Each healer rolls once. You may heal yourself after regaining ≥1 attribute point, at **−2**. A small number of injuries are **instant death** — no save. The countdown is the injury's *Time Limit* (D6 rounds/minutes/hours/days). FL `06-critical-injuries.md:7-13`.

**Source instance (West):** If a critical injury is **Fatal**, you must be **Stabilized** (a DOCTORIN' roll, sometimes with a severity modifier) or you die. Until Stabilized, each time the listed duration passes you make a **Death roll**: roll RESILIENCE using your **full Grit** (not current), **cannot push**. Fail = die; succeed = linger, roll again next interval. A few injuries are **Instant Death**. West `:499-503`. West cleanly separates the two healing jobs: one DOCTORIN' roll to **Stabilize** (save your life), another to **get you up** (restore points), optionally a third to **prevent the long-term effect**. West `:489`.

**Common pattern — the death threshold:** Lethal injuries start a **countdown** (the Time Limit). To survive, you need a **stabilization roll** from a healer (one attempt each; sometimes penalized by severity). If the countdown expires unstabilized, you're in **death-roll territory**: FL resolves it as "time's up, you die unless healed in time"; West adds an explicit **periodic un-pushable Death roll** that buys you another interval on a success. Instant-death results bypass all of this. **Layer:** General (the countdown + stabilization); the explicit periodic Death roll is Optional (West's model gives more dramatic "lingering" beats; FL's is cleaner/faster).

**Design intent:** The death threshold exists so that **Broken ≠ dead** — it creates a *rescue window* and a role for healers/doctors. The un-pushable Death roll (West) or the hard time limit (FL) means you can't Willpower/Faith your way out of a mortal wound; only another character's competence (or luck) saves you. This makes the party's medic load-bearing and gives every lethal hit a *ticking clock* the table can rally around.

**Rule Choices & Build Recipe:**
- **Death model** — *hard time limit* (FL: die when time's up unless healed) / *periodic death roll* (West: RESILIENCE/full-attribute, un-pushable, each interval). FL `:7-13`; West `:499-503`. *Use periodic rolls when you want the dying character's player to keep rolling (engagement); use the hard limit when you want urgency and GM pacing control.*
- **Stabilization gate** — *healing roll, one attempt each* (FL) / *DOCTORIN' roll with severity modifier* (West). *Severity modifiers make harder wounds harder to save.*
- **Self-heal penalty** — FL: −2 to heal yourself (`:9`). *Include if you want self-rescue to be desperate, not reliable.*

## 9. Healing and recovery

**Source instance (FL):** Attribute points recover via **rest** (see the travel/downtime recovery shifts, `06-travel-and-downtime.md`). Critical-injury **healing time** is per-row (D6/2D6/3D6 days, or Permanent). A successful **healing** roll during recovery **halves remaining healing time** (a fresh roll, distinct from any life-saving roll). You can recover all attribute points and *still* suffer a critical injury's effects. FL `06-critical-injuries.md:13-21`.

**Source instance (West):** Resting recovers **1 attribute point per Turn** (5–10 min); you choose the order across damaged attributes. The fastest way up from Broken is another's **DOCTORIN'** roll — recover points = successes rolled (one attempt each, further attempts no effect). Immediate crit effects heal only with time (expire at healing time); long-term effects are preventable by a DOCTORIN' roll *during* the healing time. West `:457-491`.

**Common pattern — the bounce-back layer:** Two recovery axes: **(a) attribute points** regenerate on a fixed cadence per rest unit (Turn/Shift/Quarter-Day), faster with a healer's roll; **(b) critical-injury effects** heal on the row's healing-time clock, accelerated by a healing roll, with long-term effects gated behind a preventive heal. Conditions block (a) until cleared (§6). **Layer:** General. Tie to `06-travel-and-downtime.md` (the rest cadence lives in the travel system) and `02-progression-and-xp.md` (training as recovery-adjacent downtime).

**Design intent:** Healing is deliberately **two-tracked and unequal**: attribute points bounce back fast (you're back in the fight soon), but *injury effects* linger on their own clock (the gut wound still hurts for 2D6 days even after your Strength returns). This is what makes critical injuries *matter* — they outlast the combat that caused them and bleed into the travel/downtime loop. The healer/doctor is the single biggest lever on both clocks.

**Rule Choices & Build Recipe:**
- **Attribute recovery cadence** — *1/Turn* (West, fast) / *per Quarter-Day or shift* (FL, slow, in travel). *Fast = action-game tempo; slow = survival attrition.*
- **Healer acceleration** — *halves remaining injury healing time* (FL) / *restores N attribute points = successes, one attempt* (West). FL `:17`; West `:463`. *Both make the medic valuable; FL's model is better for injury pacing, West's for combat re-entry.*
- **Long-term-effect prevention** — *DOCTORIN' during healing time prevents it* (West `:485`). *Include a preventive-heal window if you want permanent scars to be avoidable-but-costly rather than fated.*

## 10. Permanent injury and retirement ("When the Road Ends")

**Source instance (FL):** Two rule patterns. (a) **Permanent Injuries tables** — when a physical crit rolls **`65`** and someone saves you, you instead roll on the matching Permanent Injuries table; results range from "−1 to ENDURANCE" scarring to "Strength and Agility permanently reduced to 1; retirement is the default." FL `06-critical-injuries.md:22-27, 212-233, 259-280, 304-325, 361-382, 402-415, 435-448, 468-481`. (b) **"When the Road Ends"** — an explicit, *dignified* retirement path: when a survivor is too broken to adventure but still alive, the player may let them "step away from the danger without shame." They become a **follower/retainer NPC** (quartermaster, healer's hand, counselor) and keep earning 1 XP/session as a hireling, or are settled somewhere safe. "Such a one has not failed. They have survived." FL `:33-39`. Magic (Lucky rank 4, Physician rank 3, Mend Wounds, Regeneration) can downgrade a permanent injury — so even maiming is sometimes reversible with enough power and speed. FL `:27`.

**Source instance (West):** Permanent effects live in the master table's **Long-term Effect** column — preventable by a timely DOCTORIN' roll, otherwise permanent (limp, lost limb, blindness, vocal impairment, −1 to an ability). West `:521-560`. There is **no explicit retirement prose**: a permanently maimed PC is simply played with their lasting effects, or (by implication) replaced. The graceful-exit *beat* that FL makes explicit is left to the table in West.

**Common pattern — the graceful-exit layer:** When harm makes a PC **unplayable** (stats floor-capped, limb lost, mind gone), the system offers (1) a **permanent-injury resolution** (roll on a Permanent table instead of dying), and (2) a **retirement path** that converts the PC into an NPC asset rather than a dead sheet. The exit is framed as a *story beat and a survival*, not a failure. **Layer:** General (permanent-injury tables); the *retirement-as-NPC* path is Optional but **strongly recommended** — it preserves player investment and seeds the party with supporting cast.

**Design intent:** This layer exists to answer the hardest question in a lethal RPG: *what happens when a character is too broken to play but too loved to discard?* FL's answer is the genre's most graceful: the survivor doesn't "lose" — they *change role*. This (a) keeps the character in the fiction, (b) rewards the player's survival with continued relevance, and (c) gives the party a non-combat resource (a healer's hand, a counselor) that emerges *from loss*. The permanent-injury tables make maiming **specific and memorable** (a lost eye, a ruined liver) rather than a generic stat penalty — so the retired NPC *carries their story in their body*.

**Rule Choices & Build Recipe:**
- **Permanent-injury resolution** — *dedicated Permanent tables per family* (FL) / *Long-term Effect column on the master table, preventable by heal* (West). *Use dedicated tables when you want maiming to be a rich rule set; use the inline column when you want parsimony.*
- **Reversibility** — *high-tier magic/talent can downgrade* (FL: Lucky 4, Physician 3, Regeneration) / *preventable only during healing window, then fixed* (West). FL `:27`. *Reversibility ceiling = how forgiving your world is.*
- **Retirement path** — *explicit "become a retainer NPC, keep XP"* (FL) / *implicit* (West). *Include the explicit path; it's nearly free and transforms the experience of character loss.*

## 11. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Critical-injury architecture** | **Family of typed tables** (8 families: Slash/Blunt/Stab/Burn/Acid/Cold/Swallow/Horror) | **Single master table** indexed by location (Tens) × severity (Units) | Damage-type specificity vs anatomical parsimony | Typed families when the genre has *meaningfully different* harm types; master table when all weapon hits are basically "a wound somewhere" |
| **Damage→attribute mapping** | Single named attribute per source | Paired split (Hurts/Shakes; Doubts/Vexes), alternating | Clean routing vs two-axis attrition | Single when damage type must route to a table; split when physical/mental harm should spread across two stats |
| **Broken fiction** | Generic helplessness | Per-attribute helplessness flavor (collapse / drained / outburst / panic) | One state vs four story-beats | Per-attribute when Broken should be a narrative event, not just a number |
| **Permanent injury** | Dedicated Permanent table per family (on `65`) | Inline Long-term Effect column (preventable by heal) | Rich maiming rule set vs parsimony | Dedicated tables for survival/ horror; inline for action |
| **Death model** | Hard time limit (die when up unless healed) | Periodic un-pushable Death roll (full Grit) each interval | Urgency/pacing vs player engagement | Hard limit for GM-paced grit; death rolls to keep the dying player rolling |
| **Stabilization** | healing roll, one each, self at −2 | DOCTORIN' with severity modifier; separate stabilize/revive/prevent rolls | Simple vs layered healer roles | Layered (West) when the medic should have distinct jobs; simple (FL) for speed |
| **Conditions** | 5 (incl. Addicted); single-attr recovery block | 5 (incl. Heatstroke); paired-attr; Heatstroke imposes Trouble | Trait-flavored vs attritional-spread + dice-pressure | FL-style for clean routing; West-style (esp. Trouble-on-all-rolls) when conditions should *feel* bad at the dice |
| **Fire / explosion** | Fire routes to Burn crit table; no Blast rule | Intensity-escalating fire; Blast Power per victim | Narrative table vs rated-pressure engine | Rated pressures (West) when hazards should scale and combine; tables (FL) when outcomes should be specific |
| **Poison/disease resist** | Opposed roll (GM rolls Potency/Virulence) | Threshold (need successes ≥ rating) | Contest vs flat check | Opposed when the hazard should "fight back"; threshold for speed |
| **Disease cure** | N cumulative successes = Virulence (non-consecutive), cumulative −1/ fail | Single success ends it | Death-spiral grimness vs mercy | FL's for plague horror; West's for playable frontier medicine |
| **Self-Broken safety** | Pushing yourself Broken never crits | (no carve-out) | Push is risky-but-not-suicidal vs no special case | Include the FL carve-out to keep pushing brave |
| **Retirement path** | Explicit "retainer NPC, keep XP," dignified prose | Implicit | Story-beat exit vs table-decides | Always consider FL's explicit path; it's high-value, low-cost |
| **Called-shot crits** | (none in harm chapter) | Fix Tens (location), roll only Units for severity | — | Include when called shots should guarantee a hit *location* |

## 12. Rule Choices and Build Recipe

Each choice has FL and West as two calibrated points. To build the harm layer for a new game, set each choice — **in this order**, because earlier choices constrain later ones.

1. **Attribute-as-HP mapping** — single-attribute-per-source (FL) / paired split (West) / combined-attribute or flat-value health track (Coriolis-style, §3). *Sets how harm is recorded, how many "wound tracks" exist, and how swingy/lethal damage feels. Health tracks trade specificity for survivability.*
2. **Critical-injury architecture** — typed family set (FL) / single master table (West) / hybrid. ***The signature choice.*** *Decide which damage types your genre cares about — that list becomes your typed families (§5.4).*
3. **Table contents & lethality climax** — adopt the D66 architecture + `65`=maim / `66`=die split. *Port the architecture as-is; write genre-specific rows.*
4. **Permanent-injury layer** — dedicated Permanent tables (FL) / inline Long-term column (West) / none (pulp). *Decide whether survivors carry scars.*
5. **Death model** — hard time limit (FL) / periodic un-pushable Death roll (West). *Decides the rhythm of dying.*
6. **Stabilization** — single healing roll (FL) / layered DOCTORIN' jobs (West). *Decides the medic's role complexity.*
7. **Conditions set** — pick 4–6 deprivations your setting's *travel* threatens (food/water/sleep/warmth/heat/addiction). *Sets the slow clock.*
8. **Environmental hazards** — port the rated-pressure model (Intensity/Potency/Virulence/Blast Power) and decide which hazards exist. *Sets the world-pressure layer.*
9. **Healing cadence** — fast (1/Turn) / slow (per Quarter-Day in travel). *Sets the bounce-back tempo; tie to `06-travel-and-downtime.md`.*
10. **Retirement path** — explicit retainer-NPC exit (FL) / implicit. *Decides what happens when a PC is too broken to play.*

**Instantiation recipe (any genre):**
1. **List the harm types your genre cares about.** This list is your design commitment. (FL: edge/pierce/blunt/fire/acid/cold/swallow/madness. West: anatomical hits + fire/cold/starvation.) → becomes either typed families or confirms a single master table suffices.
2. **Set the attribute-as-HP mapping** (choice 1) — this determines how damage routes to consequences.
3. **Build the D66 architecture** (choice 2–3): port the write-up, set the `65`/`66` climax, write rows by severity tier. If typed families, build one per harm type from step 1.
4. **Decide permanence and death** (choices 4–5): how often do injuries scar, and how do people die?
5. **Wire the healer** (choice 6): what rolls save lives, restore points, prevent scars?
6. **Lay in the slow clock and world pressure** (choices 7–8): conditions + rated hazards.
7. **Set recovery tempo and the exit path** (choices 9–10): how fast do PCs bounce back, and what happens when they can't?
8. **Validate against the math** (see `13-balance-and-synergy.md`): expected damage per round, time-to-Broken, rescue-window length, condition attrition rate. Confirm the lethality climax (`65`/`66`) triggers at the intended frequency given your crit-trigger path (Crit Rating / Broken-takes-damage).

## 13. Design intent

The harm layer is engineered to make **damage stick in memory, not just on the sheet.** Specifically:

- **Attribute-as-HP** makes harm *specific* — a Strength wound and a Wits wound are different stories, route to different tables, and need different cures. There is no fungible "HP" to spend down.
- **The D66 critical-injury table is the engine's memory of harm.** It replaces generic point-loss with *named, narratively-loaded consequences* ("punctured lung," "severed foot," "gouged eye"). Every row is a vignette; players remember their characters' injuries for years. Generic HP loss is forgettable; *a severed hamstring is not.*
- **The `65`/`66` climax** makes the top of every table a *genre moment* — the maiming threshold and the final death are the two outcomes the whole table leans forward for. Reserving them makes the dice roll *dramatic*.
- **The typed-family pattern (FL's innovation)** turns "what kinds of harm matter?" into a first-class design decision. The set of tables *is* a portrait of the genre's threats — and the pattern is reusable for any category of bad outcome (magic mishaps, social ruin, vehicle crashes). See §5.4 and `05-power-layer.md`.
- **Conditions are the slow clock** that makes the *passage of time* a threat, tying harm to the travel loop (`06-travel-and-downtime.md`) and making survival logistics load-bearing.
- **Rated environmental hazards** (Intensity/Potency/Virulence/Blast Power) make the world *scalable and combinable* — pressures stack, and damage is earned through resist rolls, not declared.
- **The death threshold + stabilization window** keeps Broken ≠ dead, creates a ticking clock the party rallies around, and makes the medic load-bearing. The un-pushable death roll (West) or hard time limit (FL) ensures Willpower/Faith can't cheat a mortal wound — only competence or luck saves you.
- **The graceful-exit / retirement path** answers the hardest question in a lethal game — *what happens when a PC is too broken to play but too loved to discard?* — by converting loss into a story beat and a party asset. "Such a one has not failed. They have survived." FL `06-critical-injuries.md:37`.

The divergence between FL and West is the engine's proof that **the same D66 architecture supports opposite tones by changing the table's *shape***: FL's eight typed families produce a game where *the kind of wound is the story*; West's single anatomical master table produces a game where *where you got hit is the story*. A new genre's job is to decide *what about a wound its players should remember* — and build the table family that makes that legible.
