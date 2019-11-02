#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def symmetric(self, A):
        def symm(x, y):
            if not x or not y:
                return not x and not y
            return x.val == y.val and symm(x.left, y.right) and symm(x.right, y.left)

        return True if not A else symm(A.left, A.right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_symmetric(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.symmetric(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

