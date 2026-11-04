// Longest Consecutive Sequence (DSA ki SOCH, Ep 20). LeetCode 128:
// https://leetcode.com/problems/longest-consecutive-sequence/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

// H: only start counting where x - 1 is missing. Time O(n), space O(n).
int longestConsecutive(const vector<int>& nums) {
    unordered_set<int> s(nums.begin(), nums.end());
    int best = 0;
    for (int x : s) {
        if (s.count(x - 1)) continue;
        int y = x;
        while (s.count(y + 1)) y++;
        best = max(best, y - x + 1);
    }
    return best;
}

int main() {
    assert(longestConsecutive({100, 4, 200, 1, 3, 2}) == 4);
    assert(longestConsecutive({5, 6, 1, 7, 2}) == 3);
    assert(longestConsecutive({0, 3, 7, 2, 5, 8, 4, 6, 0, 1}) == 9);
    assert(longestConsecutive({}) == 0);
    cout << "c++: all tests passed" << endl;
    return 0;
}
