// Permutation in String (DSA ki SOCH, Ep 9). LeetCode 567:
// https://leetcode.com/problems/permutation-in-string/
#include <array>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;

// H: fixed Sliding Window + ginti (26 letters). Naya letter +1, purana -1. Time O(n).
bool checkInclusion(const string& s1, const string& s2) {
    int k = s1.size();
    if (k > (int)s2.size()) return false;
    array<int, 26> need{}, win{};
    for (int i = 0; i < k; i++) {
        need[s1[i] - 'a']++;
        win[s2[i] - 'a']++;
    }
    if (win == need) return true;
    for (int i = k; i < (int)s2.size(); i++) {
        win[s2[i] - 'a']++;
        win[s2[i - k] - 'a']--;
        if (win == need) return true;
    }
    return false;
}

int main() {
    assert(checkInclusion("ab", "eidbaooo"));
    assert(!checkInclusion("ab", "eidboaoo"));
    assert(checkInclusion("adc", "dcda"));
    assert(!checkInclusion("abc", "ab"));
    assert(checkInclusion("a", "a"));
    assert(!checkInclusion("hello", "ooolleoooleh"));
    cout << "c++: all tests passed" << endl;
    return 0;
}
