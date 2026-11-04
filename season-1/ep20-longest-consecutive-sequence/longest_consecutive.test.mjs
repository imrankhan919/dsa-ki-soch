import assert from 'node:assert/strict';
import {longestConsecutive} from './longest_consecutive.js';

const cases = [
  [[100, 4, 200, 1, 3, 2], 4],
  [[5, 6, 1, 7, 2], 3],
  [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
  [[], 0],
  [[1, 2, 0, 1], 3],
];
for (const [nums, want] of cases) assert.equal(longestConsecutive(nums), want, String(nums));
console.log('javascript: all tests passed');
