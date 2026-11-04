import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from longest_substring import length_of_longest_substring, length_of_longest_substring_brute  # noqa: E402

CASES = [
    ("pwwkew", 3),  # the episode's example: "wke"
    ("dvdf", 3),  # the comment question: "vdf"
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("", 0),
    (" ", 1),
    ("abba", 2),
]
for s, want in CASES:
    assert length_of_longest_substring(s) == want, s
    assert length_of_longest_substring_brute(s) == want, s

rng = random.Random(7)
for _ in range(2000):
    s = "".join(rng.choice("abcd") for _ in range(rng.randint(0, 12)))
    assert length_of_longest_substring(s) == length_of_longest_substring_brute(s), s

print("python: all tests passed")
