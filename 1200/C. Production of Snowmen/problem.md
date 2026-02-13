# C. Production of Snowmen  
time limit per test: 2 seconds  
memory limit per test: 512 megabytes

To create a truly festive atmosphere, Santa's helpers have opened a factory for producing snowmen!

Each snowman consists of three snowballs — a head, a torso, and legs. For the snowman to be stable, the ball forming the legs must be strictly larger than the ball forming the torso; in turn, the ball forming the torso must be strictly larger than the ball forming the head. Formally, if we denote the sizes of the head, torso, and legs as a, b, c respectively, the snowman will be stable if and only if a < b < c.

At the snowman production factory, there are three conveyors, each containing n snowballs. The first conveyor contains balls of sizes a₁, a₂, …, aₙ; the second contains balls of sizes b₁, b₂, …, bₙ; the third contains balls of sizes c₁, c₂, …, cₙ. The conveyors are cyclic; in other words, after the element numbered n, the element numbered 1 follows again, and we can consider that the ball numbered i and the ball numbered i+n (as well as the ball numbered i+2n, i+3n, and so on) are the same ball.

To produce snowmen, it is necessary to specify three parameters i, j, k (1 ≤ i, j, k ≤ n), indicating which balls on each conveyor the production starts from. After that, the snowmen will be assembled from the balls as follows:

- the first snowman will have a head of size aᵢ, a torso of size bⱼ, and legs of size cₖ;
- the second snowman will have a head of size aᵢ₊₁, a torso of size bⱼ₊₁, and legs of size cₖ₊₁;
- and so on;
- the n-th (last) snowman will have a head of size aᵢ₊ₙ₋₁, a torso of size bⱼ₊ₙ₋₁, and legs of size cₖ₊ₙ₋₁.

The parameters i, j, k must be chosen in such a way that all n snowmen are stable. Your task is to count the number of suitable combinations of parameters.

## Input
The first line contains one integer t (1 ≤ t ≤ 5000) — the number of test cases.

Each test case consists of four lines:

- the first line contains one integer n (1 ≤ n ≤ 5000);
- the second line contains n integers a₁, a₂, …, aₙ (1 ≤ aᵢ ≤ 3n);
- the third line contains n integers b₁, b₂, …, bₙ (1 ≤ bᵢ ≤ 3n);
- the fourth line contains n integers c₁, c₂, …, cₙ (1 ≤ cᵢ ≤ 3n).

Additional constraint: the sum of n across all test cases does not exceed 5000.

## Output
For each test case, output one integer — the number of combinations of parameters i, j, k for which all n snowmen will be stable.

## Example

### input
```
4
2
1 2
3 4
5 4
3
1 1 1
2 2 2
3 3 3
4
1 2 1 2
3 3 2 2
5 5 5 5
5
1 4 2 3 5
6 4 5 7 6
7 5 8 10 10
```

### output
```
4
27
0
10
```

## Note
In the first example, suitable sets of parameters i, j, k are as follows:

- i = 1, j = 1, k = 2: snowmen are (1,3,4) and (2,4,5);
- i = 1, j = 2, k = 1: snowmen are (1,4,5) and (2,3,4);
- i = 2, j = 1, k = 2: snowmen are (2,3,4) and (1,4,5);
- i = 2, j = 2, k = 1: snowmen are (2,4,5) and (1,3,4).

In the second example, all combinations of parameters are suitable.

In the third example, for any combination of parameters, a snowman with a head size of 2 and a torso size of 2 will be produced, which is not stable.


## Source
[View the original problem on Codeforces](https://codeforces.com/contest/2182/problem/C)
