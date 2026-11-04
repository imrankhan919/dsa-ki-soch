# Ep 13 · Product of Array Except Self (Prefix × Suffix)

**Problem:** [LeetCode 238 – Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

`ans[i]` = khud ko chhod ke baaki sab numbers ka guna. **Division allowed nahi.**

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `[1, 2, 3, 4]` → `[24, 12, 8, 6]`. |
| **O – Obvious** | Har index pe baaki sab ka guna: O(n²). Total ÷ nums[i]? Allowed nahi, aur zero pe fail. |
| **C – Chokepoint** | `ans[i] = (left ka guna) × (right ka guna)`. Index 2: `1×2 = 2`, right `4` → `8`. |
| **H – Hack** | Left pass: `ans[i] = left`, `left *= nums[i]`. Right pass: `ans[i] *= right`, `right *= nums[i]`. |

## Dry run

| Pass | i | ans | left / right |
| --- | --- | --- | --- |
| Left | 0..3 | `[1, 1, 2, 6]` | left = 24 |
| Right | 3 | `6 × 1 = 6` | right = 4 |
| Right | 2 | `2 × 4 = 8` | right = 12 |
| Right | 1 | `1 × 12 = 12` | right = 24 |
| Right | 0 | `1 × 24 = 24` | right = 24 |

Answer: `[24, 12, 8, 6]`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har index pe sab ka guna | O(n²) | O(1) |
| **Left pass + Right pass** | **O(n)** | **O(1)** (answer ke alawa) |

## Run karo

```bash
python3 test_product_except_self.py                                             # Python
node product_except_self.test.mjs                                               # JavaScript
g++ -std=c++17 -O2 product_except_self.cpp -o pes && ./pes && rm pes            # C++
```
