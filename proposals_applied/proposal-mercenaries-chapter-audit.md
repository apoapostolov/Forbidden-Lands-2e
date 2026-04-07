# Proposal: Chapter 12 — Mercenaries of the Forbidden Lands — Full Audit

**Scope:** Fresh Design, Synergy, and Balance analysis of the complete 13-file mercenary chapter in its current state, plus prose consistency and wording fixes.

**Method:** Each finding is tagged with a verdict (PASS / FLAG / ISSUE), a severity, and a specific fix where applicable. FLAGs are items that work but could be improved or may confuse GMs. ISSUEs are items that need resolution before the chapter ships.

---

## Part 1 — Design Analysis

### 1.1 Rule Loop Completeness

| SUBSYSTEM         | TRIGGER                | DECISION                     | ROLL                                      | CONSEQUENCE                                      | STATE CHANGE                     | VERDICT              |
| ----------------- | ---------------------- | ---------------------------- | ----------------------------------------- | ------------------------------------------------ | -------------------------------- | -------------------- |
| MORALE            | Grievance event        | Captain addresses or ignores | MANIPULATION vs difficulty                | Clear / harden / stack                           | MORALE ±1                        | **PASS**             |
| Named Man Loyalty | Trigger hit            | Captain responds or ignores  | Loyalty roll                              | Stay / depart / betray                           | Loyalty ±1                       | **PASS**             |
| Contracts         | Find work              | Negotiate terms              | MANIPULATION vs employer tier             | Accept / reject / concession                     | Allegiance ±1, coin              | **PASS**             |
| Tribute           | Arrive at settlement   | Demand or trade              | MANIPULATION or INTIMIDATION              | Tribute / resistance / feud                      | Standing ±, depletion            | **PASS**             |
| Caster WP         | Spell needed           | Cast or conserve             | Spell roll + WP spend                     | Effect / mishap / empty                          | WP reduced                       | **FLAG** — see 1.2.1 |
| Host Ledger       | Warmaster decision     | Execute or challenge         | MANIPULATION vs authority                 | Ledger ±1                                        | Authority threshold shift        | **PASS**             |
| Arguments         | Pressure trigger       | Intervene or escalate        | MANIPULATION / INTIMIDATION / PERFORMANCE | Resolve / harden / blood                         | Grievance difficulty ±, MORALE ± | **PASS**             |
| Blood Oaths       | Sworn commitment       | Honor or break               | Loyalty roll on conflict                  | Hesitation / compliance / betrayal               | Reputation ±, Loyalty ±          | **PASS**             |
| Territory Marking | Engagement / execution | Post markers or don't        | None (automatic)                          | Standing / Feud Track / MORALE check on entrants | Territory held                   | **PASS**             |

#### 1.2.1 FLAG — Caster WP: Missing Edge at Zero

The caster WP loop is complete in normal operation but has no rule for what happens when a caster reaches 0 WP mid-spell. Does the spell fizzle? Does a mishap fire? The current text says NPC casters push exactly like PCs, but the PC rules assume the player decides when to push — there is no scenario where a PC is forced to cast at 0 WP.

**Fix:** Add one sentence to Section 7 (Hired Casters), after the WP recovery paragraph:

> A caster at 0 WP cannot cast. If a caster is reduced to 0 WP by a mishap during casting, the spell fails and the mishap applies. The caster does not cast again until at least 1 WP recovers.

#### 1.2.2 FLAG — Allegiance Decay Over Time

Allegiance (0–4) has clear gain and loss rules for active events (contract completion, breach, competing work) but no rule for what happens when a band goes an entire season without engaging with an employer. Does Allegiance persist indefinitely? A band that completed one contract for a warchief two years ago and never returned should not still be at Allegiance 2.

**Fix:** Add to Section 4 (Contracts and Bounties), Allegiance Mechanics:

> Allegiance decays by 1 at the end of any full season in which the band neither completed a contract for the employer nor made contact. Minimum 0. Allegiance 4 (Sworn) decays to 3 after one season of no contact, which also ends the exclusivity obligation.

---

### 1.3 Integration Gaps

#### 1.3.1 ISSUE — TRAINING GROUNDS / SHOOTING RANGE Prerequisite Contradiction

