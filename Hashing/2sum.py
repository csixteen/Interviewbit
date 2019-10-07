#!/usr/bin/env python3
# coding: utf-8
from collections import defaultdict, deque
import unittest


class Solution:
    @staticmethod
    def twoSum(A, B):
        diffs = {}
        for i, v in enumerate(A, 1):
            if B - v in diffs:
                return [diffs[B - v], i]
            elif v not in diffs:
                diffs[v] = i

        return []


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([2, 7, 11, 15], 10), []),
            (([2, 7, 11, 15], 9), [1, 2]),
            (([2, 7, 11, 15, 2, 7], 9), [1, 2]),
            (([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8], -3), [4, 8]),
            (([1, 1, 1], 2), [1, 2])
        ]

    def test_twoSum(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.twoSum(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

