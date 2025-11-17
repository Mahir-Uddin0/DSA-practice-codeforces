<p align="center">

# E. G-C-D, Unlucky!  
time limit per test: 2 seconds  
memory limit per test: 256 megabytes  

</p>

Two arrays **p** and **s** of length **n** are given, where **p** is the prefix GCD\* of some array **a**, and **s** is the suffix GCD of the same array **a**.  
In other words, if the array **a** existed, then for each **1 ≤ i ≤ n**, the following equalities would both hold:

pi = gcd(a₁, a₂, …, aᵢ)  
si = gcd(aᵢ, aᵢ₊₁, …, aₙ)

Determine whether there exists such an array **a** for which the given arrays **p** and **s** can be obtained.

\* gcd(x, y) denotes the greatest common divisor (GCD) of integers x and y.

## Input
The first line contains an integer **t** (1 ≤ t ≤ 10⁴) — the number of test cases.

Each test case consists of three lines:

- The first line contains a single integer **n** (1 ≤ n ≤ 10⁵).  
- The second line contains **n** integers p₁, p₂, …, pₙ (1 ≤ pᵢ ≤ 10⁹).  
- The third line contains **n** integers s₁, s₂, …, sₙ (1 ≤ sᵢ ≤ 10⁹).  

It is guaranteed that the sum of all **n** across all test cases does not exceed 10⁵.

## Output
For each test case, output `"Yes"` if there exists an array **a** for which the given arrays **p** and **s** can be obtained, and `"No"` otherwise.  
Case-insensitive answers are accepted.

## Example

**Input**
```
5
6
72 24 3 3 3 3
3 3 3 6 12 144
3
1 2 3
4 5 6
5
125 125 125 25 25
25 25 25 25 75
4
123 421 282 251
125 1981 239 223
3
124 521 125
125 121 121
```

**Output**
```
YES
NO
YES
NO
NO
```

## Note
For the first test case, a possible array is:  
[72, 24, 3, 6, 12, 144]

For the second test case, such arrays do not exist.

For the third test case, a valid array is:  
[125, 125, 125, 25, 75]

[View the original problem on Codeforces](https://codeforces.com/contest/2126/problem/E)
