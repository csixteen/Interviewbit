#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def maxset(A):
        ret = []
        tmp = []
        l = len(A)
        for i in A:
            if i >= 0:
                tmp.append(i)
                continue
            elif sum(tmp) > sum(ret):
                ret = tmp
            elif sum(tmp) == sum(ret) and \
                    len(tmp) > len(ret):
                ret = tmp

            tmp = []


        if sum(tmp) > sum(ret) or \
                (sum(tmp) == sum(ret) and len(tmp) > len(ret)):
            ret = tmp

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 5, -7, 2, 3], [1, 2, 5]),
            ([1, 2, 5, -7, 2, 3, 4], [2, 3, 4]),
            ([756898537, -1973594324, -2038664370, -184803526, 1424268980], [1424268980])
        ]

    def test_maxset(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.maxset(i), e)


if __name__ == '__main__':
    unittest.main()
