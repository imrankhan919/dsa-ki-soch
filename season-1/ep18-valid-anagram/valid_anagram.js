// Valid Anagram (DSA ki SOCH, Ep 18). LeetCode 242:
// https://leetcode.com/problems/valid-anagram/

// H: +1 for s, -1 for t, all zero at the end. Time O(n), space O(1) (26 letters).
export function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const count = new Map();
  for (const ch of s) count.set(ch, (count.get(ch) ?? 0) + 1);
  for (const ch of t) count.set(ch, (count.get(ch) ?? 0) - 1);
  for (const v of count.values()) if (v !== 0) return false;
  return true;
}
