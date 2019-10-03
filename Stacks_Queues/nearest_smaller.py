#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def prevSmaller(A):
        G = [-1] * len(A)
        stack = []
        for i, n in enumerate(A):
            while stack and stack[-1] >= n:
                stack.pop()

            if len(stack) > 0:
                G[i] = stack[-1]
            stack.append(n)

        return G


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([4, 5, 2, 10, 8], [-1, 4, -1, 2, 2]),
            ([4, 5, 2, 10, 8, 32], [-1, 4, -1, 2, 2, 8]),
            ([4, 5, 2, 10, 8, 7], [-1, 4, -1, 2, 2, 2]),
            ([1, 1, 1], [-1, -1, -1]),
            ([1], [-1]),
            ([1, 2, 3, 4], [-1, 1, 2, 3]),
            ([3, 2, 1], [-1, -1, -1])
        ]

    def test_prevSmaller(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.prevSmaller(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

