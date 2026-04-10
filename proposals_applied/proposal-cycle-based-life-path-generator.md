<!-- markdownlint-disable MD013 -->

# Proposal: Cycle-Based Life Path Generator

## Purpose

The current life generator in Chapter 2 is quick and vivid.
It is not deep enough.

One childhood roll, one profession roll, and one to three formative-event rolls can leave a sharp impression, but not much weight.
The character arrives marked, yet not fully worn in.
You can often see what sort of adventurer stands before you.
You cannot always see what ground them down into that shape.

This replacement keeps the quick generator's harsh tone and strong identity, but gives the character a longer road before play begins.
Life is resolved in cycles.
Each cycle breaks into four turns.
Each turn can bring duty, weather, luck, fear, injury, silver, disgrace, or one more hard-earned skill.

## Why Replace The Current Generator

The current generator is fast.
It is not built for accumulation.

Its limits are plain:

- identity is front-loaded into a handful of rolls
- age matters numerically, but not procedurally
- there is little room for reversals, false starts, disgrace, or second careers
- a Fighter, Rogue, or Sorcerer often arrives with one sharp memory instead of a chain of hard years
- the party-bond table is strong, but it comes after a character history that is still fairly thin

The replacement keeps what already works:

- harsh and practical tone
- quick legibility at the table
- strong kin and profession identity
- support for random generation without full chaos

It adds what the chapter still lacks:

- time
- turns of fortune
- scars and contacts
- one failed turn that still leaves a mark
- a reason an old adventurer is old besides a lower attribute budget

## Design Targets

This subsystem must do six jobs.

1. Produce a character who feels lived-in before play begins.
2. Preserve Chapter 2 balance baselines for age, skills, and talents.
3. Create strong fiction without requiring the GM to write a novella for every player.
4. Support both full-random and guided play.
5. Stay compatible with existing kin talents, profession talents, and Willpower rules.
6. Avoid dominant lines, free-resource loops, or character-creation exploits.

## Design Position

This does **not** replace the chapter's normal free-build method.
It replaces only the simple life generator.

The standard quick method should remain the clean default.
This becomes the heavier option for groups who want more history, more burdens, and more hooks before the first session.

## Core Shape

The new subsystem has five layers:

1. `Kin and home`
2. `Childhood foundation`
3. `Life cycles`
4. `Mustering out`
5. `How did you meet?`

The change comes at layer 3.
Instead of one profession table and one to three formative-event tables, the character passes through several cycles.

Each cycle has:

- a chosen or rolled life path
- four dramatic turns
- one test each turn
- one event each turn
- one skill gain each turn
- one end-of-cycle advancement or departure result

## Cycle Length By Kin

The system uses the same structure for every kin, but one cycle represents a different number of calendar years depending on who lived it.

| Kin | Years Per Cycle |
|---|---:|
| Human | 4 |
| Half-Elf | 12 |
| Dwarf | 10 |
| Halfling | 4 |
| Wolfkin | 3 |
| Orc | 3 |
| Goblin | 4 |
| Elf | 25 |

This keeps the procedure playable while staying honest to the setting.
An elf may carry centuries and still reach the table through the same number of meaningful turns as a human who lived fast and hard.

## Age Bands

The chapter's age bands remain the balance anchor.
The new subsystem reaches them through completed cycles rather than free skill-point assignment.

| Age Band | Completed Cycles | Total Skill Points From Life | Attribute Budget | General Talents |
|---|---:|---:|---:|---:|
| Young | 2 | 8 | 15 | 1 |
| Adult | 3 | 12 | 14 | 3 |
| Old | 4 | 16 | 13 | 5 |

Elf exception:

- elves cannot begin as Young
- elf characters begin at Adult or Old, just as the chapter already assumes

This keeps the backbone of Chapter 2 intact:

- attributes still come from age
- general talents still come from age
- the life path now determines skill distribution, gear history, contacts, rivals, scars, and profession flavor

## Locked Spine

These decisions hold the whole structure together.
Treat them as fixed unless a later balance pass proves one of them wrong.

### Decision 1: Childhood Comes Before Age

The order is:

1. choose kin
2. choose or roll home
3. choose or roll childhood foundation
4. choose age
5. resolve the number of cycles granted by that age

Use this order for two reasons.

- Childhood is who you were before hard adult years began to shape you.
- Age should determine how much life happened after that start, not what sort of child you were.

### Decision 2: Final Profession Uses A Short Qualification Rule

The final profession does **not** come from the last path alone.
That would place too much weight on the final cycle and punish characters whose lives ended in drift, exile, or collapse.

Use this qualification procedure instead:

1. If your last cycle used a profession path, that path is your default profession.
2. If your last cycle used a fallback path, choose between the profession paths from your two previous cycles.
3. If you have only one completed profession path across the whole history, you must use that profession.
4. If no profession path was ever completed, choose the profession tied to the skill family in which you hold the most ranks.

This keeps the end of a life meaningful without letting one failed last cycle erase the whole character.

### Decision 3: Staying In One Path Is Allowed, But Taxed

A character may remain in the same path across multiple cycles.
That should remain possible.
A mercenary might stay a mercenary.
A rider might never leave the saddle.
A sorcerer might spend half a life in the same tower.

But repetition must narrow the life.

After the first completed cycle in the same path:

- the turn test in the next same-path cycle is made at `-1`
- on a failed turn test, the mishap roll is made with `+1`
- the advancement table for that repeated cycle cannot grant the same direct talent benefit twice

This gives the system the right shape:

- repeating a path is still attractive if the fiction supports it
- repeating it forever is no longer the obvious optimal line
- the system encourages second careers, exile, reinvention, and drift without forcing them every time

### Decision 4: Childhood Foundation Covers The First Two Turns Of The First Cycle

The age skill totals stay unchanged:

- Young `8`
- Adult `12`
- Old `16`

Those totals are composed like this:

| Age Band | Childhood Foundation | Remaining Resolved Turns | Total |
|---|---:|---:|---:|
| Young | 2 | 6 | 8 |
| Adult | 2 | 10 | 12 |
| Old | 2 | 14 | 16 |

This keeps the math from drifting.
Childhood does not sit outside the cycle structure.
It stands in for the first two turns of the first cycle.
That is why the age totals still land where Chapter 2 needs them to land.

Use this rule:

- childhood foundation grants the first 2 skill points of the first cycle
- each resolved turn after that grants 1 skill point
- the total always lands on the chapter's age baseline

### Decision 5: Use Three Player Modes

The subsystem supports three modes of use.

| Mode | Path Choice | Turn Event Choice | Intended Use |
|---|---|---|---|
| Full Random | Roll every path unless a rule forces one | Roll every event | maximum surprise, fastest for players who trust the dice |
| Guided Random | Choose the path | Roll the turn events | choose your broad life, discover the details |
| Full Guided | Choose the path | Pick from one of two rolled turn events | best for players who want authorship without free-build softness |

Full Guided should never mean unrestricted pick-from-the-whole-table.
The system still needs friction.
Use this rule:

- roll two results
- choose one

That keeps the life generator a life generator.

## System Summary

Use the subsystem like this.

1. Choose kin and home region.
2. Roll or choose a childhood foundation. This gives your first 2 skill points, one hook, and a suggested first path.
3. Choose Young, Adult, or Old. That determines how many completed cycles you resolve, as well as your attribute budget and general talents.
4. For each completed cycle, choose or roll a life path.
5. In the first cycle, childhood has already covered the first two turns. Resolve the remaining turns of that cycle, then resolve every later cycle in full. Each resolved turn grants 1 skill point and produces an event or mishap.
6. At cycle end, roll advancement or departure. You may stay in the same path, change path, or be forced out.
7. Repeating the same path imposes a narrowing tax: harder turn tests, harsher mishaps, and no duplicate direct talent reward.
8. After the last cycle, qualify for a profession using the short qualification rule.
9. Muster out from your final path to gain practical gear, silver, contacts, rivals, scars, and rumors.
10. Spend attributes using the chapter's age budget, choose kin talent, choose profession talent, choose general talents, then roll or choose `How Did You Meet?`

This keeps Chapter 2's math while replacing the flat story with reversals, hard turns, and hard-earned shape.

## Replacement Procedure

### 1. Choose Kin And Home

Use the existing kin and home-region material.
Keep it as the opening frame.

### 2. Roll Childhood Foundation

Childhood no longer determines most of the build.
It becomes a foundation.

A childhood result gives:

- one favored attribute pair
- the first 2 skill points of the age total
- one contact, scar, or burden
- one suggested first life path

That is enough to point the character in a direction without finishing the whole job too early.

### 3. Choose Age

Choose Young, Adult, or Old as normal.
That determines:

- completed cycles
- attribute budget
- general talent total

### 4. Resolve Life Cycles

For each completed cycle:

1. Choose or roll a life path using Full Random, Guided Random, or Full Guided mode.
2. If this is your first cycle, your childhood foundation already counts as the First Turn and Second Turn. Begin with the Third Turn.
3. If this is any later cycle, resolve all four turns in order.
4. Roll advancement or departure.
5. Either remain in the same path, change path, or be forced into another one by mishap.

If you remain in the same path after already completing one cycle there, the next same-path cycle is narrowed:

- turn tests in that cycle are made at `-1`
- failed turn tests roll mishaps with `+1`
- the same direct talent benefit cannot be gained again from that path's advancement table

### 5. Muster Out

After the final cycle, roll on the final path's mustering-out table.
This gives:

- silver
- gear
- a contact
- a rival
- a rumor
- a wound that still matters

### 6. Finish Character Creation

After all cycles:

- spend attributes from the chapter's age budget
- choose kin talent
- qualify for profession using the short qualification rule, then choose profession talent
- choose general talents by age
- use the skill points earned during the resolved turns instead of freely assigning them
- roll or choose `How Did You Meet?`

## Childhood Foundations

The old childhood tables are still useful.
They simply do too much.

In the current generator, childhood does all of this at once:

- it leans heavily toward a final stat shape
- it assigns a broad skill spread up front
- it often feels like a first profession rather than a beginning

Here, childhood is only a foundation.
It points the character somewhere.
It does not finish the march.

### Foundation Table Format

Every childhood foundation table uses the same columns.

| Column | Job |
|---|---|
| Foundation | The life you came out of |
| Favored Attributes | The two attributes childhood leaned on most |
| First 2 Skill Points | The first two skill points of the age total |
| Hook | Contact, burden, scar, rumor, or local tie left from childhood |
| Suggested First Path | A natural first adult life, not a binding one |

### Alderlander Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Orphaned | Agility, Empathy | `Scouting 1`, `Sleight of Hand 1` | You know one village, shrine, or ferryman who once took pity on you. | Rogue |
| 2 | Herder | Strength, Empathy | `Animal Handling 1`, `Survival 1` | One old herd-route or pasture still feels like yours. | Rider |
| 3 | Vagabond | Agility, Wits | `Survival 1`, `Scouting 1` | You carry one rumor about a ruined stead, bridge, or hidden shelter. | Drifter |
| 4 | Squire | Strength, Empathy | `Melee 1`, `Healing 1` | One former master, quartermaster, or stablehand still remembers your service. | Fighter |
| 5 | Laborer | Strength, Wits | `Might 1`, `Crafting 1` | You owe labor, coin, or gratitude to one farming family. | Laborer |
| 6 | Hard Studies | Wits, Empathy | `Lore 1`, `Insight 1` | You possess one scrap of writing, copied prayer, or family secret. | Peddler |

### Aslene Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Born in the Saddle | Agility, Empathy | `Move 1`, `Animal Handling 1` | One beast still knows your scent, or one clan elder does. | Rider |
| 2 | Dreamer | Wits, Empathy | `Lore 1`, `Performance 1` | You know one half-remembered legend others dismiss too quickly. | Minstrel |
| 3 | Strongest of the Clan | Strength, Empathy | `Might 1`, `Melee 1` | One childhood rival still measures themself against you. | Fighter |
| 4 | Taught by a Wise Woman | Wits, Empathy | `Healing 1`, `Insight 1` | You carry one charm, herb-lore habit, or whispered taboo. | Druid |
| 5 | Hunter | Agility, Wits | `Marksmanship 1`, `Scouting 1` | One kill, trail, or beast-sign from childhood still haunts your sleep. | Hunter |
| 6 | Child of the Winds | Agility, Wits | `Survival 1`, `Endurance 1` | You have slept in holy or cursed places and learned one omen there. | Drifter |

### Ailander Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Child of the Raven | Wits, Empathy | `Lore 1`, `Scouting 1` | One old shrine, raven sign, or wandering sister still matters to you. | Druid |
| 2 | Druid's Apprentice | Wits, Agility | `Lore 1`, `Healing 1` | You remember a rite, warning, or path your teacher never finished explaining. | Druid |
| 3 | Guardian | Strength, Agility | `Melee 1`, `Marksmanship 1` | One kin elder trusts you to stand when others run. | Fighter |
| 4 | Wanderer | Agility, Empathy | `Survival 1`, `Animal Handling 1` | You know one safe sleeping place from the bad years of the Mist. | Drifter |
| 5 | Laborer | Strength, Empathy | `Might 1`, `Crafting 1` | You left kin behind who still expect your hands at harvest or lambing. | Laborer |
| 6 | Herder | Strength, Empathy | `Animal Handling 1`, `Scouting 1` | One flock-road, cattle ford, or grazing debt binds you to a place. | Rider |

### Half-Elf Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | On the Run | Agility, Wits | `Stealth 1`, `Scouting 1` | Someone once hunted you or your family and may still want the work finished. | Rogue |
| 2 | Artist | Wits, Empathy | `Crafting 1`, `Performance 1` | You are remembered by one patron, troupe, or jealous rival. | Minstrel |
| 3 | Student | Wits, Agility | `Lore 1`, `Insight 1` | You carry one copied diagram, poem, sign, or occult note. | Sorcerer |
| 4 | Acrobat | Agility, Empathy | `Move 1`, `Sleight of Hand 1` | You know roofs, beams, and narrow places in one settlement better than its watch does. | Rogue |
| 5 | Fighter | Strength, Agility | `Melee 1`, `Marksmanship 1` | One old drill-master or war veteran still knows your name. | Fighter |
| 6 | Ghost Child | Agility, Empathy | `Stealth 1`, `Insight 1` | You belong to a loose pack of strays, thieves, or cast-offs. | Outcast |

