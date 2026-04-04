<!-- markdownlint-disable MD013 -->

# Proposal: Reputation System Overhaul

## Purpose

The current Reputation rules use a single score for each adventurer.
That is simple, but it also assumes that people in distant villages, market roads, and border keeps all hear the same stories at roughly the same speed.
That does not fit the harsh, scattered, suspicious world this manuscript otherwise presents.

This proposal replaces the single universal score with a layered, local system.
The key correction is this:

- **Reputation** remains a rolled score measured in dice
- **Standing** is tracked separately as trust, goodwill, resentment, fear, or hatred

That split fits the core rules much better.
In the current manuscript, Reputation is not simply attitude. It is a score you roll.
It needs room to climb like a meaningful dice pool, and it should still be possible to get one, two, or three ⚔️ when your name truly carries weight.

The goal is to make reputation local, uneven, and believable without losing its function as a real mechanical resource.
A fellowship should be able to be famous in one valley, trusted in one village, feared on one road, known to caravan folk across a trade route, and still be complete nobodies in the next marsh over.

## Main Problem

The current rules create five mismatches.

### 1. Everyone knows too much

A single Reputation score implies that a deed known in one corner of the land can just as easily be known in another.
That makes the Forbidden Lands feel smaller and less fractured than the rest of the game suggests.

### 2. Reputation and attitude are blurred together

The core rules already say Reputation tells how well known you are, not whether you are feared or admired.
That distinction is correct.
But with only one universal score, the game has little room to track local goodwill separately from local fame.

### 3. The current score is too flat for local play

The existing rule works for broad adventurer fame, but it does not support these common situations well:

- the group is known in one village and unknown in the next
- their names open doors with caravan folk but not with peasants
- their keep is talked about nearby even when the owners' faces are not
- a village chief trusts them while a neighboring elder hates them

### 4. Strongholds already point toward a better model

Chapter 9 already gives strongholds their own Reputation score.
That is useful.
The weak point is that stronghold fame is then folded back into player Reputation as if every tale about a keep instantly becomes universal personal fame.

### 5. The old model wastes the roll

A reputation score should be worth rolling.
If it stays small and abstract, it rarely produces the satisfying spread of outcomes that other dice pools do.
A real Reputation system should sometimes yield:

- no recognition at all
- a single useful success
- several successes that secure real benefits

That means the scale must look more like a real dice pool and less like a tiny modifier track.

## Design Goals

Any replacement should do six things.

1. Keep local memory stronger than distant rumor.
2. Preserve Reputation as a rolled dice-pool score.
3. Separate being known from being liked.
4. Let strongholds matter without turning them into universal celebrity engines.
5. Let trade circles carry news differently from peasant villages.
6. Keep table procedure practical.

## New Structure: Reputation And Standing

This proposal replaces universal player Reputation with local scores in four layers.

For each place, stronghold, or trade circle that matters, track two things when needed:

- **Reputation**: how well known you are there or among them
- **Standing**: what they think of you there

### Reputation

Reputation is always a non-negative score.
It is rolled as D6, just like the core rules already do.

A local Reputation score should usually range from `0` to `10`, though legendary cases can go higher.
That is close enough to other meaningful dice pools in the game to make rolling it feel worthwhile.

Suggested reading of the scale:

| Reputation | Meaning |
| --- | --- |
| `0` | Unknown |
| `1-2` | A few have heard the name |
| `3-4` | Known by rumor in the local area or circle |
| `5-6` | Plainly established reputation |
| `7-8` | Strong local or regional renown |
| `9-10` | Very hard to ignore in that sphere |
| `11+` | Legendary within that sphere |

### Standing

Standing is separate.
It measures trust, goodwill, resentment, fear, or local hatred.
Standing is not rolled by itself.
It modifies what successful reputation means and can affect _MANIPULATION_, prices, favors, recruitment, and similar social outcomes.

Suggested Standing scale:

