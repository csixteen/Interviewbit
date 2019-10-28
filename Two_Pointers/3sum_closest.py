#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def threeSum(self, A, t):
        A.sort()
        if A[0] >= t:
            return sum(A[:3])
        elif A[-1] <= t:
            return sum(A[-3:])

        l = len(A)
        closest = sum(A[:3])
        i = 0
        while i < l - 2:
            left, right = i + 1, l - 1
            while left < right:
                s = A[i] + A[left] + A[right]
                if s == t:
                    return s
                elif abs(t - s) < abs(t - closest):
                    closest = s

                if s < t:
                    left += 1
                else:
                    right -= 1

            i += 1

        return closest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_threeSum(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(sorted(s.threeSum(i)), sorted(e))


if __name__ == '__main__':
    unittest.main(verbosity=2)

