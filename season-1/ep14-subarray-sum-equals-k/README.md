# Ep 14 · Subarray Sum Equals K (Prefix Sum + HashMap)

**Problem:** [LeetCode 560 – Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Kitne lagatar hisson (subarrays) ka sum **exactly k** hai? List mein **negative numbers** bhi ho sakte hain, isliye Sliding Window nahi chalta.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[1, -1, 2, 1]`, k = 2 → `[1,-1,2]`, `[2]`, `[-1,2,1]` → **3**. |
| **O – Obvious** | Har shuruaat se aage jodo, sum = k pe gino: O(n²). Window? Negative se sum ghat bhi sakta hai, kab kaatein pata nahi. |
| **C – Chokepoint** | `sum(i+1..j) = P[j] − P[i]`. Chahiye `= k` → `P[i] = P[j] − k`. Har kadam pe poochho: **prefix − k pehle kitni baar dekha?** |
| **H – Hack** | `count = {0: 1}`. Har number: `prefix += x`, `ans += count[prefix − k]`, phir `count[prefix] += 1`. |

## Dry run (`[1, -1, 2, 1]`, k = 2)

| x | prefix | chahiye (prefix − k) | count mein? | ans | count (baad mein) |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | -1 | nahi | 0 | `{0:1, 1:1}` |
| -1 | 0 | -2 | nahi | 0 | `{0:2, 1:1}` |
| 2 | 2 | 0 | **2 baar** | 2 | `{0:2, 1:1, 2:1}` |
| 1 | 3 | 1 | **1 baar** | 3 | `{0:2, 1:1, 2:1, 3:1}` |

Answer: `3`

> `{0: 1}` seed kyun? Taaki shuru se shuru hone wale hisse (jaise `[1,-1,2]`) bhi gine jaayein.

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har hissa check | O(n²) | O(1) |
| **Prefix Sum + HashMap** | **O(n)** | **O(n)** |

## Run karo

```bash
python3 test_subarray_sum.py                                        # Python
node subarray_sum.test.mjs                                          # JavaScript
g++ -std=c++17 -O2 subarray_sum.cpp -o ssk && ./ssk && rm ssk       # C++
```
