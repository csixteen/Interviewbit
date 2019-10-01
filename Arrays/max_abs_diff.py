#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def maxArray2(A):
        _max = 0
        for i, ni in enumerate(A, 1):
            for j, nj in enumerate(A, 1):
                if i != j:
                    _max = max(_max, abs(ni - nj) + abs(i - j))

        return _max

    @staticmethod
    def maxArray(A):
        arr = [ni + i for i, ni in enumerate(A, 1)]
        arr2 = [ni - i for i, ni in enumerate(A, 1)]
        min1, min2, max1, max2 = arr[0], arr[0], arr2[0], arr2[0]
        for i in range(len(A)):
            min1 = min(min1, arr[i])
            min2 = min(min2, arr2[i])
            max1 = max(max1, arr[i])
            max2 = max(max2, arr2[i])
        
        return max(max1-min1, max2-min2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 3, -1], 5),
            ([2, 2, 2], 2)
        ]

    def test_maxArray(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.maxArray(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

