// Find Pivot Index (DSA ki SOCH, Ep 12). LeetCode 724:
// https://leetcode.com/problems/find-pivot-index/
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// H: total ek baar, left chalte chalte, right = total - left - x. Time O(n).
int pivotIndex(const vector<int>& nums) {
    long long total = accumulate(nums.begin(), nums.end(), 0LL), left = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (left == total - left - nums[i]) return i;
        left += nums[i];
    }
    return -1;
}

int main() {
    assert(pivotIndex({1, 7, 3, 6, 5, 6}) == 3);
    assert(pivotIndex({2, 1, -1}) == 0);
    assert(pivotIndex({1, 2, 3}) == -1);
    assert(pivotIndex({0}) == 0);
    assert(pivotIndex({-1, -1, 0, 1, 1, 0}) == 5);
    cout << "c++: all tests passed" << endl;
    return 0;
}
