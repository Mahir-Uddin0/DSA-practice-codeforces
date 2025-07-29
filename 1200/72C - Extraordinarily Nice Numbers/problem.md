# Problem C: Extraordinarily Nice Numbers

Time limit per test: 2 seconds  
Memory limit per test: 256 megabytes  

---

## Problem Statement

The positive integer `a` is a divisor of the positive integer `b` if and only if there exists a positive integer `c` such that: a × c = b
King Astyages thinks a positive integer x is extraordinarily nice if the number of its even divisors is equal to the number of its odd divisors.

For example 3 has two positive divisors 3 and 1, both of which are odd, so 3 is not extraordinarily nice. On the other hand 2 is only divisible by 2 and 1, so it has one odd and one even divisor. Therefore 2 is extraordinarily nice.

Given a positive integer x determine whether it's extraordinarily nice.

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

## Source
[View the original problem on Codeforces](https://codeforces.com/problemset/problem/72/C)
