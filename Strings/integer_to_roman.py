#!/usr/bin/env python3
# coding: utf-8
from collections import deque
import unittest


class Solution:
    @staticmethod
    def intToRoman(A):
        vals = {
            1: {
                1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'
            },
            10: {
                1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'
            },
            100: {
                1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'
            },
            1000: {
                1: 'M', 2: 'MM', 3: 'MMM'
            }
        }

        res = deque()
        n = 0
        while n < 4:
            x = (A % 10**(n+1)) // (10**n)
            if x in vals[10**n]:
                res.appendleft(vals[10**n][x])

            n += 1

        return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (5, 'V'),
            (14, 'XIV'),
            (1943, 'MCMXLIII'),
            (1940, 'MCMXL'),
            (2000, 'MM'),
            (3, 'III'),
            (10, 'X')
        ]

    def test_intToRoman(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.intToRoman(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

