# Ep 19 · Group Anagrams (Hashing: key → group)

**Problem:** [LeetCode 49 – Group Anagrams](https://leetcode.com/problems/group-anagrams/)

**Video:** [E-Skills YouTube](https://www.youtube.com/@eskillsweb)

Words ki list. Jo ek doosre ke anagram hain, unhe ek group mein daalo.

## S.O.C.H.

| Step | Idea |
| --- | --- |
| **S – Samjho** | `eat tea tan ate nat bat` → `[eat, tea, ate]`, `[tan, nat]`, `[bat]` → **3 groups**. |
| **O – Obvious** | Har pair compare karo (anagram hai?): O(n²), upar se har compare mein letters ginna. |
| **C – Chokepoint** | Anagrams ke letters same → **sorted letters same**. `eat, tea, ate` → `"aet"`. Yahi key! |
| **H – Hack** | `groups[key].append(word)` with `key = ''.join(sorted(word))`. End mein saari lists. |

## Dry run

| word | key | group |
| --- | --- | --- |
| eat | aet | naya |
| tea | aet | wahi |
| tan | ant | naya |
| ate | aet | wahi |
| nat | ant | wahi |
| bat | abt | naya |

Answer: `[[eat, tea, ate], [tan, nat], [bat]]`

## Dono tareeke

| Approach | Time | Extra space |
| --- | --- | --- |
| Har pair compare | O(n² · k) | O(n) |
| **Sorted key + HashMap** | **O(n · k log k)** | **O(n · k)** |

(n = words, k = sabse lamba word)

## Run karo

```bash
python3 test_group_anagrams.py                                          # Python
node group_anagrams.test.mjs                                            # JavaScript
g++ -std=c++17 -O2 group_anagrams.cpp -o ga && ./ga && rm ga           # C++
```
