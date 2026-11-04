import assert from 'node:assert/strict';
import {containsDuplicate} from './contains_duplicate.js';

const cases = [
  [[3, 1, 4, 1, 5], true],
  [[5, 2, 8, 2, 9], true],
  [[1, 2, 3, 1], true],
  [[1, 2, 3, 4], false],
  [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], true],
  [[7], false],
];
for (const [nums, want] of cases) assert.equal(containsDuplicate(nums), want, String(nums));
console.log('javascript: all tests passed');