| Standing | Meaning |
| --- | --- |
| `-3` | Hated, hunted, or outlawed |
| `-2` | Bitterly distrusted or openly hostile |
| `-1` | Cold, wary, suspicious |
| `0` | No special feeling |
| `+1` | Known as useful or decent |
| `+2` | Trusted friends or proven allies |
| `+3` | Honored protectors, patrons, or champions |

This split solves the core problem cleanly.
You can be:

- high Reputation and low Standing
- low Reputation and high Standing
- high in both
- low in both

That is exactly what the world needs.

## The Four Local Layers

### 1. Settlement Reputation

Each village, town, temple-hold, mine camp, ferry, or similar community can have its own Reputation score for the fellowship or for a single adventurer.
In most cases, the GM should track it for the group, not each PC separately, unless one character has clearly become distinct there.

This is the score rolled when the group arrives, asks for favors, leans on its local name, or tries to see how much of its story has already taken root.

#### What raises Settlement Reputation

Examples:

- slaying a monster that preyed on the settlement
- defending it against raiders, undead, beasts, or fire
- recovering stolen kin, goods, or livestock
- winning a public dispute in a memorable way
- spending real time in the settlement and becoming part of its life
- visibly funding repairs, defenses, or relief in a way people will keep talking about

As a rule of thumb, small deeds raise local Reputation by `+1`, major deeds by `+2`, and rare defining deeds by `+3` or more.

### 2. Settlement Standing

Track Standing only for settlements that matter.
This shows whether the locals trust, resent, fear, or honor the fellowship.

#### What raises Settlement Standing

Examples:

- good standing with the mayor, chief, elder, priest, or other local authority
- favors done for the village
- defending it from danger
- paying fair silver over time
- doing good business that actually strengthens the place
- investing enough wealth, labor, supplies, or protection to improve life there

#### What lowers Settlement Standing

Examples:

- theft, extortion, or unpaid debts
- humiliating respected locals
- cheating in trade
- bringing trouble and leaving others to bleed for it
- siding with a hated faction in a local feud
- violating hospitality, sanctuary, or local custom

Money should not buy love too easily.
A settlement may respect your silver before it trusts your face.
In most cases, even large local investment should raise Standing only by `+1` unless joined to a deed that people already care about.

### 3. Stronghold Reputation

Each stronghold keeps its own Reputation score, as Chapter 9 already does.
That part is sound and should remain.

What changes is how it spreads.
Stronghold Reputation should no longer convert directly into universal player Reputation.
Instead, it should radiate outward by distance and travel routes.

A keep is known first by:

- nearby villages
- nearby roads
- hirelings and rivals
- ferrymen and caravan folk
- raiders, envoys, and power-brokers

Its banner, walls, and tales often travel farther than the faces of the people who own it.

### 4. Trade Reputation

Track separate Reputation scores for the trades that actually matter in the campaign.
Do not track every possible craft.
Track only the ones the fellowship has truly touched.

Examples:

- peddlers and caravan folk
- smiths
- masons and builders
- hunters and trappers
- ferrymen, sailors, and river traders
- priests and shrine-keepers
- mercenaries

Trade Reputation spreads through work, contracts, stories, caravans, letters, shared contacts, and repeated dealings.
It should often travel farther than village Reputation, but only within that trade circle.

Track Trade Standing separately when it matters.
A group can be very well known among merchants and still be known as cheats.

## Rumor Spread Through Hexes

When a deed becomes widely talked about, it creates a **Rumor Source**.
The source begins in a settlement, stronghold, road station, caravan, shrine, market, fair, or adventure site tied to the event.

Each Rumor Source has:

- **Strength**: how powerful the story is
- **Tone**: admired, feared, cursed, disputed, blessed, etc.
- **Origin**: where the story began
- **Sphere**: settlement, stronghold, trade, or broader regional rumor

Suggested Rumor Source strength:

| Strength | Effect |
| --- | --- |
| `1` | Minor talk, local memory, road gossip |
| `2` | Strong local tale, likely to spread through nearby hexes |
| `3` | Major deed, hard to suppress |
| `4+` | Rare, region-shaping event |

At the end of each week, or whenever the GM advances campaign time meaningfully, a Rumor Source can spread.

Suggested spread rate:

