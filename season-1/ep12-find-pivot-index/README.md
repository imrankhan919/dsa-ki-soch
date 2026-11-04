# Ep 12 · Find Pivot Index (Prefix Sum)

**Problem:** [LeetCode 724 – Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Woh index dhoondho jiske **left ka sum = right ka sum** ho. Pivot khud kisi taraf nahi ginta. Na mile to `-1`.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[1, 7, 3, 6, 5, 6]` → index 3: left `1+7+3 = 11`, right `5+6 = 11`. Answer `3`. |
| **O – Obvious** | Har index pe dono taraf dobara jodo: O(n²). |
| **C – Chokepoint** | Total ek baar nikalo. `right = total − left − khud`. Left chalte chalte badhao. |
| **H – Hack** | Ek pass: `if left == total − left − x: return i`, warna `left += x`. |

## Dry run (total = 28)

| i | x | left | right = 28 − left − x | Barabar? |
| --- | --- | --- | --- | --- |
| 0 | 1 | 0 | 27 | ✗ |
| 1 | 7 | 1 | 20 | ✗ |
| 2 | 3 | 8 | 17 | ✗ |
| 3 | 6 | 11 | 11 | ✓ → `3` |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har index pe dono taraf jodo | O(n²) | O(1) |
| **Total + running left** | **O(n)** | **O(1)** |

## Run karo

```bash
python3 test_pivot_index.py                                         # Python
node pivot_index.test.mjs                                           # JavaScript
g++ -std=c++17 -O2 pivot_index.cpp -o piv && ./piv && rm piv       # C++
```
