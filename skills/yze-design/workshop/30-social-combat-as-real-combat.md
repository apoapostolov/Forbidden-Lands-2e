<!-- markdownlint-disable MD013 MD024 -->

# Social Combat as Real Combat — Tactical Conversation

> **STATUS: WORKSHOP MODULE.** Treats high-stakes social scenes as full tactical conflicts with the action economy, positioning, "attacks," and a Broken-equivalent — not a single opposed roll. *Core is generic; the worked example (Regency high society) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic mechanism
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — Regency high society

## 1. Origin — how this was built

- **Source primitives:** the **action economy** (`03 §7`) + **P3 (graded success + stunts)** + **P4 (typed D66, for social fallout)** + a domain transfer of the **range/positioning** model (`03 §5`) into a *social* space.
- **Reinvention operator:** **Domain Transfer (full).** Take the combat engine's load-bearing structure — 2 actions per Round, slow+fast, positioning, attack vs defense, a Broken threshold — and re-skin every noun. This is the most direct demonstration of the engine's core claim (`12 §12`): *the mechanics barely change; the fiction transforms completely.*
- **Target psychology:** **Attritional / tactical** (`17` M6, recalibrated) — produces *scenes that matter as much as fights.* The point is to make a tense negotiation as mechanically engaging and consequential as a duel, so social-focused characters (and genres) get the same depth of play combat characters always had.
- **Problem solved:** social conflict in both source games is a single opposed roll or at most a short "negotiating position" modifier. That is fine for incidental persuasion, but it makes social play *thin* compared to combat — one roll vs a 6-Round tactical scene. For genres where society *is* the battlefield (court intrigue, drawing-room drama, diplomacy, heist-cons), this is a real gap. This module closes it.

## 2. The generic mechanism

### When it triggers

Social Combat is **not** for every conversation. It triggers when:
1. The stakes are high (a reputation, a marriage, an alliance, a confession, a verdict).
2. There is an *opponent* with their own agenda who will not simply yield.
3. Failure has real consequence (loss of standing, a door closed, a relationship Broken).

For casual persuasion, use a single social roll (`03 §11`). Reserve Social Combat for scenes that *deserve* a scene.

### The structural reskin

| Combat concept | Social Combat equivalent |
| --- | --- |
| **Round** | One exchange of the conversation (~30 seconds of in-fiction talk) |
| **Turn** | One speaker's contribution |
| **Range band** | **Social distance** — Intimate / Personal / Professional / Public (see below) |
| **Zone** | **Social context** — Private (drawing room), Semi-private (dinner table), Public (ballroom floor), Performance (the stage / the witness stand) |
| **Slow action** | A full rhetorical move: a speech, a revelation, a pointed question, an appeal to a value |
| **Fast action** | A quick riposte: a quip, a deflection, a gesture, a small lie |
| **Reaction (dodge/parry)** | A **deflection**: Wit to dodge, Composure to parry (absorb the blow) |
| **Damage** | Loss of **Composure** (the social-HP equivalent) — see below |
| **Broken** | **Composure to 0** = a social Broken: an outburst, a storming-out, a capitulation, a tears-and-confession moment |
| **Critical hit** | A perfect line that deals Composure damage + rolls on the **Social Fallout** table (P4) |
| **Weapon** | **Leverage** — blackmail, a secret, a witness, rank, a favor owed. Leverage grants "weapon dice" to your social pool. |
| **Armor** | **Reputation** — established standing absorbs the first hits (an armor rating). |

### Social distance (the positioning layer)

Social distance is the combat's range band. Moves that work at Intimate (a whisper) fail at Public (a declaration). Changing distance is an action.

- **Intimate** — a whisper, a confidence, a private appeal. *Effective for:* vulnerability, threats, confessions. *Ineffective publicly:* deniable.
- **Personal** — a direct address, one-on-one, in others' presence. *Effective for:* persuasion, bargaining, intimidation.
- **Professional** — formal address, court-regulated, role-bound. *Effective for:* precedent, protocol, rank-appeals.
- **Public** — a declaration to the room. *Effective for:* reputation attacks, performance, shaming, rallying. *Cannot be taken back.*

**Weapons (leverage) have range bands too.** A whispered blackmail works Intimate-to-Personal; a public denunciation only works at Public. Mismatching the weapon to the distance imposes the same penalty as range mismatch in combat.

### Composure — the social HP

Each character (PC and NPC) has a **Composure** pool (typically Wits + Empathy, or a dedicated track, 4–8). Social "attacks" deal Composure damage. At 0 Composure, the character is **socially Broken** — they lose the exchange and suffer a Social Fallout roll (typed D66, P4). Composure regenerates slowly (1/scene, or faster with a "compose yourself" fast action).

