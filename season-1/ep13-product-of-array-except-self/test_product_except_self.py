import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_except_self import product_except_self, product_except_self_brute  # noqa: E402

CASES = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),  # the episode's example
    ([2, 3, 0, 4], [0, 0, 24, 0]),  # the comment question (zero trap)
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),  # LeetCode example
    ([0, 0], [0, 0]),
    ([5, 2], [2, 5]),
]
for nums, want in CASES:
    assert product_except_self(nums) == want, nums
    assert product_except_self_brute(nums) == want, nums

rng = random.Random(13)
for _ in range(2000):
    nums = [rng.randint(-4, 4) for _ in range(rng.randint(2, 8))]
    assert product_except_self(nums) == product_except_self_brute(nums), nums

print("python: all tests passed")
