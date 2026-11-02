import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from two_sum_ii import two_sum, two_sum_brute  # noqa: E402

CASES = [
    ([2, 5, 6, 7, 9, 13], 13, [3, 4]),  # the episode's example
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),  # negatives
    ([1, 3, 4, 6, 8], 10, [3, 4]),  # the comment question
    ([3, 3], 6, [1, 2]),  # duplicates
]

for fn in (two_sum_brute, two_sum):
    for nums, target, want in CASES:
        got = fn(nums, target)
        assert got == want, f"{fn.__name__}({nums}, {target}) = {got}, want {want}"


def steps(numbers, target):
    l, r, k = 0, len(numbers) - 1, 0
    while l < r:
        k += 1
        s = numbers[l] + numbers[r]
        if s == target:
            return k
        if s < target:
            l += 1
        else:
            r -= 1
    return k


assert steps([2, 5, 6, 7, 9, 13], 13) == 5  # "sirf paanch steps"
assert steps([1, 3, 4, 6, 8], 10) == 4  # comment question answer

# random cross-check against brute force on sorted inputs with exactly one answer
rng = random.Random(11)
checked = 0
while checked < 2000:
    nums = sorted(rng.randint(-20, 20) for _ in range(rng.randint(2, 12)))
    target = rng.randint(-40, 40)
    pairs = [(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target]
    if len({(nums[i], nums[j]) for i, j in pairs}) != 1 or len(pairs) != 1:
        continue
    assert two_sum(nums, target) == two_sum_brute(nums, target), (nums, target)
    checked += 1

print("python: all tests passed")
