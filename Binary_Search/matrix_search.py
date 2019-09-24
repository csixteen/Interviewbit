#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def binSearch(self, N, A):
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if A[mid] == N:
                return 1
            elif N > A[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return 0

    def searchMatrix(self, A, B):
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if A[mid][0] <= B <= A[mid][-1]:
                return self.binSearch(B, A[mid])
            elif B < A[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1

        return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3), 1),
            (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 4), 0),
            (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 1000), 0)
        ]

    def test_searchMatrix(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.searchMatrix(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

