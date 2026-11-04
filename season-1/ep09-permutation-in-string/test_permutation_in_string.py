import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from permutation_in_string import check_inclusion, check_inclusion_brute  # noqa: E402

CASES = [
    ("ab", "eidbaooo", True),  # the episode's example: "ba"
    ("ab", "eidboaoo", False),  # the comment question
    ("adc", "dcda", True),
    ("abc", "ab", False),
    ("a", "a", True),
    ("hello", "ooolleoooleh", False),
]
for s1, s2, want in CASES:
    assert check_inclusion(s1, s2) == want, (s1, s2)
    assert check_inclusion_brute(s1, s2) == want, (s1, s2)

rng = random.Random(9)
for _ in range(2000):
    s1 = "".join(rng.choice("abc") for _ in range(rng.randint(1, 4)))
    s2 = "".join(rng.choice("abc") for _ in range(rng.randint(0, 10)))
    assert check_inclusion(s1, s2) == check_inclusion_brute(s1, s2), (s1, s2)

print("python: all tests passed")
