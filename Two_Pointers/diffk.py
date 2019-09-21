#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def diffPossible(A, B):
        if len(A) < 2:
            return 0

        left, right = 0, 1
        while right < len(A) and (A[right] - A[left] < B):
            right += 1

        while right < len(A) and left != right:
            if A[right] - A[left] == B:
                return 1
            elif A[right] - A[left] > B:
                left += 1
                if left == right:
                    right += 1
            else:
                right += 1

        return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([1, 3, 5], 4), 1),
            (([1, 3, 5], 6), 0),
            (([1, 2, 2, 3, 4], 0), 1),
            (([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 1),
            (([1, 2, 3, 4, 5, 6, 7, 8, 9], 11), 0),
            (([1, 2, 3, 4, 5, 6, 7, 8, 9], 0), 0),
            (([-9, -3, 0, 400, 401, 500], 410), 1)
        ]

    def test_diffPossible(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.diffPossible(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

