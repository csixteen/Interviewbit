#!/usr/bin/env python3
# coding: utf-8
from itertools import chain, groupby
import unittest


class Solution:
    @staticmethod
    def countAndSay(A):
        ret = [1]
        for _ in range(2, A+1):
            ret = list(chain.from_iterable([[len(x), x[0]] for x in [list(g) for _, g in groupby(ret)]]))

        return ''.join(map(str, ret))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (1, '1'),
            (2, '11'),
            (3, '21'),
            (4, '1211'),
            (5, '111221'),
            (6, '312211')
        ]

    def test_countAndSay(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.countAndSay(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

