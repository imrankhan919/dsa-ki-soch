// Two Sum II, sorted input (DSA ki SOCH, Ep 1). LeetCode 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Return: positions, 1 se ginti (index + 1). Extra memory: O(1).
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// O: har pair check. Time O(n^2), extra space O(1).
vector<int> twoSumBrute(const vector<int>& numbers, int target) {
    int n = numbers.size();
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (numbers[i] + numbers[j] == target) return {i + 1, j + 1};
    return {};
}

// H: Two Pointers. Sum bada -> r peeche, chhota -> l aage. Time O(n), extra space O(1).
vector<int> twoSum(const vector<int>& numbers, int target) {
    int l = 0, r = (int)numbers.size() - 1;
    while (l < r) {
        int total = numbers[l] + numbers[r];
        if (total == target) return {l + 1, r + 1};
        if (total < target) l++;
        else r--;
    }
    return {};
}

int main() {
    struct Case { vector<int> nums; int target; vector<int> want; };
    vector<Case> cases = {
        {{2, 5, 6, 7, 9, 13}, 13, {3, 4}},
        {{2, 7, 11, 15}, 9, {1, 2}},
        {{2, 3, 4}, 6, {1, 3}},
        {{-1, 0}, -1, {1, 2}},
        {{1, 3, 4, 6, 8}, 10, {3, 4}},
        {{3, 3}, 6, {1, 2}},
    };
    for (auto& c : cases) {
        assert(twoSumBrute(c.nums, c.target) == c.want);
        assert(twoSum(c.nums, c.target) == c.want);
    }
    cout << "c++: all tests passed" << endl;
    return 0;
}
