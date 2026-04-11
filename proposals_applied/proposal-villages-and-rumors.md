<!-- markdownlint-disable MD013 -->

# Proposal: Villages and Rumors — Player-Facing Town Systems

## Purpose

Chapter 8 already has a strong settlement reputation system: Reputation scores, Standing, Hospitality, First Impression rolls, recognition, rumor travel, and leaning on your name. Chapter 12 has contracts and bounties for mercenary bands, complete with allegiance tracking, employer tiers, and negotiation tables.

What the manuscript lacks is the player-facing middle layer — the systems that answer what an adventuring party (not a mercenary band) actually does once they pass through the gate. The existing rules tell the GM how a settlement reacts to the fellowship. They do not tell the players what they can pursue.

This proposal fills that gap with five integrated subsystems:

1. **Gathering News and Rumors** — a procedure for collecting actionable information during a town visit
2. **The Notice Board** — a unified work-finding system for adventurers, compatible with Chapter 12 bounties
3. **Petitioning Authority** — working with the local chief, elder, or headman for favors, commissions, and Standing
4. **Town Activities** — quarter-day actions available in a settlement beyond shopping and sleeping
5. **Reputation as Leverage** — spending reputation for concrete mechanical benefits

Each subsystem builds on existing Chapter 8 mechanics rather than replacing them. The goal is to make every settlement visit a decision point, not a supply stop.

## Design Principles

- **Player-initiated.** The adventurers choose what to pursue. The GM does not narrate a menu.
- **Quarter-day economy.** Every town action costs time. Time spent gathering rumors is time not spent repairing gear, healing, or moving on. The journey rules already track quarter days; town systems should respect that currency.
- **Reputation-integrated.** Everything feeds back into Reputation and Standing. A fellowship that gathers news, takes bounties, and builds local trust grows its name. One that strips the market and rides out does not.
- **Scalable.** A hamlet with three huts and a hamlet with a full marketplace and inn should both support these systems, at different levels of depth. Settlement size gates what is available, not what is possible.
- **Compatible with Chapter 12.** Where mercenary bands have contracts and bounties, adventurers have the notice board and petitions. The two systems should share vocabulary, price scales, and reputation logic without requiring the mercenary chapter.

## Integration Points

| Existing System                    | Location | How This Proposal Connects                                         |
| ---------------------------------- | -------- | ------------------------------------------------------------------ |
| Settlement Reputation & Standing   | Ch 8     | All five subsystems generate or spend Reputation/Standing          |
| Hospitality & First Impression     | Ch 8     | Gates access to authority, notice board quality, and rumor sources |
| Rumors (strength, tone, travel)    | Ch 8     | Gathering News formalizes how players interact with rumor sources  |
| Leaning on Your Name               | Ch 8     | Reputation as Leverage expands this into concrete mechanical uses  |
| Contracts & Bounties               | Ch 12    | Notice Board is the adventurer-scale version, cross-compatible     |
| Finding Work / Getting an Audience | Ch 12    | Petitioning Authority is the non-mercenary equivalent              |
| Allegiance                         | Ch 12    | Patron relationships build through repeated petition work          |
| Stronghold Functions               | Ch 9     | INN, MARKETPLACE, TOWN HALL, TEMPLE gate specific town activities  |
| PATH OF WORDS                      | Ch 4     | Synergy with rumor evaluation and petition rolls                   |
| PATH OF TREASURE                   | Ch 4     | Synergy with appraisal, supply manipulation, and trade deals       |
| Economy & Supply                   | Ch 10    | Town activities reference supply rolls and price tables            |

---

## 1. Gathering News and Rumors

### The Problem

The existing rumor system describes how rumors spread between settlements (strength, tone, travel speed by terrain). It does not describe how a player character actively seeks information in a settlement they are visiting. There is no procedure for asking around, buying drinks, listening at the inn, or pressing a contact for details.

### The Procedure: ASK AROUND

**ASK AROUND** is a quarter-day activity. One or more characters spend a quarter day working the settlement for information: drinking at the inn, visiting the market, sitting at the shrine steps, talking to hirelings, listening at the gate. Each character who participates rolls one of the following, chosen before the roll:

