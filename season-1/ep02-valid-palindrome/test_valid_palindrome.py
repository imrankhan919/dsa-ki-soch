import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from valid_palindrome import is_palindrome, is_palindrome_reverse  # noqa: E402

CASES = [
    ("Race car!", True),  # the episode's example
    ("race a car", False),  # the comment question (caught at 'e' vs 'a')
    ("A man, a plan, a canal: Panama", True),
    (" ", True),  # empty after cleaning
    ("0P", False),  # digits count
    ("No lemon, no melon", True),
    ("ab_a", True),  # underscore is not a letter
]
for fn in (is_palindrome_reverse, is_palindrome):
    for s, want in CASES:
        assert fn(s) == want, f"{fn.__name__}({s!r}) = {fn(s)}, want {want}"

# random cross-check
rng = random.Random(5)
alphabet = "aAbB1 ,!:"
for _ in range(5000):
    s = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 10)))
    if rng.random() < 0.5:  # make some real palindromes
        s = s + s[::-1]
    assert is_palindrome(s) == is_palindrome_reverse(s), s

print("python: all tests passed")
