## C. Boats Competition  
**time limit per test:** 2 seconds  
**memory limit per test:** 256 megabytes  

There are **n** people who want to participate in a boat competition. The weight of the *i-th* participant is **wᵢ**.  
Only **teams of two people** can participate. All valid teams must have the **same total weight**.

So if there are teams  
\((a_1, b_1), (a_2, b_2), \dots, (a_k, b_k)\),  
then they must satisfy:  
\[
a_1 + b_1 = a_2 + b_2 = \dots = a_k + b_k = s
\]  
Your goal is to choose **s** such that the **maximum number of teams** can be formed.  
Each person can be used in **at most one** team.

You need to answer **t** independent test cases.

### Input  
- First line: integer `t` (1 ≤ t ≤ 1000) — number of test cases  
- For each test case:  
  - Integer `n` (1 ≤ n ≤ 50)  
  - `n` integers `w₁, w₂, …, wₙ` (1 ≤ wᵢ ≤ n)

### Output  
For each test case, print a single integer `k`:  
the **maximum** number of teams that can be formed for some chosen total weight `s`.

### Example  

**Input**
5
5
1 2 3 4 5
8
6 6 6 6 6 6 8 8
8
1 2 2 1 2 1 1 2
3
1 3 3
6
1 1 3 4 2 2


**Output**
2
3
4
1
2

### Note  
- In test case 1, choosing **s = 6** gives 2 teams: (1,5) and (2,4).  
- In test case 2, choosing **s = 12** gives 3 teams from the six participants with weight 6.  
- In test case 3, choosing **s = 3** gives 4 teams using four 1s and four 2s.  
- In test case 4, the optimal answer can be achieved with **s = 4** or **s = 6**.  
- In test case 5, choosing **s = 3** gives 2 teams; the one with weight 3 cannot be paired.

