# Ep 07 · Longest Substring Without Repeating Characters (Sliding Window, variable)

**Problem:** [LeetCode 3 – Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Sabse lamba **lagatar** hissa (substring) jismein koi letter do baar na ho.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `"pwwkew"` → `"pw"` theek, `"pww"` nahi (w do baar). Sabse lamba `"wke"` = 3. `"pwke"` nahi chalega, woh lagatar nahi hai. |
| **O – Obvious** | Har (start, end) ka substring banao, har ek mein repeat check. 6 letters pe 21 substrings. O(n³). |
| **C – Chokepoint** | Repeat aane pe poora shuru se mat karo. Left se letters nikalo jab tak purana copy bahar na ho. |
| **H – Hack** | Window ka size fix nahi: `r` se badhao, repeat aaye to `l` se ghatao. Andar ke letters ek `set` mein. |

## Dry run (`"pwwkew"`)

| r | Letter | Kaam | Window | len | best |
| --- | --- | --- | --- | --- | --- |
| 0 | p | andar | `p` | 1 | 1 |
| 1 | w | andar | `pw` | 2 | 2 |
| 2 | w | repeat → `p`, `w` nikle, phir `w` andar | `w` | 1 | 2 |
| 3 | k | andar | `wk` | 2 | 2 |
| 4 | e | andar | `wke` | 3 | 3 |
| 5 | w | repeat → `w` nikla, phir `w` andar | `kew` | 3 | 3 |

Answer: `3`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Saare substrings check | O(n³) | O(n) |
| **Sliding Window + set** | **O(n)** | **O(n)** (alphabet jitna max) |

Har letter ek baar andar aata hai, ek baar bahar: isliye O(n).

## Run karo

```bash
python3 test_longest_substring.py                                              # Python
node longest_substring.test.mjs                                                # JavaScript
g++ -std=c++17 -O2 longest_substring.cpp -o lss && ./lss && rm lss             # C++
```