- `1` hex through wilderness
- `2` hexes along a road or river
- `3` hexes if carried by active caravans, ferries, troop movement, or other regular traffic

When a rumor reaches a new settlement or trade circle, it usually does one of these:

- adds `+1` Reputation there
- adds more if the deed was enormous or repeated
- shifts Standing if the tone strongly favors or damns the fellowship

This is the key mechanical change.
Rumors do not just create a vague boolean state.
They build actual local Reputation scores that can later be rolled.

## Core Procedures

### Being Recognized In A Settlement

Replace the current universal recognition roll with this order.

### Step 1: Use local Settlement Reputation

When the fellowship enters a settlement, roll a number of D6 equal to its local Settlement Reputation there.
If one or more ⚔️ are rolled, someone has heard of them.
More ⚔️ means deeper or broader recognition.

Suggested reading:

- `1` ⚔️: a few people know the name or deed
- `2` ⚔️: the group is known by the right people or by much of the settlement
- `3+` ⚔️: the group's name carries real weight here

Standing then determines whether that recognition is warm, wary, fearful, or bitter.

If local Settlement Reputation is `0`, move to the next step.

### Step 2: Check nearby Stronghold Reputation

If the fellowship owns or rules a nearby stronghold, use that stronghold's Reputation with distance penalties.

Suggested distance bands from the stronghold:

| Distance | Effective Stronghold Reputation |
| --- | --- |
| Same hex | full score |
| `1-2` hexes | `-1` |
| `3-5` hexes | `-2` |
| `6-10` hexes | `-3` |
| beyond `10` | usually no effect unless strong routes or major rumor sources apply |

If a road, river, or caravan route directly links the stronghold and the settlement, the GM may ignore `1` point of distance penalty.

Roll the effective score as D6.
Success means people know the keep, its banner, or the people tied to it.
If this recognition keeps repeating in the same settlement, start converting it into permanent local Settlement Reputation instead of rolling the stronghold every time.

### Step 3: Check Trade Reputation

If the place includes a relevant trade circle, roll the fellowship's Trade Reputation in that trade.
This does not mean the whole village knows them.
It means the people of that trade might.

If those traders then speak of them locally over time, some of that recognition can become local Settlement Reputation.

### Step 4: Check current Rumor Sources

If an active Rumor Source has reached the hex, the GM can either:

- roll its current effective strength directly as D6, or
- simply treat it as already having granted local Reputation there

Use whichever method is cleaner in play.
The second method is usually better once a rumor has plainly settled into local memory.

## Leaning On Your Name

A Reputation score should do more than answer "have they heard of me?"
It should sometimes win concrete benefits.

This proposal therefore adds a simple procedure:

When you are dealing with a place or circle where you have local Reputation, you may **lean on your name**.
Roll the relevant Reputation score.
The GM interprets ⚔️ according to context.

Suggested benefit ladder:

| ⚔️ | Typical benefit |
| --- | --- |
| `1` | Fair hearing, access, basic hospitality, reduced suspicion |
| `2` | Minor favor, quick introduction, small credit, modest price break, useful rumor |
| `3` | Significant favor, audience with authority, meaningful local help, strong deference |
| `4+` | Exceptional response, public backing, rare privilege, or a major practical concession |

Standing modifies the outcome.
If Standing is bad, high Reputation may mean fear, resentment, or hostile attention instead of goodwill.

This is the main reason the scale must remain large enough to roll like a real pool.
A score that never grows beyond two or three dice leaves too much on the table.

## Example Tables For Social Results

These tables are not meant to replace the GM's judgment.
They are meant to show what the system should usually produce in play.

### Example Table: How People Treat You

Use this when the group is already known locally and the GM wants a quick answer for everyday treatment.
Read the result through local Standing.

