<!-- markdownlint-disable MD013 MD024 -->

# Influence & Political Power — Spendable Standing

> **STATUS: WORKSHOP MODULE.** A political-capital rule set: fictional standing converted into a spendable, *decaying* influence pool with an attrition cost. *Core is generic; the worked example (Renaissance Florence) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic design space
3. The pressure loop
4. Choices
5. Integration points
6. Failure modes & edge cases
7. Check notes
8. Worked genre example — Renaissance Florence

## 1. Origin — how this was built

- **Source pattern:** **P2 (capped pool refueled by risk)** from `16`, fused with **P4 (typed D66)** for the scandal layer.
- **Reinvention operator:** **Domain Transfer + Inversion.** Domain-transfer P2 from "personal resolve" (WP/Faith) to "social standing." Then *invert*: where WP refuels when the character takes risks, Influence *refuels when the character demonstrates public virtue* — but *decays when unused*.
- **Target psychology:** **Action-refuel + decay** (`17` M1) — an *investment loop* (cultivate, spend, scramble to rebuild). The decay valve makes Influence a resource you cannot hoard, only circulate.
- **Problem solved:** RPG political play is usually either (a) a single roll with no texture, or (b) a heavy faction-turn sub-game above the players. This gives political capital the same dramatic rhythm the push economy gives combat — a pool that rises and falls *in play*, gated by player choices, with scandals as the bane-equivalent.

## 2. The generic design space

### 2a. Rule overview

**Influence** is a character-tracked pool (cap 10) representing current social/political capital — how much weight the character's name carries *right now* with a defined constituency (court, guild, senate, neighborhood, clan, board). It is spent to compel, gain access, absorb social failures, and shift decisions; it is earned by public witnessed acts; and it **decays** at each downtime boundary unless actively cultivated. Scandals (public failures, exposed secrets) deal Influence damage via a typed D66 roll.

### 2b. NEW CONCEPTS introduced

- **NEW CONCEPT — Decay valve:** No core engine Willpower/Faith (WP, Faith) decays when unused. Influence steps down by 1 at each downtime boundary unless the PC has actively cultivated it that cycle. This converts the pool from a savings account into a current — standing not maintained evaporates. *Extends the engine by adding a maintenance pressure the core pools do not have.*
- **NEW CONCEPT — Constituency scoping:** Core reputation (FL) is local-settlement; core Faith is personal. Influence is *segmented by constituency* — a PC may have separate Influence pools with the Court, the Church, the Street, etc., and Influence spent in one does not transfer to another. *Extends the engine by making social capital a multi-track resource rather than a single modifier.*
- **NEW CONCEPT — Scandal as bane-equivalent:** Core banes (💀) are a dice-face cost. Scandals are an *event-triggered* cost — a public failure or exposed secret rolls a typed D66 that deals Influence damage. *Extends P4 (typed D66) from harm/mishap domains to the political domain, with a distinct trigger model.*

### 2c. Rules reference (tables & procedures)

#### The Influence pool

- **Cap:** 10 (per constituency). Start at 4 in your home constituency, 0 elsewhere.
- **Track:** per PC, per constituency. If using a single constituency, one pool. If multi, one pool each (cap the number of tracked constituencies at 1–2 per PC to control bookkeeping — §6).

#### Spend-cost schedule

| Spend | Cost (Influence) | Effect |
| --- | --- | --- |
#### Spend-cost schedule

**Gain audience** with a figure who would otherwise refuse you. Cost: 1 Influence. The meeting happens; no roll is required. Your name opens the door.

**Compel a NPC of lesser standing** to do something within their power. Cost: 1 Influence. This is a minor ask — a letter written, a passage granted, a small lie told on your behalf. The NPC complies because refusing you costs more than obeying.

**Compel a NPC of equal standing.** Cost: 2 Influence. This is a moderate ask — a vote cast your way, a timely appearance at a gathering, a concealment of something you'd rather not have known. The NPC complies, but they expect the favor remembered.

**Compel a NPC of greater standing.** Cost: 3 Influence. This is a major ask — a pardon issued, a contract awarded, a public endorsement. You are calling in chips with someone who outranks you, and the spend reflects the weight of the ask.

**Absorb a social failure.** Cost: 1 Influence per consequence negated. You throw your weight around — the failed roll's consequence is canceled, the social misstep is smoothed over. The spend is visible: everyone saw you lean on your name to escape the result.

**Shift a settlement or faction decision by one step.** Cost: 2 Influence. A verdict moves from "guilty" to "suspended." A tender moves from "the rival" to "you." A patrol route shifts away from your district. You are not changing minds; you are changing outcomes.

*Stakes test:* if the ask exceeds what the NPC can do or would do for anyone of your standing, the GM rules the spend invalid. Influence is not mind control — it is the weight of your name, and it has limits.

#### Earning Influence — the Public Act table (D66)

Roll once per public, witnessed act that builds your name (the GM calls for the roll; players cannot farm private acts). Add the constituency modifier: +1 if the act aligns with the constituency's values, −1 if it offends them.

