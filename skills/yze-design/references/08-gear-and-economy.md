<!-- markdownlint-disable MD013 MD024 MD041 MD060 -->

# Gear and Economy — Equipment, Crafting, Money

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the stuff layer — it assumes the dice grammar and Gear Dice of `00-engine-core.md` §3, the conflict action economy of `03-conflict-and-damage.md`, and the downtime/season loop of `06-travel-and-downtime.md`. The two central deliverables are the **Feature Grammar** (§6–7: weapons and armor are defined by *composable tags*, not stat lines) and the **Economy-Model dial** (§4: barter+silver vs cash+capital). A third portable artifact — the **Availability/Scarcity table** (§3) — is shared near-verbatim by both games.

## Contents

1. Source provenance
2. Abstraction target
3. Supply / scarcity / availability tables — **shared near-verbatim**
4. Economy models: the economy dial (barter+silver / cash+capital+loans+salaries)
5. Crafting — the making layer (talent-gated, workshop-gated, time-gated, material-gated)
6. Weapon feature grammar — **the central reusable artifact**
7. Armor feature grammar
8. Quality tiers and condition/degradation
9. Artifact / legendary gear and the artifact die
10. Consumables as resource dice
11. Divergence rows (FL vs West)
12. Dials and instantiation recipe
13. Design intent

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

Abstract **gear and economy** as a genre-neutral system of *five separable layers*, each a design dial, with FL and West as two calibrated points:

1. **Availability / Scarcity** (§3) — a rating that controls *whether* an item can be found in a given settlement, and a price-adjustment table for *how the market bends the cost*. Both games ship near-identical machinery here.
2. **Economy model** (§4) — the *form money takes*: barter+commodity-currency (FL) vs cash+capital with credit and wages (West). This is the file's **central divergence**.
3. **Crafting / the making layer** (§5) — *who can make what, where, in how long, from what*. Talent-gated, workshop-gated, time-gated, material-gated.
4. **Feature grammar** (§6–7) — **the central reusable artifact.** Weapons and armor are defined by a *small set of composable tags* (Edged, Pointed, Polearm, Parrying, Pierce Armor… / CALIBRATED, RELIABLE, PIERCING…) rather than by bespoke stat lines. The grammar is what lets two swords feel different without inflating numbers.
5. **Quality / condition / legendary tiers** (§8–9) — the *degradation and escalation* layers: quality tiers (Crude/Standard/Fine), condition tracks (Worn→broken), and the artifact/legendary die for gear so fine it has its own dice.

A sixth, cross-cutting mechanism — **consumables as resource dice** (§10) — replaces item-counting with a single degrading die, and is the engine's preferred way to track *ammo, torches, food, tools* under pressure.

## 3. Supply / scarcity / availability tables — **shared near-verbatim**

Both games solve the same problem — *not everything is for sale everywhere* — with the same two-part machine: (a) a per-item **availability rating** that the GM rolls or judges against the settlement, and (b) a **price-adjustment table** for when scarcity bites. The machinery is nearly identical; only the *labels* and the *trigger* differ.

### 3.1 The availability ladder

| FL rating (`10-gear.md:13-19`) | West rating (`06-life:500-505`) | How it's resolved |
| --- | --- | --- |
| **Common** | **Common** | Generally available in any functioning settlement. |
| **Uncommon** | **Uncommon** | FL: roll D6, **4+** = 1D6 units available, weekly restock. West: needs a better town / the right business / time to ask around. |
| **Rare** | **Rare** | FL: D6 **6 only**, single unit, weekly. West: only in strong markets or via a named contact. |
| **Extremely Rare** | **Very Rare** | FL: D66 **65–66 only**, single unit, weekly. West: needs a major town, special amenity, mail order, or its own scenario. |

**Generic mechanism:** a 4-step ladder (Common → Uncommon → Rare → Very Rare) where each step *narrows where the item can be found* and *lowers the quantity restocked*. The resolution can be a die roll (FL's per-item D6/D66 with weekly restock) or a settlement-quality judgment (West's "does this town have the right amenity / Mercantile rank?"). **Layer:** General.

### 3.2 Settlement modifiers — availability shifts with place

**FL** folds settlement capacity into the economy prose: gold items become Extremely Rare + 1D6 weeks lead time in villages, and advanced-talent items (smith/bowyer/builder) may be unavailable outside towns/strongholds even on a successful supply roll. FL `10-gear.md:25, 28`.

