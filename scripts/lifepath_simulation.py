#!/usr/bin/env python3
"""
Forbidden Lands 2E — Life Path Generator Balance Simulation
Runs thousands of simulated characters through the life path generator
and produces statistical analysis of skill/talent distributions.
"""

import random
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

# ──────────────────────────────────────────────────────────────
# MARK→RANK CONVERSION TABLE
# ──────────────────────────────────────────────────────────────
MARK_TO_RANK = {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4,
                7: 5, 8: 5, 9: 5, 10: 5}

def marks_to_rank(marks: int) -> int:
    if marks >= 7:
        return 5
    return MARK_TO_RANK.get(marks, 0)

# ──────────────────────────────────────────────────────────────
# AGE CONFIGS
# ──────────────────────────────────────────────────────────────
AGE_CONFIGS = {
    "Young":  {"cycles": 2, "attr_pts": 15, "general_talents": 1, "total_marks": 8},
    "Adult":  {"cycles": 3, "attr_pts": 14, "general_talents": 3, "total_marks": 12},
    "Old":    {"cycles": 4, "attr_pts": 13, "general_talents": 5, "total_marks": 16},
}

# ──────────────────────────────────────────────────────────────
# ALL 16 SKILLS
# ──────────────────────────────────────────────────────────────
ALL_SKILLS = [
    "Might", "Endurance", "Melee", "Crafting", "Move",
    "Stealth", "Sleight of Hand", "Scouting", "Survival",
    "Manipulation", "Performance", "Healing", "Insight",
    "Lore", "Animal Handling", "Marksmanship"
]

# ──────────────────────────────────────────────────────────────
# PATH DEFINITIONS
# ──────────────────────────────────────────────────────────────
PROFESSION_PATHS = {
    "Druid":    {"turn_test": ["Lore", "Survival"],
                 "normal": ["Lore", "Survival", "Healing", "Insight", "Animal Handling", "Scouting"],
                 "hard_lesson": ["Healing", "Insight", "Lore"],
                 "threshold_skills": ["Lore", "Healing"]},
    "Fighter":  {"turn_test": ["Melee", "Might"],
                 "normal": ["Melee", "Might", "Endurance", "Marksmanship", "Move", "Survival"],
                 "hard_lesson": ["Endurance", "Melee", "Might"],
                 "threshold_skills": []},
    "Hunter":   {"turn_test": ["Scouting", "Marksmanship"],
                 "normal": ["Scouting", "Marksmanship", "Survival", "Animal Handling", "Move", "Crafting"],
                 "hard_lesson": ["Scouting", "Survival", "Marksmanship"],
                 "threshold_skills": []},
    "Minstrel": {"turn_test": ["Performance", "Manipulation"],
                 "normal": ["Performance", "Manipulation", "Insight", "Lore", "Move", "Sleight of Hand"],
                 "hard_lesson": ["Insight", "Performance", "Manipulation"],
                 "threshold_skills": ["Performance", "Manipulation"]},
    "Peddler":  {"turn_test": ["Manipulation", "Insight"],
                 "normal": ["Manipulation", "Insight", "Crafting", "Animal Handling", "Scouting", "Lore"],
                 "hard_lesson": ["Insight", "Manipulation", "Crafting"],
                 "threshold_skills": ["Manipulation", "Insight"]},
    "Rider":    {"turn_test": ["Animal Handling", "Move"],
                 "normal": ["Animal Handling", "Move", "Melee", "Scouting", "Marksmanship", "Endurance"],
                 "hard_lesson": ["Move", "Animal Handling", "Endurance"],
                 "threshold_skills": ["Animal Handling", "Move"]},
    "Rogue":    {"turn_test": ["Stealth", "Sleight of Hand"],
                 "normal": ["Stealth", "Sleight of Hand", "Scouting", "Move", "Insight", "Melee"],
                 "hard_lesson": ["Stealth", "Sleight of Hand", "Move"],
                 "threshold_skills": []},
    "Sorcerer": {"turn_test": ["Lore", "Insight"],
                 "normal": ["Lore", "Insight", "Manipulation", "Healing", "Crafting", "Survival"],
                 "hard_lesson": ["Insight", "Lore", "Healing"],
                 "threshold_skills": ["Lore"]},
}

