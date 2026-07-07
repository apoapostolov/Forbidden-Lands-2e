<!-- markdownlint-disable MD013 MD024 -->

# Influence & Political Power — Spendable Standing

> **STATUS: WORKSHOP MODULE.** A political-capital subsystem. Converts fictional standing (renown, rank, faction favor) into a spendable influence pool with an attrition cost, calibrated for a target psychology. *Core is generic; the worked example (Renaissance Florence) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic mechanism
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — Renaissance Florence

## 1. Origin — how this was built

- **Source primitive:** **P2 (capped metacurrency refueled by risk)** from `16`, fused with a touch of **P4 (typed D66)** for the scandal/consequence layer. The base insight: political capital *is* a metacurrency — a capped pool that spends on agency and refuels from engaging the system's risk mechanics.
- **Reinvention operator:** **Domain Transfer + Inversion.** Domain-transfer P2 from "personal resolve" (WP/Faith) to "social standing." Then *invert* the polarity: where WP/Faith refuels when the character takes risks, Influence *refuels when the character demonstrates public virtue or wins public victories* — but *decays when unused* (a standing not maintained fades). The inversion produces a maintenance pressure rather than a risk pressure.
- **Target psychology:** **Action-refuel + decay** (`17` M1) — produces an *investment loop* (cultivate standing over time, spend it on big asks, scramble to rebuild it). The decay valve is the new contribution: it makes Influence *a resource you cannot hoard*, only circulate.
- **Problem solved:** RPG political play is usually either (a) a single die roll ("Persuade the Duke: 2⚔, he agrees") with no texture, or (b) a heavy faction-turn sub-game above the players. This module gives political capital the same dramatic rhythm the push economy gives combat — a pool that rises and falls *in play*, gated by player choices, with scandals as the "bane" equivalent.

## 2. The generic mechanism

**Influence** is a character-tracked pool (cap 10) representing their current social/political capital — how much weight their name carries right now with the relevant constituency (court, guild, senate, neighborhood, clan, board).

**Spending Influence.** A PC may spend Influence to:
- **Compel a NPC** of lesser or equal standing to do something within their power (1–3 points by stakes).
- **Gain audience/access** with a figure who would otherwise refuse them (1 point).
- **Absorb a social failure** — cancel a failed social roll's consequence by "throwing your weight around" (1 point per consequence negated).
- **Shift a settlement/faction decision** in your favor by one step (2 points).

**Earning Influence.** Influence is *earned* by public, witnessed actions that build your name:
- A public victory that matches the constituency's values (slay the beast threatening the town, win the trial, close the deal) — +1, +2 if it was costly or heroic.
- A display of the constituency's virtue (generosity to the poor, patronage of the arts, public piety) — +1.
- A successful social roll *in public* where you exceed the threshold by 2+ ⚔ — +1 (excellence is its own advertisement).

**The decay valve (the core innovation).** At each **downtime boundary** (end of session / season turn / whenever the campaign advances time), each character's Influence **steps down by 1** unless they have *actively cultivated* it that cycle (the GM judges "actively cultivated" — a single public action suffices; pure hoarding does not). This mirrors the real-world reality that *standing not maintained evaporates.* The decay is what makes Influence a *loop* rather than a savings account.

**Scandals — the "bane" equivalent.** A public failure, an exposed secret, a flagrant violation of the constituency's values triggers a **Scandal Roll**: roll a number of D6 equal to the severity (1–4), each 💀 = −1 Influence. This is the inverted-cost-face: where combat's push costs body, political play's "push" (a bold public move) costs standing if it backfires.

## 3. The pressure loop

- **Pressure:** Influence decays; scandals threaten it; big asks require more than you have.
- **Decision:** *do I spend now on this ask, or hoard for the bigger one? do I take the risky public move that could earn or could scandalize?*
- **Consequence:** spending depletes; scandals deplete; cultivation restores.
- **State change:** your standing in the constituency shifts, opening/closing doors.
- **Loop shape:** **cultivate → spend → scandalize/recover → cultivate.** The loop runs at session/season cadence, not Round cadence — it is a *strategic* resource, not a tactical one.

## 4. Dials

