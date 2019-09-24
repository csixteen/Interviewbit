#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def findPerm(S, I):
        res = []
        left, right = 1, I
        c = 0
        while left < right:
            if S[c] == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
            c += 1

        res.append(left)

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (('ID', 3), [1, 3, 2]),
            (('IIII', 5), [1, 2, 3, 4, 5]),
            (('DDDD', 5), [5, 4, 3, 2, 1])
        ]

    def test_findPerm(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.findPerm(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

