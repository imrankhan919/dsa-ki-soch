// Longest Substring Without Repeating Characters (DSA ki SOCH, Ep 7). LeetCode 3:
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

// H: variable Sliding Window + set. Right badhao, repeat aaye to left ghatao. Time O(n).
export function lengthOfLongestSubstring(s) {
  const seen = new Set();
  let l = 0;
  let best = 0;
  for (let r = 0; r < s.length; r++) {
    while (seen.has(s[r])) {
      seen.delete(s[l]);
      l++;
    }
    seen.add(s[r]);
    best = Math.max(best, r - l + 1);
  }
  return best;
}