| Dial | Setting A | Setting B | Psychology produced |
| --- | --- | --- | --- |
| **Cap** | 10 (single constituency) | 5 × multiple constituencies (track separately) | Broad vs segmented power |
| **Decay rate** | −1 per session (fast) | −1 per season (slow) | Maintenance pressure vs relaxed accumulation |
| **Scandal severity** | 💀 per die, 1–4 dice | Fixed −2 on any scandal | Variable dread vs predictable cost |
| **What "cultivation" requires** | Any public virtue act | A *constituency-specific* act (patronage for the Church, victory for the Army) | Easy vs demanding maintenance |
| **Constituency scope** | One (the PC's home court) | Many (track Influence separately per faction) | Simple vs factional-politics depth |
| **Scandal source** | GM-authored (exposed secrets, public fails) | Player-declared (the PC *chose* to take the risky public move) | External-pressure vs player-driven |

**Calibration guidance:** start with cap 10, decay −1/session, scandal = 💀 per die, one constituency. Add segmentation (multiple constituencies) only if political play is a *pillar* of the campaign — it adds bookkeeping.

## 5. Integration points

- **Hooks into:** the social-conflict system (`03 §11`) — Influence can substitute for a social roll's "negotiating position" modifier, or buy off a social failure. Hooks into the org layer (`07`) — a PC's Influence with a faction gates what org functions they can request. Hooks into the GM's encounter engine (`09 §4`) — high Influence shifts encounter tables (allies seek you out; rivals target you).
- **Requires:** a defined **constituency** (who you have standing *with*) and a **downtime cadence** (when decay fires).
- **Replaces / extends:** flat "Reputation" modifiers — instead of a static +1, you have a dynamic pool with a maintenance cost.
- **Cross-refs:** `00 §7` (metacurrency abstraction), `17` M1 (refuel-trigger psychology), `09` (settlement/faction standing).

## 6. Failure modes & edge cases

- **Influence-as-bribe-currency.** If Influence can be spent to bypass *every* obstacle, it becomes a universal solvent and trivializes the engine's other loops. **Fix:** Influence only works *within its constituency* and only for asks *within the NPC's power/values.* You cannot spend Church Influence to compel a crime boss. (`13 §5.5` action-economy abuse variant.)
- **Hoarding.** Without decay, players bank Influence to 10 and sit on it. **Fix:** the decay valve is non-negotiable — it is the whole pressure source.
- **Scandal farming.** If scandals are the only way to *lose* Influence, players avoid public action entirely. **Fix:** ensure public action is also the primary *earn* vector — the risk is the point. (Cross-ref `19` FE3 swinginess-as-unfairness — scandals need to feel *earned*, not random.)
- **Constituency explosion.** Tracking 5 Influence pools per PC per faction is bookkeeping hell. **Fix:** cap at 1–2 active constituencies per PC; abstract the rest into a single "general standing" modifier.
- **The GM-fiat scandal.** If scandals fire purely on GM whim, players feel targeted (`19` FE5 "too unfair"). **Fix:** tie scandals to *exposed* secrets (player-authored risk) or *witnessed* failures (mechanical triggers), not GM mood.

## 7. Validation notes

- **Math (`13 §3`):** the decay rate sets the maintenance burden. At −1/session with cap 10, a PC must earn ~1 Influence per session to hold steady — roughly one public victory or two virtue displays. This matches the engine's XP budget cadence (`02 §3`), so it should feel proportional.
- **Exploits (`13 §5`):** the universal-solvent risk (above) is the main one; gated by constituency-scope. Cap-bypass via "I cultivate trivially" is gated by the GM's "actively cultivated" judgement + the constituency-specific dial.
- **Felt experience (`19 §7` Stage C):** the decay valve is the key psychology — it prevents the hoarding-stagnation that would otherwise make the pool boring (C5 agency ledger: maintenance *keeps the player's choices mattering*). Scandals need telegraphing (C2 perceived randomness) — the GM should foreshadow that a secret is at risk before rolling.

## 8. Worked genre example — Renaissance Florence

**The setting:** Florence, 1490s. The PCs are minor nobles, merchants, and condottieri navigating the Medici court, the rival guilds, the Dominican friars (Savonarola's camp), and the street.

**Dials set:** Cap 10; decay −1 per session; scandal = 💀 per die (1–4 by severity); four constituencies tracked (Court / Guilds / Church / Street); cultivation requires a constituency-appropriate public act.

**In use:**

- **Isabella**, a patron of the arts, has **Court Influence 6, Church Influence 3.** She wants an audience with the Cardinal (1 point, Church) — she pays it, now at 2. She then sponsors a public masque (Court-appropriate cultivation) — +1 Court, now at 7. A rival exposes her secret atheism — GM calls for a Church Scandal Roll, severity 3 (grave for a pious constituency). She rolls 3D6, gets two 💀 — Church Influence drops to 0. She is *effectively excommunicated socially*; the friars denounce her from the pulpit. To recover she must publicly sponsor a chapel restoration (+1 Church, slow rebuild).
- **The spend-or-hoard decision:** Isabella's player considers spending 3 Court Influence to compel a Medici cousin to quash a lawsuit. She has 7 — spending 3 leaves 4, and decay at session-end will take her to 3 unless she cultivates. She judges the ask worth it and spends. The Medici cousin intervenes. Next session she must find another public act or watch her Court standing wither.

**Why this works in Florence:** the decay valve models the reality of Renaissance politics — *favour is a current, not a reservoir.* You are only as powerful as your last conspicuous display. The scandal mechanism makes secrets (Dark Secrets, `01 §6`) mechanically dangerous in a political campaign. The four constituencies create the cross-pressures Florentine politics is famous for (what pleases the Court offends the Church).

**Re-skin for your genre:**
- **Corporate sci-fi:** constituencies = Board / Engineering / Sales / Regulators; scandals = leaked memos; cultivation = shipped products / PR wins.
- **Feudal Japan:** constituencies = Clan / Shogunate / Temple / Town; scandals = breaches of bushidō; cultivation = duels won, poems composed, retainers gifted.
- **Modern political thriller:** constituencies = Party / Press / Donors / Voters; scandals = oppo hits; cultivation = news cycles won, fundraisers headlined.
