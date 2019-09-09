#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def get_all_factors(A):
        ret = set()
        for i in range(1, int(A**0.5)+1):
            if A % i == 0:
                ret.add(i)
                ret.add(A // i)

        return sorted(ret)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),
            (17, [1, 17]),
            (10, [1, 2, 5, 10])
        ]

    def test_get_all_factors(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.get_all_factors(i), e)


if __name__ == '__main__':
    unittest.main()

