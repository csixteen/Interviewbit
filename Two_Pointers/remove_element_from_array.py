#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def removeElement(A, B):
        curr, fut = 0, 0
        while fut < len(A):
            if A[fut] == B:
                fut += 1
            else:
                A[curr] = A[fut]
                curr += 1
                fut += 1

        A = A[:curr]
        return len(A)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([1, 1, 2], 1), 1),
            (([1, 2, 3, 4, 5], 5), 4),
            (([1, 1, 1, 1, 1], 1), 0)
        ]

    def test_removeElement(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.removeElement(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

