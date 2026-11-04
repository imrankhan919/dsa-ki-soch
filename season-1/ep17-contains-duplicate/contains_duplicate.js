// Contains Duplicate (DSA ki SOCH, Ep 17). LeetCode 217:
// https://leetcode.com/problems/contains-duplicate/

// H: hash set answers "pehle dekha?" in O(1). Time O(n), space O(n).
export function containsDuplicate(nums) {
  const seen = new Set();
  for (const x of nums) {
    if (seen.has(x)) return true;
    seen.add(x);
  }
  return false;
}
