import assert from 'node:assert/strict';
import {topKFrequent} from './top_k_frequent.js';

const sortNum = (a) => [...a].sort((x, y) => x - y);
const cases = [
  [[1, 1, 1, 2, 2, 3], 2, [1, 2]],
  [[4, 4, 5, 5, 5, 6], 2, [4, 5]],
  [[1], 1, [1]],
];
for (const [nums, k, want] of cases) assert.deepEqual(sortNum(topKFrequent(nums, k)), sortNum(want), `${nums} k=${k}`);
console.log('javascript: all tests passed');
