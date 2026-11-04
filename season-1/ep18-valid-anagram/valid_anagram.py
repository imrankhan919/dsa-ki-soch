# Valid Anagram (DSA ki SOCH, Ep 18). LeetCode 242:
# https://leetcode.com/problems/valid-anagram/


# O: sort both and compare. Time O(n log n).
def is_anagram_sort(s, t):
    return sorted(s) == sorted(t)


# H: +1 for s, -1 for t, all zero at the end. Time O(n), space O(1) (26 letters).
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        count[ch] = count.get(ch, 0) - 1
    return all(v == 0 for v in count.values())
