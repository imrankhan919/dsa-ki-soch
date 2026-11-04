import assert from 'node:assert/strict';
import {checkInclusion} from './permutation_in_string.js';

const cases = [
  ['ab', 'eidbaooo', true],
  ['ab', 'eidboaoo', false],
  ['adc', 'dcda', true],
  ['abc', 'ab', false],
  ['a', 'a', true],
  ['hello', 'ooolleoooleh', false],
];
for (const [s1, s2, want] of cases) assert.equal(checkInclusion(s1, s2), want, `${s1} ${s2}`);
console.log('javascript: all tests passed');
