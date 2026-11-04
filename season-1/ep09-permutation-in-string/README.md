# Ep 09 · Permutation in String (Sliding Window + ginti)

**Problem:** [LeetCode 567 – Permutation in String](https://leetcode.com/problems/permutation-in-string/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Kya `s1` ka koi arrangement (permutation) `s2` mein **lagatar** milta hai? Permutation = wahi letters, wahi ginti, order kuch bhi.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `s1 = "ab"`, `s2 = "eidbaooo"` → `"ba"` index 3 pe hai. Answer `true`. |
| **O – Obvious** | Har window sort karo, sorted `s1` se milao: O(n·k log k). Saare permutations banao: k! (aur bura). |
| **C – Chokepoint** | Order ki fikar hi nahi. Sirf **ginti** milani hai. |
| **H – Hack** | Window size `k` fix. Ginti rakho: naya letter `+1`, nikla letter `−1`. Ginti barabar? `true`. |

## Dry run (`s1 = "ab"`)

| Window | Kaam | Ginti | Match? |
| --- | --- | --- | --- |
| `ei` | pehli window | e:1 i:1 | ✗ |
| `id` | +d, −e | i:1 d:1 | ✗ |
| `db` | +b, −i | d:1 b:1 | ✗ |
| `ba` | +a, −d | a:1 b:1 | ✓ → `true` |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har window sort karo | O(n·k log k) | O(k) |
| **Ginti + Sliding Window** | **O(n)** | **O(1)** (26 letters) |

## Run karo

```bash
python3 test_permutation_in_string.py                                             # Python
node permutation_in_string.test.mjs                                               # JavaScript
g++ -std=c++17 -O2 permutation_in_string.cpp -o pis && ./pis && rm pis            # C++
```
