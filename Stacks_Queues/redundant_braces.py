#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def braces(A):
        ops = '+-*/'
        b = []
        o = []
        prev = None

        for c in A:
            if c == '(':
                b.append('(')
                prev = '('
            elif c == ')':
                if not o:
                    return 1
                else:
                    prev = ')'
                    b.pop()
                    o.pop()
            elif c in ops and prev and prev not in ops and b:
                o.append(c)
                prev = c

        return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ('((a + b))', 1),
            ('((a + b) + a)', 0),
            ('(((a + b)) + c)', 1),
            ('((a + b) + (c + d))', 0),
            ('(a + (a + b))', 0),
            ('(c + ((a + b)))', 1),
            ('((((a + b))))', 1),
            ('(a + b + c + d)', 0),
            ('a + b', 0),
            ('(a)', 1),
            ('(a*b)+(b*(d+(a)))', 1)
        ]

    def test_braces(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.braces(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

