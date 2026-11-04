import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from group_anagrams import group_anagrams, group_anagrams_brute  # noqa: E402


def norm(groups):
    return sorted(sorted(g) for g in groups)


CASES = [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]),  # episode + LeetCode
    (["abc", "bca", "cab", "xyz"], [["abc", "bca", "cab"], ["xyz"]]),  # the comment question: 2 groups
    ([""], [[""]]),
    (["a"], [["a"]]),
]
for words, want in CASES:
    assert norm(group_anagrams(words)) == norm(want), words
    assert norm(group_anagrams_brute(words)) == norm(want), words

rng = random.Random(19)
for _ in range(1000):
    words = ["".join(rng.choice("abc") for _ in range(rng.randint(0, 3))) for _ in range(rng.randint(1, 8))]
    assert norm(group_anagrams(words)) == norm(group_anagrams_brute(words)), words

print("python: all tests passed")
