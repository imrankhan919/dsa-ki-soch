import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from valid_anagram import is_anagram, is_anagram_sort  # noqa: E402

CASES = [
    ("race", "care", True),  # the episode's example
    ("rat", "car", False),  # the comment question
    ("anagram", "nagaram", True),  # LeetCode example 1
    ("a", "ab", False),
    ("aacc", "ccac", False),
]
for s, t, want in CASES:
    assert is_anagram(s, t) == want, (s, t)
    assert is_anagram_sort(s, t) == want, (s, t)

rng = random.Random(18)
for _ in range(2000):
    s = "".join(rng.choice("abc") for _ in range(rng.randint(0, 6)))
    t = "".join(rng.choice("abc") for _ in range(rng.randint(0, 6)))
    assert is_anagram(s, t) == is_anagram_sort(s, t), (s, t)

print("python: all tests passed")
