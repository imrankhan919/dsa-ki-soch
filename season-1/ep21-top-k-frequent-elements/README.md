# Ep 21 · Top K Frequent Elements (Hashing + Bucket)

**Problem:** [LeetCode 347 – Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Sabse zyada baar aane wale `k` numbers return karo (order koi bhi).

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[1, 1, 1, 2, 2, 3]`, k = 2 → 1 (3 baar), 2 (2 baar) → **[1, 2]**. |
| **O – Obvious** | Gino, frequency se sort karo, upar ke k uthao: O(n log n). |
| **C – Chokepoint** | Frequency kabhi `n` se zyada nahi. Toh `n` baaltiyan: `bucket[f]` = jo `f` baar aaye. Upar se neeche chalo. |
| **H – Hack** | count map → `buckets[f].append(x)` → `f = n … 1` tak uthao jab tak `k` na ho jaayein. |

## Dry run

| Step | State |
| --- | --- |
| Ginti | `{1: 3, 2: 2, 3: 1}` |
| Baaltiyan | `b[3] = [1]`, `b[2] = [2]`, `b[1] = [3]` |
| Upar se | `b[6], b[5], b[4]` khaali → `b[3]`: 1 → `b[2]`: 2 → k poora |

Answer: `[1, 2]`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Ginti + sort | O(n log n) | O(n) |
| **Ginti + bucket** | **O(n)** | **O(n)** |

## Run karo

```bash
python3 test_top_k_frequent.py                                        # Python
node top_k_frequent.test.mjs                                          # JavaScript
g++ -std=c++17 -O2 top_k_frequent.cpp -o tk && ./tk && rm tk         # C++
```
