import assert from 'node:assert/strict';
import {findMaxAverage} from './max_average_subarray.js';

const cases = [
  [[2, 6, 1, 8, 3, 7], 3, 6],
  [[4, 2, 5, 1, 6], 2, 3.5],
  [[1, 12, -5, -6, 50, 3], 4, 12.75],
  [[5], 1, 5],
  [[-1, -2, -3], 2, -1.5],
];
for (const [nums, k, want] of cases) assert.ok(Math.abs(findMaxAverage(nums, k) - want) < 1e-9, String(nums));
console.log('javascript: all tests passed');
