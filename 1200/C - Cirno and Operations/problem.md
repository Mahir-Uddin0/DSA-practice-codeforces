# C. Cirno and Operations

**time limit per test** 2 seconds  
**memory limit per test** 512 megabytes  

Cirno has a sequence a of length n. She can perform either of the following two operations for any (possibly, zero) times unless the current length of a is 1:

- Reverse the sequence. Formally, [a₁, a₂, …, aₙ] becomes [aₙ, aₙ₋₁, …, a₁] after the operation.
- Replace the sequence with its difference sequence. Formally, [a₁, a₂, …, aₙ] becomes [a₂−a₁, a₃−a₂, …, aₙ−aₙ₋₁] after the operation.

Find the maximum possible sum of elements of a after all operations.

---

## Input

The first line of input contains a single integer t (1 ≤ t ≤ 100) — the number of input test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — the length of sequence a.

The second line of each test case contains n integers a₁, a₂, …, aₙ (|aᵢ| ≤ 1000) — the sequence a.

---

## Output

For each test case, print an integer representing the maximum possible sum.

---

## Example

### Input
```
5
1
-1000
2
5 -3
2
1000 1
9
9 7 9 -9 9 -8 7 -8 9
11
678 201 340 444 453 922 128 987 127 752 0
```

### Output
```
-1000
8
1001
2056
269891
```

---

## Note

In the first test case, Cirno can not perform any operation, so the answer is −1000.

In the second test case, Cirno firstly reverses the sequence, then replaces the sequence with its difference sequence:  
[5, −3] → [−3, 5] → [8].  
It can be proven that this maximizes the sum, so the answer is 8.

In the third test case, Cirno can choose not to operate, so the answer is 1001.

---