Appendix A (Integration) states that TRAINING GROUNDS and SHOOTING RANGE are prerequisites for Veteran and Elite recruitment, respectively. But Section 6 (Named Men) and Section 2 (Recruitment and Pay) describe recruiting Veterans and Elites from settlements with no mention of stronghold prerequisites.

Both cannot be true. If a band without a stronghold cannot recruit Veterans, most early-game play breaks because Named Men are predominantly Veterans.

**Fix:** Clarify in Appendix A that TRAINING GROUNDS and SHOOTING RANGE enable **on-site training** (upgrading existing Common fighters to Veteran/Elite at the stronghold), not **field recruitment**. Field recruitment from settlements follows the rules in Section 2 without stronghold prerequisites. Add one sentence:

> TRAINING GROUNDS and SHOOTING RANGE allow the captain to train Common fighters into Veterans and Elites at the stronghold during downtime. They are not required for recruiting Veterans and Elites in the field — those are hired as-is from settlements under the rules in the Recruitment section.

#### 1.3.2 FLAG — STEWARD Referenced but Undefined

The War Room mechanics (Section 8) reference a STEWARD for standing orders. STEWARD is a stronghold hireling from THE STRONGHOLD chapter. The mercenary chapter does not restate what a STEWARD does or how to acquire one.

**Fix:** Add a parenthetical after the first STEWARD reference in the War Room section:

> ...the leader may leave standing orders with a STEWARD (a stronghold hireling; see **THE STRONGHOLD** chapter) that trigger under named conditions.

#### 1.3.3 FLAG — Protection Season Undefined in Chapter

"Protection season" is referenced in Host Play (Section 10) and implied in the contracts table, but never formally defined as a term. The reader can infer it means a season-long retainer contract, but it should be stated.

**Fix:** Add to the contract types table footnotes in Section 4:

> **Protection season:** A retainer-length protection contract lasting one full season. The band receives wages only; food is on the band. Combat call-ups are invoiced separately per day. The employer cannot demand action against the band's interest without penalty (see Allegiance 3 safety clause).

#### 1.3.4 FLAG — Named Men per Band Size

The chapter does not recommend how many Named Men a band should have at each size tier. This is the most common GM question at session zero.

**Fix:** Add to Section 1 (Introduction) or Section 6 (Named Men):

> **Guideline:** A Skirmisher band (3–6) operates with 1–2 Named Men. A Warband (7–20) supports 2–4. A Company (21–50) needs 4–8. These are guidelines, not caps — a band heavy on Named Men is expensive and politically complex; a band with too few has no sergeants and no institutional memory.

---

## Part 2 — Synergy Analysis

### Five-Test Results

| SUBSYSTEM                              | Decision Cost                | Risk Exposure               | Opportunity Cost                 | Repeatability           | Campaign Erosion               | VERDICT  |
| -------------------------------------- | ---------------------------- | --------------------------- | -------------------------------- | ----------------------- | ------------------------------ | -------- |
| MORALE + Grievance stacking            | Good                         | Good                        | Good                             | Throttled by events     | Well-paced                     | **PASS** |
| Trust-Held "The Stay"                  | Named Man loses Loyalty      | Captain still fails         | One use per Named Man            | Once per season per man | Self-limiting                  | **PASS** |
| Blood Oath Brotherhood                 | Hesitation round = real risk | Combat exposure             | One oath per pair                | Cannot be re-sworn      | Accumulates weight             | **PASS** |
| Flyting                                | PERFORMANCE roll stakes      | Humiliation at 3+ margin    | Pauses escalation                | Once per argument       | Good tension                   | **PASS** |
| Argument Escalation                    | Intervention costs           | Steel at Stage 3            | Grievance hardens                | Triggered by events     | Grievances compound            | **PASS** |
| Tribute extraction                     | Low                          | Low                         | Low                              | **Repeatable**          | **Settlement decay permanent** | **FLAG** |
| Caster Protection Duty                 | 2 fighters removed           | Caster exposed if both fall | Significant combat cost          | Every engagement        | Sustainable                    | **PASS** |
| Territory Spiked Markers               | One QD per hex               | Standing / Feud cost        | Time cost                        | Degrades in 2 weeks     | Self-limiting                  | **PASS** |
| INTIMIDATION-for-MANIPULATION (Tyrant) | Delayed cost                 | Fear-Held collapse later    | Short campaigns may not see cost | Every check             | **Slow burn**                  | **FLAG** |
| Allegiance 4 Exclusivity               | High (locked in)             | Employer's wars = your wars | No competing work                | Permanent until breach  | Intended constraint            | **PASS** |

