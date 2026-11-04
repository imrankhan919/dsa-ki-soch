import assert from 'node:assert/strict';
import {isPalindrome, isPalindromeReverse} from './valid_palindrome.js';

const cases = [
  ['Race car!', true],
  ['race a car', false],
  ['A man, a plan, a canal: Panama', true],
  [' ', true],
  ['0P', false],
  ['No lemon, no melon', true],
  ['ab_a', true],
];
for (const fn of [isPalindromeReverse, isPalindrome]) {
  for (const [s, want] of cases) assert.equal(fn(s), want, `${fn.name}(${JSON.stringify(s)})`);
}
console.log('javascript: all tests passed');
