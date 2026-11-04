// Product of Array Except Self (DSA ki SOCH, Ep 13). LeetCode 238:
// https://leetcode.com/problems/product-of-array-except-self/

// H: left pass + right pass, no division. Time O(n).
export function productExceptSelf(nums) {
  const n = nums.length;
  const ans = new Array(n).fill(1);
  let left = 1;
  for (let i = 0; i < n; i++) {
    ans[i] = left;
    left *= nums[i];
  }
  let right = 1;
  for (let i = n - 1; i >= 0; i--) {
    ans[i] *= right;
    right *= nums[i];
  }
  return ans.map((v) => (Object.is(v, -0) ? 0 : v));
}
