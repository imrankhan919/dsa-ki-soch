import assert from 'node:assert/strict';
import {groupAnagrams} from './group_anagrams.js';

const norm = (gs) => gs.map((g) => [...g].sort()).sort((a, b) => (a.join() < b.join() ? -1 : 1));
const cases = [
  [['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]],
  [['abc', 'bca', 'cab', 'xyz'], [['abc', 'bca', 'cab'], ['xyz']]],
  [[''], [['']]],
  [['a'], [['a']]],
];
for (const [words, want] of cases) assert.deepEqual(norm(groupAnagrams(words)), norm(want), String(words));
console.log('javascript: all tests passed');
