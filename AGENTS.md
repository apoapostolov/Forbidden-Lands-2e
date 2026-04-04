# Forbidden Lands 2E Public Repo AGENTS

## Purpose

This repository is a public-facing workbench for a heavily revised Forbidden Lands 2E manuscript and a living proposal area for future revisions.

It is not the private source-of-truth workspace. It is a shareable copy meant to preserve:

- the manuscript
- the proposal history
- the house style
- the legal and editorial cautions needed for public handling

## Repository Structure

- `corebook/`
  - Integrated working manuscript
  - Canonical within this repo
- `proposals/`
  - Draft design documents, revision notes, and staging material
  - Not canonical until their substance is integrated into `corebook/`
- `skills/`
  - Repo-bundled AI skills for writing, design, and rules analysis
  - Maintain these copies in the repo when the project-specific skills change
- `README.md`
  - Public explanation of scope and legal context
- `LICENSE.md`
  - Public-facing rights notice linked to the official Free League license

## Public Handling Rules

- Do not imply this repository is official.
- Do not imply Free League endorses it.
- Do not describe the integrated manuscript as a legally cleared public supplement.
- Preserve the non-affiliation and AI-disclosure notices.
- Keep references to the official Free League license current and prominent.

## Legal Guardrail

The official Free League license for Forbidden Lands was published on March 31, 2026.

That license allows compatible supplements, but it does not allow:

- standalone replacement rulebooks
- inclusion of a copy of the official core rules
- use of Free League text, artwork, or trade dress except as expressly permitted

If you edit this repo, do not weaken those warnings in the public-facing docs.

## Editorial Rule

Treat `corebook/` as the manuscript and `proposals/` as staged design support that may change over time.

Before drafting any manuscript-facing prose, consult `WRITING_GUIDE.md`.
This applies to:

- text written directly into `corebook/`
- proposal passages meant to test or preview final manuscript prose
- any final draft intended to be integrated into `corebook/` later

If a proposal is accepted:

1. integrate it into `corebook/`
2. update the chapter changelog if needed
3. keep the prose native to the manuscript
4. do not leave proposal rationale inside final rules text

## Skill Rule

If a project-specific AI skill is created or revised for this repo, keep a maintained copy under `skills/`.

The repo copy is the project-owned reference version.
External installed copies may exist for live use, but they should match the bundled version in this repository.

## Voice Rule

The manuscript must read like a real fantasy roleplaying book:

- clear
- harsh
- practical
- atmospheric
- not modern
- not mechanical AI paraphrase

`WRITING_GUIDE.md` is the operational style authority for achieving that voice.
If a new passage conflicts with the guide, revise the passage, not the standard.

## Done Standard

Public repo work is done only when:

- the docs are internally consistent
- the legal notices still match the public framing
- the manuscript reads naturally
- markdown lint passes on changed files
