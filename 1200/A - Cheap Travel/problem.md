# A. Cheap Travel

time limit per test 1 second  
memory limit per test 256 megabytes  

Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles. Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). It costs b rubles.

Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of money she will have to spend to make n rides?

## Input

The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned, the number of rides covered by the m ride ticket, the price of a one ride ticket and the price of an m ride ticket.

## Output

Print a single integer — the minimum sum in rubles that Ann will need to spend.

## Examples

### Input
```
6 2 1 2
```

### Output
```
6
```

### Input
```
5 2 2 3
```

### Output
```
8
```

## Note

For the first test case, the only pair that satisfies the constraints is (1,2), as a1 ⋅ a2 = 1 + 2 = 3.

For the second test case, the only pair that satisfies the constraints is (2,3).

For the third test case, the pairs that satisfy the constraints are (1,2), (1,5), and (2,3).

[View the original problem on Codeforces](https://codeforces.com/contest/1541/problem/B)
