#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def titleToNumber(A):
        ret = 0
        for i, c in enumerate(reversed(A)):
            ret += (ord(c) - ord('A') + 1) * (26**i)

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("A", 1),
            ("B", 2),
            ("AA", 27),
            ("AB", 28)
        ]

    def test_titleToNumber(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.titleToNumber(i), e)


if __name__ == '__main__':
    unittest.main()