CRISIS_PATHS = {
    "Captive":  {"turn_test": ["Endurance", "Insight"],
                 "normal": ["Endurance", "Insight", "Survival", "Melee", "Stealth", "Move"],
                 "hard_lesson": ["Endurance", "Might", "Insight"],
                 "threshold_skills": []},
    "Drifter":  {"turn_test": ["Survival", "Move"],
                 "normal": ["Survival", "Move", "Insight", "Scouting", "Manipulation", "Endurance"],
                 "hard_lesson": ["Survival", "Move", "Scouting"],
                 "threshold_skills": []},
    "Laborer":  {"turn_test": ["Might", "Crafting"],
                 "normal": ["Might", "Crafting", "Endurance", "Animal Handling", "Insight", "Manipulation"],
                 "hard_lesson": ["Might", "Crafting", "Endurance"],
                 "threshold_skills": []},
    "Outcast":  {"turn_test": ["Stealth", "Survival"],
                 "normal": ["Stealth", "Survival", "Scouting", "Insight", "Move", "Melee"],
                 "hard_lesson": ["Stealth", "Survival", "Scouting"],
                 "threshold_skills": []},
}

ALL_PATHS = {**PROFESSION_PATHS, **CRISIS_PATHS}

# ──────────────────────────────────────────────────────────────
# CHILDHOOD FOUNDATIONS (simplified — 2 skill marks each)
# Each kin has 6 options, we model skill pairs
# ──────────────────────────────────────────────────────────────
CHILDHOOD_SKILL_PAIRS = [
    ("Melee", "Healing"),       # Squire
    ("Lore", "Insight"),        # Temple Student
    ("Survival", "Scouting"),   # Forest Child
    ("Crafting", "Might"),      # Smith's Apprentice
    ("Manipulation", "Insight"),# Merchant's Ward
    ("Move", "Endurance"),      # Street Runner
    ("Animal Handling", "Survival"), # Herder's Child
    ("Stealth", "Move"),        # Outcast Youth
    ("Performance", "Manipulation"), # Skald's Pupil
    ("Marksmanship", "Survival"),    # Hunter's Child
]

# ──────────────────────────────────────────────────────────────
# TALENT GRANTS (from advancement benefits)
# Each path has 2 specific talents on results 1-2 of d6
# ──────────────────────────────────────────────────────────────
PATH_TALENT_GRANTS = {
    "Druid":    ["Herbalist", "Pathfinder", "Path of Healing"],
    "Fighter":  ["Defender", "Pack Rat", "Shieldmate"],
    "Hunter":   ["Master of the Hunt", "Sharpshooter", "Pathfinder"],
    "Minstrel": ["Lucky", "Sharp Tongue", "Wanderer"],
    "Peddler":  ["Incorruptible", "Wanderer", "Sharp Tongue"],
    "Rider":    ["Horseback Fighter", "Tanner", "Pathfinder"],
    "Rogue":    ["Sixth Sense", "Lightning Fast", "Wanderer"],
    "Sorcerer": ["Sharp Tongue", "Poisoner", "Herbalist"],
    "Captive":  ["Fearless", "Hard to Kill", "Lucky"],
    "Drifter":  ["Fearless", "Pack Rat", "Wanderer"],
    "Laborer":  ["Quartermaster", "Tanner", "Hard to Kill"],
    "Outcast":  ["Fearless", "Sixth Sense", "Lucky"],
}

# ──────────────────────────────────────────────────────────────
# EVENT TABLE SKILL OFFERINGS
# Each event offers a choice of 2 skills. We model these as pools.
# For simplicity: the event tables for each turn offer skills
# from the normal list (success events) or slightly outside it.
# We model this as: 80% chance from normal list, 20% from adjacent.
#
# Mishap events offer skills from hard-lesson list.
# ──────────────────────────────────────────────────────────────

