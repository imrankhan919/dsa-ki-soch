import assert from 'node:assert/strict';
import {pivotIndex} from './pivot_index.js';

const cases = [
  [[1, 7, 3, 6, 5, 6], 3],
  [[2, 1, -1], 0],
  [[1, 2, 3], -1],
  [[0], 0],
  [[-1, -1, 0, 1, 1, 0], 5],
];
for (const [nums, want] of cases) assert.equal(pivotIndex(nums), want, String(nums));
console.log('javascript: all tests passed');