### The action economy (identical to combat)

Per Round, each speaker gets **one slow action + one fast action, or two fast actions.** Reactions (deflections) draw from the same budget. This is the engine's load-bearing rule, unchanged — which is the whole point.

## 3. The pressure loop

- **Pressure:** Composure depletes; leverage is spent or exposed; distance constrains options.
- **Decision:** *do I spend my leverage now, or save it? do I move to Public distance to land the big attack (and make it permanent)? do I deflect or absorb?*
- **Consequence:** Composure drops; reputations shift; secrets come out; the room's opinion moves.
- **State change:** the relationship between the speakers, and their standing with witnesses, changes materially.
- **Loop shape:** **position → attack/deflect → expose/spend → Break or concede.** Runs at Round cadence (faster than Influence/Faction loops; slower than a single roll).

## 4. Dials

| Dial | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Composure pool size** | Wits + Empathy (variable) | Fixed 6 per character | Build-dependent vs uniform |
| **Composure regen** | 1/scene (slow) | 1/Round with "compose" fast action (fast) | Grueling vs forgiving |
| **Damage scale** | 1–3 per hit (like combat) | 1–2 per hit (lighter) | Lethal social scenes vs prolonged |
| **Leverage (weapons)** | Each secret/blackmail = a die type (D6–D12, consumable) | Flat +1 / +2 modifiers | Resource-economy vs simple |
| **Social distance bands** | All 4 (Intimate→Public) | 2 (Private / Public only) | Rich positioning vs simple |
| **Witnesses / the room** | Track the audience's opinion as a separate shifting modifier | Abstract the room into the GM's framing | Mechanical audience vs narrative |
| **Broken state** | Forced capitulation + Social Fallout roll | Player chooses: concede OR take a permanent Reputation hit to keep fighting | Hard floor vs heroic last-stand |
| **Audience as combatant** | (off) | (on) — the audience is a "third side" whose opinion is a track both speakers compete over | Duel vs debate |

**Calibration guidance:** start with Wits+Empathy Composure, 1/scene regen, 1–3 damage, leverage as consumable dice, all 4 distance bands, audience-as-modifier. Reserve the "audience as combatant" dial for formal debate scenes — it doubles the bookkeeping.

## 5. Integration points

- **Hooks into:** the social-conflict rules (`03 §11`) — this *extends* them, replacing the single roll when stakes warrant. Hooks into the Influence module (`workshop/10`) — Influence can be spent to absorb a social hit or boost an attack. Hooks into the faction web (`workshop/20`) — social combats witnessed by a faction shift Standing. Hooks into harm (`04`) — a Social Fallout roll can deal real Empathy/Docity damage (humiliation hurts).
- **Requires:** a Composure track per participant; defined leverage (what secrets/favors each side has); a sense of the social context (private/public) and the audience.
- **Replaces / extends:** the single social roll — adds the tactical layer for high-stakes scenes.
- **Cross-refs:** `03 §7–§11` (the action economy and social conflict), `17` M6 (recalibration), `04 §5` (typed D66, here as Social Fallout).

## 6. Failure modes & edge cases

- **Using it for everything.** Social Combat is *expensive* (a 4-Round scene per conversation). If every NPC interaction becomes a Social Combat, the game bogs (`19` FE2 decision fatigue; `13 §7.3` GM burden). **Fix:** reserve it for the 3 triggers (high stakes, opposed agenda, real consequence). Use single rolls for the rest.
- **The speaker-skill monopoly.** If only the party's "face" can participate, the other players watch. **Fix:** use the **audience-as-combatant** dial so the room (including other PCs) can be swayed/argued-for; allow PCs to "help" with fast-action interruptions (a witty aside, a dropped hint) using their own skills.
- **Composure-bag-of-HP.** If Composure is just depleting HP, social combat feels like combat-with-different-nouns. **Fix:** the *social distance* layer is the distinguishing tactic — make changing distance and matching leverage-to-distance the core decision, not just damage races.
- **Leverage inflation.** If players stockpile 5 black-mails and dump them in one scene, every social combat is a one-shot. **Fix:** leverage is *consumable* (a secret used is a secret spent) and *distance-gated* (a given leverage works at one distance band only).
- **The GM-fiat audience.** If the audience's opinion is pure GM whim, players feel the scene is rigged (`19` FE5). **Fix:** when using the audience modifier, define it up front (the room starts at +1 toward the NPC, say) and shift it only on defined triggers (a successful Public attack, an exposed secret).

