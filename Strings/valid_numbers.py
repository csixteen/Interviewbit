#!/usr/bin/env python3
# coding: utf-8
import string
import unittest


class Solution:
    @staticmethod
    def isNumber(N):
        N = N.strip()

        if len(N) == 0 or not N[-1] in string.digits:
            return 0
        if not (N[0] in string.digits + '.-e'):
            return 0
        
        e_index = -1
        dot_index = -1
        for i, c in enumerate(N):
            if c == 'e' and e_index != -1:
                return 0
            elif c == 'e':
                e_index = i
                continue

            if c == '.' and (dot_index > -1 or (e_index > -1 and i > e_index)):
                return 0
            elif c == '.':
                dot_index = i
                continue

            if c == '-' and (i > 0 and (e_index == i - 1) or (i == 0)):
                continue

            if c not in string.digits:
                return 0

        if dot_index > -1 and not N[dot_index+1] in string.digits:
            return 0

        return 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("     ", 0),
            ("001", 1),
            (" 0.1", 1),
            ("1 a", 0),
            ("0", 1),
            ("abc", 0),
            ("2e10", 1),
            ("2.e10", 0),
            ("3e0.1", 0),
            ("0.1e10", 1),
            ("-01.1e-10", 1)
        ]

    def test_isNumber(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.isNumber(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

