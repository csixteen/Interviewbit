#!/usr/bin/env python3
# coding: utf-8
from typing import List
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        def DFS(node, target, curr_sum, path, acc):
            if not node.left and not node.right:
                if curr_sum + node.val == target:
                    acc.append(path + [node.val])
            else:
                if node.left:
                    DFS(node.left, target, curr_sum + node.val, path + [node.val], acc)
                if node.right:
                    DFS(node.right, target, curr_sum + node.val, path + [node.val], acc)

        if not root:
            return []

        res = []
        DFS(root, s, 0, [], res)

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_pathSum(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.pathSum(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

