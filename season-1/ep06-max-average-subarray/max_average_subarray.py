"""Maximum Average Subarray I (DSA ki SOCH, Ep 6). LeetCode 643:
https://leetcode.com/problems/maximum-average-subarray-i/

Lagatar k numbers (window) ka sabse bada average.
"""


def find_max_average_brute(nums, k):
    """O: har window ka sum shuru se jodo. Time O(n*k), extra space O(1)."""
    best = max(sum(nums[i:i + k]) for i in range(len(nums) - k + 1))
    return best / k


def find_max_average(nums, k):
    """H: Sliding Window. Har slide pe ek naya jodo, ek purana ghatao. Time O(n), extra space O(1)."""
    s = sum(nums[:k])
    best = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        best = max(best, s)
    return best / k
