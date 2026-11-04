// Find Minimum in Rotated Sorted Array (DSA ki SOCH, Ep 25). LeetCode 153:
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

// H: compare the middle with the right end. Time O(log n), space O(1).
export function findMin(nums) {
  let l = 0;
  let r = nums.length - 1;
  while (l < r) {
    const m = (l + r) >> 1;
    if (nums[m] > nums[r]) l = m + 1;
    else r = m;
  }
  return nums[l];
}
