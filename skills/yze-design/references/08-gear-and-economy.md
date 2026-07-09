<!-- markdownlint-disable MD013 MD024 MD041 MD060 -->

# Gear and Economy — Equipment, Crafting, Money

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the stuff layer — it assumes the dice grammar and Gear Dice of `00-engine-core.md` §3, the conflict action budget of `03-conflict-and-combat.md`, and the downtime/season loop of `06-travel-and-downtime.md`. The central deliverables are the **Feature Grammar** (§6–7: weapons and armor are defined by *composable tags*, not stat lines), the **Economy-Model choice** (§4: barter+silver vs cash+capital), the **Inventory/Transport pressure layer** (§11), and the **Crafting/Construction/Investment translator** (§12). The **Availability/Scarcity table** (§3) is shared near-verbatim by both games.

## Contents

1. Source provenance
2. Abstraction target
3. Supply / scarcity / availability tables — **shared near-verbatim**
4. Economy models: the economy choice (barter+silver / cash+capital+loans+salaries)
5. Crafting — the making layer (talent-gated, workshop-gated, time-gated, material-gated)
6. Weapon feature grammar — **the central reusable artifact**
7. Armor feature grammar
8. Quality tiers and condition/degradation
9. Artifact / legendary gear and the artifact die
10. Consumables as resource dice
11. Inventory, transport, and storage pressure
12. Crafting, construction, investment economics, trade routes, and gambling
13. Strange Devices
14. Divergence rows (FL vs West)
15. Rule Choices and Build Recipe
16. Design intent

## 1. Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/10-gear.md:9-19` — **Supply** ratings (Common / Uncommon [D6≥4] / Rare [D6=6] / Extremely Rare [D66 65–66]) and the weekly restock rule.
- `01-corebook/10-gear.md:21-28` — **Economy**: gold is ceremonial (sponsor/special order/+1D6 weeks lead time, treat as Extremely Rare), silver + barter dominate daily trade, scarcity inflation (+50%–200%), specialist access gated by talent.
- `01-corebook/10-gear.md:30-54` — **Crafting & labor**: Raw Materials / Time (two Quarter Days/day; bonus for extra time) / Talents (simple vs *advanced*) / Tools & Functions; **workshop limits** (missing function = +50% time, −1), **specialists** (advanced needs one or it's impossible), **assistants** (−25% time each, min ½ time at 3), **fitting time** (armor 1–2 days, poor fit = −1 MOVE or −1 AR), **seasonal work** (winter +50% unless indoors).
- `01-corebook/10-gear.md:56-76` — Common Services table; `:568-616` Clothes; `:627-636` Transport; `:638-651` Tools; `:653-682` Raw Materials; `:684-698` Animals; `:700-714` Buildings.
- `01-corebook/10-gear.md:716-921` — **Craftsman items** by talent (Bowyer / Smith / Tailor / Tanner): new materials, weapons, armor, masterwork rules, alternative materials (bone/flint/steel/dwarven steel), `:739` masterwork arrows, `:802-822` the metallurgy ladder (Iron→Wrought iron→Steel→Crucible steel→Dwarven steel, each adding +1 to +3 Weapon Bonus/Armor Rating at higher crafting difficulty).
- `01-corebook/10-gear.md:922-1106` — **Artifacts**: name (D66), bonus (D8/D10/D12), type (skill vs combat), oddity table (D66), the "Artefact Die varies by moon/season/time of day" oddities.
- `01-corebook/10-gear.md:1108-1227` — **Inventor items** (firearms, bombs, acid, viscid fire, etc.).
- `01-corebook/05-combat-and-damage.md:449-461` — Weapon attributes (GRIP/BONUS/DAMAGE/RANGE/COST/FEATURES); `:462-470` **Weapon Quality** tiers (Crude −1 BONUS & breaks at 0 / Standard / Fine +1 BONUS, ×2 cost, one step rarer, +1 MANIPULATION as status); `:472-536` **Weapon Features** (the full tag set: Armor Rating x2, Blunt, Brittle/Fragile, Burning, Chained, Edged, Flexible, Half-Hand, Heavy, High-Velocity, Hook, Light, Load/Load x2, Long-Reach, Loud, Melee/Ranged, Misfire, Parrying, Pierce Armor, Pick, Pointed, Polearm, Ranged (Blunt/Pointed), Ready, Shield-breaker, Short-Reach, Smashing, Tiny, Trapping, Unarmed, Windlass); `:538-540` **Armor Features** (TOUGH); `:542-583` melee weapon table; `:587-600` ranged weapon table; `:650-727` armor, helmets, cover, shields (TOUGH flag on some weapons/armor).
- `01-corebook/07-magic.md:480` — artifact die as a crafting ingredient for permanent magic items (Cost 1/2/3 for D8/D10/D12; min total Power Level 2/4/8); `:122-124` burning a D8 for attribute damage.

**Tales of the Old West 2E (West):**
- `01-corebook/06-life-in-the-old-west.md:11-63` — **Money**: Cash (dollars) + **Capital** ($250 = 1 Capital; no upper limit); converting cash→Capital; liquidating Capital (roll D6 × $50 = $50–$300, committed once rolled); the Robber Barons warning.
- `01-corebook/06-life-in-the-old-west.md:55-63` — **Loans**: 5%–10% interest per season, ≥1 year term, collateral (land/home/farm/business), foreclosure on default; banks as fly-by-night/fraud/robbery targets.
- `01-corebook/06-life-in-the-old-west.md:84-125` — **Salaries Table** (per season; −25% if board included), ranging Army Private/Baker/Barkeep $75 → Federal Marshal $300.
- `01-corebook/06-life-in-the-old-west.md:133-351` — **Outfits/Business/Property**: starting/investing/running outfits, Business Types Table (key ability + prerequisites), Season Business rolls, Property Status Table (0–8, Capital cost), Location Table, Property Features Table, buying/selling/auctions.
- `01-corebook/06-life-in-the-old-west.md:488-617` — **Gear & Services**: Availability/Supply table (Common/Uncommon/Rare/Very Rare); settlement modifiers (Mercantile/Railroad/amenities/Law/Welfare shift availability); **Strong Markets** (Mercantile 5–6, or 4 + Railroad); **Scarcity and Price** table (−25% surplus … +100%+ panic); **Quality Grades** (Poor −25% / Worn −10% / Standard / Fine +50%); General Gear; Specialized Gear.
- `01-corebook/06-life-in-the-old-west.md:619-687` — Services; Specialist Services; **Hired Hands and Day Labor** (per-day wages).
- `01-corebook/06-life-in-the-old-west.md:689-709` — **Optional Module: Consumables as Resource Dice** (D12 abundant → D4 desperate; roll on meaningful use; 1–2 steps down; D4 rolling 1–2 = exhausted).
- `01-corebook/06-life-in-the-old-west.md:711-905` — **Weapons**: Weapon Features (SINGLE/DOUBLE/LEVER/BREECH actions; Draw Mod; Attack Mod; Damage; Crit; Range; Ammo); Revolvers/Pistols, Rifles/Shotguns/Bows, Melee tables; **Weapon Qualities** (Ranged: CALIBRATED/CONCEALABLE/FANNING/FAST DRAW/HEAVY/HIDDEN/HOT LOADER/LIGHT/LONG BARREL/SHORT BARREL/SIGHTS/SAWN-OFF + Any: BALANCED/MAINTAINED/PIERCING/POWERFUL/RELIABLE; Melee: BALANCED/FORGIVING/MOUNTED/PIERCING/SHARPENED/SLEEK/TOUGHENED/WEIGHTED); max four qualities, stack; **Weapon Conditions** (Ranged D6: DIRTY/DAMAGED BORE/HARD TO LOAD/GREASY/MISALIGNED/WEAK HAMMER; Melee D6: BLUNT/LOOSE HANDLE/BENT/HARD TO HOLD/CHIPPED/WEAKENED) — Trouble-driven degradation, repairable by a Shift of gunsmith/smith/bowyer MAKIN'.

## 2. Abstraction target

Abstract **gear and economy** as a genre-neutral system of *five separable layers*, each a design choice, with FL and West as two calibrated points:

1. **Availability / Scarcity** (§3) — a rating that controls *whether* an item can be found in a given settlement, and a price-adjustment table for *how the market bends the cost*. Both games ship near-identical machinery here.
2. **Economy model** (§4) — the *form money takes*: barter+commodity-currency (FL) vs cash+capital with credit and wages (West). This is the file's **central divergence**.
3. **Crafting / the making layer** (§5) — *who can make what, where, in how long, from what*. Talent-gated, workshop-gated, time-gated, material-gated.
4. **Feature grammar** (§6–7) — **the central reusable artifact.** Weapons and armor are defined by a *small set of composable tags* (Edged, Pointed, Polearm, Parrying, Pierce Armor… / CALIBRATED, RELIABLE, PIERCING…) rather than by bespoke stat lines. The grammar is what lets two swords feel different without inflating numbers.
5. **Quality / condition / legendary tiers** (§8–9) — the *degradation and escalation* layers: quality tiers (Crude/Standard/Fine), condition tracks (Worn→broken), and the artifact/legendary die for gear so fine it has its own dice.

A sixth, cross-cutting rule pattern — **consumables as resource dice** (§10) — replaces item-counting with a single degrading die, and is the engine's preferred way to track *ammo, torches, food, tools* under pressure.

## 3. Supply / scarcity / availability tables — **shared near-verbatim**

Both games solve the same problem — *not everything is for sale everywhere* — with the same two-part machine: (a) a per-item **availability rating** that the GM rolls or judges against the settlement, and (b) a **price-adjustment table** for when scarcity bites. The machinery is nearly identical; only the *labels* and the *trigger* differ.

### 3.1 The availability ladder

| FL rating (`10-gear.md:13-19`) | West rating (`06-life:500-505`) | How it's resolved |
| --- | --- | --- |
| **Common** | **Common** | Generally available in any functioning settlement. |
| **Uncommon** | **Uncommon** | FL: roll D6, **4+** = 1D6 units available, weekly restock. West: needs a better town / the right business / time to ask around. |
| **Rare** | **Rare** | FL: D6 **6 only**, single unit, weekly. West: only in strong markets or via a named contact. |
| **Extremely Rare** | **Very Rare** | FL: D66 **65–66 only**, single unit, weekly. West: needs a major town, special amenity, mail order, or its own scenario. |

**Common pattern:** a 4-step ladder (Common → Uncommon → Rare → Very Rare) where each step *narrows where the item can be found* and *lowers the quantity restocked*. The resolution can be a die roll (FL's per-item D6/D66 with weekly restock) or a settlement-quality judgment (West's "does this town have the right amenity / Mercantile rank?"). **Layer:** General.

### 3.2 Settlement modifiers — availability shifts with place

**FL** folds settlement capacity into the economy prose: gold items become Extremely Rare + 1D6 weeks lead time in villages, and advanced-talent items (smith/bowyer/builder) may be unavailable outside towns/strongholds even on a successful supply roll. FL `10-gear.md:25, 28`.

**West** makes settlement capacity an explicit, combinable modifier set. Availability shifts **one step** up or down based on the town's tags (`06-life:507-516`): `Mercantile 1-2` → harder; `Mercantile 5-6` → easier; a `Railroad Station`/`Express Mail Route` → easier for legal manufactured goods (if you'll wait); a matching amenity (`Blacksmith`, `Doctor`, `Apothecary`, `Horse Traders`, `Attorney's Office`, `Federal Marshal's Office`) → easier for matching goods; `Law 5-6` → illicit goods harder or impossible openly; `Law 1-2` → illicit goods easier but fraud/theft likelier; `Welfare 1-2` → decent lodging/stabling/doctoring harder.

**West's "Strong Market" definition** (`06-life:526-541`): Mercantile 5–6, *or* Mercantile 4 + a Railroad/Express/major-trade advantage. In a strong market, Rare legal goods are openly buyable, one Very Rare good can at least be *located/ordered* without a side-adventure, and the buyer chooses ordinary price *or* immediate access (immediate = +one scarcity step). Strong markets are also *bounded*: two Rare purchases of one kind per week, one Very Rare, before the shelves thin and further same-kind purchases step harder.

**Common pattern:** the settlement is itself a *rated supplier*. A small set of tags (trade rank, transport link, specialist amenity, law level, welfare level) each shift availability by one step and *stack*. A "strong market" threshold unlocks Rare/Very Rare access but is rate-limited per buyer per week. **Layer:** General (the modifier concept); the specific tag set is genre work.

### 3.3 The scarcity → price table

Once an item is *found*, both games bend the price by market condition. The two tables are functionally the same curve:

