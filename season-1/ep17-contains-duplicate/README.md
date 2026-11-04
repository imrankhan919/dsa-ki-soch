# Ep 17 · Contains Duplicate (Hashing, naya pattern)

**Problem:** [LeetCode 217 – Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Koi number list mein do baar aaya? `true`. Sab alag? `false`.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[3, 1, 4, 1, 5]` → `1` index 1 aur 3 pe → **true**. |
| **O – Obvious** | Har pair compare: O(n²). Sort karke padosi dekho: O(n log n). |
| **C – Chokepoint** | Har number pe ek hi sawaal: **pehle dekha hai?** Iska sabse tez jawaab: hash set (dhoondhna + daalna, dono O(1)). |
| **H – Hack** | `seen = set()`. `x in seen` → `return True`. Warna `seen.add(x)`. Loop khatam → `False`. |

## Dry run (`[3, 1, 4, 1, 5]`)

| x | pehle dekha? | seen (baad mein) |
| --- | --- | --- |
| 3 | nahi | `{3}` |
| 1 | nahi | `{3, 1}` |
| 4 | nahi | `{3, 1, 4}` |
| 1 | **haan** → `return True` | |

`5` tak jaana hi nahi pada (early return).

## Teen tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har pair compare | O(n²) | O(1) |
| Sort + padosi | O(n log n) | O(1)* |
| **Hash Set** | **O(n)** | **O(n)** |

\* sort ki in-place memory language pe depend karti hai.

## Run karo

```bash
python3 test_contains_duplicate.py                                         # Python
node contains_duplicate.test.mjs                                           # JavaScript
g++ -std=c++17 -O2 contains_duplicate.cpp -o cd && ./cd && rm cd          # C++
```
