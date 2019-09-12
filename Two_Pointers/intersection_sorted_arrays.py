#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def intersect(A, B):
        len_A, len_B = len(A), len(B)
        i, j = 0, 0
        ret = []
        while i < len_A and j < len_B:
            if A[i] == B[j]:
                ret.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([1, 2, 3, 3, 4, 5, 6], [3, 3, 5]), [3, 3, 5]),
            (([1, 2, 3, 3, 4, 5, 6], [3, 5]), [3, 5])
        ]

    def test_intersect(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.intersect(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

