// Range Sum Query - Immutable (DSA ki SOCH, Ep 11). LeetCode 303:
// https://leetcode.com/problems/range-sum-query-immutable/
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// H: Prefix Sum. Ek baar O(n) build, phir har query O(1): P[j+1] - P[i].
class NumArray {
    vector<long long> prefix{0};

public:
    explicit NumArray(const vector<int>& nums) {
        for (int x : nums) prefix.push_back(prefix.back() + x);
    }
    long long sumRange(int i, int j) const { return prefix[j + 1] - prefix[i]; }
};

int main() {
    NumArray a({3, 1, 4, 1, 5, 9});
    assert(a.sumRange(1, 4) == 11);
    assert(a.sumRange(2, 5) == 19);
    assert(NumArray({2, 7, 1, 8, 2, 8}).sumRange(1, 3) == 16);
    NumArray lc({-2, 0, 3, -5, 2, -1});
    assert(lc.sumRange(0, 2) == 1 && lc.sumRange(2, 5) == -1 && lc.sumRange(0, 5) == -3);
    cout << "c++: all tests passed" << endl;
    return 0;
}
