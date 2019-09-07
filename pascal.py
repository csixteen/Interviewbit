#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def solve(n):
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1, 1]]
        ret = [[1], [1, 1]]
        for i in range(2, n):
            ret.append([1] + [ret[i-1][j] + ret[i-1][j+1] for j in range(len(ret[i-1])-1)] + [1])

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (1, [[1]]),
            (2, [[1], [1, 1]]),
            (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
            (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
        ]

    def test_solve(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.solve(i), e)


if __name__ == '__main__':
    unittest.main()

