import assert from 'node:assert/strict';
import {twoSum, twoSumBrute} from './two_sum_ii.js';

const cases = [
  [[2, 5, 6, 7, 9, 13], 13, [3, 4]],
  [[2, 7, 11, 15], 9, [1, 2]],
  [[2, 3, 4], 6, [1, 3]],
  [[-1, 0], -1, [1, 2]],
  [[1, 3, 4, 6, 8], 10, [3, 4]],
  [[3, 3], 6, [1, 2]],
];
for (const fn of [twoSumBrute, twoSum]) {
  for (const [nums, target, want] of cases) {
    assert.deepEqual(fn(nums, target), want, `${fn.name}(${nums}, ${target})`);
  }
}
console.log('javascript: all tests passed');
