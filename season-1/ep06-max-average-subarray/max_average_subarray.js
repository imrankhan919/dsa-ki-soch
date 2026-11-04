// Maximum Average Subarray I (DSA ki SOCH, Ep 6). LeetCode 643:
// https://leetcode.com/problems/maximum-average-subarray-i/

// H: Sliding Window. Har slide pe ek naya jodo, ek purana ghatao. Time O(n).
export function findMaxAverage(nums, k) {
  let s = 0;
  for (let i = 0; i < k; i++) s += nums[i];
  let best = s;
  for (let i = k; i < nums.length; i++) {
    s += nums[i] - nums[i - k];
    best = Math.max(best, s);
  }
  return best / k;
}
