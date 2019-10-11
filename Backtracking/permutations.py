#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def remove(self, A, x):
        B = A[:]
        B.remove(x)
        return B

    def permute(self, A):
        if len(A) == 0:
            return [[]]
        else:
            res = []
            for c in A:
                res.extend(list(map(lambda p: [c] + p, self.permute(self.remove(A, c)))))

            return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        ]

    def test_permute(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.permute(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

