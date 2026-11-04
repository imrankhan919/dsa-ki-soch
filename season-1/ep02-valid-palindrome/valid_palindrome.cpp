// Valid Palindrome (DSA ki SOCH, Ep 2). LeetCode 125: https://leetcode.com/problems/valid-palindrome/
#include <algorithm>
#include <cassert>
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

// O: clean copy + ulti copy. Time O(n), extra space O(n).
bool isPalindromeReverse(const string& s) {
    string t;
    for (char c : s)
        if (isalnum((unsigned char)c)) t += (char)tolower((unsigned char)c);
    string rev(t.rbegin(), t.rend());
    return t == rev;
}

// H: Two Pointers, copy nahi. Time O(n), extra space O(1).
bool isPalindrome(const string& s) {
    int l = 0, r = (int)s.size() - 1;
    while (l < r) {
        if (!isalnum((unsigned char)s[l])) l++;
        else if (!isalnum((unsigned char)s[r])) r--;
        else if (tolower((unsigned char)s[l]) != tolower((unsigned char)s[r])) return false;
        else { l++; r--; }
    }
    return true;
}

int main() {
    struct Case { string s; bool want; };
    Case cases[] = {
        {"Race car!", true}, {"race a car", false}, {"A man, a plan, a canal: Panama", true},
        {" ", true}, {"0P", false}, {"No lemon, no melon", true}, {"ab_a", true},
    };
    for (auto& c : cases) {
        assert(isPalindromeReverse(c.s) == c.want);
        assert(isPalindrome(c.s) == c.want);
    }
    cout << "c++: all tests passed" << endl;
    return 0;
}
