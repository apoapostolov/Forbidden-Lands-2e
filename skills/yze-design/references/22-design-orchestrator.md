<!-- markdownlint-disable MD013 -->

# Design Orchestrator — Route, Build, Validate, Publish

> **STATUS: FILLED.** Load this file first for substantial `yze-design` work. It turns the reference library into an operating procedure: identify the task mode, select a compatibility profile, prove the five loops, choose patterns and workshop modules, validate the output, name the game, then translate it into player-facing prose.

## Contents

1. Task router
2. Mandatory output contract
3. Stop-and-ask gate
4. Complete-game generator
5. Existing-game extension contract
6. Rule invention contract
7. Naming and publication handoff

## 1. Task router

Classify every request into exactly one primary mode. Secondary modes may be loaded after the primary mode has produced its brief.

| Mode | User intent | Load next | Final output |
| --- | --- | --- | --- |
| **Analyze existing mechanic** | "What is this rule doing?", "abstract this", "why does this work?" | `00`-`15`, then `12`, `15`, and `26` if naming is requested | Abstraction ladder + choice map + source-backed verdict |
| **Adapt existing YZE game** | "Add X to this game", "make a module for Alien/Vaesen/Coriolis-like play" | `23`, host game's own skill/docs if present, `13`, `20`, `21`, `26` | Host extension contract + rule text + validation memo |
| **Build complete new game** | "Make a YZE game about X" | `23`, `14`, `16`-`18`, selected workshop modules, `24`, `26` | Complete game package with naming sheet |
| **Invent rule set** | "Create a mechanic for X" | `16`, `17`, `18`, relevant workshop modules, `24`, `26` | Modular rule set with needs/gives list + rule text |
| **Check/audit rule set** | "Is this balanced?", "stress test this" | `13`, `19`, `24` | Verdict, failure points, fixes, revised rule if requested |

If a request looks like multiple modes, route to the highest-level one: complete game > host adaptation > rule invention > checks > analysis.

## 2. Mandatory output contract

Every substantial output must include these fields, even if brief:

- **Design brief:** genre, audience promise, play loop, desired feel, exclusions.
- **Assumptions:** what was inferred rather than provided.
- **Game style:** FL anchor, West anchor, or one profile from `23`.
- **Five-loop map:** Expedition, Conflict, Recovery, Willpower, Base each marked Active / Secondary / Collapsed, with one-line reason.
- **Pattern map:** P1-P15 and advanced pattern blends used.
- **Rules inventory:** General, Situational, Optional, Campaign Mode.
- **Naming sheet:** analytical name → flavorful generic name → genre-specific name for every major rule.
- **Validation memo:** math/tempo, abuse surface, synergy, table burden, felt experience.
- **Publication handoff:** player-facing rule, GM-facing procedure, example of play, quick reference or sheet fields where needed.

## 3. Stop-and-ask gate

Ask the user only when all three are true:

1. The missing choice materially changes the game identity or safety/tone of play.
2. The answer cannot be inferred from the prompt, repo, host game, or selected compatibility profile.
3. Choosing a default would be risky or disrespectful to the requested audience.

Examples that may require asking: desired horror intensity, whether PCs can die or transform permanently, whether the game is for campaign or one-shot, whether to preserve a named host game's exact canon. Examples that do not require asking: which file owns combat, whether to run validation, whether to cite FL/West anchors.

When not asking, choose the conservative default: keep lethality moderate, keep permanent loss recoverable, limit signature mechanics to 1-3, and mark uncertain choices as assumptions.

## 4. Complete-game generator

Use this when Mode = Build complete new game. Recipe A in `14` provides the system sequence; this file upgrades the deliverable from skeleton to playable package.

### Phase A — Concept lock

Produce:

- One-sentence thesis: ambition + exposure + currency + adversary.
- Audience promise: what players repeatedly do and feel.
- Profile choice from `23`.
- Signature mechanics target: 1-3, each tied to a pressure loop.

