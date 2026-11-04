import assert from 'node:assert/strict';
import {minSubArrayLen} from './min_subarray_len.js';

const cases = [
  [7, [2, 3, 1, 2, 4, 3], 2],
  [11, [1, 2, 3, 4, 5], 3],
  [4, [1, 4, 4], 1],
  [11, [1, 1, 1, 1, 1, 1, 1, 1], 0],
  [15, [1, 2, 3, 4, 5], 5],
];
for (const [target, nums, want] of cases) assert.equal(minSubArrayLen(target, nums), want, String(nums));
console.log('javascript: all tests passed');
