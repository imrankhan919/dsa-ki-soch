"""Permutation in String (DSA ki SOCH, Ep 9). LeetCode 567:
https://leetcode.com/problems/permutation-in-string/

Kya s1 ka koi arrangement (permutation) s2 mein lagatar milta hai?
"""
from collections import Counter


def check_inclusion_brute(s1, s2):
    """O: har window sort karo, sorted s1 se milao. Time O(n * k log k)."""
    k = len(s1)
    target = sorted(s1)
    return any(sorted(s2[i:i + k]) == target for i in range(len(s2) - k + 1))


def check_inclusion(s1, s2):
    """H: fixed Sliding Window + ginti. Naya letter +1, purana -1. Time O(n), memory O(26)."""
    k = len(s1)
    if k > len(s2):
        return False
    need = Counter(s1)
    window = Counter(s2[:k])
    if window == need:
        return True
    for i in range(k, len(s2)):
        window[s2[i]] += 1
        window[s2[i - k]] -= 1
        if window == need:
            return True
    return False
