#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def solve(A):
        A = sorted(A)
        count = len(A) - 1
        i = 1
        while i < len(A):
            if (A[i] == A[i-1]) or (A[i-1] != count):
                i += 1
                count -= 1
            else:
                return 1

        return 1 if A[i-1] == count else -1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_solve(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.solve(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

