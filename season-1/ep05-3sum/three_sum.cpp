// 3Sum (DSA ki SOCH, Ep 5). LeetCode 15: https://leetcode.com/problems/3sum/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

// H: sort + har i fix + baaki pe Two Pointers. Time O(n^2).
vector<vector<int>> threeSum(vector<int> nums) {
    sort(nums.begin(), nums.end());
    set<vector<int>> res;
    int n = nums.size();
    for (int i = 0; i + 2 < n; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        int l = i + 1, r = n - 1;
        while (l < r) {
            int s = nums[i] + nums[l] + nums[r];
            if (s == 0) res.insert({nums[i], nums[l++], nums[r--]});
            else if (s < 0) l++;
            else r--;
        }
    }
    return vector<vector<int>>(res.begin(), res.end());
}

int main() {
    assert((threeSum({-1, 0, 1, 2, -1, -4}) == vector<vector<int>>{{-1, -1, 2}, {-1, 0, 1}}));
    assert((threeSum({-2, 0, 0, 2, 2}) == vector<vector<int>>{{-2, 0, 2}}));
    assert((threeSum({0, 0, 0, 0}) == vector<vector<int>>{{0, 0, 0}}));
    assert(threeSum({0, 1, 1}).empty());
    cout << "c++: all tests passed" << endl;
    return 0;
}