| Skill        | What it finds                                             | Where it works best              |
| ------------ | --------------------------------------------------------- | -------------------------------- |
| MANIPULATION | Directed questions, pressing contacts, buying information | Inns, markets, authority halls   |
| INSIGHT      | Reading mood, catching lies, sensing tension              | Anywhere with people             |
| LORE         | Historical context, old stories, pattern recognition      | Shrines, libraries, learned NPCs |
| SCOUTING     | Observing traffic, reading tracks, watching the gate      | Walls, roads, outskirts          |

The difficulty depends on what the character is looking for:

| Target                               | Difficulty               | Example                                       |
| ------------------------------------ | ------------------------ | --------------------------------------------- |
| General mood and local news          | 0 (automatic with skill) | "What's the talk this week?"                  |
| Specific local rumor or recent event | 1                        | "Has anyone come through from the north?"     |
| Named person, faction, or location   | 2                        | "What do people say about the barrow warden?" |
| Hidden or suppressed information     | 3                        | "Who killed the reeve's brother?"             |
| Deliberately concealed secrets       | 4+                       | "Where does the cult meet?"                   |

**Modifiers:**

| Factor                                       | Modifier |
| -------------------------------------------- | -------- |
| Settlement has an INN or TAVERN              | +1       |
| Settlement has a MARKETPLACE                 | +1       |
| Fellowship's local Standing is +2 or higher  | +1       |
| Fellowship's local Standing is -1 or lower   | -1       |
| Character buys drinks or gifts (1 silver)    | +1       |
| Character speaks the dominant local language | +1       |
| Different kin from the settlement majority   | -1       |
| Settlement under siege, famine, or crisis    | -1       |

**Results:**

| ⚔️    | Outcome                                                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No ⚔️ | Nothing useful. The locals are tight-lipped, ignorant, or lying. The character may have drawn attention by asking the wrong person.                                                                         |
| 1 ⚔️  | A fragment. One useful detail — a direction, a name, a warning — but incomplete.                                                                                                                            |
| 2 ⚔️  | A solid lead. Enough information to act on: a location, a timeline, a motive, a contact.                                                                                                                    |
| 3+ ⚔️ | A full picture. The character learns what is known locally, including context most people would not share with strangers. The GM should also volunteer one detail the character did not think to ask about. |

**Multiple characters.** If more than one character spends the quarter day asking around, each rolls separately but the GM combines the results into a single briefing. Duplicate successes do not stack — they confirm. Contradictions are real: the sources disagree, and the fellowship must decide whom to trust.

**Rumor quality.** Not all information gathered this way is true. The GM should tag each piece of news with a reliability level, which the players do not see:

| Reliability | Meaning                                               |
| ----------- | ----------------------------------------------------- |
| Solid       | Firsthand account or well-established local knowledge |
| Likely      | Secondhand but consistent with other sources          |
| Uncertain   | Third-hand, exaggerated, or partially garbled         |
| False       | Deliberately planted, badly confused, or malicious    |

PATH OF WORDS Rank 5 can evaluate rumor reliability directly. INSIGHT at 3+ ⚔️ when listening to a specific source can detect evasion or exaggeration but not confirm truth.

### Rumor Sources by Settlement Feature

Certain stronghold functions improve the quality and range of information available:

| Function    | Effect on ASK AROUND                                                                                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INN         | +1 modifier. Travelers carry distant news. Regional rumors available, not just local.                                                                                      |
| MARKETPLACE | +1 modifier. Traders know prices, routes, and who is buying what. Economic and caravan rumors available.                                                                   |
| TEMPLE      | Religious and historical rumors available. The GM may offer one lore-related detail automatically.                                                                         |
| TOWN HALL   | Political rumors available. If the fellowship has Standing +1 or higher, the hall clerk or scribe will share posted notices.                                               |
| DOVECOTE    | Fast-moving news from linked settlements. If the settlement has a dovecote connected to at least one other, the GM may include one piece of news from the linked location. |
| TOLL HOUSE  | Traffic rumors. The toll-keeper knows who has passed through and roughly what they carried.                                                                                |

