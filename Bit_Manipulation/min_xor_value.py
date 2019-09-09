#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def findMinXOR(A):
        A = sorted(A)
        m = A[0]^A[len(A)-1]
        i, j = 0, 1
        while j < len(A):
            m = min(m, A[i]^A[j])
            i += 1
            j += 1

        return m


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([2, 7, 5, 0], 2),
            ([9, 7, 0, 4], 3)
        ]

    def test_findMinXOR(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.findMinXOR(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

