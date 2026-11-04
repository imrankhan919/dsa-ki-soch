// Top K Frequent Elements (DSA ki SOCH, Ep 21). LeetCode 347:
// https://leetcode.com/problems/top-k-frequent-elements/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

// H: count, then bucket[f] = numbers seen f times, walk buckets from the top. Time O(n).
vector<int> topKFrequent(const vector<int>& nums, int k) {
    unordered_map<int, int> count;
    for (int x : nums) count[x]++;
    vector<vector<int>> buckets(nums.size() + 1);
    for (auto& [x, f] : count) buckets[f].push_back(x);
    vector<int> ans;
    for (int f = nums.size(); f > 0; f--)
        for (int x : buckets[f]) {
            ans.push_back(x);
            if ((int)ans.size() == k) return ans;
        }
    return ans;
}

int main() {
    auto a = topKFrequent({1, 1, 1, 2, 2, 3}, 2);
    sort(a.begin(), a.end());
    assert((a == vector<int>{1, 2}));
    auto b = topKFrequent({4, 4, 5, 5, 5, 6}, 2);
    sort(b.begin(), b.end());
    assert((b == vector<int>{4, 5}));
    assert((topKFrequent({1}, 1) == vector<int>{1}));
    cout << "c++: all tests passed" << endl;
    return 0;
}
