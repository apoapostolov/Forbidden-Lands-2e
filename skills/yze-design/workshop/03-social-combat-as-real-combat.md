<!-- markdownlint-disable MD013 MD024 -->

# Social Combat as Real Combat — Tactical Conversation

> **STATUS: WORKSHOP MODULE.** High-stakes social scenes as full tactical conflicts: the action economy, social-distance "range bands," leverage as weapons, Composure as social HP, a Broken-equivalent. *Core is generic; the worked example (Regency high society) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic design space
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — Regency high society

## 1. Origin — how this was built

- **Source primitives:** the **action economy** (`03 §7`) + **P3 (graded success + stunts)** + **P4 (typed D66, for social fallout)** + a domain transfer of the **range/positioning** model (`03 §5`).
- **Reinvention operator:** **Domain Transfer (full).** Take the combat engine's load-bearing structure — 2 actions/Round, slow+fast, positioning, attack vs defense, a Broken threshold — and re-skin every noun.
- **Target psychology:** **Attritional / tactical** (`17` M6) — scenes that matter as much as fights. Social-focused characters get the depth of play combat characters always had.
- **Problem solved:** social conflict in both source games is a single opposed roll or a short modifier. Fine for incidental persuasion; thin for genres where society *is* the battlefield. This closes the gap.

## 2. The generic design space

### 2a. Mechanism overview

When a social scene has high stakes, an opponent with an agenda, and real consequence on failure, it becomes a **Social Combat**: a multi-Round conflict using the engine's action economy (1 slow + 1 fast, or 2 fast, per Round). Each speaker has a **Composure** pool (social HP). Attacks deal Composure damage via a formula (leveraged pool + successes). **Social distance** (Intimate / Personal / Professional / Public) functions as range bands — moves that work at one distance fail at another. **Leverage** (secrets, favors, rank, witnesses) functions as weapons (consumable dice). At 0 Composure, a speaker is **socially Broken** and rolls on a typed D66 **Social Fallout** table.

### 2b. NEW CONCEPTS introduced