| Local Reputation | If Standing is `-1` to `-3` | If Standing is `0` | If Standing is `+1` to `+3` |
| --- | --- | --- | --- |
| `0-1` | strangers are wary, rude, or watchful | strangers treat you as ordinary travelers | strangers treat you politely if introduced well |
| `2-3` | people whisper, close shutters, or send for authority | some have heard your name, but little changes | useful folk know who you are and hear you out |
| `4-5` | the settlement remembers you, and trouble follows your steps | your name opens basic doors and buys patience | you are greeted by name and offered ordinary local help |
| `6-7` | folk avoid offending you, but not from love | you carry visible local weight | headmen, innkeepers, and merchants treat you as proven people |
| `8-9` | fear, resentment, or factional hostility can gather around you quickly | your arrival becomes news | you are treated as protectors, patrons, or local celebrities |
| `10+` | you may provoke panic, sabotage, denunciation, or mob pressure | almost everyone knows the name | the settlement bends custom for you unless doing so would be dangerous |

### Example Table: Lodging And Hospitality

This table assumes a settlement that has an inn, hall, temple guest-space, or local authority able to host strangers. Base prices come from the current services list in Chapter 10.

| Reputation roll result | Typical lodging expectation |
| --- | --- |
| no ⚔️ | you pay full price, if there is room at all |
| `1` ⚔️ | you are allowed into the tavern or inn without extra suspicion; normal prices apply |
| `2` ⚔️ | you may get the better table, a safer corner, credit until morning, or a reduced inn price by about one step |
| `3` ⚔️ | an innkeeper may waive the dormitory fee, cut the price of a separate room, or send food and ale to your table |
| `4+` ⚔️ | the chief, mayor, priest, guild elder, or wealthy host may offer a free stay under their roof, especially if Standing is positive |

Suggested interpretation against current listed services:

| Local mood | Dormitory (base `2` copper) | Separate room (base `5` copper) | Fine dwelling (base `2` silver) |
| --- | --- | --- | --- |
| hostile or fearful | refused, overcharged, or watched | rarely offered | not offered |
| neutral | full price | full price | full price if available |
| favorable and `2` ⚔️ | often free or half price | reduced by `1-2` copper | offered only by invitation |
| favorable and `3+` ⚔️ | free | often free or token price | reduced or granted by a patron |

### Example Table: Craftsmen, Traders, And Prices

This table should apply only where the group has either local Settlement Reputation with positive Standing or actual Trade Reputation in the relevant circle.
It should not erase scarcity, missing supply, or the need for the right talent.

| Reputation roll result | Typical market effect |
| --- | --- |
| no ⚔️ | no special treatment |
| `1` ⚔️ | fair weights, honest hearing, no attempt to cheat you openly |
| `2` ⚔️ | small courtesy: modest queue priority, small extra scrap, quicker turnaround, or a light discount |
| `3` ⚔️ | noticeable favor: better payment terms, first pick when stock is thin, reduced price, or access to the better craftsman |
| `4+` ⚔️ | exceptional favor: celebrity treatment, deep courtesy, a master craftsman taking personal interest, or being trusted with scarce goods ahead of others |

Suggested price guidance when local Standing is favorable:

| Result | Ordinary innkeeper or trader | Craftsman or specialist |
| --- | --- | --- |
| `1` ⚔️ | normal price, but no gouging | normal price |
| `2` ⚔️ | around `10-20%` off, or a small extra thrown in | around `10%` off, or faster work |
| `3` ⚔️ | around `20-40%` off on common services or goods | around `20%` off, or better queue position, or partial credit |
| `4+` ⚔️ | major courtesy on ordinary goods and lodging | a real favor rather than a simple discount |

These reductions should never bypass:

- supply restrictions
- narrative scarcity
- the need for a specialist
- the Peddler's own haggling niche

If both Reputation and a talent-based discount apply, use the better one as the main reduction and let the other add a softer edge such as faster service, better quality, credit, or goodwill.

## Manipulation

The current social rule should stay in place, but it should use the most relevant local score.

When making a _MANIPULATION_ roll, compare whichever combination matters most in the moment:

- local Standing, if this is chiefly about trust or resentment
- local Reputation, if status and public name matter more
- both, if the GM wants the full social weight of fame plus local goodwill

The cleanest default is this:

- use Standing as the modifier to the social contest
- use Reputation to determine whether the target knows who you are and whether your name can be leaned on for extra benefits

