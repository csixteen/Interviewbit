#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def solve(A, B, C):
        i, j, k = len(A)-1, len(B)-1, len(C)-1
        md = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
        while i >= 0 and j >= 0 and k >= 0:
            md = min(md, abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])))
            m = max(A[i], B[j], C[k])
            if A[i] == m:
                i -= 1
            elif B[j] == m:
                j -= 1
            else:
                k -= 1

        return md


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([1, 4, 5, 8, 10], [6, 9, 15], [2, 3, 6, 6]), 1)
        ]

    def test_solve(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.solve(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

