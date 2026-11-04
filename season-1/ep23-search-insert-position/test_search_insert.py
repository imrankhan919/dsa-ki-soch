import bisect
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from search_insert import search_insert, search_insert_linear  # noqa: E402

NUMS = [1, 3, 5, 7, 9, 11, 13, 15]
CASES = [
    (NUMS, 4, 2),  # the episode's example
    (NUMS, 16, 8),  # the comment question (after the last element)
    (NUMS, 13, 6),  # found
    (NUMS, 0, 0),  # before the first element
    ([1, 3, 5, 6], 5, 2),  # LeetCode 1
    ([1, 3, 5, 6], 2, 1),  # LeetCode 2
    ([1, 3, 5, 6], 7, 4),  # LeetCode 3
]
for nums, target, want in CASES:
    assert search_insert(nums, target) == want, (nums, target)
    assert search_insert_linear(nums, target) == want, (nums, target)

rng = random.Random(23)
for _ in range(2000):
    nums = sorted(rng.sample(range(-30, 30), rng.randint(1, 12)))
    target = rng.randint(-32, 32)
    want = bisect.bisect_left(nums, target)
    assert search_insert(nums, target) == want, (nums, target)
    assert search_insert_linear(nums, target) == want, (nums, target)

print("python: all tests passed")
