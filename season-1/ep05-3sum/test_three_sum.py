import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from three_sum import three_sum, three_sum_brute  # noqa: E402


def norm(groups):
    return sorted(tuple(g) for g in groups)


CASES = [
    ([-1, 0, 1, 2, -1, -4], [(-1, -1, 2), (-1, 0, 1)]),  # the episode's example
    ([-2, 0, 0, 2, 2], [(-2, 0, 2)]),  # the comment question: 1 unique group
    ([0, 0, 0, 0], [(0, 0, 0)]),
    ([0, 1, 1], []),
    ([3, -2, 1, 0], []),
]
for nums, want in CASES:
    assert norm(three_sum(nums)) == want, (nums, three_sum(nums))
    assert norm(three_sum_brute(nums)) == want, nums

rng = random.Random(5)
for _ in range(2000):
    nums = [rng.randint(-5, 5) for _ in range(rng.randint(0, 10))]
    assert norm(three_sum(nums)) == norm(three_sum_brute(nums)), nums

print("python: all tests passed")
