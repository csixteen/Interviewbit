#!/usr/bin/env python3
# coding: utf-8
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        def height(tree):
            if not tree:
                return 0
            else:
                return 1 + max(height(tree.left), height(tree.right))

        if not root:
            return True
        else:
            return self.isBalanced(root.left) and \
                    self.isBalanced(root.right) and \
                    abs(height(root.left) - height(root.right)) <= 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_isBalanced(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.isBalanced(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

