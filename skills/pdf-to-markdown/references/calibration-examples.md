# Calibration Examples

These examples show the kind of transformation the OCR workflow should aim for.

## Example 1: Footer Removal

Before:

```md
3

towns & villagers

## INTRODUCTION
```

After:

```md
## Introduction
```

## Example 2: Heading Recovery

Before:

```md
## **TYPE OF GOVERNMENT**
```

After:

```md
#### Type of Government
```

## Example 3: Table Recovery

Before:

```md
D66 WEALTH GEAR 11-16 Too much debt. -2 21-26 In debt. -1
```

After:

```md
| D66 | Wealth | Gear |
| --- | --- | --- |
| 11-16 | Too much debt. | -2 |
| 21-26 | In debt. | -1 |
```

## Example 4: Drop-Cap Repair

Before:

```md
elcome to Spells & Sorcerers...
```

After:

```md
Welcome to Spells & Sorcerers...
```

## Example 5: Safe Restraint

Before:

```md
The arrival of the ailanders and aslenes...
```

Preferred handling:

- preserve if confidence is uncertain
- correct only if the same document repeatedly confirms the intended term

The point is not to look clever. The point is to avoid silent invention.
