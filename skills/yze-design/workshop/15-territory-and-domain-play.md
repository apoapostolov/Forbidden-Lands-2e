<!-- markdownlint-disable MD013 -->

# Territory & Domain Play — The Map Pushes Back

> **STATUS: WORKSHOP MODULE.** Turf, settlements, patrol zones, domains, kingdoms, districts, and regional control. Built from P7 org lifecycle, P9 scale ladders, P13 settlement-as-character, and AC9.

## 1. Origin

- **Source patterns:** P7, P9, P13, P14.
- **Operators:** Abstraction-Climb + Fusion.
- **Target psychology:** owning ground creates obligations.
- **Problem solved:** territory should be a living pressure map, not a static reward.

## 2. Generic design space

A territory is a place-character with ratings, claims, pressure, and events. Each domain turn, factions act, upkeep is paid, and pressure changes the map.

### Territory sheet

- **Ratings:** Security, Wealth, Loyalty, Supply, Secrecy or Culture.
- **Claims:** who believes they own it.
- **Pressure:** 0-6 track per major threat.
- **Functions:** safehouse, market, shrine, dock, lab, barracks.
- **Events:** unrest, opportunity, attack, scarcity, scandal, discovery.

### Turn procedure

1. Pay upkeep or mark pressure.
2. Each faction takes one visible move.
3. PCs choose one domain action: Fortify, Extract, Negotiate, Build, Patrol, Hide, Celebrate.
4. Roll event if any pressure is 4+.
5. Update claims and functions.

### Domain action menu

Each domain turn, the party chooses one primary action per controlled territory. A staffed function may grant one bonus action if it is relevant.

| Action | Roll | Success | Extra ⚔ |
| --- | --- | --- | --- |
| **FORTIFY** | Craft / Command / Labor | Security +1 or remove exposed tag | create defensive function |
| **PATROL** | Scout / Ride / Survey | reduce Threat pressure by 1 | reveal hidden faction move |
| **EXTRACT** | Commerce / Survival / Labor | gain Wealth/Supply output | avoid depletion or debt |
| **NEGOTIATE** | Manipulation / Influence | improve Loyalty or claim | shift one faction Standing |
| **BUILD** | Craft / Admin / Ritual | add or repair a function | reduce future upkeep |
| **HIDE** | Stealth / Deception | reduce Heat/attention by 1 | conceal one function |
| **CELEBRATE** | Performance / Faith / Culture | Loyalty +1, clear unrest | Renown +1 or Bond Strain cleared |
| **MUSTER** | Command / Resources | create militia/crew asset | asset gains tag |

### Faction move menu

For each active faction, choose or roll. A faction with high Standing may telegraph its move; a hostile one may conceal it.

| D6 | Move | Effect |
| --- | --- | --- |
| 1 | Probe | Threat pressure +1 or reveal weak point |
| 2 | Recruit | faction asset +1 or militia appears |
| 3 | Extract | Wealth/Supply pressure +1 |
| 4 | Agitate | Loyalty −1 or unrest tag |
| 5 | Fortify claim | claim strengthens; PCs need leverage to contest |
| 6 | Strike | attack function, convoy, leader, or border |

### Territory event table

Roll when any pressure is 4+, upkeep is unpaid, or the domain turn needs a spark.

| D66 | Event | Effect |
| --- | --- | --- |
| 11-16 | **Bad season.** | Supply pressure +1; travel or upkeep costs more. |
| 21-26 | **Local dispute.** | Loyalty test; failure creates unrest. |
| 31-36 | **Opportunity.** | temporary function appears if claimed this turn. |
| 41-46 | **Raid / theft.** | lose output or defend with Patrol/Fortify. |
| 51-56 | **Political demand.** | Debt, Influence, or Standing choice. |
| 61-62 | **Hidden rot.** | reveal flaw in a function; repair project needed. |
| 63-64 | **Border flare.** | neighboring claim shifts; faction move triggers. |
| 65 | **Crisis.** | one rating drops by 2 or a function is disabled. |
| 66 | **Domain-breaking event.** | revolt, invasion, disaster, plague, or schism; start a campaign clock. |

### Resolution checks

- **Map check:** only track territories that can change ownership, function, or pressure.
- **Upkeep check:** every useful function needs upkeep, staff, secrecy, or defense.
- **Turn check:** choose one turn length and keep it stable.
- **Reward check:** territory should create actions and obligations, not passive income alone.

### Territory architecture packs

