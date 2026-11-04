"""Move Zeroes (DSA ki SOCH, Ep 3). LeetCode 283: https://leetcode.com/problems/move-zeroes/

Saare 0 end mein bhejo, baaki numbers ka order same rahe. Isi list mein (in-place), nayi list nahi.
"""


def move_zeroes_brute(nums):
    """O: zero nikalo, end mein daalo. Har remove pe baaki list khisakti hai. Time O(n^2), extra space O(1)."""
    for _ in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)


def move_zeroes(nums):
    """H: Two Pointers, ek hi direction. w = agla non-zero kahan jaayega, r = list padhta hai. Time O(n), extra space O(1)."""
    w = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1


def count_swaps(nums):
    """Kitne swaps (khud se swap bhi) — comment question ke liye."""
    nums = list(nums)
    w = swaps = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
            swaps += 1
    return swaps


if __name__ == "__main__":
    a = [0, 3, 0, 5, 8]
    move_zeroes(a)
    print(a)  # [3, 5, 8, 0, 0]
