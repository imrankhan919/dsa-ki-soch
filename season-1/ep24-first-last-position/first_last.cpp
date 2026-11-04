// First and Last Position (DSA ki SOCH, Ep 24). LeetCode 34:
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// H: binary search that keeps going after a match. Time O(log n), space O(1).
int search(const vector<int>& nums, int target, bool first) {
    int l = 0, r = (int)nums.size() - 1, ans = -1;
    while (l <= r) {
        int m = l + (r - l) / 2;  // avoids overflow for big l + r
        if (nums[m] == target) {
            ans = m;
            if (first) r = m - 1;
            else l = m + 1;
        } else if (nums[m] < target) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    return ans;
}

vector<int> searchRange(const vector<int>& nums, int target) {
    return {search(nums, target, true), search(nums, target, false)};
}

int main() {
    vector<int> nums{5, 7, 7, 8, 8, 10};
    assert((searchRange(nums, 8) == vector<int>{3, 4}));
    assert((searchRange(nums, 7) == vector<int>{1, 2}));
    assert((searchRange(nums, 6) == vector<int>{-1, -1}));
    assert((searchRange({}, 0) == vector<int>{-1, -1}));
    assert((searchRange({2, 2, 2, 2}, 2) == vector<int>{0, 3}));
    cout << "c++: all tests passed" << endl;
    return 0;
}
