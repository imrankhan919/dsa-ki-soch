# Ep 16 · Subarray Sums Divisible by K (Prefix Sum + HashMap)

**Problem:** [LeetCode 974 – Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Kitne lagatar hisson (subarrays) ka sum **k se divide** hota hai?

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[2, 3, 1, 4]`, k = 5 → `[2,3]` = 5, `[1,4]` = 5, `[2,3,1,4]` = 10 → **3**. |
| **O – Obvious** | Har shuruaat se jodo, har sum `% k` check karo: O(n²). |
| **C – Chokepoint** | `P[i] % k == P[j] % k` ⇒ `P[j] − P[i]` k se divide. Matlab beech ka hissa divisible! Prefix ki jagah **remainder ki ginti** rakho. |
| **H – Hack** | `count = {0: 1}`. Har number: `r = prefix % k`, `ans += count[r]`, phir `count[r] += 1`. |

> Negative numbers: Python mein `%` hamesha 0..k−1 deta hai. Java/C++/JS mein `((prefix % k) + k) % k` likho.

## Dry run (`[2, 3, 1, 4]`, k = 5)

| x | prefix | r = prefix % 5 | count[r] pehle | ans | count (baad mein) |
| --- | --- | --- | --- | --- | --- |
| 2 | 2 | 2 | 0 (naya) | 0 | `{0:1, 2:1}` |
| 3 | 5 | 0 | **1** | 1 | `{0:2, 2:1}` |
| 1 | 6 | 1 | 0 (naya) | 1 | `{0:2, 2:1, 1:1}` |
| 4 | 10 | 0 | **2** | 3 | `{0:3, 2:1, 1:1}` |

Answer: `3`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har hissa check | O(n²) | O(1) |
| **Remainder + HashMap** | **O(n)** | **O(k)** |

## Run karo

```bash
python3 test_subarrays_div_by_k.py                                       # Python
node subarrays_div_by_k.test.mjs                                         # JavaScript
g++ -std=c++17 -O2 subarrays_div_by_k.cpp -o sdk && ./sdk && rm sdk     # C++
```
