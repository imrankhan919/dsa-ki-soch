import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_sum import two_sum, two_sum_brute, two_sum_sorted  # noqa: E402

CASES = [
    ([5, 9, 2, 13, 7, 6], 13, [4, 5]),  # the episode's example
    ([3, 4, 2], 6, [1, 2]),  # same element twice is not allowed
    ([3, 3], 6, [0, 1]),  # duplicates
    ([4, 1, 7], 8, [1, 2]),  # the AI Check input
    ([-3, 4, 0, 3], 0, [0, 3]),  # negatives
    ([0, 5, 0], 0, [0, 2]),  # zeros
]

for fn in (two_sum_brute, two_sum_sorted, two_sum):
    for nums, target, want in CASES:
        got = sorted(fn(nums, target))
        assert got == want, f"{fn.__name__}({nums}, {target}) = {got}, want {want}"

# random cross-check: all three agree on inputs with exactly one answer
rng = random.Random(7)
for _ in range(2000):
    n = rng.randint(2, 12)
    nums = rng.sample(range(-50, 50), n)
    i, j = sorted(rng.sample(range(n), 2))
    target = nums[i] + nums[j]
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n) if nums[a] + nums[b] == target]
    if len(pairs) != 1:
        continue
    for fn in (two_sum_brute, two_sum_sorted, two_sum):
        assert sorted(fn(nums, target)) == [i, j], (fn.__name__, nums, target)

print("python: all tests passed")