### Halfling Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Baker's Apprentice | Strength, Empathy | `Crafting 1`, `Performance 1` | One oven-house, cookfire, or feast-hall would still take you in. | Peddler |
| 2 | Laborer | Strength, Empathy | `Might 1`, `Animal Handling 1` | You left behind a field, a beast, or a family argument over work. | Laborer |
| 3 | Craftsman | Agility, Wits | `Crafting 1`, `Insight 1` | You own or crave one fine tool made by better hands than yours. | Peddler |
| 4 | Raised in the Kitchen | Agility, Empathy | `Crafting 1`, `Sleight of Hand 1` | You learned how gossip moves through a house faster than smoke. | Peddler |
| 5 | Bookworm | Wits, Empathy | `Lore 1`, `Healing 1` | One book, fragment, or old tale has grown too important in your mind. | Sorcerer |
| 6 | Loner | Agility, Wits | `Stealth 1`, `Manipulation 1` | You know how to smile at kin while keeping your own counsel. | Rogue |

### Goblin Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Wolfling | Strength, Agility | `Animal Handling 1`, `Endurance 1` | You still think of one wolf pack, or one pack thinks of you. | Hunter |
| 2 | Scrounger | Agility, Empathy | `Stealth 1`, `Manipulation 1` | You know where things vanish in one camp, ruin, or market. | Rogue |
| 3 | Child of the Woods | Agility, Wits | `Scouting 1`, `Survival 1` | One grove, path, or den still feels guarded by kin you cannot name. | Hunter |
| 4 | Wildling | Strength, Empathy | `Melee 1`, `Move 1` | Your clan taught freedom first and obedience never. That still costs you. | Outcast |
| 5 | Wanderer | Agility, Wits | `Survival 1`, `Scouting 1` | You know one shelter from old Mist nights that others would miss in daylight. | Drifter |
| 6 | Storyteller | Wits, Empathy | `Performance 1`, `Lore 1` | One clan elder's tale still points toward treasure, shame, or revenge. | Minstrel |

### Orc Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Minstrel | Wits, Empathy | `Lore 1`, `Performance 1` | You learned one blood-song that can still start a fight if sung aloud. | Minstrel |
| 2 | Worker | Strength, Agility | `Might 1`, `Crafting 1` | Your hands remember labor done for others, and the anger has not left them. | Laborer |
| 3 | Brigand | Strength, Wits | `Melee 1`, `Scouting 1` | You wronged someone, or they wronged you, on a hungry road. | Rogue |
| 4 | Drifter | Agility, Empathy | `Survival 1`, `Animal Handling 1` | One road band, camp, or hidden ford still lies under your memory. | Drifter |
| 5 | Warrior | Strength, Agility | `Melee 1`, `Marksmanship 1` | You know what respect looks like when it is bought in blood. | Fighter |
| 6 | Loner | Wits, Empathy | `Insight 1`, `Survival 1` | You have one reason not to trust your own people first. | Outcast |

### Wolfkin Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Howler | Wits, Empathy | `Performance 1`, `Lore 1` | You know one old clan lament and the name bound to it. | Minstrel |
| 2 | Hunter | Strength, Wits | `Scouting 1`, `Survival 1` | One beast-sign, hunting ground, or old kill-site still draws you back. | Hunter |
| 3 | Outcast | Wits, Empathy | `Insight 1`, `Survival 1` | You still smell the moment your pack turned its back on you. | Outcast |
| 4 | Tracker | Agility, Wits | `Scouting 1`, `Stealth 1` | You can still find one person, beast, or camp by habit if not by scent. | Hunter |
| 5 | Fighter | Strength, Agility | `Melee 1`, `Might 1` | You learned early what dominance costs and what it does not win. | Fighter |
| 6 | Child of the Forest | Wits, Empathy | `Lore 1`, `Survival 1` | One herb-wife, lake, or hollow tree still feels like kin ground. | Druid |

### Dwarf Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Smith's Apprentice | Strength, Wits | `Crafting 1`, `Melee 1` | You still owe a master, forge, or god-marked tool your loyalty. | Laborer |
| 2 | Mineborn | Strength, Wits | `Endurance 1`, `Survival 1` | You know one shaft, seam, or buried way not found on any proper map. | Drifter |
| 3 | Scout's Apprentice | Agility, Wits | `Stealth 1`, `Scouting 1` | One watch-post, cairn, or hidden cut in the hills remains in your memory. | Hunter |
| 4 | Guardian-in-Training | Strength, Agility | `Melee 1`, `Endurance 1` | One oath of defense still weighs on you, fulfilled or not. | Fighter |
| 5 | Carver | Strength, Wits | `Crafting 1`, `Lore 1` | You know how stone yields, and where it refuses. That knowledge has a price. | Peddler |
| 6 | Hard Studies | Wits, Empathy | `Lore 1`, `Insight 1` | You carry one fragment of elder writing or one argument you still mean to prove. | Sorcerer |

### Elf Childhood Foundations

| **D6** | **Foundation** | **Favored Attributes** | **First 2 Skill Points** | **Hook** | **Suggested First Path** |
|---|---|---|---|---|---|
| 1 | Loner | Wits, Empathy | `Insight 1`, `Survival 1` | You spent years at the edge of your own people and learned to stay there. | Outcast |
| 2 | Fighter | Strength, Agility | `Melee 1`, `Marksmanship 1` | One elder warrior still measures you against an old war no one has forgotten. | Fighter |
| 3 | Child of the Forest | Wits, Empathy | `Lore 1`, `Survival 1` | One tree, spring, or grove still answers to your memory. | Druid |
| 4 | Hard Studies | Wits, Empathy | `Lore 1`, `Manipulation 1` | You remember words, names, or signs others wish buried. | Sorcerer |
| 5 | Wanderer | Agility, Wits | `Scouting 1`, `Survival 1` | The road taught you what your own halls would not. | Drifter |
| 6 | Druid's Apprentice | Wits, Agility | `Lore 1`, `Healing 1` | A teacher is dead, gone, or listening from somewhere you cannot reach. | Druid |

### Foundation Standards

These tables should obey five hard rules.

1. A foundation must point toward a life, not lock one in.
2. The first 2 skill points must be useful without becoming over-specialized.
3. Hooks must create pressure, not hand out clean advantages.
4. Suggested first paths should feel natural, but a player must always be free to break away.
5. No foundation result should grant direct talents, silver, or finished gear packages.

## The Four Turns

Every cycle has four different turns.
They should not feel interchangeable.

The name matters.
A turn is not a clean calendar year.
It is one reach of the wheel of life: a stretch of hunger, service, weather, fear, luck, or grace.
One turn may be brief and cruel.
Another may last long enough to grind a person down into habit, then warm them with one small spark of happiness before the wheel bites again.
That is the right grain for this system.

| Turn | Function | What It Usually Brings |
|---|---|---|
| First Turn | Entry | learning, first patron, first duty, rough initiation |
| Second Turn | Pressure | hunger, fear, obligation, debt, quarrel, hard weather |
| Third Turn | Rise | promotion, discovery, recognition, temptation, secret knowledge |
| Fourth Turn | Reckoning | betrayal, battle, scandal, oath, escape, inheritance, ruin |

Each turn is resolved in this order.

### Step A: Make The Turn's Test

Every life path has a turn test.
This is the test that says whether the character stayed afloat in that kind of life.

Examples:

- Fighter: `Melee` or `Might`
- Rogue: `Stealth` or `Sleight of Hand`
- Sorcerer: `Lore` or `Insight`
- Rider: `Animal Handling` or `Move`

The player rolls against the current rank they have at that moment.
If the skill is still `0`, they roll the linked attribute only.

### Step B: Resolve The Result

| Result | Outcome |
|---|---|
| Failure | Gain 1 skill point from the path's hard-lesson list, then roll a mishap for that turn |
| Success | Gain 1 skill point from the path's normal list, then roll the turn event |
| 2+ successes | As success, and gain 1 edge on the turn event roll or 1 extra silver die if the event grants money |

This is the key calibration rule:

- childhood foundation grants the first 2 skill points of the first cycle
- every resolved turn after that gives exactly **1 skill point**
- this preserves the age baselines of `8 / 12 / 16`
- mishaps change the shape of the build, but do not leave a character underbuilt

### Step C: Apply The Event

Each turn has a path-specific event table.
That event may give one of the following:

- gear
- silver
- a contact
- a rival
- a rumor
- a wound
- a talent mark
- a forced path change
- a shift in reputation

### Step D: Mark Wear

Every failed turn test adds one `Wear` mark.

At the end of character creation:

- `0-1 Wear`: no added effect
- `2-3 Wear`: choose one scar, rival, debt, or lingering fear
- `4+ Wear`: choose one, then also begin play with either a chronic pain, a feud, or reduced standing in one settlement

Wear is fiction-first.
It should create hooks and pressure, not hidden numerical punishment.

## Worked Example

Merigall is an Adult Alderlander human.
He begins with three completed cycles.

He rolls `Squire` on the childhood foundation table.
That gives him `Melee 1`, `Healing 1`, and a former master who still remembers his service.
His favored attributes point toward Strength and Empathy, but do not finish the build for him.

For his first cycle he takes `Fighter`.
The first two turns go well, the third leaves him scarred, and the fourth ends with a broken company.
He comes out of the cycle with better `Melee`, some `Survival`, one old comrade, and one hard memory.

For the second cycle he shifts into `Drifter`.
The road gives him `Scouting`, `Insight`, and a hidden shelter from the old Mist years, but it also leaves him with a debt and one place that does not want him back.

For the third cycle he returns to `Fighter`.
He has the skills and history for it, but the life is narrower now.
He ends with a serviceable weapon, one scar with a story behind it, and enough standing to qualify cleanly as a Fighter.

At the end of the process, Merigall does not feel like a pile of efficient picks.
He feels like a man who served, lost his place, walked hungry roads, and took up steel again because he knew nothing else well enough to trust.

## Advancement And Departure

At the end of each cycle, roll once on the path's advancement line.

| Result | Outcome |
|---|---|
| Failure | You leave that path. Roll or choose a new one next cycle. |
| Success | You may remain in the same path next cycle if you want. Gain one listed path benefit. |
| 2+ successes | As success, and gain either one extra contact, one extra rumor, or one path-specific gear benefit. |

A path benefit is never a free extra action, a Willpower engine, or a universal passive combat rider.
It should be one of these:

- one rank in a listed general talent
- one rank increase in the profession talent chosen later, up to Rank 2 at character creation
- one contact or follower
- one mount, tool, or weapon package
- one local reputation shift

## Profession Qualification

The cycle system still ends in the chapter's eight professions.
Use these rules.

- your **last** path is your default profession
- if your last two cycles used different profession paths, choose between those two professions
- if your last cycle ends in a fallback path, choose the profession path in which you hold the most ranks among its core skills

Fallback paths are `Drifter`, `Laborer`, and `Outcast`.
They catch imprisonment, exile, disgrace, hunger, and other breaks in a life.
They are not professions, but they can still lead back into one.

## Path Change And Forced Lives

No life runs clean from youth to trade, faith, or war.
People are driven off, taken in, pressed into service, jailed, bought, ruined, and sent back onto the road.
The system needs rules for that.

### Entry Gates

Most paths have no gate.
If the fiction allows it, a character may enter them.

Use gates only where the path assumes training, access, or recognized standing.

| Path | Entry Gate |
|---|---|
| Fighter | None |
| Rogue | None |
| Hunter | None |
| Drifter | None |
| Laborer | None |
| Outcast | None |
| Druid | `Lore 1` or `Healing 1`, or a shrine, grove, teacher, or sacred duty in the fiction |
| Sorcerer | `Lore 1`, or an occult contact, teacher, grimoire fragment, or marked sign in the fiction |
| Minstrel | `Performance 1` or `Manipulation 1`, or a patron, troupe, or hall that would take you in |
| Peddler | `Manipulation 1` or `Insight 1`, or trade goods, caravan work, or a market contact in the fiction |
| Rider | `Animal Handling 1` or `Move 1`, or access to a herd, mount, or riding household in the fiction |

If a character does not meet a gated path's entry condition, choose another path for that cycle.
If no other path makes sense, the character falls into `Drifter`, `Laborer`, or `Outcast`, whichever best fits the event that broke the old life.

### Voluntary Path Change

At the end of a cycle, a character may leave a path even after a success.
No roll is needed.
The old life has already paid for the next one.

The new path must follow the fiction.
You do not move from a jail pit to horse-warrior without some road between them.

### Forced Departure

A cycle forces a path change if one of these things happens:

- a Fourth Turn event says you must change path
- a mishap says the path is broken
- you fail the advancement roll
- the fiction clearly destroys the old life

When that happens, choose the next path from the event that caused the break.
If the event does not name a path, use the forced-life table below.

### Forced-Life Table

| **D6** | **Cause** | **Next Path** |
|---|---|---|
| 1 | Prison, stockade, hostage-taking, or war captivity | Outcast or Laborer |
| 2 | Debt, bond-service, confiscated goods, or a ruined bargain | Laborer or Peddler |
| 3 | Exile, outlawry, blood-feud, or banishment from kin | Outcast or Drifter |
| 4 | Patron slain, hall burned, company broken, or route collapsed | Drifter or Fighter |
| 5 | Crop failure, plague, winter hunger, or herd-loss | Laborer or Drifter |
| 6 | Scandal, sorcerous stain, shrine curse, or broken oath | Outcast or Druid |

Choose the path that best fits the event.
If both fit, the player chooses.

