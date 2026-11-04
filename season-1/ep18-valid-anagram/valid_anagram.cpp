// Valid Anagram (DSA ki SOCH, Ep 18). LeetCode 242:
// https://leetcode.com/problems/valid-anagram/
#include <array>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;

// H: +1 for s, -1 for t, all zero at the end. Time O(n), space O(1) (26 letters).
bool isAnagram(const string& s, const string& t) {
    if (s.size() != t.size()) return false;
    array<int, 26> count{};
    for (char ch : s) count[ch - 'a']++;
    for (char ch : t) count[ch - 'a']--;
    for (int v : count)
        if (v != 0) return false;
    return true;
}

int main() {
    assert(isAnagram("race", "care"));
    assert(!isAnagram("rat", "car"));
    assert(isAnagram("anagram", "nagaram"));
    assert(!isAnagram("a", "ab"));
    assert(!isAnagram("aacc", "ccac"));
    cout << "c++: all tests passed" << endl;
    return 0;
}
