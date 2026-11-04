# First and Last Position (DSA ki SOCH, Ep 24). LeetCode 34:
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


# O: walk once, note the first and last match. Time O(n).
def search_range_linear(nums, target):
    first = last = -1
    for i, x in enumerate(nums):
        if x == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


# H: binary search that does not stop on a match: note ans = m, then keep
# going left (first) or right (last). Time O(log n), space O(1).
def search(nums, target, first):
    l, r, ans = 0, len(nums) - 1, -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            ans = m
            if first:
                r = m - 1
            else:
                l = m + 1
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans


def search_range(nums, target):
    return [search(nums, target, True), search(nums, target, False)]
