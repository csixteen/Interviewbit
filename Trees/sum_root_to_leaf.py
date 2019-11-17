#!/usr/bin/env python3
# coding: utf-8
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def DFS(node, number, acc):
            if not node.left and not node.right:
                acc.append(number + [node.val])
            else:
                if node.left:
                    DFS(node.left, number + [node.val], acc)
                if node.right:
                    DFS(node.right, number + [node.val], acc)

        if not root:
            return 0

        numbers = []
        DFS(root, [], numbers)

        return sum([sum([d * 10**i for i, d in enumerate(reversed(number))]) for number in numbers])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_sumNumbers(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.sumNumbers(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

