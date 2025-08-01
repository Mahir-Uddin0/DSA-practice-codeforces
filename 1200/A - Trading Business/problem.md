# A. Trading Business

time limit per test 2 seconds  
memory limit per test 256 megabytes  

To get money for a new aeonic blaster, ranger Qwerty decided to engage in trade for a while. He wants to buy some number of items (or probably not to buy anything at all) on one of the planets, and then sell the bought items on another planet. Note that this operation is not repeated, that is, the buying and the selling are made only once. To carry out his plan, Qwerty is going to take a bank loan that covers all expenses and to return the loaned money at the end of the operation (the money is returned without the interest). At the same time, Querty wants to get as much profit as possible.

The system has n planets in total. On each of them Qwerty can buy or sell items of m types (such as food, medicine, weapons, alcohol, and so on). For each planet i and each type of items j Qwerty knows the following:

- a<sub>ij</sub> — the cost of buying an item;  
- b<sub>ij</sub> — the cost of selling an item;  
- c<sub>ij</sub> — the number of remaining items.  

It is not allowed to buy more than c<sub>ij</sub> items of type j on planet i, but it is allowed to sell any number of items of any kind.

Knowing that the hold of Qwerty's ship has room for no more than k items, determine the maximum profit which Qwerty can get.

---

## Input

The first line contains three space-separated integers n, m and k (2 ≤ n ≤ 10, 1 ≤ m, k ≤ 100) — the number of planets, the number of question types and the capacity of Qwerty's ship hold, correspondingly.

Then follow n blocks describing each planet.

The first line of the i-th block has the planet's name as a string with length from 1 to 10 Latin letters. The first letter of the name is uppercase, the rest are lowercase. Then in the i-th block follow m lines, the j-th of them contains three integers a<sub>ij</sub>, b<sub>ij</sub> and c<sub>ij</sub> (1 ≤ b<sub>ij</sub> < a<sub>ij</sub> ≤ 1000, 0 ≤ c<sub>ij</sub> ≤ 100) — the numbers that describe money operations with the j-th item on the i-th planet. The numbers in the lines are separated by spaces.

It is guaranteed that the names of all planets are different.

---

## Output

Print a single number — the maximum profit Qwerty can get.

---

## Example

### Input
```
3 3 10
Venus
6 5 3
7 6 5
8 6 10
Earth
10 9 0
8 6 4
10 9 3
Mars
4 3 0
8 4 12
7 2 5
```

### Output
```
16
```

---

## Note

In the first test case you should fly to planet Venus, take a loan on 74 units of money and buy three items of the first type and 7 items of the third type (3·6 + 7·8 = 74). Then the ranger should fly to planet Earth and sell there all the items he has bought. He gets 3·9 + 7·9 = 90 units of money for the items, he should give 74 of them for the loan. The resulting profit equals 16 units of money. We cannot get more profit in this case.

---

## Source

[View the original problem on Codeforces](https://codeforces.com/contest/176/problem/A)
