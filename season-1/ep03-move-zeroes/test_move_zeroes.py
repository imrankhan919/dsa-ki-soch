import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from move_zeroes import count_swaps, move_zeroes, move_zeroes_brute  # noqa: E402

CASES = [
    ([0, 3, 0, 5, 8], [3, 5, 8, 0, 0]),  # the episode's example
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 1], [1, 0, 0]),
    ([1, 2, 0, 3], [1, 2, 3, 0]),
]
for fn in (move_zeroes_brute, move_zeroes):
    for nums, want in CASES:
        a = list(nums)
        assert fn(a) is None and a == want, f"{fn.__name__}({nums}) -> {a}, want {want}"

assert count_swaps([0, 3, 0, 5, 8]) == 3
assert count_swaps([1, 2, 0, 3]) == 3  # comment question answer (2 khud se + 1 asli)

rng = random.Random(3)
for _ in range(3000):
    nums = [rng.choice([0, 0, 1, 2, -5, 7]) for _ in range(rng.randint(0, 12))]
    a, b = list(nums), list(nums)
    move_zeroes(a)
    move_zeroes_brute(b)
    assert a == b == [x for x in nums if x != 0] + [0] * nums.count(0), nums

print("python: all tests passed")
