<!-- markdownlint-disable MD013 -->

# Progression and XP — Advancement Models

> **STATUS: FILLED (Pass-1 + Pass-2).** Read alongside `01-character-model.md` (the model being advanced) and `06-travel-and-downtime.md` (the time blocks advancement consumes).

## Contents

1. Source provenance
2. Abstraction target
3. XP award models
4. Training costs — teacher vs self-taught
5. Talent rank ladders (5-rank FL vs 2-rank West)
6. Milestones and session-based XP
7. Downtime training
8. Legacy / long-term XP
9. The metacurrency→XP conversion (FL only)
10. Divergence rows (FL vs West)
11. Dials and instantiation recipe
12. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/02-your-adventurer.md:600-688` — XP (Tale pace vs Campaign pace), session awards, milestones, downtime, Legacy XP, training & advancement (raising attributes/skills/talents with cost tables, teacher vs without, the Slow-Study variant).
- `01-corebook/02-your-adventurer.md:404-408` — WP maximum formula and the **WP→XP conversion** rule (surrender 10 WP → 1 XP).
- `01-corebook/04-talents.md` — kin/profession/general talent ranks (1–5).
- `01-corebook/12-mercenaries-of-forbidden-lands.md` — **Named Men** (NPC advancement parallel).

**Tales of the Old West 2E (West):**
- `01-corebook/02-your-player-character.md:127-211` — XP (default pace), milestones, downtime, Legacy XP, Settlement Points, spending XP, training & advancement (raising attributes/abilities/talents with cost tables, teacher vs without).
- `01-corebook/04-talents.md` — two-rank (Basic/Advanced) talent system with access gating (self-taught vs needs teacher/workshop/institution).

## Abstraction target

Abstract **advancement** as a genre-neutral system with three knobs: how XP is *earned* (session vs milestone vs downtime), how it is *spent* (attribute/skill/talent costs, with a teacher discount), and the *depth* of the talent ladder (deep 5-rank trees vs flat 2-rank gates). The two games sit at opposite ends of the ladder-depth dial — FL's 5-rank kin/profession/general trees vs West's 2-rank Basic/Advanced. Both also share a remarkably similar XP-source mix and an almost identical cost-curve shape (the per-rank XP cost rises by +3 per rank with a teacher, doubled or tripled without), suggesting this is the engine's converged default. The West innovation worth generalizing is **narrative access gating** — some talents can't be learned without a forge, a society, or a teacher, not just XP and time.

## 3. XP award models

**Both games award XP from the same three sources, with near-identical shape:**

| Source | FL | West |
| --- | --- | --- |
| **Session (short)** | 2 XP (Tale) / 1 XP (Campaign) | 1 XP |
| **Session (long)** | 3 XP (Tale) / 2 XP (Campaign) | 2 XP |
| **Lethal-threat bonus** | +1 XP if a fight could have ended the chronicle | +1 XP if a fight/chase/disaster/reversal could have killed/ruined the PCs |
| **Minor milestone** | +2 XP | +2 XP |
| **Major milestone** | +4 XP | +4 XP |
| **Downtime** | ~1 XP per season | 1 XP per season |

FL `02-your-adventurer.md:607-631`; West `02-your-player-character.md:127-148`. The convergence is striking — the engine has settled on **1–3 XP/session + 2/4 for minor/major milestones + 1/season downtime** as its default advancement budget.

**FL adds a pace dial:** "Tale" pace (short vivid stories, faster XP) vs "Campaign" pace (multi-year sagas, slower XP). FL `02-your-adventurer.md:602-606`. West has a single default pace. **Layer:** the XP-source mix is General; the pace dial is Optional.

## 4. Training costs — teacher vs self-taught

**Both games use the same cost-curve shape:** raising a skill/ability one rank costs `3 × (new rank)` XP with a teacher, and more (×1.33 to ×3) without. Both also gate advancement behind a **time cost** (training quarters/shifts) that *also* scales with rank and is longer without a teacher.

**FL — skill ranks 0→5 (5-rank ladder):** With teacher, `3/6/9/12/15` XP for ranks 1–5; without, `4/8/12/16/20`. Time: 1–3 Quarters with teacher, 1–5 without. FL `02-your-adventurer.md:646-654`.

**West — ability ranks 0→5 (5-rank ladder, identical shape):** With teacher, `3/6/9/12/15` XP; without, `4/8/12/16/20`. Time: 1–3 Shifts with teacher, 1–5 without. West `02-your-player-character.md:189-197`. **The numbers are essentially identical** — strong evidence this is the engine's default skill curve.

**Talents diverge sharply (see §5).** Both also require a **WITS** (FL) / **DOCITY** (West) roll at the end of each training period when self-taught — failure means the time was spent but the rank didn't stick. A teacher with the *Teacher* talent removes the roll.

**Attributes:** `(new value × 10)` XP in both games. No teacher/roll required. FL caps attributes at 4 via training; West caps at 5. FL `02-your-adventurer.md:637-645`; West `02-your-player-character.md:179-188`.

**Generic abstraction:** the engine's default advancement curve is `(new rank × 3)` XP with teacher, ~×1.33 without, plus a scaling time cost and a self-taught WITS/learning-roll tax. **The teacher discount is the engine's "training matters" lever** — advancement is cheaper and surer in-fiction, which keeps the downtime loop relevant. **Layer:** General.

## 5. Talent rank ladders (5-rank FL vs 2-rank West)

**This is the central divergence in advancement design.**

**FL — deep 5-rank talent trees:** Every talent (kin, profession/"Path", general) has **5 ranks**, with rank-1 being the entry point. Cost: `rank × 3` XP with teacher, tripled without (and you cannot learn rank 1 without a teacher at all). Talents *must* have a mentor. Magic paths run 1–6. FL `02-your-adventurer.md:656-679`, `04-talents.md`.

**West — flat 2-rank (Basic + Advanced):** Every talent has exactly **two ranks: Basic then Advanced.** Basic ≈ a rank-2 talent in a granular game; Advanced ≈ rank-3. Cost: Basic 6 XP (teacher) / 18 XP (no teacher); Advanced 9 / 27. West `02-your-player-character.md:199-208`.

**The trade-off:**
- **FL (5-rank):** produces deep *build identity* — a Champion with rank-5 in a Path feels meaningfully different from a rank-2 Champion. Supports long campaigns and character specialization. Cost: more bookkeeping; the talent list is long; build choices are front-loaded.
- **West (2-rank):** produces *flat, accessible* advancement — talents are broad and potent, fewer of them, faster to grok. Supports shorter arcs and lower cognitive load. Cost: less build differentiation between two characters of the same archetype.

**West's narrative-access gating (generalizable):** Most West talents require *narrative access*, not just XP/time — a gunsmith needs a forge and a gunsmith to learn from; a polished society talent needs access to the circles that teach it; advanced doctoring/engineering shouldn't be learned alone in a shack. West `02-your-player-character.md:210`. Talents are grouped by function (Background, Combat, Frontier, Social, Trade/craft, Outlaw/law) to help the GM judge self-taught vs needs-mentor. **This is a transferable principle:** gate *what* can be learned by the fiction, not just *how fast*.

**Generic abstraction — "the ladder-depth dial":**
- **Flat (2-rank):** fast, accessible, broad talents. Best for short arcs, new players, genres where competence is binary-ish (you can or you can't).
- **Deep (5-rank):** builds identity, long campaigns, specialist characters. Best for long play, optimization-friendly tables.
- **Hybrid:** some talents flat (utility), some deep (signature builds). FL's magic paths (1–6) vs general talents (1–5) already show this internally.

**Layer:** General (talents advance); the ladder depth is a **core design dial**.

## 6. Milestones and session-based XP

(See §3.) Both use minor (+2) / major (+4) milestones with near-identical trigger language — minor = "exposing a traitor, saving a homestead, securing an alliance"; major = "finishing a tale, toppling a major foe, founding a town, changing the balance of power." FL `02-your-adventurer.md:627-631`; West `02-your-player-character.md:139-148`. The milestone trigger examples are genre-reskinned but structurally identical. **Layer:** General.

## 7. Downtime training

Advancement consumes the **time block** from `06-travel-and-downtime.md` — FL's Quarter Day, West's Shift. Training takes one Quarter/Shift per calendar day, only one lesson at a time, quarters need not be consecutive. FL `02-your-adventurer.md:633-635`; West `02-your-player-character.md:173-177`. This is what binds advancement to the travel/survival loop: you can't grind levels in a dungeon; you must *spend in-fiction time*, which the journey system taxes. **Layer:** General (ties to the downtime loop).

## 8. Legacy / long-term XP

**Identical rule in both games:** when a PC leaves play (dies/retires), count their sessions, take half (rounded up), add half their unspent XP (rounded down) → that's **Legacy XP** for the player's *next* character, spendable at creation. Both gate what Legacy can buy (FL: skill ≤3, talent ≤2; West: ability ≤3, talent ≤Basic). FL `02-your-adventurer.md:631`; West `02-your-player-character.md:145-147`.

**Generic abstraction:** Legacy XP is the engine's "death doesn't waste the player's investment" valve — a transferable rule that softens lethality without removing it. **Layer:** General (strongly recommended for any lethal game).

## 9. The metacurrency→XP conversion (FL only)

**FL-only:** at end of session, a character with ≥3 WP may siphon reserve for long-term growth — keep ≥2 WP, and every **10 WP surrendered across sessions = 1 XP.** FL `02-your-adventurer.md:404-408`. (Note: this is distinct from the optional *Surge of Willpower* rule, which converts XP→WP within a session; this is the reverse direction, WP→XP across sessions.)

**Generic abstraction:** an Optional valve linking the short-term metacurrency economy to the long-term advancement economy. Use it if WP/Faith pools tend to cap out and you want unspent reserve to mean something. West has no equivalent. **Layer:** Optional.

## 10. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Talent ladder depth** | 5-rank (kin/profession/general) | 2-rank (Basic/Advanced) | Build identity vs accessibility | 5-rank for long campaigns; 2-rank for short arcs / new players |
| **Talent cost curve** | `rank × 3` XP, ×3 without teacher, mentor required | `6`/`9` XP, ×3 without | Linear scaling vs two flat steps | Match to ladder depth |
| **Magic-path ladder** | 1–6 (taller than talents) | (no magic) | Power-class growth arc | Only if power layer is on (see `05`) |
| **Narrative access gating** | (implicit, via teacher requirement) | Explicit (forge/society/institution) | Implicit vs fiction-gated | Always make it explicit (West-style) |
| **XP pace dial** | Tale (fast) vs Campaign (slow) | Single default pace | Adjustable arc length vs simplicity | Add a pace dial for flexible groups |
| **Self-taught roll** | WITS roll per Quarter, failure = no progress | DOCITY roll per Shift, failure = no progress | (identical mechanic) | Keep — it's the engine's default |
| **Attribute training cap** | 4 (key attr up to 6 at creation) | 5 | Narrow ceiling vs wider | Match to desired power spread |
| **Metacurrency→XP** | Yes (10 WP → 1 XP, optional) | No | Links short-term pool to long-term growth | Optional; use if pools cap out |
| **NPC advancement parallel** | Named Men (mercenaries) | (none formalized) | NPCs grow alongside PCs | Add if you have long-term NPC allies (`07`) |

## 11. Dials and instantiation recipe

To set advancement for a new YZE game:

1. **Set the XP-source mix.** Default to the converged engine standard: 1–3 XP/session + lethal-threat +1, minor milestone +2, major +4, downtime 1/season. Adjust the session range up/down for faster/slower growth.
2. **Decide the pace dial.** Optional: offer two paces (short-arc-fast vs long-campaign-slow) like FL's Tale/Campaign.
3. **Set the skill cost curve.** Use the engine default `(new rank × 3)` XP with teacher, ~×1.33 without, + scaling time cost + self-taught WITS roll. Cap at rank 5.
4. **Set attribute cost + cap.** `(new value × 10)` XP, no teacher; cap at 4 or 5.
5. **Pick the talent ladder depth** — the central choice: flat 2-rank (West) / deep 5-rank (FL) / hybrid. This single decision sets the advancement feel.
6. **Write the talent cost curve** to match the ladder (flat = two steps; deep = rank×3).
7. **Make narrative access gating explicit.** Group talents by function and tag each as self-taught-OK vs needs-teacher/workshop/institution. This is free in-fiction texture.
8. **Add Legacy XP** (death/retirement → next PC) — strongly recommended for any lethal game.
9. **(Optional) Add metacurrency→XP conversion** if short-term pools cap out.
10. **(Optional) Add an NPC advancement parallel** if you have long-term NPC allies.
11. **Validate against the math** (`13-balance-and-synergy.md`): how many sessions to reach rank-5 in a signature talent? Does the milestone rate support the desired arc length? Does downtime XP make the season-calendar meaningful?

## 12. Design intent

Advancement in YZE is engineered to make **the character's arc visible** and to **gate power behind in-fiction time, not just XP:**

- **XP buys potential; time and sweat turn it into expertise.** Both books are emphatic on this (FL `02-your-adventurer.md:633`; West `02-your-player-character.md:171`). You cannot level up mid-dungeon — you must spend Quarters/Shifts in training, which the travel/survival loop taxes. This binds advancement to the downtime calendar.
- **The teacher discount makes the world matter.** Advancement is cheaper and surer when you have a mentor, a workshop, a society. This means *where you are and who you know* directly affects *how fast you grow* — geography and relationships become advancement resources.
- **The ladder-depth dial sets the advancement feel.** FL's 5-rank trees produce specialists with build identity over long campaigns; West's 2-rank gates produce broadly competent characters accessible to new players in short arcs. Neither is better; the choice is about campaign length and table taste.
- **Legacy XP makes death playable.** In a lethal engine (see `04`, `10`), death could waste a player's investment. Legacy XP transfers half the investment forward, so a character's death funds their successor — lethality without despair.
- **Milestones + downtime + sessions form a three-source budget** that produces steady but variable growth. The convergence of both books on near-identical numbers (1–3/session, +1 lethal, +2/+4 milestones, 1/season downtime) is the engine telling you its sweet spot: fast enough to feel growth, slow enough that rank-5 feels earned.
