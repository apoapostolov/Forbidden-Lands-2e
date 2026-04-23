# Agent Turn Template

Use this template when performing a serious OCR cleanup turn.

## 1. Diagnose

State:

- what the source file is
- whether you are starting from PDF or raw markdown
- what artifact classes you see first
- which profile you are choosing and why

## 2. Plan

State the phases you will execute.

Good example:

- preserve raw
- audit artifacts
- repair title and heading structure
- reconstruct critical tables
- normalize paragraphs
- lint and report

## 3. Process

Work in batches.

After each major batch, tell the user:

- what you just fixed
- what remains risky

## 4. Verify

Minimum verification:

- run the audit script
- run lint on the cleaned file
- spot-check the opening, middle, and a table-heavy section

## 5. Report

At the end, report:

- created files
- repaired artifact classes
- remaining ambiguity
- whether lint passed

This template is intentionally repetitive. Repetition is safer than improvising
during OCR recovery.