| Market condition | FL | West |
| --- | --- | --- |
| Surplus / desperate seller / hard competition | (scarcity inflation only goes *up* in FL) | **−25%** |
| Ordinary availability | listed price | listed price |
| One step scarcer than normal | +50% (FL's floor for found Rare/Extremely Rare) | **+25%** |
| Two steps scarcer | up to +200% | **+50%** |
| Barely obtainable / urgent demand / panic | up to +200% | **+100% or more** |

FL `10-gear.md:27` ("increase the price by 50% to 200% based on local need"); West `06-life:547-553`. West adds the explicit *downward* leg (−25% surplus) and the granularity of one-step-vs-two-steps; FL states only the upward range but permits barter-at-face-value or a service obligation as a non-cash substitute (`:26`).

**Common pattern:** a 5-row price-adjustment table keyed to *how hard it was to find* (surplus → panic), applied after the availability roll succeeds. **Layer:** General. *Recommended port:* West's version (it includes the downward leg, which makes trade feel two-sided).

## 4. Economy models: the economy choice — **the central divergence**

This is where FL and West diverge most sharply, because the two genres have *opposite relationships to money*. FL is a post-collapse survival setting where coin is scarce and most exchange is personal; West is a frontier-cash-economy setting where dollars flow, credit exists, and property is a game.

**Deep economy handoff:** this section identifies the economy model. When the task is to price new functions, build property, translate FL stronghold construction into West-style Capital/property, validate investment payback, or design business/amenity cost bands, continue to §12 of this file. When the task is to run businesses, factions, families, settlements, or other owned entities across weeks/months/seasons, load `25-season-downtime-and-enterprises.md`.

### 4.1 The choice

| | **FL — barter + commodity silver** (`10-gear.md:21-28`) | **West — cash + capital + credit + wages** (`06-life:11-125`) |
| --- | --- | --- |
| **Daily currency** | Silver and copper for ordinary goods; **barter at face value** or a service obligation substitutes for coin. | **Dollars** (cash) for ordinary goods and services. |
| **Prestige / large currency** | **Gold is ceremonial** — marks prestige and patronage, *not* daily trade. Gold-priced items need a sponsor, special order, or rare caravan; in a village treat as Extremely Rare + 1D6 weeks lead time. | **Capital** ($250 = 1 point) — money tied up in property, businesses, investments. *Cannot buy ordinary gear* unless liquidated. No upper limit. |
| **Liquidation** | (implicit: spend the silver, swap the barter) | **Liquidating Capital** is risky and committed: roll D6 × $50 = $50–$300, decided once rolled, lose the underlying asset. |
| **Credit / debt** | (none — no banking layer) | **Loans**: 5%–10% interest per season, ≥1-year term, collateralized (land/home/farm/business), foreclosure on default; banks are fragile (fraud, robbery). |
| **Income** | (earned ad hoc: looting, favors, strongholds) | **Salaries** per season (table, $65–$300); −25% if board included. Plus **business/season rolls** and **hired-hands** day-wages. |
| **Property / stronghold** | Stronghold building (raw materials + labor + time, `10-gear.md:700-714`). | **Property Status 0–8** (Capital-priced), **Location Types**, **Property Features**, buying/selling/auction rules (`06-life:214-351`). |
| **Thematic load** | *Scarcity is the story.* Geography and isolation decide what you can have. | *Money is the story.* Cash flow, debt, investment, and reputation-through-property drive play. |

**Common pattern — the economy choice.** A setting picks, from a small menu, *which forms of value exist and how they convert*:

1. **Medium of daily exchange** — barter / commodity coin / fiat cash / scrip.
2. **Prestige or large-denomination store** — ceremonial gold (FL) / investment Capital (West) / none.
3. **Credit** — none / seasonal-interest loans with collateral / full banking.
4. **Income stream** — ad hoc looting / seasonal salaries / business rolls / rents.
5. **Property model** — stronghold-as-craft-project (FL) / property-as-rated-asset-with-Status (West) / none.

Each is independently toggleable. **Layer:** the choice is **core**; each sub-choice is a design choice.

**Design intent:** The economy model is not flavour — it *is* the genre's statement about what characters are struggling for. FL's barter+ceremonial-gold says "you will mostly not have money, and the things you want will be gated by *who you know and where you are*." West's cash+capital+loans says "money is available, but it comes with *obligations* — debt, investment risk, reputation — that are themselves the drama." A new genre's job is to decide whether its characters are *starved* of money (use the FL pole) or *managed* by money (use the West pole).

### 4.2 West's capital machinery — the deeper simulation

West is the only one of the two with a full *asset-and-business* simulation, and it is worth abstracting because it generalizes to any genre where *owning things* should matter (noble houses, trading companies, criminal empires, starship fleets):

- **Capital converts one way at a fixed rate** ($250 → 1 Capital) **but liquidates at a random rate** (D6 × $50). This asymmetry — *easy in, risky out* — makes investment a genuine decision, not a savings account. `06-life:21, 49`.
- **Capital is locked to its purpose**: invested-in-a-business Capital stays Capital but must be liquidated to move it; you can't shift it directly between assets (except the one-time starting-outfit merger). `06-life:43, 141`.
- **Businesses are rated by a key ability + prerequisites**, run by a named proprietor, pay seasonal wages scaled by invested Capital (+5%/point after the first), and earn **Business Bonuses** only on 2+ success season rolls — failure imposes a **Business Penalty**, and reaching 0 Capital = **gone bust**. `06-life:155-210`.
- **Property is a Status ladder (0–8)**, each step a Capital price, with build-cheaper-than-buy (but build costs *time*), Location Types controlling availability/cost, and a Features table (Forge, Oven, Stables, Library, Strong Room…) that gates business types and grants rolling bonuses. `06-life:230-307`.
- **Buying/selling is a haggle**: opposed PERFORMIN' vs INSIGHT, ±1 Capital per net success (min ½, max +50%); competitive bidding can overshoot value and the excess is *lost*. `06-life:332-350`.

**Abstract pattern — "the asset layer."** A rule set where (a) a large-denomination currency converts in at a fixed rate and out at a random rate, (b) assets are rated by a linked ability and pay out on seasonal rolls, (c) owning property is a Status ladder with build-vs-buy trade-offs and prerequisite-gating features, and (d) transactions are haggle-able. **Layer:** Optional — include only in genres where *property and business* are intended to be a pillar of play. FL deliberately omits this entire layer (its "stronghold" is a craft project, not a financial instrument).

## 5. Crafting — the making layer

Both games gate *making things* behind the same four gates, in the same order: **you need the right skill/talent, the right workshop/tools, the right raw materials, and the right time.** FL exposes the full machinery in its gear tables; West folds most of it into the Availability/Quality system and the training rules. The structure is identical.

### 5.1 The four gates

| Gate | FL | West |
| --- | --- | --- |
| **Talent** | Every craftable item lists a **Talent**. No talent = the item is *simple* and anyone can make it; a listed talent (Smith, Bowyer, Tailor, Tanner, Builder, Chef, Poisoner, Lockpicker, Inventor…) makes it *advanced* and gates it. `10-gear.md:38`. Higher talent *ranks* unlock better materials and masterwork. `:741, 816-822`. | Crafting routes through the **MAKIN'** ability and the **smith/gunsmith/bowyer** talents; repairing weapon Conditions costs a Shift of effort by a talented character using MAKIN'. `06-life:846`. |
| **Workshop / tools** | Items list required **Tools** and sometimes a **Function** (forge, tannery, tailor shop, kiln, laboratory). **Missing the function/tool set = +50% time and −1 to the roll**; advanced items need a **specialist** present or they're impossible. `10-gear.md:40, 46-48`. | Outfits list **prerequisites** (a property *with a Forge*, *with an Oven*, farming land, a Claim, Stables…); without them the business roll suffers **−2**. `06-life:188, 605-613`. |
| **Raw materials** | Every item lists exact **Raw Materials** (½ Iron, 1 Wood, 2 Leather…) with fractional units; materials themselves are craftable (Iron Ore→Iron, Pelts→Leather, Wood, Stone, Glass…) and have their own supply/shelf-life. `10-gear.md:652-682`. | Gear is bought, not built from units, but the *Specialized Gear* table notes when equipment is prerequisite to a business (Farming/Mining/Panning equipment). `06-life:596-614`. |
| **Time** | Each item lists a **Time** (Quarter Day / One Day / Two Days / One Week…), assuming two Quarter Days of work per day; extra time = bonus to the roll. Large items (armor, crossbows, vehicles) need an **assistant**; each beyond the first shaves **25%** of time (min ½ at three). Armor needs **1–2 days fitting** (poor fit = −1 MOVE or −1 AR). **Seasonal work**: outdoor/heavy craft is +50% time in winter unless indoors. `10-gear.md:36, 50-54`. | Building property costs **seasons** of time (Status 3 = a season; Status 8 = four seasons). `06-life:232-242`. |

**Common pattern — "the making gate."** To make an item, satisfy four independent prerequisites — **talent, workshop, materials, time** — each of which can independently *block* the craft, *slow* it, or *penalize* the roll. Assistants and extra time are the two choices that trade resources for speed/quality. **Layer:** General (the four-gate structure); the depth of the material simulation is a choice (FL's unit-economy vs West's buy-it-ready-made). For cost bands, function value, construction curves, payback checks, and persistent-bonus pricing, load `27`.

### 5.2 The material-quality ladder (FL innovation)

FL alone makes *the material you make it from* a first-class choice. The metallurgy ladder (`10-gear.md:802-822`) is exemplary and generalizes: each step up the material ladder adds **+1 Weapon Bonus / Armor Rating** at the cost of a harder crafting roll (−2 to −6, halved by sufficient talent rank) and rarer supply:

| Material | Craft penalty | Effect | Talent floor |
| --- | --- | --- | --- |
| Iron (baseline) | — | — | — |
| Bronze/Brass/Silver | varies | can replace iron; masterwork capped at ½ bonus | varies |
| Wrought iron | −2 | +1 Bonus | Smith rank 2 halves penalty |
| Steel | −4 | +2 Bonus | Smith rank 3 halves penalty |
| Crucible steel | as steel + rare minerals | +2 Bonus, +1 MANIPULATION (beauty) | Smith rank 4 |
| Dwarven steel | −6 | +3 Bonus, rust-immune, tougher | Smith rank 4 halves penalty |

The same pattern repeats for leather/cloth (Buckskin / Wax-hardened / Glue-hardened / Glass-composite leather; Wool / Linen / Oilcloth / Silk / Silk-wool) and for alternative weapon materials (Bone = fragile; Flint = +1 damage). `10-gear.md:836-921`.

**Abstract pattern:** a *material ladder* where each tier trades crafting difficulty and scarcity for a +1 bonus, with a talent rank that halves the penalty — so *being a better craftsman literally lets you work better materials*. **Layer:** Optional (genre-dependent; include where *crafting depth* is a pillar — alchemy, cybernetics, starship components).

## 6. Weapon feature grammar — **the central reusable artifact**

> This is the file's key deliverable. The insight: **weapons are defined by a small set of composable tags, not by bespoke stat lines.** A longsword is not "a longsword" — it is `Edged, Pointed, Parrying, Half-Hand, Heavy` with Grip 2H, Bonus +2, Damage 3. Change one tag and you have a different weapon; the stat block barely moves.

### 6.1 The shared stat skeleton

Both games describe a weapon with a *fixed column write-up* plus a *free-form tag list*. The write-up holds the numbers; the tags hold the *feel*.

| Column | FL (`05-combat:449-461`) | West (`06-life:715-735`) |
| --- | --- | --- |
| **Grip / Action** | GRIP (1H/2H) | ACTION (SINGLE/DOUBLE/LEVER/BREECH/Special) |
| **Attack bonus** | BONUS (Gear Dice) | ATTACK MOD (+n to SHOOTIN'/FIGHTIN') + DRAW MOD |
| **Damage** | DAMAGE (Weapon Damage on hit) | DAMAGE RATING |
| **Critical** | (via surplus ⚔/Stunts) | CRIT RATING (stunts needed for a crit) |
| **Range** | RANGE (Arm/Near/Short/Long/Distant) | RANGE (Arm's Length/Near/Short/Long/Distant) |
| **Ammo** | (per weapon: Arrows/Quarrels/Stones…) | AMMO (capacity) |
| **Cost / Weight / Supply** | COST (silver) / WEIGHT / SUPPLY | COST ($) / WEIGHT / RARITY |
| **FEATURES / QUALITIES** | the tag list | the tag list (max 4, stack) |

The two write-ups are nearly isomorphic. The one structural difference: FL's BONUS is a pool of **Gear Dice** that *degrade when pushed* (a pushed roll drops the weapon's bonus by 1 per 💀 on a Gear Die, breaking it at 0) — so the weapon's potency is itself a depletable resource. West's ATTACK MOD is a flat modifier with no push-degradation; instead, weapons degrade via the **Condition** tables (§8) driven by Trouble. This mirrors the engine's core push-cost divergence (`00-engine-core.md` §6): FL's gear *is* the cost face; West's gear is taxed by a separate Trouble layer.

### 6.2 FL's feature set — the combat-action grammar

FL's tags are unusually well-designed because they **double as the action-prerequisite system**: a tag doesn't just describe the weapon, it *unlocks or gates a combat action*. This is the deepest version of the grammar and the one most worth porting.

| Tag family | Tags | What they do (FL `05-combat:472-536`) |
| --- | --- | --- |
| **Damage-type / crit-table selectors** | **Edged**, **Pointed**, **Blunt** | *Enable* SLASH (Edged/Blunt) or STAB (Pointed) and select the critical-injury *family* (`04-harm §5.2`: Slash / Stab / Blunt Force). This is the bridge between the feature grammar and the typed-crit-family engine. |
| **Reach / engagement** | **Short-reach**, **Long-Reach**, **Polearm**, **Half-Hand** | Decide who controls distance: Short-reach must be inside the foe's reach; Long-Reach fights from Near and forces a **CUT IN** roll; Polearm adds the haft-fighting fallback; Half-Hand lets a longsword shorten its grip one band. `05-combat:247-265, 496, 502, 518`. |
| **Defensive** | **Parrying** | Allows the PARRY reactive action; without it, weapon-parries are at −2. `:510`. |
| **Maneuver-enabling** | **Hook** | Enables the SHOVE action. `:492`. **Trapping** penalizes enemy PARRY/DISARM. `:532`. |
| **Anti-armor** | **Pierce Armor** (−3 to target's AR, min 1), **Smashing** (3+⚔ destroys 1 AR or damages the parrying weapon; counts ⚔ twice vs objects), **Armor Rating x2** (whip — target doubles AR). `:474, 512, 526`. |
| **Defense-piercing** | **Chained** (−2 to PARRY), **Flexible** (−1 to shield parry), **High-Velocity** (−2 to DODGE, melee-only parry). `:482-490`. |
| **Special damage** | **Burning** (3⚔ → target catches fire, 1 dmg/turn until MOVE roll), **Pick** (deals Stab damage on a Slash action). `:480, 514`. |
| **Size / handling flags** | **Light**, **Heavy**, **Tiny**, **Unarmed** | Reference flags for talents and rules (e.g. CRAMPED zones penalize Heavy; Heavy enables SWING WEAPON for +1🩸). `:488, 494, 530, 534`. |
| **Ranged-specific** | **Load / Load x2**, **Ready**, **Windlass**, **Ranged (Blunt/Pointed)**, **Melee/Ranged**, **Loud**, **Misfire**, **High-Velocity**, **Shield-breaker** | Reload action budget, the pre-shot READY action, crit-table selector for ranged, thrown-melee hybrids, animal-fright, the misfire self-damage risk. `:498-524, 536`. |
| **Durability** | **Brittle/Fragile** (item damage on any item-die 💀, even un-pushed; un-repairable), **TOUGH** (soaks the first damage, checkbox repairable). `05-combat:478, 540`. |

**The composability proof.** Compare three FL weapons from the same table (`05-combat:544-583`):
- **Dagger**: `Light, Edged, Pointed, Short-reach` — slashes *and* stabs, but must get inside reach.
- **Shortsword**: `Tough, Edged, Pointed, Parrying` — same damage types, can parry, soaks a hit, no reach weakness.
- **Halberd**: `Heavy, Pointed, Edged, Hook, Polearm, Long-reach` — controls distance, shoves, stabs, slashes, but is dead inside arm's length.

Same six columns; wildly different weapons — because the *tags* carry the meaning. This is the grammar's whole value.

### 6.3 West's quality/condition grammar — the modifier-stack model

West splits the tag concept into three explicit, separable layers (`06-life:842-905`):

1. **Features** (the stat-block columns: Action, Draw Mod, Attack Mod, Damage, Crit, Range) — the *numbers*, baked into the weapon. `:715-735`.
2. **Qualities** — *positive* tags a skilled maker can add or that come built-in; **max four, bonuses stack**. Split by weapon class: `:848-868` Ranged (CALIBRATED, CONCEALABLE, FANNING, FAST DRAW, HEAVY, HIDDEN, HOT LOADER, LIGHT, LONG BARREL, SHORT BARREL, SIGHTS, SAWN-OFF + the Any-cross-cut BALANCED/MAINTAINED/PIERCING/POWERFUL/RELIABLE); `:874-883` Melee (BALANCED, FORGIVING, MOUNTED, PIERCING, SHARPENED, SLEEK, TOUGHENED, WEIGHTED). Each is a one-line effect (CALIBRATED = +1 Attack; RELIABLE = Trouble −1 min 1; MOUNTED = free second push on horseback; TOUGHENED = can't be broken by Trouble).
3. **Conditions** — *negative* tags applied by Trouble, repairable. Ranged D6 (DIRTY, DAMAGED BORE, HARD TO LOAD, GREASY, MISALIGNED, WEAK HAMMER) and Melee D6 (BLUNT, LOOSE HANDLE, BENT, HARD TO HOLD, CHIPPED, WEAKENED). `:885-905`. The last row of each is the *break* threshold (WEAK HAMMER / WEAKENED: a second Trouble in the scene breaks it beyond repair).

**Common pattern — the three-layer tag model.** A weapon = (a) a **fixed stat block** + (b) a **stack of positive Qualities** (capped, trade-off-laden, maker-addable) + (c) a **stack of negative Conditions** (Trouble-driven, repairable, escalating to "broken"). This cleanly separates *what the weapon is* (stats), *what's good about it* (qualities), and *what's wrong with it right now* (conditions) — three things FL conflates into the single degrading Gear Bonus.

### 6.4 Generalizing the feature grammar — the recipe

> **Port this.** The grammar is more reusable than any stat line in either book.

**The fixed architecture (port as-is):**
1. **A weapon = a fixed column write-up + a tag list.** The write-up holds numbers (grip/action, attack bonus, damage, crit, range, ammo, cost, weight, supply). The tags hold *behavior*.
2. **Tags are small, composable, and each does exactly one thing.** Name the *behavior* (Edged = enables SLASH + selects Slash crits), not the *weapon* ("sword-like").
3. **Tags double as action prerequisites** where possible (FL's model): a tag *unlocks or gates a combat action* (Parrying → PARRY; Hook → SHOVE; Pointed → STAB). This binds the gear layer to the conflict layer (`03-conflict-and-combat.md`) and makes loadout a tactical choice.
4. **Cap and trade off positive tags** (West's max-4, stack rule) so optimization has a ceiling and every weapon has a *profile* rather than "all the good tags."
5. **Drive negative tags through the engine's existing failure layer** (FL: Gear-Die 💀 on push; West: Trouble), so degradation *reuses* the harm system rather than adding a new one. See §8.

**The genre choice — choosing the tag set:**
| Genre | Recommended tag families |
| --- | --- |
| **Dark fantasy / survival** (FL) | Damage-type (Edged/Pointed/Blunt), reach (Short/Long/Polearm/Half-Hand), defensive (Parrying), maneuver (Hook/Trapping), anti-armor (Pierce/Smashing), special (Burning), durability (Brittle/TOUGH). |
| **Historical firearm** (West) | Action (Single/Double/Lever/Breech), draw/attack/damage/crit/range stats, Qualities (Calibrated/Reliable/Concealable/Fanning/Mounted…), Conditions (Dirty/Bent/Chipped…). |
| **Modern/sci-fi** | Port West's three-layer model; add tags for smart-link, recoil, armor-piercing ammo-types, overheating, electronic-jamming Conditions. |
| **Any** | Always include a *damage-type selector* family (so the weapon picks its crit table — see `04-harm §5`) and a *reach/engagement* family (so loadout controls distance). |

## 7. Armor feature grammar

Armor is the quieter sibling of the weapon grammar: fewer tags, but the same *composable-tag* philosophy. Both games model armor as **a Gear Bonus that rolls against incoming damage and degrades when penetrated**.

### 7.1 FL armor — rating + features + degradation

FL armor (`05-combat:650-727`) has an **Armor Rating** (AR): when you take physical 🩸, roll AR Gear Dice; each 💀 reduces damage by 1. **If any damage penetrates, the armor's AR drops by 1 per 💀 rolled** (if it absorbed everything, no degradation). Armor is *repaired* with CRAFTING. Helmets add their AR to body armor and grant a crit-saving grace: on a lethal head crit, roll the helmet's AR in Gear Dice — a 💀 downgrades it to a minor blunt-force hit (but ruins the helmet). `:654-660`.

Armor "features" in FL are mostly **stat annotations** rather than a separate tag grammar: `Light`/`Heavy` (weight, with Heavy imposing MOVE/STEALTH penalties), `Cover 6` (tower shield when set), "Roll half rating vs stabs/arrows" (chainmail), "Modifies MOVE by −2" (plate), "Modifies SCOUT by −2" (great helm). The one true *feature* tag is **TOUGH** (`05-combat:540`): the item soaks the first damage it receives, repairable like a Gear Die — a durability tag that also appears on some weapons (Shortsword, Battleaxe, Halberd…).

### 7.2 West armor

West's harm model (`04-harm`) doesn't use a rolling AR; armor functions through the weapon Qualities/Conditions and the Hurts/Shakes damage split. Armor appears mainly as *protective gear* and *specialized equipment* in the gear tables, and the same Quality-Grade ladder (Poor/Worn/Standard/Fine) applies to it as to any goods. The degradation grammar is the Conditions layer (§8).

**Common pattern — "armor-as-tag-set."** Armor = (a) a **protection value** that either *rolls dice* against damage (FL) or *grants flat reduction/modifiers* (West), (b) a small set of **feature tags** for weight class, mobility cost, sense penalty, and special protection (cover, half-rating-vs-X), and (c) a **degradation rule** tied to the engine's harm layer. **Layer:** General. *Recommended port:* FL's rolling-AR-with-degradation is the more tactically interesting model and pairs naturally with the push-cost loop (a pushed attack can shred armor); use West's flat-reduction model for faster, lighter combat.

## 8. Quality tiers and condition/degradation

Both games layer a **quality** axis and a **condition/degradation** axis on top of the feature grammar. The two axes answer different questions: *how well was it made?* (quality, mostly fixed) vs *what shape is it in right now?* (condition, dynamic).

### 8.1 The quality ladder

| Tier | FL (`05-combat:462-470`) | West (`06-life:561-566`) |
| --- | --- | --- |
| **Low** | **Crude**: −1 BONUS (min +0); **breaks if Gear Bonus hits 0**; makeable with minimal facilities. | **Poor** (−25%): shoddy/second-hand; GM may rule it becomes Worn on first hard push. **Worn** (−10%): used hard but serviceable, one step closer to failing. |
| **Standard** | **Standard**: table as written. | **Standard**: listed price, solid frontier quality. |
| **High** | **Fine/Masterwork**: +1 BONUS, ×2+ cost, supply one step rarer; +1 MANIPULATION as a displayed status symbol; needs a specialist + proper tools. | **Fine** (+50%): better made/looking/resellable; counts as the one applicable +1 gear bonus *or* ignores the first Worn result from hard use (chosen when bought). |

The ladders align almost perfectly: Crude↔Poor, Standard↔Standard, Fine↔Fine. FL's Fine is in the rules stronger (+1 Gear Die, which is a real combat bonus); West's Fine is more *socially/economically* loaded (resale, the one-gear-bonus cap). West uniquely splits the low tier into **Poor** (badly made) and **Worn** (used hard) — distinguishing *origin* quality from *acquired* wear.

FL also applies quality to **rope and textile** separately (`10-gear.md:146-156`): Rough (½ lifespan, −25%, damages on 2💀/tears on 3💀) / Standard / Fine (double lifespan, +50%, doesn't wear from normal strain) — a model for any *consumable-adjacent* gear where lifespan, not performance, is the axis.

**Common pattern:** a 3-tier (or 4-tier) quality ladder where the low tier *breaks or fails first*, the high tier *adds a bonus and costs more + is rarer*, and the high tier optionally carries *social* value (MANIPULATION/resale/Fame). **Layer:** General (the ladder); whether the high tier grants a *combat* bonus (FL) or a *social/economic* one (West) is a choice.

### 8.2 The condition/degradation engine

This is where the two games diverge in *rule pattern* while agreeing in *effect* — and the divergence tracks the core push-cost split (`00-engine-core.md` §6):

| | **FL — gear-as-cost-face** | **West — Trouble-driven Conditions** |
| --- | --- | --- |
| **Trigger** | Pushing a roll: each 💀 on a **Gear Die** drops the weapon/armor bonus by 1. Also: armor penetrated by damage loses 1 AR per 💀 rolled. | Trouble generated by rolled `1`s (the failure-pressure layer, `00 §10`); also the "becomes Worn on first hard push" Quality rule. |
| **Effect** | The Gear Bonus *degrades in real time during a fight*; at Bonus 0 the item is **broken** and needs CRAFTING to fix. | A Condition tag is applied (DIRTY/BENT/CHIPPED…), each a discrete penalty; repairable by a Shift of talented MAKIN'. |
| **Granularity** | Continuous (a counter ticking down). | Discrete (a named tag from a D6 table). |
| **Climax** | Broken at 0. | "Broken beyond repair" if Trouble strikes twice in one scene (WEAK HAMMER / WEAKENED). |

FL `05-combat:456, 654-656`; West `06-life:846, 885-905`.

**Common pattern — "the degradation layer."** A rule that *using gear under pressure makes it worse*, wired into the engine's existing failure rule (push-cost in FL, Trouble in West) so no new rule set is needed. Choose **continuous-counter** (FL: bonus ticks down, repairs restore it) for granular, attritional pressure where gear *is* a resource pool; choose **discrete-tag** (West: named Conditions from a table, each a fixed penalty) for lighter bookkeeping and more *narrative* breakage ("the bore's damaged, it's low-powered"). **Layer:** General (some degradation rule); the rule pattern is a choice tied to the push-cost model.

## 9. Artifact / legendary gear and the artifact die

FL alone has a **legendary tier** — gear so fine it doesn't roll normal Gear Dice, it rolls its *own* larger die. This is the gear-layer instance of the engine's escalating-success-die rule set (`00-engine-core.md` §9).

### 9.1 The artifact die

FL artifacts grant a **D8 (Mighty) / D10 (Epic) / D12 (Legendary)** in addition to (or instead of) normal Gear Dice, read as **6+ = ⚔ with scaled multi-successes** (a D12 can yield up to 4 ⚔ on a 12). The bonus is rolled on the Artifact Bonus table (D66: 11–46 = D8, 51–63 = D10, 64–66 = D12). FL `10-gear.md:961-967`. **Artifact dice are never degraded by wear** — legendary gear is immune to the §8 degradation economy. `00-engine-core.md §9`. The artifact die is also a *craftable* ingredient for permanent magic items: a D8/D10/D12 artifact die costs 1/2/3 Power Levels (min total item PL 2/4/8). FL `07-magic.md:480`.

### 9.2 The artifact as a *named, oddity-bearing* object

FL artifacts are not just "a +2 sword." They are **named** (D66 prefix table: "Alur's…", "Brambolo's…"), **typed** (Skill artifact = adds the die to a skill; Combat artifact = weapon/armor/shield), and **oddity-laden** — every artifact carries a D66 **Oddity** that afflicts or aids the bearer only while possessed (`10-gear.md:1067-1106`): demonic faces that watch you, paranoid whispers, always-freezing cold, nightmares, telepathic complaint, the die that *varies by moon/season/time-of-day* (rows 64–66), the soul trapped inside whose personality bleeds into the bearer (row 33), the "discharge all power once, then explode" self-destruct (row 63).

**Abstract pattern — "the legendary tier."** An optional top tier of gear that (a) uses the **escalating-success-die** (D8/D10/D12, 6+ = ⚔, scaled, immune to degradation), (b) is **named and typed** rather than generic, and (c) carries a **quirk/oddity table** that makes possession itself a story — the item is *wanted and feared*, not just powerful. **Layer:** Optional — omit for grounded/low-power genres (West has no equivalent; its nearest analogue is the Faith, a player-side pressure-relief choice, not a success-scaling die). Cross-ref `05-power-layer.md` (artifact dice as magic-item ingredient) and `00-engine-core.md §9` (the die itself).

## 10. Consumables as resource dice

The engine's preferred solution to *tracking ammo, torches, food, feed, oil, medical supplies, tools* under pressure is not to count units — it is to assign the consumable a **Resource Die** that *degrades on use*. This is the consumables analogue of the push-cost loop: each use is a small gamble.

### 10.1 The resource-die ladder

Both games use the same ladder, just at different defaultness:

| Die | State | FL context | West context |
| --- | --- | --- | --- |
| **D12** | abundant | — | abundant |
| **D10** | sound | — | sound |
| **D8** | running down | `Makeshift Tools` ship at D8 (`10-gear.md:105, 164`) | running down |
| **D6** | low | (common starting point for Arrows/Torches/Food) | low |
| **D4** | desperate | — | desperate |

**The rule:** roll the die when the supply is *meaningfully used*. On **1–2**, step the die down one size. If a **D4** rolls 1–2, the supply is **exhausted**. One purchased unit usually raises a depleted supply by one step; a full resupply (wagon, pack train, town) raises it two steps or restores D12. West `06-life:701-709`; FL `10-gear.md:164-168` (Makeshift Tools: roll after hard use, 1–2 = spent, broken at lost die).

FL applies resource dice as the **default** tracking for adventure consumables: Arrows ("Increases the Arrows Resource Die by one step," `:91`), Torches (D6, rolled each turn/15 min, `:99`), Food/Field Rations (`:112`), and Makeshift Tools (D8, `:105`). The gear tables are explicit that buying/crafting one unit *steps the die up*, not "adds N arrows."

West ships the same machinery as an **Optional Module** explicitly recommended for "remote expeditions, outlaw flight, mountain crossings, cavalry patrols, and bad-country survival" — and defaults to *loose counting* for ordinary town-centered play. West `06-life:689-709`. The trigger cadence is spelled out: once/day for trail food/feed/oil on a hard journey; once/scene of heavy firing for loose ammo; once/day of rough doctoring for medical supplies.

### 10.2 Why it works — and when to default it

**Common pattern:** a *single degrading die* replaces a unit-count for any consumable the genre wants to feel *scarce under pressure*. It converts "I have 14 arrows" into "my Arrow Die is D6, and every fight might shrink it." It is lighter than counting, more dramatic than tracking, and it makes *resupply* a meaningful event (stepping the die back up) rather than bookkeeping. **Layer:** Optional in West, default in FL — a **scope choice**. *Default it on* for survival/wilderness/expedition genres where logistics is a pillar; default it *off* (loose counting) for urban/cinematic genres where supply runs aren't the story. Either way, port the ladder as-is. For transport requirements, group stores, stockpiles, and the no-double-charge rule, load `26`.

## 11. Inventory, Transport, and Storage Pressure

> This section consolidates the former standalone inventory/transport/storage chapter into the gear and economy chapter. Inventory is not a separate system in the architecture; it is the physical pressure layer of gear, consumables, transport, and stockpiles.

### 11.1 The Core Thesis

Inventory matters only when it changes decisions. YZE's carry system works because it is row-based, visible, and tied to exertion rather than arithmetic weight.

**The invariant spine:**

- one item row = one ordinary carried thing;
- base carry = primary physical attribute x2;
- heavy/light/tiny modify row use;
- containers extend capacity but introduce access, hand, and stealth/movement costs;
- over-carrying is allowed but taxed when the character acts under strain;
- consumables can become Resource Dice when counting would become busywork;
- stockpiles require transport or storage and should not fit invisibly in a backpack.

**FL pole:** inventory is expedition pressure. Backpacks and sacks are explicit, consumables default to Resource Dice, raw materials have shelf lives and transport costs, and stronghold functions create storage infrastructure.

**West pole:** inventory is frontier pragmatism. Base carry is still row-based, but ordinary town play counts loosely; Resource Dice are optional for hard-country pressure, and group stores are tied to pack animals, wagons, carts, and upkeep.

### 11.2 The Personal Inventory Model

#### 3.1 Row-Based Carry

| Element | FL | West | Abstract pattern |
| --- | --- | --- | --- |
| Sheet rule | one item per row; if not listed, not carried | one item per row; horse/wagon sheet if carried for you | inventory is a written-state contract |
| Base limit | Strength x2 | Grit x2 | primary physical attribute x2 |
| Damage effect | use base Strength, not damaged current rating | use base Grit, not damaged current rating | carry capacity is stable during injury |
| Heavy | counts as 2+ rows | counts as 2, 3, or 4 rows | heavy items consume multiple rows |
| Light | half row | half row or quarter row | small useful items share rows |
| Tiny | no encumbrance, still listed | no gear row, still listed elsewhere | tiny items must exist on sheet but do not tax carry |

**Generic rule:** A character can carry normal items equal to **primary physical attribute x2** without strain. A Heavy item counts as 2 rows by default. A Light item counts as 1/2 row. A Tiny item does not count against the limit, but must still be listed if it matters.

**Design intent:** row inventory is legible at the table. It makes "what did you bring?" a pre-adventure decision and prevents retrospective gear creation.

#### 3.2 Inventory Grain

Use three grains:

| Grain | Use for | Example |
| --- | --- | --- |
| Personal row | gear a PC can use in a scene | sword, lantern, doctoring bag, rope |
| Resource die | many small uses under pressure | arrows, food, water, feed, lamp oil, medical stores |
| Stockpile/store | bulk goods needing transport/storage | wagon of grain, stone, timber, gang provisions, stronghold stores |

**Rule:** Never track the same thing at two grains as a cost. If gang upkeep covers ordinary food, a Provisions die should model shortage under pressure, not another food bill. West states this explicitly for outlaw gangs.

### 11.3 Container and Access Rules

FL makes containers matter in the rules; West mostly lets horse/wagon carriage handle bulk. The FL container pattern is the stronger generic tool.

| Container | Capacity effect | Access / hand cost | Penalty | Use when |
| --- | --- | --- | --- | --- |
| No container | base physical x2 | worn/wielded/belt items only | none | danger-ready loadout |
| Travel backpack | capacity to x3 | worn; can remove or hold with two hands | -1 MOVE/STEALTH above x2 | expedition default |
| Large backpack | capacity to x4 | worn; removing negates penalty | -1 above x2, -2 above x3 | heavy expedition, slow travel |
| Sack | +2 rows | requires one free hand | -2 MOVE/STEALTH while carried | loot, temporary haul |
| Large sack | +4 rows | requires two hands | -3 MOVE/STEALTH when full | bodies, bulky loot, desperate haul |
| Saddle bags / pack saddle | mount storage | tied to animal | access requires mount | travel storage |
| Cart/wagon/boat | party storage | needs vehicle/animal/water/road | mobility and concealment costs | bulk stores |
| Stronghold storage | campaign storage | location-bound | vulnerable to events | stockpiles, wealth, materials |

**Access rule:** A thing in hand, worn, or on the belt is combat-accessible. A thing in a backpack, saddle bag, wagon, or storage is carried but not instantly accessible unless the table spends time or an action.

**Container design test:** every capacity increase must introduce one of: hand occupancy, action cost, stealth/movement penalty, transport dependency, or vulnerability to theft/loss.

### 11.4 Over-Encumbrance and Exertion

Both games allow characters to carry too much, but tax exertion.

**Generic over-carry rule:** A character may temporarily exceed their normal limit. When they run, hike, walk a significant distance, climb, flee, fight under load, or do anything strenuous, roll the physical endurance skill.

- On success: continue.
- On failure: choose one:
  - drop enough load to become legal;
  - stop moving or fail to act;
  - take 1 point of physical/mobility damage and continue.

**FL calibration:** roll Endurance when running in combat or hiking for a Quarter Day; failure can deal 1 Agility damage.
**West calibration:** roll Resilience when running, walking significant distance, or doing strenuous work; failure can deal 1 Shakes.

**Design rule:** over-carrying should be allowed. The interesting decision is not "you cannot," but "you can, if you accept risk at the moment of strain."

### 11.5 Mounts, Pack Animals, Carts, Wagons, and Boats

#### 6.1 Transport Scale Ladder

| Transport | Generic capacity role | Risk |
| --- | --- | --- |
| Riding mount | personal overflow; speed | injury, lameness, spooking, feed |
| Led mount / pack animal | doubled animal carry; supplies | slower, vulnerable, needs handling |
| Cart / handcart | low-cost bulk haul | roads/terrain, concealment, breakdown |
| Wagon | party/group stores | draft animals, roads, pursuit burden |
| Boat/canoe/rowboat | water-route cargo | route dependency, weather, portage |
| Stronghold/warehouse/vault | long-term stockpile | theft, siege, events, distance |

**Core rule:** Animals carry physical attribute x2, doubled when led rather than ridden. Use this as the personal-to-party transport bridge.

#### 6.2 Group Stores and Transport Requirement

West's outlaw Provisions table is the clearest YZE source for bulk consumables. Generalize it as follows:

| Shared store die | Small party / crew | Gang / company | Large outfit |
| --- | --- | --- | --- |
| D6 | saddle bags, spare pack saddle | one pack animal or handcart | two pack animals or cart |
| D8 | one pack animal | two pack animals or light wagon | four pack animals or wagon |
| D10 | two pack animals or light cart | four pack animals or wagon | eight pack animals or two wagons |
| D12 | three pack animals or wagon | six pack animals or two wagons | twelve pack animals or three wagons |

If transport is lost, abandoned, stolen, lame, burned, or impossible to move through the terrain, the store die cannot stay high. Step it down immediately or at the next meaningful strain.

**Design intent:** high supplies are not invisible. D10/D12 stores create safety but also create a footprint: pack animals, carts, wagons, roads, tracks, guards, and feed needs.

### 11.6 Consumables as Resource Dice

#### 7.1 The Ladder

| Die | State |
| --- | --- |
| D12 | abundant |
| D10 | sound |
| D8 | running down |
| D6 | low |
| D4 | desperate |
| exhausted | gone |

**Rule:** Roll when the supply is meaningfully used. On 1-2, step down one die size. If D4 rolls 1-2, the supply is exhausted.

#### 7.2 Roll Cadence

| Consumable | FL-style cadence | West-style cadence | Use when |
| --- | --- | --- | --- |
| Food/water | daily journey checklist | hard journey / rough living | survival is active |
| Arrows/ammo | after meaningful combat/use | scene of heavy firing | ammunition pressure matters |
| Torches/oil | each turn / meaningful light use | day or scene of rough use | darkness matters |
| Medical supplies | after hard use | day of rough doctoring | treatment resources matter |
| Feed | daily travel / hard country | when grazing is poor or group is cut off | animals matter |
| Tools | after hard use | after hard project | tool degradation matters |

**Defaulting rule:** FL-style survival games default Resource Dice on. West-style town/cinematic games default them off until the table enters hard-country, outlaw-flight, military-patrol, expedition, winter, siege, or survival mode.

#### 7.3 Resupply

| Resupply | Effect |
| --- | --- |
| one purchased unit / small restock | step depleted die up one |
| proper town resupply | step up two or restore D12 if ordinary |
| wagon/pack train/strong refuge | restore D12 if transport is adequate |
| forage/hunt/craft | step up by success, capped by terrain/season |

**No double charge:** If a lifestyle/upkeep/seasonal expense already pays for ordinary food, do not also roll a Resource Die for ordinary meals. Roll the die only when scarcity is a scene pressure.

### 11.7 Stockpiles, Stores, and Bulk Goods

#### 8.1 When Personal Inventory Becomes Stores

Convert to Stores when any of these are true:

- it cannot be carried by one person in rows;
- it is meant to last multiple days for a group;
- it is raw material for construction/crafting;
- it needs a wagon, pack animals, room, cellar, warehouse, vault, stable, granary, or similar function;
- it is valuable enough that theft/security matters;
- it has shelf life or spoilage.

#### 8.2 Store Types

| Store | Source calibration | Design use |
| --- | --- | --- |
| Food/feed | FL consumables, West Provisions | survival, animal upkeep, siege, winter |
| Raw materials | FL wood/stone/iron/leather/cloth | crafting and building |
| Trade goods | West pelts, gold, whiskey, gear | commerce and theft |
| Secure valuables | FL Vault, West Strong Room | crime, robbery, investment |
| Perishables | FL shelf life, cellar/granary | weather, season, spoilage |
| Equipment pools | West farming/mining/panning equipment | business prerequisites |

#### 8.3 Storage Functions

| Function | Abstract effect |
| --- | --- |
| Granary / Root Cellar | extend shelf life; prevent spoilage |
| Warehouse | hold trade goods and enable market access |
| Vault / Strong Room | protect valuables from theft |
| Stables / Barn | house animals, feed, tack, wagons |
| Forge / Workshop / Tailor Shop | convert materials into crafted goods |
| Field / Garden / Pasture / Mine / Quarry | produce recurring materials |

**Design rule:** if a campaign cares about bulk materials, it must care about storage. Otherwise raw materials become weightless points.

### 11.8 Crafting/Building Material Flow

Use this flow for any game with crafting, construction, or enterprise supply:

1. **Acquire:** buy, harvest, mine, hunt, loot, claim, trade, or produce.
2. **Transport:** carry, mount, cart, wagon, boat, caravan.
3. **Store:** personal rows, pack stores, warehouse, cellar, vault, field, stable.
4. **Preserve:** shelf life, spoilage, weather, theft, rats, fire.
5. **Convert:** craft item, build function, pay upkeep, resupply Resource Die.
6. **Expose:** transport and storage create hooks: theft, damage, delay, inspection, siege, debt.

**Source proof:** FL raw materials have shelf lives and production functions; FL stronghold functions store and convert them. West property/business equipment creates prerequisites and penalties; outlaw provisions require visible transport.

### 11.9 Rule choices

| Choice | FL pole | West pole | Generic choice |
| --- | --- | --- | --- |
| Inventory detail | strict rows + containers | strict rows but lighter container detail | row strictness |
| Consumables | Resource Dice default | Resource Dice optional | survival default |
| Container depth | backpack/sack thresholds | horse/wagon carriage | personal vs transport detail |
| Over-carry tax | Endurance on run/hike | Resilience on strenuous action | trigger frequency |
| Group stores | stockpiles/functions | provisions die + transport table | bulk abstraction |
| Storage | stronghold functions | property/hideout/wagon | location-bound assets |
| Spoilage | shelf life explicit | mostly event/lifestyle based | perishability depth |
| Transport burden | mounts, animals, wagons | horses/wagons central | pursuit/concealment pressure |
| Gear access | worn/wielded/container | listed on person/horse/wagon | action cost to retrieve |

### 11.10 Resolution Checks

Use these checks when designing a new inventory or logistics rule.

#### Carry Check

- What is the base carry formula?
- What counts as Heavy, Light, Tiny?
- Does the system require written rows?
- What happens when the PC exceeds the limit?
- Which action triggers the exertion roll?
- What attribute damage/condition lands on failure?

#### Container Check

- How much capacity does the container add?
- Does it occupy hands?
- Does it impose MOVE/STEALTH or equivalent penalties?
- Is gear inside accessible in combat?
- Can it be dropped quickly?
- Can it be damaged, stolen, or lost?

#### Transport Check

- What die/stockpile level does the party claim?
- What animal/cart/wagon/boat infrastructure justifies it?
- What terrain blocks or taxes that transport?
- What happens when transport is lost?
- Does transport create a footprint for pursuit, concealment, or events?

#### Consumable Check

- Is the consumable scene-pressure or lifestyle/upkeep?
- If lifestyle/upkeep pays for it, do not also roll the die.
- What is the roll cadence?
- What restores one step?
- What restores D12?
- What happens at D6, D4, exhausted?

#### Storage Check

- Where is the stockpile?
- Who guards it?
- What preserves it?
- What events threaten it?
- What does it convert into?

### 11.11 Validation and Failure Modes

| Failure mode | Symptom | Fix |
| --- | --- | --- |
| Invisible bulk | players carry wagon-scale material in personal rows | require transport/storage threshold |
| Double charging | same food paid by lifestyle and resource die | pick one pressure grain |
| No access cost | backpack contains instant combat gear | define action/time to retrieve |
| Container with no downside | capacity increase is always optimal | add penalty, hand cost, or theft risk |
| Resource die spam | rolling every trivial use becomes noise | roll only on meaningful use/cadence |
| Transport ignored | D12 provisions have no animals/wagons | require transport ladder |
| Storage invulnerable | stockpiles cannot be stolen/spoil/burn | add events, guards, functions |
| Inventory as punishment | load rules only say "no" | allow over-carry with exertion choice |

### 11.12 Instantiation Recipe

1. **Choose the physical attribute.** Strength, Grit, Body, Might, Load, Hull, etc.
2. **Set base carry = attribute x2.** Change only if the game intentionally wants very light or heroic load.
3. **Define Heavy/Light/Tiny.** Keep row math simple.
4. **Choose container depth.** FL-style backpacks/sacks for expedition games; West-style horse/wagon carriage for frontier/cinematic games; both for logistics-heavy games.
5. **Set the over-carry trigger.** Run/hike/strenuous work is the default.
6. **Choose Resource Dice default.** Default on for survival; optional for town/cinematic play.
7. **Write the transport ladder.** Say what supports D6/D8/D10/D12 group stores.
8. **Define storage functions.** Cellar/granary/vault/warehouse/stable/workshop equivalents.
9. **Map crafting materials to stores.** Personal rows are for tools and small inputs; bulk raw materials are stores.
10. **Validate:** no invisible bulk, no double charge, no free capacity, no invulnerable stockpile.

**Final acceptance test:** after preparing for an expedition or season, the players should know what is on their bodies, what is on the animals/vehicle, what is in storage, what can run out, and what must be protected.


## 12. Crafting, Construction, and Investment Economics

> This section consolidates the former standalone crafting/construction/investment chapter into the gear and economy chapter. Crafting, stronghold functions, property features, Capital, and business investment are the long-form economy of gear and assets. For period turns and enterprise management, use `25-season-downtime-and-enterprises.md`.

### 12.1 The Core Thesis

YZE economics are not about simulating a market. They are about making long-term choices carry forward.

**FL says:** if you want a capability, you must find the place, materials, labor, time, and skilled hands to build it. The payoff is usually a function: crafting access, storage, food production, defense, recruitment, healing, travel, market access, or Willpower/Faith support.

**West says:** if you want position, you must tie money into assets and accept illiquidity, debt, reputation, business risk, and seasonal fortune. The payoff is cash flow, wages, dividends, property status, town growth, and social leverage.

The agnostic YZE economy must therefore distinguish:

1. **liquid spending** for gear and services;
2. **bulk materials** for making/building;
3. **illiquid investment** for assets and businesses;
4. **period income/upkeep** for long-term play.

If a design collapses these into one money pool, it loses the FL/West tension: scarcity vs investment.

### 12.2 Four Economies, Not One

| Economy | FL expression | West expression | Design use |
| --- | --- | --- | --- |
| Liquid cash | copper/silver; barter; gold ceremonial | dollars | gear, services, wages, lifestyle |
| Bulk materials | wood, stone, iron, leather, food, raw materials | property/build costs abstracted into cash/Capital | crafting and construction |
| Illiquid assets | stronghold functions and buildings | Capital, property Status, business stake | long-term ownership |
| Period flow | weekly upkeep, function production, hireling pay | season wages, business rolls, loans, lifestyle, town fortune | campaign pressure |

**Design rule:** choose which economy a cost belongs to before pricing it. A forge built from stone/iron/time is not the same design object as a $100 property feature named Forge, even though both unlock smithing play.

### 12.3 Crafting Gates

FL provides the cleanest crafting abstraction. Use its four gates as the default.

| Gate | Source expression | Generic use |
| --- | --- | --- |
| Talent / expertise | simple vs advanced; specialists required for advanced work | who can attempt it |
| Workshop / tools / function | forge, workshop, tailor shop, tannery, etc.; missing function = +50% time and -1 | where it can happen |
| Materials | fractional units, bulk units, quality tiers, shelf life | what it consumes |
| Time / labor | two Quarter Days/day; assistants reduce time; winter slows outdoor heavy work | how long the opportunity cost lasts |

#### 4.1 Crafting Result Model

Use this when abstracting new craftables:

1. **Define the output:** item, repair, component, function, quality upgrade, stockpile conversion.
2. **Assign complexity:** simple / advanced / masterwork / legendary.
3. **Set required gate:** no talent / talent / rank floor / specialist / rare function.
4. **Set material grain:** personal material / bulk store / rare ingredient / Capital-equivalent asset.
5. **Set time:** scene / Quarter Day / day / week / month / season.
6. **Set roll:** physical craft skill + tools/function + help.
7. **On failure:** no retry until skill improves for major construction, or add flaw/delay/material loss for ordinary work.

#### 4.2 Crafting Benchmark Table

| Output | Gate | Time | Cost grain | Effect ceiling |
| --- | --- | --- | --- | --- |
| simple repair | tools | Turn/Shift/Quarter Day | minor materials/cash | restore function/item |
| ordinary item | skill + tools | Quarter Day to day | row-scale materials | listed gear |
| advanced item | talent + function | day to week | specific materials | gear bonus/tag |
| large item | talent + assistant | week | bulk materials | vehicle/armor/crossbow |
| masterwork | high talent + rare material + function | week+ | rare materials | +1 die/tag/social value |
| function | Builder/craft + materials | days to month | bulk materials | persistent capability |
| building | Builder + crew + tools | month to years | huge bulk materials | Housing/status/base |
| magical/legendary item | power layer + artifact die/rare ingredient | project/season | rare resource + risk | escalating-success die/oddity |

**Validation gate:** a persistent broad +1 die should require at least three gates: expertise, proper function, and meaningful cost/time. If it requires only cash, it should be narrow, temporary, or socially/economically rather than combat-useful.

### 12.4 Construction and Function Value

#### 5.1 FL Construction Curve

FL buildings show a cost/time/labor scale:

| Scale | FL examples | Materials/time/labor pattern | Generic meaning |
| --- | --- | --- | --- |
| Small dwelling | Cottage | hundreds of wood, two months, 2 builders | base shelter |
| Defensive small site | Tower / Palisade | hundreds wood/stone, 1-3 months, 4-6 builders | defense/control |
| Productive holding | Farm | hundreds wood, two months, 3 builders | production base |
| Fortified base | Fort | 1,000 wood + stone, six months, 6 builders | serious party base |
| Regional fortress | Fortress/Castle | thousands of stone, years, 10-20 builders | campaign/political asset |
| Monumental palace | Palace | tens of thousands materials, decade, 30 builders | polity-scale prestige |

The curve is not linear. Higher-tier construction adds political signal, storage, Housing, defense, and event gravity.

#### 5.2 Function Value Families

FL stronghold functions and West property features fall into repeatable value families:

| Family | FL examples | West examples | Value |
| --- | --- | --- | --- |
| Prerequisite | Forge, Oven/Fireplace, Workshop, Tannery | Forge, Oven, Crop Field, Paddocks, Pasture, Machinery | unlocks business/crafting |
| Production | Field, Garden, Pasture, Mine, Quarry, Apiary | Garden, Orchard, Animal Run | creates goods/cash |
| Storage/preservation | Granary, Root Cellar, Warehouse, Vault | Root Cellar, Strong Room, Barn | protects/extends resources |
| Defense/security | Ramparts, Guard Tower, Moat, Portcullis | Secure Fixings, Strong Room | reduces intrusion/loss |
| Social/reputation | Theatre, Shrine, Temple, Monument, Marketplace | Kerosene Lamps, Porch/Balcony, Status property | reputation/social access |
| Recovery | Infirmary, Fireplace, Temple | Open Fireplace, Well, Latrine | recovery/fortune/welfare |
| Training/knowledge | Library, Scriptorium, Training Grounds, Shooting Range | Library | skill/research support |
| Transport/market | Road, Pier, Marketplace, Warehouse | Stables, Barn, Railroad/Express amenities | access and logistics |

#### 5.3 Function Pricing Heuristic

Use this only after checking the source examples.

| Function strength | Source calibration | Generic price |
| --- | --- | --- |
| Minor convenience | FL 1 day / 20-60 wood; West $25-$50 | small cash/materials, no roll or simple roll |
| Prerequisite only | FL 2 days-1 week / 100-400 materials; West $50-$150 | modest cost, unlocks another rule |
| Narrow +1 die | West $100 Barn/False Front; FL function + staff | cost + upkeep/staff or situational scope |
| Broad +2 local bonus | FL Library/Laboratory +2 | function + staff/location-bound |
| Production engine | FL Field/Garden/Mine; West seasonal cash feature | seasonal/weekly output + event/spoilage risk |
| Security/defense | FL Ramparts/Guard Tower; West Strong Room | significant materials/cash, reduces intrusion |
| Willpower/Faith/recovery | FL Stronghold WP; West Open Fireplace Faith | once/session/period cap + base vulnerability |
| Scale/reputation | FL Fortress/Castle/Palace; West Status 6-8 | high asset cost + public attention |

**Design rule:** a function's price is not only its cost. Its price is also time, staff, location, upkeep, event exposure, and opportunity cost.

### 12.5 Property, Capital, and Rated Assets

West gives the cleanest YZE asset economy.

#### 6.1 Capital Rules to Preserve

- Cash converts into Capital at a fixed rate.
- Capital cannot buy ordinary gear unless liquidated.
- Capital invested in a business remains your investment, but cannot transfer directly to another asset.
- Liquidating Capital is risky and committed: roll for cash value after deciding.
- Loans create seasonal interest, collateral, and foreclosure risk.
- Business or property can go bust/forfeit if Capital reaches zero or debt cannot be covered.

**Abstract pattern:** Illiquid investment should be easy to create, hard to move, risky to liquidate, and vulnerable to debt.

#### 6.2 Property Status Curve

West's property Status 0-8 creates a rated-asset ladder:

| Status band | Meaning | Buy/build pattern | Social effect |
| --- | --- | --- | --- |
| 0-1 | no property / canvas | no meaningful asset | reputation penalty |
| 2-3 | shack/basic dwelling/store | 1-2 Capital buy; cheaper build with weeks/season | barely respectable |
| 4-5 | good homestead/saloon/large property | 5-8 Capital buy; build costs 3-6 Capital and 1-2 seasons | functional standing |
| 6-7 | substantial / excellent property | 12-16 Capital buy; 9-12 build and 3 seasons | +1/+2 Reputation |
| 8 | mansion/huge ranch | 20 Capital buy; 16 build and 4 seasons | +3 Reputation |

**Build vs buy principle:** building costs less Capital but costs time. Buying costs more Capital but gives immediate access. The finished asset retains purchase value, not build cost.

#### 6.3 Location Value

Location is a separate asset layer. It controls availability, price, conflict, and business fit.

**Generic location variables:**

- centrality/access;
- land quality/resources;
- legal claim strength;
- competition for the plot;
- reputation of neighborhood;
- exposure to violence, disease, weather, law, and faction pressure.

### 12.6 Town Amenities and Civic Investment

West town amenities are community-scale construction.

#### 7.1 Amenity Rules to Preserve

- Town has multiple aspects.
- Each aspect has tally points and rank thresholds.
- One amenity is chosen per season by default.
- Extra amenities require Settlement Points earned through community-spirited play.
- Amenities take one season and apply modifiers at the next Turn of the Season.
- Some amenities have prerequisites or minimum Civic rank.
- Amenities may boost some aspects while lowering others.
- If any aspect falls below rank 1, the town fails and begins irreversible decline.

#### 7.2 Amenity Value Families

| Amenity value | Mechanical expression |
| --- | --- |
| aspect growth | +1 to +3 tally in one or more aspects |
| trade access | makes goods/services easier to find |
| law/safety | improves Law/Safety but may reduce vice/profit |
| welfare/care | improves Fortune modifiers and survival |
| civic capacity | unlocks higher-rank amenities |
| resource extraction | boosts Natural Riches but may harm Law/Welfare |
| settlement points | recurring civic growth currency |

**Design rule:** civic improvements should change the community's future probability space, not only grant immediate bonuses.

### 12.7 Business Income and Seasonal Returns

West's Season Business Roll is the baseline YZE business-reckoning engine.

#### 8.1 Business Roll Formula

**Dice pool:** proprietor key ability + help from owners/employees/compadres (max +3) + Competition modifier (-2 to +2) + Law aspect modifier + relevant town aspect modifier + business features/equipment.

**Roll rule:** cannot be pushed and does not trigger Trouble.

**Results:**

- **0 successes:** wages/running costs not covered; roll Business Penalty; owners cover debts or risk liquidation/loan/bust.
- **1 success:** steady; wages and costs paid.
- **2+ successes:** Business Bonus; each success beyond the first adds +1 to the Tens die of the D66 Bonus result.

#### 8.2 Income Types

| Income | Source | Risk profile |
| --- | --- | --- |
| salary | seasonal job; proprietor/employee wage | reliable if business succeeds |
| dividends | 2+ success Business Bonus | only if business outperforms |
| seasonal feature cash | Garden/Animal Run/Orchard-style features | small roll-based side income |
| congregation donations | preacher roll x Prosperity | tied to town wealth and social support |
| lifestyle effects | paid up-front | social modifier, not profit |
| outlaw score | episodic take | high heat/cohesion risk |

#### 8.3 Return Benchmarks

| Investment type | Expected return posture | Pressure |
| --- | --- | --- |
| 1 Capital business stake | safety of stake + wage if working; dividend only on 2+ successes | failure can create debt/bust |
| property feature $25-$50 | small fortune/lifestyle/resupply modifier | narrow, often personal |
| property feature $100-$150 | +1 business roll or prerequisite | depends on business roll |
| property Status | reputation, business/home eligibility | debt, maintenance, Fortune events |
| town amenity | aspect rank / future Fortune | one season delay, community opportunity cost |
| FL function | persistent capability | material/time/staff/upkeep/event exposure |

**Design rule:** ordinary investment should not out-earn adventure safely. Its value is reliability, belonging, capability, and future hooks. High returns must attract competition, debt, attention, or event risk.

### 12.8 Cost/Value Translator

Use this translator to move between FL-style construction and West-style investment without pretending their currencies are identical.

#### 9.1 Translate by Function, Not Price

| If the source object does this... | FL expression | West expression | Generic output |
| --- | --- | --- | --- |
| unlocks crafting/business | Forge/Oven/Workshop function | Forge/Oven/Machinery feature | prerequisite function |
| gives +1 to enterprise roll | staff/function support | $100 Barn/False Front/General Amenities | narrow enterprise bonus |
| preserves supplies | Granary/Root Cellar | Root Cellar/Barn | storage function |
| protects valuables | Vault | Strong Room | security function |
| grants public standing | Fortress/Castle/Temple/Theatre | Status 6+, lamps, porch, property | reputation/status asset |
| generates Willpower/Faith/recovery | stronghold base effect, Shrine | Open Fireplace, church support | capped recovery/Willpower/Faith source |
| grows community | stronghold attracts residents | town amenity/aspect tally | civic improvement |

#### 9.2 Cost Bands

| Band | FL material/time example | West cash/Capital example | Generic use |
| --- | --- | --- | --- |
| Minor | 20-60 wood/stone; 1 QD-1 day | $25-$50 | small feature, comfort, narrow fortune |
| Small function | 100-200 materials; 2 days-1 week | $50-$100 | prerequisite or narrow +1 |
| Major function | 300-600 materials; 1-4 weeks | $100-$150 | +1 business, security, storage, production |
| Building / Status 2-3 | 200-600 materials; 6 weeks-season | 1-2 Capital buy/build | home/store/basic base |
| Serious property / Status 4-5 | hundreds+ materials; season+ | 5-8 Capital buy; 3-6 build | established business/home |
| High status / Status 6-8 | thousands materials; seasons-years | 12-20 Capital buy | political/social asset |
| Stronghold/polity | fortress/castle/palace | town/city-level amenities/assets | campaign-scale subject |

#### 9.3 Time Bands

| Time | Use for |
| --- | --- |
| scene / Turn | repair, emergency work, access, small services |
| Quarter Day / Shift | simple craft, maintenance, training, treatment |
| day | minor function, small construction, repair |
| week | major function, specialist item, property feature |
| month | field, mine, rampart, serious build |
| season | West property build, town amenity, business reckoning |
| year+ | fortress, castle, dynasty, major civic transformation |

#### 9.4 Bonus Pricing Rule

| Bonus | Allowed if |
| --- | --- |
| +1 narrow scene/location bonus | modest feature or tool; no upkeep needed if narrow |
| +1 enterprise/season bonus | feature/function + cost + prerequisite or staff |
| +2 local skill bonus | location-bound function and specific activity |
| +2 broad bonus | rare; should be talent, artifact, or campaign-mode asset |
| persistent broad +1 | requires upkeep, location lock, risk, or limited scope |

#### 9.5 Outcome Economics

Do not price an asset only by its name. Price the outcome it creates. FL functions and West property features show the reusable outcome families below.

| Outcome | Source calibration | Allowed ceiling | Required brakes |
| --- | --- | --- | --- |
| Prerequisite unlock | FL Forge/Workshop/Tannery; West Forge/Oven/Machinery/Pasture | unlocks an activity or business, no direct profit by itself | location, cost, build time, sometimes staff/talent |
| Batch conversion | FL Bakery/Forge/Tannery/Smokery convert up to 12 units per Quarter Day | converts stock into usable/sellable form | input stock, staff, work period, storage |
| Seasonal production | FL Field 300/year; FL Garden 10/week in season; West Garden/Orchard/Animal Run 2D6 dollars x successes | resource/cash output in a defined season | seasonal timing, roll or labor, spoilage/storage, land |
| Narrow +1 enterprise bonus | West Barn/False Front/General Amenities | +1 to one business family or period roll | property feature, cost, business scope |
| Local +2 skill bonus | FL Library/Laboratory/Workshop-like functions; West Library | +2 to a specific skill/activity only while using the location | location lock, function cost, prerequisite materials/books/tools |
| Fortune modifier | West Latrine/Root Cellar/Well add Units-die modifiers to Personal Fortune | improves event table posture, not direct cash | property-bound, period-limited |
| Security penalty | West Secure Fixings -1, Strong Room -3; FL Vault/Guard Tower/Ramparts | penalizes intrusion or improves defense | fixed target, does not attack enemies by itself |
| Storage preservation | FL Granary/Root Cellar x10 shelf life; West Root Cellar fortune help | extends shelf life or protects stock | stockpile still needs place, guard, transport |
| Recovery/Willpower/Faith | FL stronghold +1 WP/session at home; West Open Fireplace bonus Faith once/session | once/session or once/period recovery/refuel | base vulnerability, comfort/time requirement |
| Reputation/status | FL Fortress/Castle/Palace; West Status 6-8/Kerosene Lamps | social modifier, recognition, access | public attention, cost, maintenance, rivalry |
| Civic aspect growth | West town amenities | changes future town modifiers | one-season delay, aspect floor, SP/amenity limits |

**Design rule:** an asset may combine two modest outcomes, but a three-outcome asset is a campaign-mode feature and needs higher cost, upkeep, public exposure, or a dedicated event table.

#### 9.6 Source-Calibrated Pricing Bands by Outcome

| New asset effect | Minimum source-backed price posture |
| --- | --- |
| Allows a business to exist | West $50-$150 property feature or FL 2 days-1 week function with tools/materials |
| Gives +1 to a specific season business roll | West $100-ish feature, scoped to a business type |
| Gives +1 to any enterprise roll | campaign-mode only; require upkeep, staff, and stacking cap |
| Gives +2 to a skill | FL/West Library-like function, location-bound and narrow |
| Produces small seasonal cash | West $25-$50 feature plus ability roll; payout 2D6 dollars x successes |
| Produces bulk yearly stores | FL field/garden/pasture scale; requires land, season, labor, storage |
| Protects valuables at -3 intrusion | West Strong Room / FL Vault scale; high feature/function cost |
| Adds Fame/Reputation | visible property/status feature; invite attention and social consequences |
| Adds Willpower/Faith | once/session cap and requires rest/shift/day at owned safe place |
| Improves settlement modifiers | one season delay and community aspect bookkeeping |

#### 9.7 Business Bonus and Penalty Calibration

West's Season Business Roll gives a usable economic envelope:

- **0 successes:** no wages/running costs; roll Penalty and cover debts immediately or by adventure deadline.
- **1 success:** wages and costs are covered; no investor dividend.
- **2+ successes:** roll Bonus; each success beyond the first improves the D66 Tens die.

Use these bands when designing new bonus/penalty tables:

| Band | Bonus posture | Penalty posture |
| --- | --- | --- |
| Low | small cash windfall, about a few D6 | no extra loss or small debt |
| Middle | cash x Capital, next-roll bonus, Competition shift, Fame/Reputation movement | D3 x small debt, Reputation hit, Competition worsens |
| High | bonus Capital immediately liquidated, new helper, strong next-roll bonus | D6/2D6/3D6 x debt unit, employee quits, large reputation harm |
| Extreme | half Capital pool equivalent liquidated as bonanza | Capital-pool-scaled debt, likely bust unless rescued |

**Debt design rule:** failed business should not merely say "no profit." It should ask who pays, who goes unpaid, what gets liquidated, who loses trust, and what adventure can save it.

### 12.9 Payback, Upkeep, and Pressure Checks

#### 10.1 Payback Check

For any income-producing asset:

1. What is the up-front cost?
2. How often can it pay out?
3. What is the ordinary payout?
4. What roll gates payout?
5. What is the failure cost?
6. How many successful periods repay the investment?
7. What story pressure appears before payback?

**Rule of thumb:** safe payback inside 1-2 periods is too generous unless the investment is very small. Major assets should need several successful periods or should pay in capability/status rather than cash.

#### 10.2 Upkeep Check

Every asset with persistent value needs at least one upkeep vector:

| Asset | Upkeep vector |
| --- | --- |
| hireling/staff | wages or housing/food |
| resident | housing + food/water |
| function | maintenance/staff/materials |
| business | season roll and wage coverage |
| property | lifestyle, Fortune events, repairs |
| town | aspect risk, amenities, Fortune |
| gang | seasonal upkeep, Provisions, Cohesion |
| vault/warehouse | guard/security/event exposure |

#### 10.3 Pressure Equivalence

When converting between FL and West:

| FL pressure | West pressure |
| --- | --- |
| raw material scarcity | Capital scarcity |
| crafting failure/flaw | build delay/debt/property dispute |
| hireling non-payment | wage shortfall/debt/employee quits |
| unguarded stronghold | robbery/foreclosure/contested property |
| lacking upkeep | repair bill, Status loss, Fortune event |
| stronghold Reputation event | Fame/Reputation/town attention |
| function staff requirement | proprietor/employee/prerequisite equipment |

#### 10.4 Costing New Assets Procedure

Use this procedure when inventing a new function, feature, business asset, or investment from the source abstractions.

1. **Choose the outcome family** from §9.5.
2. **Choose the source pole:** FL material/function, West property/Capital, or hybrid.
3. **Assign cost unit:** cash, Capital, raw materials, labor, stores, SP, or project ticks.
4. **Assign time band:** day, week, month, season, year.
5. **Assign gates:** talent, tools, function, location, specialist, staff, town aspect, legal claim.
6. **Assign upkeep:** wages, food/water, repair check, lifestyle, debt interest, event exposure, stock input.
7. **Assign failure:** no retry until skill improves, flaw, delay, debt, reputation loss, employee trouble, contested claim, function damage.
8. **Check stacking:** if it adds dice, state whether it stacks with tools, help, town aspects, and investment.
9. **Check payback:** calculate successful periods to recover cost if it produces cash.
10. **Write rule prose:** name what characters do at the table, not only what the asset represents.

#### 10.5 Example Abstractions

**Clinic / infirmary.** Outcome family: recovery. Source pole: FL Infirmary + West Doctoring. Cost: major function or $150-ish feature plus trained staff. Effect ceiling: improved healing/doctoring at the location, not portable immunity to critical injuries. Upkeep: doctor wages, supplies, clean space. Failure: infection, supply shortage, malpractice rumor, or a patient obligation.

**Printing office / rumor press.** Outcome family: reputation/status + batch conversion. Source pole: West Newspaper prerequisite property + FL Scriptorium. Cost: property, press/machinery, paper/ink, staff. Effect ceiling: +1 to public-facing reputation/propaganda enterprise moves or create rumor output. Upkeep: wages, paper, legal exposure. Failure: libel suit, mob, censor, rival editor, broken press.

**Safehouse network.** Outcome family: security/storage + secrecy. Source pole: West Strong Room/Secure Fixings + FL several strongholds. Cost: multiple minor properties or Capital/contacts. Effect ceiling: reduce Heat/Exposure or protect one stockpile/person. Upkeep: bribes, caretakers, secrecy. Failure: one safehouse exposed, informant, stored goods seized.

**Arcane laboratory / experimental shop.** Outcome family: local +2 skill bonus + project gate. Source pole: FL Laboratory/Library. Cost: function, rare tools, specialist, week/month build. Effect ceiling: +2 only to defined research/craft rolls performed there. Upkeep: ingredients, safety, patron suspicion. Failure: accident, corrupted result, damaged function.

**Commercial route office.** Outcome family: market/transport + enterprise bonus. Source pole: FL Marketplace/Warehouse/Road + West business roll. Cost: warehouse/office, route contacts, transport. Effect ceiling: +1 to route/trade enterprise rolls or reduce transport friction. Upkeep: guards, tolls, animals/vehicles, staff. Failure: cargo delay, extortion, road damage, lost customer.

### 12.10 Trade routes, cargo, and gambling scenes

FL's Traderoads chapter adds a complete medium-scale economy that sits between personal gear and seasonal enterprise: the **cargo run**. West adds a compact **gambling** procedure that turns money, reputation, cheating, and social reading into a scene economy. Both should be abstracted because they are reusable beyond their genres.

#### Cargo run sheet

Use this for caravans, freight lines, smugglers, riverboats, pack trains, starship haulers, courier routes, merchant houses, salvage runs, pilgrim roads, and medical supply lines.

| Field | What it records | Why it matters |
| --- | --- | --- |
| Transport | wagons, pack animals, boats, rail, starship hold | hard capacity cap |
| Load units | how much cargo each vehicle/animal carries | prevents invisible bulk |
| Crew roles | master, scout, guard, driver, quartermaster, negotiator | gives PCs jobs |
| Cargo category | staple, luxury, contraband, fragile, perishable, sacred, military | sets price and hazards |
| Purchase price | cost at source | investment at risk |
| Origin profile | surplus/ordinary/scarce source | buy-side modifier |
| Destination profile | surplus/ordinary/scarce destination | sell-side modifier |
| Perishability | none / days / route / season | clock against delay |
| Fragility | none / rough road / combat / weather | hazard handshake |
| Route | distance, terrain, tolls, water, danger | travel handshake |
| Market intelligence | rumor, contact, false lead, old price | uncertainty source |
| Reputation | caravan name, reliability, fear, scandal | future access and price |
| Return load | contract, passenger, empty, backhaul cargo | stops one-way profit loops |

#### Cargo run procedure

1. **Choose a route thesis.** What are you moving, from where, to whom, and why is the price different?
2. **Buy cargo.** Commit cash, Capital, credit, goods, favors, or stolen stock before knowing the final market result.
3. **Load and expose.** Check capacity, crew, guards, animals/vehicles, stores, and legal cover. Excess cargo requires more transport or creates penalties.
4. **Travel the route.** Use `06` for movement, camp, pursuit, weather, and hazards. Delay matters because perishability and opportunity cost are real.
5. **Roll market.** At destination, roll trade/negotiation/merchant skill plus market intelligence, destination demand, reputation, cargo quality, and competition.
6. **Spend successes.** Sell more units, raise margin, secure a return contract, avoid tariffs, find a passenger, improve reputation, or learn a new route rumor.
7. **Handle unsold cargo.** Store it, dump it at loss, carry it onward, split it, convert it, or pledge it as collateral.
8. **Account.** Subtract purchase price, wages, provisions, tolls, damage, bribes, debt interest, and repairs.
9. **Reinvest or exit.** Buy better transport, warehouse space, guards, contacts, route rights, insurance, or market intelligence.
10. **Write fallout.** Rival merchants, bandits, tax collectors, broken axle, spoiled cargo, false rumor, grateful settlement, unpaid guards, or a dangerous passenger.

#### Market result ladder

| Successes | Result |
| --- | --- |
| 0 | Bad market. Sell only at loss or carry cargo onward. Add a complication: spoilage, tariff, seizure, theft, rival undercuts, buyer defaults. |
| 1 | Ordinary sale. Recover costs and modest margin if the route thesis was sound. No special opportunity. |
| 2 | Good sale. Profit is meaningful; choose one: reputation +1, return contract, passenger, rumor, bulk buyer, avoided cost. |
| 3+ | Breakout sale. Strong profit and two benefits; each extra success may increase margin, sell unsold cargo, or improve future market position. |

#### Cargo choices

| Choice | Low-detail pole | High-detail pole |
| --- | --- | --- |
| Capacity | one cargo slot per vehicle | load units by transport |
| Price | fixed margin | buy/sell profiles + market roll |
| Spoilage | ignored | perishability clock by weather/delay |
| Fragility | ignored | hazard checks on rough travel/combat |
| Reputation | none | modifies market, guards, contracts, law |
| Return trip | handwaved | required backhaul/passenger/empty-cost decision |
| Legality | ordinary trade | contraband, customs, seizure, Heat |

**Validation:** cargo profit must not become safe compounding wealth. At least one of these must be active: capacity cap, purchase risk, route hazard, perishability, market uncertainty, debt, guard wages, legal exposure, rival pressure, or unsold cargo.

#### Gambling scene procedure

Use this for poker, dice, horse wagering, illegal fight books, speculative trading, courtly wagers, casino nights, starport games, magical auctions, and any scene where money and reputation are risked under social pressure.

1. **Set the stake.** Cash, item, favor, information, debt, reputation, access, or ownership share.
2. **Set the table.** Honest / sharp / fixed / desperate / watched by law / faction-owned / high society.
3. **Choose approach.** Play straight, read opponents, bully, charm, cheat, count cards, collude, throw the game, or bait a mark.
4. **Roll.** Use the best fitting social, insight, gambling, sleight, or profession skill. Oppose sharp opponents; use a static difficulty for ordinary games.
5. **Resolve money.** Success wins or protects stake. Extra successes buy profit, read, contact, rumor, or reputation.
6. **Resolve exposure.** Cheating, bullying, impossible luck, and big wins create suspicion. Trouble/banes can trigger accusation, duel, law, debt, or enemy.
7. **Close the scene.** Decide who is richer, who is offended, who owes, who saw too much, and what rumor leaves the room first.

| Extra success spend | Effect |
| --- | --- |
| Increase take | win an additional stake unit |
| Read a player | learn motive, fear, tell, debt, hidden patron |
| Build reputation | gain fame as lucky, dangerous, honest, or crooked |
| Create contact | a player offers work, information, or patronage |
| Hide method | reduce suspicion from cheating/collusion |
| Trap a mark | target leaves owing money/favor |

**Gambling validation:** gambling should create hooks as often as money. If the only output is profit, the optimal play becomes repetitive bankroll grinding. Always bind large wins to witnesses, reputation, debt, law, enemies, or social leverage.

### 12.11 Rule choices

| Choice | FL pole | West pole | Generic choice |
| --- | --- | --- | --- |
| Cost unit | raw materials + labor | cash + Capital | material vs asset economy |
| Construction resolution | Crafting roll; failure flaw/lockout | pay cost/time; haggling possible | roll-risk vs capital/time certainty |
| Time scale | Quarter Day to years | season for property/amenity | active period |
| Asset liquidity | function is fixed | Capital liquidates risky | resale/liquidation model |
| Income | function production/capability | salary/dividend/business roll | cash vs capability |
| Upkeep | weekly craft/guard/pay | seasonal wage/debt/lifestyle | cadence |
| Bonus style | location function + staff | +1 business/fortune/reputation | scope |
| Community growth | stronghold residents/reputation | town aspect tally/SP | base vs town |
| Failure | flaw, decay, event, hireling trouble | debt, bust, Status loss, town decline | consequence family |

### 12.12 Validation Worksheets

#### Crafting Validation

- Does the item require the correct gates for its power?
- Does any +1 die require enough cost, scope, or upkeep?
- Can players bypass scarcity by crafting too cheaply?
- Is failure a real cost: material loss, flaw, delay, no retry, event?
- Does the craft time compete with adventure/season time?

#### Construction Validation

- What cost band is it?
- What time band is it?
- How many workers/staff are required?
- Does it need a prerequisite function/location?
- Does it create Housing, storage, defense, production, reputation, or recovery?
- What threatens it if unguarded/unmaintained?

#### Investment Validation

- Is the investment liquid or illiquid?
- Can it be moved to another asset freely? If yes, why does Capital matter?
- What is the expected payback period?
- What happens on a failed season?
- Can the asset go bust, be foreclosed, be contested, or lose status?
- Does it out-earn adventuring without comparable risk?

#### Economy Validation

| Check | Fail sign | Fix |
| --- | --- | --- |
| Passive wealth | money grows without roll/risk/time | add season roll, upkeep, debt, event |
| Safe liquidation | assets convert at full value anytime | add delay, discount, roll, buyer, risk |
| Bonus stacking | property/features grant many +1s | cap feature bonuses or make them prerequisites |
| Free staff | employees add dice without wages/housing | add wage/upkeep/loyalty |
| Instant build | major functions appear between scenes | move to week/month/season |
| No consequence | failed season only says "no money" | add debt, Reputation, Capital loss, employee trouble |
| Double bill | same lifestyle/upkeep charged twice | choose one pressure grain |

### 12.13 Instantiation Recipe

1. **Choose economy posture:** material-scarcity, cash-business, hybrid, or civic/domain.
2. **Define cost units:** cash, Capital, raw materials, labor, stores, SP, project ticks.
3. **Define asset types:** item, function, building, property, amenity, enterprise, town.
4. **Set cost bands:** minor, small function, major function, building, serious property, high-status asset.
5. **Set time bands:** Quarter Day, day, week, month, season, year.
6. **Write gate rules:** talent, tool/function, material, specialist, staff, location.
7. **Write income/upkeep rules:** salary, dividends, production, feature output, lifestyle, debt, staff.
8. **Write failure families:** flaw, debt, delay, loss, staff trouble, Reputation, event, collapse.
9. **Write conversion rules:** personal cash -> investment, materials -> function, function -> bonus, asset -> storage/status.
10. **Validate payback:** major assets should create hooks before they repay safely.

**Final acceptance test:** a designer should be able to explain for every asset: what it costs, how long it takes, who must work it, where it exists, what it unlocks, how it pays out, what it consumes, and what goes wrong when neglected.


## 13. Strange Devices

Strange Devices are the generic version of inventions, contraptions, unstable gear, alchemy, alien tools, occult apparatus, prototype machines, black-market weapons, siege tricks, cybernetics, and other crafted objects that bend ordinary gear rules without becoming full powers.

Use this section when an item is more than a weapon tag but less than a spell tradition. A Strange Device should feel tempting, useful, and a little unsafe.

### 13.1 Device sheet

| Field | Required answer |
| --- | --- |
| Name | a flavorful object name |
| Kind | contraption, invention, alchemy, gadget, relic, cybernetic, prototype, occult tool |
| Function | what it lets the user do that ordinary gear cannot |
| Activation | SLOW, FAST, Turn, Shift, period, or passive |
| Charges/fuel | uses, resource die, battery, reagent, heat, crew attention, rare parts |
| Build gate | talent, workshop, teacher, plan, rare material, power tradition, license |
| Upkeep | what must be repaired, cooled, cleaned, fed, tuned, recharged |
| Misfire | what happens on banes, Trouble, failed activation, or overuse |
| Bulk | row count, mount/vehicle need, fixed emplacement, hidden item |
| Legality | ordinary, restricted, scandalous, illegal, heretical, classified |
| Repair | skill, time, parts, workshop, specialist |
| Reskin | at least two genre skins using the same rules |

### 13.2 Device roles

| Role | What it does | Examples |
| --- | --- | --- |
| Breacher | opens armor, doors, walls, wards | acid charge, shaped explosive, rune drill, plasma cutter |
| Shelter | protects from environment or attack | smoke bomb, ward lantern, pressure suit, portable barricade |
| Sense | reveals hidden things | spirit lens, radio scanner, bloodhound engine, microscope |
| Motion | moves people or cargo strangely | grapnel, jump rig, levitation disk, mule drone |
| Control | binds, stuns, lures, frightens | flash powder, shock prod, charm bell, riot foam |
| Conversion | turns one resource into another | still, generator, blood battery, recycler, forge engine |
| Treatment | heals, purges, preserves, revives | injector, field kit, alchemical poultice, surgery rig |
| Signal | sends, hides, jams, records | cipher box, beacon, ghost radio, drone relay |
| Ruin | damages an area or creates hazard | fire pot, gas shell, swarm jar, unstable reactor |

### 13.3 Charges and upkeep

| Charge model | Use when | Rule |
| --- | --- | --- |
| Fixed charges | the device has discrete uses | mark 1 use per activation; reload in downtime |
| Resource die | uncertainty is more fun than counting | roll after use; 1-2 steps die down |
| Heat | repeated use is tempting | each use adds Heat; at threshold roll misfire |
| Rare part | activation consumes scarce input | each use spends a named part/reagent |
| Crew attention | device is big or dangerous | a helper must spend an action/station |
| Debt/legal risk | device is socially costly | each use creates heat, witness, favor, or Menace |

**Upkeep rule:** a Strange Device with a strong effect must have at least one active upkeep pressure: rare fuel, noisy use, slow reload, fragile condition, legal danger, repair burden, visible sign, or specialist maintenance.

### 13.4 Building and repairing

**BUILD A STRANGE DEVICE.** Choose a role, write the device sheet, gather gates, and treat construction as a project from `12` or `workshop/13-rituals-projects-and-research.md`. Roll Craft, Lore, Power, or a profession skill at each project interval. Success adds progress. Extra successes may lower charge cost, reduce bulk, add a narrow safety, or improve quality. Failure adds flaw, delay, lost material, debt, injury, or attention.

**REPAIR A STRANGE DEVICE.** Repair requires the right tools and one of: plan, teacher, rare part, workshop, or matching talent. Simple repair takes a Turn/Shift; serious repair takes a period. Failure does not merely say "no": add Worn, Unstable, Leaking, Loud, Hungry, Illegal Mark, or a hidden flaw.

| Build strength | Required gates |
| --- | --- |
| Minor trick | tools + common parts + skill |
| Reliable scene device | talent or plan + workshop + parts |
| Strong combat/escape device | talent + rare part + misfire + upkeep |
| Broad utility device | specialist + project + cost + legal/social exposure |
| Power-adjacent device | power tradition or rare source + backlash table |
| Campaign-changing device | season project + faction attention + irreplaceable part |

### 13.5 Misfire table

Roll or choose when the device is pushed, overused, badly maintained, activated on a failure, hit in combat, or fed poor parts.

| D66 | Misfire |
| --- | --- |
| 11-13 | sputter: effect is delayed until the end of the round/turn |
| 14-16 | hungry: spend one extra charge, part, or fuel step |
| 21-23 | loud: nearby enemies, law, spirits, sensors, or rivals notice |
| 24-26 | hot: user takes 1 damage/condition or must drop it |
| 31-33 | crooked: effect hits the wrong target, place, or quality |
| 34-36 | jammed: device cannot be used again until repaired |
| 41-43 | leaking: creates smoke, acid, sparks, magic residue, data trace, poison, radiation |
| 44-46 | backlash: user suffers the device's own effect in lesser form |
| 51-53 | broken part: lose a rare part or step quality down |
| 54-56 | witness mark: use creates legal heat, rumor, scandal, or Menace |
| 61-63 | runaway: effect continues one round/turn longer than wanted |
| 64-66 | catastrophe: explosion, possession, fatal flaw, public disaster, or permanent break |

### 13.6 Effect menu

| Effect | Low effect | Strong effect | Required brake |
| --- | --- | --- | --- |
| Blast | area noise, knockdown | area damage | loud, rare charge, friendly fire |
| Acid/corrosion | weaken lock/armor | destroy barrier/gear | dangerous storage, splash |
| Fire | light, smoke, panic | burn area/foe | spread risk, weather, witness |
| Smoke/dark | conceal escape | blind zone | affects allies, wind, limited duration |
| Light/signal | reveal, communicate | stun, expose hidden | visible to everyone |
| Shock/stun | cost action | disable briefly | charge limit, armor/insulation |
| Binding | slow, restrain | hold monster/vehicle | setup, escape roll |
| Pierce/breach | ignore part armor | open strong barrier | single-use, noise, specialist |
| Medicine | heal condition | prevent lasting harm | rare dose, side effect |
| Sensor | clue/track | reveal hidden system | false positive, trace |

### 13.7 Genre skins

| Same device role | Fantasy | Western | Sci-fi | Horror / occult |
| --- | --- | --- | --- | --- |
| Breacher | troll-acid vial | nitro charge | plasma cutter | saint-bone corrosive |
| Shelter | witch-smoke jar | canvas fire screen | hardlight shield | salt-circle lantern |
| Sense | spirit lens | prospector's assay rig | alien scanner | dead man's camera |
| Motion | goblin grapnel | rope gun | jump pack | possessed harness |
| Treatment | druidic poultice press | patent medicine injector | trauma foam | blood transfuser |

### 13.8 Strange Devices validation

- A device may be strong, reliable, cheap, discreet, and easy to repair in any two ways; never all five.
- If it grants a broad +1 or replaces a skill, make it a talent, artifact, or power instead.
- If it produces repeated area damage, add rare charges, misfire, noise, and legal attention.
- If it solves travel, hauling, healing, or locks, make its fuel and repair matter in those same loops.
- If everyone should own one, make it ordinary gear with tags instead of a Strange Device.
- If only one character can build or safely use it, write the needed talent/path gate in `02`.

## 14. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Economy model** | Barter + commodity silver; gold ceremonial | Cash (dollars) + Capital + loans + salaries | Scarcity-as-story vs money-as-story | FL pole for survival/post-collapse; West pole for any genre where property, debt, or business is a pillar |
| **Large-denomination store** | Ceremonial gold (prestige, +lead time) | Investment Capital ($250=1; liquidates D6×$50) | Static prestige vs liquidatable-but-risky assets | Use Capital only if you want an *asset/business* rule set; otherwise ceremonial-gold is lighter |
| **Credit / debt** | None | Seasonal-interest loans (5–10%), collateral, foreclosure | No debt drama vs default-as-story-beat | Include loans when debt should be a lever NPCs and PCs pull on each other |
| **Income stream** | Ad hoc (loot, favors, stronghold) | Salaries table + business rolls + hired-hands day-wages | Found money vs predictable budget | Salaries for settled/working characters; ad hoc for drifters/raiders |
| **Property model** | Stronghold = craft project (materials + labor + time) | Property Status 0–8 (Capital-priced) + Location + Features | Build-it-yourself vs buy/haggle/auction | West model when *owning* is the game; FL model when *building* is the game |
| **Availability resolution** | Per-item die roll (D6/D66), weekly restock | Settlement-tag judgment (Mercantile/Law/amenities shift steps) | Randomized stock vs deterministic town-quality | FL's roll for sandbox unpredictability; West's tags for settlement-as-character |
| **Strong-market concept** | Implicit (specialist access, town-only items) | Explicit Strong Market threshold + per-buyer rate limits | Implicit vs bounded availability | Port West's explicit threshold + rate limits if you want trade to feel *finite* |
| **Scarcity → price** | Upward only (+50–200%) | Two-sided (−25% surplus … +100%+ panic), per-step | One-sided vs full curve | West's two-sided table is the better default |
| **Weapon stat model** | Gear Dice (BONUS) that *degrade on push* | Flat ATTACK/DRAW mods, no push-degradation | Weapon-as-resource-pool vs weapon-as-modifier | FL model when gear should *be* the cost face (survival); West model for faster, lighter combat |
| **Feature grammar shape** | Tags double as action-prerequisites (Parrying→PARRY, Hook→SHOVE) | Three layers: Features (stats) / Qualities (pos, max 4, stack) / Conditions (neg, Trouble-driven) | Unified action-gating tags vs separated good/bad stacks | FL model when loadout should drive *tactical options*; West model when you want clean positive/negative optimization |
| **Quality tier high-end effect** | +1 Gear Die (combat bonus) + status | +1 gear bonus (one-cap) *or* ignore first Worn + resale/social | Mechanical power vs social/economic load | FL for lethal games where Fine must *hit harder*; West for games where Fine is about *standing* |
| **Low quality split** | Crude (breaks at 0) | Poor (badly made) + Worn (used hard) — two distinct low tiers | One low tier vs origin-quality vs acquired-wear | West's split is more expressive; use it when *provenance* of gear matters |
| **Degradation rule pattern** | Continuous counter (Bonus ticks down on push 💀/penetration) | Discrete Conditions (named tags from D6 table, Trouble-driven) | Granular attrition vs narrative breakage | FL's counter when gear is a resource pool; West's tags for lighter bookkeeping |
| **Legendary tier** | Artifact die (D8/D10/D12) + named + oddity table | None (nearest analogue: Faith) | Escalating-success-die + story-loaded items vs flat power ceiling | Include for fantasy/pulp; omit for grounded/historical |
| **Consumables tracking** | Resource dice as default (Arrows/Torches/Food/Tools) | Resource dice as Optional Module; loose counting default | Always-on logistics pressure vs opt-in survival mode | Default-on for wilderness/survival; default-off for urban/cinematic |
| **Crafting depth** | Full unit-economy (fractional raw materials, material ladder, masterwork) | Folded into Availability/Quality + business prerequisites | Deep simulation vs light resolution | FL depth when *crafting is a pillar*; West lightness otherwise |
| **Material-quality ladder** | Iron→Wrought→Steel→Crucible→Dwarven (+1 to +3, talent-gated) | (not present — quality is a buyable grade, not a craftable material) | Make-it-better-by-being-better vs buy-it-better | Port the ladder for any genre where *crafting mastery* should scale output |

## 15. Rule Choices and Build Recipe

Each choice has FL and West as two calibrated points. To build a new game's gear-and-economy layer, set each choice.

1. **Economy model** — barter+commodity / cash / cash+capital / multi-currency. *(Sets what characters struggle for. The single most tone-defining gear choice.)*
2. **Large-denomination store** — ceremonial prestige-gold / liquidatable Capital / none. *(Whether an asset-and-business rule set exists.)*
3. **Credit** — none / seasonal-interest loans with collateral / full banking. *(Whether debt is a lever.)*
4. **Income stream** — ad hoc / seasonal salaries / business rolls / rents. *(How characters get money.)*
5. **Property model** — none / craft-project stronghold / rated-asset Status ladder. *(Whether owning things is a pillar.)*
6. **Availability resolution** — per-item die roll (random stock) / settlement-tag judgment (deterministic). *(How "can I buy it here?" is answered.)*
7. **Strong-market concept** — implicit / explicit threshold + rate limits. *(Whether trade feels finite.)*
8. **Scarcity → price curve** — one-sided (upward) / two-sided (surplus→panic). *(West's two-sided is the better default.)*
9. **Weapon stat model** — degrading Gear Dice (weapon-as-resource) / flat modifiers. *(Whether gear is itself a cost face.)*
10. **Feature grammar shape** — action-prerequisite tags (FL) / three-layer stats+qualities+conditions (West). *(How loadout drives play.)*
11. **Quality ladder** — 3-tier / 4-tier (split low); high-end = combat bonus (FL) / social bonus (West). *(What "Fine" means.)*
12. **Degradation rule pattern** — continuous counter (FL) / discrete Conditions (West). *(How gear gets worse — must match choice 9 and the push-cost model from `00 §6`.)*
13. **Legendary tier** — on (artifact die + oddities) / off. *(Power ceiling; omit for grounded genres.)*
14. **Consumables tracking** — resource dice default-on / default-off (loose counting). *(Whether logistics is always-on or opt-in.)*
15. **Crafting depth** — full unit-economy + material ladder / folded into availability. *(Whether making things is a pillar.)*
16. **Strange Devices** — off / ordinary gear tags / contraptions with charges + misfires / power-adjacent prototypes. *(Whether unstable inventions are a pillar.)*

**Instantiation recipe (any genre):**
1. **Set the economy model (choice 1)** first — it does more to set the *feel* of gear than any other choice. Decide whether your characters are *starved* of money (FL pole) or *managed* by it (West pole).
2. **Decide the property/asset layer (choices 2–5)** as a block: include Capital+loans+salaries+property *only* if owning/business/debt is intended to be a pillar. Otherwise strip it all (FL).
3. **Port the availability/scarcity table (choices 6–8)** near-verbatim from §3 — it is shared machinery. Default to West's settlement-tag + two-sided-price version.
4. **Choose the feature grammar shape (choice 10)** — this is the central design decision for *gear feel*. Use FL's action-prerequisite tags if loadout should unlock tactical options; use West's three-layer model if you want clean positive/negative optimization. In either case, port §6.4's architecture.
5. **Align the weapon-stat, degradation, and push-cost models (choices 9, 12, and `00 §6`)** — these *must* be consistent: degrading Gear Dice pair with bane-self-harm; flat mods + Conditions pair with currency-spend + Trouble.
6. **Set quality + condition + legendary (choices 11, 13)** to the genre's power ceiling and grit level.
7. **Set consumables tracking (choice 14)** to the genre's logistics appetite (default-on for survival, default-off for cinematic).
8. **Decide crafting depth (choice 15)** and, if deep, port the material-quality ladder (§5.2).
9. **Decide Strange Devices (choice 16)** if inventions, alchemy, gadgets, occult tools, prototypes, or alien devices need more than ordinary gear tags.
10. **Validate against the math** (see `13-balance-and-synergy.md`): expected weapon damage per round, time-to-Broken, degradation rate vs repair cadence, resource-die exhaustion length for a typical expedition, salary-vs-lifestyle cash flow over a season, and Strange Device charge/misfire cadence.

## 16. Design intent

The gear-and-economy layer is engineered so that **what a character carries and what a character is worth are both load-bearing fiction**, not bookkeeping. Specifically:

- **The feature grammar makes gear *feel* different, not just numerically different.** A dagger and a shortsword have the same Damage and Bonus; what separates them is `Short-reach, no Parrying` vs `Parrying, Tough`. Tags carry *meaning* — and because tags double as action-prerequisites (FL) or stack into a profile (West), loadout becomes a *tactical and expressive* choice rather than a DPS optimization. This is why the grammar is the file's central deliverable: it is the part of the system that survives any reskin.
- **The availability table makes *geography* matter.** Scarcity is not a price modifier tacked on at the end — it is the rule that *decides whether the item exists at all* in this settlement, and the settlement's tags (Mercantile, Law, amenities, railroad) make the world's map a gear-gating surface. You can't get a fine rifle in a town with no gunsmith; you can't get illicit goods openly where Law is 5–6. The world *is* the shop.
- **The economy model *is* the genre's statement about value.** FL's barter+ceremonial-gold says scarcity and isolation are the story; West's cash+capital+loans says money, debt, and reputation are the story. The same engine produces opposite tones by swapping the currency — exactly as the core loop does by swapping the push-cost model (`00 §12`). A new genre must find *its* relationship to money and wire the choice to it.
- **Crafting takes in-fiction time and gates**, so it ties into the downtime/season loop (`06-travel-and-downtime.md`) rather than being a between-combat menu. The four gates (talent, workshop, materials, time) and the material ladder mean *being a better craftsman literally produces better goods* — mastery has a material payoff.
- **Quality + condition + degradation make gear a *lived* object.** A Fine sword that you've kept Fine, a Standard one now Worn, a Crude club about to snap — these tell the character's history. And because degradation is wired to the engine's existing failure layer (push 💀 / Trouble), *gear wears out for the same reason characters get hurt*, unifying the pressure.
- **The legendary tier (artifact die + oddities) makes top-tier gear *wanted and feared*, not just owned.** A +2 sword is forgettable; "Alur's Cloak, which whispers paranoid fantasies and grows stronger in the wilderness" is not. The oddity table is the proof that *a magic item is a story, not a stat*.
- **Consumables-as-resource-dice convert logistics into drama.** "I have 14 arrows" is bookkeeping; "my Arrow Die is D6 and every fight might cost me a step" is a gamble. It is the consumables analogue of the push: each use is a small decision with a real downside, and resupply becomes an event rather than a line item.

The divergence between FL and West is the engine's proof that **the same availability table, feature grammar, and quality ladder support opposite genres by changing the economy choice and the degradation rule pattern.** FL's degrading Gear Dice and barter economy make a game where *your body and your axe are the same kind of scarce*; West's flat mods, Conditions, and cash+capital make a game where *your gun and your wallet degrade by different logics*. A new genre's job is to choose, for each choice, which logic its world runs on — and the grammar, the table, and the ladder will port unchanged.
