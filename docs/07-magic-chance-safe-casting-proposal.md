<!-- markdownlint-disable MD013 -->

# Draft Proposal: Speak to the Wind and Casting-Mode Spell Ribbons

## Status

**Implemented in `01-corebook/07-magic.md`.** This document is retained as the design record for the casting-mode procedure. The complete spell-by-spell allocation is recorded in `01-corebook/07-magic-ribbon-audit-proposal.md`; the corebook chapter is authoritative where its final wording differs from this proposal.

This proposal has two parts:

1. add the Awareness spell **Speak to the Wind**
2. create spell-specific effects for chance casting and spell-specific
   limitations for safe casting

The second part is a design-space proposal. No spell should receive a ribbon or
limitation until the underlying procedure and balance budget are approved.

## Contents

1. Executive Recommendation
2. Speak to the Wind
3. Existing Spell Comparison
4. Casting-Mode Design Space
5. Proposed Core Procedure
6. Spell Entry Syntax
7. Chance-Casting Ribbon Budget
8. Safe-Casting Limitation Budget
9. Selection Rules
10. Banishing Example
11. Initial Cross-Discipline Candidate Pass
12. Rollout Procedure
13. Risks and Safeguards
14. Decisions Requested

## Executive Recommendation

Add **Speak to the Wind** as a Rank 2 Awareness spell. It permits concise,
one-way communication with a person the caster has observed long enough to
form a stable mental image of them. It requires no name. It does not allow a
reply, locate the recipient, confirm delivery, read thoughts, or cross between
worlds.

Adopt casting-mode riders as explicit spell-entry fields:

- `CHANCE CASTING:` grants a narrow utility, control, or conditional finishing
  effect when the caster accepts a guaranteed mishap.
- `SAFE CASTING:` imposes a narrow but meaningful limitation when safe casting
  removes at least one casting die.

Give most selected spells a chance-casting effect. Reserve safe-casting
limitations for unusually broad, repeatable, or generally useful spells whose
caster has a credible reason to trade scope for reliability. Give both to the
same spell only when the three modes are exceptionally clear.

Do not apply these fields to every spell. They should sharpen frequently cast
spells and create decisions, not become mandatory decoration.

## Speak to the Wind

### Proposed placement

- **Discipline:** Awareness
- **Rank:** 2
- **Table placement:** after `WORDS ON THE WIND` in the Awareness spell list,
  with the full entry among the Rank 2 spells
- **Role:** remote one-way communication

Rank 2 is recommended because the spell has campaign-scale reach but carries
little tactical force. Rank 1 would make unrestricted long-distance
coordination too cheap and would sit too close to `WORDS ON THE WIND`. Rank 3
would price a concise one-way message too close to `TELEPATHY`, which can send
thoughts, read minds, and inflict mental harm.

### Proposed spell text

```markdown
#### SPEAK TO THE WIND

✦ **RANK** 2
✦ **RANGE**: Unlimited, within the same world
✦ **DURATION**: Immediate
✦ **INGREDIENT**: A feather released into the air

You picture one person whom you have observed long enough to remember as a
living presence. About one hour of direct observation is normally sufficient.
If the view was intermittent, obscured, disguised, or otherwise uncertain, the
GM may require that you have observed the person for up to a Quarter Day. You
do not need to know the person's name.

Speak a message of no more than two long sentences, using no more than two
breaths. The wind carries the words in your voice and delivers them to the
imagined person's ears. The recipient hears the message if they are conscious,
able to hear, and in the same world as you. No one else hears the carried
voice. The spell does not tell you where the recipient is, whether the message
arrived, or what they did after hearing it.

The recipient cannot answer through this spell. To answer at a distance, they
must cast SPEAK TO THE WIND themselves and must separately meet its familiarity
requirement for you.
```

### Familiarity adjudication

The spell targets a remembered person, not a name or description. Use the
following standard:

- One hour of direct, reasonably clear observation is normally enough.
- Briefly seeing a stranger in a crowd is not enough.
- A portrait, verbal description, magical vision, or second-hand memory is not
  enough by itself.
