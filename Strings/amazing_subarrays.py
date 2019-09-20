#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def solve(A):
        l = len(A)
        total = 0
        for i, c in enumerate(A):
            if c in 'aeiouAEIOU':
                total += l - i

        return total % 10003


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_solve(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.solve(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

