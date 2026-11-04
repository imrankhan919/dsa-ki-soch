// Subarray Sum Equals K (DSA ki SOCH, Ep 14). LeetCode 560:
// https://leetcode.com/problems/subarray-sum-equals-k/
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

// H: prefix sum + hashmap of prefix counts. Time O(n), space O(n).
int subarraySum(const vector<int>& nums, int k) {
    unordered_map<int, int> count{{0, 1}};
    int prefix = 0, ans = 0;
    for (int x : nums) {
        prefix += x;
        auto it = count.find(prefix - k);
        if (it != count.end()) ans += it->second;
        count[prefix]++;
    }
    return ans;
}

int main() {
    assert(subarraySum({1, -1, 2, 1}, 2) == 3);
    assert(subarraySum({1, 2, 3}, 3) == 2);
    assert(subarraySum({1, 1, 1}, 2) == 2);
    assert(subarraySum({0, 0, 0}, 0) == 6);
    assert(subarraySum({-1, -1, 1}, 0) == 1);
    cout << "c++: all tests passed" << endl;
    return 0;
}