- A disguised or shapechanged person is remembered as the identity the caster
  observed. The spell follows the actual living person behind that observed
  identity; it does not target the disguise as a separate being.
- The GM may require up to a Quarter Day when the observation was broken,
  unclear, or deliberately misleading.

The GM should adjudicate whether the caster can form a stable mental image, not
whether they passed a hidden social threshold.

### Delivery adjudication

- The magical wind crosses ordinary walls, weather, and enclosed spaces.
- It does not cross into Churmog, dreams, death, the past, or another plane.
- A sleeping person is conscious only if the rules currently treat ordinary
  sleep as conscious for spell targeting. The recommended ruling is that normal
  sleep does not receive the message; the wind does not wake the target.
- An unconscious or deaf recipient does not receive it.
- The caster receives no failure signal. Uncertain delivery remains part of the
  spell's character.
- The recipient recognizes the caster's voice if they would ordinarily
  recognize it.

### Message adjudication

“Two long sentences” and “two breaths” are simultaneous limits. The caster may
not evade the limit through lists, codes recited at impossible speed, a written
text read without breathing, or language magic. Ordinary concise military,
travel, warning, and personal messages are intended to fit.

The message is transmitted as spoken. The spell does not translate it.

### Proposed safe-casting limitation

If the casting-mode system is accepted, **Speak to the Wind** is a good
candidate for a safe-casting limitation because its default utility is broad,
repeatable, and campaign-relevant:

```markdown
**SAFE CASTING:** The wind can find the recipient only if they are within your
current map hex.
```

This preserves useful distant communication within a hex while making
long-range strategic communication retain magical risk. Do not add this line
unless the general safe-casting proposal is accepted.

## Existing Spell Comparison

### Words on the Wind, Rank 1

`WORDS ON THE WIND` enhances the caster's hearing out to DISTANT range. It
requires sight of the place being heard. It gathers information and sends
nothing.

**Speak to the Wind** sends information to a remembered person at unlimited
distance. It hears nothing and receives no reply. The names are close, but the
functions form a deliberate pair: one listens on the wind, the other speaks
into it.

### Telepathy, Rank 3

`TELEPATHY` reads surface thoughts, digs into memory at higher Power Level,
sends thoughts to a well-known target at LONG range, and can inflict Wits or
Empathy damage.

**Speak to the Wind** does none of these. It sends ordinary spoken language,
requires the target to hear, permits no reply, conveys no emotion beyond the
voice, and cannot attack the mind.

### Dream Visit, Rank 2

`DREAM VISIT` is a ritual performed in sleep. It reaches a previously visited
place, allows observation, and at additional Power Level permits communication
with people there.

**Speak to the Wind** is immediate and person-targeted, but is one-way and
provides no observation. Neither spell replaces the other.

### Familiar communication

A familiar can communicate only very short telepathic phrases and normally
operates nearby as an embodied scout. **Speak to the Wind** cannot provide
senses, receive reports, or issue an interactive chain of commands.

## Casting-Mode Design Space

### Design goal

Create spell-specific reasons to choose risk or restraint.

At present, chance casting answers “can I cast a spell one rank beyond my
talent?” Safe casting answers “how many casting dice am I willing to remove?”
The proposed fields let individual spells answer two further questions:

- What extra shape can this magic take when the caster deliberately lets it
  run beyond control?
- What part of this magic becomes too faint, local, simple, or constrained when
  the caster removes its danger?

The result should be a tactical or utility decision, not a general power tax.

### Terminology

Use **chance-casting effect** in rules text. “Ribbon” remains design language.

Use **safe-casting limitation** in both rules and design discussion.

These terms distinguish the proposal from overcharging:

- **Overcharging** increases Power Level through ⚔️.
- **Chance casting** guarantees a mishap and may activate a listed
  chance-casting effect.
- **Safe casting** removes casting dice and may activate a listed limitation.

## Proposed Core Procedure

### Voluntary chance casting

