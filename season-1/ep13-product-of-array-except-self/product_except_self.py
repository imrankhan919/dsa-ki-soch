"""Product of Array Except Self (DSA ki SOCH, Ep 13). LeetCode 238:
https://leetcode.com/problems/product-of-array-except-self/

ans[i] = khud ko chhod ke baaki sab ka guna. Division allowed nahi.
"""


def product_except_self_brute(nums):
    """O: har index pe baaki sab ka guna. Time O(n^2)."""
    out = []
    for i in range(len(nums)):
        p = 1
        for j, x in enumerate(nums):
            if j != i:
                p *= x
        out.append(p)
    return out


def product_except_self(nums):
    """H: left pass (left ka guna) + right pass (right ka guna). Time O(n), extra O(1) (ans ke alawa)."""
    n = len(nums)
    ans = [1] * n
    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans
