#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def trailingZeros(A):
        exp = 1
        res = 0
        while True:
            v = A // (5**exp)
            if v < 1:
                break
            res += v
            exp += 1

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_trailingZeros(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.trailingZeros(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

