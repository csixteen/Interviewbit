#!/usr/bin/env python3
# coding: utf-8
import re
import unittest


class Solution:
    def atoi(self, N):
        g = re.match(r'\s*((\-|\+)?\d+)[\s|\w]*', N)
        if g:
            i = int(g.group(1))
            i = max(min(i, 2147483647), -2147483648)
            return i
        else:
            return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ('+1', 1),
            ('42', 42),
            ('      -42', -42),
            ('4193 with words', 4193),
            ('words and 987', 0),
            ('-91283472332', -2147483648),
            ('91283472332', 2147483647),
            ('9 200', 9)
        ]

    def test_atoi(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.atoi(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

