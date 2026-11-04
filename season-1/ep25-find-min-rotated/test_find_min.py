import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from find_min import find_min, find_min_linear  # noqa: E402

CASES = [
    ([4, 5, 6, 7, 0, 1, 2], 0),  # the episode's example (LeetCode 2)
    ([3, 4, 5, 1, 2], 1),  # the comment question (LeetCode 1)
    ([11, 13, 15, 17], 11),  # LeetCode 3, not rotated
    ([2, 1], 1),
    ([1], 1),
]
for nums, want in CASES:
    assert find_min(nums) == want, nums
    assert find_min_linear(nums) == want, nums

rng = random.Random(25)
for _ in range(2000):
    base = sorted(rng.sample(range(-50, 50), rng.randint(1, 15)))
    k = rng.randrange(len(base))
    nums = base[k:] + base[:k]
    assert find_min(nums) == base[0], nums

print("python: all tests passed")