- **NEW CONCEPT — Social distance as range bands:** Core combat uses physical range bands (Arm's Length → Distant). Social Combat maps these to *relational* distance (Intimate → Public) where each band enables and forbids specific move types. *Extends the engine's positioning model into a non-physical domain.*
- **NEW CONCEPT — Composure as parallel HP:** Core social conflict deals attribute damage (Empathy/Docity) or a binary comply-or-attack. Composure is a *dedicated social-HP pool* that depletes through a scene and recovers between scenes, parallel to but distinct from attribute-HP. *Extends the engine by adding a scene-scoped health track.*
- **NEW CONCEPT — Leverage as consumable weapon-die:** Core weapons are persistent gear (Gear Dice). Leverage in Social Combat is *consumable* — a secret used is a secret spent; it grants a die for one attack, then is gone. *Extends the gear-as-dice model with a single-use weapon class.*
- **NEW CONCEPT — Audience as a combatant (optional dial):** When enabled, the *room's opinion* is a tracked third-side that both speakers compete to shift — modeling performative debate where the audience is the real prize. *Extends the conflict model from dyadic to triadic.*

### 2c. Mechanical reference (tables & procedures)

#### Composure

- **Pool:** Wits + Empathy (typical 4–8). Alternatively a fixed 6 per character for uniformity.
- **Regen:** 1/scene by default; or 1/Round with a "compose yourself" fast action (faster dial).
- **At 0:** socially Broken — lose the exchange, roll on the Social Fallout table (below).

#### The Composure damage formula

> **Damage = (successes on the attack roll) + (leverage die face, if leverage spent and rolls 6+)**

- The attack roll is a standard ability pool (the speaker's social skill + attribute + any gear/help), read on the success ladder (P3).
- **Successes dealt as damage:** 1⚔ = 1 damage; 2⚔ = 2 damage; 3⚔ = 3 damage (critical).
- **Leverage die:** if leverage is spent (consumed), roll its die (D6/D8/D10/D12 per the Leverage table). On a 6+, add the die's success-count to the damage (using the artifact-die scaling from `00 §9`: D8 6–7 = 1, 8 = 2; D10 6–7 = 1, 8–9 = 2, 10 = 3; D12 6–7 = 1, 8–9 = 2, 10–11 = 3, 12 = 4).
- **Defense reduces damage:** a successful deflection (dodge/parry reaction) cancels 1⚔ per success on the deflection roll. A failed deflection deals no reduction.
- **Reputation armor:** if the defender has established Reputation with the constituency (per `workshop/01`), subtract the Reputation rating from incoming damage (to a minimum of 0). Reputation is "social armor."

#### The Leverage table (consumable weapon-dice)

| Leverage type | Die | Notes |
| --- | --- | --- |
| A whispered rumor, a small favor owed | D6 | Single-use; consumed on spend. |
| A documented secret (a letter, a contract) | D8 | Single-use; the document can be stolen back if exposed. |
| A witness present who will testify | D8 | Requires the witness be in the scene; consumed if the witness is discredited. |
| Rank / official authority | D10 | Not consumed (persistent) — but misusing it triggers a Scandal Roll (`workshop/01`). |
| Blackmail (a damning secret) | D10 | Single-use; consumed; exposes the secret publicly. |
| A public threat (exposed violence) | D12 | Single-use; consumed; shifts the scene to Public distance forcibly. |

*Leverage is distance-gated* (see below): a whispered rumor only works Intimate-to-Personal; a public threat only at Public. Mismatching leverage-to-distance imposes a −2 penalty on the attack roll.

#### Social distance — the positioning layer

| Band | What works here | What fails here | Move cost |
| --- | --- | --- | --- |
| **Intimate** (a whisper, a confidence) | Vulnerability, threats, confessions, private appeals | Public declarations, performances, shaming | — |
| **Personal** (direct one-on-one, in others' presence) | Persuasion, bargaining, intimidation | Deniable whispers (ineffective); public performances | 1 fast action to move here from Professional |
| **Professional** (formal, role-bound) | Precedent, protocol, rank-appeals | Confessions, personal threats | 1 fast action to move here from Personal or Public |
| **Public** (a declaration to the room) | Reputation attacks, performance, shaming, rallying | Cannot be taken back; private leverage becomes public | 1 slow action to move here (the move is itself a dramatic act) |

**Distance move procedure:**
1. The speaker declares the move as their fast (Intimate↔Personal↔Professional) or slow (to Public) action.
2. The opponent may **contest the move** with a reaction (a deflection) — success keeps the distance where it was; failure allows the move.
3. Once at a distance, both speakers are at that distance until one moves. Attacks use the distance's enabled moves; mismatched leverage takes the −2 penalty.

#### The action economy (identical to combat)

Per Round: **1 slow + 1 fast, OR 2 fast.** Reactions (deflections) draw from the same budget — a reaction costs your fast action. Below are the full action lists for Social Combat. Each is a reskin of the combat action tables (`03 §7`); the verbs change, the economy does not.

#### Slow actions (choose one per Round)

**SPEECH** is a SLOW action and the baseline offensive move — a full rhetorical turn: a speech, an argument, a case laid out before the room. Roll MANIPULATION or PERFORMANCE (plus your attribute plus any leverage you spend). On a success, you deal Composure damage per the damage formula. This is what most attacks in a Social Combat look like.

**REVELATION** is a SLOW action that deploys a secret, a fact, or a piece of evidence publicly. It requires leverage — you must have something to reveal. Roll MANIPULATION or PERFORMANCE plus the leverage die. The damage is as a SPEECH, but if the leverage was a secret, it is consumed and becomes public knowledge. You cannot take it back, and everyone in the room now knows what you revealed.

**APPEAL TO VALUE** is a SLOW action that invokes something the audience holds dear — honor, piety, family, duty, profit, freedom. The audience is the target, not the opponent. Roll PERFORMANCE plus your attribute. On a success, the audience modifier shifts toward you by 1, and the opponent takes −1 to their next roll as the crowd's favor turns against them. This is the move for turning a room, not for breaking a person.

**POINTED QUESTION** is a SLOW action that forces the opponent to answer. Roll MANIPULATION opposed against the opponent's INSIGHT. On a win, the opponent must either answer (costing their fast action) or dodge the question and take a −1 penalty to their next roll for evading. A POINTED QUESTION deals no damage, but it sets up your next move — the opponent is on the back foot, and the audience is watching how they respond.

**PUBLIC DECLARATION** is a SLOW action that moves the conversation to Public distance and makes a statement that cannot be taken back — a denunciation, a proposal, a threat, a verdict. Roll PERFORMANCE plus your attribute. The damage is as a SPEECH at Public distance, and the statement is permanent: you cannot later claim you didn't say it. The speaker's Reputation is now on the line. A failed PUBLIC DECLARATION triggers a Scandal Roll (`workshop/01`) — the crowd watched you stake your name and lose.

**EXPOSE / SHAME** is a SLOW action that turns the audience against the opponent by highlighting a flaw, failure, or hypocrisy. Roll MANIPULATION resisted by the opponent's Composure. On a success, the opponent loses 1 Composure per ⚔ rolled, and the audience shifts toward you by 1. On a failure, the audience finds you cruel rather than convincing — the audience shifts toward the opponent by 1. This is a high-risk, high-reward move: land it and the room turns; miss it and you look like a bully.

**BUILD RAPPORT** is a SLOW action that lowers the opponent's guard — a warm anecdote, a shared memory, a concession, an appeal to your shared history. Roll MANIPULATION opposed against the opponent's INSIGHT. On a success, the opponent's next attack takes a −1 penalty; they are softened. This deals no damage. A failed BUILD RAPPORT makes you look weak — the audience shifts −1 toward the opponent. Use this when you have time to set up a bigger move.

**COMPROMISE / OFFER** is a SLOW action that proposes a deal. No roll — the offer is the action. The opponent can accept, ending the scene on agreed terms, or refuse. A refusal is public: the audience sees them as unreasonable, and the opponent takes −1 to their next roll. This is the exit valve — when you want the scene to end without a clear winner, or when you're losing and want to salvage something.

#### Fast actions (choose one per Round, or two if you forgo your slow action)

**QUIP** is a FAST action — a quick jab, a one-liner, a sarcastic aside, a cutting remark. Roll MANIPULATION or PERFORMANCE. On 2 or more ⚔, deal 1 Composure damage. A QUIP cannot crit — it is light pressure, not a killing blow.

**DEFLECT** is a FAST action — the social parry. Absorb an incoming attack with composure or insight. Roll INSIGHT or the relevant social ability against the attacker's ⚔ count. Each ⚔ you roll cancels one of the attacker's successes, reducing the damage. This is the reliable defense: it never fully avoids an attack, but it always reduces it.

**COUNTER** is a FAST action that turns an opponent's attack against them — "you would say that," "is that what you told them, too?" You must DEFLECT first; the COUNTER is a follow-up. Roll INSIGHT against the attacker's MANIPULATION or PERFORMANCE. On a success, deal 1 Composure damage back to the attacker. A COUNTER uses both your fast actions — you cannot also QUIP or GESTURE this Round.

**GESTURE / PROPS** is a FAST action — a gesture, a brandished letter, a meaningful glance at a witness. No roll. You bank a +1 bonus to your next SLOW action. This does not stack — you can only hold one banked bonus at a time. This is the setup move: it costs your fast action now to make your next speech land harder.

**SMALL LIE** is a FAST action — a minor falsehood: "I heard he was there too," "the Cardinal said as much." Roll MANIPULATION opposed against the opponent's INSIGHT. On a success, bank a +1 to your next attack. On a failure, you take −1 to your next roll and the audience shifts −1 toward you — they caught you, and the room noticed.

**INTERRUPT** is a FAST action that cuts the opponent off mid-speech. Risky but disruptive. Roll MANIPULATION opposed against the opponent's WITS. On a success, cancel the opponent's SLOW action — they lose it. On a failure, you lose your next SLOW action: the crowd finds you rude, and you've ceded the floor.

**DISTANCE MOVE** is a FAST action that shifts the social distance one band — from Intimate to Personal, Personal to Professional, or back. No roll is required unless the opponent contests it (they may spend a fast action to block the move). Moving to Public distance is a SLOW action, not a fast one — a PUBLIC DECLARATION is a dramatic act, not a casual shift.

#### Reactions

Reactions cost your fast action. You may react once per incoming attack. If you have already spent your fast action, you cannot react.

**DEFLECT** (parry) is a reaction used when an attack lands on you. Roll INSIGHT or the relevant social ability. Each ⚔ you roll cancels one of the attacker's ⚔, reducing the damage. This is the reliable defense — it always reduces, never fully avoids.

**DODGE** is a reaction used when an attack lands on you. Roll WITS or the relevant social ability. On 2 or more ⚔, you avoid the attack entirely — no damage. On 0 or 1 ⚔, you take full damage. This is the high-risk, high-reward defense: it can save you completely, or it can fail and leave you exposed.

**RIPOSTE** is a reaction used after a successful DEFLECT. Roll MANIPULATION or PERFORMANCE opposed against the attacker's INSIGHT. On a success, deal 1 Composure damage back to the attacker. A RIPOSTE costs your fast action — you cannot also act this Round. This is the counterattack: you defended, and now you sting back.

#### Stunts (surplus successes)

Any ⚔ beyond the first on an attack may be spent on stunts, exactly as in physical combat (`03 §7`). Choose one stunt per surplus ⚔:

**Extra damage.** +1 Composure damage. May be taken multiple times if you have multiple surplus ⚔.

**Force a distance shift.** Move the opponent one band — toward Intimate to soften them, toward Public to expose them. They cannot resist; the shift is the cost of your success.

**Expose a tell.** Bank a +1 to your next attack against this opponent. They have shown a weakness, and you saw it.

**Rally the audience.** Shift the audience modifier toward you by 1. The room is with you.

**Discredit leverage.** If the opponent used leverage this Round, nullify its damage. The leverage is still consumed — they spent it for nothing, and everyone saw it fail.

**Force a retreat.** The opponent loses their next FAST action. They are back on their heels, struggling to respond.

**Open a vulnerability.** The opponent takes −1 to their next defense. They are off-balance, and your next move will land cleaner.

#### Crowd / audience modifiers

When the **audience-as-modifier** dial is on, the scene has an **audience rating** — a number from −3 (hostile) to +3 (favorable) representing the room's current lean. It starts at the GM's call: often 0 for a neutral room, or set by the fiction (a rival's home turf starts at +1 toward the rival). The audience rating applies as a modifier to both speakers' attack rolls, but in opposite directions — a favorable audience adds to your attacks and subtracts from your opponent's.

**Hostile (−3).** The room is against you. You take −1 to your attacks; your opponent gains +1. The audience may interrupt — the GM rolls 1D6, and on a 1 a heckler disrupts your next action.

**Cool (−1).** The room leans away from you. You take −1 to your attacks.

**Neutral (0).** No modifier. The room is waiting to be convinced.

**Warm (+1).** The room leans toward you. You gain +1 to your attacks.

**Favorable (+2).** The room is with you. You gain +1 to your attacks; your opponent takes −1.

**Rapt (+3).** The room hangs on your words. You gain +2 to your attacks; your opponent takes −1. But a failed attack at Rapt triggers an audience backlash — the rating drops to Cool (−1). "We expected better."

**What shifts the audience.** A successful APPEAL TO VALUE shifts the audience +1 toward the speaker. A successful EXPOSE / SHAME does the same, but only if the audience shares the value invoked — a cynical crowd won't care about hypocrisy. A critical hit (3⚔) shifts the audience +1. A failed Public Declaration shifts the audience −2 toward the speaker — the crowd turned. A successful BUILD RAPPORT shifts the audience +1. A visibly cruel move — an EXPOSE that fails, or a QUIP targeting a sympathetic figure — shifts the audience −1 toward the speaker, at the GM's judgement.

**Audience size matters.** A small audience (2–5 witnesses) shifts ±1 per trigger. A large audience (a ballroom, a courtroom gallery) shifts ±2 per trigger — the crowd amplifies everything. A mob (an angry crowd) shifts ±1 per Round toward its existing lean unless someone acts to sway it — a mob is a clock, and it is ticking.

#### Environmental / social-context modifiers

The setting of the social combat grants modifiers, exactly as terrain grants modifiers in physical combat (`03 §5`).

**Formal / ritualized** settings — a court, a courtroom, a ceremony — grant +1 to appeals based on authority, protocol, or precedent, and impose −1 on intimacy or personal appeals. Speakers using rank, protocol, or formal procedure fight from strength here.

**Informal / intimate** settings — a back room, a bedchamber, a fireside — grant +1 to intimacy, vulnerability, and threat, and impose −1 on formal protocol. Speakers at Personal or Intimate distance fight from strength here.

**A public stage** — a podium, a dais, the floor of a hall — grants +1 to Public-distance moves and doubles all reputation effects, both gains and losses. A triumph on the stage is twice as sweet; a fall is twice as far.

**Sacred ground** — a temple, a shrine, a consecrated hall — grants +1 to appeals to faith or piety and imposes −1 on lies and threats. A lie caught on sacred ground triggers a Scandal Roll (`workshop/01`) at +1 severity. The divine is watching.

**A professional domain** — a guildhall, a barracks, a market floor — grants +1 to the domain's masters and imposes −1 on outsiders. The home team knows the room, the rules, and the people.

**Neutral ground** — a roadside inn, a foreign court, a neutral meeting point — grants no modifier, but neither speaker gets a home advantage. Both fight on even terms.

**Hostile territory** — the opponent's home, their faction's turf — imposes −1 on the visitor to all rolls. You are out of your element, and everyone knows it.

#### Multi-participant social combat

Social Combat scales beyond 1v1. The action economy and distance rules still apply; the differences are in how turns are allocated and how damage flows.

**Two against one.** The lone speaker takes two full turns per Round — one against each opponent — but each turn is a separate slow+fast set. This is exhausting but not action-starved: the lone speaker is defending on two fronts. The pair may coordinate: one can set up (BUILD RAPPORT, POINTED QUESTION) while the other strikes. Coordination requires the fast action of the striker to receive the cue. The lone speaker may focus on one opponent per Round; the other gets a free QUIP — a fast jab, no roll needed, 1 damage on 2+ ⚔ — representing the ignored opponent pressing their advantage.

**Two against two (or team versus team).** Each side rolls initiative once; teammates alternate turns. A teammate may defend another by spending their fast action to DEFLECT for their partner — the spokesperson shielding a principal. Optionally, a side may share a single Composure pool (the sum of both members') rather than tracking separately. This is simpler, but a single Broken breaks both.

**Three-way or chaotic.** A debate, a council, a squabble — each speaker has their own Composure and their own agenda. The audience modifier splits: track the audience's lean toward each speaker, or simplify by giving the current frontrunner +1. Cross-fire is the danger: a speaker attacked by two others in one Round may only DEFLECT one of the attacks. The other lands unopposed. The exception is COVER GROUND — a general defense that costs a slow action, deals no damage, but reduces all incoming damage this Round by 1.

#### Escalation — when a single roll becomes a Social Combat

Not every social roll should become a scene. Use this procedure to decide when to escalate:

1. **The roll is made** (a social skill check, per `03 §11`).
2. **Check the triggers:** (a) high stakes (reputation, a marriage, an alliance, a confession, a verdict); (b) an opponent with an agenda who will not simply yield; (c) real consequence on failure.
3. **If all three are present and the roll fails (or succeeds narrowly):** the GM offers escalation — "This isn't over with a single roll. Do you want to press this into a scene?" The player may accept or concede.
4. **If the player accepts:** begin Social Combat. The initiating roll's result carries forward: a success grants the escalator +1 to their first attack (they have the floor); a failure grants the opponent +1 (they're on the back foot).
5. **If the player declines:** the single-roll result stands. The NPC's reaction is as the roll dictated.

**GM guidance:** escalate when the fiction demands a scene — when the outcome matters enough that a single roll feels like a cheat. Do not escalate for routine persuasion, bartering, or information-gathering. The rule of thumb: if the *players* would feel shortchanged by a single roll resolving this, escalate. If they'd feel bogged down by a scene, don't.

#### The Social Fallout table (typed D66)

When a speaker hits 0 Composure, roll D66. The constituency family is the social context of the scene.

**Court / elite family** (sample — build parallel families for Street / Diplomatic / Professional / Familial):

| D66 | Result | Mechanical effect |
| --- | --- | --- |
| 11–14 | **Lost composure.** A stammer, a flushed face, a missed word. | The Broken speaker concedes the point; −1 Influence (`workshop/01`) with the audience. |
| 15–22 | **Sharp retort fled.** The devastating line comes to you — an hour too late. | The opponent's point stands uncontested for the rest of the scene. |
| 23–31 | **Visible anger.** You raise your voice; the room notices. | −1 Composure regen this scene; the opponent gains +1 attack next Round (your guard is down). |
| 32–41 | **Tactical retreat.** You leave the exchange to compose yourself. | You exit the scene; the opponent wins by default; you regain 2 Composure but lose standing. |
| 42–51 | **Concession extracted.** You agree to something you did not intend. | You owe the opponent a favor (Debt +1 per `workshop/02` or `06`). |
| 52–61 | **Public humiliation.** A line landed; the room laughs or gasps. | −2 Influence; the opponent gains +2. A rival may record the moment (leverage D6, consumable). |
| 62–64 | **Storming out.** You leave in a visible rage. | You are absent from the scene's resolution; the opponent's narrative wins; −1 Influence. |
| 65 | **Breakdown.** Tears, a confession, a loss of face. | −3 Influence; a Dark Secret may be exposed (GM call); you cannot re-enter the scene. |
| 66 | **Social destruction.** A ruinous exposure; you are finished in this constituency. | Influence drops to −3 (active hostility) with this constituency; the opponent becomes the constituency's favorite. |

*Other families use the same D66 architecture with re-skinned rows: Street (dissed → marked), Diplomatic (rebuked → recalled), Professional (reprimanded → blacklisted), Familial (scolded → disowned).*

## 3. The pressure loop

- **Pressure:** Composure depletes; leverage is spent; distance constrains options.
- **Decision:** *spend leverage now or save it? move to Public to land the big attack (and make it permanent)? deflect or absorb?*
- **Consequence:** Composure drops; reputations shift; secrets come out.
- **State change:** the relationship between speakers, and their standing with witnesses, changes materially.
- **Loop shape:** **position → attack/deflect → expose/spend → Break or concede.** Round cadence.

## 4. Dials

| Dial | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Composure pool** | Wits + Empathy (variable) | Fixed 6 | Build-dependent vs uniform |
| **Regen** | 1/scene (slow) | 1/Round with "compose" fast action | Grueling vs forgiving |
| **Damage scale** | 1–3 per hit | 1–2 per hit | Lethal social scenes vs prolonged |
| **Leverage** | Consumable dice (D6–D12) | Flat +1/+2 modifiers | Resource-economy vs simple |
| **Distance bands** | All 4 | 2 (Private / Public) | Rich positioning vs simple |
| **Witnesses** | Audience modifier (defined up front) | Abstract (GM framing) | Mechanical vs narrative |
| **Broken state** | Forced capitulation + Fallout | Player chooses: concede OR take permanent Reputation hit to keep fighting | Hard floor vs last-stand |
| **Audience as combatant** | Off | On (audience opinion is a track both compete over) | Duel vs debate |

**Default:** Wits+Empathy Composure, 1/scene regen, 1–3 damage, consumable leverage dice, all 4 bands, audience-as-modifier.

## 5. Integration points

- **Hooks into:** social conflict (`03 §11`) — extends it for high-stakes scenes. Influence (`workshop/01`) — Influence can absorb a social hit or boost an attack. Faction web (`workshop/02`) — witnessed social combats shift Standing. Harm (`04`) — a Social Fallout can deal real Empathy/Docity damage (humiliation hurts).
- **Requires:** a Composure track per participant; defined leverage; a sense of the social context; an audience (real or implied).
- **Replaces / extends:** the single social roll.
- **Cross-refs:** `03 §7–§11`, `17` M6, `04 §5`.

## 6. Failure modes & edge cases

- **Using it for everything.** Social Combat is expensive (a 4-Round scene). **Fix:** reserve for the 3 triggers (high stakes, opposed agenda, real consequence). (`19` FE2.)
- **The speaker-skill monopoly.** If only the "face" can participate, others watch. **Fix:** the audience-as-combatant dial; allow PCs to "help" with fast-action interruptions.
- **Composure-bag-of-HP.** If Composure is just HP, it feels like combat-with-different-nouns. **Fix:** the *social distance* layer is the distinguishing tactic.
- **Leverage inflation.** Stockpiling 5 black-mails and dumping them in one scene one-shots any opponent. **Fix:** leverage is consumable and distance-gated; one leverage per attack.
- **The GM-fiat audience.** If the audience opinion is GM whim, it feels rigged (`19` FE5). **Fix:** define the audience modifier up front; shift only on defined triggers.

## 7. Validation notes

- **Math (`13 §3`):** at 1–3 damage and Wits+Empathy pools (4–8), a typical Social Combat resolves in 3–5 Rounds (like a real fight). At 2⚔ average per successful attack and ~5 Composure, ~3 hits to Break — consistent with combat's 3–5 Round target.
- **Exploits (`13 §5`):** leverage-inflation gated by consumable + distance + one-per-attack. Two-fast-action quip-spam gated by GM ruling quips ineffective against serious slow attacks.
- **Felt experience (`19`):** the *audience* dial is key psychology — performance scenes are about the room's opinion (C5). The distance layer prevents FE1 (false choice) by ensuring moves are situational.

## 8. Worked genre example — Regency high society

**Setting:** a country-house ball, 1813. The PCs seek the Duke's blessing for a marriage; the Duke's sister opposes; the Duchess's companion holds a ruinous secret.

**Dials set:** Composure = Wits + Empathy; regen 1/scene; damage 1–3; consumable leverage dice; all 4 bands; audience-as-modifier (the room starts +1 toward the sister, the favored hostess).

**Cast leverage:**
- PC (Eleanor): D8 leverage = a letter proving the sister's own elopement (blackmail, consumable).
- Lady Caroline (sister): D6 leverage = a whispered rumor about Eleanor's mother (consumable) + native Reputation armor (+1).
- Mrs. Jennings (companion): neutral, holds D10 = the actual truth about Eleanor's birth (could be exposed by either side).

**In use (excerpt):**

- **Round 1.** Eleanor opens at **Professional** (formal suit-presentation) with a slow action: a speech appealing to the Duke's honor. Pool: Empathy 3 + Performance 2 = 5 dice; rolls 2⚔ — a clean hit. **Damage = 2⚔ + 0 leverage = 2** to the Duke (the audience-object). The Duke warms.
- Lady Caroline **reacts** (deflect, fast): a quip undermining the speech. Rolls Insight vs Eleanor's ⚔ count: 1⚔ — partial deflection, cancels 1 of Eleanor's 2 successes. **Damage reduced to 1.** She then takes her slow action: **moves the conversation to Personal** and deploys her rumor-leverage (D6). Pool: Wits 3 + Insight 2 + leverage D6 = 6 dice; rolls 1⚔; leverage die rolls a 3 (no bonus). **Damage = 1⚔ + 0 = 1**, minus Eleanor's Reputation armor (0) = 1 Composure to Eleanor.
- **Round 2.** Eleanor **moves to Intimate** (a confidence, stepping to the window — fast action, uncontested) and **spends her leverage** (the letter, D8 — slow action). Pool: Empathy 3 + Manipulation 2 + leverage D8 = 5 dice + leverage; rolls 3⚔; leverage D8 rolls an 8 (= 2 successes). **Damage = 3⚔ + 2 = 5**, minus Caroline's Reputation armor (1) = **4 Composure damage.** Caroline (pool ~5) drops to ~1. A critical hit — Caroline rolls on the **Social Fallout table**: 62 (**Storming out**) — she flees the room. The audience modifier flips to +2 toward Eleanor. The Duke, seeing his sister flee, grants the blessing.

**Why Regency:** the *audience* dial models drawing-room drama as performance — what matters is who the room thinks won. *Social distance* maps onto Regency etiquette (a whisper vs a public declaration are wildly different). Leverage as consumable dice makes secrets *spent*, not just known — which is how blackmail works.

**Re-skin:**
- **Diplomacy:** distance = bilateral / small-group / plenary / communiqué; leverage = intelligence, guarantees; Broken = a walk-out.
- **Courtroom:** distance = sidebar / cross-exam / closing / press; leverage = evidence, precedents; jury = audience track.
- **Interrogation:** distance = off-the-record / formal / recorded / charges; leverage = evidence, immunity; Broken = a confession.
- **Market haggling (high-stakes):** distance = back-room / counter / floor / auction; leverage = rival offers; Broken = a deal closed.