#### 2.1 FLAG — Tribute Rotation Exploit

A band can visit settlement A, extract tribute, move to settlement B, extract tribute, move to settlement C, and loop back to A next season. Each settlement has depletion limits (Hamlet 1, Village 2, etc.) but there is no inter-settlement awareness. The band's Standing drops at each settlement independently, but if the band never needs to return for recruitment or contracts, the Standing loss is purely cosmetic.

**Fix:** Add one paragraph to Section 3 (Extortion and Tribute), after the depletion rules:

> **Reputation travels.** When a band extracts tribute from a settlement by INTIMIDATION, word reaches neighboring settlements within one season. Each settlement within two days' travel of the extorted settlement adjusts Standing toward the band by −1, even if the band has never visited. Tribute by MANIPULATION (negotiated, not forced) does not trigger this spread. This prevents systematic rotation — a band that shakes down every village on a circuit will find the circuit closing ahead of them.

#### 2.2 FLAG — Settlement Decay: No Recovery Path

Settlement decay (Section 3) is permanent and has no recovery mechanic. A Hamlet that decays becomes Ruins forever. This is thematically appropriate for the Ravenlands but creates a potential campaign problem: a band that causes too much decay early on destroys the economic infrastructure it depends on.

**Fix:** This is intentional design (the Ravenlands are dying), but add a GM guidance note:

> **GM Note:** Settlement decay is permanent by design. The Ravenlands do not rebuild easily. If the campaign requires a settlement to recover, the GM may allow it as a multi-season project requiring significant external investment (200+ silver in materials and labor, plus a full season of protection). This is not a default rule — it is a campaign rescue valve.

#### 2.3 FLAG — Fear-Held Delayed Cost in Short Campaigns

The Tyrant archetype's INTIMIDATION substitution is powerful and costs nothing in the short term. The Fear-Held collapse mechanics (silent departure, information concealment, covert dissolution) are excellent but require multiple sessions to manifest. A one-shot or short campaign may never see the cost.

**Fix:** No mechanical change needed. Add a GM note to Section 5 (Campaign Life), Tyrant Companies:

> **GM Note:** The Fear-Held collapse is designed for campaigns of three or more sessions. In one-shots or short arcs, the Tyrant archetype will appear strictly superior because the cost has not arrived yet. If running a short game, consider starting a Tyrant band at MORALE 3 instead of 4 to compress the timeline.

---

## Part 3 — Balance Analysis

### Four-Lens Results

| SUBSYSTEM                                                | Mathematical             | Perceived                              | Table-Level                    | Campaign Arc                   | VERDICT   |
| -------------------------------------------------------- | ------------------------ | -------------------------------------- | ------------------------------ | ------------------------------ | --------- |
| Fighter wages (1s/2s/3s per day)                         | Linear, clean            | Fair                                   | Easy to track                  | Sustainable                    | **PASS**  |
| Caster wages (5–8s / 12–18s / 25+s)                      | Exponential by design    | Expensive feels expensive              | Adds tension                   | Master unsustainable = correct | **PASS**  |
| Loot shares (4 archetypes)                               | Differentiated           | Each feels distinct                    | Players choose meaningfully    | Long-term identity             | **PASS**  |
| Contract premium with caster (+35%)                      | Net positive past day 2  | Caster "earns their keep"              | Clear value signal             | Encourages hiring              | **PASS**  |
| MORALE breakpoints (5→1)                                 | Geometric penalty        | Escalating danger                      | Clear decision pressure        | Paces campaign beats           | **PASS**  |
| Grievance escalation (base 1–2, cap 4)                   | Well-bounded             | Visceral at difficulty 4               | Captain fears Stage 3+         | Arguments drive drama          | **PASS**  |
| Warmaster Ledger (−6 to +6)                              | Wide range               | Practical range is −3 to +3            | **Extremes rarely reached**    | Auto-dissolution at −6         | **FLAG**  |
| Warband → Company transition                             | **No intermediate step** | Sudden logistics jump                  | Confusing for new players      | Unclear when to grow           | **FLAG**  |
| Named Man → PC transition (15 XP)                        | Clean conversion         | Feels earned                           | Good individual endgame        | Band-level endgame missing     | **FLAG**  |
| OATH-BREAKER flag (−2 MANIPULATION)                      | Devastating              | **Unclear severity at time of choice** | Trap option if not telegraphed | Potentially campaign-ending    | **ISSUE** |
| Occupation economics (2 per 10 adults, −1 Standing/week) | Costs exceed returns     | **Not clearly communicated**           | GM must calculate for players  | Drain trap                     | **ISSUE** |