**West** makes settlement capacity an explicit, combinable modifier set. Availability shifts **one step** up or down based on the town's tags (`06-life:507-516`): `Mercantile 1-2` → harder; `Mercantile 5-6` → easier; a `Railroad Station`/`Express Mail Route` → easier for legal manufactured goods (if you'll wait); a matching amenity (`Blacksmith`, `Doctor`, `Apothecary`, `Horse Traders`, `Attorney's Office`, `Federal Marshal's Office`) → easier for matching goods; `Law 5-6` → illicit goods harder or impossible openly; `Law 1-2` → illicit goods easier but fraud/theft likelier; `Welfare 1-2` → decent lodging/stabling/doctoring harder.

**West's "Strong Market" definition** (`06-life:526-541`): Mercantile 5–6, *or* Mercantile 4 + a Railroad/Express/major-trade advantage. In a strong market, Rare legal goods are openly buyable, one Very Rare good can at least be *located/ordered* without a side-adventure, and the buyer chooses ordinary price *or* immediate access (immediate = +one scarcity step). Strong markets are also *bounded*: two Rare purchases of one kind per week, one Very Rare, before the shelves thin and further same-kind purchases step harder.

**Generic mechanism:** the settlement is itself a *rated supplier*. A small set of tags (trade rank, transport link, specialist amenity, law level, welfare level) each shift availability by one step and *stack*. A "strong market" threshold unlocks Rare/Very Rare access but is rate-limited per buyer per week. **Layer:** General (the modifier concept); the specific tag set is genre work.

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

**Generic mechanism:** a 5-row price-adjustment table keyed to *how hard it was to find* (surplus → panic), applied after the availability roll succeeds. **Layer:** General. *Recommended port:* West's version (it includes the downward leg, which makes trade feel two-sided).

## 4. Economy models: the economy dial — **the central divergence**

This is where FL and West diverge most sharply, because the two genres have *opposite relationships to money*. FL is a post-collapse survival setting where coin is scarce and most exchange is personal; West is a frontier-cash-economy setting where dollars flow, credit exists, and property is a game.

### 4.1 The dial

| | **FL — barter + commodity silver** (`10-gear.md:21-28`) | **West — cash + capital + credit + wages** (`06-life:11-125`) |
| --- | --- | --- |
| **Daily currency** | Silver and copper for ordinary goods; **barter at face value** or a service obligation substitutes for coin. | **Dollars** (cash) for ordinary goods and services. |
| **Prestige / large currency** | **Gold is ceremonial** — marks prestige and patronage, *not* daily trade. Gold-priced items need a sponsor, special order, or rare caravan; in a village treat as Extremely Rare + 1D6 weeks lead time. | **Capital** ($250 = 1 point) — money tied up in property, businesses, investments. *Cannot buy ordinary gear* unless liquidated. No upper limit. |
| **Liquidation** | (implicit: spend the silver, swap the barter) | **Liquidating Capital** is risky and committed: roll D6 × $50 = $50–$300, decided once rolled, lose the underlying asset. |
| **Credit / debt** | (none — no banking layer) | **Loans**: 5%–10% interest per season, ≥1-year term, collateralized (land/home/farm/business), foreclosure on default; banks are fragile (fraud, robbery). |
| **Income** | (earned ad hoc: looting, favors, strongholds) | **Salaries** per season (table, $65–$300); −25% if board included. Plus **business/season rolls** and **hired-hands** day-wages. |
| **Property / stronghold** | Stronghold building (raw materials + labor + time, `10-gear.md:700-714`). | **Property Status 0–8** (Capital-priced), **Location Types**, **Property Features**, buying/selling/auction mechanics (`06-life:214-351`). |
| **Thematic load** | *Scarcity is the story.* Geography and isolation decide what you can have. | *Money is the story.* Cash flow, debt, investment, and reputation-through-property drive play. |

**Generic mechanism — the economy dial.** A setting picks, from a small menu, *which forms of value exist and how they convert*:

1. **Medium of daily exchange** — barter / commodity coin / fiat cash / scrip.
2. **Prestige or large-denomination store** — ceremonial gold (FL) / investment Capital (West) / none.
3. **Credit** — none / seasonal-interest loans with collateral / full banking.
4. **Income stream** — ad hoc looting / seasonal salaries / business rolls / rents.
5. **Property model** — stronghold-as-craft-project (FL) / property-as-rated-asset-with-Status (West) / none.

