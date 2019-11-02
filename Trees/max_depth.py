#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def maxDepth(self, t):
        if not t:
            return 0
        else:
            return 1 + max(self.maxDepth(t.left), self.maxDepth(t.right))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_maxDepth(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.maxDepth(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

