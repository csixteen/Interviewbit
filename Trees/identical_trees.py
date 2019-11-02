#!/usr/bin/env python3
# coding: utf-8
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def identical(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.identical(p.left, q.left) and self.identical(p.right, q.right)
        else:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_identical(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(Solution.identical(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

