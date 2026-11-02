import assert from 'node:assert/strict';
import {twoSum, twoSumBrute, twoSumSorted} from './two_sum.js';

const cases = [
  [[5, 9, 2, 13, 7, 6], 13, [4, 5]],
  [[3, 4, 2], 6, [1, 2]],
  [[3, 3], 6, [0, 1]],
  [[4, 1, 7], 8, [1, 2]],
  [[-3, 4, 0, 3], 0, [0, 3]],
  [[0, 5, 0], 0, [0, 2]],
];
for (const fn of [twoSumBrute, twoSumSorted, twoSum]) {
  for (const [nums, target, want] of cases) {
    assert.deepEqual([...fn(nums, target)].sort((a, b) => a - b), want, `${fn.name}(${nums}, ${target})`);
  }
}
console.log('javascript: all tests passed');
