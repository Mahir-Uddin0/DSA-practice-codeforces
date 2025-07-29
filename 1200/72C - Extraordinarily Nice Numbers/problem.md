# Problem C: Extraordinarily Nice Numbers

**Time limit per test:** 2 seconds  
**Memory limit per test:** 256 megabytes  

---

## Problem Statement

The positive integer `a` is a divisor of the positive integer `b` if and only if there exists a positive integer `c` such that: a × c = b

King Astyages defines a positive integer `x` as extraordinarily nice if the number of its even divisors is equal to the number of its odd divisors.

### Examples:

- The number `3` has two positive divisors: `1` and `3`, both of which are odd. So, `3` is not extraordinarily nice.
- The number `2` has two divisors: `1` (odd) and `2` (even). Since there's one even and one odd divisor, `2` is extraordinarily nice.

---

## Input

A single integer `x`  
Constraints: `1 ≤ x ≤ 10^3`

---

## Output

Print `yes` if the number is extraordinarily nice, otherwise print `no`.  
The output is case-insensitive — both `yes` and `YES` are acceptable.

---

## Examples

### Input
```
2
```

### Output
```
yes
```

### Input
```
3
```

### Output
```
no
```

---

## Note

To solve this problem, count all positive divisors of `x`, and separate them into even and odd divisors. If the counts are equal, `x` is extraordinarily nice.
