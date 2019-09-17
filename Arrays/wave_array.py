#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def wave(self):
        A = sorted(A)
        for i in range(0, len(A)-1, 2):
            A[i], A[i+1] = A[i+1], A[i]
        return A


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_wave(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.wave(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

