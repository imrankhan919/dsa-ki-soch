import assert from 'node:assert/strict';
import {moveZeroes, moveZeroesBrute} from './move_zeroes.js';

const cases = [
  [[0, 3, 0, 5, 8], [3, 5, 8, 0, 0]],
  [[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]],
  [[0], [0]],
  [[1, 2, 3], [1, 2, 3]],
  [[0, 0, 1], [1, 0, 0]],
  [[1, 2, 0, 3], [1, 2, 3, 0]],
];
for (const fn of [moveZeroesBrute, moveZeroes]) {
  for (const [nums, want] of cases) {
    const a = [...nums];
    fn(a);
    assert.deepEqual(a, want, `${fn.name}(${nums})`);
  }
}
console.log('javascript: all tests passed');
