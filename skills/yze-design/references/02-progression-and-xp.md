<!-- markdownlint-disable MD013 -->

# Progression and XP — Advancement Models

> **STATUS: FILLED (Pass-1 + Pass-2).** Read alongside `01-character-model.md` (the model being advanced) and `06-travel-and-downtime.md` (the time blocks advancement consumes).

## Contents

1. Source provenance
2. Abstraction target
3. XP award models
4. Training costs — teacher vs self-taught
5. Talents and Paths
6. Talent effect grammar and design validation
7. Milestones and session-based XP
8. Downtime training
9. Legacy / long-term XP
10. The Willpower/Faith→XP conversion (FL only)
11. Divergence rows (FL vs West)
12. Rule Choices and Build Recipe
13. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/02-your-adventurer.md:600-688` — XP (Tale pace vs Campaign pace), session awards, milestones, downtime, Legacy XP, training & advancement (raising attributes/skills/talents with cost tables, teacher vs without, the Slow-Study variant).
- `01-corebook/02-your-adventurer.md:404-408` — WP maximum formula and the **WP→XP conversion** rule (surrender 10 WP → 1 XP).
- `01-corebook/04-talents.md` — race/profession/general talent ranks (1–5).
- `01-corebook/12-mercenaries-of-forbidden-lands.md` — **Named Men** (NPC advancement parallel).

**Tales of the Old West 2E (West):**
- `01-corebook/02-your-player-character.md:127-211` — XP (default pace), milestones, downtime, Legacy XP, Settlement Points, spending XP, training & advancement (raising attributes/abilities/talents with cost tables, teacher vs without).
- `01-corebook/04-talents.md` — two-rank (Basic/Advanced) talent system with access gating (self-taught vs needs teacher/workshop/institution).

## Abstraction target

Abstract **advancement** as a genre-neutral system with three knobs: how XP is *earned* (session vs milestone vs downtime), how it is *spent* (attribute/skill/talent costs, with a teacher discount), and the *depth* of the talent ladder (deep 5-rank trees vs flat 2-rank gates). The two games sit at opposite ends of the ladder-depth choice — FL's 5-rank race/profession/general trees vs West's 2-rank Basic/Advanced. Both also share a remarkably similar XP-source mix and an almost identical cost-curve shape (the per-rank XP cost rises by +3 per rank with a teacher, doubled or tripled without), suggesting this is the engine's converged default. The West innovation worth generalizing is **narrative access gating** — some talents can't be learned without a forge, a society, or a teacher, not just XP and time.

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

**FL adds a pace choice:** "Tale" pace (short vivid stories, faster XP) vs "Campaign" pace (multi-year sagas, slower XP). FL `02-your-adventurer.md:602-606`. West has a single default pace. **Layer:** the XP-source mix is General; the pace choice is Optional.

## 4. Training costs — teacher vs self-taught

**Both games use the same cost-curve shape:** raising a skill/ability one rank costs `3 × (new rank)` XP with a teacher, and more (×1.33 to ×3) without. Both also gate advancement behind a **time cost** (training quarters/shifts) that *also* scales with rank and is longer without a teacher.

**FL — skill ranks 0→5 (5-rank ladder):** With teacher, `3/6/9/12/15` XP for ranks 1–5; without, `4/8/12/16/20`. Time: 1–3 Quarters with teacher, 1–5 without. FL `02-your-adventurer.md:646-654`.

**West — ability ranks 0→5 (5-rank ladder, identical shape):** With teacher, `3/6/9/12/15` XP; without, `4/8/12/16/20`. Time: 1–3 Shifts with teacher, 1–5 without. West `02-your-player-character.md:189-197`. **The numbers are essentially identical** — strong evidence this is the engine's default skill curve.

**Talents diverge sharply (see §5).** Both also require a **WITS** (FL) / **DOCITY** (West) roll at the end of each training period when self-taught — failure means the time was spent but the rank didn't stick. A teacher with the *Teacher* talent removes the roll.

**Attributes:** `(new value × 10)` XP in both games. No teacher/roll required. FL caps attributes at 4 via training; West caps at 5. FL `02-your-adventurer.md:637-645`; West `02-your-player-character.md:179-188`.

**Abstract pattern:** the engine's default advancement curve is `(new rank × 3)` XP with teacher, ~×1.33 without, plus a scaling time cost and a self-taught WITS/learning-roll tax. **The teacher discount is the engine's "training matters" lever** — advancement is cheaper and surer in-fiction, which keeps the downtime loop relevant. **Layer:** General.

## 5. Talents and Paths

**This is the central divergence in advancement design.**

**FL — deep 5-rank talent trees:** Every talent (race, profession/"Path", general) has **5 ranks**, with rank-1 being the entry point. Cost: `rank × 3` XP with teacher, tripled without (and you cannot learn rank 1 without a teacher at all). Talents *must* have a mentor. Magic paths run 1–6. FL `02-your-adventurer.md:656-679`, `04-talents.md`.

**West — flat 2-rank (Basic + Advanced):** Every talent has exactly **two ranks: Basic then Advanced.** Basic ≈ a rank-2 talent in a granular game; Advanced ≈ rank-3. Cost: Basic 6 XP (teacher) / 18 XP (no teacher); Advanced 9 / 27. West `02-your-player-character.md:199-208`.

**The trade-off:**
- **FL (5-rank):** produces deep *build identity* — a Champion with rank-5 in a Path feels meaningfully different from a rank-2 Champion. Supports long campaigns and character specialization. Cost: more bookkeeping; the talent list is long; build choices are front-loaded.
- **West (2-rank):** produces *flat, accessible* advancement — talents are broad and potent, fewer of them, faster to grok. Supports shorter arcs and lower cognitive load. Cost: less build differentiation between two characters of the same archetype.

**West's narrative-access gating (generalizable):** Most West talents require *narrative access*, not just XP/time — a gunsmith needs a forge and a gunsmith to learn from; a polished society talent needs access to the circles that teach it; advanced doctoring or invention shouldn't be learned alone in a shack. West `02-your-player-character.md:210`. Talents are grouped by function (Background, Combat, Frontier, Social, Trade/craft, Outlaw/law) to help the GM judge self-taught vs needs-mentor. **This is a transferable principle:** gate *what* can be learned by the fiction, not just *how fast*.

**Abstract pattern — "the ladder-depth choice":**
- **Flat (2-rank):** fast, accessible, broad talents. Best for short arcs, new players, genres where competence is binary-ish (you can or you can't).
- **Deep (5-rank):** builds identity, long campaigns, specialist characters. Best for long play, optimization-friendly tables.
- **Hybrid:** some talents flat (utility), some deep (signature builds). FL's magic paths (1–6) vs general talents (1–5) already show this internally.

**Layer:** General (talents advance); the ladder depth is a **core design choice**.

### 5.1 Talent families

Use these names in agnostic rules text. They are broad enough for any genre while still sounding like RPG rules.

| Family | What it means | Source shape | Use for | Do not use for |
| --- | --- | --- | --- | --- |
| Race talents | gifts, instincts, old blood, built-in knack | FL Race talents | what a people can do that others cannot easily copy | ordinary learned skills |
| Profession talents | trade secrets, combat schools, social callings | FL profession Paths; West archetype access | what a role is famous for doing | universal competence |
| Path talents | a deep road of mastery, usually 3-5 ranks | FL Path talents | long-campaign identity and signature builds | one-off perks |
| General talents | tricks anyone may learn with training | FL general talents; West broad talents | common adventuring excellence | setting-defining powers |
| Secrets | hidden teaching, outlaw craft, forbidden method | West narrative access gating | talents gated by teachers, societies, cults, labs, guilds | public techniques |
| Masteries | high-rank capstone expressions | FL rank 4-5 effects | rare late-campaign authority | early advancement |

### 5.2 Rank rhythm

Deep talent paths should feel like a character walking farther down a road, not buying five unrelated perks.

| Rank | What the rank should feel like | Typical effect | Safe ceiling |
| --- | --- | --- | --- |
| 1 | Initiate | permission, narrow +1, new option, minor spend | lets you enter the playstyle |
| 2 | Practiced | stronger reliability, extra stunt, limited protection | makes the playstyle dependable |
| 3 | Proven | action unlock, resource conversion, scene authority | signature moment once/scene or with cost |
| 4 | Master | action compression, broad protection, rare access | powerful but gated by risk, cost, or scope |
| 5 | Legendary | table-visible exception, command of a niche | never removes all cost or all risk |
| 6 | Mythic path only | world-bending power | belongs in powers, not ordinary talents |

**Design rule:** a path should usually alternate between *permission*, *reliability*, *new choice*, *risk control*, and *capstone*. Five ranks of flat dice bonuses are not a path; they are a spreadsheet.

### 5.3 Profession path sheet

Use this sheet when building a profession, class, calling, job, order, gang role, military specialty, school, or trade.

| Field | Required answer |
| --- | --- |
| Name | a flavorful calling, not a job-code |
| Key attribute | the attribute the calling leans on |
| Key skills | 3-5 skills it uses often |
| Starting gear | enough to perform the role at session one |
| Path talent | the deep road of mastery |
| General talent picks | 3-6 talents that fit the calling |
| Pride/Faith prompt | what the calling refuses to abandon |
| Dark Secret prompt | what can be used against the character |
| Relationship prompts | how this calling tends to bind or irritate allies |
| Teacher/access | who can teach higher ranks and where |

### 5.4 Talent menus by effect

| Menu | Low-rank forms | High-rank forms | Validation |
| --- | --- | --- | --- |
| Gifts | sense, endure, speak, recover, resist | ignore one narrow limit, act where others cannot | race talents should be distinctive, not universally stronger |
| Tricks | draw faster, climb better, read tracks, repair quickly | combine two steps, carry a bonus forward | action compression needs a cap |
| Secrets | craft advanced gear, treat rare wounds, know hidden law | unlock forbidden places, rites, black markets | require teacher, institution, or dangerous proof |
| Masteries | +1 in a narrow scene, extra stunt | spend Willpower/Faith for a decisive exception | never grant free permanent broad +2 |
| Bonds | ally gains help, mount stays calm, crew obeys | protect attached NPC/asset from collapse | attached thing must have upkeep or risk |
| Holdings | business, stronghold, gang, ship, town improves | period roll gains option or protection | do not create safe passive wealth |
| Powers | cast, resist, shape, ward, overcharge safely | epic or world-changing access | belongs under `05`; check mishap and fuel |

### 5.5 Talent access table

| Access | Fictional requirement | Good for | Failure if ignored |
| --- | --- | --- | --- |
| Self-taught | practice alone with ordinary tools | simple tricks, survival, common craft | wasted time on failed learning roll |
| Teacher | mentor, veteran, elder, master, coach | most rank increases | higher cost, impossible rank 1 in deep systems |
| Place | forge, school, temple, arena, lab, hospital, shipyard | craft, science, powers, status talents | cannot learn until travel/downtime finds it |
| Society | guild, gang, court, church, regiment, cult | social, outlaw, legal, command secrets | social obligation or initiation price |
| Trial | survive a duel, hunt, siege, exam, pilgrimage | masteries and capstones | injury, debt, enemy, public failure |
| Relic | book, device, drug, spirit, alien tutor | powers, weird science, old lore | corruption, misfire, obsession, theft |

### 5.6 Talents and Paths validation

- A Race talent may be exclusive, but not broadly better than all other races.
- A profession path must change table behavior by rank 2.
- A general talent should either sharpen a common action or unlock a narrow trick; if it defines a whole role, make it a path.
- A Secret must name who teaches it and what they demand.
- A Mastery must still leave the player choosing between cost, risk, time, exposure, or limited scope.
- Any talent that creates resources must have a cap and a danger trigger.
- Any talent that compresses actions must be checked against `03-conflict-and-combat.md`.
- Any talent that protects from harm, mishaps, Trouble, Menace, or critical injuries must be narrow, costly, or late.

## 6. Talent effect grammar and design validation

The corebooks do not treat talents as loose perks. They are the engine's main way to **license exceptions** to normal play: who can attempt advanced work, who can compress an action, who can carry a social identity, who can turn risk into advantage, and who can make an NPC, mount, business, or spell behave differently. A YZE designer should write talents from effect families, not from cool names.

| Talent family | FL expressions | West expressions | Generic use |
| --- | --- | --- | --- |
| Identity / origin | race talents, profession Paths | Background talents | says "what kind of person you are" |
| Skill amplifier | rank adds dice, rerolls, extra effect | Basic/Advanced ability support | makes a familiar roll better |
| Permission gate | magic paths, crafting talents, taming/training | gunsmithing, doctoring, business, society access | lets you attempt advanced work at all |
| Action unlock | combat maneuvers, mounted tricks, profession actions | dueling, shooting, riding, gambling, outlaw/law talents | adds a new action or scene option |
| Action compression | do a slow thing faster, combine steps | fast draw, reload/fire support, business shortcuts | buys tempo, which is usually more valuable than dice |
| Resource conversion | WP spend, gear/resource improvements | Faith/Trouble interaction, cash/business effects | turns one economy into another |
| Risk protection | ignore penalty, reduce mishap, resist fear/poison | buy off Trouble, resist social/legal fallout | changes consequence probability |
| Companion / roster | animal handling, taming, hireling support | Compadre/Pardner, horse talents, gang loyalty | improves an attached NPC or mount |
| Asset / enterprise | stronghold/crafting support | business, property, congregation, outlaw band | links character growth to owned things |
| Social/status | reputation, manipulation, court/authority | Fame, standing, society, preacher/lawman | changes access and reaction, not just rolls |
| Power layer | magic Paths, spell ranks | none in grounded West | unlocks exceptional rule sets |

### 6.1 Effect Shapes

Use these shapes when creating new talents.

| Shape | Rule form | Safe ceiling | Validation check |
| --- | --- | --- | --- |
| Narrow +1 | `+1 die to X in situation Y` | safe if X is specific | does it stack with gear/help? |
| Broad +1 | `+1 die to X generally` | expensive, late, or identity-defining | does it erase skill investment? |
| Reroll / ignore penalty | reroll one failed die, ignore darkness/range/etc. | once per scene/roll or narrow trigger | does it remove the genre's pressure? |
| Extra stunt | spend surplus success for a new menu item | safe when menu-bound | does it require a success first? |
| New action | adds a new move to a scene | safe if action still costs time | does it bypass another rule set? |
| Action compression | slow→fast, two steps→one | dangerous; price heavily | check `03` action budget thresholds |
| Resource discount | cost 1 less WP/Faith/cash/material | safe with floor of 1 or per-session cap | can it make a loop free? |
| Resource generation | gain WP/Faith/cash/material on trigger | dangerous; cap and require risk | can players farm it without danger? |
| Consequence shield | reduce crit, Trouble, mishap, legal fallout | narrow or costly | does it make catastrophe impossible? |
| NPC/asset upgrade | companion, mount, hireling, business, gang improves | safe if attached thing has upkeep/risk | can it be sold or stacked into passive profit? |

### 6.2 Talent Writing Procedure

1. **Name the fiction first.** A talent is an identity, trade, discipline, or exceptional method, not a floating bonus.
2. **Choose one family** from the table above. Hybrid talents are allowed only when one half is clearly subordinate.
3. **Choose one primary effect shape.** If it grants both dice and tempo, raise cost, rank, prerequisites, or risk.
4. **Attach a gate.** Teacher, institution, tool, social circle, battlefield experience, wilderness season, business, mount, spell path, or faction.
5. **State cadence.** Always-on, once per roll, once per scene, once per session, once per period, or when spending Willpower/Faith.
6. **State stacking.** Say whether it stacks with help, gear, quality, property, town aspects, spells, or other talents.
7. **State failure interaction.** Does it change pushed rolls, Trouble, mishaps, critical injuries, or aftermath?
8. **Validate against adjacent systems.** Action compression goes to `03`; harm protection to `04`; power talents to `05`; enterprise talents to `08`/`25`; roster talents to `07`.

### 6.3 Signature Talent Test

A talent is worth writing only if at least one is true:

- it changes what the character can attempt;
- it changes which risk the player chooses to accept;
- it makes a neglected rule set attractive;
- it anchors a profession, Race, archetype, order, gang, school, or trade;
- it creates a recurring table behavior other players notice.

If the talent merely renames `+1 die sometimes`, fold it into gear, help, a scene modifier, or a broader talent.

## 7. Milestones and session-based XP

(See §3.) Both use minor (+2) / major (+4) milestones with near-identical trigger language — minor = "exposing a traitor, saving a homestead, securing an alliance"; major = "finishing a tale, toppling a major foe, founding a town, changing the balance of power." FL `02-your-adventurer.md:627-631`; West `02-your-player-character.md:139-148`. The milestone trigger examples are genre-reskinned but structurally identical. **Layer:** General.

## 8. Downtime training

Advancement consumes the **time block** from `06-travel-and-downtime.md` — FL's Quarter Day, West's Shift. Training takes one Quarter/Shift per calendar day, only one lesson at a time, quarters need not be consecutive. FL `02-your-adventurer.md:633-635`; West `02-your-player-character.md:173-177`. This is what binds advancement to the travel/survival loop: you can't grind levels in a dungeon; you must *spend in-fiction time*, which the journey system taxes. **Layer:** General (ties to the downtime loop).

## 9. Legacy / long-term XP

**Identical rule in both games:** when a PC leaves play (dies/retires), count their sessions, take half (rounded up), add half their unspent XP (rounded down) → that's **Legacy XP** for the player's *next* character, spendable at creation. Both gate what Legacy can buy (FL: skill ≤3, talent ≤2; West: ability ≤3, talent ≤Basic). FL `02-your-adventurer.md:631`; West `02-your-player-character.md:145-147`.

**Abstract pattern:** Legacy XP is the engine's "death doesn't waste the player's investment" valve — a transferable rule that softens lethality without removing it. **Layer:** General (strongly recommended for any lethal game).

## 10. The Willpower/Faith→XP conversion (FL only)

**FL-only:** at end of session, a character with ≥3 WP may siphon reserve for long-term growth — keep ≥2 WP, and every **10 WP surrendered across sessions = 1 XP.** FL `02-your-adventurer.md:404-408`. (Note: this is distinct from the optional *Surge of Willpower* rule, which converts XP→WP within a session; this is the reverse direction, WP→XP across sessions.)

**Abstract pattern:** an Optional valve linking the short-term Willpower/Faith economy to the long-term advancement economy. Use it if WP/Faith pools tend to cap out and you want unspent reserve to mean something. West has no equivalent. **Layer:** Optional.

## 11. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Talent ladder depth** | 5-rank (Race/profession/general) | 2-rank (Basic/Advanced) | Build identity vs accessibility | 5-rank for long campaigns; 2-rank for short arcs / new players |
| **Talent cost curve** | `rank × 3` XP, ×3 without teacher, mentor required | `6`/`9` XP, ×3 without | Linear scaling vs two flat steps | Match to ladder depth |
| **Magic-path ladder** | 1–6 (taller than talents) | (no magic) | Power-class growth arc | Only if power layer is on (see `05`) |
| **Narrative access gating** | (implicit, via teacher requirement) | Explicit (forge/society/institution) | Implicit vs fiction-gated | Always make it explicit (West-style) |
| **XP pace choice** | Tale (fast) vs Campaign (slow) | Single default pace | Adjustable arc length vs simplicity | Add a pace choice for flexible groups |
| **Self-taught roll** | WITS roll per Quarter, failure = no progress | DOCITY roll per Shift, failure = no progress | (identical rule) | Keep — it's the engine's default |
| **Attribute training cap** | 4 (key attr up to 6 at creation) | 5 | Narrow ceiling vs wider | Match to desired power spread |
| **Willpower/Faith→XP** | Yes (10 WP → 1 XP, optional) | No | Links short-term pool to long-term growth | Optional; use if pools cap out |
| **NPC advancement parallel** | Named Men (mercenaries) | (none formalized) | NPCs grow alongside PCs | Add if you have long-term NPC allies (`07`) |

## 12. Rule Choices and Build Recipe

To set advancement for a new YZE game:

1. **Set the XP-source mix.** Default to the converged engine standard: 1–3 XP/session + lethal-threat +1, minor milestone +2, major +4, downtime 1/season. Adjust the session range up/down for faster/slower growth.
2. **Decide the pace choice.** Optional: offer two paces (short-arc-fast vs long-campaign-slow) like FL's Tale/Campaign.
3. **Set the skill cost curve.** Use the engine default `(new rank × 3)` XP with teacher, ~×1.33 without, + scaling time cost + self-taught WITS roll. Cap at rank 5.
4. **Set attribute cost + cap.** `(new value × 10)` XP, no teacher; cap at 4 or 5.
5. **Pick the talent ladder depth** — the central choice: flat 2-rank (West) / deep 5-rank (FL) / hybrid. This single decision sets the advancement feel.
6. **Write the talent effect grammar** from §6 before writing individual talents.
7. **Write the talent cost curve** to match the ladder (flat = two steps; deep = rank×3).
8. **Make narrative access gating explicit.** Group talents by function and tag each as self-taught-OK vs needs-teacher/workshop/institution. This is free in-fiction texture.
9. **Add Legacy XP** (death/retirement → next PC) — strongly recommended for any lethal game.
10. **(Optional) Add Willpower/Faith→XP conversion** if short-term pools cap out.
11. **(Optional) Add an NPC advancement parallel** if you have long-term NPC allies.
12. **Validate against the math** (`13-balance-and-synergy.md`): how many sessions to reach rank-5 in a signature talent? Does the milestone rate support the desired arc length? Does downtime XP make the season-calendar meaningful?

## 13. Design intent

Advancement in YZE is engineered to make **the character's arc visible** and to **gate power behind in-fiction time, not just XP:**

- **XP buys potential; time and sweat turn it into expertise.** Both books are emphatic on this (FL `02-your-adventurer.md:633`; West `02-your-player-character.md:171`). You cannot level up mid-dungeon — you must spend Quarters/Shifts in training, which the travel/survival loop taxes. This binds advancement to the downtime calendar.
- **The teacher discount makes the world matter.** Advancement is cheaper and surer when you have a mentor, a workshop, a society. This means *where you are and who you know* directly affects *how fast you grow* — geography and relationships become advancement resources.
- **The ladder-depth choice sets the advancement feel.** FL's 5-rank trees produce specialists with build identity over long campaigns; West's 2-rank gates produce broadly competent characters accessible to new players in short arcs. Neither is better; the choice is about campaign length and table taste.
- **Legacy XP makes death playable.** In a lethal engine (see `04`, `10`), death could waste a player's investment. Legacy XP transfers half the investment forward, so a character's death funds their successor — lethality without despair.
- **Milestones + downtime + sessions form a three-source budget** that produces steady but variable growth. The convergence of both books on near-identical numbers (1–3/session, +1 lethal, +2/+4 milestones, 1/season downtime) is the engine telling you its sweet spot: fast enough to feel growth, slow enough that rank-5 feels earned.
