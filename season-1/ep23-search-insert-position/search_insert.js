// Search Insert Position (DSA ki SOCH, Ep 23). LeetCode 35:
// https://leetcode.com/problems/search-insert-position/

// H: plain binary search; when l > r, l is the insert slot. Time O(log n), space O(1).
export function searchInsert(nums, target) {
  let l = 0;
  let r = nums.length - 1;
  while (l <= r) {
    const m = (l + r) >> 1;
    if (nums[m] === target) return m;
    if (nums[m] < target) l = m + 1;
    else r = m - 1;
  }
  return l;
}
