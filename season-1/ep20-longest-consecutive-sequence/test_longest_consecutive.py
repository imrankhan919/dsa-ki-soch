import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from longest_consecutive import longest_consecutive, longest_consecutive_sort  # noqa: E402

CASES = [
    ([100, 4, 200, 1, 3, 2], 4),  # the episode's example (LeetCode 1)
    ([5, 6, 1, 7, 2], 3),  # the comment question
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),  # LeetCode 2
    ([], 0),
    ([1, 2, 0, 1], 3),
]
for nums, want in CASES:
    assert longest_consecutive(nums) == want, nums
    assert longest_consecutive_sort(nums) == want, nums

rng = random.Random(20)
for _ in range(2000):
    nums = [rng.randint(-8, 8) for _ in range(rng.randint(0, 10))]
    assert longest_consecutive(nums) == longest_consecutive_sort(nums), nums

print("python: all tests passed")
