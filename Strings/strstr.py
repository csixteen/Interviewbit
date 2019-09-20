#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def strstr(N, H):
        if not N or not H or (len(N) > len(H)):
            return -1

        if N == H:
            return 0

        len_N = len(N)
        i = 0
        while i < len(H) - len(N):
            if H[i:i+len_N] == N:
                return i

            i += 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_strstr(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.strstr(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

