#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def evalRPN(A):
        def evaluate(x, y, o):
            if o == '/':
                return x // y
            elif o == '+':
                return x + y
            elif o == '-':
                return x - y
            else:
                return x * y

        stack = []
        ops = {'+', '-', '*', '/'}
        for c in A:
            if c not in ops:
                stack.append(c)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(evaluate(x, y, c))

        return stack[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (["2", "1", "+", "3", "*"], 9),
            (["4", "13", "5", "/", "+"], 6)
        ]

    def test_evalRPN(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.evalRPN(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

