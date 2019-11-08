#!/usr/bin/env python3
# coding: utf-8
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None

        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])

        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_sortedArrayToBST(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.sortedArrayToBST(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

