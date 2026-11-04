"""Longest Repeating Character Replacement (DSA ki SOCH, Ep 10). LeetCode 424:
https://leetcode.com/problems/longest-repeating-character-replacement/

Zyada se zyada k letters badal sakte ho. Sabse lamba hissa jismein saare letters same hon.
"""
from collections import Counter


def character_replacement_brute(s, k):
    """O: har hissa gino: badlaav = length - max count. Time O(n^2 * 26)."""
    best = 0
    for i in range(len(s)):
        c = Counter()
        for j in range(i, len(s)):
            c[s[j]] += 1
            if (j - i + 1) - max(c.values()) <= k:
                best = max(best, j - i + 1)
    return best


def character_replacement(s, k):
    """H: variable Sliding Window. badlaav = len - maxf; k se zyada ho to left se nikalo. Time O(n)."""
    count = {}
    l = best = maxf = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
