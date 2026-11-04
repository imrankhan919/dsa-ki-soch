# Contiguous Array (DSA ki SOCH, Ep 15). LeetCode 525:
# https://leetcode.com/problems/contiguous-array/


# O: every start, count 0s and 1s, note length when equal. Time O(n^2).
def find_max_length_brute(nums):
    best = 0
    for i in range(len(nums)):
        bal = 0
        for j in range(i, len(nums)):
            bal += 1 if nums[j] == 1 else -1
            if bal == 0:
                best = max(best, j - i + 1)
    return best


# H: 0 -> -1, prefix sum, keep the FIRST index of every prefix. Time O(n), space O(n).
def find_max_length(nums):
    first = {0: -1}
    prefix = 0
    best = 0
    for i, x in enumerate(nums):
        prefix += 1 if x == 1 else -1
        if prefix in first:
            best = max(best, i - first[prefix])
        else:
            first[prefix] = i
    return best
