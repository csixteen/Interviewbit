#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def simplifyPath(A):
        path = list(filter(lambda x: len(x) > 0, A.split('/')))
        stack = []
        for x in path:
            if x == '..':
                if len(stack) > 0:
                    stack.pop()
            elif x == '.':
                continue
            else:
                stack.append(x)

        return '/' + '/'.join(stack)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_simplifyPath(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.simplifyPath(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

