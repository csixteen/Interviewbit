#!/usr/bin/env python3
# coding: utf-8
from array import array
import unittest


class Solution:
    @staticmethod
    def first_missing_positive(A):
        m = max(A)
        if m <= 0:
            return 1

        tmp = array('b', [0] * m)
        for i in A:
            if i > 0:
                tmp[i - 1] = 1

        for i, v in enumerate(tmp):
            if v == 0:
                return i + 1
        else:
            return m + 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_case = [
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([-8, -7, -6], 1)
        ]

    def test_first_missing_integer(self):
        for i, e in self.test_case:
            self.assertEqual(Solution.first_missing_positive(i), e)


if __name__ == '__main__':
    unittest.main()