| D66 | Result | Influence gained |
| --- | --- | --- |
| 11–22 | **Forgettable.** The act was witnessed but made no impression. | +0 |
| 23–34 | **Noted.** A modest show; the constituency remembers you. | +1 |
| 35–46 | **Talked of.** A clear display of the constituency's virtue or a costly public victory. | +2 |
| 47–55 | **Celebrated.** A heroic, costly, or spectacularly apt public act. | +3 |
| 56–64 | **Legendary.** The act will be retold; the constituency claims you as their own. | +4 |
| 65 | **Mixed blessing.** The act raises your standing but also raises expectations (see §6). | +3, but the next decay hits for −2 not −1. |
| 66 | **Cult figure.** You become a symbol; the constituency will defend you — but rivals now see you as a threat. | +5, and pick one rival constituency: their Standing with you drops by 2. |

#### The decay procedure

1. **When it fires:** at each downtime boundary (end of session, or season turn if using slower pacing — see Choices).
2. **The cultivation test:** did the PC perform at least one public, constituency-appropriate act this cycle? (GM judgement — a single public action suffices; pure hoarding does not.)
3. **If yes:** no decay. The PC maintained their profile.
4. **If no:** Influence steps down by 1 (to a minimum of 0). Standing not maintained evaporates.
5. **The 65-row exception:** a "Mixed blessing" result (above) hits for −2 on the next decay, even if cultivated — the raised expectations cost.

#### The Scandal Roll (typed D66)

**Trigger:** a public failure, an exposed secret (Dark Secret, `01 §6`), a flagrant violation of the constituency's values, or a defeated social-combat opponent who chooses to "ruin" you rather than concede (`03`).

**Severity dice:** roll 1D6 (minor) to 4D6 (grave), set by the GM based on the scandal's weight. Each 💀 (1) rolled = −1 Influence. Then roll on the table below for the *nature* of the fallout (typed by constituency family). The constituency is the one whose values were offended.

**Scandal Fallout table (D66) — Court / elite constituency family**

