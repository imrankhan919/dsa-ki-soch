// Subarray Sums Divisible by K (DSA ki SOCH, Ep 16). LeetCode 974:
// https://leetcode.com/problems/subarray-sums-divisible-by-k/
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// H: same prefix remainder -> the span between is divisible. Time O(n), space O(k).
int subarraysDivByK(const vector<int>& nums, int k) {
    vector<int> count(k, 0);
    count[0] = 1;
    int prefix = 0, ans = 0;
    for (int x : nums) {
        prefix = ((prefix + x) % k + k) % k;  // C++ % can be negative
        ans += count[prefix];
        count[prefix]++;
    }
    return ans;
}

int main() {
    assert(subarraysDivByK({2, 3, 1, 4}, 5) == 3);
    assert(subarraysDivByK({4, 2, 1}, 3) == 2);
    assert(subarraysDivByK({4, 5, 0, -2, -3, 1}, 5) == 7);
    assert(subarraysDivByK({5}, 9) == 0);
    assert(subarraysDivByK({-1, 2, 9}, 2) == 2);
    cout << "c++: all tests passed" << endl;
    return 0;
}