Settlements without any of these functions still support ASK AROUND, but the information is limited to what locals have personally seen or heard from the last traveler who passed through.

### Connecting to the Rumor System

When ASK AROUND succeeds in finding a rumor, it should connect to an existing rumor source from Chapter 8 if one exists. The GM checks:

1. Has a rumor source reached this settlement? If yes, the character learns about it (filtered through local bias and Standing).
2. Has no rumor source reached here? Then the information is purely local — what these people have seen with their own eyes.
3. Is the character looking for something that no rumor covers? Then ASK AROUND is original investigation, not rumor collection. The GM generates new information based on what is actually true in the fiction.

Successful ASK AROUND does not create new rumor sources. It taps existing ones. New rumor sources are created by deeds, not by asking.

---

## 2. The Notice Board

### The Problem

Chapter 12 has a robust contract and bounty system for mercenary bands: Finding Work, Getting an Audience, Negotiating Terms, Contract Categories, Bounty Types, and Payment in Goods. That system assumes a band of armed professionals with a captain, a reputation, and the muscle to fulfill military contracts.

Adventuring parties are not mercenary bands. They are smaller, less organized, and take on different kinds of work: clearing a ruin, recovering a stolen heirloom, escorting a priest, hunting a beast, delivering a message, investigating a disappearance. They need a work-finding system that scales to their size and interests.

### The Notice Board

Most settlements of Reputation 3 or higher maintain some form of public work posting. In a village this might be a carved post outside the chief's hall, notched and painted. In a town it is a board at the inn or market gate. In a stronghold it is a ledger at the town hall.

The notice board is not a magical quest dispenser. It is a list of problems that locals are willing to pay strangers to solve, because the locals cannot or will not solve them themselves.

#### What the Board Shows

The GM generates available notices when the fellowship first checks the board. Roll once to determine how many notices are posted, then roll on the Notice Category Table for each.

**Number of notices.** Roll D6 and consult the settlement's row:

| Settlement Size          | D6 1-3    | D6 4-6    |
| ------------------------ | --------- | --------- |
| Hamlet (Rep 0-2)         | 0 notices | 1 notice  |
| Village (Rep 3-4)        | 1 notice  | 2 notices |
| Town (Rep 5-7)           | 2 notices | 3 notices |
| Stronghold/City (Rep 8+) | 3 notices | 4 notices |

A settlement with a TOWN HALL adds +1 notice. A settlement with a MARKETPLACE adds +1 notice. These bonuses can exceed the table maximum.

At a hamlet with zero notices, there is no board — but the elder, the innkeep, or the gate-guard may mention a problem if the fellowship asks. Treat that as a single verbal notice (roll on the category table).

**Notice Category Table.** For each notice, roll D6:

| D6  | Category      |
| --- | ------------- |
| 1   | Clearing      |
| 2   | Escort        |
| 3   | Delivery      |
| 4   | Recovery      |
| 5   | Investigation |
| 6   | Labor         |

Hamlets (Rep 0-2) re-roll results of 5 (Investigation). Villages without outside trade links (no INN, no MARKETPLACE, no ROAD) re-roll results of 2 (Escort) — there is no one to escort and nowhere to go. The GM may always substitute a category that fits the settlement's current situation.

#### Notice Categories

| Category          | Description                                                                              | Typical Pay                 | Typical Difficulty       |
| ----------------- | ---------------------------------------------------------------------------------------- | --------------------------- | ------------------------ |
| **Clearing**      | Kill or drive off a threat near the settlement: beasts, undead, bandits, a monster lair  | 20-100 silver               | Moderate to high         |
| **Escort**        | Protect a person, wagon, or cargo on a journey of 1-10 days                              | 10-50 silver + expenses     | Low to moderate          |
| **Delivery**      | Carry an item or message to a named destination                                          | 5-30 silver                 | Low (distance-dependent) |
| **Recovery**      | Retrieve a stolen or lost item, person, or livestock                                     | 30-150 silver               | Variable                 |
| **Investigation** | Discover information: who stole the grain, where the raiders camp, what killed the sheep | 15-60 silver                | Moderate to high         |
| **Labor**         | Physical work the settlement needs: repair a wall, dig a ditch, clear a road blockage    | 5-20 silver or food/lodging | Low                      |

