#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def power(x, n, d):
        res = 1 % d  # Cover case d == 1
        while n > 0:
            if n & 1:   # Odd?
               res = (res * x) % d
            x = x**2 % d
            n >>= 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_power(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.power(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

