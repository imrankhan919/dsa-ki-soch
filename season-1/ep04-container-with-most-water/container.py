"""Container With Most Water (DSA ki SOCH, Ep 4). LeetCode 11: https://leetcode.com/problems/container-with-most-water/

Har number ek deewar ki height. Do deewarein chuno: paani = chhoti height x doori. Sabse zyada paani?
"""


def max_area_brute(height):
    """O: har pair. Time O(n^2), extra space O(1)."""
    best = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            best = max(best, min(height[i], height[j]) * (j - i))
    return best


def max_area(height):
    """H: Two Pointers. Hamesha chhoti deewar andar. Time O(n), extra space O(1)."""
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        best = max(best, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best


if __name__ == "__main__":
    print(max_area([3, 7, 2, 5, 4, 8, 3]))  # 28
