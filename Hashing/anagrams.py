#!/usr/bin/env python3
# coding: utf-8
from collections import defaultdict
import unittest


class Solution:
    @staticmethod
    def anagrams(A):
        def string_hash(s):
            _sum, _prod = 0, 1
            for c in s:
                _sum += ord(c)
                _prod *= ord(c)

            return ((_sum % 1000000007) + (_prod % 1000000007)) % 1000000007

        d = defaultdict(list)
        for i, v in enumerate(A, 1):
            d[string_hash(v)].append(i)

        return [v for _, v in d.items()]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (['cat', 'dog', 'god', 'tca'], [[1, 4], [2, 3]])
        ]

    def test_anagrams(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.anagrams(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

