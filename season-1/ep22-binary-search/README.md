# Ep 22 · Binary Search (naya pattern)

**Problem:** [LeetCode 704 – Binary Search](https://leetcode.com/problems/binary-search/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Sorted list mein `target` ka index batao. Na mile toh `-1`.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[1, 3, 5, 7, 9, 11, 13, 15]`, target 13 → **index 6**. |
| **O – Obvious** | Shuru se ek ek karke dekho: O(n). 13 tak 7 steps. |
| **C – Chokepoint** | List **sorted** hai. Beech dekho: chhota → left half bekaar, bada → right half bekaar. Range 8 → 4 → 2 → 1. |
| **H – Hack** | `l, r = 0, n − 1`; `m = (l + r) // 2`; equal → return; chhota → `l = m + 1`; bada → `r = m − 1`. |

## Dry run (target 13)

| l | r | m | nums[m] | faisla |
| --- | --- | --- | --- | --- |
| 0 | 7 | 3 | 7 | 7 < 13 → l = 4 |
| 4 | 7 | 5 | 11 | 11 < 13 → l = 6 |
| 6 | 7 | 6 | 13 | mil gaya → **6** |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Ek ek karke | O(n) | O(1) |
| **Binary Search** | **O(log n)** | **O(1)** |

## Run karo

```bash
python3 test_binary_search.py                                       # Python
node binary_search.test.mjs                                         # JavaScript
g++ -std=c++17 -O2 binary_search.cpp -o bs && ./bs && rm bs        # C++
```
