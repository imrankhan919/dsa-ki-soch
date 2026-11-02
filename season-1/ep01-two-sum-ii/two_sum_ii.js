// Two Sum II, sorted input (DSA ki SOCH, Ep 1). LeetCode 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Return: positions, 1 se ginti (index + 1). Extra memory: O(1).

// O: har pair check. Time O(n^2), extra space O(1).
export function twoSumBrute(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) return [i + 1, j + 1];
    }
  }
  return [];
}

// H: Two Pointers. Sum bada -> r peeche, chhota -> l aage. Time O(n), extra space O(1).
export function twoSum(numbers, target) {
  let l = 0;
  let r = numbers.length - 1;
  while (l < r) {
    const total = numbers[l] + numbers[r];
    if (total === target) return [l + 1, r + 1];
    if (total < target) l++;
    else r--;
  }
  return [];
}
