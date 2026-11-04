import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subarrays_div_by_k import subarrays_div_by_k, subarrays_div_by_k_brute  # noqa: E402

CASES = [
    ([2, 3, 1, 4], 5, 3),  # the episode's example
    ([4, 2, 1], 3, 2),  # the comment question
    ([4, 5, 0, -2, -3, 1], 5, 7),  # LeetCode example 1
    ([5], 9, 0),  # LeetCode example 2
    ([-1, 2, 9], 2, 2),  # negatives
]
for nums, k, want in CASES:
    assert subarrays_div_by_k(nums, k) == want, (nums, k)
    assert subarrays_div_by_k_brute(nums, k) == want, (nums, k)

rng = random.Random(16)
for _ in range(2000):
    nums = [rng.randint(-6, 6) for _ in range(rng.randint(1, 9))]
    k = rng.randint(2, 6)
    assert subarrays_div_by_k(nums, k) == subarrays_div_by_k_brute(nums, k), (nums, k)

print("python: all tests passed")