Add the following rule after the existing `CHANCE CASTING` paragraph:

```markdown
**VOLUNTARY CHANCE CASTING:** You may declare a spell to be chance cast even if
its rank does not exceed your rank in the discipline. Resolve the spell
normally, but you are guaranteed to suffer a magic mishap. Some spells have an
additional CHANCE CASTING effect, stated in their descriptions. That effect
applies both when you voluntarily chance cast the spell and when you chance
cast it because its rank is one step above your talent rank.
```

Without this addition, chance-casting effects would disappear as a character's
talent improves. A player could access a spell's special risk mode only while
underqualified to cast it. That would punish advancement and fail to create the
intended recurring decision.

### Guaranteed mishap resolution

Clarify that chance casting guarantees one mishap rather than adding a second
independent mishap:

```markdown
**CHANCE-CAST MISHAPS:** A chance-cast spell always causes one magic mishap. If
the casting roll shows one or more 💀, resolve the mishap normally using the
number rolled. If it shows no 💀, roll on the discipline's mishap table as if
one 💀 had been rolled. Chance casting does not cause a second mishap in
addition to one already triggered by the casting roll.
```

This preserves the guaranteed price while avoiding two unrelated mishaps from
one casting. It also closes an ambiguity in the existing chance-casting rule.

### Safe-casting activation

Add the following sentence to `SAFE CASTING`:

```markdown
A spell counts as safely cast only if safe casting removes at least one casting
die. If the spell has a SAFE CASTING limitation, that limitation applies for
the entire effect.
```

Merely being higher rank than the spell does not impose the limitation. The
caster must actually take the safety benefit.

### Mutually exclusive modes

A casting cannot be both chance cast and safely cast. Chance casting guarantees
a mishap; safe casting removes mishap exposure. Any effect that forces chance
casting makes safe casting unavailable for that casting.

### Resolution order

Resolve the mode in this order:

1. Declare normal, chance, or safe casting.
2. Apply any mode-specific target, range, or effect restrictions.
3. Spend WP and determine casting dice.
4. Roll casting dice, if any, and determine final Power Level.
5. Resolve the spell's primary effect.
6. Resolve its chance-casting effect if applicable and if its trigger occurred.
7. Resolve the guaranteed or rolled mishap.

The mishap normally follows the spell because mishaps are consequences of
magic already released. A specific mishap may still alter, redirect, or undo
what happened when its text says so.

## Spell Entry Syntax

Add either field after the spell's normal effect paragraph.

### Chance-casting field

```markdown
**CHANCE CASTING:** [Narrow additional effect and exact trigger.]
```

The line should answer:

- when it triggers
- who or what it affects
- whether it changes damage, control, information, position, or duration
- how it scales, if at all
- what happens on a partial or failed condition

### Safe-casting field

```markdown
**SAFE CASTING:** [Narrow limitation on targets, range, duration, flexibility,
or secondary functions.]
```

Write the limitation positively where possible: “targets only yourself,” “the
illusion must remain motionless,” or “the recipient must be in the same hex.”
Avoid vague statements such as “the spell is weaker.”

### Spell with both fields

Rarely, a spell may contain both. Its three modes must be easy to summarize:

- normal: standard reliable function with ordinary mishap risk
- chance: narrow extra expression plus guaranteed mishap
- safe: narrower standard function with reduced mishap exposure

If the distinction needs a paragraph of exceptions, use only one field.

## Chance-Casting Ribbon Budget

### Intended chance-effect size

A chance-casting effect should be small but meaningful. It should influence one
decision, open one situational route, or create one conditional payoff.

Appropriate effects include:

- a brief forced movement or positional opening
- one extra clue, sensory trace, or directional impression
- a conditional finisher against an already weakened or prepared target
- a minor environmental residue the party can exploit
- a one-round utility attached to a combat spell
- a small non-damage condition when the main spell succeeds
- a secondary use of a resource already present in the spell

### Numeric ceiling

Use these as maximum starting points, not entitlements:

