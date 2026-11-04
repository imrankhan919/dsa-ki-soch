# Subarray Sums Divisible by K (DSA ki SOCH, Ep 16). LeetCode 974:
# https://leetcode.com/problems/subarray-sums-divisible-by-k/


# O: every start, keep adding, count when sum % k == 0. Time O(n^2).
def subarrays_div_by_k_brute(nums, k):
    ans = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s % k == 0:
                ans += 1
    return ans


# H: same prefix remainder -> the span between is divisible. Time O(n), space O(k).
def subarrays_div_by_k(nums, k):
    count = {0: 1}
    prefix = 0
    ans = 0
    for x in nums:
        prefix += x
        r = prefix % k  # Python's % is never negative
        ans += count.get(r, 0)
        count[r] = count.get(r, 0) + 1
    return ans
