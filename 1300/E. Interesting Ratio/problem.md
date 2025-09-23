# E. Interesting Ratio

time limit per test 2 seconds  
memory limit per test 256 megabytes  

Recently, Misha at the IT Campus "NEIMARK" camp learned a new topic — the Euclidean algorithm.  

He was somewhat surprised when he realized that  

a⋅b = lcm(a,b) ⋅ gcd(a,b)

where gcd(a,b) — is the greatest common divisor (GCD) of the numbers a and b, and lcm(a,b) — is the least common multiple (LCM).  

Misha thought that since the product of LCM and GCD exists, it might be interesting to consider their quotient:  

F(a,b) = lcm(a,b) / gcd(a,b)

For example, he took a=2 and b=4, computed F(2,4)=4/2=2 and obtained a prime number (a number is prime if it has exactly two divisors)!  

Now he considers F(a,b) to be an interesting ratio if a<b and F(a,b) is a prime number.  

Since Misha has just started studying number theory, he needs your help to calculate — how many different pairs of numbers a and b are there such that F(a,b) is an interesting ratio and 1≤a<b≤n.

## Input

The first line contains the number of test cases t (1≤t≤10³). The description of the test cases follows.  

A single line of each test case contains a single integer n (2≤n≤10⁷).  

It is guaranteed that the sum of n over all test cases does not exceed 10⁷.

## Output

For each test case, output the number of interesting ratios F(a,b) for pairs satisfying 1≤a<b≤n.

## Examples

### Input
4
5
10
34
10007

### Output
4
11
49
24317

[View the original problem on Codeforces](https://codeforces.com/contest/2091/problem/E)
