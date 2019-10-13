#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def subsets(self, A):
        res = {()}
        for c in A:
            res = res.union(set(map(lambda x: tuple(sorted(list(x) + [c])), res)))

        return [list(x) for x in res]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([], [[]]),
            ([1], [[], [1]]),
            ([1, 2], [[], [1], [2], [1, 2]]),
            ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
            ([1, 2, 3, 4], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]])
        ]

    def test_subsets(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.subsets(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

