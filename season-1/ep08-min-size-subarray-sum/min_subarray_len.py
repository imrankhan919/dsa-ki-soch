"""Minimum Size Subarray Sum (DSA ki SOCH, Ep 8). LeetCode 209:
https://leetcode.com/problems/minimum-size-subarray-sum/

Sabse chhota lagatar hissa jiska sum >= target. Nahi mila to 0. (Saare numbers positive.)
"""


def min_sub_array_len_brute(target, nums):
    """O: har shuruaat se jodte jao jab tak sum target tak na pahunche. Time O(n^2)."""
    best = float("inf")
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s >= target:
                best = min(best, j - i + 1)
                break
    return 0 if best == float("inf") else best


def min_sub_array_len(target, nums):
    """H: variable Sliding Window. Sum kam? r badhao. Pura? length note karo, l se kaato. Time O(n)."""
    l = s = 0
    best = float("inf")
    for r in range(len(nums)):
        s += nums[r]
        while s >= target:
            best = min(best, r - l + 1)
            s -= nums[l]
            l += 1
    return 0 if best == float("inf") else best
