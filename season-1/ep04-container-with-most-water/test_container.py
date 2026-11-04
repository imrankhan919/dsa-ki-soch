import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from container import max_area, max_area_brute  # noqa: E402

CASES = [
    ([3, 7, 2, 5, 4, 8, 3], 28),  # the episode's example
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # the comment question
    ([1, 1], 1),
    ([4, 6, 3, 7, 8], 18),  # the C-step example
]
for fn in (max_area_brute, max_area):
    for h, want in CASES:
        assert fn(h) == want, f"{fn.__name__}({h}) = {fn(h)}, want {want}"

rng = random.Random(4)
for _ in range(3000):
    h = [rng.randint(0, 12) for _ in range(rng.randint(2, 12))]
    assert max_area(h) == max_area_brute(h), h

print("python: all tests passed")