#### 3.1 ISSUE — OATH-BREAKER Flag Visibility

The OATH-BREAKER flag (−2 MANIPULATION on all new contract negotiations) is devastating — it essentially halves the captain's effectiveness at finding and negotiating work. It accumulates after 3+ contract breaches. The reversal condition ("publicly honoring a costly obligation") is vague and has no defined metric.

The problem is not the severity — it is the visibility. A player making their second breach may not realize the third will lock them out of most contract negotiation. This is a trap option: a choice that looks acceptable in the moment but produces an outcome the player could not reasonably have predicted.

**Fix (two changes):**

1. Add a warning at the point of the second breach (Section 4, Contracts and Bounties):

> When the band's breach count reaches 2, the GM should state plainly: "One more breach and the band carries the OATH-BREAKER mark. Every new contract negotiation will be two steps harder. Some employers will not meet with you at all." This is not a hidden mechanic. The men know what three breaches means.

1. Define the reversal condition:

> **Clearing OATH-BREAKER:** The captain must publicly complete a contract that demonstrably costs the band more than it pays — a contract taken at a loss, honored through hardship, where walking away would have been the profitable choice. The GM confirms when the obligation qualifies. The flag clears at the end of that contract. The breaches on record remain.

#### 3.2 ISSUE — Occupation Economics Not Legible

Occupation (Section 3) requires 2 fighters per 10 adults, costs −1 Standing per week, and extracts weekly tribute. But the math is buried: a Village (50 adults) needs 10 fighters on garrison, costs 10 silver/week in wages alone, and extracts perhaps 4–8 silver/week in tribute. The band is losing money. This is probably intentional (occupation is supposed to be costly), but it reads like a viable strategy rather than a desperation trap.

**Fix:** Add a summary note after the occupation rules:

> **Note:** Occupation is expensive. The garrison cost in wages typically exceeds the tribute extracted, and Standing drops weekly. Occupation is not a revenue strategy — it is a territorial control tool for situations where holding the ground matters more than the coin. A captain who occupies a settlement for profit will discover the arithmetic does not work within two weeks.

#### 3.3 FLAG — Warmaster Ledger Range

The Warmaster Ledger runs −6 to +6 but practical play is unlikely to reach the extremes. At +4 to +6, authority calls need no MANIPULATION roll — this is unreachable in most campaigns (requires 4–6 consecutive positive events with zero negative ones). At −4 to −6, the Host fractures — but 4–6 consecutive failures without any captain calling an emergency council at −3 seems unlikely.

**Fix:** No mechanical change. Compress the guidance:

> **GM Note:** Most Host campaigns will see the Ledger move between −3 and +3. The extremes (+4 to +6, −4 to −6) are end-of-arc states. If the Ledger has not reached ±3 by mid-campaign, adjust the pace of Ledger-affecting events.

#### 3.4 FLAG — Warband to Company Transition

A Warband (7–20) needs one logistics Quarter Day per day. A Company (21–50) needs two unless a STEWARD or sergeant handles it, reducing to one. The jump from 20 to 21 fighters doubles logistics overhead with no intermediate step. A player approaching the Company threshold has no way to test-drive the increased burden.

**Fix:** Add a transitional rule to Section 1 (Introduction) or Section 5 (Campaign Life):

> **Transition rule:** A band at 15–20 fighters begins to feel the logistics pressure of a Company. At 15+, the captain chooses: run lean (one logistics QD, risk of shortfall — the GM rolls D6 each week; on a 1, one supply category runs short) or run heavy (add the second logistics QD early). This gives the captain a season to decide whether to push past 20 or trim back.

