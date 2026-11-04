# Binary Search (DSA ki SOCH, Ep 22). LeetCode 704:
# https://leetcode.com/problems/binary-search/


# O: check one by one. Time O(n).
def search_linear(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1


# H: look at the middle, throw away half. Time O(log n), space O(1).
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
