import assert from 'node:assert/strict';
import {searchRange} from './first_last.js';

const NUMS = [5, 7, 7, 8, 8, 10];
const cases = [
  [NUMS, 8, [3, 4]],
  [NUMS, 7, [1, 2]],
  [NUMS, 6, [-1, -1]],
  [[], 0, [-1, -1]],
  [[2, 2, 2, 2], 2, [0, 3]],
];
for (const [nums, target, want] of cases) assert.deepEqual(searchRange(nums, target), want, `${nums} t=${target}`);
console.log('javascript: all tests passed');