Each is independently toggleable. **Layer:** the dial is **core**; each sub-dial is a design choice.

**Design intent:** The economy model is not flavour — it *is* the genre's statement about what characters are struggling for. FL's barter+ceremonial-gold says "you will mostly not have money, and the things you want will be gated by *who you know and where you are*." West's cash+capital+loans says "money is available, but it comes with *obligations* — debt, investment risk, reputation — that are themselves the drama." A new genre's job is to decide whether its characters are *starved* of money (use the FL pole) or *managed* by money (use the West pole).

### 4.2 West's capital machinery — the deeper simulation

West is the only one of the two with a full *asset-and-business* simulation, and it is worth abstracting because it generalizes to any genre where *owning things* should matter (noble houses, trading companies, criminal empires, starship fleets):

- **Capital converts one way at a fixed rate** ($250 → 1 Capital) **but liquidates at a random rate** (D6 × $50). This asymmetry — *easy in, risky out* — makes investment a genuine decision, not a savings account. `06-life:21, 49`.
- **Capital is locked to its purpose**: invested-in-a-business Capital stays Capital but must be liquidated to move it; you can't shift it directly between assets (except the one-time starting-outfit merger). `06-life:43, 141`.
- **Businesses are rated by a key ability + prerequisites**, run by a named proprietor, pay seasonal wages scaled by invested Capital (+5%/point after the first), and earn **Business Bonuses** only on 2+ success season rolls — failure imposes a **Business Penalty**, and reaching 0 Capital = **gone bust**. `06-life:155-210`.
- **Property is a Status ladder (0–8)**, each step a Capital price, with build-cheaper-than-buy (but build costs *time*), Location Types controlling availability/cost, and a Features table (Forge, Oven, Stables, Library, Strong Room…) that gates business types and grants rolling bonuses. `06-life:230-307`.
- **Buying/selling is a haggle**: opposed PERFORMIN' vs INSIGHT, ±1 Capital per net success (min ½, max +50%); competitive bidding can overshoot value and the excess is *lost*. `06-life:332-350`.

**Generic abstraction — "the asset layer."** A subsystem where (a) a large-denomination currency converts in at a fixed rate and out at a random rate, (b) assets are rated by a linked ability and pay out on seasonal rolls, (c) owning property is a Status ladder with build-vs-buy trade-offs and prerequisite-gating features, and (d) transactions are haggle-able. **Layer:** Optional — include only in genres where *property and business* are intended to be a pillar of play. FL deliberately omits this entire layer (its "stronghold" is a craft project, not a financial instrument).

## 5. Crafting — the making layer

Both games gate *making things* behind the same four gates, in the same order: **you need the right skill/talent, the right workshop/tools, the right raw materials, and the right time.** FL exposes the full machinery in its gear tables; West folds most of it into the Availability/Quality system and the training rules. The structure is identical.

### 5.1 The four gates

| Gate | FL | West |
| --- | --- | --- |
| **Talent** | Every craftable item lists a **Talent**. No talent = the item is *simple* and anyone can make it; a listed talent (Smith, Bowyer, Tailor, Tanner, Builder, Chef, Poisoner, Lockpicker, Inventor…) makes it *advanced* and gates it. `10-gear.md:38`. Higher talent *ranks* unlock better materials and masterwork. `:741, 816-822`. | Crafting routes through the **MAKIN'** ability and the **smith/gunsmith/bowyer** talents; repairing weapon Conditions costs a Shift of effort by a talented character using MAKIN'. `06-life:846`. |
| **Workshop / tools** | Items list required **Tools** and sometimes a **Function** (forge, tannery, tailor shop, kiln, laboratory). **Missing the function/tool set = +50% time and −1 to the roll**; advanced items need a **specialist** present or they're impossible. `10-gear.md:40, 46-48`. | Outfits list **prerequisites** (a property *with a Forge*, *with an Oven*, farming land, a Claim, Stables…); without them the business roll suffers **−2**. `06-life:188, 605-613`. |
| **Raw materials** | Every item lists exact **Raw Materials** (½ Iron, 1 Wood, 2 Leather…) with fractional units; materials themselves are craftable (Iron Ore→Iron, Pelts→Leather, Wood, Stone, Glass…) and have their own supply/shelf-life. `10-gear.md:652-682`. | Gear is bought, not built from units, but the *Specialized Gear* table notes when equipment is prerequisite to a business (Farming/Mining/Panning equipment). `06-life:596-614`. |
| **Time** | Each item lists a **Time** (Quarter Day / One Day / Two Days / One Week…), assuming two Quarter Days of work per day; extra time = bonus to the roll. Large items (armor, crossbows, vehicles) need an **assistant**; each beyond the first shaves **25%** of time (min ½ at three). Armor needs **1–2 days fitting** (poor fit = −1 MOVE or −1 AR). **Seasonal work**: outdoor/heavy craft is +50% time in winter unless indoors. `10-gear.md:36, 50-54`. | Building property costs **seasons** of time (Status 3 = a season; Status 8 = four seasons). `06-life:232-242`. |

