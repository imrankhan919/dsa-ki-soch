// Longest Repeating Character Replacement (DSA ki SOCH, Ep 10). LeetCode 424:
// https://leetcode.com/problems/longest-repeating-character-replacement/

// H: variable Sliding Window. badlaav = len - maxf; k se zyada ho to left se nikalo. Time O(n).
export function characterReplacement(s, k) {
  const count = {};
  let l = 0;
  let best = 0;
  let maxf = 0;
  for (let r = 0; r < s.length; r++) {
    count[s[r]] = (count[s[r]] ?? 0) + 1;
    maxf = Math.max(maxf, count[s[r]]);
    while (r - l + 1 - maxf > k) {
      count[s[l]]--;
      l++;
    }
    best = Math.max(best, r - l + 1);
  }
  return best;
}
