<!-- markdownlint-disable MD013 -->

# Vehicles & Crews — The Shared Machine

> **STATUS: WORKSHOP MODULE.** A framework for ships, starships, caravans, trains, mechs, airships, rigs, and other shared vehicles. Built from P6 activity menus, P7 org lifecycle, P8 feature grammar, AC7, and AC8.

## 1. Origin

- **Source patterns:** P6, P7, P8, P9.
- **Operators:** Domain Transfer + Abstraction-Climb.
- **Target psychology:** coordination under shared risk.
- **Problem solved:** vehicle play should involve the whole table, not only the pilot.

## 2. Generic design space

A vehicle is a small org with attributes, stations, tags, damage, upkeep, and roles. Each vehicle Round, crew choose stations. Unfilled stations create vulnerabilities.

### Vehicle sheet

- **Frame:** light / standard / heavy / colossal.
- **Attributes:** Hull, Handling, Power, Systems.
- **Stations:** Helm, Weapons, Craft, Sensors/Comms, Support.
- **Tags:** ARMORED, FAST, FRAGILE, CARGO, STEALTH, LONG-RANGE, TEMPERAMENTAL.
- **Tracks:** Damage, Stress, Supply, Heat.

### Round procedure

1. Declare objective: escape, close, strike, hold, scan, repair, protect.
2. Each PC chooses one station action.
3. Resolve station rolls in fiction order.
4. Apply vehicle damage or crew stress.
5. If a station was unfilled under threat, GM may advance a vulnerability clock.

### Station action menu

Each station can be crewed by one PC. A station may be uncrewed, but if the vehicle is under pressure the GM may advance a Vulnerability clock tied to that station.

| Station | SLOW action | FAST action | Success menu |
| --- | --- | --- | --- |
| **HELM** | Maneuver, evade, close, break away | Jink: cancel 1 incoming shift | gain position, impose −1, clear hazard, set range |
| **WEAPONS** | Fire, lock, ram, suppress | Snap shot: low damage / force reaction | damage, disable tag, pin target, trigger crit |
| **SYSTEMS** | Repair, reroute, overcharge | Brace: reduce incoming damage by 1 | restore track, add Power, clear tag, prevent crit |
| **SENSORS/COMMS** | Scan, jam, spoof, hail | Mark: give ally +1 | reveal weakness, block signal, create leverage |
| **SUPPORT** | Treat crew, coordinate, load cargo, handle passengers | Assist station at +1 | clear Stress, move crew, protect asset, recover supply |
| **COMMAND** (optional) | Issue plan, rally, change objective | Spend Willpower or Faith for team +1 | let two stations share a tag, clear confusion |

### Vehicle resolution checks

Use this order when the machine is in danger.

1. **Position:** did HELM win, lose, or hold relative position?
2. **Effect:** did WEAPONS or a hazard create damage?
3. **Systems:** did SYSTEMS prevent, repair, or overcharge?
4. **Information:** did SENSORS/COMMS reveal or conceal?
5. **Crew:** did SUPPORT prevent Stress, injury, or passenger loss?
6. **Vulnerability:** any uncrewed critical station under pressure advances its clock.

### Damage and criticals

Vehicle Damage is a 0-6 track by default. At 3, the vehicle is **Compromised**; at 6, it is **Disabled**. When a powerful hit lands, or damage reaches 3/6, roll or choose a vehicle critical.

| D66 | Critical | Effect |
| --- | --- | --- |
| 11-16 | **Shaken frame.** | −1 HELM until repaired. |
| 21-26 | **Weapon jam / cargo shift.** | WEAPONS or cargo function offline until SYSTEMS succeeds. |
| 31-36 | **Power drop.** | Lose one FAST station action next Round. |
| 41-46 | **Crew hit.** | One station crew takes 1 damage or Stress. |
| 51-56 | **Exposed system.** | Next hit deals +1 Damage unless braced. |
| 61-62 | **Fire / breach.** | Start 4-clock; fills = Disabled. |
| 63-64 | **Station dead.** | One station unusable for the scene. |
| 65 | **Crippled.** | Vehicle cannot pursue objective; needs project repair. |
| 66 | **Catastrophic failure.** | Vehicle destroyed, captured, crashed, or abandoned; occupants face fallout. |

### Overcharge and strain

A crew may overcharge once per Round: gain +2 dice to one station or take an extra station action. Then roll the vehicle Stress die; on 1-2 it steps down. At D6 + contraction, roll a critical and reset Stress to D8 only after downtime repair.

### Vehicle design checks

- **Spotlight check:** every station must have a SLOW action that can decide a scene.
- **Pilot check:** HELM cannot solve damage, information, repair, and morale alone.
- **Scale check:** vehicle dice should stay near character dice; threat comes from tags, stations, and criticals.
- **Repair check:** serious vehicle consequences require time, parts, safe port, or Debt.

### Vehicle build procedure

Use this to create a vehicle in five minutes.

