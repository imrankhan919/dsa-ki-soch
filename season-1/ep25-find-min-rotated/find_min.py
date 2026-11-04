# Find Minimum in Rotated Sorted Array (DSA ki SOCH, Ep 25). LeetCode 153:
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


# O: look at everything. Time O(n).
def find_min_linear(nums):
    return min(nums)


# H: compare the middle with the right end. Bigger → the drop is to the
# right of m; otherwise the minimum is m or to its left. Time O(log n), space O(1).
def find_min(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]
