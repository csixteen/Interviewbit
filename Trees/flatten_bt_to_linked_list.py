#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def flatten(self, root):
        if not root or (not root.left and not root.right):
            return root

        current = root
        prev_right = root.right

        if current.left:
            current.right = self.flatten(current.left)
            current.left = None

            while current.right:
                current = current.right

        current.right = self.flatten(prev_right)

        return root

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_flatten(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.flatten(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

