// Two Sum — 3 tareeke se (DSA ki SOCH, Ep 0). LeetCode 1: https://leetcode.com/problems/two-sum/

// O: har pair check. Time O(n^2), extra space O(1).
export function twoSumBrute(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
  return [];
}

// H1: sort + two pointers, original index saath rakho. Time O(n log n), space O(n).
export function twoSumSorted(nums, target) {
  const pairs = nums.map((v, i) => [v, i]).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  let left = 0;
  let right = pairs.length - 1;
  while (left < right) {
    const s = pairs[left][0] + pairs[right][0];
    if (s === target) return [pairs[left][1], pairs[right][1]].sort((a, b) => a - b);
    if (s < target) left++;
    else right--;
  }
  return [];
}

// H2: hash map, one pass. Pehle check, phir daalo. Time O(n) average, space O(n).
export function twoSum(nums, target) {
  const seen = new Map(); // number -> index
  for (let i = 0; i < nums.length; i++) {
    const need = target - nums[i];
    if (seen.has(need)) return [seen.get(need), i];
    seen.set(nums[i], i);
  }
  return [];
}
