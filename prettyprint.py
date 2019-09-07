#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def prettyPrint(A):
        ret = [[1]]
        for i in range(2, A + 1):
            outer = 2*i - 1
            ret = [[i]*outer] + list(map(lambda row: [i] + row + [i], ret)) + [[i]*outer]

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (3, [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]),
            (4, [
                [4, 4, 4, 4, 4, 4, 4],
                [4, 3, 3, 3, 3, 3, 4],
                [4, 3, 2, 2, 2, 3, 4],
                [4, 3, 2, 1, 2, 3, 4],
                [4, 3, 2, 2, 2, 3, 4],
                [4, 3, 3, 3, 3, 3, 4],
                [4, 4, 4, 4, 4, 4, 4]
            ])
        ]

    def test_prettyPrint(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.prettyPrint(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

