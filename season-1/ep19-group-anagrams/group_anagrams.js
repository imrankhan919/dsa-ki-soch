// Group Anagrams (DSA ki SOCH, Ep 19). LeetCode 49:
// https://leetcode.com/problems/group-anagrams/

// H: sorted letters are the key; anagrams share it. Time O(n * k log k).
export function groupAnagrams(words) {
  const groups = new Map();
  for (const w of words) {
    const key = [...w].sort().join('');
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(w);
  }
  return [...groups.values()];
}