| D66 | Result | Rule effect |
| --- | --- | --- |
| 11–14 | **Whisper campaign.** Snide remarks at the next gathering. | −1 Influence (in addition to the severity-die loss). |
| 15–22 | **Cold shoulder.** Key figures refuse audiences for a session. | Cannot spend Influence on "access" for one session. |
| 23–31 | **Public slight.** A rival denounces you in a public forum. | −2 Influence; the rival gains +1. |
| 32–41 | **Loss of patronage.** A patron withdraws support. | Lose 1 ongoing benefit (a stipend, a post, a protector's name). |
| 42–51 | **Scandalous rumor.** A specific calumny spreads. | Standing with one *ally* constituency drops by 1 (propagation-lite). |
| 52–61 | **Formal censure.** The constituency's governing body rebukes you. | −3 Influence; cannot hold office/position for a season. |
| 62–64 | **Exposure.** A secret is now public knowledge. | The Dark Secret is "spent" (no longer usable as a hook); −2 Influence. |
| 65 | **Disgrace.** You are cast out of the constituency's inner circle. | Influence drops to 0; regain at half-rate (cap 5) until a redemption arc. |
| 66 | **Banishment / excommunication.** You are named anathema. | Influence drops to −3 (active hostility); the constituency will act against you. |

*Other constituency families use the same D66 architecture with re-skinned rows: Church (pious → heretic axis), Street (respected → marked axis), Guild (licensed → blacklisted axis), Military (decorated → cashiered axis). Build one family per constituency type in your campaign.*

## 3. The pressure loop

- **Pressure:** Influence decays; scandals threaten it; big asks require more than you have.
- **Decision:** *spend now on this ask, or hoard for the bigger one? take the risky public move that could earn or could scandalize?*
- **Consequence:** spending depletes; scandals deplete; cultivation restores.
- **State change:** your standing in the constituency shifts, opening/closing doors.
- **Loop shape:** **cultivate → spend → scandalize/recover → cultivate.** Runs at session/season cadence — a *strategic* resource, not a tactical one.

## 4. Choices

| Choice | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Cap** | 10 (single constituency) | 5 × multiple constituencies (track separately) | Broad vs segmented power |
| **Decay rate** | −1 per session (fast) | −1 per season (slow) | Maintenance pressure vs relaxed accumulation |
| **Scandal severity** | 💀 per die, 1–4 dice | Fixed −2 on any scandal | Variable dread vs predictable cost |
| **Cultivation requirement** | Any public virtue act | Constituency-specific act (patronage for Church, victory for Army) | Easy vs demanding maintenance |
| **Constituency scope** | One (home court) | Many (track per faction) | Simple vs factional-politics depth |
| **Scandal source** | GM-authored (exposed secrets, public fails) | Player-declared (the PC chose the risky public move) | External-pressure vs player-driven |

**Default:** cap 10, decay −1/session, scandal = 💀 per die, one constituency. Add segmentation only if political play is a *pillar*.

## 5. Integration points

- **Hooks into:** social conflict (`03 §11`) — Influence substitutes for "negotiating position" or buys off a social failure. Org layer (`07`) — Influence with a faction gates what org functions you can request. Encounter engine (`09 §4`) — high Influence shifts encounter tables (allies seek you; rivals target you). Faction web (`workshop/02`) — Influence is the per-PC face of faction Standing.
- **Requires:** a defined constituency and a downtime cadence.
- **Replaces / extends:** flat Reputation modifiers — a dynamic pool with a maintenance cost instead of a static +1.
- **Cross-refs:** `00 §7` (Willpower/Faith), `17` M1 (refuel psychology), `09` (settlement/faction standing).

## 5a. Handshake

- **Prerequisites:** persistent constituencies, social access, and downtime or scene boundaries.
- **Inputs:** constituency list, Influence cap, decay cadence, public-act triggers, scandal family.
- **Outputs:** Influence pools, spend menu, decay procedure, scandal events.
- **Touched systems:** social conflict, faction/base, GM encounters, reputation.
- **Replaces or stacks:** replaces generic reputation bonuses; stacks with Debt only when Influence buys access and Debt records obligation.
- **Incompatibilities:** merge with Reputation/Renown if both track the same public audience.

## 6. Failure modes & edge cases

- **Influence-as-bribe-currency.** If spendable to bypass every obstacle, it trivializes other loops. **Fix:** Influence only works *within its constituency* and only for asks *within the NPC's power/values.* (`13 §5.5` action-budget abuse.)
- **Hoarding.** Without decay, players bank to 10 and sit. **Fix:** the decay valve is non-negotiable.
- **Scandal farming.** If scandals are the only way to lose Influence, players avoid public action. **Fix:** ensure public action is also the primary *earn* vector — the risk is the point. (`19` FE3 — scandals must feel *earned*, not random.)
- **Constituency explosion.** 5 pools per PC per faction is bookkeeping hell. **Fix:** cap at 1–2 active constituencies per PC.
- **The GM-fiat scandal.** If scandals fire on GM whim, players feel targeted (`19` FE5). **Fix:** tie scandals to *exposed* secrets or *witnessed* failures, not GM mood.

## 7. Check notes

- **Math (`13 §3`):** at −1/session with cap 10, a PC must earn ~1 Influence/session to hold steady — one public victory or two virtue displays. This matches the engine's XP cadence (`02 §3`), so it feels proportional. The Public Act table's expected value is ~+1.5 per roll (most results 23–46), so one public act per session roughly offsets decay.
- **Abuses (`13 §5`):** universal-solvent risk gated by constituency-scope; cap-bypass via trivial cultivation gated by GM judgement + the constituency-specific choice.
- **Felt experience (`19`):** the decay valve prevents hoarding-stagnation (C5 agency ledger). Scandals need telegraphing (C2 perceived randomness) — foreshadow that a secret is at risk before rolling.

## 8. Worked genre example — Renaissance Florence

**Setting:** Florence, 1490s. PCs are minor nobles, merchants, and condottieri navigating the Medici court, the rival guilds, Savonarola's friars, and the street.

**Settings chosen:** cap 10; decay −1/session; scandal = 💀 per die (1–4); four constituencies (Court / Guilds / Church / Street); cultivation requires a constituency-appropriate public act.

**In use:**

- **Isabella** has Court Influence 6, Church Influence 3. She wants an audience with the Cardinal (1 point, Church) — pays it, now at 2. She sponsors a public masque (Court-appropriate cultivation) — GM calls for a Public Act roll; she rolls 36 (**Talked of**), +2 Court, now at 8.
- A rival exposes her secret atheism — GM calls for a Church Scandal Roll, severity 3 (grave for a pious constituency). She rolls 3D6: results 1, 3, 5 → one 💀 → −1 Church Influence (now 1). Then rolls on the Church Scandal Fallout table: a 62 (**Formal censure**) → −3 Influence → Church drops to −2 (active hostility); the friars denounce her. To recover she must publicly sponsor a chapel restoration (+1 Church via Public Act, slow rebuild).
- **The spend-or-hoard decision:** Isabella considers spending 3 Court Influence to compel a Medici cousin to quash a lawsuit. She has 8 — spending 3 leaves 5, and decay at session-end takes her to 4 unless she cultivates. She judges the ask worth it. The Medici cousin intervenes. Next session she must find another public act or watch her Court standing wither.

**Why Florence:** the decay valve models Renaissance political reality — *favour is a current, not a reservoir.* Scandals make secrets dangerous in the rules. Four constituencies create the cross-pressures Florentine politics is famous for (what pleases the Court offends the Church).

**Re-skin:**
- **Corporate sci-fi:** constituencies = Board / Craft / Sales / Regulators; scandals = leaked memos; cultivation = shipped products / PR wins.
- **Feudal Japan:** constituencies = Clan / Shogunate / Temple / Town; scandals = bushidō breaches; cultivation = duels won, poems composed.
- **Modern political thriller:** constituencies = Party / Press / Donors / Voters; scandals = oppo hits; cultivation = news cycles won.