# Adjacent/off-list skills that appear in event tables per path
PATH_EVENT_EXTRAS = {
    "Druid":    ["Manipulation", "Melee", "Marksmanship", "Crafting", "Move", "Endurance"],
    "Fighter":  ["Insight", "Scouting", "Healing", "Crafting", "Lore", "Manipulation"],
    "Hunter":   ["Melee", "Insight", "Endurance", "Healing", "Manipulation", "Lore"],
    "Minstrel": ["Survival", "Melee", "Scouting", "Crafting", "Stealth", "Endurance"],
    "Peddler":  ["Melee", "Move", "Survival", "Endurance", "Healing", "Stealth"],
    "Rider":    ["Insight", "Survival", "Healing", "Manipulation", "Crafting", "Stealth"],
    "Rogue":    ["Manipulation", "Survival", "Endurance", "Crafting", "Lore", "Healing"],
    "Sorcerer": ["Manipulation", "Scouting", "Move", "Crafting", "Endurance", "Lore"],
    "Captive":  ["Might", "Manipulation", "Sleight of Hand", "Scouting", "Crafting", "Healing"],
    "Drifter":  ["Might", "Crafting", "Melee", "Stealth", "Sleight of Hand", "Lore"],
    "Laborer":  ["Move", "Melee", "Survival", "Healing", "Stealth", "Lore"],
    "Outcast":  ["Manipulation", "Sleight of Hand", "Animal Handling", "Lore", "Endurance", "Melee"],
}


def roll_d6() -> int:
    return random.randint(1, 6)


def roll_d6_pool(pool_size: int) -> int:
    """Roll pool_size d6s, count successes (6s)."""
    if pool_size <= 0:
        return 0
    return sum(1 for _ in range(pool_size) if roll_d6() == 6)


@dataclass
class Character:
    age: str
    skill_marks: dict = field(default_factory=lambda: defaultdict(int))
    talent_marks: dict = field(default_factory=lambda: defaultdict(int))
    wear: int = 0
    paths_taken: list = field(default_factory=list)
    cycles_in_current_path: int = 0
    contacts: int = 0
    rivals: int = 0
    enemies: int = 0
    scars: int = 0
    rumors: int = 0
    silver_dice: int = 0
    advancement_benefits: int = 0
    forced_departures: int = 0
    pride_claimed: bool = False
    dark_secret_claimed: bool = False
    total_turns_resolved: int = 0
    total_successes: int = 0
    total_failures: int = 0

    def current_skill_rank(self, skill: str) -> int:
        return marks_to_rank(self.skill_marks[skill])

    def meets_threshold(self, path_name: str) -> bool:
        path = ALL_PATHS[path_name]
        if not path["threshold_skills"]:
            return True
        # Meet threshold if any threshold skill >= 1 mark (=Rank 1)
        for s in path["threshold_skills"]:
            if self.skill_marks[s] >= 1:
                return True
        # 50% chance to meet via fiction (contact, patron, etc.)
        return random.random() < 0.35

    def get_final_skills(self) -> dict:
        """Convert marks to final ranks."""
        result = {}
        for skill in ALL_SKILLS:
            m = self.skill_marks[skill]
            if m > 0:
                result[skill] = marks_to_rank(m)
        return result

    def get_final_talents(self) -> dict:
        result = {}
        for talent, m in self.talent_marks.items():
            if m > 0:
                result[talent] = marks_to_rank(m)
        return result


def choose_path(char: Character, cycle_num: int) -> str:
    """Choose a path for this cycle. Models realistic player behavior."""
    last_path = char.paths_taken[-1] if char.paths_taken else None

    # If forced departure from last cycle, 40% crisis path, 60% new profession
    if char.forced_departures > 0 and cycle_num > 1:
        char.forced_departures = 0
        if random.random() < 0.4:
            crisis = random.choice(list(CRISIS_PATHS.keys()))
            return crisis

    # Probability distribution of path choices (modeling player behavior)
    # Players prefer profession paths; crisis paths come from forced departure
    profession_names = list(PROFESSION_PATHS.keys())

    # Try to stay in same path 30% of the time
    if last_path and last_path in PROFESSION_PATHS and random.random() < 0.30:
        if char.meets_threshold(last_path):
            return last_path

    # Otherwise pick a new profession path
    random.shuffle(profession_names)
    for p in profession_names:
        if char.meets_threshold(p):
            return p

    # Fallback: any no-threshold path
    return random.choice(["Fighter", "Rogue", "Hunter"])


