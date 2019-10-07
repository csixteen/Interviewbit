#!/usr/bin/env python3
# coding: utf-8
from collections import defaultdict, deque
import unittest


class Solution:
    @staticmethod
    def twoSum2(A, B):
        d = defaultdict(deque)
        for i, n in enumerate(A, 1):
            d[n].append(i)

        index1, index2 = None, float('inf')
        for n in A:
            if n in d and B - n in d:
                i = d[n].popleft()
                if len(d[n]) == 0:
                    del d[n]

                if B - n in d:
                    j = d[B - n].popleft()
                    if len(d[B - n]) == 0:
                        del d[B - n]
                else:
                    continue

                if j < index2:
                    index1 = i
                    index2 = j

        if index1:
            return [index1, index2]

        return []

    def twoSum(A, B):
        diffs = {}
        for i, v in enumerate(A, 1):
            if B - v in diffs:
                return [diffs[B - v], i]
            elif v not in diffs:
                diffs[v] = i

        return []


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (([2, 7, 11, 15], 10), []),
            (([2, 7, 11, 15], 9), [1, 2]),
            (([2, 7, 11, 15, 2, 7], 9), [1, 2]),
            (([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8], -3), [4, 8]),
            (([1, 1, 1], 2), [1, 2])
        ]

    def test_twoSum(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.twoSum(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

