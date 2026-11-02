"""Two Sum II, sorted input (DSA ki SOCH, Ep 1). LeetCode 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

numbers sorted hai (chhote se bade). Do numbers dhoondho jinka sum = target.
Return: positions, 1 se ginti (index + 1). Extra memory: O(1).
"""


def two_sum_brute(numbers, target):
    """O: har pair check. Time O(n^2), extra space O(1)."""
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []


def two_sum(numbers, target):
    """H: Two Pointers. Sum bada -> r peeche, chhota -> l aage. Time O(n), extra space O(1)."""
    l, r = 0, len(numbers) - 1
    while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
            return [l + 1, r + 1]
        elif total < target:
            l += 1
        else:
            r -= 1
    return []


if __name__ == "__main__":
    print(two_sum([2, 5, 6, 7, 9, 13], 13))  # [3, 4]
