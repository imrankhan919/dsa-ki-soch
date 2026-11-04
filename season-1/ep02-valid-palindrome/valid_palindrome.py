"""Valid Palindrome (DSA ki SOCH, Ep 2). LeetCode 125: https://leetcode.com/problems/valid-palindrome/

Sirf letters aur numbers count hote hain, capital = small. Aage se = peeche se? True / False.
"""


def is_palindrome_reverse(s):
    """O: clean copy + ulti copy, phir compare. Time O(n), extra space O(n)."""
    t = "".join(c.lower() for c in s if c.isalnum())
    return t == t[::-1]


def is_palindrome(s):
    """H: Two Pointers, copy nahi. Time O(n), extra space O(1)."""
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("Race car!"))  # True
    print(is_palindrome("race a car"))  # False
