import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from first_last import search_range, search_range_linear  # noqa: E402

NUMS = [5, 7, 7, 8, 8, 10]
CASES = [
    (NUMS, 8, [3, 4]),  # the episode's example (LeetCode 1)
    (NUMS, 7, [1, 2]),  # the comment question
    (NUMS, 6, [-1, -1]),  # LeetCode 2
    ([], 0, [-1, -1]),  # LeetCode 3
    ([2, 2, 2, 2], 2, [0, 3]),
]
for nums, target, want in CASES:
    assert search_range(nums, target) == want, (nums, target)
    assert search_range_linear(nums, target) == want, (nums, target)

rng = random.Random(24)
for _ in range(2000):
    nums = sorted(rng.choice(range(-8, 8)) for _ in range(rng.randint(0, 14)))
    target = rng.randint(-9, 9)
    assert search_range(nums, target) == search_range_linear(nums, target), (nums, target)

print("python: all tests passed")
