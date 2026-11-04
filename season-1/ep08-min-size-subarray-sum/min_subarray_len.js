// Minimum Size Subarray Sum (DSA ki SOCH, Ep 8). LeetCode 209:
// https://leetcode.com/problems/minimum-size-subarray-sum/

// H: variable Sliding Window. Sum kam? r badhao. Pura? length note karo, l se kaato. Time O(n).
export function minSubArrayLen(target, nums) {
  let l = 0;
  let s = 0;
  let best = Infinity;
  for (let r = 0; r < nums.length; r++) {
    s += nums[r];
    while (s >= target) {
      best = Math.min(best, r - l + 1);
      s -= nums[l];
      l++;
    }
  }
  return best === Infinity ? 0 : best;
}
