// Contiguous Array (DSA ki SOCH, Ep 15). LeetCode 525:
// https://leetcode.com/problems/contiguous-array/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

// H: 0 -> -1, prefix sum, keep the FIRST index of every prefix. Time O(n), space O(n).
int findMaxLength(const vector<int>& nums) {
    unordered_map<int, int> first{{0, -1}};
    int prefix = 0, best = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        prefix += nums[i] == 1 ? 1 : -1;
        auto it = first.find(prefix);
        if (it != first.end()) best = max(best, i - it->second);
        else first[prefix] = i;
    }
    return best;
}

int main() {
    assert(findMaxLength({1, 0, 1, 1, 1, 0, 0}) == 6);
    assert(findMaxLength({0, 0, 1, 0, 1}) == 4);
    assert(findMaxLength({0, 1}) == 2);
    assert(findMaxLength({0, 1, 0}) == 2);
    assert(findMaxLength({1, 1, 1}) == 0);
    cout << "c++: all tests passed" << endl;
    return 0;
}