### Prison, Captivity, And Bond-Service

Prison, war captivity, debt bondage, and forced labor do not need their own full paths.
They are engines that drive a character into the fallback lives.

Use these conversions:

- prison, stockade labor, or chain work becomes `Laborer`
- escape, branding, disgrace, or outlaw flight becomes `Outcast`
- release into rootless wandering becomes `Drifter`
- ransom into a new patron's service may lead to `Fighter`, `Peddler`, or `Rider` if the fiction supports it

The event that caused the fall should leave one mark behind.
Choose one:

- one scar
- one rival
- one debt
- one lowered Standing in a settlement
- one dark secret

### Patron Collapse

Many paths depend on someone stronger than you.
A captain dies.
A trader is ruined.
A shrine loses protection.
A hall closes its gates.

When a patron collapses, do not erase the old cycle.
Turn the break into the next one.

- if the old patron's fall leaves you hunted, move to `Outcast`
- if it leaves you hungry and looking for hire, move to `Drifter`
- if it leaves you bound to salvage, debt, or service, move to `Laborer`
- if a new power takes you in at once, move to the path that new service implies

### Staying In The Same Path

The narrowing tax already discourages staying in one path forever.
Use it every time a character repeats a path after the first completed cycle there.

If a path event or advancement result says the character may remain without an advancement roll, that waives only the roll.
It does not remove the narrowing tax.

## Life Paths

Each path needs one complete suite of turns, mishaps, advancement, and mustering-out.
The table below shows the engine each one must follow.

| Path | Turn Test | Normal Skill List | Hard-Lesson Skill List | Advancement Benefits | Mustering-Out Tone |
|---|---|---|---|---|---|
| Druid | `Lore` or `Survival` | Lore, Survival, Healing, Insight, Animal Handling, Marksmanship | Survival, Insight, Healing | Path of Healing/Sight/Shifting Shapes, Herbalist, Pathfinder, shrine contact | staff, herbs, sacred map, old enemy |
| Fighter | `Melee` or `Might` | Melee, Might, Endurance, Marksmanship, Move, Survival | Endurance, Survival, Healing | Path of Blade/Shield/Enemy, Defender, Pack Rat, war contact | armor, weapon, old standard, scar |
| Hunter | `Scouting` or `Marksmanship` | Scouting, Marksmanship, Survival, Move, Animal Handling, Insight | Survival, Scouting, Endurance | Path of Beast/Arrow/Forest, Sharpshooter, Master of the Hunt, beast contact | bow, traps, hide, hunting feud |
| Minstrel | `Performance` or `Manipulation` | Performance, Manipulation, Lore, Insight, Sleight of Hand, Move | Insight, Performance, Healing | Path of Song/Hymn/Warcry, Lucky, Sharp Tongue, patron contact | instrument, clothes, rumor, rival singer |
| Peddler | `Manipulation` or `Insight` | Manipulation, Insight, Lore, Animal Handling, Scouting, Crafting | Insight, Survival, Manipulation | Path of Gold/Many Things/Lies, Incorruptible, Wanderer, caravan contact | silver, cart, ledgers, debt |
| Rider | `Animal Handling` or `Move` | Animal Handling, Move, Melee, Marksmanship, Survival, Scouting | Survival, Animal Handling, Endurance | Path of Companion/Knight/Plains, Horseback Fighter, Tanner, clan contact | horse, tack, bow, old oath |
| Rogue | `Stealth` or `Sleight of Hand` | Stealth, Sleight of Hand, Scouting, Move, Insight, Melee | Survival, Endurance, Stealth | Path of Face/Poison/Killer, Sixth Sense, Lightning Fast, underworld contact | lockpicks, dagger, hidden stash, bounty |
| Sorcerer | `Lore` or `Insight` | Lore, Insight, Manipulation, Healing, Crafting, Survival | Insight, Survival, Healing | Path of Signs/Stone/Blood/Death, Sharp Tongue, Poisoner, occult contact | staff, books, artifact, stain of magic |
| Drifter | `Survival` or `Move` | Survival, Move, Insight, Scouting, Melee, Manipulation | Endurance, Survival, Insight | Fearless, Lucky, Pack Rat | blanket, knife, rumor, trouble behind you |
| Laborer | `Might` or `Crafting` | Might, Crafting, Endurance, Animal Handling, Survival, Melee | Endurance, Crafting, Survival | Quartermaster, Tanner, Strong Back | tools, beast, kin duty, old injury |
| Outcast | `Stealth` or `Survival` | Stealth, Survival, Scouting, Insight, Move, Melee | Survival, Endurance, Scouting | Sixth Sense, Fearless, Killer's eye | hidden camp, enemy, stolen keepsake |

## Balance Calibration

The subsystem must obey these limits.

### 1. No Extra Skill Inflation

The age totals stay where they are now:

- Young: 8
- Adult: 12
- Old: 16

The path system distributes those points through time.
It does not increase them.

### 2. No Talent Bloom At Character Creation

The current chapter already gives:

- kin talent
- profession talent
- age-based general talents

The life path may shape or redirect those choices, but it should not add a large second talent economy on top.

Safe uses for path advancement:

- allow the chosen profession talent to begin at Rank 2
- swap one general talent into a path-specific one
- grant a narrow non-combat benefit

Unsafe uses:

- free extra attacks
- permanent armor bypass
- standing dodge bonuses
- Willpower refund loops
- free spellcasting outside the existing path structure

### 3. No Willpower Engines

Nothing in character creation should create stored Willpower, bonus Willpower generation, or pseudo-push loops.
The Willpower loop belongs to play.

### 4. Mishaps Must Hurt Fiction First

A failed turn should matter, but not by making the character mathematically dead on arrival.

Good mishaps:

- a rival
- a wound
- debt
- disgrace
- lost gear
- a forced path change
- lower standing in one settlement

Bad mishaps:

- losing a whole turn's skill point
- beginning with broken core numbers
- permanent penalties that stack faster than age already does

### 5. Old Characters Must Gain Breadth, Not Invulnerability

Old characters should feel capable because they have:

- more skills
- more contacts
- more rumors
- more scars

They should not feel untouchable.
The current age attribute loss is correct and should stay.

## Synergy And Exploitation Audit

From the synergy and balance side, the main danger zones are obvious.

### Danger Zone 1: Front-Loaded Combat Builds

If the path system hands out too many direct talent ranks, a player can build a one-decision dominant line before play begins.

Correction:

- no path may grant more than one direct talent-rank increase per cycle
- no character may begin with more than one profession talent above Rank 1

### Danger Zone 2: Safe Caster Starts

Sorcerer and Druid cycles are tempting places to sneak in extra magical access.
That would flatten the early-game danger curve.

Correction:

- magic paths remain profession-gated
- life events may grant grimoires, mentors, symbols, or occult enemies, but not extra spell access outside the existing profession structure

### Danger Zone 3: Gear Compression

If several cycles stack too much armor, rare gear, mounts, and silver, the expedition loop begins too soft.

Correction:

- gear results should be broad but humble
- path gear should mostly be practical, worn, local, and incomplete
- rare treasure should be rumor-facing, not inventory-facing

### Danger Zone 4: Universal Best Path

If one life path gives the cleanest skills, the best gear, and the least dangerous mishaps, the random system stops being a system and becomes a trapdoor into the same build every time.

Correction:

- every path must carry one real pressure
- every path must solve one problem well and leave another exposed

### Cross-Path Audit

The audit below treats the obvious exploit lines as hostile design targets.
If a table result feeds one of these lines too cleanly, the result should be rewritten.

| Exploit Line | Why It Is Dangerous | Required Brake |
|---|---|---|
| Fighter -> Fighter -> Fighter -> Fighter | too much armor, combat talent pressure, and war gear in one line | narrowing tax, scars, debt, deserter pressure, no repeated direct combat talent gain |
| Rogue -> Rogue -> Peddler -> Rogue | too much silver, stealth, underworld access, and light gear efficiency | stash and silver results must come with pursuit, debt, or rivalry |
| Sorcerer -> Sorcerer -> Druid -> Sorcerer | too much occult support with too little social cost | magic paths give stain, patron pressure, exile risk, and no extra spell access |
| Rider -> Rider -> Fighter -> Rider | too much mobility, mount quality, and battlefield competence | only one reliable mount, no warhorse start, armor gains stay modest |
| Peddler -> Peddler -> Rogue -> Peddler | too much silver knowledge plus social leverage | route profit must stay tied to debt, contraband, jealousy, or confiscation |
| Drifter -> Rogue -> Fighter | too smooth a fallback into optimized breadth | fallback paths should harden survival, not hand out premium combat packages |

### Talent Review

Talent-facing results need the hardest leash in the whole subsystem.

Use these rules:

- one path may point strongly toward one profession talent, but not stack several talent boosts in the same life
- fallback paths should lean on broad survival talents such as `Fearless`, `Lucky`, `Pack Rat`, `Quartermaster`, or `Tanner`
- no path should grant both a direct combat talent and a clean second combat package in the same cycle
- social paths should not become the easiest road to combat upgrades

### Gear Review

Gear results need to feel rich in history, not rich in purchasing power.

Use these rules:

- armor packages belong mainly to `Fighter`, and even there should usually top out at studded leather or a worn mail result with history attached
- `Rider` keeps first claim on reliable mounts
- `Rogue` gets concealment, tools, and hidden wealth, not battlefield gear
- `Peddler` gets utility, route knowledge, scales, ledgers, carts, and pack beasts, not military superiority
- fallback paths should almost always grant patched, borrowed, stolen, or improvised gear

### Caster Review

The magic paths must never become the safe answer for clever players.

Use these rules:

- `Sorcerer` and `Druid` may grant occult contacts, signs, tools, fragments, and enemies
- they may not grant extra spellcasting access, free rituals, or extra Willpower engines
- occult success should leave marks: fear, stain, patron claims, exile, or dangerous notice
- the best magic starts should still feel exposed in flesh, gear, or social standing

### Social And Rogue Review

`Rogue`, `Minstrel`, and `Peddler` can easily become soft-optimal paths because they solve too many problems at once.

Use these rules:

- silver on these paths should come with people who want it back
- secret knowledge should create leverage, not automatic safety
- disguise, rumor, and blackmail results should open doors in one place and close them in another
- no social path should grant both rich silver and a clean talent bump in the same turn

### Old Character Review

Old characters should look broad, scarred, and burdened.
They should not look strictly better in every direction.

Use these rules:

- Old characters gain more contacts, rumors, and scars before they gain better gear
- extra cycles should widen the sheet more often than they sharpen one core attack plan
- old age already reduces attribute budget, and the life generator must not quietly buy that loss back through stacked premium rewards

### Banned Result Types

The following result types should not appear on life-path tables:

- free extra attacks
- free Willpower or Willpower regeneration
- direct armor bypass
- permanent dodge or defense bonuses with no cost
- more than one direct talent-rank increase in a cycle
- a second profession talent at character creation
- a warhorse or elite mount outside exceptional campaign-specific play
- heavy armor plus rich silver on the same start
- extra spell access outside normal profession rules
- clean treasure windfalls with no debt, feud, pursuit, stain, or dispute attached

## Lore Fit

The system belongs in Ravenland only if the tables remember the land that shaped them.

This means:

- no abstract academy track detached from place and patron
- no modern institutions
- no clean career ladder
- no retirement comfort

The paths must smell of the setting:

- village duty
- wet roads
- rusted mail
- shrines in old groves
- old silver
- horse clans
- refugee stockades
- outlaw camps
- lords with six men and one rotten tower pretending to be kingdoms

The human peoples should also show up without becoming fenced subclasses.

Examples:

- Aslene results should lean toward herds, riding, clan duty, storms, and the long horizon
- Alderlander results should lean toward levy, walls, oaths, ledgers, priests, and feudal command
- Ailander results should lean toward pasture, shrine, kin obligation, old songs, and practical mysticism

These should be event colors, not separate mechanical engines.

## Human Peoples And Local Pressures

The three human peoples need to be felt throughout the tables without breaking into three separate subsystems.
They should lean on different fears, duties, and kinds of authority.

### Alderlander Color

Use Alderlander color when the life points toward walls, levy service, toll roads, ferries, scribes, castellans, tax men, and half-starved lordships pretending to old power.

Good pressures:

- levy duty
- hall service
- grain tallies
- shrine offerings made from fear rather than love
- Rust Brother scrutiny
- old war roads and broken towers

### Aslene Color

Use Aslene color when the life points toward herd wealth, clan honor, horse-flesh, open wind, riding routes, cattle theft, feud, and old gods remembered in the saddle.

Good pressures:

- blood-feud
- herd loss
- clan elders
- horse trade
- fire and storm on the plains
- long roads between camps

### Ailander Color

Use Ailander color when the life points toward raven signs, kin sorrow, hidden shrines, practical mysticism, hunted villages, old songs, and the memory of living half-hidden under fear.

Good pressures:

- Raven Sisters
- shrine care
- kin defense
- omen-reading
- blight, plague, and hunger
- small settlements that remember every face

### Recent World State

The Blood Mist has not been gone long.
That should still shape the tables.

Use these truths everywhere they fit:

- roads have only recently opened
- most people still think in terms of a day's safe travel
- settlements are suspicious of strangers and hungry for rumor
- old routes, ferry points, shrines, and fair-grounds matter because people clung to them for generations
- Rust Brothers, outlaw bands, half-ruined halls, hidden camps, and abandoned steadings still define the edges of safety

### Allowed Social Texture

Use local, broken, or makeshift structures of power.
Prefer these:

- hall-lord
- castellan
- chieftain
- clan elder
- Raven Sister
- Rust Brother
- shrine-keeper
- ferryman
- caravan master
- outlaw chief

Avoid these tones:

- clean courts
- guild bureaucracy
- banks
- academies
- civic ladders that feel whole and orderly

## Draft Landing In Chapter 2

If adopted, the Chapter 2 structure should become:

