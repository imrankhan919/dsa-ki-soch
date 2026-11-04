// Group Anagrams (DSA ki SOCH, Ep 19). LeetCode 49:
// https://leetcode.com/problems/group-anagrams/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// H: sorted letters are the key; anagrams share it. Time O(n * k log k).
vector<vector<string>> groupAnagrams(const vector<string>& words) {
    unordered_map<string, vector<string>> groups;
    vector<string> order;
    for (const string& w : words) {
        string key = w;
        sort(key.begin(), key.end());
        if (!groups.count(key)) order.push_back(key);
        groups[key].push_back(w);
    }
    vector<vector<string>> out;
    for (const string& k : order) out.push_back(groups[k]);
    return out;
}

int main() {
    auto g = groupAnagrams({"eat", "tea", "tan", "ate", "nat", "bat"});
    assert(g.size() == 3);
    assert((g[0] == vector<string>{"eat", "tea", "ate"}));
    assert((g[1] == vector<string>{"tan", "nat"}));
    assert((g[2] == vector<string>{"bat"}));
    assert(groupAnagrams({"abc", "bca", "cab", "xyz"}).size() == 2);
    cout << "c++: all tests passed" << endl;
    return 0;
}