- +1 die to one subsequent, tightly related roll
- one additional range step for a secondary effect
- one round of a minor control state
- one extra target only if the extra target receives a reduced effect
- effective additional damage no greater than the spell's base Power Level,
  gated behind injury, setup, or another narrow condition
- one small item, trace, or piece of information

The ribbon should not simply add +1 Power Level. Overcharging already owns that
design space.

### Required narrowness

Use at least one limiter:

- target must already be injured, marked, restrained, burning, sleeping, or
  otherwise prepared
- effect applies only to a narrow creature type or material
- effect occurs only if the primary spell succeeds
- effect changes position rather than adding damage
- effect expires at the end of the next round or scene
- effect creates opportunity rather than resolving the entire problem

### Cost integrity

The guaranteed mishap is a severe cost, but it is not a blank cheque. A player
should choose chance casting because the current situation makes the ribbon
valuable, not because chance casting is the mathematically correct default.

## Safe-Casting Limitation Budget

### Intended safe-limitation size

Safe casting already pays a price by removing overcharge dice. The additional
limitation should therefore be small, legible, and connected to the spell's
broad utility. It should narrow use, not make the spell pointless.

Appropriate limitations include:

- self only instead of several targets
- same hex instead of unlimited range
- stationary instead of moving
- one named material or creature category
- one function chosen from a flexible menu
- no secondary damage, forced movement, or information
- concentration or line of sight where the full spell does not require it
- shorter duration that remains useful for the immediate task

### Prohibited limitations

Do not make a safe-cast spell:

- fail automatically against ordinary opposition
- spend the same WP for no useful effect
- require a new rare ingredient
- damage the caster
- impose a long-term condition
- lose its defining purpose
- secretly less safe through another random roll

### Why safe limitations should be rare

Safe casting is a reward for mastery. If every spell acquires a limitation, the
system turns that reward into a universal surcharge. Apply safe limitations
only where a spell's default breadth is itself part of its power and a narrower
version remains clearly useful.

## Selection Rules

### Prefer frequently cast spells

Add mode text where players are likely to face the choice repeatedly:

- common combat tools
- travel and scouting spells
- healing and protection staples
- communication and information spells
- flexible spells with several ordinary uses

One-use epic rituals and spells chosen mainly for campaign climax do not need
extra mode text unless the mode creates a particularly important story choice.

### Prefer chance effects over safe limitations

For the first pass, use roughly this distribution among spells selected for
mode text:

- 70-80% chance-casting effect only
- 15-25% safe-casting limitation only
- no more than 5-10% both

These percentages apply to selected spells, not the complete chapter. Most
spells should initially remain unchanged.

### Exclude poor candidates

Avoid mode text on:

- spells already declared risky and unable to be safely cast
- spells whose existing procedure is already complex
- spells with permanent or world-changing results unless the mode is central
- spells whose main balance depends on a highly specific ritual ingredient
- reaction spells where another rider would overload resolution
- spells rarely cast more than once in a campaign

## Banishing Example

### Proposed Banish Demon chance effect

Add this paragraph to `BANISH DEMON` if the general system is accepted:

```markdown
**CHANCE CASTING:** After the spell inflicts its Strength damage, if the target
is a true demon, remains unbroken, and has current Strength no greater than the
damage it just suffered, the demon's wounded substance tears open a rift around
it. The rift drags the demon back to the world from which it came. This is
banishment, not additional damage. The rift closes immediately after consuming
the demon.
```

### Mechanical reading

Suppose the spell inflicts 3 Strength damage:

- A demon reduced from Strength 9 to 6 remains because 6 is greater than 3.
- A demon reduced from Strength 6 to 3 is banished because its remaining
  Strength equals the damage suffered.
- A demon reduced from Strength 5 to 2 is banished because 2 is less than 3.
- A demon Broken by the damage resolves as Broken; the ribbon is not needed.

The result behaves like conditional double damage against weakened demons, but
does not literally inflict a second damage packet. Armor, damage triggers,
regeneration, and effects reacting to damage therefore apply only once.

