#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def singleNumber(A):
        singular = set()
        for i in A:
            if i in singular:
                singular.remove(i)
            else:
                singular.add(i)
        
        return singular.pop()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 2, 4, 4, 1], 3)
        ]

    def test_singleNumber(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.singleNumber(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

