// Two Sum — 3 tareeke se (DSA ki SOCH, Ep 0). LeetCode 1: https://leetcode.com/problems/two-sum/
// Build & test: g++ -std=c++17 -O2 two_sum.cpp -o two_sum && ./two_sum
#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

// O: har pair check. Time O(n^2), extra space O(1).
vector<int> twoSumBrute(const vector<int>& nums, int target) {
    int n = nums.size();
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (nums[i] + nums[j] == target) return {i, j};
    return {};
}

// H1: sort + two pointers, original index saath rakho. Time O(n log n), space O(n).
vector<int> twoSumSorted(const vector<int>& nums, int target) {
    vector<pair<int, int>> pairs;  // (value, original index)
    for (int i = 0; i < (int)nums.size(); i++) pairs.push_back({nums[i], i});
    sort(pairs.begin(), pairs.end());
    int left = 0, right = (int)pairs.size() - 1;
    while (left < right) {
        int s = pairs[left].first + pairs[right].first;
        if (s == target) {
            int a = pairs[left].second, b = pairs[right].second;
            return {min(a, b), max(a, b)};
        }
        if (s < target) left++;
        else right--;
    }
    return {};
}

// H2: hash map, one pass. Pehle check, phir daalo. Time O(n) average, space O(n).
vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> seen;  // number -> index
    for (int i = 0; i < (int)nums.size(); i++) {
        int need = target - nums[i];
        auto it = seen.find(need);
        if (it != seen.end()) return {it->second, i};
        seen[nums[i]] = i;
    }
    return {};
}

int main() {
    struct Case { vector<int> nums; int target; vector<int> want; };
    vector<Case> cases = {
        {{5, 9, 2, 13, 7, 6}, 13, {4, 5}},
        {{3, 4, 2}, 6, {1, 2}},
        {{3, 3}, 6, {0, 1}},
        {{4, 1, 7}, 8, {1, 2}},
        {{-3, 4, 0, 3}, 0, {0, 3}},
        {{0, 5, 0}, 0, {0, 2}},
    };
    for (auto& c : cases) {
        for (auto fn : {twoSumBrute, twoSumSorted, twoSum}) {
            auto got = fn(c.nums, c.target);
            sort(got.begin(), got.end());
            assert(got == c.want);
        }
    }
    cout << "c++: all tests passed" << endl;
}
