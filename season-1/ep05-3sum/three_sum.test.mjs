import assert from 'node:assert/strict';
import {threeSum} from './three_sum.js';

const norm = (g) => g.map((x) => x.join(',')).sort();
const cases = [
  [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
  [[-2, 0, 0, 2, 2], [[-2, 0, 2]]],
  [[0, 0, 0, 0], [[0, 0, 0]]],
  [[0, 1, 1], []],
];
for (const [nums, want] of cases) assert.deepEqual(norm(threeSum(nums)), norm(want), String(nums));
console.log('javascript: all tests passed');
