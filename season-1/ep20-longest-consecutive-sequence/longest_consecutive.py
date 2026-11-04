# Longest Consecutive Sequence (DSA ki SOCH, Ep 20). LeetCode 128:
# https://leetcode.com/problems/longest-consecutive-sequence/


# O: sort, then count runs (skip duplicates). Time O(n log n).
def longest_consecutive_sort(nums):
    if not nums:
        return 0
    s = sorted(set(nums))
    best = run = 1
    for a, b in zip(s, s[1:]):
        run = run + 1 if b == a + 1 else 1
        best = max(best, run)
    return best


# H: only start counting where x - 1 is missing. Time O(n), space O(n).
def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)
    return best