#### 3.5 FLAG — Campaign Endgame Undefined

The chapter describes ongoing mercenary operation and individual Named Man → PC transition (15 XP), but does not define what a band-level endgame looks like. What does "winning" mean for a mercenary campaign? Retirement? A landed title? Taking a seat on a warchief's council? The absence of an endgame definition means the campaign can drift without resolution.

**Fix:** Add an "Endgame" subsection to Section 1 (Introduction) or Section 5 (Campaign Life):

> ### Campaign Endgame
>
> A mercenary campaign does not end when the band runs out of contracts. It ends when the captain decides what the band was for. Three common endings:
>
> **Retirement.** The band disbands on good terms. Named Men scatter. The captain's name persists as a Reputation fact in the settlements that knew the company. Requires: all active contracts completed, all debts settled, MORALE 3+ at dissolution.
>
> **Landed.** The captain takes a title, a stronghold grant, or a warchief's favor and transitions from mercenary leader to landed authority. The band becomes a garrison or a retinue. Requires: Allegiance 3+ with a faction, Reputation 4+, and a demonstrated service that justifies the grant.
>
> **Absorbed.** The band joins a larger Host permanently. The captain becomes a subordinate commander. Individual Named Men may resist or embrace this. Requires: a Host invitation, MORALE 4+, and at least one Named Man at Loyalty 3 who endorses the decision.
>
> The GM and players should discuss endgame direction by mid-campaign. A band with no destination is a band that fights until it cannot.

---

## Part 4 — Wording and Consistency Fixes

### 4.1 ISSUE — Remaining "Hex" References (34 instances across 11 files)

The earlier editorial pass removed hex references from Section 8 (Special Rules), but 34 instances remain across the other files. "Hex" is a game-mechanical grid term that breaks immersion when used in prose and vignettes. The core Forbidden Lands 2E manuscript uses "hex" as a map unit in the JOURNEYS chapter, so mechanical references to "hex" in rules text are acceptable. The problem is "hex" appearing in fiction, examples, and vignettes.

**Fix — three-tier approach:**

1. **Rules text** (tables, mechanics): Keep "hex" where it refers to the map unit. Example: "Route or hex. Employer specifies the ground" (contracts table) — keep as-is.
2. **Prose and examples**: Replace "hex" with appropriate terrain language — "the ground between settlements," "a day's march," "the territory," "the area," etc. Case by case.
3. **Vignettes**: Replace all "hex" with named or described locations. Example: "a marsh hex east of Glethra" → "the marshland east of Glethra."

**Specific replacements (vignettes and examples only — rules text stays):**

| FILE             | LINE | CURRENT                                                          | PROPOSED                                                             |
| ---------------- | ---- | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| 01-introduction  | 23   | "change who controls a hex"                                      | "change who controls a stretch of road"                              |
| 01-introduction  | 47   | "Twenty men in a hex with poor hunting"                          | "Twenty men in barren country with poor hunting"                     |
| 03-extortion     | 133  | "The hex becomes Ruins"                                          | "The settlement becomes Ruins"                                       |
| 03-extortion     | 145  | "passes through the same hex"                                    | "passes through the same ground"                                     |
| 03-extortion     | 245  | "passes through Ashwick's hex" / "camped one hex south"          | "passes through Ashwick's territory" / "camped a day south"          |
| 05-campaign-life | 11   | "movement through the hex"                                       | "movement through the terrain"                                       |
| 05-campaign-life | 52   | "hold a hex as a temporary stronghold"                           | "hold the ground as a temporary stronghold"                          |
| 05-campaign-life | 443  | "the hex between settlements"                                    | "the ground between settlements"                                     |
| 05-campaign-life | 447  | "trees at a hex boundary"                                        | "trees at the boundary"                                              |
| 05-campaign-life | 449  | "entering a marked hex" (×2)                                     | "entering marked ground"                                             |
| 07-hired-casters | 224  | "call conditions in a hex"                                       | "call conditions over an area"                                       |
| 07-hired-casters | 284  | "marches into a hex empty-handed"                                | "marches into empty country"                                         |
| 07-hired-casters | 399  | "on the approach to the next hex"                                | "on the approach to the next day's march"                            |
| 07-hired-casters | 401  | "into the next hex blind"                                        | "into the next stretch of road blind"                                |
| 09-serving       | 124  | "a tree line one hex south"                                      | "a tree line to the south"                                           |
| 10-host-play     | 129  | "one hex apart or twenty hexes apart"                            | "one day apart or twenty days apart"                                 |
| 13-premade-bands | 200  | "a marsh hex east of Glethra"                                    | "the marshland east of Glethra"                                      |
| 13-premade-bands | 226  | "one hex west of their current position"                         | "a half-day west of their current position"                          |
| 13-premade-bands | 888  | "over hex territory" / "clear a specific hex" / "is in that hex" | "over territory" / "clear a stretch of ground" / "is on that ground" |
| 13-premade-bands | 1024 | "in a hex adjacent to" / "one hex south"                         | "in the country beside" / "a day's walk south"                       |
| 13-premade-bands | 1042 | "clear the hex"                                                  | "clear the ground"                                                   |
| 13-premade-bands | 1151 | "through a contested hex"                                        | "through contested ground"                                           |

