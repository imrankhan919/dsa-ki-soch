# Contains Duplicate (DSA ki SOCH, Ep 17). LeetCode 217:
# https://leetcode.com/problems/contains-duplicate/


# O: compare every pair. Time O(n^2).
def contains_duplicate_brute(nums):
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            if nums[a] == nums[b]:
                return True
    return False


# O (better): sort, then a duplicate must sit next to its twin. Time O(n log n).
def contains_duplicate_sort(nums):
    s = sorted(nums)
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))


# H: hash set answers "pehle dekha?" in O(1). Time O(n), space O(n).
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
