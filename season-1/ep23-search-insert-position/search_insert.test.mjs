import assert from 'node:assert/strict';
import {searchInsert} from './search_insert.js';

const NUMS = [1, 3, 5, 7, 9, 11, 13, 15];
const cases = [
  [NUMS, 4, 2],
  [NUMS, 16, 8],
  [NUMS, 13, 6],
  [NUMS, 0, 0],
  [[1, 3, 5, 6], 5, 2],
  [[1, 3, 5, 6], 2, 1],
  [[1, 3, 5, 6], 7, 4],
];
for (const [nums, target, want] of cases) assert.equal(searchInsert(nums, target), want, `${nums} t=${target}`);
console.log('javascript: all tests passed');
