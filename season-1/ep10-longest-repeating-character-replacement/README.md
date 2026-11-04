# Ep 10 · Longest Repeating Character Replacement (Sliding Window, last boss)

**Problem:** [LeetCode 424 – Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Zyada se zyada `k` letters badal sakte ho. Sabse lamba hissa batao jismein saare letters same hon.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `"AABABBA"`, `k = 1` → `"AABA"` mein B ko A bana do: `"AAAA"`, length 4. |
| **O – Obvious** | Har hissa gino: sabse zyada wala letter rakho, baaki badlo. O(n²) (ya n³). |
| **C – Chokepoint** | Ek window ka sawaal: **badlaav = length − max count**. k se zyada? Left se nikalo. |
| **H – Hack** | `r` se badhao, ginti aur `maxf` update. `while len − maxf > k`: `l` aage. `best` = sabse lambi valid window. |

## Dry run (`k = 1`)

| r | Letter | Window | len − maxf | Kaam | best |
| --- | --- | --- | --- | --- | --- |
| 0 | A | `A` | 1 − 1 = 0 | ✓ | 1 |
| 1 | A | `AA` | 2 − 2 = 0 | ✓ | 2 |
| 2 | B | `AAB` | 3 − 2 = 1 | ✓ | 3 |
| 3 | A | `AABA` | 4 − 3 = 1 | ✓ | 4 |
| 4 | B | `AABAB` | 5 − 3 = 2 | A nikla | 4 |
| 5 | B | `ABABB` | 5 − 3 = 2 | A nikla | 4 |
| 6 | A | `BABBA` | 5 − 3 = 2 | B nikla | 4 |

Answer: `4`

> `maxf` kabhi kam nahi hota. Isse answer galat nahi hota: window tabhi badi hoti hai jab koi letter sach mein `maxf` se zyada baar aaye.

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har hissa gino | O(n²) | O(1) |
| **Sliding Window** | **O(n)** | **O(1)** (26 letters) |

## Run karo

```bash
python3 test_character_replacement.py                                           # Python
node character_replacement.test.mjs                                             # JavaScript
g++ -std=c++17 -O2 character_replacement.cpp -o cr && ./cr && rm cr             # C++
```
