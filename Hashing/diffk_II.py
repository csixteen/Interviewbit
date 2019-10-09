#!/usr/bin/env python3
# coding: utf-8
from collections import defaultdict
import unittest


class Solution:
    @staticmethod
    def diffPossible2(A, B):
        d = defaultdict(set)
        for i, v in enumerate(A):
            if (B + v in d and len(d[B + v] - {i}) > 0) or \
                    (v - B in d and len(d[v - B] - {i}) > 0):
                return 1
            else:
                d[v].add(i)

        return 0

    @staticmethod
    def diffPossible(A, B):
        d = {}
        for x in A:
            if d.get(x - B, False) or d.get(x + B, False):
                return 1
            d[x] = True

        return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_diffPossible(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.diffPossible(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