def resolve_turn(char: Character, path_name: str, turn_num: int,
                 cycle_repetition: int) -> bool:
    """Resolve one turn within a cycle. Returns True on success, False on failure."""
    path = ALL_PATHS[path_name]
    char.total_turns_resolved += 1

    # Turn test: roll attribute (typically 3-4) + skill rank
    # We model attribute as 3 for young, 3 for adult, 3 for old (average)
    test_skill = random.choice(path["turn_test"])
    skill_rank = char.current_skill_rank(test_skill)
    pool = 3 + skill_rank  # attribute dice + skill dice

    # Narrowing tax: -1 per extra cycle in same path
    narrowing_penalty = max(0, cycle_repetition - 1)
    pool = max(1, pool - narrowing_penalty)

    successes = roll_d6_pool(pool)

    if successes >= 1:
        # SUCCESS: mark 1 skill from normal list via event
        char.total_successes += 1
        chosen_skill = pick_event_skill(char, path_name, path["normal"])
        char.skill_marks[chosen_skill] += 1

        # Event extras (contacts, rivals, scars, rumors, silver, etc.)
        resolve_event_extras(char, turn_num)

        # ~12% chance of pride/dark secret tag on events
        if not char.pride_claimed and random.random() < 0.08:
            char.pride_claimed = True
        if not char.dark_secret_claimed and random.random() < 0.06:
            char.dark_secret_claimed = True

        return True
    else:
        # FAILURE: mark 1 skill from hard-lesson list via mishap
        char.total_failures += 1
        chosen_skill = random.choice(path["hard_lesson"])
        char.skill_marks[chosen_skill] += 1
        # Wear is NOT added here — tracked by caller via consecutive failures

        # Mishap extras
        resolve_mishap_extras(char)

        # Dark secret tags more common on mishaps
        if not char.dark_secret_claimed and random.random() < 0.10:
            char.dark_secret_claimed = True

        return False


def pick_event_skill(char: Character, path_name: str, normal_skills: list) -> str:
    """Model the event table's skill offering.
    Events offer pairs like 'Gain X or Y' — player picks the more useful one.
    80% from normal list, 20% from event extras (adjacent skills).
    Player optimizes by picking whichever skill they have fewer marks in
    (diminishing returns from mark system) or the one more useful.
    """
    if random.random() < 0.80:
        pool = normal_skills
    else:
        pool = PATH_EVENT_EXTRAS.get(path_name, normal_skills)

    # Offer 2 choices, pick the one with fewer marks (player optimization)
    s1 = random.choice(pool)
    s2 = random.choice(pool)
    if char.skill_marks[s1] <= char.skill_marks[s2]:
        return s1
    return s2


def resolve_event_extras(char: Character, turn_num: int) -> None:
    """Model contacts, rivals, scars, rumors, silver from events."""
    r = random.random()
    if r < 0.25:
        char.contacts += 1
    elif r < 0.35:
        char.rivals += 1
    elif r < 0.45:
        char.rumors += 1
    elif r < 0.50:
        char.scars += 1
    # Turn 3-4 events more likely to give silver
    if turn_num >= 3 and random.random() < 0.15:
        char.silver_dice += 1


def resolve_mishap_extras(char: Character) -> None:
    """Model mishap consequences."""
    r = random.random()
    if r < 0.20:
        char.scars += 1
    elif r < 0.35:
        char.enemies += 1
    elif r < 0.50:
        char.rivals += 1
    # 20% chance of forced departure from mishap
    if random.random() < 0.20:
        char.forced_departures += 1


