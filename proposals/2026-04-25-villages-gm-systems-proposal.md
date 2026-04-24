# Villages and Towns: GM-Side Procedures Proposal

## Purpose

Chapter 10 now gives settlements a history, a present condition, people, locations, and long-term change. It still lacks a GM-facing procedure set for what happens after the settlement is built and the adventurers leave it alone.

This proposal fills that gap with procedures that fit the Forbidden Lands corebook better than whimsical town color or abstract worldbuilding. The goal is a village system that behaves like part of the living world: hungry, local, political, and tied to travel.

Status: implemented in `02-gamemasters-guide/10-villages.md`.

## What Is Missing

- A settlement turn that advances the village between visits.
- A route procedure that ties villages to the journey chapter.
- A household or faction ledger for local power.
- A store and shortage procedure for grain, fuel, and trade goods.
- An entry procedure for first contact, audience, and demands.
- A simple justice and retaliation loop for crime, insult, and blood price.

## Proposed Systems

### 1. Settlement Turn

Use this when a settlement is active in the campaign and the GM wants its condition to change over time.

Procedure:

1. Advance the settlement once per month, or whenever a major event changes local life.
2. Start with `2D6`.
3. Add `+1` for each unresolved serious problem.
4. Add `+1` if food, fuel, or water is short.
5. Add `+1` if the roads to the settlement are blocked, taxed, or unsafe.
6. Add `+1` if authority is weak, disputed, or absent.
7. Subtract `1` if authority is firm and broadly accepted.
8. Subtract `1` if the settlement ended the last turn with a surplus or a solved problem.

| Roll | Result | Effect |
| --- | --- | --- |
| 2-4 | Crisis | Add one new problem and worsen one settlement feature or location. |
| 5-6 | Strain | Add pressure. The GM introduces a warning, shortage, or dispute. |
| 7-8 | Hold | No major change. The settlement keeps its present shape. |
| 9-10 | Recovery | Solve one minor problem or improve one settlement feature. |
| 11-12 | Growth | Add one location, improve one feature, or raise local confidence. |

This is the missing GM loop for a recurring village. It gives the settlement a life between visits without requiring the GM to improvise everything from scratch.

### 2. Household Ledger

Use this for the people who actually keep the settlement together: a family, a priest, a reeve, a smith, a widow with stores, or a household that can feed half the village.

Procedure:

1. Name 3-5 important households or power holders.
2. Give each one `Need` from `0` to `3`.
3. Give each one `Heat` from `0` to `3`.
4. Increase `Need` by 1 each turn if the household was not fed, paid, protected, or honored.
5. Increase `Heat` by 1 each turn if the household was insulted, cheated, or threatened.
6. At `Need 3`, the household starts taking desperate action: begging, stealing, deserting, or selling loyalty.
7. At `Heat 3`, the household creates trouble: feud, boycott, sabotage, or open violence.

This makes the village political without turning it into a court simulator.

### 3. Route Links

Use this to connect the settlement to the journey chapter.

Procedure:

1. Give the settlement 1-3 named route links to nearby places.
2. Mark each link as `Open`, `Poor`, `Blocked`, `Dangerous`, or `Taxed`.
3. When the adventurers travel through the link, the GM uses the link state to set encounter pressure, road delay, and market access.
4. When the settlement turn produces a recovery result and the road is protected or used, the link may improve one step.
5. When the settlement turn produces a crisis result and the road is ignored or attacked, the link worsens one step.

This keeps the village from feeling isolated from the rest of the map.

### 4. Stores And Shortages

Use this for grain, firewood, feed, salt, and coin.

Procedure:

1. Track each key store on a 4-step scale: `Bare`, `Thin`, `Adequate`, `Full`.
2. Start most villages at `Thin` for grain and `Bare` for coin.
3. At each seasonal turn, reduce one store by 1 step unless the settlement had a clear surplus or a successful harvest, trade run, or levy.
4. If a store reaches `Bare`, the settlement gains a fitting problem: hunger, theft, poaching, woodcutting, black market trade, or debt.
5. If a store reaches `Full`, the GM may improve a location, lower tension, or create a new trade opportunity.

This gives the GM a grounded way to model winter, scarcity, and recovery.

### 5. Arrival Procedure

Use this when the adventurers enter a settlement for the first time or return after a long absence.

Procedure:

1. Determine the road state from the nearest route link.
2. Determine whether the settlement is watched, open, fearful, or hungry.
3. Decide who meets the adventurers first: a watchman, a child, a trader, a priest, or nobody at all.
4. Decide what the settlement wants right now: news, coin, labor, protection, justice, or silence.
5. Decide whether the first demand is spoken at the gate, in the yard, or at the table.

This creates a strong opening scene and prevents settlements from becoming generic stops.

### 6. Justice And Retaliation

Use this when the adventurers break the law, offend a household, or kill inside a settlement.

Procedure:

1. Mark the offended household or authority with `Heat +1`.
2. If the offense was public, add `Heat +1` again.
3. If the offense killed someone or ruined food, add `Heat +1` again.
4. At `Heat 2`, the settlement responds with warning, demand, or fine.
5. At `Heat 3`, the settlement responds with denial of shelter, armed pursuit, ransom, or blood price.
6. If the adventurers repair the damage or pay compensation, reduce `Heat` by 1.

This keeps violence tied to the social world instead of treating villages as free loot containers.

## Where It Lands

If promoted, these systems fit after the current vicissitude material in Chapter 10, or as a new `Settlement Play` section after the location and character generators.

## Why It Fits The Book

- It keeps the village local.
- It keeps change visible.
- It gives the GM a procedure, not just a prompt.
- It matches the journey chapter by making settlements behave like places the road leads to and away from.
- It avoids whimsical drift and keeps the tone grounded in scarcity, obligation, and consequence.

## Recommended Next Step

Promote the settlement turn, arrival procedure, and route links first. They do the most work with the least space. Add the household ledger and stores next if the chapter needs more campaign pressure.
