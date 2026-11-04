import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from max_average_subarray import find_max_average, find_max_average_brute  # noqa: E402

CASES = [
    ([2, 6, 1, 8, 3, 7], 3, 6.0),  # the episode's example: best window [8, 3, 7] = 18
    ([4, 2, 5, 1, 6], 2, 3.5),  # the comment question: best sum 7 ([2, 5] or [1, 6])
    ([1, 12, -5, -6, 50, 3], 4, 12.75),  # LeetCode example
    ([5], 1, 5.0),
    ([-1, -2, -3], 2, -1.5),
]
for nums, k, want in CASES:
    assert abs(find_max_average(nums, k) - want) < 1e-9, (nums, k)
    assert abs(find_max_average_brute(nums, k) - want) < 1e-9, (nums, k)

rng = random.Random(6)
for _ in range(2000):
    nums = [rng.randint(-50, 50) for _ in range(rng.randint(1, 15))]
    k = rng.randint(1, len(nums))
    assert abs(find_max_average(nums, k) - find_max_average_brute(nums, k)) < 1e-9, (nums, k)

print("python: all tests passed")
