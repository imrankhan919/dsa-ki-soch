// Search Insert Position (DSA ki SOCH, Ep 23). LeetCode 35:
// https://leetcode.com/problems/search-insert-position/
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// H: plain binary search; when l > r, l is the insert slot. Time O(log n), space O(1).
int searchInsert(const vector<int>& nums, int target) {
    int l = 0, r = (int)nums.size() - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;  // avoids overflow for big l + r
        if (nums[m] == target) return m;
        if (nums[m] < target) l = m + 1;
        else r = m - 1;
    }
    return l;
}

int main() {
    vector<int> nums{1, 3, 5, 7, 9, 11, 13, 15};
    assert(searchInsert(nums, 4) == 2);
    assert(searchInsert(nums, 16) == 8);
    assert(searchInsert(nums, 13) == 6);
    assert(searchInsert(nums, 0) == 0);
    assert(searchInsert({1, 3, 5, 6}, 5) == 2);
    assert(searchInsert({1, 3, 5, 6}, 2) == 1);
    assert(searchInsert({1, 3, 5, 6}, 7) == 4);
    cout << "c++: all tests passed" << endl;
    return 0;
}
