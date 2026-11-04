// Permutation in String (DSA ki SOCH, Ep 9). LeetCode 567:
// https://leetcode.com/problems/permutation-in-string/

// H: fixed Sliding Window + ginti (26 letters). Naya letter +1, purana -1. Time O(n).
export function checkInclusion(s1, s2) {
  const k = s1.length;
  if (k > s2.length) return false;
  const need = new Array(26).fill(0);
  const win = new Array(26).fill(0);
  const idx = (ch) => ch.charCodeAt(0) - 97;
  for (let i = 0; i < k; i++) {
    need[idx(s1[i])]++;
    win[idx(s2[i])]++;
  }
  const same = () => need.every((v, i) => v === win[i]);
  if (same()) return true;
  for (let i = k; i < s2.length; i++) {
    win[idx(s2[i])]++;
    win[idx(s2[i - k])]--;
    if (same()) return true;
  }
  return false;
}
