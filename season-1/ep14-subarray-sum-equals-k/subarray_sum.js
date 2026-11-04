// Subarray Sum Equals K (DSA ki SOCH, Ep 14). LeetCode 560:
// https://leetcode.com/problems/subarray-sum-equals-k/

// H: prefix sum + hashmap of prefix counts. Time O(n), space O(n).
export function subarraySum(nums, k) {
  const count = new Map([[0, 1]]);
  let prefix = 0;
  let ans = 0;
  for (const x of nums) {
    prefix += x;
    ans += count.get(prefix - k) ?? 0;
    count.set(prefix, (count.get(prefix) ?? 0) + 1);
  }
  return ans;
}
