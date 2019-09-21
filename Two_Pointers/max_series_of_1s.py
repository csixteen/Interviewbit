#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def maxone(A, B):
        i = j = besti = bestj = 0
        while j < len(A):
            if A[j] == 0:
                B -= 1
                while i <= j and B < 0:
                    B += 1 if A[i] == 0 else 0
                    i += 1
            j += 1
            if j - i > bestj - besti:
                besti, bestj = i, j

        return list(range(besti, bestj))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([0, 0, 0, 0], 2), [0, 1]),
            (([0, 0, 0, 0], 5), [0, 1, 2, 3]),
            (([1, 1, 0], 2), [0, 1, 2]),
            (([1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 1), [0, 1, 2, 3, 4]),
            (([1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 2), [3, 4, 5, 6, 7, 8, 9]),
            (([1, 1, 1, 1, 1, 1], 3), [0, 1, 2, 3, 4, 5]),
            (([1, 1, 0, 0, 1, 1, 0, 0], 1), [0, 1, 2]),
            (([1, 0, 0, 0, 0, 0, 1, 0, 1, 1], 2), [5, 6, 7, 8, 9])
        ]

    def test_maxone(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.maxone(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

