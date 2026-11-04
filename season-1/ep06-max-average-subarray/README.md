# Ep 06 · Maximum Average Subarray I (Sliding Window)

**Problem:** [LeetCode 643 – Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Lagatar `k` numbers ka group = **window**. Har window ka average nikalo, sabse bada batao.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[2, 6, 1, 8, 3, 7]`, `k = 3` → windows `9, 15, 12, 18` → best `18 / 3 = 6`. |
| **O – Obvious** | Har window ka sum shuru se jodo: har window pe `k` additions. O(n·k). |
| **C – Chokepoint** | `[2,6,1]` se `[6,1,8]`: sirf `2` bahar, `8` andar. `6, 1` wahi ke wahi! |
| **H – Hack** | Purane sum mein se nikla number ghatao, naya jodo. Har slide pe sirf do kaam. |

## Dry run (`k = 3`)

| Window | Kaam | Sum | best |
| --- | --- | --- | --- |
| `[2, 6, 1]` | 2 + 6 + 1 | 9 | 9 |
| `[6, 1, 8]` | 9 + 8 − 2 | 15 | 15 |
| `[1, 8, 3]` | 15 + 3 − 6 | 12 | 15 |
| `[8, 3, 7]` | 12 + 7 − 1 | 18 | 18 |

Answer: `18 / 3 = 6.0`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har window dobara jodo | O(n·k) | O(1) |
| **Sliding Window** | **O(n)** | **O(1)** |

## Run karo

```bash
python3 test_max_average_subarray.py                                              # Python
node max_average_subarray.test.mjs                                                # JavaScript
g++ -std=c++17 -O2 max_average_subarray.cpp -o max_avg && ./max_avg && rm max_avg  # C++
```
