# Ep 03 · Move Zeroes (Two Pointers, same direction)

**Problem:** [LeetCode 283 – Move Zeroes](https://leetcode.com/problems/move-zeroes/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

List mein saare `0` end mein bhejo. Baaki numbers ka **order same** rahe, aur kaam **isi list mein** ho (in-place), nayi list nahi.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[0, 3, 0, 5, 8]` → `[3, 5, 8, 0, 0]`. Order same, in-place. |
| **O – Obvious** | Zero mila? `remove` karo, `append` karo. Har remove pe baaki list khisakti hai → O(n²). |
| **C – Chokepoint** | Asli kaam: non-zero ko aage, line se rakhna. Pehla non-zero jagah 0 pe, doosra jagah 1 pe... |
| **H – Hack** | `w` = agla non-zero kahan jaayega, `r` = list padhta hai. `nums[r] != 0` → swap(w, r), `w += 1`. |

## Dry run: `[0, 3, 0, 5, 8]`

| r | nums[r] | Action | nums after | w |
| --- | --- | --- | --- | --- |
| 0 | 0 | aage | `[0, 3, 0, 5, 8]` | 0 |
| 1 | 3 | swap(0, 1) | `[3, 0, 0, 5, 8]` | 1 |
| 2 | 0 | aage | `[3, 0, 0, 5, 8]` | 1 |
| 3 | 5 | swap(1, 3) | `[3, 5, 0, 0, 8]` | 2 |
| 4 | 8 | swap(2, 4) | `[3, 5, 8, 0, 0]` | 3 |

## Teeno tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Remove + append | O(n²) | O(1) |
| Nayi list | O(n) | O(n) (allowed nahi) |
| **Two Pointers** | **O(n)** | **O(1)** |

## Run karo

```bash
python3 test_move_zeroes.py                                            # Python
node move_zeroes.test.mjs                                              # JavaScript
g++ -std=c++17 -O2 move_zeroes.cpp -o move_zeroes && ./move_zeroes     # C++
```