**Generic mechanism — "the making gate."** To make an item, satisfy four independent prerequisites — **talent, workshop, materials, time** — each of which can independently *block* the craft, *slow* it, or *penalize* the roll. Assistants and extra time are the two dials that trade resources for speed/quality. **Layer:** General (the four-gate structure); the depth of the material simulation is a dial (FL's unit-economy vs West's buy-it-ready-made).

### 5.2 The material-quality ladder (FL innovation)

FL alone makes *the material you make it from* a first-class dial. The metallurgy ladder (`10-gear.md:802-822`) is exemplary and generalizes: each step up the material ladder adds **+1 Weapon Bonus / Armor Rating** at the cost of a harder crafting roll (−2 to −6, halved by sufficient talent rank) and rarer supply:

| Material | Craft penalty | Effect | Talent floor |
| --- | --- | --- | --- |
| Iron (baseline) | — | — | — |
| Bronze/Brass/Silver | varies | can replace iron; masterwork capped at ½ bonus | varies |
| Wrought iron | −2 | +1 Bonus | Smith rank 2 halves penalty |
| Steel | −4 | +2 Bonus | Smith rank 3 halves penalty |
| Crucible steel | as steel + rare minerals | +2 Bonus, +1 MANIPULATION (beauty) | Smith rank 4 |
| Dwarven steel | −6 | +3 Bonus, rust-immune, tougher | Smith rank 4 halves penalty |

The same pattern repeats for leather/cloth (Buckskin / Wax-hardened / Glue-hardened / Glass-composite leather; Wool / Linen / Oilcloth / Silk / Silk-wool) and for alternative weapon materials (Bone = fragile; Flint = +1 damage). `10-gear.md:836-921`.

**Generic abstraction:** a *material ladder* where each tier trades crafting difficulty and scarcity for a +1 bonus, with a talent rank that halves the penalty — so *being a better craftsman literally lets you work better materials*. **Layer:** Optional (genre-dependent; include where *crafting depth* is a pillar — alchemy, cybernetics, starship components).

## 6. Weapon feature grammar — **the central reusable artifact**

> This is the file's key deliverable. The insight: **weapons are defined by a small set of composable tags, not by bespoke stat lines.** A longsword is not "a longsword" — it is `Edged, Pointed, Parrying, Half-Hand, Heavy` with Grip 2H, Bonus +2, Damage 3. Change one tag and you have a different weapon; the stat block barely moves.

### 6.1 The shared stat skeleton

Both games describe a weapon with a *fixed column schema* plus a *free-form tag list*. The schema holds the numbers; the tags hold the *feel*.

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

The two schemas are nearly isomorphic. The one structural difference: FL's BONUS is a pool of **Gear Dice** that *degrade when pushed* (a pushed roll drops the weapon's bonus by 1 per 💀 on a Gear Die, breaking it at 0) — so the weapon's potency is itself a depletable resource. West's ATTACK MOD is a flat modifier with no push-degradation; instead, weapons degrade via the **Condition** tables (§8) driven by Trouble. This mirrors the engine's core push-cost divergence (`00-engine-core.md` §6): FL's gear *is* the cost face; West's gear is taxed by a separate Trouble layer.

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
| **Ranged-specific** | **Load / Load x2**, **Ready**, **Windlass**, **Ranged (Blunt/Pointed)**, **Melee/Ranged**, **Loud**, **Misfire**, **High-Velocity**, **Shield-breaker** | Reload action economy, the pre-shot READY action, crit-table selector for ranged, thrown-melee hybrids, animal-fright, the misfire self-damage risk. `:498-524, 536`. |
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

