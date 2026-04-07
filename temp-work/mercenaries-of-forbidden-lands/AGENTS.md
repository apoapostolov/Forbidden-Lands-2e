# Chapter 12 — Editing Guide

## Edit here, not in corebook/

`corebook/12-mercenaries-of-forbidden-lands.md` is a **generated file**.

Do not edit it directly. Every edit must go into the part files in this directory. The corebook file is overwritten completely each time the build script runs. Any change made directly to the corebook file will be silently lost on the next build.

## Why parts?

Chapter 12 is the largest chapter in the manuscript. As a single file it exceeds the practical context window for cheap AI inference. Splitting it into named parts allows targeted editing without loading the full ~5000-line chapter. Each part is small enough to read, reason about, and edit in a single inference pass at any model tier.

## Parts in build order

| File | Content |
|---|---|
| `01-introduction.md` | Chapter introduction and framing |
| `02-recruitment-and-pay.md` | Hiring, pay rates, and the retainer model |
| `03-extortion-and-tribute.md` | Tribute and Tyrant band mechanics |
| `04-contracts-and-bounties.md` | Contract types, Allegiance, bounty tables |
| `05-campaign-life.md` | Travel, supply, morale, and STANDING |
| `06-named-men.md` | Named Man rules, tiers, and advancement |
| `07-hired-casters.md` | Caster integration and caster contracts |
| `08-special-rules.md` | Kin bands, blood oaths, special mechanics |
| `09-serving-in-anothers-company.md` | PC serving under an NPC band |
| `10-host-play.md` | Running the band as an ongoing faction |
| `11-appendix-a-meet-the-band.md` | Faction sheet and session-zero tools |
| `12-appendix-b-premade-bands.md` | Eight ready-to-run premade bands |
| `XX-appendix-integration.md` | Cross-chapter integration notes |

## After editing any part

Run the build script from the repository root:

```bash
python3 scripts/build_mercenaries.py
```

This concatenates all parts in the order above and writes the assembled chapter to:

```
corebook/12-mercenaries-of-forbidden-lands.md
```

Then commit both the edited part file and the rebuilt corebook file together.

## Commit pattern

```bash
git add temp-work/mercenaries-of-forbidden-lands/<changed-part>.md \
        corebook/12-mercenaries-of-forbidden-lands.md
git commit -m "Describe the change"
```

Never commit the corebook file without also committing the part that produced it.