### Why the effect fits

- It requires chance casting and therefore guarantees a mishap.
- It is useless against a demon too healthy for the threshold.
- It rewards timing rather than increasing every casting's output.
- It reinforces the spell's identity as banishment rather than generic damage.
- It creates a visible, dramatic finishing opportunity without replacing the
  ordinary spell.
- It has no effect on demon-tainted creatures because `BANISH DEMON` already
  excludes them.

### Recommended wording choice

Use “the world from which it came” rather than “whence it came” in the rules
paragraph for immediate clarity. The descriptive text may use older or more
ritual language elsewhere.

## Initial Cross-Discipline Candidate Pass

This table is a scope proposal, not final spell text. It demonstrates that the
new design space can serve every discipline without forcing the same bonus onto
all of them. Each candidate must be audited against its complete entry before
implementation.

| Discipline | Candidate Spell | Mode | Proposed Direction |
| --- | --- | --- | --- |
| General Spells | Sense Magic | Chance | In addition to detecting magic, perceive the direction in which the effect's caster departed or the last direction in which the magic moved. |
| Healing | Banish Demon | Chance | Banish an already weakened true demon when remaining Strength is no greater than damage just suffered. |
| Shapeshifting | Animal Speech | Chance | After the normal questions, the animal volunteers one urgent sensory impression connected to danger, food, young, or territory. |
| Awareness | Speak to the Wind | Safe | The recipient must be within the caster's current map hex. |
| Symbolism | Illusion | Safe | The illusion must be motionless and cannot imitate speech or changing sound. |
| Stone Song | Open | Chance | The opening is quiet and the caster immediately hears any trap mechanism disturbed by the movement; this does not disarm it. |
| Blood Magic | Blood Oath | Chance | When the subject first knowingly acts against the oath, the caster immediately senses that the oath was breached and the direction to the subject, but not the distance. |
| Death Magic | Speak to the Dead | Chance | The corpse involuntarily yields one sensory fragment from the final minute of life before answering ordinary questions. |
| Elemental Magic | Wind Blast | Chance | Targets forced from their position also drop one unsecured light item of the caster's choice. |
| Ice Affinity | Winter Grip | Chance | For the first turn of the spell, affected targets leave no tracks on snow or ice unless they choose to. |
| Nature | Fog | Chance | Choose one creature in the fog; until the caster's next turn, it can see silhouettes at ARM'S LENGTH clearly enough to distinguish friend from foe. |
| Swarm Magic | Harass | Chance | The insects leave a distinctive scent and sound on the target, granting +1 die to track it until the spell ends. |
| Magma Song | Hearth | Chance | Wet clothing, bedrolls, and ordinary fuel within NEAR range become dry enough for immediate use, without creating extra food or fuel. |
| Mentalism | Traceless | Safe | The spell can alter only the caster, not additional people or creatures. |
| Oneiromancy | Premonition | Chance | When a premonitioned roll is abandoned, the dreamer receives one sensory omen indicating the immediate cause of failure, not the full hidden situation. |
| Magnetism | Iron Will | Safe | The spell can manipulate only unattended metal and locks not actively held or resisted. |
| Demonic Magic | Demon Tongue | Chance | While conversing with a demon, the caster hears one dominant appetite or emotion beneath its words; this does not reveal truth or intent. |

### Secondary candidates

If the first pass plays well, consider the following without assuming they all
need implementation:

- `DISPEL MAGIC`: a chance effect that suppresses one surviving Power Level
  until the end of the next initiative segment
- `NATURE'S WATCH`: a chance effect that distinguishes one familiar person's
  passage from other trespassers
- `FIREBALL`: a chance effect that leaves one small route briefly clear of
  smoke, not more damage
- `DUST FROM THE DEEP`: a chance effect that lets the caster identify movement
  through the dust by sound for one round
- `MIRROR IMAGES`: a chance effect that reveals the position of the attacker
  who destroys the first image
- `DREAM VISIT`: a safe limitation restricting observation to one fixed vantage
  point