- `## LIFE GENERATOR`
- `### USE THIS METHOD`
- `### STEP 1: KIN AND HOME`
- `### STEP 2: CHILDHOOD FOUNDATION`
- `### STEP 3: CHOOSE AGE`
- `### STEP 4: RESOLVE LIFE CYCLES`
- `#### YEAR ONE`
- `#### YEAR TWO`
- `#### YEAR THREE`
- `#### YEAR FOUR`
- `### STEP 5: MUSTER OUT`
- `### STEP 6: CHOOSE PROFESSION`
- `### STEP 7: HOW DID YOU MEET?`

The current childhood and formative-event tables do not need to be thrown away entirely.
Large parts of them can be mined into:

- childhood foundation tables
- path event tables
- mishap tables
- mustering-out tables

## Fighter Path

### Fighter First Turn: Levy, Guard, Or Blade For Hire

| **D6** | **Event** |
|---|---|
| 1 | **Barracks Lesson.** A hard sergeant beat fear out of you with a stave. Gain `Melee` or `Endurance`. You also gain a rival in the same company. |
| 2 | **Shield Wall.** You held a line for the first time and learned to trust wood and iron. Gain `Might` or `Melee`. If you already have a shield, it is scarred but serviceable. |
| 3 | **Night Watch.** You learned boredom, cold, and how danger sounds before it shows itself. Gain `Scouting` or `Insight`. |
| 4 | **Hall-Lord's Favor.** Someone above your station noticed you. Gain `Manipulation` or `Melee`. You also gain one contact tied to a hall, tower, or garrison. |
| 5 | **Camp Sickness.** Fever took half the tent rows. Gain `Healing` or `Endurance`. You also gain one Wear. |
| 6 | **Spoils.** The dead had no use for what they carried. Gain `Survival` or `Melee`. Roll one silver die and keep the result. |

### Fighter Second Turn: March, Hunger, And Orders

| **D6** | **Event** |
|---|---|
| 1 | **Long March.** Your boots rotted and your back bent under the pack. Gain `Survival` or `Endurance`. |
| 2 | **Dirty Work.** You were ordered to do something shameful. Gain `Insight` or `Manipulation`. You also gain one rival or one dark memory. |
| 3 | **Rough Company.** You learned how soldiers settle quarrels where no law can hear them. Gain `Melee` or `Might`. |
| 4 | **Supply Raid.** Hunger drove your band to theft, or your captain called it requisition. Gain `Scouting` or `Move`. |
| 5 | **Winter Camp.** Mud, wet wool, and thin stew taught you patience. Gain `Endurance` or `Healing`. |
| 6 | **Veteran's Tale.** An older fighter taught you where lines break and men lie. Gain `Lore` or `Melee`. You also gain one rumor about a battlefield, ruin, or buried standard. |

### Fighter Third Turn: Battle And Promotion

| **D6** | **Event** |
|---|---|
| 1 | **First Blood.** You killed at arm's length and learned the sound it makes. Gain `Melee` or `Marksmanship`. |
| 2 | **Standard Duty.** You carried colors, messages, or commands through danger. Gain `Move` or `Manipulation`. |
| 3 | **Arrow Storm.** You survived what should have dropped you. Gain `Endurance` or `Healing`. You also gain one scar. |
| 4 | **Picked For The Front.** A captain trusted you where the line would buckle first. Gain `Might` or `Melee`. |
| 5 | **Siege Work.** You learned ladders, ropes, and patience under stones. Gain `Crafting` or `Marksmanship`. |
| 6 | **Field Name.** The company began calling you by deed instead of birth. Gain `Melee` or `Insight`. You also gain +1 Standing in one settlement tied to the campaign. |

### Fighter Fourth Turn: Last Stand, Oath, Or Defeat

| **D6** | **Event** |
|---|---|
| 1 | **Broken Company.** The banner fell, the captain died, or the pay chest vanished. Gain `Survival` or `Scouting`. You must change path next cycle unless you spend your advancement result to remain. |
| 2 | **Honors Paid In Silver.** Your service ended cleanly. Gain `Manipulation` or `Insight`. Roll two silver dice and keep the highest. |
| 3 | **Bad Wound.** You left the field alive but not whole. Gain `Healing` or `Endurance`. You also gain one Wear and one scar. |
| 4 | **Sworn Blade.** A hall-lord, clan chief, or war-band leader offered continued service. Gain `Melee` or `Manipulation`. You may remain in Fighter next cycle without an advancement roll if you accept that patron as a contact. |
| 5 | **Massacre.** You escaped what others did not. Gain `Survival` or `Move`. You also gain one rumor about the killer responsible. |
| 6 | **Named In Victory.** Your deed was seen and remembered. Gain `Melee` or `Marksmanship`. You may take one Fighter path benefit even if your advancement roll later fails. |

### Fighter Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Captured and stripped. Change your next cycle to Outcast or Rogue. |
| 2 | Left for dead. Gain one scar and one enemy who thinks you should have stayed buried. |
| 3 | You obeyed a foul order. Begin play with a dark secret tied to that deed. |
| 4 | You deserted. Lower your Standing by 1 in one settlement that knows your face. |
| 5 | A comrade died because of you, or because you think so. Gain a grieving contact or a blood-feud rival. |
| 6 | Your body held, your nerve did not. Gain `Insight` or `Endurance`, then take one fear tied to fire, cavalry, sorcery, or enclosed places. |

### Fighter Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Defender` |
| 2 | Rank 1 in `Pack Rat` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Fighter |
| 4 | One war contact |
| 5 | One armor or weapon package of standard quality |
| 6 | One local reputation gain and one rumor about a ruin, battlefield, or old treasury |

### Fighter Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Chainmail or studded leather, worn but sound |
| 2 | One good weapon and one scar with a name behind it |
| 3 | One old comrade contact and one rumor about buried spoils |
| 4 | `2D6` silver and one debt still unpaid |
| 5 | One mount or pack beast, not a warhorse |
| 6 | A banner scrap, officer's token, or campaign relic that can open one door and close another |

## Rogue Path

### Rogue First Turn: Lookout, Runner, Or Cutpurse

| **D6** | **Event** |
|---|---|
| 1 | **Street Lesson.** Someone taught you where the knives come from and where the bodies go. Gain `Stealth` or `Insight`. |
| 2 | **Quick Hands.** You found coin in a place someone else thought safe. Gain `Sleight of Hand` or `Move`. |
| 3 | **Night Roofs.** You crossed beams, sheds, and wet shingles in the dark. Gain `Move` or `Scouting`. |
| 4 | **Knife In The Sleeve.** You learned what happens when theft turns to panic. Gain `Melee` or `Stealth`. |
| 5 | **Bought Silence.** Someone paid you not to talk. Gain `Manipulation` or `Insight`. Roll one silver die. |
| 6 | **Taken In.** A gang, crew, or smuggling ring gave you work. Gain `Stealth` or `Sleight of Hand`. You also gain one criminal contact. |

### Rogue Second Turn: Heat And Hunger

| **D6** | **Event** |
|---|---|
| 1 | **Guard Sweep.** The village, ferry, or camp grew watchful. Gain `Scouting` or `Move`. |
| 2 | **Bad Fence.** You sold to the wrong buyer. Gain `Insight` or `Manipulation`. You also gain one rival. |
| 3 | **Cold Nights.** Hunger and wet straw taught you patience. Gain `Survival` or `Endurance`. |
| 4 | **Marked Door.** You cased a richer house than usual. Gain `Scouting` or `Sleight of Hand`. |
| 5 | **Work For A Patron.** A hall-lord, Raven Sister, or peddler used you quietly. Gain `Manipulation` or `Insight`. You also gain one high-born or dangerous contact. |
| 6 | **Shared Score.** A partner saved your skin on the way out. Gain `Stealth` or `Melee`. Choose one contact or one future debt. |

### Rogue Third Turn: Big Score Or Dirty Fall

| **D6** | **Event** |
|---|---|
| 1 | **Empty Vault.** The map was wrong or the treasure already gone. Gain `Insight` or `Survival`. |
| 2 | **Perfect Entry.** For one night every hinge, dog, and drunk slept at the right time. Gain `Sleight of Hand` or `Stealth`. |
| 3 | **Poison Lesson.** Someone taught you a quieter way to end trouble. Gain `Crafting` or `Insight`. You may treat poison use as part of your later profession history. |
| 4 | **Cell Door.** You spent time behind wood or iron. Gain `Endurance` or `Insight`. You also gain one Wear. |
| 5 | **Guild Notice.** Bigger thieves learned your name. Gain `Manipulation` or `Scouting`. |
| 6 | **Hidden Cache.** You salted coin or tools away where only you could find them. Gain `Move` or `Sleight of Hand`. Roll two silver dice and keep both. |

### Rogue Fourth Turn: Betrayal, Escape, Or Reinvention

| **D6** | **Event** |
|---|---|
| 1 | **Sold Out.** A friend gave you to guards, slavers, or a wronged patron. Gain `Insight` or `Endurance`. You must change path next cycle unless you take the traitor as a sworn enemy. |
| 2 | **Clean Getaway.** You left with enough silver and no one close behind. Gain `Move` or `Scouting`. Roll two silver dice. |
| 3 | **Blood On The Job.** A theft became a killing. Gain `Melee` or `Stealth`. You also gain one dark secret. |
| 4 | **Under New Name.** You vanished and returned as someone else. Gain `Manipulation` or `Insight`. Start with one false identity in one settlement. |
| 5 | **Shared Blackmail.** You learned something worth more than coin. Gain `Insight` or `Manipulation`. You also gain one rumor tied to a hall-lord, Raven Sister, or caravan master. |
| 6 | **King Of Rats.** For a short while, everyone below the law answered to you. Gain `Stealth` or `Sleight of Hand`. You may take one Rogue advancement benefit even if your advancement roll later fails. |

### Rogue Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Branded, beaten, or maimed in public. Gain one scar and lower Standing by 1 in one settlement. |
| 2 | A score went bad and left a corpse behind. Gain one enemy tied to that dead person's kin or patron. |
| 3 | Thrown into a cell. Your next cycle must be Fighter, Outcast, or Drifter unless you buy your way free through an event. |
| 4 | Your hidden cache was found first. Lose one gear result from this cycle and gain one rival. |
| 5 | You crossed an outlaw chief. Gain one bounty or one gang feud. |
| 6 | Panic taught you caution. Gain `Endurance` or `Insight`, then begin play with one fear tied to dogs, prison, heights, or bells in the night. |

### Rogue Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Sixth Sense` |
| 2 | Rank 1 in `Lightning Fast` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Rogue |
| 4 | One underworld contact |
| 5 | Lockpicks, dagger, and a hidden stash of silver |
| 6 | One rumor about a lair, treasure site, or compromising secret |

### Rogue Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Lockpicks, dagger, and a rolled cloak that hides more than rain |
| 2 | `2D6` silver and one person who wants it back |
| 3 | One underworld contact and one jealous rival |
| 4 | A hidden stash in one settlement |
| 5 | A stolen trinket, seal, or letter worth trouble |
| 6 | A map fragment or blackmail secret tied to a ruin, hall, or caravan route |

## Sorcerer Path

### Sorcerer First Turn: Apprentice, Reader, Or Dabbler

| **D6** | **Event** |
|---|---|
| 1 | **Dusty Lessons.** You read until your eyes burned and your sleep soured. Gain `Lore` or `Insight`. |
| 2 | **Master's Errand.** A teacher trusted you with a dangerous task. Gain `Manipulation` or `Survival`. |
| 3 | **Hidden Text.** You found writing not meant for your hands. Gain `Lore` or `Crafting`. |
| 4 | **Circle Of Salt.** You took part in your first true rite and learned fear. Gain `Healing` or `Insight`. |
| 5 | **Patron's Coin.** Someone paid for your studies and expects a return. Gain `Manipulation` or `Lore`. Roll one silver die and take one patron contact. |
| 6 | **Night Voices.** Something answered from the other side of sleep. Gain `Insight` or `Survival`. You also gain one occult rumor. |

### Sorcerer Second Turn: Experiment And Price

| **D6** | **Event** |
|---|---|
| 1 | **Failed Working.** You bled for knowledge and learned caution. Gain `Healing` or `Lore`. Add one Wear. |
| 2 | **Old Bones.** A grave, ruin, or cairn yielded secrets. Gain `Scouting` or `Lore`. |
| 3 | **Court Service.** You read omens, soothed nerves, or lied for someone in power. Gain `Manipulation` or `Insight`. |
| 4 | **Poison Shelf.** You learned what grows, seeps, and kills. Gain `Crafting` or `Healing`. |
| 5 | **Forbidden Companion.** Another student, ghost, or hidden correspondent traded knowledge with you. Gain `Insight` or `Manipulation`. You also gain one occult contact. |
| 6 | **Hard Winter.** Books do not keep the cold out. Gain `Survival` or `Lore`. |

### Sorcerer Third Turn: Recognition Or Stain

| **D6** | **Event** |
|---|---|
| 1 | **Symbol Found.** A sign, stone, vein, or bloodline called to you. Gain `Lore` or `Insight`. |
| 2 | **Named As Useful.** A hall-lord, cult, or caravan wanted a sorcerer close at hand. Gain `Manipulation` or `Lore`. |
| 3 | **Blood Cost.** You learned power is dearer than silver. Gain `Healing` or `Insight`. You also gain one scar or one dark secret. |
| 4 | **Buried Artifact.** You touched something older than your teacher admitted. Gain `Crafting` or `Lore`. |
| 5 | **Jealous Eye.** Another practitioner marked you as rival or prey. Gain `Insight` or `Manipulation`. You also gain one rival. |
| 6 | **Whispered Name.** People began seeking you for cures, omens, lies, or curses. Gain `Manipulation` or `Healing`. Gain +1 Standing in one settlement that fears or needs you. |

### Sorcerer Fourth Turn: Break, Exile, Or Patronage

