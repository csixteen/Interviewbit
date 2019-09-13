#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def sortColors(A):
        """
        Naive solution: implemented a Quicksort.
        Time complexity: O(nlgn) or O(n^2)
        """
        if len(A) == 0:
            return A
        else:
            return sortColors([c for c in A if c < A[0]]) + \
                    [c for c in A if c == A[0]] + \
                    sortColors([c for c in A if c > A[0]])

    def sortColors2(A):
        """
        There are only 3 different values: 0, 1 and 2. We can
        count the occurrences of each value and get the resulting
        sorted array in linear time.
        Time complexity: O(n)
        """
        ret = [0, 0, 0]
        for i in A:
            ret[i] += 1

        return [0]*ret[0] + [1]*ret[1] + [2]*ret[2]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_sortColors(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.sortColors(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

