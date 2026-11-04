import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subarray_sum import subarray_sum, subarray_sum_brute  # noqa: E402

CASES = [
    ([1, -1, 2, 1], 2, 3),  # the episode's example
    ([1, 2, 3], 3, 2),  # the comment question
    ([1, 1, 1], 2, 2),  # LeetCode example
    ([0, 0, 0], 0, 6),
    ([5], 5, 1),
    ([-1, -1, 1], 0, 1),
]
for nums, k, want in CASES:
    assert subarray_sum(nums, k) == want, (nums, k)
    assert subarray_sum_brute(nums, k) == want, (nums, k)

rng = random.Random(14)
for _ in range(2000):
    nums = [rng.randint(-3, 3) for _ in range(rng.randint(1, 9))]
    k = rng.randint(-4, 4)
    assert subarray_sum(nums, k) == subarray_sum_brute(nums, k), (nums, k)

print("python: all tests passed")
