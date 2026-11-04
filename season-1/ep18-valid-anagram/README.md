# Ep 18 · Valid Anagram (Hashing: ginti)

**Problem:** [LeetCode 242 – Valid Anagram](https://leetcode.com/problems/valid-anagram/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Kya `t`, `s` ke hi letters ko upar neeche karke bana hai?

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `race` aur `care`: dono mein ek r, ek a, ek c, ek e → **true**. |
| **O – Obvious** | s ka har letter t mein dhoondho aur kaato: O(n²). Ya dono sort karke compare: O(n log n). |
| **C – Chokepoint** | Anagram = same letters, **same ginti**. Order matter nahi karta, toh sirf ginti compare karo. |
| **H – Hack** | `s` ke har letter pe `+1`, `t` ke har letter pe `−1`. End mein sab zero → anagram. |

## Dry run (`race`, `care`)

| Step | Letter | count |
| --- | --- | --- |
| s | r, a, c, e (+1) | `{r:1, a:1, c:1, e:1}` |
| t | c, a, r, e (−1) | `{r:0, a:0, c:0, e:0}` |

Sab zero → `true`.

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Sort + compare | O(n log n) | O(n) |
| **Letter ginti (hash)** | **O(n)** | **O(1)** (sirf 26 letters) |

## Run karo

```bash
python3 test_valid_anagram.py                                          # Python
node valid_anagram.test.mjs                                            # JavaScript
g++ -std=c++17 -O2 valid_anagram.cpp -o va && ./va && rm va           # C++
```
