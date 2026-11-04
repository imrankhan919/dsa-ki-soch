// Contiguous Array (DSA ki SOCH, Ep 15). LeetCode 525:
// https://leetcode.com/problems/contiguous-array/

// H: 0 -> -1, prefix sum, keep the FIRST index of every prefix. Time O(n), space O(n).
export function findMaxLength(nums) {
  const first = new Map([[0, -1]]);
  let prefix = 0;
  let best = 0;
  nums.forEach((x, i) => {
    prefix += x === 1 ? 1 : -1;
    if (first.has(prefix)) best = Math.max(best, i - first.get(prefix));
    else first.set(prefix, i);
  });
  return best;
}
