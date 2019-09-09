#!/usr/bin/env python3
# coding: utf-8
from functools import cmp_to_key
import unittest


class Solution:
    @staticmethod
    def is_larger(a, b):
        ab = int("{}{}".format(a, b))
        ba = int("{}{}".format(b, a))
        if ab > ba:
            return 1
        elif ba > ab:
            return -1
        else:
            return 0

    @staticmethod
    def largestNumber(A):
        return str(int("".join(map(str, sorted(A, reverse=True,key=cmp_to_key(Solution.is_larger))))))

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([3, 30, 34, 5, 9], "9534330"),
            ([0, 0, 0, 0, 0], "0"),
            ([12, 121], "12121"),
            ([271, 27], "27271"),
            ([9, 99, 999, 9999, 9998], "99999999999998")
        ]

    def test_largestNumber(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.largestNumber(i), e)


if __name__ == '__main__':
    unittest.main()

