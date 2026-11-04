// Longest Substring Without Repeating Characters (DSA ki SOCH, Ep 7). LeetCode 3:
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

// H: variable Sliding Window + set. Right badhao, repeat aaye to left ghatao. Time O(n).
int lengthOfLongestSubstring(const string& s) {
    unordered_set<char> seen;
    int l = 0, best = 0;
    for (int r = 0; r < (int)s.size(); r++) {
        while (seen.count(s[r])) seen.erase(s[l++]);
        seen.insert(s[r]);
        best = max(best, r - l + 1);
    }
    return best;
}

int main() {
    assert(lengthOfLongestSubstring("pwwkew") == 3);
    assert(lengthOfLongestSubstring("dvdf") == 3);
    assert(lengthOfLongestSubstring("abcabcbb") == 3);
    assert(lengthOfLongestSubstring("bbbbb") == 1);
    assert(lengthOfLongestSubstring("") == 0);
    assert(lengthOfLongestSubstring("abba") == 2);
    cout << "c++: all tests passed" << endl;
    return 0;
}