| **D6** | **Event** |
|---|---|
| 1 | **Driven Out.** Your work frightened the wrong people. Gain `Survival` or `Move`. You must change path next cycle unless you stay under a powerful patron's protection. |
| 2 | **Arcane Favor.** Someone in a hall, shrine, or tower decided your gift was worth the risk. Gain `Manipulation` or `Insight`. Gain one patron contact. |
| 3 | **Ritual Scar.** The rite worked, but not cleanly. Gain `Lore` or `Healing`. You also gain one scar touched by sorcery. |
| 4 | **Grimoire Fragment.** You leave with pages, notes, or signs incomplete but precious. Gain `Crafting` or `Lore`. |
| 5 | **Haunted Success.** You got what you wanted and hate the memory of it. Gain `Insight` or `Manipulation`. Add one dark secret. |
| 6 | **Master Departed.** Your teacher died, vanished, or surrendered the work to you. Gain `Lore` or `Insight`. You may take one Sorcerer advancement benefit even if your advancement roll later fails. |

### Sorcerer Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Your experiment maimed someone important. Gain one enemy and one fear of discovery. |
| 2 | You were denounced as unclean, cursed, or dangerous. Lower Standing by 1 in one settlement. |
| 3 | Your notes were stolen. Gain one occult rival and lose one gear benefit from this cycle. |
| 4 | A patron demanded more than you can safely give. Begin play owing a service, secret, or relic. |
| 5 | Mishap and backlash left a mark on your flesh. Gain one scar known to those who understand magic. |
| 6 | You saw too much. Gain `Insight` or `Healing`, then begin play with one recurring omen, nightmare, or hallucination. |

### Sorcerer Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Sharp Tongue` |
| 2 | Rank 1 in `Poisoner` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Sorcerer |
| 4 | One occult contact or former mentor |
| 5 | Staff, writing kit, and one useful occult text |
| 6 | One rumor about an artifact, demon site, hidden library, or blood-bound lineage |

### Sorcerer Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Staff, writing kit, and a satchel of notes |
| 2 | One occult contact and one occult rival |
| 3 | A grimoire fragment, copied sign, or half-legible formula |
| 4 | `D6` silver and one expensive promise owed to a patron |
| 5 | One scar, stain, or visible mark tied to mishap or rite |
| 6 | One rumor about an artifact, demon-haunt, or hidden teacher that the GM may build on later |

## Druid Path

### Druid First Turn: Shrine, Grove, Or Wandering Teacher

| **D6** | **Event** |
|---|---|
| 1 | **Shrine Duty.** You kept a lonely holy place through rain and neglect. Gain `Lore` or `Survival`. |
| 2 | **Herb Basket.** You learned what heals, what numbs, and what kills. Gain `Healing` or `Crafting`. |
| 3 | **Forest Warning.** Something in the trees taught you caution. Gain `Scouting` or `Animal Handling`. |
| 4 | **Pilgrim's Question.** A stranger asked for truth and left trouble behind. Gain `Insight` or `Manipulation`. |
| 5 | **Burial Work.** You laid out dead kin, beast, or wanderer. Gain `Healing` or `Lore`. |
| 6 | **Old Teacher.** Someone showed you signs no village priest or Raven Sister would dare name. Gain `Lore` or `Insight`. Gain one druidic contact. |

### Druid Second Turn: Weather, Duty, And Omen

| **D6** | **Event** |
|---|---|
| 1 | **Flood Or Drought.** The land failed and folk came begging. Gain `Survival` or `Healing`. |
| 2 | **Broken Beast.** You saved or slew something wounded and dangerous. Gain `Animal Handling` or `Marksmanship`. |
| 3 | **Sacred Boundary.** You guarded a place others should not have crossed. Gain `Melee` or `Scouting`. |
| 4 | **Bad Dream.** Sleep brought warning, if not clarity. Gain `Insight` or `Lore`. |
| 5 | **Village Suspicion.** Someone called you holy, someone else called you cursed. Gain `Manipulation` or `Insight`. |
| 6 | **Long Forage.** You lived lean and kept moving. Gain `Survival` or `Scouting`. |

### Druid Third Turn: Power And Burden

| **D6** | **Event** |
|---|---|
| 1 | **Hidden Pool.** You found a place where the world felt thin. Gain `Lore` or `Healing`. |
| 2 | **Protected The Wild.** Men with axes or torches learned you would not step aside. Gain `Marksmanship` or `Melee`. |
| 3 | **Spoken For.** A chieftain, village, or clan sought your blessing. Gain `Manipulation` or `Insight`. |
| 4 | **Spirit Sign.** A beast, storm, or blight took on meaning for you. Gain `Lore` or `Animal Handling`. |
| 5 | **Forbidden Rite.** You stood too close to power and did not forget it. Gain `Healing` or `Insight`. Add one Wear. |
| 6 | **Gathered Favors.** Quiet folk started owing you thanks. Gain `Insight` or `Survival`. Gain one contact. |

### Druid Fourth Turn: Exile, Reverence, Or Loss

| **D6** | **Event** |
|---|---|
| 1 | **Driven Out.** Someone feared your work or needed a scapegoat. Gain `Survival` or `Move`. You must change path next cycle unless protected by a strong contact. |
| 2 | **Sacred Charge.** You were entrusted with a place, relic, or oath. Gain `Lore` or `Manipulation`. |
| 3 | **Plague Work.** You stayed where others fled. Gain `Healing` or `Endurance`. Gain one scar or one grateful settlement. |
| 4 | **Blighted Grove.** Something ancient was spoiled, cut down, or burned. Gain `Scouting` or `Insight`. Gain one enemy tied to the deed. |
| 5 | **Pilgrimage.** You walked farther than you intended and learned the land by foot and hunger. Gain `Survival` or `Lore`. |
| 6 | **Recognized As Wise.** Word of your judgment spread. Gain `Insight` or `Manipulation`. You may take one Druid advancement benefit even if your later advancement roll fails. |

### Druid Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | You misread a sign and someone paid for it. Gain one guilty memory and one rival. |
| 2 | A rite turned on you. Gain one scar or visible mark tied to the mishap. |
| 3 | Villagers denounced you. Lower Standing by 1 in one settlement. |
| 4 | You protected the wrong thing, or at the wrong cost. Gain one enemy. |
| 5 | Something followed you out of a holy or cursed place. Gain one recurring omen. |
| 6 | Your teacher died, vanished, or condemned you. Your next cycle must change path unless you take one Wear. |

### Druid Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Herbalist` |
| 2 | Rank 1 in `Pathfinder` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Druid |
| 4 | One shrine, circle, or wise contact |
| 5 | Staff, herbs, and a healer's satchel |
| 6 | One sacred rumor, hidden grove, or old curse the GM may develop later |

### Druid Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Staff, herbs, and simple ritual tools |
| 2 | One wise contact and one suspicious priest, elder, or hunter |
| 3 | A sacred charm, rune-stick, or bark-scroll |
| 4 | `D6` silver and one debt of gratitude from common folk |
| 5 | One scar from plague, rite, beast, or weather |
| 6 | One rumor about a hidden grove, blighted shrine, or ancient site |

## Hunter Path

### Hunter First Turn: Trail, Bow, And Cold Camp

| **D6** | **Event** |
|---|---|
| 1 | **Tracked Fresh Kill.** You followed blood before you knew wisdom. Gain `Scouting` or `Survival`. |
| 2 | **Learned The Bow.** Someone corrected your hands until the shot flew true. Gain `Marksmanship` or `Move`. |
| 3 | **Camp Meat.** Others ate because you did not miss. Gain `Survival` or `Animal Handling`. |
| 4 | **Snare Line.** You learned patience from cord, branch, and spoor. Gain `Crafting` or `Scouting`. |
| 5 | **Bad Weather.** The sky taught you what pride is worth. Gain `Endurance` or `Survival`. |
| 6 | **Old Forester.** Someone taught you where beasts break and where men do. Gain `Insight` or `Marksmanship`. |

### Hunter Second Turn: Range And Risk

| **D6** | **Event** |
|---|---|
| 1 | **Wounded Beast.** The prey doubled back and made you earn the kill. Gain `Melee` or `Scouting`. |
| 2 | **Lean Season.** You hunted for hungry folk and felt each empty day. Gain `Survival` or `Insight`. |
| 3 | **Taken Trail.** You found signs of other hunters where none should have been. Gain `Scouting` or `Move`. Gain one rival or rumor. |
| 4 | **Long Shot.** One arrow made your name in camp. Gain `Marksmanship` or `Insight`. |
| 5 | **Beast Tamer.** A dog, hawk, or stubborn mount taught you humility. Gain `Animal Handling` or `Endurance`. |
| 6 | **Night Fire.** Stories by the coals taught you the old paths of the land. Gain `Lore` or `Survival`. |

### Hunter Third Turn: Reputation, Blood, And Teeth

| **D6** | **Event** |
|---|---|
| 1 | **Big Kill.** You brought down something folk feared. Gain `Marksmanship` or `Melee`. |
| 2 | **Guide Work.** You led others who knew less than they admitted. Gain `Scouting` or `Manipulation`. |
| 3 | **Winter Hunger.** You learned what men become when game runs thin. Gain `Insight` or `Survival`. |
| 4 | **Territory Mark.** You began to think of a stretch of land as yours. Gain `Scouting` or `Animal Handling`. |
| 5 | **Rust Or Raven.** Rust Brothers, Raven Sisters, or tax-hands took interest in the woods. Gain `Move` or `Insight`. |
| 6 | **Best Skin.** A pelt, antler rack, or set of fangs bought you more notice than comfort. Gain `Crafting` or `Marksmanship`. Roll one silver die. |

### Hunter Fourth Turn: Mastery Or Mauling

| **D6** | **Event** |
|---|---|
| 1 | **Mauled.** You lived, but the beast left something behind in flesh or nerve. Gain `Endurance` or `Healing`. Gain one scar. |
| 2 | **Named Guide.** Caravans, scouts, or hall-lords sought your eye. Gain `Manipulation` or `Scouting`. |
| 3 | **Poacher's Fight.** Another hunter crossed your line or you crossed theirs. Gain `Melee` or `Marksmanship`. Gain one rival. |
| 4 | **Forest Fire.** Flame or smoke ruined land you knew by heart. Gain `Survival` or `Move`. You must change path next cycle unless revenge or duty keeps you here. |
| 5 | **Trained Another.** You passed on what the wild taught you. Gain `Insight` or `Animal Handling`. |
| 6 | **True Reputation.** Folk began trusting your judgment in the wastes. Gain `Scouting` or `Insight`. You may take one Hunter advancement benefit even if the later roll fails. |

### Hunter Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | A beast tore you open. Gain one scar and one fear. |
| 2 | You led someone into danger and they did not come back out. Gain one guilty contact or one grieving enemy. |
| 3 | Hunger drove you to theft. Lower Standing by 1 in one settlement. |
| 4 | You crossed the wrong forester, clan, or patrol. Gain one rival. |
| 5 | You brought something home that should have stayed in the dark woods. Gain one omen or rumor. |
| 6 | Your prey was no beast at all, or not only that. Your next cycle must change path unless you take one Wear. |

### Hunter Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Master of the Hunt` |
| 2 | Rank 1 in `Sharpshooter` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Hunter |
| 4 | One hunting contact, guide, or forester ally |
| 5 | Bow, traps, and field gear |
| 6 | One rumor about a beast den, hidden trail, or monster haunt |

### Hunter Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Bow, arrows, knife, and practical field gear |
| 2 | Traps, skins, and one winter-worthy cloak |
| 3 | One beastwise contact and one hunting rival |
| 4 | `D6` silver and one claim on meat, hides, or guiding work |
| 5 | One scar from horn, fang, claw, or weather |
| 6 | One rumor about a lair, legendary beast, or unmarked trail |

## Minstrel Path

### Minstrel First Turn: Firelight And First Audience

| **D6** | **Event** |
|---|---|
| 1 | **Campfire Song.** Folk quieted to hear you. Gain `Performance` or `Lore`. |
| 2 | **Cheap Inn.** You learned how to hold a room full of drunks. Gain `Performance` or `Manipulation`. |
| 3 | **Borrowed Tale.** You stole a story and told it better than its owner. Gain `Lore` or `Insight`. |
| 4 | **Traveling Troupe.** A loose company took you in. Gain `Move` or `Performance`. Gain one contact. |
| 5 | **Hall Fire.** You learned the difference between applause and danger. Gain `Manipulation` or `Insight`. |
| 6 | **Street Performance.** Hunger taught you timing and nerve. Gain `Performance` or `Sleight of Hand`. |

### Minstrel Second Turn: Patronage And Jealousy

| **D6** | **Event** |
|---|---|
| 1 | **Proud Patron.** A hall-lord, shrine-keeper, or rich widow kept you in drink and demanded flattery. Gain `Manipulation` or `Performance`. |
| 2 | **Sharp Rival.** Another singer, poet, or player wanted you humbled. Gain `Insight` or `Performance`. Gain one rival. |
| 3 | **Love Ballad.** You turned somebody's grief into your living. Gain `Lore` or `Manipulation`. |
| 4 | **Road Dust.** You walked from hall to fair to camp with your art on your back. Gain `Move` or `Survival`. |
| 5 | **Improvised Lie.** Your tongue got you out of one danger and into the next. Gain `Manipulation` or `Insight`. |
| 6 | **Strange Audience.** Soldiers, outlaws, or cultists paid to hear what decent folk would not. Gain `Performance` or `Scouting`. |

### Minstrel Third Turn: Renown Or Trouble

