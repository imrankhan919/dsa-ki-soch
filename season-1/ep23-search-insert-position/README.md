# Ep 23 · Search Insert Position (Binary Search)

**Problem:** [LeetCode 35 – Search Insert Position](https://leetcode.com/problems/search-insert-position/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Sorted list mein `target` mile toh uska index. Na mile toh woh index jahan daalne pe list sorted rahe.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[1, 3, 5, 7, 9, 11, 13, 15]`, target 4 → 3 aur 5 ke beech → **index 2**. |
| **O – Obvious** | Shuru se chalo; pehla number jo `>= target` ho, wahi jagah: O(n). |
| **C – Chokepoint** | Binary search ke end mein `l > r`. `r` tak sab chhote, `l` se sab bade → **`l` hi insert ki jagah**. |
| **H – Hack** | Wahi binary search, bas end mein `return -1` ki jagah `return l`. |

## Dry run (target 4)

| l | r | m | nums[m] | faisla |
| --- | --- | --- | --- | --- |
| 0 | 7 | 3 | 7 | 7 > 4 → r = 2 |
| 0 | 2 | 1 | 3 | 3 < 4 → l = 2 |
| 2 | 2 | 2 | 5 | 5 > 4 → r = 1 |
| 2 | 1 | – | – | l > r → **return l = 2** |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Ek ek karke | O(n) | O(1) |
| **Binary Search → l** | **O(log n)** | **O(1)** |

## Run karo

```bash
python3 test_search_insert.py                                        # Python
node search_insert.test.mjs                                          # JavaScript
g++ -std=c++17 -O2 search_insert.cpp -o si && ./si && rm si         # C++
```
