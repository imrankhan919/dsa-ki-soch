import assert from 'node:assert/strict';
import {maxArea, maxAreaBrute} from './container.js';

const cases = [
  [[3, 7, 2, 5, 4, 8, 3], 28],
  [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
  [[1, 1], 1],
  [[4, 6, 3, 7, 8], 18],
];
for (const fn of [maxAreaBrute, maxArea]) for (const [h, want] of cases) assert.equal(fn(h), want, `${fn.name}(${h})`);
console.log('javascript: all tests passed');