| **D6** | **Event** |
|---|---|
| 1 | **Popular Ballad.** A song of yours started walking without you. Gain `Performance` or `Lore`. |
| 2 | **Hall Intrigue.** Your ears heard more than your mouth should repeat. Gain `Insight` or `Manipulation`. |
| 3 | **Battlefield Song.** You saw men march to death and learned what rhythm does to fear. Gain `Performance` or `Melee`. |
| 4 | **Mockery.** You made the wrong hall-lord, Raven Sister, or chief a laughingstock. Gain `Insight` or `Move`. Gain one enemy. |
| 5 | **Epic Fragment.** You found a half-remembered tale tied to a real ruin or relic. Gain `Lore` or `Scouting`. Gain one rumor. |
| 6 | **Paid In Kind.** Silver was short, so folk paid in food, clothes, gossip, or favors. Gain `Manipulation` or `Sleight of Hand`. Roll one silver die. |

### Minstrel Fourth Turn: Last Performance, New Name

| **D6** | **Event** |
|---|---|
| 1 | **Driven Off.** Your voice stayed welcome longer than your face. Gain `Move` or `Survival`. You must change path next cycle unless a patron keeps you. |
| 2 | **Favored Entertainer.** A hall or camp became yours for a season. Gain `Performance` or `Manipulation`. |
| 3 | **Duel Of Words.** Insults ended in steel, blood, or both. Gain `Melee` or `Insight`. |
| 4 | **Witness To History.** You were present at something others will sing about badly. Gain `Lore` or `Insight`. |
| 5 | **Broken Heart.** Love, vanity, or betrayal drove you back onto the road. Gain `Performance` or `Move`. Gain one dark memory. |
| 6 | **True Name Won.** You gained a name folk remember. Gain `Performance` or `Lore`. You may take one Minstrel advancement benefit even if the later roll fails. |

### Minstrel Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | You slandered the wrong person. Gain one enemy. |
| 2 | Drink, lust, or pride left you in disgrace. Lower Standing by 1 in one settlement. |
| 3 | Your troupe broke apart violently. Gain one rival or one dead contact's memory. |
| 4 | You stole a song, tale, or lover and paid for it. Gain one scar or one dark secret. |
| 5 | A patron's protection turned to ownership. Your next cycle must change path unless you carry that patron as a burden. |
| 6 | Something you sang woke more than applause. Gain one omen, rumor, or uncanny follower. |

### Minstrel Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Lucky` |
| 2 | Rank 1 in `Sharp Tongue` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Minstrel |
| 4 | One patron, troupe ally, or hall contact |
| 5 | Instrument, good clothes, and writing kit |
| 6 | One rumor, legend fragment, or map clue learned through song |

### Minstrel Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Instrument, good cloak, and writing tools |
| 2 | `D6` silver and one favor owed from a hall, tavern, or camp |
| 3 | One patron contact and one jealous rival |
| 4 | A famous song, insult, or story tied to your name |
| 5 | One scar from a duel, bottle, or bad road |
| 6 | One legend fragment pointing toward a ruin, relic, or feud |

## Peddler Path

### Peddler First Turn: Cart, Ledger, And Road Dust

| **D6** | **Event** |
|---|---|
| 1 | **Learned The Trade.** Someone taught you weights, lies, and patience. Gain `Manipulation` or `Insight`. |
| 2 | **Pack Beast.** You learned the worth of calm hands and sound rope. Gain `Animal Handling` or `Move`. |
| 3 | **Village Fair.** Folk bought what they could not grow. Gain `Manipulation` or `Lore`. |
| 4 | **Thin Profit.** You learned how little separates trade from begging. Gain `Insight` or `Survival`. |
| 5 | **Traveling Stock.** You kept goods dry through mud and rain. Gain `Crafting` or `Animal Handling`. |
| 6 | **Good Eye.** You learned what something is worth before its owner does. Gain `Insight` or `Manipulation`. |

### Peddler Second Turn: Bargain And Risk

| **D6** | **Event** |
|---|---|
| 1 | **Caravan Work.** You moved with others and learned road discipline. Gain `Scouting` or `Animal Handling`. |
| 2 | **Smuggling Run.** Law, priests, or guards made a business opportunity. Gain `Scouting` or `Manipulation`. |
| 3 | **Bad Debtor.** Someone smiled and paid you never. Gain `Insight` or `Melee`. |
| 4 | **Unexpected Market.** You sold to hunters, soldiers, or worse. Gain `Manipulation` or `Lore`. |
| 5 | **Storm Loss.** Weather and water taught you what stock truly matters. Gain `Survival` or `Crafting`. |
| 6 | **Soft Tongue.** You talked your way past danger. Gain `Manipulation` or `Insight`. Gain one contact. |

### Peddler Third Turn: Wider Roads

| **D6** | **Event** |
|---|---|
| 1 | **Profitable Route.** You found a road others feared more than they should. Gain `Scouting` or `Insight`. Roll one silver die. |
| 2 | **Strong Buyer.** A hall, shrine, or clan chief began buying from you. Gain `Manipulation` or `Lore`. |
| 3 | **Escort Trouble.** Guards, mercenaries, or robbers made trade expensive. Gain `Melee` or `Insight`. |
| 4 | **Found Stock.** A ruin, corpse, or abandoned cart improved your inventory. Gain `Crafting` or `Scouting`. |
| 5 | **False Weights.** You cheated or were cheated and learned to count twice. Gain `Insight` or `Manipulation`. |
| 6 | **Map In The Margins.** A ledger, note, or idle talk gave you a lead worth more than silver. Gain `Lore` or `Scouting`. Gain one rumor. |

### Peddler Fourth Turn: Fortune, Debt, Or Flight

| **D6** | **Event** |
|---|---|
| 1 | **Ruinous Deal.** One bargain broke your purse or your nerves. Gain `Insight` or `Survival`. You must change path next cycle unless you stay to rebuild. |
| 2 | **Well-Liked Trader.** Folk began saving goods for your return. Gain `Manipulation` or `Insight`. |
| 3 | **Dangerous Goods.** You carried something worth killing for. Gain `Scouting` or `Move`. Gain one enemy or one shadowing rumor. |
| 4 | **Good Season.** Silver finally stayed in your hand. Gain `Manipulation` or `Animal Handling`. Roll `2D6` silver and keep the higher die. |
| 5 | **Protected By Favor.** A hall-lord, clan, or shrine took interest in your route. Gain `Lore` or `Insight`. Gain one contact. |
| 6 | **Trader Of Repute.** Your word began carrying weight. Gain `Manipulation` or `Scouting`. You may take one Peddler advancement benefit even if the later roll fails. |

### Peddler Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Robbed on the road. Lose one gear benefit from this cycle and gain one enemy. |
| 2 | You cheated the wrong buyer. Gain one rival. |
| 3 | Debt closed around your throat. Begin play owing silver or service. |
| 4 | Pack animal lost, stolen, or eaten. Gain one bitter memory and one practical shortage. |
| 5 | Rust Brothers, shrine wardens, or hall-lords seized your wares. Lower Standing by 1 in one settlement. |
| 6 | You carried contraband without knowing how far it reached. Your next cycle must change path unless you accept one dangerous patron. |

### Peddler Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Incorruptible` |
| 2 | Rank 1 in `Wanderer` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Peddler |
| 4 | One caravan, fair-ground, or hall contact |
| 5 | Cart, pack beast, scales, and trade kit |
| 6 | One rumor, map lead, or market secret tied to treasure or danger |

### Peddler Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Cart or pack beast with basic trade gear |
| 2 | `2D6` silver and one debt not yet settled |
| 3 | Scales, ledger, writing kit, and fair-day clothes |
| 4 | One strong trade contact and one jealous rival |
| 5 | One hidden route, fair-ground, or supply source |
| 6 | One rumor about contraband, treasure flow, or a buyer who pays too well |

## Rider Path

### Rider First Turn: Saddle, Herd, And Open Ground

| **D6** | **Event** |
|---|---|
| 1 | **Learned The Seat.** You stopped falling and started listening to the beast. Gain `Animal Handling` or `Move`. |
| 2 | **Herd Duty.** You kept stock moving and alive. Gain `Animal Handling` or `Survival`. |
| 3 | **Steppe Wind.** Distance and weather made your lungs and legs their own. Gain `Endurance` or `Move`. |
| 4 | **Mounted Errand.** You carried word or goods where feet would fail. Gain `Scouting` or `Animal Handling`. |
| 5 | **Spear Drill.** You learned to strike without dismounting. Gain `Melee` or `Marksmanship`. |
| 6 | **Clan Elder.** Someone taught you the price of horse-flesh and pride. Gain `Insight` or `Animal Handling`. |

### Rider Second Turn: Speed And Obligation

| **D6** | **Event** |
|---|---|
| 1 | **Hard Ride.** One long ride nearly killed beast and rider alike. Gain `Endurance` or `Survival`. |
| 2 | **Escort Work.** You guarded tribute, kin, or rich fools from horseback. Gain `Melee` or `Scouting`. |
| 3 | **Broken Mount.** You learned the cost of fear, injury, or poor hands. Gain `Healing` or `Animal Handling`. |
| 4 | **Open Competition.** You raced or fought for local pride. Gain `Move` or `Marksmanship`. |
| 5 | **Road Ambush.** Riders can be prey as well as hunters. Gain `Scouting` or `Melee`. |
| 6 | **Good Breeding.** You came into a better beast or better tack than before. Gain `Animal Handling` or `Insight`. |

### Rider Third Turn: War, Herd, Or Renown

| **D6** | **Event** |
|---|---|
| 1 | **War Band.** Mounted steel taught you speed and terror together. Gain `Melee` or `Marksmanship`. |
| 2 | **Messenger Ride.** You crossed dangerous ground for news that mattered. Gain `Move` or `Scouting`. |
| 3 | **Horse Trade.** You learned the silver side of the saddle. Gain `Manipulation` or `Animal Handling`. |
| 4 | **Storm Camp.** You kept beasts and folk alive through bad weather. Gain `Survival` or `Insight`. |
| 5 | **Mounted Hunt.** Open land and bow work sharpened your eye. Gain `Marksmanship` or `Animal Handling`. |
| 6 | **Name On The Plain.** Folk began to speak of you by mount, speed, or temper. Gain `Move` or `Manipulation`. Gain one contact. |

### Rider Fourth Turn: Broken Legs Or Hard-Won Place

| **D6** | **Event** |
|---|---|
| 1 | **Fall.** Beast, weather, or battle threw you hard. Gain `Endurance` or `Healing`. Gain one scar. |
| 2 | **Trusted With The Herd.** Others put living wealth in your hands. Gain `Animal Handling` or `Insight`. |
| 3 | **Blood On The Saddle.** A raid, feud, or skirmish marked you for good. Gain `Melee` or `Marksmanship`. Gain one rival. |
| 4 | **Lost Ground.** Drought, war, or theft ruined the life you knew. Gain `Survival` or `Move`. You must change path next cycle unless you stay to rebuild. |
| 5 | **Good Mount.** You and one beast became hard to separate. Gain `Animal Handling` or `Move`. |
| 6 | **Rider Of Repute.** Your seat and judgment earned respect. Gain `Manipulation` or `Scouting`. You may take one Rider advancement benefit even if the later roll fails. |

### Rider Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Your mount died and took part of you with it. Gain one scar and one grief. |
| 2 | You lost herd, goods, or passengers under your watch. Gain one enemy or one debt. |
| 3 | A fall left you wary. Gain one fear tied to speed, height, or hooves. |
| 4 | Clan or employer judged you poorly. Lower Standing by 1 in one settlement or camp. |
| 5 | Raiders or soldiers marked your trail. Gain one rival. |
| 6 | Your path is broken by loss of beast, clan, or pasture. Your next cycle must change path unless you take one Wear. |

### Rider Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Horseback Fighter` |
| 2 | Rank 1 in `Tanner` |
| 3 | Begin with your chosen profession talent at Rank 2 if you become a Rider |
| 4 | One clan, caravan, or mounted contact |
| 5 | Riding horse with tack and travel gear |
| 6 | One rumor about a road, raid route, hidden pasture, or moving camp |

### Rider Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Riding horse and serviceable tack |
| 2 | Bow or spear, saddle bags, and field kit |
| 3 | One mounted contact and one bitter rival |
| 4 | `D6` silver and one beast-related debt or duty |
| 5 | A branded token, clan knot, or horse charm recognized in some camps |
| 6 | One rumor about raiders, migration, or a fast road to danger |

## Drifter Path

### Drifter First Turn: No Wall, No Master

| **D6** | **Event** |
|---|---|
| 1 | **Road Shelter.** You learned where to sleep without dying. Gain `Survival` or `Scouting`. |
| 2 | **Odd Work.** You took whatever labor the day offered. Gain `Might` or `Manipulation`. |
| 3 | **Quiet Watching.** You lasted by seeing trouble early. Gain `Insight` or `Scouting`. |
| 4 | **Bad Bread.** Hunger taught you what pride can be traded for. Gain `Endurance` or `Survival`. |
| 5 | **Borrowed Name.** It was easier not to tell folk the truth. Gain `Manipulation` or `Move`. |
| 6 | **Fellow Traveler.** Someone on the road shared fire, food, or lies. Gain `Insight` or `Survival`. Gain one contact. |

### Drifter Second Turn: Thin Luck

| **D6** | **Event** |
|---|---|
| 1 | **Mercy Work.** Someone paid you in stew and floorboards. Gain `Manipulation` or `Crafting`. |
| 2 | **Chased Out.** One camp, village, or hall turned cold on you. Gain `Move` or `Survival`. |
| 3 | **Found Shelter.** You learned one hidden place from the old Mist years. Gain `Scouting` or `Insight`. |
| 4 | **Travel Company.** You walked with traders, pilgrims, or soldiers for a while. Gain `Survival` or `Lore`. |
| 5 | **Knife Trouble.** Poverty and fear brought steel close. Gain `Melee` or `Endurance`. |
| 6 | **Road Gossip.** The road pays in rumor if not silver. Gain `Insight` or `Manipulation`. Gain one rumor. |

### Drifter Third Turn: Hard Habit

