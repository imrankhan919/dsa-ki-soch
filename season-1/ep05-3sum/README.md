# Ep 05 · 3Sum (sort + Two Pointers)

**Problem:** [LeetCode 15 – 3Sum](https://leetcode.com/problems/3sum/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Teen numbers chuno jinka sum `0` ho. Saare aise groups do, lekin **koi group do baar nahi** (list mein same number do baar ho, tab bhi).

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[-1, 0, 1, 2, -1, -4]` → `[-1, 0, 1]` aur `[-1, -1, 2]`. |
| **O – Obvious** | Teen loops: 6 numbers pe 20 groups. O(n³), upar se duplicates hatao. |
| **C – Chokepoint** | Ek number fix karo (maan lo −1) → baaki do ka sum `+1` chahiye = **Two Sum**. Sort kar do to sorted Two Sum = Ep 1 ka Two Pointers. |
| **H – Hack** | Sort → har `i` fix (pichle jaisa ho to skip) → `l = i+1`, `r = end` → Two Pointers. |

## Dry run (sorted: `[-4, -1, -1, 0, 1, 2]`)

| i | Chahiye | Pairs check | Result |
| --- | --- | --- | --- |
| −4 | 4 | 1, 1, 2, 3 (sab chhote) | — |
| −1 | 1 | −1+2 = 1 ✓, 0+1 = 1 ✓ | `[-1,-1,2]`, `[-1,0,1]` |
| −1 | — | pichle jaisa → skip | — |
| 0 | 0 | 1+2 = 3 (bada) | — |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Teen loops | O(n³) | O(1) + dedupe |
| **Sort + Two Pointers** | **O(n²)** | **O(1)** (answer ke alawa) |

## Run karo

```bash
python3 test_three_sum.py                                   # Python
node three_sum.test.mjs                                     # JavaScript
g++ -std=c++17 -O2 three_sum.cpp -o three_sum && ./three_sum  # C++
```
