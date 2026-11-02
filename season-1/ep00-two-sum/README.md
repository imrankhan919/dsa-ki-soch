# Ep 00 · Two Sum (3 tareeke se)

**Problem:** [LeetCode 1 – Two Sum](https://leetcode.com/problems/two-sum/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Numbers ki ek list aur ek target diya hai. Do **alag** positions dhoondho jinke numbers ka sum target ke barabar ho, aur unke index return karo. Exactly ek answer hai.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | Same element do baar use nahi kar sakte. Duplicates aa sakte hain (`[3, 3]`, target 6 → `[0, 1]`). |
| **O – Obvious** | Har pair check karo (do loops). |
| **C – Chokepoint** | Har number ke liye `need = target - num` dhoondhne ke liye poori list baar baar scan ho rahi hai. |
| **H – Hack** | Jo dekha, use dictionary (hash map) mein yaad rakho. `need in seen` ek step mein. |

## Teen tareeke

| Approach | Time | Extra space | Function |
| --- | --- | --- | --- |
| Brute force (har pair) | O(n²) | O(1) | `two_sum_brute` |
| Sort + Two Pointers | O(n log n) | O(n) | `two_sum_sorted` |
| Hash map (one pass) | O(n) | O(n) | `two_sum` |

## Run karo

```bash
python3 test_two_sum.py                               # Python
node two_sum.test.mjs                                 # JavaScript
g++ -std=c++17 -O2 two_sum.cpp -o two_sum && ./two_sum   # C++
```

## Homework

Agar list pehle se **sorted** ho, toh dictionary ke bina kaise karoge? (Hint: `two_sum_sorted` dekho. Next episode: Two Pointers.)
