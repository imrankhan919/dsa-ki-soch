import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contains_duplicate import contains_duplicate, contains_duplicate_brute, contains_duplicate_sort  # noqa: E402

CASES = [
    ([3, 1, 4, 1, 5], True),  # the episode's example
    ([5, 2, 8, 2, 9], True),  # the comment question (found at index 3)
    ([1, 2, 3, 1], True),  # LeetCode example 1
    ([1, 2, 3, 4], False),  # LeetCode example 2
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),  # LeetCode example 3
    ([7], False),
]
for nums, want in CASES:
    for f in (contains_duplicate, contains_duplicate_brute, contains_duplicate_sort):
        assert f(nums) == want, (f.__name__, nums)

rng = random.Random(17)
for _ in range(2000):
    nums = [rng.randint(-9, 9) for _ in range(rng.randint(1, 10))]
    assert contains_duplicate(nums) == contains_duplicate_brute(nums) == contains_duplicate_sort(nums), nums

print("python: all tests passed")
