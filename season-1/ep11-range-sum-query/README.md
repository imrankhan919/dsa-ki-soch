# Ep 11 · Range Sum Query (naya pattern: Prefix Sum)

**Problem:** [LeetCode 303 – Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Ek list, aur bahut saare sawaal: index `i` se `j` tak ka sum kitna?

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[3, 1, 4, 1, 5, 9]` → `sum(1, 4) = 1+4+1+5 = 11`, `sum(2, 5) = 19`. Aise sawaal hazaaron baar. |
| **O – Obvious** | Har sawaal pe loop: ek sawaal O(n), q sawaal O(n·q). 10 lakh × 10 lakh = lakh crore kaam. |
| **C – Chokepoint** | Wahi jodna baar baar ho raha hai. Ek baar **running total** likh lo. |
| **H – Hack** | `P[k]` = pehle k numbers ka sum (`P[0] = 0`). `sum(i, j) = P[j+1] − P[i]`. |

## Dry run

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `P[k]` | 0 | 3 | 4 | 8 | 9 | 14 | 23 |

- `sum(1, 4) = P[5] − P[1] = 14 − 3 = 11`
- `sum(2, 5) = P[6] − P[2] = 23 − 4 = 19`

## Dono tareeke

| Approach | Build | Har query | Extra space |
| --- | --- | --- | --- |
| Har query pe loop | – | O(n) | O(1) |
| **Prefix Sum** | **O(n)** | **O(1)** | **O(n)** |

## Run karo

```bash
python3 test_range_sum_query.py                                         # Python
node range_sum_query.test.mjs                                           # JavaScript
g++ -std=c++17 -O2 range_sum_query.cpp -o rsq && ./rsq && rm rsq        # C++
```
