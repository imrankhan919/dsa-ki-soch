# Search Insert Position (DSA ki SOCH, Ep 23). LeetCode 35:
# https://leetcode.com/problems/search-insert-position/


# O: first index whose value is >= target. Time O(n).
def search_insert_linear(nums, target):
    for i, x in enumerate(nums):
        if x >= target:
            return i
    return len(nums)


# H: plain binary search; when the loop ends (l > r), everything up to r is
# smaller and everything from l is bigger, so l is the insert slot.
# Time O(log n), space O(1).
def search_insert(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return l
