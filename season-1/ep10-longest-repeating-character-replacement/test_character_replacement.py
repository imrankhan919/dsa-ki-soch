import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from character_replacement import character_replacement, character_replacement_brute  # noqa: E402

CASES = [
    ("AABABBA", 1, 4),  # the episode's example
    ("ABBCB", 1, 4),  # the comment question: BBCB -> BBBB
    ("ABAB", 2, 4),
    ("AAAA", 0, 4),
    ("ABCDE", 1, 2),
    ("", 2, 0),
]
for s, k, want in CASES:
    assert character_replacement(s, k) == want, (s, k)
    assert character_replacement_brute(s, k) == want, (s, k)

rng = random.Random(10)
for _ in range(2000):
    s = "".join(rng.choice("ABC") for _ in range(rng.randint(0, 12)))
    k = rng.randint(0, 3)
    assert character_replacement(s, k) == character_replacement_brute(s, k), (s, k)

print("python: all tests passed")
