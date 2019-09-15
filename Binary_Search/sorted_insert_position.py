#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def searchInsert(A, B):
        if B < A[0]:
            return 0
        if B > A[-1]:
            return len(A)

        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([1, 3, 5, 6], 5), 2),
            (([1, 3, 5, 6], 2), 1),
            (([1, 3, 5, 6], 0), 0),
            (([1, 3, 5, 6], 7), 4)
        ]

    def test_searchInsert(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.searchInsert(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

