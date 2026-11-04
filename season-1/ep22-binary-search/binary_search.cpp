// Binary Search (DSA ki SOCH, Ep 22). LeetCode 704:
// https://leetcode.com/problems/binary-search/
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// H: look at the middle, throw away half. Time O(log n), space O(1).
int search(const vector<int>& nums, int target) {
    int l = 0, r = (int)nums.size() - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;  // avoids overflow for big l + r
        if (nums[m] == target) return m;
        if (nums[m] < target) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

int main() {
    vector<int> nums{1, 3, 5, 7, 9, 11, 13, 15};
    assert(search(nums, 13) == 6);
    assert(search(nums, 4) == -1);
    assert(search({-1, 0, 3, 5, 9, 12}, 9) == 4);
    assert(search({-1, 0, 3, 5, 9, 12}, 2) == -1);
    cout << "c++: all tests passed" << endl;
    return 0;
}
