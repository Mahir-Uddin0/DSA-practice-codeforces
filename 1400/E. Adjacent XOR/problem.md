# E. Adjacent XOR

You are given an array **a** of length **n**.  
For each index `i` such that `1 ≤ i < n`, you may perform the following operation **at most once**:

```
a[i] = a[i] XOR a[i+1]
```

You may choose the indices and perform the operations in **any sequential order**.

Given another array **b** of length **n**, determine whether it is possible to transform `a` into `b`.

---

## ✅ Input Format
- Multiple test cases  
- `t` — number of test cases (1 ≤ t ≤ 10⁴)
- Each test case:
  - `n` — size of arrays (2 ≤ n ≤ 2⋅10⁵)
  - `a1, a2, ..., an` — array `a` (0 ≤ ai < 2³⁰)
  - `b1, b2, ..., bn` — array `b` (0 ≤ bi < 2³⁰)

Total `n` across tests ≤ 2⋅10⁵.

---

## ✅ Output
For each test case, print:

```
YES
```

if it is possible to transform `a` to `b`, otherwise print:

```
NO
```

(Case insensitive output allowed)

---

## 💡 Idea

For each `i`, you may apply XOR once: `a[i] = a[i] XOR a[i+1]`.  
You must determine if sequence `a` can become `b`.

---

## 📎 Example

### **Input**
```text
7
5
1 2 3 4 5
3 2 7 1 5
3
0 0 1
1 0 1
3
0 0 1
0 0 0
4
0 0 1 2
1 3 3 2
6
1 1 4 5 1 4
0 5 4 5 5 4
3
0 1 2
2 3 2
2
10 10
11 10
```

### **Output**
```text
YES
NO
NO
NO
YES
NO
NO
```

---

## 📝 Explanation Example

For test case 1:

Initial array:

```
[1, 2, 3, 4, 5]
```

Operations:

```
i = 3 → a[3] = 3 XOR 4 = 7 → [1, 2, 7, 4, 5]
i = 4 → a[4] = 4 XOR 5 = 1 → [1, 2, 7, 1, 5]
i = 1 → a[1] = 1 XOR 2 = 3 → [3, 2, 7, 1, 5]
```

Final array becomes:

```
[3, 2, 7, 1, 5]
```

Which matches **b**, so the answer is `YES`.

---


