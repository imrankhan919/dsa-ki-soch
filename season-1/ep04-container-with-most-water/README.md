# Ep 04 · Container With Most Water (Two Pointers)

**Problem:** [LeetCode 11 – Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Har number ek deewar ki height hai. Do deewarein chuno, beech mein paani bharo. Paani **chhoti deewar tak** hi rukta hai, isliye `paani = min(h[l], h[r]) × (r − l)`. Sabse zyada paani kitna?

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[3, 7, 2, 5, 4, 8, 3]`: 7 aur 8, doori 4 → `7 × 4 = 28`. |
| **O – Obvious** | Har pair: 7 deewarein → 21 pairs. O(n²). |
| **C – Chokepoint** | Lambi deewar andar laane se paani kabhi nahi badhta (chhoti hi limit hai, doori kam ho gayi). |
| **H – Hack** | `l` shuru, `r` end. Area nikalo, best update, **chhoti deewar andar**. Ek pass. |

## Dry run

| l, r | Heights | Area | Best | Move |
| --- | --- | --- | --- | --- |
| 0, 6 | 3, 3 | 3 × 6 = 18 | 18 | barabar → r |
| 0, 5 | 3, 8 | 3 × 5 = 15 | 18 | l |
| 1, 5 | 7, 8 | 7 × 4 = 28 | 28 | l |
| 2, 5 | 2, 8 | 2 × 3 = 6 | 28 | l |
| 3, 5 | 5, 8 | 5 × 2 = 10 | 28 | l |
| 4, 5 | 4, 8 | 4 × 1 = 4 | 28 | l → stop |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har pair | O(n²) | O(1) |
| **Two Pointers** | **O(n)** | **O(1)** |

## Run karo

```bash
python3 test_container.py                                    # Python
node container.test.mjs                                      # JavaScript
g++ -std=c++17 -O2 container.cpp -o container && ./container  # C++
```
