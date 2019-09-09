#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def cover_points(A, B):
        steps = 0
        prev_x, prev_y = A[0], B[0]

        for x, y in zip(A, B):
            dx, dy = abs(x - prev_x), abs(y - prev_y)
            steps += max(dx, dy)
            
            prev_x = x
            prev_y = y

        return steps


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([0, 1, 1], [0, 1, 2]), 2),
            (([0, 1, 1], [0, 1, 4]), 4),
            (([-7, -13], [1, -5]), 6),
            (([-2], [7]), 0),
            (([4, 8, -7, -5, -13, 9, -7, 8], [4, -15, -10, -3, -13, 12, 8, -8]), 108)
        ]

    def test_cover_points(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.cover_points(*i), e)


if __name__ == '__main__':
    unittest.main()
