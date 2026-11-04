# Ep 08 · Minimum Size Subarray Sum (Sliding Window, variable)

**Problem:** [LeetCode 209 – Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Sabse chhota lagatar hissa jiska sum `>= target` ho. Koi hissa target tak na pahunche to `0`. Saare numbers positive hain.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[2, 3, 1, 2, 4, 3]`, target `7` → `[2,3,1,2]` sum 8 (length 4), `[4,3]` sum 7 (length 2). Answer `2`. |
| **O – Obvious** | Har shuruaat se jodte jao jab tak sum target tak na pahunche. O(n²). |
| **C – Chokepoint** | Positive numbers: right badhao to sum badhta, left badhao to sum ghatta. Pura hua? Note karo aur left se kaato. |
| **H – Hack** | Variable window: `r` se jodo, `while sum >= target` length note karo aur `l` se ghatao. |

## Dry run (target `7`)

| Kaam | Window | sum | best |
| --- | --- | --- | --- |
| +2, +3, +1 | `[2,3,1]` | 6 | ∞ |
| +2 | `[2,3,1,2]` | 8 ✓ | 4 |
| −2 | `[3,1,2]` | 6 | 4 |
| +4 | `[3,1,2,4]` | 10 ✓ | 4 |
| −3 | `[1,2,4]` | 7 ✓ | 3 |
| −1 | `[2,4]` | 6 | 3 |
| +3 | `[2,4,3]` | 9 ✓ | 3 |
| −2 | `[4,3]` | 7 ✓ | 2 |
| −4 | `[3]` | 3 | 2 |

Answer: `2`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har shuruaat se jodo | O(n²) | O(1) |
| **Sliding Window** | **O(n)** | **O(1)** |

## Run karo

```bash
python3 test_min_subarray_len.py                                            # Python
node min_subarray_len.test.mjs                                              # JavaScript
g++ -std=c++17 -O2 min_subarray_len.cpp -o msl && ./msl && rm msl           # C++
```
