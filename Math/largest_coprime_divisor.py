#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def gcd(X, Y):
        if Y == 0:
            return X
        else:
            return Solution.gcd(Y, X % Y)

    @staticmethod
    def cpFact(A, B):
        for i in range(A + 1, 0, -1):
            if A % i == 0 and Solution.gcd(i, B) == 1:
                return i


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ((30, 12), 5),
            ((2, 3), 2),
            ((90, 47), 90)
        ]

    def test_cpFact(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.cpFact(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