| **D6** | **Event** |
|---|---|
| 1 | **Crossed Country.** You traveled farther than most folk ever do. Gain `Move` or `Scouting`. |
| 2 | **Worked A Season.** You stayed in one place just long enough to regret it. Gain `Crafting` or `Might`. |
| 3 | **Mist Memory.** Old fear from the Blood Mist years still clings to roads and ditches. Gain `Insight` or `Survival`. |
| 4 | **Shared Fire.** You became useful to outcasts, widows, hunters, or old men with no sons. Gain `Manipulation` or `Insight`. |
| 5 | **Night Theft.** Need pushed your hands before your conscience. Gain `Stealth` or `Sleight of Hand`. |
| 6 | **Weathered.** The road thinned you but did not break you. Gain `Endurance` or `Survival`. |

### Drifter Fourth Turn: Last Road Or New Life

| **D6** | **Event** |
|---|---|
| 1 | **Too Many Doors Closed.** The road ran out of kindness. Gain `Survival` or `Melee`. You must change path next cycle. |
| 2 | **Taken In.** A hall, camp, ferry, or caravan finally offered steadier work. Gain `Manipulation` or `Crafting`. |
| 3 | **Old Enemy Found You.** The road is wide until it narrows all at once. Gain `Move` or `Insight`. Gain one enemy. |
| 4 | **Road Wisdom.** You learned which folk lie first and which weather kills fastest. Gain `Insight` or `Scouting`. |
| 5 | **Quiet Reputation.** Some places began treating you as useful instead of rootless. Gain `Manipulation` or `Survival`. |
| 6 | **Would Not Break.** Hard years tempered rather than hollowed you. Gain `Endurance` or `Move`. You may take one Drifter advancement benefit even if the later roll fails. |

### Drifter Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Beaten and robbed. Gain one scar and lose one gear benefit from this cycle. |
| 2 | Turned away in winter or storm. Gain one fear or one bitter oath. |
| 3 | Accused of theft, sorcery, or plague-carrying. Lower Standing by 1 in one settlement. |
| 4 | Hunger drove you low. Gain one dark memory or one debt. |
| 5 | Someone kind died after helping you. Gain one grieving contact or one guilty burden. |
| 6 | You can no longer bear the road alone. Your next cycle must change path unless you take one Wear. |

### Drifter Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Fearless` |
| 2 | Rank 1 in `Pack Rat` |
| 3 | Rank 1 in `Lucky` |
| 4 | One road contact, ferryman, widow, or caravan hand |
| 5 | Blanket roll, knife, and patched but useful travel gear |
| 6 | One rumor about a shelter, ruin, or forgotten way |

### Drifter Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Blanket, knife, waterskin, and travel kit |
| 2 | One road contact and one place you should not return to |
| 3 | `D6` silver hidden in stitching, boot, or belt |
| 4 | One scar and one tale behind it |
| 5 | One hidden shelter or route known only to a few |
| 6 | One rumor about a ruin, ford, or lost company |

## Laborer Path

### Laborer First Turn: Hands, Tools, And Orders

| **D6** | **Event** |
|---|---|
| 1 | **Field Work.** Soil, frost, and strain hardened you. Gain `Might` or `Endurance`. |
| 2 | **Workshop Chores.** Tools taught care before craft. Gain `Crafting` or `Insight`. |
| 3 | **Stable Labor.** Animals make no allowances for weakness. Gain `Animal Handling` or `Might`. |
| 4 | **Heavy Carry.** You learned how much a body can bear before it curses you. Gain `Endurance` or `Move`. |
| 5 | **Kitchen Or Yard.** Somebody always needs thankless work done. Gain `Crafting` or `Manipulation`. |
| 6 | **Master's Eye.** Someone noticed you were not useless. Gain `Crafting` or `Might`. Gain one contact. |

### Laborer Second Turn: Duty And Exhaustion

| **D6** | **Event** |
|---|---|
| 1 | **Harvest Rush.** Work swallowed dawn and dusk alike. Gain `Endurance` or `Animal Handling`. |
| 2 | **Broken Tool.** You learned repair because replacement was impossible. Gain `Crafting` or `Insight`. |
| 3 | **Poor Pay.** The hand that worked hardest did not eat best. Gain `Manipulation` or `Insight`. |
| 4 | **Building Work.** Rope, timber, stone, or mud became your world for a while. Gain `Crafting` or `Might`. |
| 5 | **Sick Beast.** Livestock are silver with breath inside them. Gain `Animal Handling` or `Healing`. |
| 6 | **Shared Burden.** Another worker became friend, rival, or both. Gain `Insight` or `Melee`. |

### Laborer Third Turn: Skill Or Resentment

| **D6** | **Event** |
|---|---|
| 1 | **Trusted With More.** Better tools or harder work came your way. Gain `Crafting` or `Endurance`. |
| 2 | **Managed Others.** For a while, your hands gave orders instead. Gain `Manipulation` or `Insight`. |
| 3 | **Winter Repairs.** Cold months sharpened useful skill. Gain `Crafting` or `Survival`. |
| 4 | **Workplace Hurt.** Labor bit back with splinter, hoof, stone, or blade. Gain `Healing` or `Endurance`. Gain one scar. |
| 5 | **Side Trade.** You learned to make a little extra under the table. Gain `Crafting` or `Manipulation`. |
| 6 | **Good Reputation.** Someone would ask for you by name when hard work needed doing. Gain `Insight` or `Crafting`. |

### Laborer Fourth Turn: Leaving The Yoke

| **D6** | **Event** |
|---|---|
| 1 | **Worked To The Bone.** You could not stay in that life another season. Gain `Endurance` or `Might`. You must change path next cycle. |
| 2 | **Kept It Running.** A farm, workshop, or camp held together because of you. Gain `Crafting` or `Animal Handling`. |
| 3 | **Bad Master.** Anger finally outweighed obedience. Gain `Melee` or `Manipulation`. Gain one enemy. |
| 4 | **Own Tools.** You ended with gear that was yours and not borrowed. Gain `Crafting` or `Insight`. |
| 5 | **Family Duty.** Kin need and labor bound you tighter than coin ever did. Gain `Insight` or `Animal Handling`. Gain one burden. |
| 6 | **Solid Name.** Folk began to trust your work without standing over it. Gain `Manipulation` or `Crafting`. You may take one Laborer advancement benefit even if the later roll fails. |

### Laborer Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Bad injury on the job. Gain one scar and one fear tied to tool, beast, or height. |
| 2 | Cheated of wages. Begin play owed silver or holding a grudge. |
| 3 | Driven off by a master or kin. Lower Standing by 1 in one settlement. |
| 4 | Hunger and overwork made you cruel or desperate. Gain one dark memory. |
| 5 | A beast, wagon, or structure failed under your care. Gain one enemy or one guilty burden. |
| 6 | This life has wrung all it can from you. Your next cycle must change path unless you take one Wear. |

### Laborer Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Quartermaster` |
| 2 | Rank 1 in `Tanner` |
| 3 | Rank 1 in `Pack Rat` |
| 4 | One employer, craft contact, or farming kin ally |
| 5 | Tool set, practical clothes, and work gear |
| 6 | One rumor tied to stores, hidden tools, cellar caches, or abandoned steadings |

### Laborer Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Tool kit and sturdy practical gear |
| 2 | Pack beast or work animal, if the fiction allows it |
| 3 | `D6` silver and one unpaid obligation |
| 4 | One employer contact and one bitter former master or rival worker |
| 5 | One scar and one useful lesson behind it |
| 6 | One rumor about an abandoned farm, workshop, cellar, or supply cache |

## Outcast Path

### Outcast First Turn: Cut Loose

| **D6** | **Event** |
|---|---|
| 1 | **Cast Out.** You learned quickly what the world charges for solitude. Gain `Survival` or `Insight`. |
| 2 | **Kept Hidden.** Someone sheltered you for reasons of pity, guilt, or profit. Gain `Stealth` or `Manipulation`. Gain one contact. |
| 3 | **Living Rough.** Ditch, hollow, cave, and hedgerow became enough. Gain `Survival` or `Scouting`. |
| 4 | **Stole To Eat.** Shame came second to hunger. Gain `Sleight of Hand` or `Move`. |
| 5 | **Knife Warning.** Loneliness makes poor company and quick steel. Gain `Melee` or `Endurance`. |
| 6 | **Watched From Afar.** You learned settlement life from outside the firelight. Gain `Insight` or `Stealth`. |

### Outcast Second Turn: Harsh Lessons

| **D6** | **Event** |
|---|---|
| 1 | **Hunted.** Dogs, guards, kin, or debt followed your trail. Gain `Move` or `Scouting`. |
| 2 | **Bitter Shelter.** You stayed with worse folk than yourself because the weather demanded it. Gain `Manipulation` or `Insight`. |
| 3 | **Small Theft Ring.** Outcasts find each other eventually. Gain `Stealth` or `Sleight of Hand`. |
| 4 | **Wild Companion.** Beast or half-broken soul kept near your camp for a while. Gain `Animal Handling` or `Insight`. |
| 5 | **Rotten Bargain.** You traded clean conscience for one more month alive. Gain `Manipulation` or `Survival`. |
| 6 | **Silent Country.** You learned the shape of land folk fear after dark. Gain `Scouting` or `Lore`. Gain one rumor. |

### Outcast Third Turn: Hard Reputation

| **D6** | **Event** |
|---|---|
| 1 | **Useful Monster.** Folk who hated your face still used your hands. Gain `Manipulation` or `Melee`. |
| 2 | **Bandit Camp.** You drifted among worse company and learned from it. Gain `Stealth` or `Scouting`. |
| 3 | **Settlement Edge.** You survived by moving just close enough to the walls. Gain `Insight` or `Move`. |
| 4 | **Night Deal.** Something traded in whispers became your business for a season. Gain `Manipulation` or `Sleight of Hand`. |
| 5 | **Ambush Or Escape.** You learned when to strike and when to vanish. Gain `Melee` or `Stealth`. |
| 6 | **Cold Wisdom.** Hard years taught you to read men faster than weather. Gain `Insight` or `Survival`. |

### Outcast Fourth Turn: Return, Revenge, Or Vanishing

| **D6** | **Event** |
|---|---|
| 1 | **No Way Back.** The door truly shut behind you. Gain `Survival` or `Endurance`. You must change path next cycle or remain Outcast under narrowing tax. |
| 2 | **Taken In By The Damned.** A gang, hidden camp, or harsh patron gave you belonging of a sort. Gain `Manipulation` or `Stealth`. |
| 3 | **Revenge Taken.** You hurt one of those who cast you out. Gain `Melee` or `Insight`. Gain one enemy and one grim satisfaction. |
| 4 | **Return In Secret.** You stepped back into old ground under another name or by moonlight. Gain `Move` or `Manipulation`. |
| 5 | **Worse Than Alone.** Someone beside you proved more dangerous than solitude. Gain `Insight` or `Scouting`. |
| 6 | **Endured Anyway.** Survival itself became a kind of strength. Gain `Endurance` or `Insight`. You may take one Outcast advancement benefit even if the later roll fails. |

### Outcast Mishaps

| **D6** | **Mishap** |
|---|---|
| 1 | Beaten, branded, or stoned out of a place. Gain one scar. |
| 2 | Betrayed by one of the few you trusted. Gain one rival. |
| 3 | Starved, froze, or nearly drowned before crawling back. Gain one fear or chronic pain. |
| 4 | Branded a thief, plague-bearer, or witch. Lower Standing by 1 in one settlement. |
| 5 | You hurt someone who did not deserve it. Gain one dark secret. |
| 6 | The road outside society has changed you too much. Your next cycle must change path or gain one extra Wear before it begins. |

### Outcast Advancement Benefits

| **D6** | **Benefit** |
|---|---|
| 1 | Rank 1 in `Fearless` |
| 2 | Rank 1 in `Sixth Sense` |
| 3 | Rank 1 in `Lucky` |
| 4 | One hidden-camp, outlaw, or edge-of-settlement contact |
| 5 | Hidden camp gear, knife, blanket, and practical survival kit |
| 6 | One rumor about a forgotten path, outlaw hoard, or place decent folk avoid |

### Outcast Mustering-Out

| **D6** | **Result** |
|---|---|
| 1 | Knife, blanket, patched gear, and camp kit |
| 2 | One hidden contact and one settlement that wants you gone |
| 3 | `D6` silver in stolen or buried form |
| 4 | One scar and one story that cannot be told in every firelight |
| 5 | One hidden shelter, outlaw trail, or buried cache |
| 6 | One rumor about a ruin, outlaw band, or enemy worth hunting |

## Current Assessment

The replacement has the right shape now.
It gives Chapter 2 a harder, richer way to build a character without breaking the chapter's skill, talent, and age math.

It is still proposal work, but it now stands as a full replacement draft rather than a loose design brief.
What remains after this point is optional expansion and eventual manuscript integration, not missing core structure.

## Chapter 2 Calibration Audit

This system does not get to define its own power band.
Chapter 2 already has one.
The life generator must land inside it.

### Attribute Audit

The life generator does not hand out attribute points.
Age still does that work alone.

| Age | Chapter 2 Attribute Points | Life-Path Rule |
|---|---|---|
| Young | 15 | unchanged |
| Adult | 14 | unchanged |
| Old | 13 | unchanged |

This means the life-path system may shape scars, burdens, standing, gear, and skill spread, but it must not add hidden attribute inflation through events, advancement, or mustering-out.

### Skill Audit

The skill totals match Chapter 2 exactly.

| Age | Childhood Foundation | Turn Skill Points | Total |
|---|---|---|---|
| Young | 2 | 6 | 8 |
| Adult | 2 | 10 | 12 |
| Old | 2 | 14 | 16 |

That is the whole allowance.
No event, mishap, advancement result, or mustering-out roll may grant extra skill points outside this structure.

### Talent Audit

Chapter 2 already grants:

- one kin talent
- one profession talent
- age-based general talents at `1 / 3 / 5`

The life-path system may bend those starts, but not multiply them.

Use these limits:

