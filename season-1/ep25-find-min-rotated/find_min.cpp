// Find Minimum in Rotated Sorted Array (DSA ki SOCH, Ep 25). LeetCode 153:
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// H: compare the middle with the right end. Time O(log n), space O(1).
int findMin(const vector<int>& nums) {
    int l = 0, r = (int)nums.size() - 1;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (nums[m] > nums[r]) l = m + 1;
        else r = m;
    }
    return nums[l];
}

int main() {
    assert(findMin({4, 5, 6, 7, 0, 1, 2}) == 0);
    assert(findMin({3, 4, 5, 1, 2}) == 1);
    assert(findMin({11, 13, 15, 17}) == 11);
    assert(findMin({2, 1}) == 1);
    assert(findMin({1}) == 1);
    cout << "c++: all tests passed" << endl;
    return 0;
}