def resolve_advancement(char: Character, path_name: str,
                        cycle_repetition: int) -> bool:
    """End-of-cycle advancement roll. Returns True if stayed."""
    path = ALL_PATHS[path_name]
    test_skill = random.choice(path["turn_test"])
    skill_rank = char.current_skill_rank(test_skill)
    pool = 3 + skill_rank
    narrowing_penalty = max(0, cycle_repetition - 1)
    pool = max(1, pool - narrowing_penalty)

    successes = roll_d6_pool(pool)

    if successes >= 1:
        # Advancement benefit: 1-3 on d6 = talent, 4 = contact, 5 = gear, 6 = rumor
        char.advancement_benefits += 1
        benefit_roll = roll_d6()
        if benefit_roll <= 3:
            talents = PATH_TALENT_GRANTS.get(path_name, [])
            if talents:
                chosen = random.choice(talents)
                char.talent_marks[chosen] += 1
        elif benefit_roll == 4:
            char.contacts += 1
        elif benefit_roll == 5:
            pass  # gear
        else:
            char.rumors += 1
        return True  # stayed
    else:
        char.forced_departures += 1
        return False


def simulate_character(age: str) -> Character:
    """Run a full life path generation for one character."""
    config = AGE_CONFIGS[age]
    char = Character(age=age)

    # Childhood foundation: 2 skill marks
    childhood = random.choice(CHILDHOOD_SKILL_PAIRS)
    char.skill_marks[childhood[0]] += 1
    char.skill_marks[childhood[1]] += 1

    current_path = None
    cycles_in_path = 0

    for cycle in range(config["cycles"]):
        # Choose path
        path = choose_path(char, cycle)
        if path == current_path:
            cycles_in_path += 1
        else:
            current_path = path
            cycles_in_path = 1
        char.paths_taken.append(path)

        # Profession talent seed: first cycle grants 1 mark toward a profession talent
        if cycle == 0:
            talents = PATH_TALENT_GRANTS.get(path, [])
            if talents:
                char.talent_marks[talents[0]] += 1

        # Determine turns to resolve
        if cycle == 0:
            # First cycle: childhood covers turns 1-2, resolve 3-4
            turns = [3, 4]
        else:
            turns = [1, 2, 3, 4]

        last_turn_failed = False  # Track consecutive failures within this cycle
        for turn in turns:
            success = resolve_turn(char, path, turn, cycles_in_path)
            if not success:
                if last_turn_failed:
                    char.wear += 1  # Consecutive failure adds Wear
                last_turn_failed = True
            else:
                last_turn_failed = False

        # Advancement roll
        stayed = resolve_advancement(char, path, cycles_in_path)
        if not stayed:
            current_path = None
            cycles_in_path = 0

    # Mustering out (just adds 1 contact, scar, gear, or rumor)
    r = roll_d6()
    if r <= 2:
        pass  # gear
    elif r <= 4:
        char.contacts += 1
    else:
        char.rumors += 1

    return char


