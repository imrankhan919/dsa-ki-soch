import assert from 'node:assert/strict';
import {search} from './binary_search.js';

const NUMS = [1, 3, 5, 7, 9, 11, 13, 15];
const cases = [
  [NUMS, 13, 6],
  [NUMS, 4, -1],
  [[-1, 0, 3, 5, 9, 12], 9, 4],
  [[-1, 0, 3, 5, 9, 12], 2, -1],
  [[5], 5, 0],
];
for (const [nums, target, want] of cases) assert.equal(search(nums, target), want, `${nums} t=${target}`);
console.log('javascript: all tests passed');
