"""3Sum (DSA ki SOCH, Ep 5). LeetCode 15: https://leetcode.com/problems/3sum/

Teen numbers jinka sum 0 ho. Saare unique groups (koi group do baar nahi).
"""
from itertools import combinations


def three_sum_brute(nums):
    """O: teen loops (har group). Time O(n^3). Duplicate groups set se hatao."""
    return sorted({tuple(sorted(c)) for c in combinations(nums, 3) if sum(c) == 0})


def three_sum(nums):
    """H: sort + har i fix + baaki pe Two Pointers. Time O(n^2), extra space O(1) (answer ke alawa)."""
    nums = sorted(nums)
    res = set()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.add((nums[i], nums[l], nums[r]))
                l, r = l + 1, r - 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return [list(g) for g in res]


if __name__ == "__main__":
    print(sorted(three_sum([-1, 0, 1, 2, -1, -4])))  # [[-1, -1, 2], [-1, 0, 1]]
