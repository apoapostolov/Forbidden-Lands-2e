# Calibration Examples

These examples show the sort of transformation the cleanup pipeline should aim for.

## Footer removal

Before:

```md
3

some footer line

## INTRODUCTION
```

After:

```md
## Introduction
```

## Heading recovery

Before:

```md
## **TYPE OF GOVERNMENT**
```

After:

```md
### Type of Government
```

## Table recovery

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

## Drop-cap repair

Before:

```md
elcome to the book...
```

After:

```md
Welcome to the book...
```

## Safe restraint

If the right correction is not obvious, keep the damaged text and mark it for review.