| Pack | Turn | Ratings | Functions | Pressure | Use for |
| --- | --- | --- | --- | --- | --- |
| **Gang Turf** | week/job | Security, Profit, Loyalty | safehouse, market, lookout | Heat, rivals, police | crime/heist |
| **Frontier Holding** | season | Food, Defense, Labor, Morale | farm, wall, shrine, workshop | weather, raiders, debt | survival fantasy |
| **War Front** | mission/week | Supply, Intel, Control, Morale | depot, trenches, radio, medics | enemy moves, attrition | military |
| **Noble Domain** | season/year | Wealth, Law, Faith, Loyalty | court, levy, road, granary | unrest, famine, succession | politics |
| **Wasteland Route** | journey leg | Water, Fuel, Safety, Trade | cache, garage, well, watch | scarcity, mutants, storms | post-apoc |

### Function catalog

Functions are why territory matters. Each function grants one concrete benefit and one upkeep vector.

| Function | Benefit | Upkeep | Event vulnerability |
| --- | --- | --- | --- |
| **Safehouse** | recover or hide Heat once/turn | secrecy | betrayal, surveillance |
| **Workshop** | repair/craft without penalty | materials/specialist | fire, theft, sabotage |
| **Market** | buy/sell scarce goods | law/trust | tax, gang pressure |
| **Watchtower / Sensors** | warning before raids | staff/power | false alarm, blind spot |
| **Shrine / Clinic** | recovery +1 die | faith/medicine | plague, taboo, schism |
| **Barracks / Militia** | defend with +1 | pay/morale | desertion, brutality |
| **Storehouse** | Supply die starts one step higher | guards/weatherproofing | spoilage, raid |
| **Road / Dock / Gate** | travel/trade access | tolls/maintenance | blockade, collapse |

### Claim and contest procedure

Use when multiple actors want the same territory.

1. **Name claims:** legal, ancestral, military, economic, sacred, occupation, fear.
2. **Rate claim strength:** weak (+0), plausible (+1), strong (+2), dominant (+3).
3. **Contest action:** PCs roll NEGOTIATE, FORTIFY, PATROL, BUILD, or MUSTER against the rival's claim strength + pressure.
4. **On success:** reduce rival claim or raise PC claim by 1.
5. **On failure:** pressure +1 or function disabled.
6. **At claim +3:** actor controls the territory until a crisis changes it.

### Domain-scale fallout

Roll when a domain action fails by 2+, a pressure hits 6, or a faction Strike lands.

| D66 | Fallout | Effect |
| --- | --- | --- |
| 11-16 | **Shortage.** | Supply/Wealth output reduced next turn. |
| 21-26 | **Unrest.** | Loyalty −1; Celebrate or Negotiate needed. |
| 31-36 | **Sabotage.** | function disabled until repaired. |
| 41-46 | **Border loss.** | rival claim +1 or travel route cut. |
| 51-56 | **Scandal / grievance.** | Influence or Reputation cost. |
| 61-62 | **Leadership crisis.** | named NPC demands action or resigns. |
| 63-64 | **Open violence.** | resolve raid, battle, duel, or crackdown. |
| 65 | **Revolt / takeover.** | territory changes hands unless immediate scene succeeds. |
| 66 | **Ruin.** | disaster, massacre, famine, purge, or collapse; rebuild as project. |

### Worked mini-build

**Frontier holding:** Turn = season. Ratings: Food 2, Defense 1, Labor 2, Morale 1. Functions: Palisade, Storehouse, Shrine. Pressures: Winter 3/6, Raiders 2/6, Debt 1/6. In spring the PCs choose BUILD to improve the Palisade; raiders choose Probe; event roll at Raiders 4 would trigger a raid unless PATROL succeeds.

## 3. Pressure loop

Claim -> upkeep/faction moves -> domain action -> event -> changed map.

## 4. Choices

| Choice | Local | Domain | Psychology |
| --- | --- | --- | --- |
| Turn length | session/week | season/year | turf drama vs kingdom play |
| Ratings | 3 | 5+ | light vs strategic |
| Faction moves | GM chosen | procedure/table | authored vs emergent |

## 5. Integration points

Hooks into base, faction web, reputation, heat, economy, travel, and mass conflict.

## 6. Handshake

- **Prerequisites:** map or node list, factions or threats.
- **Inputs:** territory ratings, faction list, turn length.
- **Outputs:** territory sheets, pressure tracks, domain actions.
- **Touched systems:** base, travel, economy, faction, GM.
- **Replaces or stacks:** replaces ad hoc base events at domain scale.
- **Incompatibilities:** if using a full faction turn, merge turn procedures.

## 7. Failure modes

Too many territories create spreadsheet play. Track only contested or player-owned places. Domain rewards must create upkeep, attention, or rivals.

## 8. Check notes

Use `24 §6`. Domain play is Campaign Mode unless the whole game is about territory.

## 9. Publication handoff

**Player rule:** A territory is useful because it has functions. It is dangerous because functions must be defended.

## 10. Worked example — Gang turf

Districts have Security, Profit, Loyalty. Each week, gangs make moves. PCs can Fortify, Shake Down, Recruit, or Lie Low. Heat 6 triggers a police raid.
