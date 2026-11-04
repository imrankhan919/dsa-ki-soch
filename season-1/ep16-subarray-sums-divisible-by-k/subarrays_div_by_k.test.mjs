import assert from 'node:assert/strict';
import {subarraysDivByK} from './subarrays_div_by_k.js';

const cases = [
  [[2, 3, 1, 4], 5, 3],
  [[4, 2, 1], 3, 2],
  [[4, 5, 0, -2, -3, 1], 5, 7],
  [[5], 9, 0],
  [[-1, 2, 9], 2, 2],
];
for (const [nums, k, want] of cases) assert.equal(subarraysDivByK(nums, k), want, `${nums} k=${k}`);
console.log('javascript: all tests passed');