#### Payment Structure

Most notices follow a simple structure:

- **Flat fee:** Paid on completion. The standard for small jobs.
- **Advance + completion:** Half up front, half on return. Common for escort and clearing work.
- **Bounty:** Paid on proof. The standard for clearing and recovery. Proof means a head, a token, the stolen goods, or the person delivered alive.

Prices scale with the settlement's prosperity. A wealthy trade town pays 50% more than listed. A starving hamlet pays in food, lodging, or future favor.

#### Cross-Compatibility with Chapter 12

The notice board is the adventurer-scale entry point to the same economy that Chapter 12 describes at band scale. The categories overlap deliberately:

| Notice Board Category | Chapter 12 Equivalent                      |
| --------------------- | ------------------------------------------ |
| Clearing              | Clearing contracts                         |
| Escort                | Escort contracts                           |
| Recovery              | Recovery bounties                          |
| Investigation         | No direct equivalent (adventurer-specific) |
| Labor                 | No direct equivalent (adventurer-specific) |
| Delivery              | No direct equivalent (adventurer-specific) |

A mercenary band can take notice board work, but it is beneath their operating costs unless the band is desperate or very small. An adventuring party can attempt to fulfill Chapter 12 contracts, but they lack the manpower for most garrison, patrol, and assault work.

**Bounties specifically.** Chapter 12 bounty types (grievance, professional breach, elimination, recovery) can appear on the notice board. When they do, use Chapter 12 pricing. The notice board does not create a separate bounty economy — it is the same economy, posted publicly instead of delivered through private audience.

---

## 3. Petitioning Authority

### The Problem

Chapter 12 describes how mercenary bands get an audience with an employer and negotiate terms. Chapter 8 describes Hospitality and First Impression. Neither describes what happens when an adventuring party wants to work with the local authority directly — the village elder, the trade-town reeve, the temple warden, the mine boss.

Many of the most interesting things a fellowship can do in a settlement require authority's permission or cooperation: using the militia, accessing restricted areas, getting a letter of introduction, requesting an escort, borrowing equipment, or receiving a commission too sensitive for public posting.

### The Petition

A **petition** is a formal or semi-formal request to the settlement's authority figure. It is the adventurer-scale equivalent of Chapter 12's "Getting an Audience."

#### Getting the Meeting

| Situation                                          | Requirement                                                                |
| -------------------------------------------------- | -------------------------------------------------------------------------- |
| Fellowship has local Standing +2 or higher         | Automatic. The chief knows you and will hear you.                          |
| Fellowship has local Reputation 3+ and Standing 0+ | MANIPULATION difficulty 1. A name that carries no ill will opens the door. |
| Fellowship has a letter of introduction or sponsor | No roll. The sponsor's Standing applies for the first meeting.             |
| Fellowship has just completed a notice board job   | No roll. The employer wants your report.                                   |
| Cold approach, Reputation 1-2                      | MANIPULATION difficulty 2. The chief is busy.                              |
| Cold approach, Reputation 0 or Standing negative   | MANIPULATION difficulty 3. You are strangers or they remember you badly.   |

#### What You Can Petition For

| Request                                                   | Difficulty | Standing Requirement | Typical Cost                                     |
| --------------------------------------------------------- | ---------- | -------------------- | ------------------------------------------------ |
| Local information (maps, routes, known threats)           | 1          | 0+                   | Free or 1 silver for a scribe's work             |
| Letter of introduction to a nearby settlement             | 1          | +1                   | Free (the chief vouches for you)                 |
| Use of settlement resources (forge, stable, stores)       | 1          | 0+                   | Standard rates, no markup                        |
| Access to restricted areas (armory, vault, records)       | 2          | +1                   | Usually a service in return                      |
| Militia escort or armed support (1-3 fighters, 1-3 days)  | 2          | +1                   | 5 silver/day per fighter, or a service           |
| Commission (private job, too sensitive for the board)     | 2          | 0+                   | Above-market pay, discretion expected            |
| Emergency supplies (food, medicine, arms during shortage) | 3          | +2                   | Triple price, repayment expected                 |
| Political favor (endorsement, alliance, intercession)     | 3          | +2                   | Significant service or reputation at stake       |
| Settlement resources for stronghold building              | 3          | +2                   | Standard price, but access itself is the barrier |

