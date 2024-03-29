#!/usr/bin/env python3
# coding: utf-8
from collections import defaultdict
import unittest


class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        if len(points) < 3:
            # We can always form a line between two points.
            return len(points)

        max_points = 0
        for i in range(len(points) - 1):
            slopes = defaultdict(int)
            line, repeated = 0, 0
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]
                if dx == 0 and dy == 0:
                    # For then we have the same point repeated
                    repeated += 1
                    continue

                g = gcd(dx, dy)
                s = (dy // g, dx // g)
                slopes[s] += 1
                line = max(line, slopes[s])

            max_points = max(max_points, line + repeated + 1)

        return max_points


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([], 0),
            ([[0, 0]], 1),
            ([[0, 0], [0, 0]], 2), 
            ([[1,1],[2,2],[3,3]], 3),
            ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4)
        ]

    def test_maxPoints(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.maxPoints(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

