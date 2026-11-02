"""Two Sum — 3 tareeke se (DSA ki SOCH, Ep 0).

Problem (apne shabdon mein): numbers ki list aur ek target. Do ALAG positions dhoondho
jinke numbers ka sum target ho; unke index return karo. Exactly ek answer hai.
LeetCode 1: https://leetcode.com/problems/two-sum/
"""


def two_sum_brute(nums, target):
    """O: har pair check. Time O(n^2), extra space O(1)."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_sorted(nums, target):
    """H1: sort + two pointers. Original index saath rakho. Time O(n log n), space O(n)."""
    pairs = sorted((v, i) for i, v in enumerate(nums))
    left, right = 0, len(pairs) - 1
    while left < right:
        s = pairs[left][0] + pairs[right][0]
        if s == target:
            return sorted([pairs[left][1], pairs[right][1]])
        if s < target:
            left += 1
        else:
            right -= 1
    return []


def two_sum(nums, target):
    """H2: hash map, one pass. Pehle check, phir daalo. Time O(n) average, space O(n)."""
    seen = {}  # number -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []
