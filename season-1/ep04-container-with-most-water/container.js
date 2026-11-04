// Container With Most Water (DSA ki SOCH, Ep 4). LeetCode 11: https://leetcode.com/problems/container-with-most-water/

// O: har pair. Time O(n^2), extra space O(1).
export function maxAreaBrute(height) {
  let best = 0;
  for (let i = 0; i < height.length; i++)
    for (let j = i + 1; j < height.length; j++) best = Math.max(best, Math.min(height[i], height[j]) * (j - i));
  return best;
}

// H: Two Pointers, chhoti deewar andar. Time O(n), extra space O(1).
export function maxArea(height) {
  let l = 0;
  let r = height.length - 1;
  let best = 0;
  while (l < r) {
    best = Math.max(best, Math.min(height[l], height[r]) * (r - l));
    if (height[l] < height[r]) l++;
    else r--;
  }
  return best;
}
