import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from range_sum_query import NumArray, NumArrayBrute  # noqa: E402

a = NumArray([3, 1, 4, 1, 5, 9])  # the episode's example
assert a.prefix == [0, 3, 4, 8, 9, 14, 23]
assert a.sumRange(1, 4) == 11
assert a.sumRange(2, 5) == 19
assert NumArray([2, 7, 1, 8, 2, 8]).sumRange(1, 3) == 16  # the comment question
lc = NumArray([-2, 0, 3, -5, 2, -1])  # LeetCode example
assert (lc.sumRange(0, 2), lc.sumRange(2, 5), lc.sumRange(0, 5)) == (1, -1, -3)

rng = random.Random(11)
for _ in range(500):
    nums = [rng.randint(-20, 20) for _ in range(rng.randint(1, 12))]
    fast, slow = NumArray(nums), NumArrayBrute(nums)
    for _ in range(10):
        i = rng.randrange(len(nums))
        j = rng.randrange(i, len(nums))
        assert fast.sumRange(i, j) == slow.sumRange(i, j)

print("python: all tests passed")
