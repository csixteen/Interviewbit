#!/usr/bin/env python3
# coding: utf-8
from collections import deque
import unittest


class Solution:
    def maxSlidingWindowBruteForce(self, nums, k):
        """
        Time complexity: O(Nk)
        Space complexity: O(N - k)
        """
        return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

    def maxSlidingWindowDoubleEndedQueue(self, A, B):
        res = []
        d = deque()

        for index, current in enumerate(A):
            if d and d[0] == index - B:
                d.popleft()

            while d and A[d[-1]] < current:
                d.pop()
            d.append(index)

            if index + 1 >= B:
                res.append(A[d[0]])

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([], 4), []),
            (([9, 11], 2), [11]),
            (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
            (([5, 4, 3, 2, 1, 0, -1, -2], 3), [5, 4, 3, 2, 1, 0]),
            (([5, 4, 3, 2, 1, 0, -1, -2], 2), [5, 4, 3, 2, 1, 0, -1]),
            (([1, 1, 1, 1, 1, 1, 1, 1], 6), [1, 1, 1]),
            (([100, 0, 99, -1, 3, -2, -22], 2), [100, 99, 99, 3, 3, -2]) 
        ]

    def test_maxSlidingWindow(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.maxSlidingWindowBruteForce(*i), e)
            self.assertEqual(s.maxSlidingWindowDoubleEndedQueue(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

