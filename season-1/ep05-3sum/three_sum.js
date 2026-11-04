// 3Sum (DSA ki SOCH, Ep 5). LeetCode 15: https://leetcode.com/problems/3sum/

// H: sort + har i fix + baaki pe Two Pointers. Time O(n^2).
export function threeSum(input) {
  const nums = [...input].sort((a, b) => a - b);
  const seen = new Set();
  const res = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let l = i + 1;
    let r = nums.length - 1;
    while (l < r) {
      const s = nums[i] + nums[l] + nums[r];
      if (s === 0) {
        const key = `${nums[i]},${nums[l]},${nums[r]}`;
        if (!seen.has(key)) {
          seen.add(key);
          res.push([nums[i], nums[l], nums[r]]);
        }
        l++;
        r--;
      } else if (s < 0) l++;
      else r--;
    }
  }
  return res;
}
