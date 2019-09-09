#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def maxSpecialProduct(A):
        specialProduct = 0
        l = len(A)

        for i, v in enumerate(A):
            leftSpecial, rightSpecial, leftMax, rightMax = 0, 0, 0, 0
            # Determine left
            k = i-1
            while k >= 0:
                if A[k] > v and A[k] > leftMax:
                    leftSpecial = k
                    leftMax = A[k]
                    break
                k -= 1

            # Determine right
            k = i + 1
            while k < l:
                if A[k] > v and A[k] > rightMax:
                    rightSpecial = k
                    rightMax = A[k]
                    break
                k += 1

            if leftSpecial * rightSpecial > specialProduct:
                specialProduct = leftSpecial * rightSpecial

        return specialProduct % 1000000007



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9], 80),
            ([6, 7, 9, 5, 5, 8], 10)
        ]

    def test_maxSpecialProduct(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.maxSpecialProduct(i), e)


if __name__ == '__main__':
    unittest.main()

