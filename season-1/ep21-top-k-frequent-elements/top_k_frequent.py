# Top K Frequent Elements (DSA ki SOCH, Ep 21). LeetCode 347:
# https://leetcode.com/problems/top-k-frequent-elements/


# O: count, sort by frequency, take the first k. Time O(n log n).
def top_k_frequent_sort(nums, k):
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1
    return [x for x, _ in sorted(count.items(), key=lambda p: -p[1])[:k]]


# H: count, then bucket[f] = numbers seen f times, walk buckets from the top. Time O(n).
def top_k_frequent(nums, k):
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for x, f in count.items():
        buckets[f].append(x)
    ans = []
    for f in range(len(nums), 0, -1):
        for x in buckets[f]:
            ans.append(x)
            if len(ans) == k:
                return ans
    return ans
