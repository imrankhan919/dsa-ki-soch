# Ep 02 · Valid Palindrome (Two Pointers on a string)

**Problem:** [LeetCode 125 – Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Ek string di hai. Sirf **letters aur numbers** count hote hain (space, comma, `!` ignore), aur **capital = small**. Kya string aage se aur peeche se same padhi jaati hai? `True` / `False` return karo.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `"Race car!"` → clean → `"racecar"` → palindrome → `True`. |
| **O – Obvious** | Clean copy banao, ulti copy banao, compare: `t == t[::-1]`. Time O(n), par **2 extra copies** = O(n) memory. |
| **C – Chokepoint** | Ulti copy sirf ye check karne ke liye hai ki pehla aakhri se mile, doosra second last se. Ye original string mein hi ho sakta hai. |
| **H – Hack** | Two Pointers: `l` shuru, `r` end. Letter/number nahi → skip. Alag → `False`. Same → dono andar. Mil gaye → `True`. |

## Dry run: `"Race car!"`

| Step | l, r | s[l], s[r] | Action |
| --- | --- | --- | --- |
| 1 | 0, 8 | `R`, `!` | `!` skip → r peeche |
| 2 | 0, 7 | `R`, `r` | same (small mein) → dono andar |
| 3 | 1, 6 | `a`, `a` | same → dono andar |
| 4 | 2, 5 | `c`, `c` | same → dono andar |
| 5 | 3, 4 | `e`, space | space skip → r peeche |
| 6 | 3, 3 | – | l, r mil gaye → `True` |

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Clean + reverse + compare | O(n) | O(n) |
| **Two Pointers** | **O(n)** | **O(1)** |

## Run karo

```bash
python3 test_valid_palindrome.py                                                  # Python
node valid_palindrome.test.mjs                                                    # JavaScript
g++ -std=c++17 -O2 valid_palindrome.cpp -o valid_palindrome && ./valid_palindrome  # C++
```
