<!-- markdownlint-disable MD013 -->

# Multi-Rule Sequence Calibration

## Purpose

This reference teaches how to write examples that must teach several small rules inside one short scene. Use it when the manuscript needs a playable example — combat exchanges, journey pressure chains, recovery countdowns — rather than a static rule summary.

The goal is to explain it in the order the table experiences it. Not in the order the rules appear in the chapter. Not in the order a designer thinks about the system. In the order a player and a GM would actually encounter the triggers, rolls, and consequences during play.

## The Pattern

The strongest multi-rule examples in this manuscript do five things:

1. Establish who is acting and what the immediate pressure is.
2. Move through the action in real timing order.
3. Mention only the rule hooks that actually matter to the outcome.
4. Show consequences immediately after the triggering action.
5. Stop as soon as the lesson is learned.

They do not try to exhaust the subsystem. They teach one live sequence. The reader extrapolates the rest.

## Combat Sequence

Primary source: `corebook/05-combat-and-damage.md`

### What The Original Example Teaches

The Tyrgar and the orcs example teaches several rules at once:

- Movement across range bands
- Action economy — one fast and one slow action
- The effect of having already spent both actions
- Knocking an enemy prone for positional advantage
- Bonus dice from position
- Damage overflow after the first success
- Broken as the terminal consequence

### Why It Works

The example does not pause to restate each rule in abstract terms. It moves from:

1. Enemy movement into melee range
2. Tyrgar's shove (fast action)
3. Tyrgar's attack against the prone orc (slow action)
4. The orc's inability to defend (both actions spent)
5. The damage result and overflow
6. The next character's turn

The reader learns action timing by following the scene. Not by being told about action timing and then seeing it demonstrated.

### What To Preserve When Writing New Combat Examples

- Start with the tactical position, not with a lecture about the rules being demonstrated.
- Name which action is fast and which is slow only when that distinction changes the outcome.
- Show defensive limits only when they affect the result. If the defender can parry, do not mention it until they try.
- Convert extra successes into immediate bodily consequence: armor absorbs, wound opens, bone breaks. Not: "the excess damage is applied as additional attribute reduction."
- End once the interaction is clear. If the reader has seen the rule chain resolve, stop.

### Good Shape

> The raider has already spent both actions, so he cannot parry when Heme swings.

### Bad Shape

> As explained above, characters normally have two actions, and because of the reactive-action structure established earlier, the raider is no longer eligible to parry.

The first version teaches through the scene. The second teaches through cross-referencing its own explanations. The first trusts the reader to remember the two-action rule. The second does not.

### The Combat-Example Rule

Combat examples should read like a brief exchange of blows — three to six short paragraphs where each paragraph is one action or one consequence. They should never read like annotated design notes.

## Journey Sequence

Primary source: `corebook/08-journeys.md`, `corebook/06-critical-injuries.md`

### What The Original Sequence Teaches

The `BARE GROUND` and `SLEEP` rules teach an understated but important pressure chain:

- The party saves time by not making camp
- Each traveler must roll Survival
- Failure means no sleep
- No sleep means becoming Sleepy
- No fire also exposes the group to cold
- At extreme cold, the risk compounds

This is not one rule. It is a pressure chain. The rules interact because the first shortcut (skipping camp) triggers the second cost (no sleep), which triggers the third cost (a condition), which worsens under the fourth condition (cold weather). The manuscript teaches this chain by following the player decision that starts it.

### Why It Works

The text starts with the tempting shortcut: you can save time by not making camp. Only then does it reveal the price. That is a strong manuscript habit:

- Choice first
- Cost second
- Downstream pressure third

The reader does not learn about the Sleepy condition in isolation. They learn about it because a character skipped camp and failed a roll. The condition has weight because it has a cause.

### What To Preserve When Writing New Journey Examples

- Begin with the travel decision, not with condition bookkeeping.
- Move into the roll that determines comfort or shelter.
- State the failed outcome as a thing that happens to the character: "She gets no sleep."
- Then show the condition or recovery consequence: "She becomes Sleepy."
- If weather compounds the problem, add it after the camp failure, not before.