- `DEFLECT METAL`: no first-pass ribbon; its reaction timing is already dense
- `GENERATE MOG`: no first-pass ribbon; its resource and corruption economy is
  already sufficient

## Rollout Procedure

### Stage 1: approve the core procedure

Decide:

- whether voluntary chance casting is allowed
- whether a chance cast causes one guaranteed mishap rather than possibly two
- whether safe limitations apply only when at least one die is removed
- whether the `CHANCE CASTING` and `SAFE CASTING` labels are accepted

Do not write dozens of spell riders before these rules are settled.

### Stage 2: implement the anchor examples

Implement and playtest:

1. **Speak to the Wind** with its proposed safe limitation
2. **Banish Demon** with its chance-casting finisher
3. one control spell, recommended `OPEN` or `WIND BLAST`
4. one information spell, recommended `SENSE MAGIC` or `ANIMAL SPEECH`

These examples test communication, conditional finishing, control, and utility.

### Stage 3: audit frequently cast spells

For each discipline:

1. identify the five spells most likely to recur in ordinary play
2. reject spells already complex or adequately mode-sensitive
3. draft no more than two chance effects and one safe limitation
4. compare each effect to a normal action and to +1 Power Level
5. test the spell at minimum and maximum plausible Power Level
6. check interaction with rituals, power words, reactions, grimoires, and risky
   spells

### Stage 4: expand conservatively

After playtest, keep effects that produce visible casting decisions. Remove
effects that players forget, that always justify chance casting, or that make
safe casting feel punitive.

## Risks and Safeguards

### Risk: chance casting becomes the optimum damage mode

**Safeguard:** Prefer utility and control. Gate damage behind a weakened target
or setup. Never give universal additional damage.

### Risk: guaranteed mishaps dominate campaign tone

**Safeguard:** Make ribbons situational enough that chance casting remains an
emergency, gambit, or expressive choice rather than routine spell rotation.

### Risk: advancement removes access to the mechanic

**Safeguard:** Permit voluntary chance casting for spells already within the
caster's talent rank.

### Risk: safe casting becomes unattractive

**Safeguard:** Apply limitations only to broad spells, keep the narrowed form
useful, and leave most spells without a safe limitation.

### Risk: modes add text to every entry

**Safeguard:** Select only frequently cast spells with a strong thematic mode.
Do not pursue numerical coverage targets.

### Risk: spell identity blurs

**Safeguard:** Derive every ribbon from the spell's existing material action.
Banishing opens a rift, Open reveals moved mechanisms, Harass leaves insects and
scent, and Demon Tongue exposes demonic appetite.

### Risk: mode effects interact badly with Power Level

**Safeguard:** Do not scale ribbons unless scaling is essential. Where scaling
exists, cap it independently from the main spell.

### Risk: safe casting and grimoires compound too efficiently

**Safeguard:** Safe limitations apply whenever safe casting removes dice,
regardless of why the effective spell rank is lower. Test zero-die casting
explicitly.

### Risk: rituals and power words become overloaded

**Safeguard:** Avoid the first pass on reactive power words, epic magic, and
rituals with several existing subprocedures.

## Decisions Requested

Before implementation, approve or revise these points:

1. **Speak to the Wind:** Rank 2 Awareness, unlimited range within the same
   world, one-way, two sentences/two breaths, one-hour-to-Quarter-Day familiarity.
2. **Normal sleep:** recommended not to receive or wake for the message.
3. **Safe limitation:** recipient must be in the same map hex when safely cast.
4. **Voluntary chance casting:** permit it for spells already within talent rank.
5. **Mishap handling:** one guaranteed mishap; rolled 💀 determine its severity,
   with a no-💀 chance cast treated as one 💀.
6. **Banishing threshold:** remaining Strength less than or equal to damage just
   suffered causes banishment.
7. **Rollout scale:** begin with four anchor spells, then audit no more than
   three candidates per discipline before broader adoption.

No changes to the magic chapter should be made until these decisions are
accepted.