**Retained unchanged** (rules text where "hex" is the mechanical map unit):

- 04-contracts line 52: "cleared a hex" — keep, this is rules text
- 04-contracts line 131: "Route or hex" — keep, contract definition
- 04-contracts line 133: "Multi-hex route" — keep, contract definition
- 04-contracts lines 450–491: Hoard mechanics — keep all, hex is the map coordinate
- 08-special-rules line 29: "one hex out" — keep, spread distance is mechanical
- 08-special-rules line 107: "target hex" — keep, War Room mechanic
- 11-appendix-a line 17: "claimed hex" — keep, Feud Track rule

### 4.2 FLAG — "Common Fighters" vs "Anonymous Fighters"

The chapter uses both "Common fighters" (a tier from Section 2) and "anonymous fighters" (a narrative term from the same section) to mean the same thing. The reader cannot tell whether these are different categories.

**Fix:** Standardize on "Common fighters" in all mechanical text. Use "the men" or "the rank and file" in prose. Remove "anonymous fighters" or define it once as a synonym:

> The stats above are for Common fighters — the anonymous rank and file who do not have individual names, triggers, or agendas. Throughout this chapter, "Common fighter" and "the men" refer to this tier.

### 4.3 FLAG — "Reputation" vs "Standing" Usage

"Reputation" (a JOURNEYS chapter stat tracking the fellowship's renown) and "Standing" (per-settlement opinion) are distinct mechanics but are sometimes used loosely in the mercenary chapter. Example: "The company's reputation preceded them" (narrative) vs "Reputation 3+ settlement" (mechanical) vs "Standing at that settlement" (mechanical).

**Fix:** No mechanical change. Add a definitions box at the start of Section 1 or Appendix A:

> **Reputation** is the fellowship's overall renown across the Ravenlands — a number from the JOURNEYS chapter. **Standing** is the fellowship's relationship with a specific settlement — tracked per settlement. This chapter uses both. When the text says "Reputation," it means the number. When it says "Standing," it means the settlement-specific score. When the text says "reputation" in lowercase, it means the word — what people say about the band.

### 4.4 FLAG — Inconsistent Grievance Capitalization

"Grievance" appears both capitalized (as a game term: GRIEVANCE from the JOURNEYS chapter) and lowercase (as a narrative word: "the underlying grievance"). This is fine in principle but creates confusion when the lowercase usage is adjacent to mechanical text.

**Fix:** Capitalize GRIEVANCE when the JOURNEYS mechanic is invoked. Use lowercase only in purely narrative sentences where no roll, difficulty, or Standing consequence is attached.

---

## Part 5 — Missing Rules to Add

### 5.1 Recommended Named Man Count per Band Size

See Fix 1.3.4 above.

### 5.2 Caster Loyalty Mechanics

Section 7 (Hired Casters) never states whether casters use Named Men–style Loyalty mechanics or a separate system. Casters have Triggers and Agendas, which implies Loyalty tracking, but no Loyalty score is assigned in the caster tier tables.

**Fix:** Add to Section 7 after the Caster Triggers table:

> Hired casters do not use the Named Men Loyalty scale. Their commitment is governed by their contract terms (coin or agenda). A caster on coin terms stays as long as paid. A caster on agenda terms stays as long as the agenda is progressing. If the agenda stalls for a full season with no visible effort from the captain, the caster leaves — no roll, no warning. A caster whose Trigger is hit responds according to their personality: an Initiate protests; an Adept withdraws magical services for 1D6 days; a Master leaves, often taking something.

### 5.3 Hoard Search Clarification

"Consecutive successful SCOUTING rolls equal to the hoard level" (Section 4) is ambiguous — does "consecutive" mean rolls must succeed without a failure in between, or does it mean one roll per Quarter Day in sequence?

**Fix:** Replace the current wording:

> **Without a marker:** The seeker rolls SCOUTING once per Quarter Day at the hoard's finder difficulty. They must accumulate successful rolls equal to the hoard level. Failures do not reset the count — they cost the Quarter Day and nothing else. A hoard at level 3 requires three successful rolls, which may take three or more Quarter Days.

### 5.4 Bounty Cold-Clock Reset

If a bounty is posted, goes cold after one year (drops 1 tier per season uncollected), but is then re-posted by the same or a different party — does the cold clock restart?

**Fix:** Add to Section 8 (Wanted Men), Clearing Wanted Status:

> **Re-posting:** A bounty that has gone cold may be re-posted by anyone willing to pay. The cold clock resets to full spread. A bounty that goes cold and is re-posted within the same year starts at the lower tier it had reached, not the original posting tier. A bounty re-posted after a full year of cold starts fresh.

### 5.5 Captain Succession on Death (Non-Mutiny)

Section 9 (Serving in Another's Company) covers mutiny succession but no section covers what happens when a captain simply dies in combat.

**Fix:** Add to Section 1 (Introduction) or Section 5 (Campaign Life):

> ### Captain's Death
>
> When the captain dies, the sergeant takes command immediately — no vote, no ceremony. If there is no sergeant, the most senior Named Man (highest Loyalty, longest service) assumes command by default. If no Named Man steps forward, the band dissolves at the end of the current contract.
>
> A band that loses its captain checks MORALE immediately regardless of current level. The new leader's first MORALE check is at +1 difficulty. After one completed contract under the new leader without a breach or MORALE failure, the difficulty modifier lapses.

---

## Part 6 — Open Questions (Not Resolved Here)

These items surfaced during analysis but require design decisions beyond the scope of an audit. They are recorded for future discussion.

1. **Can a caster be appointed Sergeant?** The chapter doesn't address this. A caster with high EMP and Loyalty 3 could theoretically fill the role, but the chapter's implicit assumption is that Sergeants are fighters.

2. **Can Named Men have multiple Triggers?** One Trigger is rolled per Named Man. Can a GM assign a second Trigger to a Named Man with a complex history? If so, does each Trigger fire independently?

3. **Does Warmaster pay himself from Host Treasury?** No wage line exists for the Warmaster. If the Warmaster is a PC, this needs a rule.

4. **Can Host Treasury favor one band?** The Warmaster's authority over treasury allocation is described but not limited. Can a Warmaster pre-allocate a bonus to one band at the expense of another? If so, what is the Ledger cost?

5. **Guard hireling → Named Man promotion.** Can a GUARD from the stronghold chapter be promoted to Named Man status? Or are they permanently Common-tier?

6. **Multiple Call Names.** Section 9 implies one Call Name per character. Can a character with a long career earn a second? If so, which do settlements recognize?

---

## Summary of Verdicts

| CATEGORY              | PASS   | FLAG   | ISSUE         |
| --------------------- | ------ | ------ | ------------- |
| Design — Rule Loops   | 8      | 1      | 0             |
| Design — Integration  | 0      | 3      | 1             |
| Synergy — Five Tests  | 7      | 3      | 0             |
| Balance — Four Lenses | 6      | 3      | 2             |
| Wording / Consistency | 0      | 3      | 1             |
| Missing Rules         | —      | —      | 5 (additions) |
| **TOTAL**             | **21** | **13** | **9**         |

All ISSUEs have proposed fixes above. All FLAGs have either proposed fixes or GM-guidance additions. The chapter's core design is sound — the MORALE/Loyalty/Grievance/Contract/Host systems form interlocking loops that generate play. The fixes are sharpening, not restructuring.