## 7. Validation notes

- **Math (`13 §3`):** Composure pools and damage should be tuned so a typical Social Combat resolves in 3–5 Rounds (like a real fight). At 1–3 damage and Wits+Empathy pools (4–8), this holds. If scenes drag, raise damage or lower pools.
- **Exploits (`13 §5`):** the leverage-inflation risk (above) is the main one. The "two-fast-action spam" of weak quips is gated by the same rule that gates it in combat (the GM rules quips ineffective against a serious slow-action attack).
- **Felt experience (`19`):** the *audience* dial is the key psychology — it makes the scene feel like a *performance*, which is what high-society/diplomatic scenes are about (C5 agency ledger: the room's opinion is the real prize, not just the opponent's). The distance layer prevents FE1 (false choice) by ensuring not every move works at every range.

## 8. Worked genre example — Regency high society

**The setting:** A country-house ball, 1813. The PCs are trying to secure the Duke's blessing for a marriage — but the Duke's sister opposes it, and the Duchess's companion holds a secret that could ruin the PC's suit.

**Dials set:** Composure = Wits + Empathy; regen 1/scene; damage 1–3; leverage as consumable D6/D8/D10 dice; all 4 distance bands; **audience as modifier** (the room starts at +1 toward the sister — she is the favored hostess).

**The cast's leverage:**
- PC (Eleanor): a D8 leverage = a letter proving the sister's own elopement (blackmail, consumable).
- The sister (Lady Caroline): a D6 leverage = a whispered rumor about Eleanor's mother (a secret, consumable) + her native Reputation armor (+1).
- The companion (Mrs. Jennings): neutral, but holds a D10 = the actual truth about Eleanor's birth (could be exposed by either side).

**In use (excerpt):**

- **Round 1.** Eleanor opens at **Professional distance** (formal suit-presentation) with a slow action: a speech appealing to the Duke's honor. Pool: Empathy 3 + Performance 2 + leverage 0 = 5 dice; 2⚔ — a clean hit, 2 Composure damage to the Duke (who is the *audience-object* here, not the opponent). The Duke warms.
- Lady Caroline **reacts** (deflect): a fast-action quip undermining the speech. She rolls Insight vs Eleanor's ⚔ count, partially deflects (−1 ⚔). She then takes her slow action: **moves the conversation to Personal distance** and deploys her rumor-leverage (D6) — "Of course, we must consider what we *know* of the girl's mother..." Pool: Wits 3 + Insight 2 + leverage D6 = 6 dice; 1⚔ — a glancing blow, 1 Composure to Eleanor.
- **Round 2.** Eleanor **moves to Intimate distance** (a confidence, stepping to the window) and **spends her leverage** (the letter, D8) — "I wonder what the Duke would make of *your* letter, Caroline." This is a big move: Intimate-distance leverage at the right band. Pool: Empathy 3 + Manipulation 2 + leverage D8 = 5 dice + 1 from the leverage's 8 = 6 effective; 3⚔ — a critical. Lady Caroline takes 3 Composure damage (now at ~2/5) and must roll on the **Social Fallout table** (typed D66, "humiliation" family): rolls a 23 = "public composure breaks; storms from the room." The audience modifier flips to +2 toward Eleanor. The Duke, seeing his sister flee, grants the blessing.

**Why this works in Regency:** the *audience* dial models the reality that drawing-room drama is *performative* — what matters is who the room thinks won. The *social distance* layer maps perfectly onto Regency etiquette (a whisper vs a public declaration are wildly different moves with different consequences). Leverage as consumable dice makes secrets *spent*, not just known — which is exactly how blackmail works (you can only play a card once).

**Re-skin for your genre:**
- **Diplomacy / treaty negotiation:** distance bands = bilateral / small-group / plenary / public-communiqué; leverage = intelligence, economic threats, third-party guarantees; Broken = a walking-out or a signature.
- **Courtroom drama:** distance = sidebar / cross-exam / closing / press-conference; leverage = evidence, precedents, witness credibility; the jury = the audience track.
- **Interrogation:** distance = off-the-record / formal / recorded / public-charges; leverage = evidence, immunity, protection; Broken = a confession.
- **Market haggling (high-stakes):** distance = back-room / counter / floor / public-auction; leverage = rival offers, insider knowledge; Broken = a deal closed.
- **Greek symposium / philosophical duel:** distance = aside / discourse / challenge / public-lecture; leverage = citations, paradoxes, witnesses; Broken = a public refutation.
