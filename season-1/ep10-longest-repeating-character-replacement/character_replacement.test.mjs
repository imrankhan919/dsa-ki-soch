import assert from 'node:assert/strict';
import {characterReplacement} from './character_replacement.js';

const cases = [
  ['AABABBA', 1, 4],
  ['ABBCB', 1, 4],
  ['ABAB', 2, 4],
  ['AAAA', 0, 4],
  ['ABCDE', 1, 2],
  ['', 2, 0],
];
for (const [s, k, want] of cases) assert.equal(characterReplacement(s, k), want, `${s} ${k}`);
console.log('javascript: all tests passed');