That preserves the existing logic while giving the system more texture.

## Growth And Loss

The current "gain one Reputation after a great deed" rule should be split.
A great deed no longer grants universal fame by default.
Instead, it should do one or more of these:

- raise Settlement Reputation where the deed happened
- raise Settlement Standing there if the deed truly helped or harmed the locals
- create or strengthen a Rumor Source
- raise Stronghold Reputation if the deed strengthened, defended, enriched, or elevated the keep
- raise Trade Reputation in the trade circles that care about it
- raise or lower Trade Standing depending on how the deed is judged

This keeps growth concrete.
The group becomes known where the world has actually had time to hear of them.

## Balance Analysis And Talent Synergies

This section evaluates the proposal through mathematical, perceived, table, and campaign balance.

## What The Rule Rewards

The revised system rewards:

- repeated involvement in the same settlements
- building trust through deeds instead of abstract global fame
- trade-route play and caravan play
- stronghold play with real local consequence
- social specialists who return to the same places and cultivate circles of influence

That is a good fit for the game's travel, stronghold, and sandbox logic.

## What Players Will Probably Believe It Rewards

Players will likely read the system as saying:

- "If we invest in a place, that place will matter."
- "If we make a name for ourselves, we can actually cash it in."
- "A social character can build a real network instead of relying on one global number."

That reading is mostly correct.
That is good.
The danger begins only if local Reputation becomes too easy to farm or if discounts stack too hard with existing talents.

## Table And Campaign Strengths

### 1. It gives social play a geography

This is the strongest gain.
Reputation now follows roads, rivers, villages, keeps, and trade circles.
That makes the map matter more.

### 2. It gives downtime a clearer reward

If the group lingers, helps, spends silver wisely, or protects commerce, it can grow actual local leverage.
That supports a slower, rooted campaign without forcing every party down that path.

### 3. It supports strongholds without absurd fame inflation

Nearby hexes may know your keep even when they do not know your faces.
That is both believable and useful.

## Main Balance Risks

### 1. Discount stacking with the Peddler's Talents

This is the sharpest economic risk.

The Peddler's `PATH OF TREASURE` already grants strong price manipulation:

- Rank `1` can reduce buying prices dramatically by spending WP
- Rank `2` increases sale value
- Rank `3` improves access to uncommon and rare goods

If local Reputation also grants large percentage discounts, the Peddler can become too dominant in any settlement where they are established.

#### Recommended correction for trade discounts

Do not let Reputation discounts stack additively with Peddler percentage discounts.
Use this priority instead:

- apply the stronger single price reduction
- let the weaker source grant a side benefit instead

Side benefits can be:

- quicker access
- first choice of stock
- partial credit
- waived insult premiums
- a small extra item or service

This preserves the Peddler's niche while still letting reputation matter.

### 2. Minstrel feedback loops in settlements

The Minstrel's `PATH OF INFLUENCE` and `PATH OF THE SONG` already interact strongly with crowds, rumor, and mood.
Under this proposal, that synergy becomes even stronger.

Most important are:

- `PATH OF INFLUENCE` Rank `3`, which already spreads gossip through the settlement
- `PATH OF INFLUENCE` Rank `4`, which explicitly spends one point of local Reputation
- `PATH OF THE SONG` Rank `2`, which can lower hostility or plant rumor

This is thematically excellent, but it risks a self-feeding engine where one successful performer can farm rapid local Reputation growth.

#### Recommended correction for minstrel crowd play

Do not let a single PERFORMANCE or crowd scene grant more than `+1` local Reputation by itself unless tied to an already significant public deed.
Performance can spread, shape, or revive reputation, but should not usually create heroic fame from nothing.

### 3. Rogue and deception synergies

The Rogue's `PATH OF THE FACE` and some `DIRTY FIGHTING` or `PATH OF THE FENCER` social tricks can benefit from a system where recognition matters.

This is mostly healthy.
The main edge case is impersonation.
If local Reputation is meaningful, impersonating someone famous becomes more potent.

#### Recommended correction for impersonation

