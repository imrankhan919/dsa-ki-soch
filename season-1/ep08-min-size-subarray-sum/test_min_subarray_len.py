import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from min_subarray_len import min_sub_array_len, min_sub_array_len_brute  # noqa: E402

CASES = [
    (7, [2, 3, 1, 2, 4, 3], 2),  # the episode's example: [4, 3]
    (11, [1, 2, 3, 4, 5], 3),  # the comment question: [3, 4, 5]
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    (15, [1, 2, 3, 4, 5], 5),
]
for target, nums, want in CASES:
    assert min_sub_array_len(target, nums) == want, (target, nums)
    assert min_sub_array_len_brute(target, nums) == want, (target, nums)

rng = random.Random(8)
for _ in range(2000):
    nums = [rng.randint(1, 9) for _ in range(rng.randint(1, 12))]
    target = rng.randint(1, 40)
    assert min_sub_array_len(target, nums) == min_sub_array_len_brute(target, nums), (target, nums)

print("python: all tests passed")