The MANIPULATION roll to petition uses the difficulty listed. Standing modifies the roll as usual. A successful petition grants the request with whatever terms the authority sets. Extra swords on the roll may reduce the cost, remove a condition, or add a bonus (the authority throws in a guide, extends the loan, or shares a private detail).

A failed petition does not mean hostility. It means the authority declines — too busy, too cautious, or does not trust you enough yet. The fellowship can try again after improving Standing or completing work that proves their value.

#### Building a Patron Relationship

Repeated successful interactions with the same authority figure build toward a patron relationship, tracked the same way Chapter 12 tracks Allegiance for mercenary employers:

| Level | Name     | Access                                                                                  |
| ----- | -------- | --------------------------------------------------------------------------------------- |
| 0     | Stranger | Cold approach required                                                                  |
| 1     | Known    | Audience automatic. No other benefit.                                                   |
| 2     | Trusted  | Supply at local rates, priority access to commissions, letter of introduction available |
| 3     | Favored  | Private commissions, militia support, political backing within the settlement's sphere  |

Patron level increases by +1 each time the fellowship completes a commission or major favor for that authority. It decreases by -1 for each betrayal, public embarrassment, or broken promise. Unlike Chapter 12 Allegiance, adventurer-patron relationships do not offer exclusive contracts or sworn service — the scale is smaller, the obligations lighter.

---

## 4. Town Activities

### The Problem

The journey system tracks quarter days carefully. Camp activities (Make Camp, Keep Watch, Forage, Hunt, Fish, Rest, Sleep, Explore) are well defined. But when the fellowship arrives in a settlement, the quarter-day system goes quiet. The players buy gear, heal, and leave. Settlements feel like supply caches, not living places.

### Settlement Quarter-Day Activities

Each of the following costs one quarter day, the same as any journey activity. A character may perform one town activity per quarter day spent in the settlement.

#### ASK AROUND

Described in Section 1 above. Gather news, rumors, and local intelligence.

#### SEEK WORK

Check the notice board (Section 2) or make a MANIPULATION roll to find unlisted work. Difficulty 1 in a town with a MARKETPLACE or INN, difficulty 2 otherwise. Success turns up a notice or a verbal lead on available work.

#### PETITION

Request a meeting with the local authority (Section 3). The petition itself is a quarter-day commitment — traveling to the hall, waiting, presenting your case, and hearing the answer.

#### TRADE

Buy or sell goods at the local market. This is the existing Chapter 10 economy system, but framed as a time cost. One quarter day covers a full session of buying, selling, and bartering — not one item at a time as assumed by most shopping lists.

A character with PATH OF TREASURE may appraise goods as part of this activity at no extra time cost.

#### REPAIR AND CRAFT

