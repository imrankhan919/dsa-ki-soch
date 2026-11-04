// Longest Repeating Character Replacement (DSA ki SOCH, Ep 10). LeetCode 424:
// https://leetcode.com/problems/longest-repeating-character-replacement/
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;

// H: variable Sliding Window. badlaav = len - maxf; k se zyada ho to left se nikalo. Time O(n).
int characterReplacement(const string& s, int k) {
    array<int, 26> count{};
    int l = 0, best = 0, maxf = 0;
    for (int r = 0; r < (int)s.size(); r++) {
        maxf = max(maxf, ++count[s[r] - 'A']);
        while ((r - l + 1) - maxf > k) count[s[l++] - 'A']--;
        best = max(best, r - l + 1);
    }
    return best;
}

int main() {
    assert(characterReplacement("AABABBA", 1) == 4);
    assert(characterReplacement("ABBCB", 1) == 4);
    assert(characterReplacement("ABAB", 2) == 4);
    assert(characterReplacement("AAAA", 0) == 4);
    assert(characterReplacement("ABCDE", 1) == 2);
    assert(characterReplacement("", 2) == 0);
    cout << "c++: all tests passed" << endl;
    return 0;
}
