import assert from 'node:assert/strict';
import {findMin} from './find_min.js';

const cases = [
  [[4, 5, 6, 7, 0, 1, 2], 0],
  [[3, 4, 5, 1, 2], 1],
  [[11, 13, 15, 17], 11],
  [[2, 1], 1],
  [[1], 1],
];
for (const [nums, want] of cases) assert.equal(findMin(nums), want, `${nums}`);
console.log('javascript: all tests passed');
