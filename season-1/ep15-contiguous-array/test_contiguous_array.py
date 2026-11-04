import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contiguous_array import find_max_length, find_max_length_brute  # noqa: E402

CASES = [
    ([1, 0, 1, 1, 1, 0, 0], 6),  # the episode's example
    ([0, 0, 1, 0, 1], 4),  # the comment question
    ([0, 1], 2),  # LeetCode example 1
    ([0, 1, 0], 2),  # LeetCode example 2
    ([1, 1, 1], 0),
    ([0], 0),
]
for nums, want in CASES:
    assert find_max_length(nums) == want, nums
    assert find_max_length_brute(nums) == want, nums

rng = random.Random(15)
for _ in range(2000):
    nums = [rng.randint(0, 1) for _ in range(rng.randint(1, 12))]
    assert find_max_length(nums) == find_max_length_brute(nums), nums

print("python: all tests passed")
