// Find Pivot Index (DSA ki SOCH, Ep 12). LeetCode 724:
// https://leetcode.com/problems/find-pivot-index/

// H: total ek baar, left chalte chalte, right = total - left - x. Time O(n).
export function pivotIndex(nums) {
  const total = nums.reduce((a, b) => a + b, 0);
  let left = 0;
  for (let i = 0; i < nums.length; i++) {
    if (left === total - left - nums[i]) return i;
    left += nums[i];
  }
  return -1;
}
