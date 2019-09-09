#!/usr/bin/env python3
# coding: utf-8
from functools import reduce
import unittest


class Solution:
    @staticmethod
    def factors_prod(A):
        prod = 1
        factors = set()
        for i in range(1, int(A**0.5)+1):
            if A % i == 0:
                factors.add(i)
                factors.add(A // i)

        return reduce(lambda x, y: x*y, factors, 1)

    @staticmethod
    def solve(A, B):
        # Steps 1 and 2 - Insert the max of every subarray of A in G
        G = [max(A[i:j]) for i in range(len(A)+1) for j in range (i+1, len(A)+1)]
        G = sorted(map(lambda x: Solution.factors_prod(x) % int(1e9 + 7), G), reverse=True)
        return [G[i-1] for i in B]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([1, 2, 4], [1, 2, 3, 4, 5, 6]), [8, 8, 8, 2, 2, 1])
        ]

    def test_solve(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.solve(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

