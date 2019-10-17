#!/usr/bin/env python3
# coding: utf-8
import unittest


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class MergingRanges:
    def merge(self, A):
        if len(A) <= 1:
            return A

        ret = []
        start, end = A[0].start, A[0].end
        
        for i in range(1, len(A)):
            if A[i].start > end:
                ret.append(Interval(s=start, e=end))
                start, end = A[i].start, A[i].end
            else:
                end = max(A[i].end, end)

        ret.append(Interval(s=start, e=end))
        
        return ret

    def insert(self, A, B):
        A.append(B)
        return self.merge(sorted(A, key=lambda x: x.start))


class TestMergingRanges(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_merge(self):
        for i, e in self.test_cases:
            self.assertEqual(MergingRanges.merge(i), e)


if __name__ == '__main__':
    unittest.main()

