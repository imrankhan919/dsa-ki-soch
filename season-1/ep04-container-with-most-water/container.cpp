// Container With Most Water (DSA ki SOCH, Ep 4). LeetCode 11: https://leetcode.com/problems/container-with-most-water/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// O: har pair. Time O(n^2), extra space O(1).
int maxAreaBrute(const vector<int>& h) {
    int best = 0;
    for (int i = 0; i < (int)h.size(); i++)
        for (int j = i + 1; j < (int)h.size(); j++) best = max(best, min(h[i], h[j]) * (j - i));
    return best;
}

// H: Two Pointers, chhoti deewar andar. Time O(n), extra space O(1).
int maxArea(const vector<int>& h) {
    int l = 0, r = (int)h.size() - 1, best = 0;
    while (l < r) {
        best = max(best, min(h[l], h[r]) * (r - l));
        if (h[l] < h[r]) l++;
        else r--;
    }
    return best;
}

int main() {
    vector<pair<vector<int>, int>> cases = {{{3, 7, 2, 5, 4, 8, 3}, 28}, {{1, 8, 6, 2, 5, 4, 8, 3, 7}, 49}, {{1, 1}, 1}, {{4, 6, 3, 7, 8}, 18}};
    for (auto& [h, want] : cases) {
        assert(maxAreaBrute(h) == want);
        assert(maxArea(h) == want);
    }
    cout << "c++: all tests passed" << endl;
    return 0;
}
