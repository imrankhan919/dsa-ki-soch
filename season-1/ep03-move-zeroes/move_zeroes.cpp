// Move Zeroes (DSA ki SOCH, Ep 3). LeetCode 283: https://leetcode.com/problems/move-zeroes/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// O: zero nikalo, end mein daalo. Time O(n^2), extra space O(1).
void moveZeroesBrute(vector<int>& nums) {
    int zeros = count(nums.begin(), nums.end(), 0);
    while (zeros-- > 0) {
        nums.erase(find(nums.begin(), nums.end(), 0));
        nums.push_back(0);
    }
}

// H: Two Pointers, ek hi direction. Time O(n), extra space O(1).
void moveZeroes(vector<int>& nums) {
    int w = 0;
    for (int r = 0; r < (int)nums.size(); r++) {
        if (nums[r] != 0) {
            swap(nums[w], nums[r]);
            w++;
        }
    }
}

int main() {
    vector<pair<vector<int>, vector<int>>> cases = {
        {{0, 3, 0, 5, 8}, {3, 5, 8, 0, 0}}, {{0, 1, 0, 3, 12}, {1, 3, 12, 0, 0}}, {{0}, {0}},
        {{1, 2, 3}, {1, 2, 3}}, {{0, 0, 1}, {1, 0, 0}}, {{1, 2, 0, 3}, {1, 2, 3, 0}},
    };
    for (auto& [nums, want] : cases) {
        auto a = nums, b = nums;
        moveZeroesBrute(a);
        moveZeroes(b);
        assert(a == want && b == want);
    }
    cout << "c++: all tests passed" << endl;
    return 0;
}