def run_simulation(n: int = 10000) -> dict:
    """Run n characters and collect statistics."""
    results = {"Young": [], "Adult": [], "Old": []}

    # Distribution: roughly 25% young, 50% adult, 25% old
    age_dist = (["Young"] * (n // 4) +
                ["Adult"] * (n // 2) +
                ["Old"] * (n // 4))
    random.shuffle(age_dist)

    for age in age_dist:
        char = simulate_character(age)
        results[age].append(char)

    return results


def analyze_results(results: dict) -> str:
    """Produce comprehensive statistical analysis."""
    lines = []
    lines.append("=" * 80)
    lines.append("FORBIDDEN LANDS 2E — LIFE PATH GENERATOR BALANCE AUDIT")
    lines.append("=" * 80)
    lines.append("")

    for age in ["Young", "Adult", "Old"]:
        chars = results[age]
        n = len(chars)
        if n == 0:
            continue

        lines.append(f"\n{'─' * 80}")
        lines.append(f"  AGE: {age.upper()} ({n} characters, {AGE_CONFIGS[age]['cycles']} cycles)")
        lines.append(f"{'─' * 80}")

        # ── SKILL MARK DISTRIBUTION ──
        all_marks = defaultdict(list)
        for c in chars:
            for skill in ALL_SKILLS:
                all_marks[skill].append(c.skill_marks[skill])

        lines.append(f"\n  SKILL MARKS (raw tallies before rank conversion)")
        lines.append(f"  {'Skill':<20} {'Mean':>6} {'Med':>4} {'Max':>4} {'Std':>6} {'%≥3':>5} {'%≥4':>5} {'%≥7':>5}")
        for skill in sorted(ALL_SKILLS, key=lambda s: -statistics.mean(all_marks[s])):
            vals = all_marks[skill]
            mean = statistics.mean(vals)
            med = statistics.median(vals)
            mx = max(vals)
            std = statistics.stdev(vals) if len(vals) > 1 else 0
            pct3 = sum(1 for v in vals if v >= 3) / n * 100
            pct4 = sum(1 for v in vals if v >= 4) / n * 100
            pct7 = sum(1 for v in vals if v >= 7) / n * 100
            lines.append(f"  {skill:<20} {mean:>6.2f} {med:>4.0f} {mx:>4} {std:>6.2f} {pct3:>4.1f}% {pct4:>4.1f}% {pct7:>4.1f}%")

        # ── FINAL RANK DISTRIBUTION ──
        rank_dist = defaultdict(lambda: Counter())
        max_ranks = []
        total_skills_with_rank = []
        skills_at_rank = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

        for c in chars:
            final = c.get_final_skills()
            max_r = max(final.values()) if final else 0
            max_ranks.append(max_r)
            total_skills_with_rank.append(len(final))
            for rank in range(6):
                count = sum(1 for r in final.values() if r == rank)
                skills_at_rank[rank].append(count)
            for skill, rank in final.items():
                rank_dist[skill][rank] += 1

        lines.append(f"\n  FINAL RANK DISTRIBUTION (after mark→rank conversion)")
        lines.append(f"  {'Skill':<20} {'R0%':>5} {'R1%':>5} {'R2%':>5} {'R3%':>5} {'R4%':>5} {'R5%':>5}")
        for skill in sorted(ALL_SKILLS, key=lambda s: -sum(r * rank_dist[s].get(r, 0) for r in range(6))):
            rd = rank_dist[skill]
            total_with = sum(rd.values())
            r0_pct = (n - total_with) / n * 100
            r1_pct = rd.get(1, 0) / n * 100
            r2_pct = rd.get(2, 0) / n * 100
            r3_pct = rd.get(3, 0) / n * 100
            r4_pct = rd.get(4, 0) / n * 100
            r5_pct = rd.get(5, 0) / n * 100
            lines.append(f"  {skill:<20} {r0_pct:>4.1f}% {r1_pct:>4.1f}% {r2_pct:>4.1f}% {r3_pct:>4.1f}% {r4_pct:>4.1f}% {r5_pct:>4.1f}%")

        lines.append(f"\n  SUMMARY STATISTICS")
        lines.append(f"  Max skill rank:     mean={statistics.mean(max_ranks):.2f}  "
                      f"med={statistics.median(max_ranks):.0f}  "
                      f"max={max(max_ranks)}")
        lines.append(f"  Skills with rank≥1: mean={statistics.mean(total_skills_with_rank):.2f}  "
                      f"med={statistics.median(total_skills_with_rank):.0f}  "
                      f"max={max(total_skills_with_rank)}")
        for rank in [1, 2, 3]:
            vals = skills_at_rank[rank]
            lines.append(f"  Skills at Rank {rank}:   mean={statistics.mean(vals):.2f}  "
                          f"med={statistics.median(vals):.0f}  "
                          f"max={max(vals)}")

        lines.append(f"\n  HIGHEST RANK ACHIEVED (% of characters)")
        for rank in range(1, 6):
            pct = sum(1 for m in max_ranks if m == rank) / n * 100
            lines.append(f"  Rank {rank}: {pct:>5.1f}%")
        pct_above_3 = sum(1 for m in max_ranks if m > 3) / n * 100
        lines.append(f"  ** Characters with any skill above Rank 3: {pct_above_3:.1f}% **")

        # ── TALENT DISTRIBUTION ──
        talent_counts = []
        talent_rank_max = []
        for c in chars:
            ft = c.get_final_talents()
            talent_counts.append(len(ft))
            if ft:
                talent_rank_max.append(max(ft.values()))
            else:
                talent_rank_max.append(0)

        lines.append(f"\n  TALENT GRANTS (from advancement benefits only)")
        lines.append(f"  Characters with≥1 talent: {sum(1 for t in talent_counts if t > 0)/n*100:.1f}%")
        lines.append(f"  Mean talents granted: {statistics.mean(talent_counts):.2f}")
        if any(t > 0 for t in talent_rank_max):
            lines.append(f"  Max talent rank: mean={statistics.mean(talent_rank_max):.2f}  max={max(talent_rank_max)}")

        # ── WEAR DISTRIBUTION ──
        wear_vals = [c.wear for c in chars]
        lines.append(f"\n  WEAR")
        lines.append(f"  Mean: {statistics.mean(wear_vals):.2f}  Med: {statistics.median(wear_vals):.0f}  Max: {max(wear_vals)}")
        lines.append(f"  0-1 Wear: {sum(1 for w in wear_vals if w <= 1)/n*100:.1f}%")
        lines.append(f"  2-3 Wear: {sum(1 for w in wear_vals if 2 <= w <= 3)/n*100:.1f}%")
        lines.append(f"  4+  Wear: {sum(1 for w in wear_vals if w >= 4)/n*100:.1f}%")

        # ── FICTION ELEMENTS ──
        lines.append(f"\n  FICTION ELEMENTS")
        lines.append(f"  Contacts: mean={statistics.mean([c.contacts for c in chars]):.2f}")
        lines.append(f"  Rivals:   mean={statistics.mean([c.rivals for c in chars]):.2f}")
        lines.append(f"  Enemies:  mean={statistics.mean([c.enemies for c in chars]):.2f}")
        lines.append(f"  Scars:    mean={statistics.mean([c.scars for c in chars]):.2f}")
        lines.append(f"  Rumors:   mean={statistics.mean([c.rumors for c in chars]):.2f}")

        # ── PRIDE / DARK SECRET CLAIMS ──
        pride_pct = sum(1 for c in chars if c.pride_claimed) / n * 100
        ds_pct = sum(1 for c in chars if c.dark_secret_claimed) / n * 100
        lines.append(f"\n  PRIDE/DARK SECRET")
        lines.append(f"  Pride claimed:       {pride_pct:.1f}%")
        lines.append(f"  Dark Secret claimed: {ds_pct:.1f}%")

        # ── PATH USAGE ──
        path_counts = Counter()
        for c in chars:
            for p in c.paths_taken:
                path_counts[p] += 1
        total_path_slots = sum(path_counts.values())
        lines.append(f"\n  PATH USAGE (across all cycles)")
        for path, count in path_counts.most_common():
            pct = count / total_path_slots * 100
            lines.append(f"  {path:<12} {count:>5} ({pct:>5.1f}%)")

        # ── SUCCESS/FAILURE RATES ──
        success_rates = [c.total_successes / c.total_turns_resolved * 100
                         if c.total_turns_resolved > 0 else 0 for c in chars]
        lines.append(f"\n  TURN TEST SUCCESS RATE")
        lines.append(f"  Mean: {statistics.mean(success_rates):.1f}%  "
                      f"Med: {statistics.median(success_rates):.1f}%")

    # ── CROSS-AGE COMPARISON ──
    lines.append(f"\n\n{'=' * 80}")
    lines.append("  CROSS-AGE COMPARISON")
    lines.append(f"{'=' * 80}")

    comp_lines = []
    for age in ["Young", "Adult", "Old"]:
        chars = results[age]
        n = len(chars)
        if n == 0:
            continue
        max_ranks = [max(c.get_final_skills().values()) if c.get_final_skills() else 0 for c in chars]
        num_skills = [len(c.get_final_skills()) for c in chars]
        pct_above_3 = sum(1 for m in max_ranks if m > 3) / n * 100
        ranks_list = []
        for c in chars:
            for r in c.get_final_skills().values():
                ranks_list.append(r)
        mean_rank = statistics.mean(ranks_list) if ranks_list else 0

        comp_lines.append(f"  {age:<8} Max rank mean={statistics.mean(max_ranks):.2f}  "
                           f"Skills≥1 mean={statistics.mean(num_skills):.2f}  "
                           f"Mean rank={mean_rank:.2f}  "
                           f"%above R3={pct_above_3:.1f}%")

    for l in comp_lines:
        lines.append(l)

    # ── STANDARD METHOD COMPARISON ──
    lines.append(f"\n\n{'=' * 80}")
    lines.append("  COMPARISON WITH STANDARD METHOD")
    lines.append(f"{'=' * 80}")
    lines.append("""
  Standard Method (Chapter 2):
    Young: 8 skill points.  Max rank 3 in profession skills, 1 elsewhere.
    Adult: 12 skill points. Max rank 3 in profession skills, 1 elsewhere.
    Old:   16 skill points. Max rank 3 (one skill may be 4), 1 elsewhere.

  Standard method typical optimized builds:
    Young:  One skill at R3, two at R1-2, 1-2 misc at R1.  (3-5 skills total)
    Adult:  One skill at R3, two at R2-3, rest at R1.      (5-7 skills total)
    Old:    One skill at R4, two at R3, rest at R1.        (6-9 skills total)

  Life Path Generator (this simulation):
    Young:  See above. More spread, fewer high ranks.
    Adult:  See above. More spread, moderate concentration.
    Old:    See above. Widest spread, potential for R3-4 in focused skills.
    """)

    # ── IDENTIFIED ISSUES ──
    lines.append(f"\n{'=' * 80}")
    lines.append("  IDENTIFIED BALANCE CONCERNS")
    lines.append(f"{'=' * 80}")

    # Check for R4+ frequency
    for age in ["Young", "Adult", "Old"]:
        chars = results[age]
        n = len(chars)
        r4_count = 0
        r5_count = 0
        for c in chars:
            for skill, marks in c.skill_marks.items():
                rank = marks_to_rank(marks)
                if rank >= 4:
                    r4_count += 1
                if rank >= 5:
                    r5_count += 1
        lines.append(f"\n  {age}: R4 skill instances: {r4_count} across {n} characters "
                      f"({r4_count/n:.2f} per char)")
        lines.append(f"  {age}: R5 skill instances: {r5_count} across {n} characters "
                      f"({r5_count/n:.3f} per char)")

    # Skill concentration analysis
    lines.append(f"\n  SKILL CONCENTRATION (Herfindahl index of skill marks)")
    for age in ["Young", "Adult", "Old"]:
        chars = results[age]
        hhi_vals = []
        for c in chars:
            total = sum(c.skill_marks.values())
            if total == 0:
                continue
            shares = [(v / total) ** 2 for v in c.skill_marks.values() if v > 0]
            hhi_vals.append(sum(shares))
        if hhi_vals:
            lines.append(f"  {age}: mean HHI={statistics.mean(hhi_vals):.4f}  "
                          f"(1.0=all marks in one skill, 0.0625=perfect spread across 16)")

    # Narrowing tax effectiveness
    lines.append(f"\n  NARROWING TAX ANALYSIS")
    for age in ["Young", "Adult", "Old"]:
        chars = results[age]
        n = len(chars)
        stayed_all = sum(1 for c in chars if len(set(c.paths_taken)) == 1) / n * 100
        changed_all = sum(1 for c in chars if len(set(c.paths_taken)) == len(c.paths_taken)) / n * 100
        lines.append(f"  {age}: Same path entire life: {stayed_all:.1f}%  "
                      f"Never repeated a path: {changed_all:.1f}%")

    return "\n".join(lines)


def main():
    random.seed(42)  # Reproducible
    print("Running simulation (10,000 characters)...")
    results = run_simulation(10000)
    report = analyze_results(results)
    print(report)

    # Write to file
    with open("scripts/lifepath_balance_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport written to scripts/lifepath_balance_report.txt")


if __name__ == "__main__":
    main()
