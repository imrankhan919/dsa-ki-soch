// Valid Palindrome (DSA ki SOCH, Ep 2). LeetCode 125: https://leetcode.com/problems/valid-palindrome/
const isAlnum = (c) => /^[a-z0-9]$/i.test(c);

// O: clean copy + ulti copy. Time O(n), extra space O(n).
export function isPalindromeReverse(s) {
  const t = [...s].filter(isAlnum).join('').toLowerCase();
  return t === [...t].reverse().join('');
}

// H: Two Pointers, copy nahi. Time O(n), extra space O(1).
export function isPalindrome(s) {
  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    if (!isAlnum(s[l])) l++;
    else if (!isAlnum(s[r])) r--;
    else if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
    else {
      l++;
      r--;
    }
  }
  return true;
}
