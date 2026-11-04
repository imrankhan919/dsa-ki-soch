# Ep 25 · Find Minimum in Rotated Sorted Array (Binary Search)

**Problem:** [LeetCode 153 – Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Sorted list (sab alag numbers) kisi point se ghuma di gayi hai. Sabse chhota number O(log n) mein batao.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[0, 1, 2, 4, 5, 6, 7]` ghuma ke `[4, 5, 6, 7, 0, 1, 2]` → minimum **0**. |
| **O – Obvious** | Poori list dekho, sabse chhota yaad rakho: O(n). |
| **C – Chokepoint** | List ke do sorted hisse hain. **Beech ko right end se compare karo**: `nums[m] > nums[r]` → drop (minimum) m ke right mein; warna minimum m pe ya uske left mein. |
| **H – Hack** | `while l < r`: bada → `l = m + 1`, warna `r = m`. End mein `nums[l]`. |

## Dry run

| l | r | m | nums[m] vs nums[r] | faisla |
| --- | --- | --- | --- | --- |
| 0 | 6 | 3 | 7 > 2 | l = 4 |
| 4 | 6 | 5 | 1 ≤ 2 | r = 5 |
| 4 | 5 | 4 | 0 ≤ 1 | r = 4 |
| 4 | 4 | – | l == r | **min = 0** |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Poori list | O(n) | O(1) |
| **Binary Search** | **O(log n)** | **O(1)** |

## Run karo

```bash
python3 test_find_min.py                                         # Python
node find_min.test.mjs                                           # JavaScript
g++ -std=c++17 -O2 find_min.cpp -o fm && ./fm && rm fm          # C++
```
