// Move Zeroes (DSA ki SOCH, Ep 3). LeetCode 283: https://leetcode.com/problems/move-zeroes/

// O: zero nikalo, end mein daalo. Time O(n^2), extra space O(1).
export function moveZeroesBrute(nums) {
  let zeros = nums.filter((x) => x === 0).length;
  while (zeros-- > 0) {
    nums.splice(nums.indexOf(0), 1);
    nums.push(0);
  }
}

// H: Two Pointers, ek hi direction. Time O(n), extra space O(1).
export function moveZeroes(nums) {
  let w = 0;
  for (let r = 0; r < nums.length; r++) {
    if (nums[r] !== 0) {
      [nums[w], nums[r]] = [nums[r], nums[w]];
      w++;
    }
  }
}