- a life path may raise the chosen profession talent to Rank 2
- no character may begin with more than one talent above Rank 1
- life-path advancement should prefer contacts, local standing, practical gear, mounts, rumors, or narrow general talents over direct combat growth
- `Peddler` still keeps `_Educated_` as a profession feature, not a life-path reward

### Profession Access Audit

Every profession must be reachable by a clean line, and every fallback life must still leave a way back.

| Profession | Clean Route | Recovery Route |
|---|---|---|
| Druid | Childhood toward Druid, then one Druid cycle | Druid -> Outcast or Drifter -> Druid or Hunter |
| Fighter | Childhood toward Fighter, then one Fighter cycle | Fighter -> Laborer or Drifter -> Fighter or Rider |
| Hunter | Childhood toward Hunter, then one Hunter cycle | Hunter -> Drifter or Outcast -> Hunter or Rogue |
| Minstrel | Childhood toward Minstrel, then one Minstrel cycle | Minstrel -> Drifter -> Minstrel or Peddler |
| Peddler | Childhood toward Peddler, then one Peddler cycle | Peddler -> Laborer or Drifter -> Peddler or Rogue |
| Rider | Childhood toward Rider, then one Rider cycle | Rider -> Laborer or Drifter -> Rider or Fighter |
| Rogue | Childhood toward Rogue, then one Rogue cycle | Rogue -> Outcast or Drifter -> Rogue or Fighter |
| Sorcerer | Childhood toward Sorcerer, then one Sorcerer cycle | Sorcerer -> Outcast or Drifter -> Sorcerer or Druid |

This preserves profession identity while allowing broken lives to bend without snapping the build.

### Gear And Silver Audit

Chapter 2 profession starts are modest.
The life-path version must stay that way.

| Profession Baseline In Chapter 2 | Life-Path Ceiling |
|---|---|
| Druid or Sorcerer: staff or knife, one trade good, `D6-D8` silver | one practical occult or sacred package, no extra armor, silver usually `D6` or `D8` |
| Fighter: one-handed weapon, studded leather, one trade good, `D6` silver | may start with one armor package or one strong weapon package, not both plus extra premium gear |
| Hunter: bow or sling, two trade goods, `D6` silver | may start with bow, traps, hides, or guide gear, but not military armor |
| Minstrel: instrument, knife, one trade good, `D8` silver | may start with instrument, clothes, writing tools, one patron favor, but not rich court excess |
| Peddler: knife, three trade goods, strong silver start | may start with scales, cart, pack beast, or market kit, but silver must stay tied to debt or risk |
| Rider: riding horse, spear or handaxe, short bow or sling, one trade good, `D6` silver | mount access belongs here first; no other path should casually outdo it |
| Rogue: dagger, two trade goods, `D10` silver | hidden stash and light criminal tools are fine, but not a full burglary arsenal plus large silver |

Use these hard caps:

- only one major gear package from life-path advancement or mustering-out
- only `Rider` should begin with a reliable riding mount by default
- armor above studded leather should be rare and usually come with debt, wear, or history
- silver spikes above `D8` should be uncommon and usually paired with debt, pursuit, or disputed ownership
- rumors about wealth are better than wealth itself

### Contact And Scar Audit

The system should create denser histories, but not drown the sheet.

At the end of character creation, a normal result should usually leave the character with:

- one to three contacts
- one to three rumors
- one to two rivals or enemies
- one to three visible scars, debts, burdens, or fears

Old characters may sit at the high end of that spread.
If the average build starts above it, the system is overloading the sheet before play begins.

### Balance Note

The life generator is allowed to improve texture, memory, pressure, and social weight.
It is not allowed to improve raw starting efficiency by much.

It may make a character feel older, stranger, more burdened, and more rooted.
It may not quietly turn every start into better armor, cleaner talents, easier silver, and broader skill reach than the standard Chapter 2 build.

## Integration Draft For Chapter 2

What follows is the replacement package in Chapter 2 form.
It is still proposal text, but it is written to be moved into the manuscript with light revision rather than rebuilt from notes.

### Transition From Alternative Method

Replace the current `ALTERNATIVE METHOD` paragraph with this:

If you want a heavier way to build your adventurer, use the life generator later in this chapter. It replaces the quick method with a longer road through childhood, hard turns, setbacks, and second lives. You will begin play with more scars, more hooks, and a past that feels earned.

### Replacement Heading Ladder

Use this heading ladder in Chapter 2:

- `## LIFE GENERATOR`
- `### USE THIS METHOD`
- `### REFERENCE GUIDE FOR ROLLING UP AN ADVENTURER`
- `### BACKSTORIES`
- `### KIN AND HOME`
- `### CHILDHOOD FOUNDATION`
- `### CHOOSE AGE`
- `### RESOLVE LIFE CYCLES`
- `#### FIRST TURN`
- `#### SECOND TURN`
- `#### THIRD TURN`
- `#### FOURTH TURN`
- `### MUSTER OUT`
- `### CHOOSE PROFESSION`
- `### HOW DID YOU MEET?`

### Manuscript Draft

## LIFE GENERATOR

This section lets you build an adventurer through childhood, hardship, work, ruin, and the long turns that came before the game begins.

Use this method if you want more history from the start.
It is slower than the quick method in this chapter, but it leaves you with stronger scars, ties, and burdens.

These rules replace the normal skill-allocation method.
They do not replace the rest of Chapter 2 unless the text below says so.

### USE THIS METHOD

Use the life generator if you want any of the following:

- a character who feels worn into shape rather than assembled
- a stronger sense of age and second careers
- more contacts, rivals, rumors, and old debts before play begins
- a harsher, more random path into your profession

Do not use it if your group wants the fastest possible start.
The normal method remains the cleaner choice when speed matters more than history.

### REFERENCE GUIDE FOR ROLLING UP AN ADVENTURER

1. Choose or roll your kin.
2. Roll or choose your home region.
3. Roll or choose a childhood foundation for your kin. Record the first 2 skill points and the hook from that result.
4. Choose Young, Adult, or Old. This determines how many completed cycles you resolve.
5. For each completed cycle, choose or roll a life path.
6. In your first cycle, childhood already counts as the First Turn and Second Turn. Resolve the rest of that cycle, then resolve every later cycle in full. Each resolved turn gives 1 skill point and one event or mishap.
7. At the end of each cycle, roll advancement or departure. You may remain in the same path, leave it, or be forced out of it.
8. After the last cycle, roll on the mustering-out table for your final path.
9. Choose your profession using the qualification rules in this section.
10. Spend attribute points by age as normal.
11. Choose kin talent, profession talent, and general talents by age as normal.
12. Determine Pride, Dark Secret, relationships, silver, and Resource Dice as described below.
13. Roll or choose on the `How Did You Meet?` table.

### BACKSTORIES

The tables in this section build an adventurer who already carries the marks of a life.
They replace the ordinary distribution of skill points in Chapter 2.

Age still governs attributes and general talents.
Kin still governs kin talent.
Profession still governs profession talent, Pride suggestions, Dark Secret suggestions, relationships, Resource Dice, and the rest of your place in the chapter.

What changes here is the road into that life.

### KIN AND HOME

Choose your kin as normal, or roll if your group wants the dice to rule the whole process.
Then roll or choose your home region.

Your home still matters.
It tells the GM what roads, ferries, shrines, halls, camps, and nearby settlements might know your name when play begins.

### CHILDHOOD FOUNDATION

Roll or choose one childhood foundation for your kin.
That result gives you:

- favored attributes
- the first 2 skill points of your age total
- one hook such as a contact, scar, rumor, burden, or local tie
- one suggested first path

Childhood points you toward a life.
It does not finish one.
It also counts as the First Turn and Second Turn of your first cycle.

### CHOOSE AGE

Choose Young, Adult, or Old as normal.
This determines:

- your attribute points
- your general talents
- how many completed cycles you resolve

Use this table:

| Age | Completed Cycles |
|---|---:|
| Young | 2 |
| Adult | 3 |
| Old | 4 |

Elves do not begin as Young.
They begin at Adult or Old.

### RESOLVE LIFE CYCLES

For each completed cycle, choose or roll a life path.
Then resolve the four turns of that cycle in order.

In the first cycle, childhood has already filled the First Turn and Second Turn.
Begin that cycle at the Third Turn.
Every later cycle is resolved in full.

If you repeat the same path after already completing one cycle in it, the path narrows:

- the turn test is made at `-1`
- failed turn tests roll mishaps with `+1`
- the same direct talent benefit cannot be gained twice from that path

#### FIRST TURN

The first turn is entry.
It is where duty, apprenticeship, first blood, rough work, first patrons, and hard beginnings take hold.

#### SECOND TURN

The second turn is pressure.
It is where hunger, weather, debt, fear, and obligation begin to lean on the life.

#### THIRD TURN

The third turn is rise.
It is where a name may spread, where secrets deepen, and where the life begins to feel like it might hold.

#### FOURTH TURN

The fourth turn is reckoning.
It is where betrayal, battle, scandal, inheritance, exile, oath, or ruin break the old shape and force the next one.

For each turn, resolve the path's turn test first.

| Result | Outcome |
|---|---|
| Failure | Gain 1 skill point from the path's hard-lesson list, then roll a mishap |
| Success | Gain 1 skill point from the path's normal list, then roll the turn event |
| 2+ successes | As success, and gain 1 edge on the event roll or 1 extra silver die if the event grants money |

Every failed turn test also adds one `Wear`.

At the end of character creation:

- `0-1 Wear`: no extra effect
- `2-3 Wear`: choose one scar, rival, debt, or lingering fear
- `4+ Wear`: choose one of those, then also begin play with either a chronic pain, a feud, or lowered Standing in one settlement

After the fourth turn, roll advancement or departure for that path.

| Result | Outcome |
|---|---|
| Failure | You leave that path |
| Success | You may remain in the same path next cycle and gain one path benefit |
| 2+ successes | As success, and gain one extra contact, rumor, or path-specific gear benefit |

If the fiction or the tables drive you out of a life, move into a new one that fits the fall.
Drifter, Laborer, and Outcast exist for that reason.

### MUSTER OUT

After the last cycle, roll on the mustering-out table for your final path.
This gives you the practical remains of the life you just left behind:

- gear
- silver
- a contact
- a rival
- a rumor
- a scar, stain, or burden that still matters

### CHOOSE PROFESSION

The life path does not replace the chapter's professions.
It leads into them.

Use these rules:

- if your last cycle used a profession path, that path is your default profession
- if your last cycle used a fallback path, choose between the profession paths from your two previous cycles
- if you completed only one profession path across your whole history, you must use that profession
- if no profession path was ever completed, choose the profession tied to the skill family in which you hold the most ranks

Once your profession is set, continue with the profession rules already in this chapter:

- choose your profession talent
- choose your general talents by age
- record Pride, Dark Secret, and relationships from your profession entry
- take Resource Dice from your profession entry as normal
- use the gear and silver from the life generator instead of adding the profession's ordinary starting gear and silver on top

Languages and Willpower remain unchanged from the rest of Chapter 2.

### HOW DID YOU MEET?

Use the `How Did You Meet?` table after every character has finished the life generator.
The table still does the same job as before: it explains how the adventuring company came together.

The stronger backstories make that table better, not weaker.
A prison escape, shared debt, storm shelter, or bloody battle carries more weight when every adventurer already comes in with old roads behind them.

### Removal And Conversion Map

If this draft is promoted into the manuscript, replace the current life-generator material as follows:

| Current Material | Keep, Remove, Or Transform | Notes |
|---|---|---|
| `REFERENCE GUIDE FOR ROLLING UP AN ADVENTURER` | Replace | use the new cycle-based guide |
| `BACKSTORIES` opening text | Replace | use the new method description |
| `Kin` table | Keep in transformed form | still useful as an optional all-random entrypoint |
| `Home Region` tables | Keep | still fit cleanly |
| old `Childhood` tables | Remove and replace | use childhood foundations instead |
| `Profession` table | Remove from life generator | profession now comes from qualification at the end |
| `Profession Talent` table | Remove from life generator | profession talent is chosen after profession qualification |
| old `Formative Events` tables | Remove and mine | their best material feeds life paths, mishaps, and mustering-out |
| `How Did You Meet?` | Keep | retain with only bridge text above it |

### Integration Decisions

These are the current answers to the open integration questions:

- `How Did You Meet?` stays as its own table
- it only needs a short bridge, not a full rewrite
- the old simple generator should be removed rather than kept as a sidebar
- the normal quick-build method already serves the role of the lighter option
- childhood should count as the first two turns of the first cycle
- profession Resource Dice stay, but profession starting gear and silver do not stack on top of life-path gear and silver

## Migration Note

The old generator gives you one childhood, one profession, and one to three formative events.
The new one gives you childhood, then a chain of turns across several cycles.

The biggest changes are these:

- profession is chosen at the end of the life rather than near the beginning
- formative events are replaced by full path suites with mishaps, advancement, and mustering-out
- age still governs attributes and general talents, but now also determines how much life is resolved
- childhood no longer finishes the build; it covers the first two turns of the first cycle
- `How Did You Meet?` stays, but now lands on stronger personal histories

This makes character creation slower.
It also makes the result harder, stranger, and better rooted in the world.

## Integration Checklist

When this moves into `corebook/02-your-adventurer.md`, check all of the following:

- heading levels match the rest of Chapter 2
- `ALTERNATIVE METHOD` points to the new section cleanly
- age, talents, languages, Willpower, gear, Pride, Dark Secret, and relationships still line up with the rest of the chapter
- life-path gear does not silently overwrite profession starting gear where the text does not intend it
- `How Did You Meet?` sits after the life generator with its bridge text intact
- no proposal-rationale language remains in the chapter copy

## Next Work

- Revisit all eleven path suites for voice and density consistency
- Add more worked examples that show prison, exile, debt, and patron collapse driving path change at the table
- Write one settlement-standing and contact appendix
- Compare all mustering-out tables against profession starting gear in Chapter 2
- Playtest for skill spread, talent bloom, and gear inflation
