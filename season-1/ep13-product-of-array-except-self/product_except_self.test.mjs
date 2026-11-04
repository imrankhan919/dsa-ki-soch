import assert from 'node:assert/strict';
import {productExceptSelf} from './product_except_self.js';

const cases = [
  [[1, 2, 3, 4], [24, 12, 8, 6]],
  [[2, 3, 0, 4], [0, 0, 24, 0]],
  [[-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]],
  [[0, 0], [0, 0]],
  [[5, 2], [2, 5]],
];
for (const [nums, want] of cases) assert.deepEqual(productExceptSelf(nums), want, String(nums));
console.log('javascript: all tests passed');
