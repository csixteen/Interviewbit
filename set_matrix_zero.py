#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def setZeroes(self):
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([[0, 0], [1, 0]], [[0, 0], [0, 0]])
        ]

    def test_setZeroes(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.setZeroes(i), e)


if __name__ == '__main__':
    unittest.main()

