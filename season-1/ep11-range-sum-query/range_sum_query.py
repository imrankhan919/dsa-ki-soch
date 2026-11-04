"""Range Sum Query - Immutable (DSA ki SOCH, Ep 11). LeetCode 303:
https://leetcode.com/problems/range-sum-query-immutable/

Naya pattern: Prefix Sum. sum(i, j) bahut baar poocha jaayega.
"""


class NumArrayBrute:
    """O: har query pe i se j tak loop. Har query O(n), q queries O(n * q)."""

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i, j):
        return sum(self.nums[i:j + 1])


class NumArray:
    """H: Prefix Sum. Ek baar O(n) build, phir har query O(1): P[j+1] - P[i]."""

    def __init__(self, nums):
        self.prefix = [0]
        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]
