// Contains Duplicate (DSA ki SOCH, Ep 17). LeetCode 217:
// https://leetcode.com/problems/contains-duplicate/
#include <cassert>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

// H: hash set answers "pehle dekha?" in O(1). Time O(n), space O(n).
bool containsDuplicate(const vector<int>& nums) {
    unordered_set<int> seen;
    for (int x : nums) {
        if (seen.count(x)) return true;
        seen.insert(x);
    }
    return false;
}

int main() {
    assert(containsDuplicate({3, 1, 4, 1, 5}));
    assert(containsDuplicate({5, 2, 8, 2, 9}));
    assert(containsDuplicate({1, 2, 3, 1}));
    assert(!containsDuplicate({1, 2, 3, 4}));
    assert(!containsDuplicate({7}));
    cout << "c++: all tests passed" << endl;
    return 0;
}
