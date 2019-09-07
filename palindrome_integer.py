#!/usr/bin/env python3
# coding: utf-8
import math
import unittest


class Solution:
    @staticmethod
    def isPalindrome(X):
        rev = 0
        num = X
        while num > 0:
            temp = num % 10
            rev = rev*10 + temp
            num = math.floor(num / 10)

        if X == num:
            return 1
        else:
            return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (1, 1),
            (12, 0),
            (121, 1),
            (1221, 1),
            (12212, 0)
        ]

    def test_isPalindrome(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.isPalindrome(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