### Good Shape

> The company pushes on into dusk and saves the Quarter Day they would have spent making camp. That night each of them must roll Survival to find a place to sleep. Siga fails. She gets no sleep, becomes Sleepy, and because there is no fire she must also face the cold.

### Bad Shape

> Remember that characters can become Sleepy and Cold due to multiple interacting factors in the journey subsystem.

The first version follows a character through a decision chain. The second version summarizes the existence of a system. The first creates a bargain the player can feel — save time now, pay for it in comfort. The second creates nothing.

### The Journey-Example Rule

Journey examples should make the player feel the bargain: time traded for safety, short-cuts traded for comfort, speed traded for supplies. The example teaches the chain of consequence by following the road decision that starts it.

## Recovery Sequence

Primary source: `corebook/05-combat-and-damage.md`, `corebook/06-critical-injuries.md`

### What The Original Sequence Teaches

The Tyrgar critical-injury example teaches a compact but complex chain:

- A character is already hurt
- The next hit makes him Broken
- A critical injury is rolled
- The injury creates a lethal timer
- The character may recover consciousness before the timer ends
- Self-treatment is possible but risky
- Failure leaves only the remaining time to find help

The healing rules elsewhere add more pressure:

- A successful Healing roll takes one hour
- It pauses the timer during treatment
- Each patient has a daily limit
- Poor conditions penalize treatment

### Why It Works

The example is short because it does not explain every branch. It follows only the branch Tyrgar actually walks:

1. Broken
2. Injury roll
3. Death clock starts
4. Return to awareness
5. Failed self-heal
6. Narrowed remaining window

That is enough to teach urgency. The reader does not need to see every possible outcome. They need to see one outcome that makes the stakes clear.

### What To Preserve When Writing New Recovery Examples

- Establish the wound and the timer early. The reader needs to know the clock is running.
- Keep the clock visible. If four hours have passed, say so.
- Mention treatment time only when it changes the stakes. "The healing roll takes an hour — and he has three hours left."
- Show the difference between getting back on your feet and actually being safe. Consciousness is not recovery. Attribute recovery is not injury resolution. These are different clocks.
- Stop before the example turns into a full rescue narrative. The lesson is the pressure, not the story.

### Good Shape

> Varg is conscious again after an hour, but that does not end the danger. The spear wound in his side will still kill him unless someone succeeds with Healing before the timer runs out. Three hours remain.

### Bad Shape

> This demonstrates the distinction between recovering attribute points and resolving the underlying critical-injury state.

The first version puts the reader on the ground with a dying man and a clock. The second version explains the architecture of the subsystem. The first is an example. The second is a footnote.

### The Recovery-Example Rule

Recovery examples should feel like dwindling time, cold ground, and bad odds. They should never sound clinical. The reader should feel the same pressure the player feels when a friend is bleeding and the healer has one shot.

## Reusable Rules For Writing Sequences

1. **Use names, not placeholders.** "Siga fails her Survival roll" carries weight. "Character B fails the relevant roll" carries none.

2. **Put the triggering choice or blow first.** The example starts with the action that creates the chain, not with the rules that govern it.

3. **Teach order of operations through the scene.** Do not list the rules and then demonstrate them. Walk through the scene and let the rules appear when they fire.

4. **Mention only the rule hooks that change the outcome.** If the armor value does not matter in this exchange, do not mention it. If the initiative order does not create drama, start after initiative is resolved.

5. **Keep the consequence close to the roll.** The damage should follow the attack in the next sentence, not after a paragraph of explanation.

6. **Keep it short.** If the example takes more than three paragraphs to explain one interaction, it is too broad. Narrow the scope. Teach one chain per example.

7. **End on the practical result.** The enemy is Broken. The traveler is Sleepy. The wounded ally is still dying with three hours left. The example ends on a world state the player can act on, not on a system observation the designer can admire.
