# Ep 15 · Contiguous Array (Prefix Sum + HashMap)

**Problem:** [LeetCode 525 – Contiguous Array](https://leetcode.com/problems/contiguous-array/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Binary list mein sabse lamba lagatar hissa jismein **0 aur 1 barabar** hon. Uski length return karo.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[1, 0, 1, 1, 1, 0, 0]` → index 1..6 (teen 0, teen 1) → **6**. |
| **O – Obvious** | Har shuruaat se aage badho, 0 aur 1 gino: O(n²). |
| **C – Chokepoint** | **0 ko −1 bana do.** Barabar ⇔ sum 0 ⇔ prefix pehle wala hi wapas aaya. Length = `i − first[prefix]`. |
| **H – Hack** | `first = {0: -1}`. Prefix pehle dekha? `best = max(best, i − first[prefix])`. Naya? `first[prefix] = i` (sirf **pehla** index, taaki hissa sabse lamba ho). |

## Dry run (`[1, 0, 1, 1, 1, 0, 0]`)

| i | x | prefix | first mein? | length | best |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | naya → first[1] = 0 | | 0 |
| 1 | 0 | 0 | -1 pe | 2 | 2 |
| 2 | 1 | 1 | 0 pe | 2 | 2 |
| 3 | 1 | 2 | naya → first[2] = 3 | | 2 |
| 4 | 1 | 3 | naya → first[3] = 4 | | 2 |
| 5 | 0 | 2 | 3 pe | 2 | 2 |
| 6 | 0 | 1 | 0 pe | **6** | **6** |

Answer: `6`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har hissa check | O(n²) | O(1) |
| **Prefix + pehla index (HashMap)** | **O(n)** | **O(n)** |

## Run karo

```bash
python3 test_contiguous_array.py                                          # Python
node contiguous_array.test.mjs                                            # JavaScript
g++ -std=c++17 -O2 contiguous_array.cpp -o ca && ./ca && rm ca            # C++
```
