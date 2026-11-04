// Top K Frequent Elements (DSA ki SOCH, Ep 21). LeetCode 347:
// https://leetcode.com/problems/top-k-frequent-elements/

// H: count, then bucket[f] = numbers seen f times, walk buckets from the top. Time O(n).
export function topKFrequent(nums, k) {
  const count = new Map();
  for (const x of nums) count.set(x, (count.get(x) ?? 0) + 1);
  const buckets = Array.from({length: nums.length + 1}, () => []);
  for (const [x, f] of count) buckets[f].push(x);
  const ans = [];
  for (let f = nums.length; f > 0; f--) {
    for (const x of buckets[f]) {
      ans.push(x);
      if (ans.length === k) return ans;
    }
  }
  return ans;
}
