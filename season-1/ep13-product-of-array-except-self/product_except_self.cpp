// Product of Array Except Self (DSA ki SOCH, Ep 13). LeetCode 238:
// https://leetcode.com/problems/product-of-array-except-self/
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// H: left pass + right pass, no division. Time O(n).
vector<int> productExceptSelf(const vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, 1);
    int left = 1;
    for (int i = 0; i < n; i++) {
        ans[i] = left;
        left *= nums[i];
    }
    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
        ans[i] *= right;
        right *= nums[i];
    }
    return ans;
}

int main() {
    assert((productExceptSelf({1, 2, 3, 4}) == vector<int>{24, 12, 8, 6}));
    assert((productExceptSelf({2, 3, 0, 4}) == vector<int>{0, 0, 24, 0}));
    assert((productExceptSelf({-1, 1, 0, -3, 3}) == vector<int>{0, 0, 9, 0, 0}));
    assert((productExceptSelf({5, 2}) == vector<int>{2, 5}));
    cout << "c++: all tests passed" << endl;
    return 0;
}
