import assert from 'node:assert/strict';
import {findMaxLength} from './contiguous_array.js';

const cases = [
  [[1, 0, 1, 1, 1, 0, 0], 6],
  [[0, 0, 1, 0, 1], 4],
  [[0, 1], 2],
  [[0, 1, 0], 2],
  [[1, 1, 1], 0],
  [[0], 0],
];
for (const [nums, want] of cases) assert.equal(findMaxLength(nums), want, String(nums));
console.log('javascript: all tests passed');
