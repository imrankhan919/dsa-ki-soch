// First and Last Position (DSA ki SOCH, Ep 24). LeetCode 34:
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

// H: binary search that keeps going after a match. Time O(log n), space O(1).
function search(nums, target, first) {
  let l = 0;
  let r = nums.length - 1;
  let ans = -1;
  while (l <= r) {
    const m = (l + r) >> 1;
    if (nums[m] === target) {
      ans = m;
      if (first) r = m - 1;
      else l = m + 1;
    } else if (nums[m] < target) l = m + 1;
    else r = m - 1;
  }
  return ans;
}

export function searchRange(nums, target) {
  return [search(nums, target, true), search(nums, target, false)];
}
