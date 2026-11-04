# Subarray Sum Equals K (DSA ki SOCH, Ep 14). LeetCode 560:
# https://leetcode.com/problems/subarray-sum-equals-k/


# O: every start, keep adding, count when sum == k. Time O(n^2).
def subarray_sum_brute(nums, k):
    ans = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s == k:
                ans += 1
    return ans


# H: prefix sum + hashmap of prefix counts. Time O(n), space O(n).
def subarray_sum(nums, k):
    count = {0: 1}
    prefix = 0
    ans = 0
    for x in nums:
        prefix += x
        ans += count.get(prefix - k, 0)
        count[prefix] = count.get(prefix, 0) + 1
    return ans