Treat high local Reputation as raising the stakes of disguise rather than making it easier.
Impersonating a known person should usually grant stronger results on success, but also attract closer scrutiny.

### 4. Economic bypass through celebrity treatment

Free rooms, favored craftsmen, and lowered prices feel right.
But if these become automatic at modest Reputation levels, coin pressure softens too much.

The game's economy still wants:

- inns to cost money
- craftsmen to charge for scarce labor
- comfort to remain a meaningful choice

#### Recommended correction

Make the best hospitality outcomes contingent on three things together:

- at least moderate local Reputation
- favorable Standing
- a place that can actually afford the favor

A starving hamlet should not hand out free separate rooms and cut-rate smith work merely because the heroes are loved.
It may instead offer:

- floor space by the hearth
- plain food
- labor
- rumor
- guides

That keeps the tone harsh and practical.

## Talent Synergy Map

### Strong positive synergies

These combinations are good and should be preserved.

#### Minstrel

- `PATH OF INFLUENCE`
- `PATH OF THE SONG`
- `PATH OF WARCRY` in public, martial, or command contexts

Why it works:

- minstrel play already revolves around crowds, rumor, morale, and public memory
- the new system gives those talents a clearer social terrain

#### Peddler

- `PATH OF TREASURE`
- `PATH OF WORDS`
- `EDUCATED`

Why it works:

- trade reputation, contracts, rumor evaluation, and local bargaining now reinforce each other cleanly

#### Stronghold builders and leaders

- `BUILDER`
- hireling and resident recruitment rules in Chapter 9
- any talent or spell that improves roads, security, supply, or settlement order

Why it works:

- a better keep should create better nearby recognition
- that supports campaign-level play well

#### Performance and quality display

- instruments that add to PERFORMANCE
- fine weapons that grant status on MANIPULATION
- high-quality visible gear, clothes, or heraldic display

Why it works:

- the group can turn fame into visible authority
- this fits the existing gear logic without rewriting it

### Conditional or risky synergies

These should be watched closely.

#### Peddler price cuts + reputation discounts

This is the single biggest numerical risk.
Cap the stacking, as noted above.

#### Minstrel rumor loops

Very flavorful, but easy to overfeed if every crowd scene becomes permanent local Reputation.

#### Stronghold Reputation + player local Reputation

Healthy in principle, but the GM should convert repeated stronghold recognition into local settlement Reputation slowly, not instantly.
Otherwise the old universal-fame problem returns in regional form.

### Anti-synergies and natural brakes

These are good pressure valves already present in the manuscript.

- facial and throat injuries that penalize `MANIPULATION`
- hygiene penalties that damage social presence
- bad Standing despite high Reputation
- scarcity and supply limits in gear acquisition
- kin penalties in unfamiliar settlements

These brakes help keep the system from becoming a pure charisma escalator.

## Mathematical And Procedural Notes

### Dice growth

The proposal's larger local Reputation bands are appropriate because the game already supports rolls where `2-3` ⚔️ matter.
That is visible in the core skill guidance for Challenging and Difficult actions.

This matters because Reputation is no longer just a yes-or-no recognition gate.
It can now support graded outcomes like:

- hospitality
- lodging quality
- access to leaders
- trade favors
- public backing

That means a score of `4-6` is not excessive in an established home settlement.
It is where the rule starts to feel alive.

### GM load

The system does add tracking.
That burden stays acceptable only if the GM tracks local Reputation and Standing for:

- settlements that matter
- trades that matter
- strongholds that matter

Do not track the whole map exhaustively.
Track what the fellowship has actually touched.

## Recommended Guardrails

If this proposal is adopted, these limits are recommended:

1. A single social scene should rarely grant more than `+1` local Reputation by itself.
2. Performance, gossip, and public speech should usually spread or reshape Reputation, not create large amounts from nothing.
3. Reputation-based discounts should not stack directly with the strongest Peddler discounts.
4. The richest benefits should require both good Standing and actual local capacity.
5. Stronghold recognition should become permanent local Reputation gradually.

## Overall Balance Verdict

This proposal is strong in perceived and campaign balance.
It makes the world feel larger, more grounded, and more responsive.

