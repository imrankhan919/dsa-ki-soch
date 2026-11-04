import assert from 'node:assert/strict';
import {isAnagram} from './valid_anagram.js';

const cases = [
  ['race', 'care', true],
  ['rat', 'car', false],
  ['anagram', 'nagaram', true],
  ['a', 'ab', false],
  ['aacc', 'ccac', false],
];
for (const [s, t, want] of cases) assert.equal(isAnagram(s, t), want, `${s} ${t}`);
console.log('javascript: all tests passed');
