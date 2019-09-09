#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def longestCommonPrefix(A):
        ret = []
        for s in [set(x) for x in zip(*A)]:
            if len(s) > 1:
                break
            else:
                ret.append(s.pop())

        return ''.join(ret)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (["abcd", "abde", "abcf"], "ab")
        ]

    def test_longestCommonPrefix(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.longestCommonPrefix(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

