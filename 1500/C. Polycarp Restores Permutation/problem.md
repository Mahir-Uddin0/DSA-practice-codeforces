# C. Polycarp Restores Permutation  
time limit per test: 2 seconds  
memory limit per test: 256 megabytes

An array of integers p₁, p₂, …, pₙ is called a permutation if it contains each number from 1 to n exactly once. For example, the following arrays are permutations: [3,1,2], [1], [1,2,3,4,5] and [4,3,1,2]. The following arrays are not permutations: [2], [1,1], [2,3,4].

Polycarp invented a really cool permutation p₁, p₂, …, pₙ of length n. It is very disappointing, but he forgot this permutation. He only remembers the array q₁, q₂, …, qₙ₋₁ of length n−1, where qᵢ = pᵢ₊₁ − pᵢ.

Given n and q = q₁, q₂, …, qₙ₋₁, help Polycarp restore the invented permutation.

## Input
The first line contains the integer n (2 ≤ n ≤ 2⋅10⁵) — the length of the permutation to restore.  

The second line contains n−1 integers q₁, q₂, …, qₙ₋₁ (−n < qᵢ < n).

## Output
Print the integer -1 if there is no such permutation of length n which corresponds to the given array q. Otherwise, if it exists, print p₁, p₂, …, pₙ. Print any such permutation if there are many of them.

## Examples

### input
```
3
-2 1
```

### output
```
3 1 2
```

### input
```
5
1 1 1 1
```

### output
```
1 2 3 4 5
```

### input
```
4
-1 2 2
```

### output
```
-1
```


## Source
[View the original problem on Codeforces](https://codeforces.com/contest/1141/problem/C)
