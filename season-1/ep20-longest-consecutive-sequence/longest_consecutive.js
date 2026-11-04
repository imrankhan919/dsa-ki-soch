// Longest Consecutive Sequence (DSA ki SOCH, Ep 20). LeetCode 128:
// https://leetcode.com/problems/longest-consecutive-sequence/

// H: only start counting where x - 1 is missing. Time O(n), space O(n).
export function longestConsecutive(nums) {
  const s = new Set(nums);
  let best = 0;
  for (const x of s) {
    if (s.has(x - 1)) continue;
    let y = x;
    while (s.has(y + 1)) y++;
    best = Math.max(best, y - x + 1);
  }
  return best;
}
