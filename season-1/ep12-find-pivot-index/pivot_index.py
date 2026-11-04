"""Find Pivot Index (DSA ki SOCH, Ep 12). LeetCode 724:
https://leetcode.com/problems/find-pivot-index/

Woh index jiske left ka sum = right ka sum (index khud kisi taraf nahi). Na mile to -1.
"""


def pivot_index_brute(nums):
    """O: har index pe dono taraf dobara jodo. Time O(n^2)."""
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i
    return -1


def pivot_index(nums):
    """H: total ek baar, left chalte chalte, right = total - left - x. Time O(n), memory O(1)."""
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
