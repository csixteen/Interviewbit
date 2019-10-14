#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def longest(self, A):
        res = A[0]

        start, curr = 0, 0
        d = {}
        while curr < len(A):
            if A[curr] in d:
                if len(A[start:curr]) > len(res):
                    res = A[start:curr]

                while start < d[A[curr]]:
                    del d[A[start]]
                    start += 1

                start = d[A[curr]] + 1
                del d[A[curr]]
            else:
                d[A[curr]]  = curr
                curr += 1

        return max(len(A[start:curr]), len(res))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ('a', 1),
            ('aaaaaaaa', 1),
            ('dadbc', 4),
            ('aaabcdaeafghijajb', 7),
            ('abcdefghijaiiiiibcdefghijkloo', 12)
        ]

    def test_longest(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.longest(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

