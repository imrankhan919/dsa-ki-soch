import assert from 'node:assert/strict';
import {subarraySum} from './subarray_sum.js';

const cases = [
  [[1, -1, 2, 1], 2, 3],
  [[1, 2, 3], 3, 2],
  [[1, 1, 1], 2, 2],
  [[0, 0, 0], 0, 6],
  [[5], 5, 1],
  [[-1, -1, 1], 0, 1],
];
for (const [nums, k, want] of cases) assert.equal(subarraySum(nums, k), want, `${nums} k=${k}`);
console.log('javascript: all tests passed');