Its main numerical risk is economic stacking through:

- Peddler price talents
- positive Standing
- high local Reputation
- celebrity-tier hospitality

Its main procedural risk is social snowballing through:

- crowd performance
- rumor loops
- rapid conversion of stronghold fame into settlement fame

Both risks are manageable with the guardrails above.

If those guardrails are observed, this overhaul should be healthier than the current universal system because it rewards rooted play, preserves scarcity, and gives social specialists stronger toys without making them globally dominant.

## Why This Works Better

### It respects the core rule

Reputation remains a score you roll, not just an abstract label.
That means it still feels like a real part of the engine.

### It separates fame from trust

Being known is not the same as being welcome.
This model finally lets both things exist at once without confusion.

### It keeps strongholds meaningful without making them absurd

A keep can project power, rumor, and political weight into nearby hexes without magically making its owners famous everywhere.

### It makes trade routes matter

Caravans, ferries, and road traffic become real social arteries.
That gives travel and commerce sharper mechanical meaning.

### It supports richer outcomes

A larger Reputation score means the raw roll can matter.
Sometimes your name gets you through the door.
Sometimes it wins a meal, a guide, a discount, a warning, or a night's shelter.
Sometimes it brings trouble.
That is much closer to how the rest of the game's dice feel.

## Example

The fellowship clears a grave-cairn near Pelgreve and kills the ash-wight that has been taking children from the sheep paths.
Pelgreve gains Settlement Reputation `4` for the fellowship and Settlement Standing `+2`.
That is enough that their names are now plainly known there, and a roll can often yield more than a single ⚔️.

Later the fellowship funds a new palisade gate, pays fair wages, and buys winter grain locally instead of stripping the stores bare.
Pelgreve's Standing rises to `+3`, and its local Reputation climbs to `5`.
Now their name does not just ring a bell. It opens doors.

Months later, they raise Black Barrow Keep three hexes away and build its strength to Stronghold Reputation `6`.
Nearby settlements begin to hear of the keep through drovers, messengers, and road talk.
A village three hexes away might first know the banner before it knows the faces behind it.
After enough contact, that borrowed recognition becomes local Settlement Reputation of its own.

At the same time, the fellowship has Trade Reputation `4` and Trade Standing `+1` among caravan folk after protecting wagons and honoring contracts.
A ferryman in a distant river-town may know them by business even if the farmers there do not.

That produces the right feel:

- Pelgreve knows them well and likes them
- nearby villages know the keep and start to know the people tied to it
- merchants know them by reputation carried through trade
- remote strangers may still know nothing at all

## Integration Points

If adopted, this proposal would mainly affect:

- `corebook/02-your-adventurer.md`
  - replace the current player Reputation section with local Reputation plus Standing guidance
- `corebook/03-skills.md`
  - update _MANIPULATION_ language to reference local Standing and relevant Reputation
- `corebook/09-the-stronghold.md`
  - keep stronghold Reputation, but stop converting it directly into universal player Reputation
- `corebook/08-journeys.md`
  - optionally add a short note on rumor movement through roads, rivers, ferries, caravans, and travel time

## Recommended Direction

Adopt this as a full replacement for universal player Reputation.

If a lighter version is preferred, the minimum worthwhile change is this:

1. replace universal player Reputation with local Settlement Reputation
2. track local Standing separately only where it matters
3. keep Stronghold Reputation separate and let it spread by distance and traffic routes
4. add Trade Reputation for trade-heavy campaigns
5. let rumors create actual local Reputation points instead of abstract awareness

That lighter version would already solve most of the realism problem while preserving the rolled-dice identity of Reputation.

## Draft Rule Language Seed

If this proposal is promoted later, the manuscript-facing terminology should likely be split cleanly:

- `Reputation` for how widely known you are in a specific place or circle
- `Standing` for how that place or circle feels about you
- `Stronghold Reputation` for the renown of a keep, fort, or hall

That keeps the social logic legible at the table.
It also better matches the actual world: trust is local, fame travels unevenly, and rumor settles by road, river, and repeated telling.
