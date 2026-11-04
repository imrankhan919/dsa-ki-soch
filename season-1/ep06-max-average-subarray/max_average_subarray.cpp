// Maximum Average Subarray I (DSA ki SOCH, Ep 6). LeetCode 643:
// https://leetcode.com/problems/maximum-average-subarray-i/
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

// H: Sliding Window. Har slide pe ek naya jodo, ek purana ghatao. Time O(n).
double findMaxAverage(const vector<int>& nums, int k) {
    long long s = 0;
    for (int i = 0; i < k; i++) s += nums[i];
    long long best = s;
    for (int i = k; i < (int)nums.size(); i++) {
        s += nums[i] - nums[i - k];
        best = max(best, s);
    }
    return (double)best / k;
}

int main() {
    auto near = [](double a, double b) { return fabs(a - b) < 1e-9; };
    assert(near(findMaxAverage({2, 6, 1, 8, 3, 7}, 3), 6.0));
    assert(near(findMaxAverage({4, 2, 5, 1, 6}, 2), 3.5));
    assert(near(findMaxAverage({1, 12, -5, -6, 50, 3}, 4), 12.75));
    assert(near(findMaxAverage({5}, 1), 5.0));
    assert(near(findMaxAverage({-1, -2, -3}, 2), -1.5));
    cout << "c++: all tests passed" << endl;
    return 0;
}
