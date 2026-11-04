import assert from 'node:assert/strict';
import {lengthOfLongestSubstring} from './longest_substring.js';

const cases = [
  ['pwwkew', 3],
  ['dvdf', 3],
  ['abcabcbb', 3],
  ['bbbbb', 1],
  ['', 0],
  [' ', 1],
  ['abba', 2],
];
for (const [s, want] of cases) assert.equal(lengthOfLongestSubstring(s), want, s);
console.log('javascript: all tests passed');
