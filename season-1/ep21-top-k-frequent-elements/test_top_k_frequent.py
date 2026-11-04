import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from top_k_frequent import top_k_frequent, top_k_frequent_sort  # noqa: E402

CASES = [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),  # the episode's example (LeetCode 1)
    ([4, 4, 5, 5, 5, 6], 2, [5, 4]),  # the comment question
    ([1], 1, [1]),  # LeetCode 2
]
for nums, k, want in CASES:
    assert sorted(top_k_frequent(nums, k)) == sorted(want), (nums, k)
    assert sorted(top_k_frequent_sort(nums, k)) == sorted(want), (nums, k)


def valid(nums, k, got):
    c = Counter(nums)
    if len(got) != k or len(set(got)) != k:
        return False
    worst_in = min(c[x] for x in got)
    best_out = max([c[x] for x in c if x not in got] or [0])
    return worst_in >= best_out


rng = random.Random(21)
for _ in range(1000):
    nums = [rng.randint(0, 5) for _ in range(rng.randint(1, 12))]
    k = rng.randint(1, len(set(nums)))
    assert valid(nums, k, top_k_frequent(nums, k)), (nums, k)

print("python: all tests passed")
