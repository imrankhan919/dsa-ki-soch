// Range Sum Query - Immutable (DSA ki SOCH, Ep 11). LeetCode 303:
// https://leetcode.com/problems/range-sum-query-immutable/

// H: Prefix Sum. Ek baar O(n) build, phir har query O(1): P[j+1] - P[i].
export class NumArray {
  constructor(nums) {
    this.prefix = [0];
    for (const x of nums) this.prefix.push(this.prefix[this.prefix.length - 1] + x);
  }

  sumRange(i, j) {
    return this.prefix[j + 1] - this.prefix[i];
  }
}
