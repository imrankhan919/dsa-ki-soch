"""Longest Substring Without Repeating Characters (DSA ki SOCH, Ep 7). LeetCode 3:
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Sabse lamba lagatar hissa jismein koi letter repeat na ho.
"""


def length_of_longest_substring_brute(s):
    """O: har (start, end) ka substring, har ek mein repeat check. Time O(n^3)."""
    best = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            part = s[i:j + 1]
            if len(set(part)) == len(part):
                best = max(best, len(part))
    return best


def length_of_longest_substring(s):
    """H: variable Sliding Window + set. Right badhao, repeat aaye to left ghatao. Time O(n)."""
    seen = set()
    l = best = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        best = max(best, r - l + 1)
    return best
