# E. Product Queries  
time limit per test: 3 seconds  
memory limit per test: 256 megabytes

Today, Sabyrzhan was called to the board with an array a of length n and was assigned an officer's task — to answer n questions.

In the i-th question, it is required to determine the minimum number of elements from the array that need to be selected from the board (it is allowed to use the same element multiple times) so that their product is exactly equal to i, or to report that it is impossible to achieve such a product.

Note that at least one element must be selected.

## Input
Each test consists of several test cases. The first line contains one integer t (1 ≤ t ≤ 10⁴) — the number of test cases. The description of the test cases follows.

The first line of each test case contains one integer n (1 ≤ n ≤ 3⋅10⁵).

The second line of each test case contains n integers a₁, a₂, …, aₙ (1 ≤ aᵢ ≤ n).

It is guaranteed that the sum of the values of n across all test cases does not exceed 3⋅10⁵.

## Output
For the i-th question, output one integer — the minimum number of elements from the array required to obtain a product equal to i, or −1 if it is impossible to achieve such a product.

## Example

### input
```
6
8
3 2 2 3 7 3 6 7
5
1 2 3 4 5
3
1 1 1
10
2 1 2 1 3 5 5 7 7 7
4
1 1 2 2
1
1
```

### output
```
-1 1 1 2 -1 1 1 3
1 1 1 1 1
1 -1 -1
1 1 1 2 1 2 1 3 2 2
1 1 -1 2
1
```

## Note
Consider the first test case. The products can be obtained as follows:

1 cannot be obtained.  
2 can be obtained by selecting a₂.  
3 can be obtained by selecting a₁.  
4 can be obtained by selecting a₂ twice.  
5 cannot be obtained.  
6 can be obtained by selecting a₇.  
7 can be obtained by selecting a₅.  
8 can be obtained by selecting a₂ three times.

