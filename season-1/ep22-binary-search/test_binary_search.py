import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from binary_search import search, search_linear  # noqa: E402

NUMS = [1, 3, 5, 7, 9, 11, 13, 15]
CASES = [
    (NUMS, 13, 6),  # the episode's example
    (NUMS, 4, -1),  # the comment question (3 steps, not found)
    ([-1, 0, 3, 5, 9, 12], 9, 4),  # LeetCode 1
    ([-1, 0, 3, 5, 9, 12], 2, -1),  # LeetCode 2
    ([5], 5, 0),
]
for nums, target, want in CASES:
    assert search(nums, target) == want, (nums, target)
    assert search_linear(nums, target) == want, (nums, target)

rng = random.Random(22)
for _ in range(2000):
    nums = sorted(rng.sample(range(-30, 30), rng.randint(1, 12)))
    target = rng.randint(-32, 32)
    assert search(nums, target) == search_linear(nums, target), (nums, target)

print("python: all tests passed")
