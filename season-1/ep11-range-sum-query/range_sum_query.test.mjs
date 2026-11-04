import assert from 'node:assert/strict';
import {NumArray} from './range_sum_query.js';

const a = new NumArray([3, 1, 4, 1, 5, 9]);
assert.deepEqual(a.prefix, [0, 3, 4, 8, 9, 14, 23]);
assert.equal(a.sumRange(1, 4), 11);
assert.equal(a.sumRange(2, 5), 19);
assert.equal(new NumArray([2, 7, 1, 8, 2, 8]).sumRange(1, 3), 16);
const lc = new NumArray([-2, 0, 3, -5, 2, -1]);
assert.deepEqual([lc.sumRange(0, 2), lc.sumRange(2, 5), lc.sumRange(0, 5)], [1, -1, -3]);
console.log('javascript: all tests passed');
