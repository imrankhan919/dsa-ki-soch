# Ep 24 · First and Last Position (Binary Search)

**Problem:** [LeetCode 34 – Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Sorted list mein `target` ka pehla aur aakhri index. Na mile toh `[-1, -1]`.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[5, 7, 7, 8, 8, 10]`, target 8 → **[3, 4]**. |
| **O – Obvious** | Ek ek karke chalo, pehla aur aakhri 8 note karo: O(n). |
| **C – Chokepoint** | Normal binary search koi bhi ek 8 deta hai. **Mila toh `ans = m` note karo, par ruko mat**: first ke liye left jao (`r = m − 1`), last ke liye right (`l = m + 1`). |
| **H – Hack** | Ek hi function, `first` flag ke saath; do baar chalao. 2 × O(log n) = O(log n). |

## Dry run (target 8)

**Pass 1 – first**

| l | r | m | nums[m] | faisla |
| --- | --- | --- | --- | --- |
| 0 | 5 | 2 | 7 | 7 < 8 → l = 3 |
| 3 | 5 | 4 | 8 | ans = 4, r = 3 |
| 3 | 3 | 3 | 8 | ans = 3, r = 2 → **first = 3** |

**Pass 2 – last**

| l | r | m | nums[m] | faisla |
| --- | --- | --- | --- | --- |
| 0 | 5 | 2 | 7 | 7 < 8 → l = 3 |
| 3 | 5 | 4 | 8 | ans = 4, l = 5 |
| 5 | 5 | 5 | 10 | 10 > 8 → r = 4 → **last = 4** |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Ek ek karke | O(n) | O(1) |
| **2 × Binary Search** | **O(log n)** | **O(1)** |

## Run karo

```bash
python3 test_first_last.py                                         # Python
node first_last.test.mjs                                           # JavaScript
g++ -std=c++17 -O2 first_last.cpp -o fl && ./fl && rm fl          # C++
```
