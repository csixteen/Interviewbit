#!/usr/bin/env python3
# coding: utf-8
from functools import reduce
import unittest


class Solution:
    def colorful(self, A):
        l = len(A)
        parts = [list(map(int, A[i:j+1])) for i in range(l + 1) for j in range(i, l)]
        prods = set()
        for part in parts:
            prod = reduce(int.__mul__, part, 1)
            if prod in prods:
                return 0
            prods.add(prod)

        return 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ('23', 1),
            ('33', 0),
            ('3245', 1)
        ]

    def test_colorful(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.colorful(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

