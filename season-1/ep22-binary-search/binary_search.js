// Binary Search (DSA ki SOCH, Ep 22). LeetCode 704:
// https://leetcode.com/problems/binary-search/

// H: look at the middle, throw away half. Time O(log n), space O(1).
export function search(nums, target) {
  let l = 0;
  let r = nums.length - 1;
  while (l <= r) {
    const m = (l + r) >> 1;
    if (nums[m] === target) return m;
    if (nums[m] < target) l = m + 1;
    else r = m - 1;
  }
  return -1;
}
