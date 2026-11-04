// Minimum Size Subarray Sum (DSA ki SOCH, Ep 8). LeetCode 209:
// https://leetcode.com/problems/minimum-size-subarray-sum/
#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

// H: variable Sliding Window. Sum kam? r badhao. Pura? length note karo, l se kaato. Time O(n).
int minSubArrayLen(int target, const vector<int>& nums) {
    int l = 0, best = INT_MAX;
    long long s = 0;
    for (int r = 0; r < (int)nums.size(); r++) {
        s += nums[r];
        while (s >= target) {
            best = min(best, r - l + 1);
            s -= nums[l++];
        }
    }
    return best == INT_MAX ? 0 : best;
}

int main() {
    assert(minSubArrayLen(7, {2, 3, 1, 2, 4, 3}) == 2);
    assert(minSubArrayLen(11, {1, 2, 3, 4, 5}) == 3);
    assert(minSubArrayLen(4, {1, 4, 4}) == 1);
    assert(minSubArrayLen(11, {1, 1, 1, 1, 1, 1, 1, 1}) == 0);
    assert(minSubArrayLen(15, {1, 2, 3, 4, 5}) == 5);
    cout << "c++: all tests passed" << endl;
    return 0;
}
