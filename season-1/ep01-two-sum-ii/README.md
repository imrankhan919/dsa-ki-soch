# Ep 01 · Two Sum II (Two Pointers)

**Problem:** [LeetCode 167 – Two Sum II, Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Numbers ki list **pehle se sorted** hai (chhote se bade) aur ek target diya hai. Do numbers dhoondho jinka sum target ke barabar ho. Answer mein unki **positions** do, jo 1 se ginte hain (index + 1). Extra memory sirf constant, matlab koi dictionary nahi.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | List sorted hai. Answer 1-indexed. Extra memory O(1). |
| **O – Obvious** | Har pair check karo (do loops): O(n²). Dictionary fast hai, par O(n) memory leti hai. |
| **C – Chokepoint** | Sorted ka fayda koi nahi utha raha. Sabse chhota + sabse bada > target? Toh sabse bada kisi ke saath kaam ka nahi. Ek check, ek number bahar. |
| **H – Hack** | Two Pointers: `l` shuru mein, `r` end mein. Sum bada → `r -= 1`, chhota → `l += 1`, barabar → answer. |

## Dry run: `[2, 5, 6, 7, 9, 13]`, target 13

| Step | l, r | Sum | Action |
| --- | --- | --- | --- |
| 1 | 0, 5 | 2 + 13 = 15 | bada → r peeche |
| 2 | 0, 4 | 2 + 9 = 11 | chhota → l aage |
| 3 | 1, 4 | 5 + 9 = 14 | bada → r peeche |
| 4 | 1, 3 | 5 + 7 = 12 | chhota → l aage |
| 5 | 2, 3 | 6 + 7 = 13 | answer: positions [3, 4] |

## Teeno tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Brute force | O(n²) | O(1) |
| Dictionary (hash map) | O(n) | O(n) |
| **Two Pointers** | **O(n)** | **O(1)** |

## Run karo

```bash
python3 test_two_sum_ii.py                                     # Python
node two_sum_ii.test.mjs                                       # JavaScript
g++ -std=c++17 -O2 two_sum_ii.cpp -o two_sum_ii && ./two_sum_ii   # C++
```
