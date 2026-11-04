import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pivot_index import pivot_index, pivot_index_brute  # noqa: E402

CASES = [
    ([1, 7, 3, 6, 5, 6], 3),  # the episode's example
    ([2, 1, -1], 0),  # the comment question: left 0, right 1 + (-1) = 0
    ([1, 2, 3], -1),
    ([0], 0),
    ([-1, -1, 0, 1, 1, 0], 5),
]
for nums, want in CASES:
    assert pivot_index(nums) == want, nums
    assert pivot_index_brute(nums) == want, nums

rng = random.Random(12)
for _ in range(3000):
    nums = [rng.randint(-3, 3) for _ in range(rng.randint(1, 9))]
    assert pivot_index(nums) == pivot_index_brute(nums), nums

print("python: all tests passed")
