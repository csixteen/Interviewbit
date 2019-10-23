#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def maxArea(self, heights):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i, j = 0, len(heights) - 1
        max_area = 0
        while i != j:
            area = (j - i) * min(heights[i], heights[j])
            if area > max_area:
                max_area = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 1], 1),
            ([7, 9, 12, 5], 15),
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 3, 2, 5, 25, 24, 5], 24)
        ]

    def test_maxArea(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.maxArea(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