Acceptance: a stranger can tell why this game should exist as YZE, not a generic RPG.

### Phase B — Core rules package

Produce:

- Attribute grid with damage names.
- 16-skill grid.
- Push cost, Willpower, Pride/Faith/inner-fire rule, and failure pressure.
- Conflict model, harm model, travel/downtime model, org/base model, gear/economy model, power layer, advancement.
- GM procedures: principles, encounter engine, consequence tracks, statblock grammar.

Acceptance: a player can build a character and a GM can resolve ordinary uncertainty.

### Phase C — Loop proof

For each loop:

| Loop | Must answer |
| --- | --- |
| Expedition | What journey, mission, investigation, or project turns time into pressure? |
| Conflict | What tactical or dramatic confrontation is common enough to need rules? |
| Recovery | What damage or pressure takes time, safety, or help to repair? |
| Willpower | What risk refuels agency, and what agency does it buy? |
| Base | What persistent people/place/org matters between scenes? |

If a loop is collapsed, state the replacement. Example: in a locked-room mystery, Expedition may collapse into Investigation Turns; in a one-shot duel game, Base may collapse into Relationships.

Acceptance: no major reward channel is free of exposure.

### Phase D — Play package

Produce:

- Character creation checklist.
- Character sheet field list.
- Starter scenario: premise, three scenes, three NPCs, one pressure clock/table, one consequence table.
- Three examples of play: ordinary roll, pushed roll, signature rule.
- Manuscript outline: player chapters, GM chapters, optional modules.

Acceptance: a GM can run a one-shot from the package without designing missing procedures.

### Phase E — Validation and publication

Run `24` worksheets and `13`/`19` protocols. Then load `26` to name the game, followed by `20` and `21` to translate core rules into publication prose.

Acceptance: every General rule has a pressure loop, no persistent broad bonus lacks cost/scope/cap/risk, and the final text is player-readable.

## 5. Existing-game extension contract

Before adding a rule to a host game, document:

- **Host cost model:** bane-self-harm, currency-spend, Trouble, hybrid, other.
- **Host loop weights:** which of the five loops dominate.
- **Host optional surface:** what the game already treats as optional.
- **Forbidden changes:** what would erase the game's identity.
- **Native voice:** terse survival, documentary, cinematic horror, social gothic, military procedural, etc.

Every extension must state:

- Layer: General / Situational / Optional / Campaign Mode.
- Replaces or stacks with existing rules.
- Willpower interaction.
- Action-budget interaction.
- Harm/recovery interaction.
- Tone risk.

Default: extensions are Optional unless the user explicitly asks for a core rewrite.

## 6. Rule invention contract

For a new rule set:

1. State the pressure problem in one sentence.
2. Pick one primary pattern and at most two supporting patterns from `16`.
3. Generate 3 possible rules using `18`; for high-creativity requests generate 5 or 10.
4. Compare each candidate against a lighter reskin.
5. Select the smallest candidate that changes play behavior.
6. Write what the rule needs, what it gives, systems touched, and incompatibilities.
7. Validate with `24`.
8. Name with `26`, then publish using `20`/`21`.

A signature mechanic must pass this test: if removed, the game plays differently, not merely with different nouns.

## 7. Naming and publication handoff

Use this output order:

1. **Naming sheet:** analytical name, flavorful generic name, and genre-specific name for the rule and any sheet fields.
2. **Player rule:** what the player does, in rulebook voice.
3. **GM procedure:** when to call for it, how to adjudicate edge cases.
4. **Designer note:** why it exists, where it hooks, validation caveats.
5. **Example of play:** one short example showing the decision and cost.
6. **Quick reference:** action names, costs, triggers, recovery, sheet fields.

Design jargon belongs in designer notes, not player rules. Terms such as "pressure loop," "primitive," "dial," "metacurrency," "protected dial," "subsystem," "payload," and "validation pipeline" must be translated before publication. Use `26-naming-the-game.md` before `20-publication-voice.md`.
