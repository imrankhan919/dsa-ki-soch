# Ep 20 · Longest Consecutive Sequence (Hashing: set)

**Problem:** [LeetCode 128 – Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

List mein lagatar numbers (1, 2, 3, 4…) ki sabse lambi chain kitni hai? List ka order matter nahi.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[100, 4, 200, 1, 3, 2]` → `1 → 2 → 3 → 4` → **4**. |
| **O – Obvious** | Sort karke gino: O(n log n). Bina sort, har number se upar chalo aur list mein dhoondho: O(n²). |
| **C – Chokepoint** | Har number se gino toh ek hi chain baar baar giniyegi. Chain **sirf wahan se** shuru karo jahan `x − 1` set mein nahi. |
| **H – Hack** | `s = set(nums)`. `x − 1 not in s` → `y = x`, `while y + 1 in s: y += 1`, `best = max(best, y − x + 1)`. |

## Dry run

| x | x − 1 set mein? | kya hua | best |
| --- | --- | --- | --- |
| 100 | 99 nahi | start, chain 1 | 1 |
| 4 | 3 hai | skip | 1 |
| 200 | 199 nahi | start, chain 1 | 1 |
| 1 | 0 nahi | start → 2 → 3 → 4, chain 4 | **4** |
| 3 | 2 hai | skip | 4 |
| 2 | 1 hai | skip | 4 |

Har number zyada se zyada do baar chhua (ek baar loop mein, ek baar walk mein) → O(n).

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Sort + gino | O(n log n) | O(1)* |
| **Set + chain start** | **O(n)** | **O(n)** |

## Run karo

```bash
python3 test_longest_consecutive.py                                         # Python
node longest_consecutive.test.mjs                                           # JavaScript
g++ -std=c++17 -O2 longest_consecutive.cpp -o lcs && ./lcs && rm lcs       # C++
```