1. **Choose frame:** light, standard, heavy, colossal.
2. **Assign ratings:** distribute 10 points across Hull, Handling, Power, Systems; min 1, max 4 for normal vehicles.
3. **Pick stations:** 3 for light, 5 for standard/heavy, 6-7 for colossal.
4. **Pick tags:** one strength tag, one limitation tag, one genre tag.
5. **Set tracks:** Damage 6; Stress die D8 or D10; Supply die if travel matters.
6. **Write critical weakness:** what kind of hit creates a crisis?

### Frame table

| Frame | Ratings | Stations | Tags | Damage | Use for |
| --- | --- | --- | --- | --- | --- |
| **Light** | 8 points, max 4 | 3 | 1 strength, 1 flaw | 4 | bike, skiff, fighter, small mech |
| **Standard** | 10 points, max 4 | 5 | 2 strength, 1 flaw | 6 | ship, truck, shuttle, suit |
| **Heavy** | 12 points, max 5 | 5-6 | 3 strength, 2 flaws | 8 | tank, frigate, crawler |
| **Colossal** | 14+ points, max 5 | 6-7 | 4 strength, 3 flaws | segmented | capital ship, walking fortress |

### Vehicle tag menu

| Strength tag | Rule effect |
| --- | --- |
| **ARMORED** | first damage each scene reduced by 1 |
| **FAST** | +1 HELM when closing/escaping |
| **STEALTH** | +1 to avoid detection before combat |
| **HEAVY WEAPONS** | WEAPONS can trigger critical on 2+ extra ⚔ |
| **REDUNDANT SYSTEMS** | ignore first Station Dead critical |
| **CREWED WELL** | unfilled station clock starts at 0 instead of 1 |

| Flaw tag | Rule effect |
| --- | --- |
| **FRAGILE** | criticals trigger at Damage 2/5 instead of 3/6 |
| **LOUD** | Heat +1 when overcharging or entering scene |
| **HUNGRY** | Supply/Power die steps on 1-3 |
| **SLUGGISH** | −1 HELM in tight spaces |
| **TEMPERAMENTAL** | pushed SYSTEMS failure triggers critical |
| **EXPOSED CREW** | crew hit criticals affect two stations |

### Crew complication table

Roll when Support is unfilled during a critical, passengers panic, or crew Stress contracts at D6.

| D6 | Complication | Effect |
| --- | --- | --- |
| 1 | Panic in compartment | SUPPORT required before next objective. |
| 2 | Injured specialist | one station at −1 until treated. |
| 3 | Conflicting orders | COMMAND or SENSORS needed; otherwise next margin cannot carry. |
| 4 | Passenger/cargo loose | choose: lose cargo, lose position, or take Damage +1. |
| 5 | Mutiny/refusal | Bond/Crew morale test or station unavailable. |
| 6 | Heroic save | clear complication, but mark Bond Strain or crew injury. |

### Installation examples

**Starship:** Hull, Maneuver, Reactor, Sensors. Stations: Helm, Tactical, Craft, Comms, Medical. Stress die is Reactor. Criticals can vent atmosphere, fry jump drive, or injure crew.

**Mecha:** Hull, Agility, Reactor, Targeting. Stations collapse into pilot actions for solo mechs: Maneuver, Strike, Vent, Scan, Guard. Overcharge is central; pilot takes Stress when Reactor contracts.

**Caravan:** Hull, Handling, Supply, Morale. Stations: Driver, Scout, Guard, Quartermaster, Healer. Damage includes axle break, animal panic, lost cargo, and passenger injury.

## 3. Pressure loop

Mission -> station choices -> shared machine risk -> damage/upkeep -> base/project pressure.

## 4. Choices

| Choice | Light | Heavy | Psychology |
| --- | --- | --- | --- |
| Stations | 3 | 5-7 | fast scenes vs crew drama |
| Damage | single track | typed criticals | cinematic vs technical |
| Upkeep | abstract cost | project + parts | pulpy vs simulation |

## 5. Integration points

Uses conflict, gear tags, repair/crafting, base upkeep, chase rules, and signature conflicts.

## 6. Handshake

- **Prerequisites:** action budget and repair/recovery.
- **Inputs:** vehicle scale, station skills, damage rules.
- **Outputs:** vehicle sheet, station actions, damage/upkeep.
- **Touched systems:** conflict, gear, travel, base, economy.
- **Replaces or stacks:** replaces single-pilot vehicle rolls for major scenes.
- **Incompatibilities:** do not run a full vehicle rule set for trivial travel.

## 7. Failure modes

Avoid station imbalance. Helm and Weapons are obvious; Craft, Comms, and Support need equally decisive actions. Vehicle harm must affect crew choices, not become separate bookkeeping.

## 8. Check notes

Use `24 §4`. One PC filling two critical stations for free collapses the crew puzzle.

## 9. Publication handoff

**Player rule:** In a vehicle scene, choose one station each Round. Your station decides how the machine survives, moves, strikes, or recovers.

**GM procedure:** Use full vehicle rules only when the vehicle is at stake.

## 10. Worked example — Mecha squad

Each mech has Hull, Handling, Reactor, Systems. Pilot chooses Maneuver, Strike, Vent, Scan, or Guard. Reactor Stress powers extra actions but rolls Heat at scene end.
