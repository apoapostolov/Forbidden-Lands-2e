#!/usr/bin/env python3
"""
Replace single-paragraph RESOURCES blocks in 02-gamemasters-guide/06-bestiary.md
with 3-item bold format. Abyss Worm (block 1) and Death Knight (block 4) are
already updated; this script handles the remaining 21 blocks.
"""

import re
import sys

PATH = "02-gamemasters-guide/06-bestiary.md"

# Each entry: (unique_anchor_in_old_block, full_new_block_text)
# The anchor is a unique substring from the current (old) RESOURCES paragraph.
REPLACEMENTS = [
    # 2. Bloodling
    (
        "A manifest bloodling put down with copper leaves a dark red residue",
        """> **RESOURCES**
>
> Bloodling matter holds its scent and memory long after the creature dissolves. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **bloodling-ichor**, **blood-film**, or **scent-node**.
>
> **Bloodling-ichor.** A dark-red fluid that smells of wet iron. A dose burned as incense draws the nearest bloodling within NEAR range toward the smoke within one Quarter Day — useful as bait, or as a warning that more are close. A dose rubbed onto the hands lets the bearer handle a dying or dead creature without nearby bloodlings reacting; a careless second dose on the same day draws three bloodlings from any direction.
>
> **Blood-film.** The dried exterior membrane of the creature, translucent and rust-red. Rubbed across the eyelids before sleep, it shows the bearer, in dream, every place where mortal blood soaked ground, stone, or linen within the past Quarter Day and within SHORT range. The bearer's own eyes weep red for the rest of the following day, and nothing about the vision is accurate after the first watch of the dream.
>
> **Scent-node.** A gland from the creature's interior, smaller than a walnut. Sealed in a clay pot and buried at a threshold, it keeps all bloodlings from crossing that line for one season. Broken open, the raw gland calls D3 bloodlings to the smell in one stretch. The Rust Brothers will pay silver for intact nodes and ask nothing about where they were found.""",
    ),
    # 3. Demon
    (
        "Demon matter rarely keeps its shape, but fresh mog, splintered horn",
        """> **RESOURCES**
>
> Demon matter is dangerous, coveted, and illegal in most settlements. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **mog**, **ground horn**, or **demon-ichor**.
>
> **Mog.** The raw demonic substance from the slain demon's body. One dose replaces a rare ingredient in any Demonic Magic ritual or potion that calls for a demon-touched component. The Raven Sisters confiscate it on sight; the Rust Brothers pay silver for it and ask no questions. No third use is documented without lasting consequence.
>
> **Ground horn.** One horn powdered by a SMITH over a Quarter Day. Stirred into blood-wine, a dose grants +2 Strength for one scene; when the scene ends, the Strength fades and the drinker rolls a random critical injury as the body pays what the demon lent. A second dose in the same day means the critical injury rolls twice and the GM keeps the worse result.
>
> **Demon-ichor.** A thick black fluid from the demon's veins. A dose mixed into a hearth-fire makes the fire burn without visible light and without heat but without going out for one Quarter Day; it is used in wards to hide a threshold from demonic sight. A dose swallowed raw grants the drinker one unambiguous answer about the nearest demon within SHORT range — its location, its hunger, or its binding. The drinker bleeds from the mouth for the rest of the day.""",
    ),
    # 5. Dragon
    (
        "Dragon flesh is harvested in the hour after the kill",
        """> **RESOURCES**
>
> Dragon flesh does not stay dead; it transforms. An adventurer with the ALCHEMIST or SMITH talent, with a HEALING or CRAFTING roll, draws one of the following per ⚔️ rolled, player's choice: **dragon's blood**, **dragon's scale**, or **dragon's tooth** — one dose per ⚔️ from a small dragon, one dose per two ⚔️ from a great dragon.
>
> **Dragon's blood.** The canonical alchemical ingredient for **Elixir of Life** (see the Corebook). A phial drunk raw restores D3 points of any one attribute lost in the fight and cures the Sick condition; the drinker runs a high fever for one Quarter Day after, which cannot be cured and must pass on its own. A second phial the same week kills. Blood kept out of a sealed flask goes to grey ash in two days.
>
> **Dragon's scale.** The canonical alchemical ingredient for **Tincture of Earth-Hide** (see the Corebook). One intact scale given to a SMITH of Rank 3 or higher counts as one Valuable Find toward a superior commission. A matched set of nine scales, worn as corselet or helm by a SMITH's art, raises Armor Rating by 3 against fire for one full season; the scales crack and fall away when the season ends. The Iron Guard recognizes dragon-scale work and will ask how it was obtained.
>
> **Dragon's tooth.** The canonical alchemical ingredient for **Tooth Powder of the Stoneborn** (see the Corebook). One tooth set into a weapon haft by a SMITH adds a D10 Artifact Die to the first attack roll in any fight; the tooth cracks at the end of the fight and the bonus is gone. Any dwarf-hold within reach will pay two gold for a whole tooth and ask no questions about the dragon it came from.""",
    ),
    # 6. Drakewyrm
    (
        "The drakewyrm's stomach acid is the primary harvest",
        """> **RESOURCES**
>
> The drakewyrm's acid and its scales are tools for anyone who knows the price of each. An adventurer with the ALCHEMIST talent, with a CRAFTING roll, draws one of the following per ⚔️ rolled, player's choice: **stomach acid**, **scale-dust**, or **drake-musk**.
>
> **Stomach acid.** The canonical alchemical ingredient for **Intoxicating Decoction** (see the Corebook). A dose poured on a sleeping humanoid wakes them in a state of confused, good-natured willingness for one scene; all MANIPULATION rolls against them gain a D8 Artifact Die during that scene. The acid must be stored in sealed clay or glass; any other vessel gives way within a stretch.
>
> **Scale-dust.** Ground from the drakewyrm's outer scales. A dose scattered on a person, weapon, or beast marks it until the next rainfall: any drakewyrm, wyvern, or small dragon sighting the marked target in a fight will attack it in preference to any other. Mixed into an oil-based paint or dye by a CRAFTER, it produces a pigment that does not dim under torchlight; one jar sells for D6 silver to any herald, alchemist, or guild artisan willing to ask no questions about the source.
>
> **Drake-musk.** A glandular oil from the belly skin, bitter and rank. Rubbed on boots and cloak hem before travel, it keeps all natural lizards, serpents, and minor drakes from approaching the bearer for one journey leg; larger drakes and drakewyrms are merely delayed, not deterred. The smell lingers three days after application and makes horses uneasy.""",
    ),
    # 7. Ent
    (
        "Ent sap runs clear and sweet in the hour after the kill",
        """> **RESOURCES**
>
> Fallen splinters, sap, and heartwood from a slain Ent hold old green strength and old green grief. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **ent sap**, **heartwood fragment**, or **bark-shaving**.
>
> **Ent sap.** A bright green fluid that smells of old forest rain. A dose poured into a shared cup cures the Thirsty condition for every adventurer within ARM'S LENGTH of the draught in one stretch — not one drinker, but all. A dose poured on a fresh-cut stump raises a hand's breadth of new bark and new leaves by sunrise. Villagers who see the stump know what the bearer has done and will tell the Ents, eventually.
>
> **Heartwood fragment.** A dense red-brown chip from the oldest core of the trunk. Set into a weapon haft by a CRAFTER, it grants that weapon a D8 Artifact Die on the first attack roll of every combat for one natural season; at season's end the heartwood cracks and the weapon is ordinary again. The elves know heartwood craft when they see it; encountering them while carrying such a weapon may cost something unexpected.
>
> **Bark-shaving.** A broad curl of outer bark, taken after the sap is extracted. Dried and ground into a powder by an ALCHEMIST, it can be burned on a fire to call the attention of any Ent within NEAR range of the smoke. The ent comes curious, not friendly; what it does when it arrives is the GM's work. A pouchful added to a stronghold wall's mortar strengthens it against fire for one full winter.""",
    ),
    # 8. Ghost
    (
        "Gravefrost is scraped from the cold place where the ghost last walked",
        """> **RESOURCES**
>
> Ghosts leave nothing that can be cut. What remains is the place: frost on a hinge, dust that will not settle, the last object the dead touched. An adventurer with the ALCHEMIST talent, with an INSIGHT roll at the place of rest, draws one of the following per ⚔️ rolled, player's choice: **gravefrost**, **cold-seam dust**, or **echo-fragment**.
>
> **Gravefrost.** Cold crystals scraped from the threshold, stones, or furniture of the place where the ghost lingered. A dose sealed in wax and carried preserves any corpse or cut meat for one full season with no rot or decay. A dose burned in an oil lamp makes any recently dead person audible through the flame for one Quarter Day if she has something unsaid; when the flame goes out, she goes with it.
>
> **Cold-seam dust.** Fine grey powder from the crack or doorframe where the ghost passed through solid matter. Added to any potion that restores Empathy, it doubles the Empathy restored; the drinker sleeps one extra Quarter Day afterward and speaks in an unfamiliar accent for the rest of the day. A dose rubbed onto a doorstep makes the ghost unable to pass that threshold for one full night.
>
> **Echo-fragment.** A small object — a coin, a button, a bone ring — that the ghost held or wore in its previous life, found by INSIGHT at the place of rest. Carried, the bearer can hear the ghost's last repeated thought whenever they are within NEAR range of the ghost's territory. Sold to a Raven Sister: she will use it for a binding. Sold to a Rust Brother: he will use it for something worse.""",
    ),
    # 9. Giant
    (
        "Giant blood is the named ingredient of the alchemical preparation called",
        """> **RESOURCES**
>
> A slain giant feeds a great many crafts. An adventurer with the ALCHEMIST talent, with a HEALING roll and a fire large enough for the work, draws one of the following per ⚔️ rolled, player's choice: **giant's blood**, **bone tooth**, or **beard-braid**.
>
> **Giant's blood.** The canonical alchemical ingredient for **Drops of Strength** (see the Corebook). A dose drunk raw restores D3 Strength at the end of the scene; when the Strength fades after the next rest, the drinker rolls once on the critical injuries table for blunt force, unmodified. Blood goes cold and useless after one stretch unless sealed.
>
> **Bone tooth.** A fang the size of a forearm, root intact. One tooth set into a club or war-hammer by a SMITH adds +2 Weapon Damage for as long as the tooth holds; the tooth cracks on any push and shatters at the end of the next fight that uses it. Skalds pay D6 silver for a single verifiable molar.
>
> **Beard-braid.** A thick plait of beard-hair cut from a full-grown giant and wound tight by a CRAFTER. The braid holds where hemp breaks and hauls four times its weight without fraying — one braid can drag a laden cart out of deep mud or pull a man and horse out of a crevasse. It lasts one season before rotting.""",
    ),
    # 10. Giant Squid
    (
        "Cave squid ink is drawn from the sac in the mantle",
        """> **RESOURCES**
>
> A cave squid's ink and its strange eyes each carry the dark they lived in. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **squid ink**, **eye-lens**, or **sucker-strip**.
>
> **Squid ink.** A thick black fluid that mixes with water but not oil. Mixed into a black oil and poured on the surface of still water up to LONG range across, the ink holds that water in full darkness for one Quarter Day — infrared vision reads through it, torchlight and sunlight do not. A dose applied to rope or leather before a battle makes it invisible in dark water or shadow for one combat.
>
> **Eye-lens.** One intact lens, removed before the body cools. Held against the eye like a coin and pressed to the brow, it gives the bearer full sight in complete darkness for one scene and then clouds over, spent. During that scene all MARKSMANSHIP, SCOUT, and SNEAK rolls under dark sky or in deep stone gain a D8 Artifact Die. The bearer's own eyes weep clear fluid for one full day afterward and will not bear sunlight without a hood.
>
> **Sucker-strip.** A band of adhesive skin from one of the larger tentacles. Wound around a boot or glove, it allows the wearer to grip wet stone, ice, or a ship's hull without a MOVE roll for one Quarter Day, after which the adhesive dries and the strip falls away. Used as a bandage, it seals a bleeding wound and holds for one stretch without slipping, but pulling it off reopens the wound for 1 Strength.""",
    ),
    # 11. Gray Bear
    (
        "Gray bear fat is rendered from haunches and neck-glands",
        """> **RESOURCES**
>
> Gray Bear fat holds its heat in the skin long after death. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **bear fat**, **claw-cap**, or **bile sac**.
>
> **Bear fat.** A dense yellowish grease rendered from the haunch and throat. Worked into a traveller's cloak, boots, and hood at the end of a Quarter Day's rest outdoors, it cures the Cold condition immediately and grants the wearer full Cold immunity for the following night, no matter the weather. A second application within a day sours the fat and causes a painful rash; the rash fades in three days but the Cold immunity with it.
>
> **Claw-cap.** A horn tip cut from one of the bear's major claws; D3 per kill. Lashed onto the head of an arrow or spear-point and used to draw first blood on any creature of flesh, it provokes in that creature the same patient, terrible stalking the Gray Bear shows its chosen prey: the wounded creature follows the bearer wherever she goes — night by night, pacing her doorways and waiting at her windows — until the cap is washed off in snow-water. The bearer decides whether to feed it, fight it, or let it find her.
>
> **Bile sac.** The gallbladder of the bear, its contents a thick, nearly black fluid. A dose added to a CHEF's campfire meal grants every diner a D8 Artifact Die on SURVIVAL rolls in cold terrain for the next day. A dose rubbed on a trapper's snares makes them undetectable by SCOUTING for one stretch; wolves and foxes will not approach a snare so treated.""",
    ),
    # 12. Gryphon
    (
        "Gryphon pinion-feathers are the primary harvest",
        """> **RESOURCES**
>
> Gryphon pinion-feathers, talons, and crop-stones each find a use. An adventurer with the ALCHEMIST talent, with a CRAFTING roll, draws one of the following per ⚔️ rolled, player's choice: **gryphon pinion**, **talon-pair**, or **crop-stone**.
>
> **Gryphon pinion.** The canonical alchemical ingredient for **Quick Nectar** (see the Corebook). A single pinion lashed to a ranged weapon by a CRAFTER grants a D8 Artifact Die to the first MARKSMANSHIP roll made with it on any day; the feather burns clean after three such shots. A pinion carried as a trophy in gryphon country marks the bearer as a proven hunter; gryphon-breeders of the Iron Guard will make an offer for it.
>
> **Talon-pair.** Two large primary talons, dried and ground over one Quarter Day. A dose of ground talon mixed into fresh horse-blood and fed to a mount drives that mount into a charging rage against the first gryphon it sees and renders it useless for any other task until it either survives the fight or is put down. Ground and mixed into boot leather instead, one dose gives MOVE rolls a D8 Artifact Die when climbing cliff faces or scrambling over loose rock, for one journey leg.
>
> **Crop-stone.** A smooth pebble swallowed in place of grit, one per kill, found in the crop alongside half-digested horse. Carried loose in a belt pouch, it vibrates faintly within ARM'S LENGTH of any bird of prey larger than a raven; useful to gryphon-hunters approaching a nest blind. Given to a breeder of warhorses, it calms a horse who has scented gryphon for one Quarter Day; breeders in gryphon country will pay a silver for one in good faith.""",
    ),
    # 13. Harpies
    (
        "Harpy voice-ash is the most sought-after harvest",
        """> **RESOURCES**
>
> A slain harpy yields feathers, throat-stones, and a long grey tongue. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **voice-ash**, **throat-stone**, or **plume-oil**.
>
> **Voice-ash.** Ground from the dried tongue and throat of a slain harpy. A pinch placed on the tongue lets the bearer imitate any one voice she has heard within the past Quarter Day, down to breath, hesitation, and rhythm, for the length of one conversation; all MANIPULATION, PERFORMANCE, and DECEIT rolls within that conversation gain a D8 Artifact Die. Voice-ash used twice in the same day leaves the bearer's own voice indistinguishable from a raven's cry for the rest of that day; no village will open a door to the sound.
>
> **Throat-stone.** A small smooth nodule from behind the harpy's tongue, one per flock member put down. Held in the mouth while the bearer sleeps, the stone brings the face of one person she has wronged into the dream. She may ask one honest question and must answer one in return; the stone dissolves on her tongue before waking, taking the dream-face with it. A throat-stone saved unswallowed keeps for one fortnight before it rots.
>
> **Plume-oil.** A waxy oil from the base of the wing feathers, one dose per flock of six or more. Rubbed over the eyes before approaching a harpy flock in the field, it suppresses the bearer's smell and fear-sweat for one scene; the flock will not immediately single out the bearer as prey unless she attacks first. Used as lamp oil, it burns without smell and without smoke, which is how the older Raven orders mark their own shrines at night.""",
    ),
    # 14. Hydra
    (
        "Hydra blood is counted by the head",
        """> **RESOURCES**
>
> Hydra blood still fights in the cup. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **hydra's blood**, **spent acid**, or **neck-scale**.
>
> **Hydra's blood.** One dose per head remaining at the moment of death. The canonical alchemical ingredient for **Healing Water** (see the Corebook). A dose drunk raw restores D3 Strength and regrows a single severed finger, toe, or ear over the following Quarter Day; the regrown part is one shade too pale and does not warm in cold. Brewing hydra blood requires a sealed cauldron with a lid that can be sat upon; if the HEALING roll fails, the brew grows small teeth and bites the alchemist for 1 Strength before the vessel cracks.
>
> **Spent acid.** The fluid remaining in a spit-gland after a combat. The canonical alchemical ingredient for **Refreshing Decoction** (see the Corebook). A dose rubbed onto a leather strap or wood handle before a journey prevents the item from rotting, cracking, or softening in any wet for one full season.
>
> **Neck-scale.** One scale from the seam between a head and the neck, where the hide is thinnest. Set into the inside face of a shield by a CRAFTER, it adds +1 Block Value against bite attacks and acid for one season; at season's end it flakes off. Ground to dust and blown across still water, a pinch will show the outline of any hydra below the surface within NEAR range as a shimmer for one round — useful to watermen who know the sign and fatal to those who do not.""",
    ),
    # 15. Insectoids
    (
        "Insectoid soldier venom is a paralytic of considerable potency",
        """> **RESOURCES**
>
> An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **soldier venom**, **worker blood**, or **queen's honey** (one pot per queen slain — no more).
>
> **Soldier venom.** A paralyzing poison of Potency 8 drawn from the soldier caste's sting. Unlike most poisons, soldier venom does not degrade for a full season; it can be stockpiled. A dose can coat a single blade edge, arrow-point, or caltrops for one use each. The Rust Brothers will purchase intact venom phials and never ask for the colony's location unless they already know it.
>
> **Worker blood.** A pale brown fluid, the canonical alchemical ingredient for **Honey of Embers** (see the Corebook). A dose added to a CHEF's meal grants the diner a D8 Artifact Die on the next STAMINA or ENDURANCE roll against exhaustion, heat, or sustained effort. Carrying worker blood through a living colony is taken as a declaration of war; no quiet exit is possible.
>
> **Queen's honey.** One pot per queen slain, no more. The moment the pot is opened, it smells of childhood to every person within ARM'S LENGTH — each in a different way, each in her own memory. A full pot fully restores Empathy and cures the Hungry condition for every person within ARM'S LENGTH at that moment. A pot kept sealed for a season turns to a black resin that the colony can smell from a full day's travel.""",
    ),
    # 16. Manticore
    (
        "Manticore venom and blood are both valuable",
        """> **RESOURCES**
>
> Manticore barbs, venom glands, and the triple row of teeth each have a use. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **manticore blood**, **tail venom**, or **tooth-row**.
>
> **Manticore blood.** The canonical alchemical ingredient for **Calming Decoction** (see the Corebook). A dose drunk from a man's cupped hands — not a cup — suppresses the drinker's fear, rage, and immediate flight-response for one full Quarter Day; she cannot be frightened, panicked, or goaded into unplanned action. At Quarter Day's end, every suppressed emotion returns at once and she makes one untriggered INSIGHT roll or suffers its consequence.
>
> **Tail venom.** A paralyzing poison of Potency 8, drawn from the crushed gland. Unlike barb-venom, the rendered liquid does not degrade for one season. A dose loaded into a weapon coating paralyzes on hit for one stretch; a second dose on the same weapon corrodes the blade and ruins both. A single intact tail barb, if taken without crushing the gland, can be thrown by hand as a ranged attack with Weapon Damage 2 and full Potency 8 paralytic; no skill required, one use, and the thrower can recover the barb with a SCOUTING roll if she misses.
>
> **Tooth-row.** A full row of triple-staggered teeth cut from the jaw, one row per kill. Set by a SMITH into the edge of a saw, axe, or heavy chisel, the row halves the time needed to cut wood, bone, or frozen flesh for one Quarter Day; the row cannot be reset or reused once it has worked a full Quarter Day.""",
    ),
    # 17. Minotaur
    (
        "Minotaur horn powder is prized for its strength-granting properties",
        """> **RESOURCES**
>
> Minotaur horn and marrow are the most prized parts. An adventurer with the ALCHEMIST talent, with a CRAFTING roll, draws one of the following per ⚔️ rolled, player's choice: **horn powder**, **minotaur marrow**, or **hide-patch**.
>
> **Horn powder.** Powdered horn from a slain minotaur, D3 doses per kill. Stirred into blood-wine, one dose grants +2 Strength for one scene; for that scene the drinker's Empathy drops to 1, she is immune to fear and to MANIPULATION, and her allies must succeed on an INSIGHT roll to be certain she still knows them. At scene's end the Strength and the loss both fade. A whole horn still attached to its brow-plate can be carved into a drinking-cup by a CRAFTER; liquid drunk from that cup cannot be poisoned by any alchemical or natural venom of Potency 6 or lower while the cup holds it. The cup lasts one year before it splits.
>
> **Minotaur marrow.** A thick fluid pressed from the long bones over one Quarter Day of ALCHEMIST work. A dose stirred into a paste and packed into a fresh wound stops bleeding and restores D3 Strength at the scene's end; the wound seals but does not heal — it aches and stiffens for a full day afterward. A dose added to a smith's metalwork makes iron forged that day hold its edge one season longer than the SMITH's craft alone would allow.
>
> **Hide-patch.** A palm-sized piece of minotaur hide, thick as doubled leather. Stitched onto leather armor or a shield by a CRAFTER, it raises that piece's Armor Rating by 1 against blunt attacks for one season before it cracks. The smell of it unnerves any natural bovine within ARM'S LENGTH; milk cows will not stay in a barn where it is stored.""",
    ),
    # 18. Nightwargs
    (
        "Nightwarg shadow-residue must be collected before dawn",
        """> **RESOURCES**
>
> A slain nightwarg dissolves at dawn, but a careful alchemist can preserve what remains of the dark. An adventurer with the ALCHEMIST talent, with a SURVIVAL roll before sunrise, draws one of the following per ⚔️ rolled, player's choice: **night-shadow**, **frost-saliva**, or **pale-eye membrane**.
>
> **Night-shadow.** A dark, oily residue scraped from where the nightwarg dissolved. Must be stored in a horn-and-tallow vessel sealed by hot wax; in any other flask, it escapes and returns to the dark by the next dawn. A dose brushed onto a cloak before nightfall grants a D10 Artifact Die to all STEALTH rolls and attempts to move unseen for one full night, under any sky without direct sun. The bearer's eyes are pale as full moons from dusk to dawn; any sworn Iron Guard who sees the eye-mark takes it as cause to hang.
>
> **Frost-saliva.** Taken from the glands in the warg's jaw before the body dissolves; one dose per kill. Swallowed, it makes the drinker's breath plume visibly cold even in summer and lets any bite she makes with weapon, tooth, or tool leave a crackling frost on the wound for the following Quarter Day. Fresh-frozen blood is easier to preserve in transit and easier to read by a tracker or augur who knows the sign.
>
> **Pale-eye membrane.** The thin inner eyelid of the nightwarg, which sees in total darkness. Pressed over one eye and sealed with a drop of wax by an ALCHEMIST, it grants full sight in complete darkness for one scene; during that scene all SCOUTING rolls in total darkness gain a D8 Artifact Die. At the scene's end the membrane dries and falls away. The eye it covered is pale for D3 days after, drawing stares in every village.""",
    ),
    # 19. Sea Serpent
    (
        "Sea serpent gall is the named ingredient of the alchemical preparation",
        """> **RESOURCES**
>
> Sea serpent tail-glands, gall, and crown-horn each have long-standing uses. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **serpent's gall**, **tail-gland fluid**, or **crown-horn**.
>
> **Serpent's gall.** The canonical alchemical ingredient for **Quenching Swig** (see the Corebook). A dose drunk raw at sea or in fresh water after a submersion calms the belly and grants the drinker a D8 Artifact Die on the next ENDURANCE roll against drowning or hypothermia. Kept sealed in a tallow-stoppered flask, it holds without souring for one season.
>
> **Tail-gland fluid.** A potent hormonal oil from the serpent's genital glands. A dose poured into any still water up to SHORT range draws every sea serpent, water drake, or drowning dead within NEAR range toward that water for one full hour. A CHEF can render D6 units of FOOD from the tail blubber by the usual method, separately; the tail-gland fluid is not edible.
>
> **Crown-horn.** A single hollow spur from above the serpent's eyes, one per kill. Carved into a whistle by a CRAFTER over one Quarter Day, the horn will, once and once only, call the next living sea serpent under that stretch of water to the surface when blown. Whether the serpent comes as a friend or a meal is the serpent's own judgment. The whistle crumbles after the one call and cannot be remade.""",
    ),
    # 20. Strangling Vine
    (
        "Strangling vine spores are a paralytic poison of considerable potency",
        """> **RESOURCES**
>
> An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **violet spores**, **root-fibre**, or **flower-extract**.
>
> **Violet spores.** A paralytic poison of Potency 8, drawn from the sensory flowers. Two doses brewed together by an ALCHEMIST with a HEALING roll reach Potency 12 for a single preparation; no further stacking is possible without the brew souring. The spores serve as the rare ingredient in any sleep-draught recipe. A single dose used as a weapon coating affects the target for one full stretch; the vine harvested for its spores will not regrow any flowers for a full season.
>
> **Root-fibre.** A fibrous cord cut from the root network of the central trunk, one basket per adult vine. With a CRAFTING roll by a CRAFTER, ten feet of root-fibre can be woven into a living rope. A living rope will strangle any living thing bound in it over one full day, ignoring 3 points of Armor Rating and keeping its victim from sleep, food, and water until she is cut free or the rope is burned. Carrying a living rope is not unlawful; settlements that know what it is close their gates to it.
>
> **Flower-extract.** A sticky purple oil pressed from the intact blossoms before they are harvested for spores. A dose rubbed on the ground around a campsite draws the nearest strangling vine toward the scent within one Quarter Day — useful bait for a vine-hunter who knows what she is doing and fatal for everyone else. Sealed in a pine-resin vial and burned in a lantern, the oil attracts every natural insect within SHORT range and keeps them circling the light for one stretch; herbalists in vine country use this to locate hidden colonies by swarm-path at dusk.""",
    ),
    # 21. Troll
    (
        "Troll bile is the most widely known of the troll harvests",
        """> **RESOURCES**
>
> An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **troll's blood**, **troll's gastric juice**, or **troll's tooth**.
>
> **Troll's blood.** The canonical alchemical ingredient for **Healing Decoction** (see the Corebook). A dose rubbed into an open wound restores D3 Strength at the end of the scene and holds any disease contracted in that fight at its current Virulence for one day, giving the afflicted time to seek treatment. A second dose within the same Quarter Day causes violent spasms instead of healing.
>
> **Troll's gastric juice.** The canonical alchemical ingredient for **Aqua Fortis of the Smiths** (see the Corebook). A dose poured onto worked iron eats through it in one stretch: a shackle, a lock, a sword-blade, or a gate-hinge dissolves and falls open without sound. The Iron Guard hangs anyone found carrying it without a SMITH's guild-mark.
>
> **Troll's tooth.** The canonical alchemical ingredient for **Elixir of Wisdom** (see the Corebook). A tooth given to a dwarven SMITH of Rank 2 or higher is a Rare Find in ore; in the forge, it reforges a broken weapon to full Weapon Damage at no iron cost. The SMITH who works it tastes what the troll last ate. This is why dwarves rarely share the method.""",
    ),
    # 22. Undead (Restless Dead / Skeleton / Ghoul)
    (
        "Grave-salt is scraped from the places the undead tread most heavily",
        """> **RESOURCES**
>
> Most undead matter is best burned. What remains — grave-salt, ghoul bones, ghoul teeth — has use in specific craft. An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **grave-salt**, **ghoul bones**, or **ghoul's tooth**.
>
> **Grave-salt.** A dry white powder scraped from the threshold, floorboard, or grave-stone the undead last touched. A dose sprinkled across a threshold prevents any restless dead, skeleton, or ghoul from crossing that line for one Quarter Day. It also, by the same working, prevents any living person who was already inside from crossing back out — which is why the salt is rarely used at any door not first emptied. A second dose laid over the first extends the effect but neither dose can be recalled.
>
> **Ghoul bones.** The canonical alchemical ingredient for **Longwalk** (see the Corebook). One finger-bone from a skeleton, kept sealed in a tallow-stoppered flask, also serves as a dead-compass: carried in an open palm, it rotates slowly to point at the nearest restless dead person within SHORT range. It spins freely when none are close and spins fast when one is very close indeed.
>
> **Ghoul's tooth.** One tooth cut from a ghoul, set into a ring and worn in plain sight. While worn, the bearer can understand the broken, fragmented speech of any restless dead she encounters. The tooth disturbs every village the bearer enters, and any Rust Brother who sees it will make an inquiry. The tooth crumbles to grey dust at the next full moon.""",
    ),
    # 23. Wyvern
    (
        "Wyvern blubber is the most traded harvest in cold country",
        """> **RESOURCES**
>
> An adventurer with the ALCHEMIST talent, with a HEALING roll, draws one of the following per ⚔️ rolled, player's choice: **wyvern blubber**, **pinion-bone**, or **bile-oil**. A CHEF can render D6 units of FOOD from any slain wyvern without an alchemist's art.
>
> **Wyvern blubber.** D3 doses per ⚔️. A dose burned in open flame casts warmth equal to a fair cooking-fire for one Quarter Day, gives no smoke, and leaves no scent; it is legendary among winter-scouts and cold-country smugglers. A dose rendered into boot-leather by a TANNER before a winter journey provides Cold immunity for one journey leg; a second rendering stiffens the leather and splits it.
>
> **Pinion-bone.** One intact primary wing-bone per adult wyvern, taken before the body cools. Split lengthwise and set into a shield by a SMITH, it adds +2 to DODGE against any flying creature for the shield's natural life. The bone oil pressed from its marrow, rubbed onto a bowstring, grants a D8 Artifact Die to one MARKSMANSHIP roll aimed upward at a flying target; the string must be re-oiled after each such shot, and the oil is sold by the drop in wyvern country.
>
> **Bile-oil.** A thin yellowish oil from the liver, acrid to the nose. Rubbed on steel before a fight in wet terrain, it prevents rust for one season and makes the blade surface slightly repellent to water, which speeds the draw from a wet scabbard. Applied to rope or rigging, it makes the cordage supple and waterproof for one full season. The village tanneries of wyvern country value it as a preservative and will trade leather gear for it.""",
    ),
]


def main():
    with open(PATH, "r", encoding="utf-8") as f:
        content = f.read()

    changes = 0
    for anchor, new_block in REPLACEMENTS:
        # Find the RESOURCES blockquote that contains the anchor text
        # Pattern: > **RESOURCES**\n>\n> ...paragraph containing anchor...
        pattern = r'(> \*\*RESOURCES\*\*\n>\n> [^\n]*' + re.escape(anchor) + r'[^\n]*\n)'
        match = re.search(pattern, content)
        if not match:
            print(f"ERROR: Could not find anchor: {anchor[:60]!r}", file=sys.stderr)
            continue
        # Replace from > **RESOURCES** through the end of the blockquote paragraph
        start = match.start()
        # find end of this blockquote block (next blank line not starting with ">")
        end = match.end()
        # keep consuming lines that are blockquote lines
        rest = content[end:]
        # the old block is a single paragraph: end is at the \n after the paragraph
        content = content[:start] + new_block + "\n" + content[end:]
        changes += 1
        print(f"OK: replaced anchor {anchor[:60]!r}")

    with open(PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nDone: {changes}/{len(REPLACEMENTS)} replacements applied.")


if __name__ == "__main__":
    main()