**Generic mechanism — the three-layer tag model.** A weapon = (a) a **fixed stat block** + (b) a **stack of positive Qualities** (capped, trade-off-laden, maker-addable) + (c) a **stack of negative Conditions** (Trouble-driven, repairable, escalating to "broken"). This cleanly separates *what the weapon is* (stats), *what's good about it* (qualities), and *what's wrong with it right now* (conditions) — three things FL conflates into the single degrading Gear Bonus.

### 6.4 Generalizing the feature grammar — the recipe

> **Port this.** The grammar is more reusable than any stat line in either book.

**The fixed architecture (port as-is):**
1. **A weapon = a fixed column schema + a tag list.** The schema holds numbers (grip/action, attack bonus, damage, crit, range, ammo, cost, weight, supply). The tags hold *behavior*.
2. **Tags are small, composable, and each does exactly one thing.** Name the *behavior* (Edged = enables SLASH + selects Slash crits), not the *weapon* ("sword-like").
3. **Tags double as action prerequisites** where possible (FL's model): a tag *unlocks or gates a combat action* (Parrying → PARRY; Hook → SHOVE; Pointed → STAB). This binds the gear layer to the conflict layer (`03-conflict-and-damage.md`) and makes loadout a tactical choice.
4. **Cap and trade off positive tags** (West's max-4, stack rule) so optimization has a ceiling and every weapon has a *profile* rather than "all the good tags."
5. **Drive negative tags through the engine's existing failure layer** (FL: Gear-Die 💀 on push; West: Trouble), so degradation *reuses* the harm system rather than adding a new one. See §8.

**The genre dial — choosing the tag set:**
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

**Generic mechanism — "armor-as-tag-set."** Armor = (a) a **protection value** that either *rolls dice* against damage (FL) or *grants flat reduction/modifiers* (West), (b) a small set of **feature tags** for weight class, mobility cost, sense penalty, and special protection (cover, half-rating-vs-X), and (c) a **degradation rule** tied to the engine's harm layer. **Layer:** General. *Recommended port:* FL's rolling-AR-with-degradation is the more tactically interesting model and pairs naturally with the push-cost loop (a pushed attack can shred armor); use West's flat-reduction model for faster, lighter combat.

## 8. Quality tiers and condition/degradation

Both games layer a **quality** axis and a **condition/degradation** axis on top of the feature grammar. The two axes answer different questions: *how well was it made?* (quality, mostly fixed) vs *what shape is it in right now?* (condition, dynamic).

### 8.1 The quality ladder

| Tier | FL (`05-combat:462-470`) | West (`06-life:561-566`) |
| --- | --- | --- |
| **Low** | **Crude**: −1 BONUS (min +0); **breaks if Gear Bonus hits 0**; makeable with minimal facilities. | **Poor** (−25%): shoddy/second-hand; GM may rule it becomes Worn on first hard push. **Worn** (−10%): used hard but serviceable, one step closer to failing. |
| **Standard** | **Standard**: table as written. | **Standard**: listed price, solid frontier quality. |
| **High** | **Fine/Masterwork**: +1 BONUS, ×2+ cost, supply one step rarer; +1 MANIPULATION as a displayed status symbol; needs a specialist + proper tools. | **Fine** (+50%): better made/looking/resellable; counts as the one applicable +1 gear bonus *or* ignores the first Worn result from hard use (chosen when bought). |

The ladders align almost perfectly: Crude↔Poor, Standard↔Standard, Fine↔Fine. FL's Fine is *mechanically* stronger (+1 Gear Die, which is a real combat bonus); West's Fine is more *socially/economically* loaded (resale, the one-gear-bonus cap). West uniquely splits the low tier into **Poor** (badly made) and **Worn** (used hard) — distinguishing *origin* quality from *acquired* wear.

FL also applies quality to **rope and textile** separately (`10-gear.md:146-156`): Rough (½ lifespan, −25%, damages on 2💀/tears on 3💀) / Standard / Fine (double lifespan, +50%, doesn't wear from normal strain) — a model for any *consumable-adjacent* gear where lifespan, not performance, is the axis.

**Generic mechanism:** a 3-tier (or 4-tier) quality ladder where the low tier *breaks or fails first*, the high tier *adds a bonus and costs more + is rarer*, and the high tier optionally carries *social* value (MANIPULATION/resale/Fame). **Layer:** General (the ladder); whether the high tier grants a *combat* bonus (FL) or a *social/economic* one (West) is a dial.

### 8.2 The condition/degradation engine

This is where the two games diverge in *mechanism* while agreeing in *effect* — and the divergence tracks the core push-cost split (`00-engine-core.md` §6):

| | **FL — gear-as-cost-face** | **West — Trouble-driven Conditions** |
| --- | --- | --- |
| **Trigger** | Pushing a roll: each 💀 on a **Gear Die** drops the weapon/armor bonus by 1. Also: armor penetrated by damage loses 1 AR per 💀 rolled. | Trouble generated by rolled `1`s (the failure-pressure layer, `00 §10`); also the "becomes Worn on first hard push" Quality rule. |
| **Effect** | The Gear Bonus *degrades in real time during a fight*; at Bonus 0 the item is **broken** and needs CRAFTING to fix. | A Condition tag is applied (DIRTY/BENT/CHIPPED…), each a discrete penalty; repairable by a Shift of talented MAKIN'. |
| **Granularity** | Continuous (a counter ticking down). | Discrete (a named tag from a D6 table). |
| **Climax** | Broken at 0. | "Broken beyond repair" if Trouble strikes twice in one scene (WEAK HAMMER / WEAKENED). |

FL `05-combat:456, 654-656`; West `06-life:846, 885-905`.

**Generic mechanism — "the degradation layer."** A rule that *using gear under pressure makes it worse*, wired into the engine's existing failure mechanic (push-cost in FL, Trouble in West) so no new subsystem is needed. Choose **continuous-counter** (FL: bonus ticks down, repairs restore it) for granular, attritional pressure where gear *is* a resource pool; choose **discrete-tag** (West: named Conditions from a table, each a fixed penalty) for lighter bookkeeping and more *narrative* breakage ("the bore's damaged, it's low-powered"). **Layer:** General (some degradation rule); the mechanism is a dial tied to the push-cost model.

## 9. Artifact / legendary gear and the artifact die

FL alone has a **legendary tier** — gear so fine it doesn't roll normal Gear Dice, it rolls its *own* larger die. This is the gear-layer instance of the engine's escalating-success-die subsystem (`00-engine-core.md` §9).

### 9.1 The artifact die

FL artifacts grant a **D8 (Mighty) / D10 (Epic) / D12 (Legendary)** in addition to (or instead of) normal Gear Dice, read as **6+ = ⚔ with scaled multi-successes** (a D12 can yield up to 4 ⚔ on a 12). The bonus is rolled on the Artifact Bonus table (D66: 11–46 = D8, 51–63 = D10, 64–66 = D12). FL `10-gear.md:961-967`. **Artifact dice are never degraded by wear** — legendary gear is immune to the §8 degradation economy. `00-engine-core.md §9`. The artifact die is also a *craftable* ingredient for permanent magic items: a D8/D10/D12 artifact die costs 1/2/3 Power Levels (min total item PL 2/4/8). FL `07-magic.md:480`.

### 9.2 The artifact as a *named, oddity-bearing* object

FL artifacts are not just "a +2 sword." They are **named** (D66 prefix table: "Alur's…", "Brambolo's…"), **typed** (Skill artifact = adds the die to a skill; Combat artifact = weapon/armor/shield), and **oddity-laden** — every artifact carries a D66 **Oddity** that afflicts or aids the bearer only while possessed (`10-gear.md:1067-1106`): demonic faces that watch you, paranoid whispers, always-freezing cold, nightmares, telepathic complaint, the die that *varies by moon/season/time-of-day* (rows 64–66), the soul trapped inside whose personality bleeds into the bearer (row 33), the "discharge all power once, then explode" self-destruct (row 63).

**Generic abstraction — "the legendary tier."** An optional top tier of gear that (a) uses the **escalating-success-die** (D8/D10/D12, 6+ = ⚔, scaled, immune to degradation), (b) is **named and typed** rather than generic, and (c) carries a **quirk/oddity table** that makes possession itself a story — the item is *wanted and feared*, not just powerful. **Layer:** Optional — omit for grounded/low-power genres (West has no equivalent; its nearest analogue is the Faith metacurrency, a player-side pressure-relief dial, not a success-scaling die). Cross-ref `05-power-layer.md` (artifact dice as magic-item ingredient) and `00-engine-core.md §9` (the die itself).

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

**Generic mechanism:** a *single degrading die* replaces a unit-count for any consumable the genre wants to feel *scarce under pressure*. It converts "I have 14 arrows" into "my Arrow Die is D6, and every fight might shrink it." It is lighter than counting, more dramatic than tracking, and it makes *resupply* a meaningful event (stepping the die back up) rather than bookkeeping. **Layer:** Optional in West, default in FL — a **scope dial**. *Default it on* for survival/wilderness/expedition genres where logistics is a pillar; default it *off* (loose counting) for urban/cinematic genres where supply runs aren't the story. Either way, port the ladder as-is.

## 11. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Economy model** | Barter + commodity silver; gold ceremonial | Cash (dollars) + Capital + loans + salaries | Scarcity-as-story vs money-as-story | FL pole for survival/post-collapse; West pole for any genre where property, debt, or business is a pillar |
| **Large-denomination store** | Ceremonial gold (prestige, +lead time) | Investment Capital ($250=1; liquidates D6×$50) | Static prestige vs liquidatable-but-risky assets | Use Capital only if you want an *asset/business* subsystem; otherwise ceremonial-gold is lighter |
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
| **Degradation mechanism** | Continuous counter (Bonus ticks down on push 💀/penetration) | Discrete Conditions (named tags from D6 table, Trouble-driven) | Granular attrition vs narrative breakage | FL's counter when gear is a resource pool; West's tags for lighter bookkeeping |
| **Legendary tier** | Artifact die (D8/D10/D12) + named + oddity table | None (nearest analogue: Faith metacurrency) | Escalating-success-die + story-loaded items vs flat power ceiling | Include for fantasy/pulp; omit for grounded/historical |
| **Consumables tracking** | Resource dice as default (Arrows/Torches/Food/Tools) | Resource dice as Optional Module; loose counting default | Always-on logistics pressure vs opt-in survival mode | Default-on for wilderness/survival; default-off for urban/cinematic |
| **Crafting depth** | Full unit-economy (fractional raw materials, material ladder, masterwork) | Folded into Availability/Quality + business prerequisites | Deep simulation vs light resolution | FL depth when *crafting is a pillar*; West lightness otherwise |
| **Material-quality ladder** | Iron→Wrought→Steel→Crucible→Dwarven (+1 to +3, talent-gated) | (not present — quality is a buyable grade, not a craftable material) | Make-it-better-by-being-better vs buy-it-better | Port the ladder for any genre where *crafting mastery* should scale output |

## 12. Dials and instantiation recipe

Each dial has FL and West as two calibrated points. To build a new game's gear-and-economy layer, set each dial.

1. **Economy model** — barter+commodity / cash / cash+capital / multi-currency. *(Sets what characters struggle for. The single most tone-defining gear dial.)*
2. **Large-denomination store** — ceremonial prestige-gold / liquidatable Capital / none. *(Whether an asset-and-business subsystem exists.)*
3. **Credit** — none / seasonal-interest loans with collateral / full banking. *(Whether debt is a lever.)*
4. **Income stream** — ad hoc / seasonal salaries / business rolls / rents. *(How characters get money.)*
5. **Property model** — none / craft-project stronghold / rated-asset Status ladder. *(Whether owning things is a pillar.)*
6. **Availability resolution** — per-item die roll (random stock) / settlement-tag judgment (deterministic). *(How "can I buy it here?" is answered.)*
7. **Strong-market concept** — implicit / explicit threshold + rate limits. *(Whether trade feels finite.)*
8. **Scarcity → price curve** — one-sided (upward) / two-sided (surplus→panic). *(West's two-sided is the better default.)*
9. **Weapon stat model** — degrading Gear Dice (weapon-as-resource) / flat modifiers. *(Whether gear is itself a cost face.)*
10. **Feature grammar shape** — action-prerequisite tags (FL) / three-layer stats+qualities+conditions (West). *(How loadout drives play.)*
11. **Quality ladder** — 3-tier / 4-tier (split low); high-end = combat bonus (FL) / social bonus (West). *(What "Fine" means.)*
12. **Degradation mechanism** — continuous counter (FL) / discrete Conditions (West). *(How gear gets worse — must match dial 9 and the push-cost model from `00 §6`.)*
13. **Legendary tier** — on (artifact die + oddities) / off. *(Power ceiling; omit for grounded genres.)*
14. **Consumables tracking** — resource dice default-on / default-off (loose counting). *(Whether logistics is always-on or opt-in.)*
15. **Crafting depth** — full unit-economy + material ladder / folded into availability. *(Whether making things is a pillar.)*

**Instantiation recipe (any genre):**
1. **Set the economy model (dial 1)** first — it does more to set the *feel* of gear than any other choice. Decide whether your characters are *starved* of money (FL pole) or *managed* by it (West pole).
2. **Decide the property/asset layer (dials 2–5)** as a block: include Capital+loans+salaries+property *only* if owning/business/debt is intended to be a pillar. Otherwise strip it all (FL).
3. **Port the availability/scarcity table (dials 6–8)** near-verbatim from §3 — it is shared machinery. Default to West's settlement-tag + two-sided-price version.
4. **Choose the feature grammar shape (dial 10)** — this is the central design decision for *gear feel*. Use FL's action-prerequisite tags if loadout should unlock tactical options; use West's three-layer model if you want clean positive/negative optimization. In either case, port §6.4's architecture.
5. **Align the weapon-stat, degradation, and push-cost models (dials 9, 12, and `00 §6`)** — these *must* be consistent: degrading Gear Dice pair with bane-self-harm; flat mods + Conditions pair with currency-spend + Trouble.
6. **Set quality + condition + legendary (dials 11, 13)** to the genre's power ceiling and grit level.
7. **Set consumables tracking (dial 14)** to the genre's logistics appetite (default-on for survival, default-off for cinematic).
8. **Decide crafting depth (dial 15)** and, if deep, port the material-quality ladder (§5.2).
9. **Validate against the math** (see `13-balance-and-synergy.md`): expected weapon damage per round, time-to-Broken, degradation rate vs repair cadence, resource-die exhaustion length for a typical expedition, salary-vs-lifestyle cash flow over a season.

## 13. Design intent

The gear-and-economy layer is engineered so that **what a character carries and what a character is worth are both load-bearing fiction**, not bookkeeping. Specifically:

- **The feature grammar makes gear *feel* different, not just numerically different.** A dagger and a shortsword have the same Damage and Bonus; what separates them is `Short-reach, no Parrying` vs `Parrying, Tough`. Tags carry *meaning* — and because tags double as action-prerequisites (FL) or stack into a profile (West), loadout becomes a *tactical and expressive* choice rather than a DPS optimization. This is why the grammar is the file's central deliverable: it is the part of the system that survives any reskin.
- **The availability table makes *geography* matter.** Scarcity is not a price modifier tacked on at the end — it is the rule that *decides whether the item exists at all* in this settlement, and the settlement's tags (Mercantile, Law, amenities, railroad) make the world's map a gear-gating surface. You can't get a fine rifle in a town with no gunsmith; you can't get illicit goods openly where Law is 5–6. The world *is* the shop.
- **The economy model *is* the genre's statement about value.** FL's barter+ceremonial-gold says scarcity and isolation are the story; West's cash+capital+loans says money, debt, and reputation are the story. The same engine produces opposite tones by swapping the currency — exactly as the core loop does by swapping the push-cost model (`00 §12`). A new genre must find *its* relationship to money and wire the dial to it.
- **Crafting takes in-fiction time and gates**, so it ties into the downtime/season loop (`06-travel-and-downtime.md`) rather than being a between-combat menu. The four gates (talent, workshop, materials, time) and the material ladder mean *being a better craftsman literally produces better goods* — mastery has a material payoff.
- **Quality + condition + degradation make gear a *lived* object.** A Fine sword that you've kept Fine, a Standard one now Worn, a Crude club about to snap — these tell the character's history. And because degradation is wired to the engine's existing failure layer (push 💀 / Trouble), *gear wears out for the same reason characters get hurt*, unifying the pressure.
- **The legendary tier (artifact die + oddities) makes top-tier gear *wanted and feared*, not just owned.** A +2 sword is forgettable; "Alur's Cloak, which whispers paranoid fantasies and grows stronger in the wilderness" is not. The oddity table is the proof that *a magic item is a story, not a stat*.
- **Consumables-as-resource-dice convert logistics into drama.** "I have 14 arrows" is bookkeeping; "my Arrow Die is D6 and every fight might cost me a step" is a gamble. It is the consumables analogue of the push: each use is a small decision with a real downside, and resupply becomes an event rather than a line item.

The divergence between FL and West is the engine's proof that **the same availability table, feature grammar, and quality ladder support opposite genres by changing the economy dial and the degradation mechanism.** FL's degrading Gear Dice and barter economy make a game where *your body and your axe are the same kind of scarce*; West's flat mods, Conditions, and cash+capital make a game where *your gun and your wallet degrade by different logics*. A new genre's job is to choose, for each dial, which logic its world runs on — and the grammar, the table, and the ladder will port unchanged.
