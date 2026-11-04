// Subarray Sums Divisible by K (DSA ki SOCH, Ep 16). LeetCode 974:
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

// H: same prefix remainder -> the span between is divisible. Time O(n), space O(k).
export function subarraysDivByK(nums, k) {
  const count = new Map([[0, 1]]);
  let prefix = 0;
  let ans = 0;
  for (const x of nums) {
    prefix += x;
    const r = ((prefix % k) + k) % k; // JS % can be negative
    ans += count.get(r) ?? 0;
    count.set(r, (count.get(r) ?? 0) + 1);
  }
  return ans;
}
