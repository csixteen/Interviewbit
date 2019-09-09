#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def getRow(row):
        if row == 0:
            return [1]
        elif row == 1:
            return [1, 1]

        prev = [1, 1]
        for _ in range(2, row+1):
            ret = [1] + [prev[j] + prev[j+1] for j in range(len(prev)-1)] + [1]
            prev = ret

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (3, [1, 3, 3, 1]),
            (4, [1, 4, 6, 4, 1])
        ]

    def test_getRow(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.getRow(i), e)


if __name__ == '__main__':
    unittest.main()