Use the settlement's available tools and functions to repair damaged gear or craft items. This follows the Chapter 10 crafting rules, but access to the settlement's FORGE, TANNERY, or workshop replaces needing your own. The settlement may charge for access (1-5 silver per quarter day, depending on the function and the settlement's disposition).

#### CAROUSE

Spend time and silver at the inn, drinking hall, or whatever passes for entertainment. Roll MANIPULATION.

| ⚔️    | Outcome                                                                                                                                                                                                  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No ⚔️ | Drunk, broke, or in trouble. Lose 1D6 silver and suffer a MISHAP: pick a pocket gone wrong, insult a local, pass out in the street, or worse. Standing -1 at this settlement if the incident was public. |
| 1 ⚔️  | A decent night. Lose 1D6 silver but recover 1 WP and hear one piece of local gossip (treat as ASK AROUND with 1 ⚔️).                                                                                     |
| 2 ⚔️  | A good night. Lose 1D6 silver but recover 2 WP, hear useful gossip (ASK AROUND with 2 ⚔️), and make a friendly acquaintance who might help later.                                                        |
| 3+ ⚔️ | A legendary night. Lose 2D6 silver but recover 3 WP, gain a contact (the GM names them), and the story of the evening may itself become a minor rumor source. Standing +1 if the crowd was impressed.    |

Carousing is the messy alternative to ASK AROUND — louder, riskier, more expensive, but with WP recovery and a chance at contacts that careful questioning does not produce.

#### HEAL

Seek treatment from a local healer, herbalist, or temple. This follows the standard healing rules but uses the settlement's resources. A settlement with a TEMPLE or skilled NPC healer may offer treatment beyond what the fellowship can provide. Cost follows the Common Services table in Chapter 10 (1-5 silver depending on severity).

#### REST

Spend the quarter day doing nothing productive. Recovery follows standard rules. In a settlement with an INN, rest is comfortable and guaranteed — no mishaps, no WP loss.

#### TRAIN

Seek a teacher for a new skill or talent rank. This follows the existing teacher rules but frames it as a town activity. Teachers are Rare on the supply table; a settlement with a TEMPLE, GUILD HALL, or specialist NPC may offer training that a roadside camp cannot.

---

## 5. Reputation as Leverage

### The Problem

The existing "Leaning on Your Name" system is good but narrow. It provides a general table of outcomes (fair hearing, minor favor, significant favor, scene-shaping response) without connecting those outcomes to specific mechanical benefits. This section catalogues concrete things a fellowship can purchase with reputation.

### Spending Your Name

These benefits are not free. Each one requires the fellowship to roll their local Settlement Reputation as described in "Leaning on Your Name" (Chapter 8). Standing modifies the outcome as usual. Each use is a social transaction — the fellowship is drawing on goodwill, and repeated draws without replenishment diminish the well.

| Benefit               | ⚔️ Required | Standing Minimum | Effect                                                                                                                                            |
| --------------------- | ----------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Credit**            | 1           | 0                | Buy goods up to 10 silver on promise of future payment. Default within one season damages Standing by -2.                                         |
| **Shelter**           | 1           | 0                | Free lodging for the group for one night, no questions asked.                                                                                     |
| **Introduction**      | 1           | 0                | A local vouches for you to an NPC, faction, or nearby settlement. Acts as a sponsor for your next First Impression roll there.                    |
| **Discount**          | 2           | +1               | 10% reduction on a single large purchase (20+ silver).                                                                                            |
| **Priority service**  | 2           | +1               | Skip the queue. Immediate access to a healer, smith, or official who would otherwise require waiting.                                             |
| **Local guide**       | 2           | +1               | A knowledgeable local accompanies the group for up to 3 days, providing terrain knowledge (+1 to SURVIVAL for navigation) and local intelligence. |
| **Emergency aid**     | 3           | +2               | The settlement commits resources in a crisis: militia reinforcement (3-6 fighters for 1 day), emergency grain, medical supplies, or a fast horse. |
| **Political backing** | 3           | +2               | The settlement's authority figure publicly endorses the fellowship's cause. This carries weight with neighboring settlements and factions.        |
| **Sanctuary**         | 3           | +2               | The settlement shelters the fellowship from pursuers, conceals their presence, or refuses to cooperate with those hunting them.                   |

**Reputation drain.** Each time the fellowship uses Reputation as Leverage for a benefit of 2 ⚔️ or higher, the GM may note it. If the fellowship draws heavily on a settlement's goodwill without replenishing it through deeds, prices, or service, the GM may apply a -1 penalty to future Leaning on Your Name rolls at that settlement, representing social fatigue. Completing work, donating resources, or improving the settlement resets this penalty.

### Negative Reputation as Threat

Where Standing is -2 or worse, leaning on your name still works — but the mechanism is fear, not friendship. The same Reputation roll applies, but outcomes take a different shape:

| ⚔️  | Outcome                                                                                                                                                                                          |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Locals comply but resent it. They do what you ask to avoid trouble, and Standing worsens by -1.                                                                                                  |
| 2   | Locals comply and spread the word. Obedience in the moment, but a rumor source of strength 1-2 (tone: feared/hated) begins spreading.                                                            |
| 3+  | Locals comply completely and visibly. The settlement bends. But the rumor is strength 3, and neighboring settlements that hear it may prepare to resist, ally against you, or seek outside help. |

Fear is a lever, not a currency. It works until someone decides the cost of obedience is higher than the cost of resistance.

---

## Settlement Visit Flow — Putting It Together

When the fellowship arrives at a settlement, the visit follows a natural sequence:

1. **Arrival.** First Impression roll if needed (Chapter 8). Gate encounter if fortified.
2. **Recognition.** Being Recognized procedure (Chapter 8). The settlement decides what it knows about you.
3. **Quarter-day activities.** The fellowship chooses how to spend their time. Each character picks one activity per quarter day: ASK AROUND, SEEK WORK, PETITION, TRADE, REPAIR, CAROUSE, HEAL, REST, or TRAIN.
4. **Work.** If the fellowship takes a notice board job or accepts a commission, the work itself follows standard adventure procedures — travel, exploration, combat, social encounters, and return.
5. **Return and report.** Completing work adjusts Reputation, Standing, and patron level. Payment is collected. The notice board updates.
6. **Departure.** The fellowship leaves with whatever they gained — gear, information, reputation, silver, or scars.

This loop turns every settlement visit into a small arc: arrival, engagement, work, return. The arc may take one session or many, depending on what the fellowship pursues. But even a single quarter day of ASK AROUND and TRADE gives the players meaningful decisions inside the walls.

---

## Open Questions

1. **Carouse risk table.** Should carousing mishaps have an expanded random table (D66 results), or should the GM wing it? A table adds flavor and replayability. Free narration preserves the GM's authority. The proposal leans toward a short table (6-12 entries) as a compromise.

2. **Patron level cap.** Should adventurer-patron relationships cap at level 3 (Favored), or should level 4 (Retained, sworn-service equivalent) exist for adventurers? The proposal caps at 3 because adventurers are not retainers. But GMs who want deeper patron arcs could extend it.

3. **Notice board refresh.** How often does the notice board update? The proposal suggests the GM refreshes available notices each time the fellowship visits after an absence of at least one week. Notices taken by other parties (NPC adventurers, mercenary bands) may disappear between visits.

4. **ASK AROUND and INSIGHT.** Should INSIGHT be a separate activity (OBSERVE) that covers reading the settlement's mood without speaking to anyone — watching the gate traffic, studying the market, reading faces? Or is that covered by SCOUTING already? The proposal uses INSIGHT within ASK AROUND, but a dedicated observation activity could be split out.

5. **Integration with Traderoads.** The companion proposal (Traderoads of the Forbidden Lands) covers caravan economics. Town activities should reference caravan arrival, cargo selling, and trade-route rumors. The two proposals should be integrated once both are drafted.

---

## Summary of New Rules

| New Rule                            | Type                                 | Integrates With                    |
| ----------------------------------- | ------------------------------------ | ---------------------------------- |
| ASK AROUND                          | Quarter-day activity + skill roll    | Ch 8 Rumors, Stronghold functions  |
| Notice Board                        | Work-finding system + payment tables | Ch 12 Contracts & Bounties         |
| Petition                            | Social encounter + MANIPULATION roll | Ch 12 Allegiance, Ch 8 Standing    |
| Town Activities (6 types)           | Quarter-day action framework         | Ch 8 Journey system, Ch 10 Economy |
| Reputation as Leverage (9 benefits) | Mechanical spend table               | Ch 8 Leaning on Your Name          |
| Negative Reputation as Threat       | Fear-based leverage table            | Ch 8 Standing                      |
| Patron Relationships (0-3)          | Adventurer-scale allegiance          | Ch 12 Allegiance                   |
| Settlement Visit Flow               | Procedural framework                 | All above                          |

<!-- markdownlint-enable MD013 -->
