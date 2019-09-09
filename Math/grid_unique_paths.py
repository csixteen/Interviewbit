#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def uniquePaths(A, B):
        def fact(N):
            res = 1
            while N > 0:
                res *= N
                N -= 1
            return res

        return fact(A + B - 2) // (fact(B - 1)*fact(A - 1))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ((100, 1), 1),
            ((2, 2), 2),
            ((15, 9), 319770)
        ]

    def test_uniquePaths(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.uniquePaths(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

