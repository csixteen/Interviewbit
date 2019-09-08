#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def addBinary(A, B):
        tmp, carry = 0, 0
        A, B = list(map(int, A)), list(map(int, B))
        len_A, len_B = len(A), len(B)
        ret = []
        while not (len_A <= 0 and len_B <= 0):
            if carry > 0:
                tmp = 1
                carry -= 1
            if len_A > 0:
                carry += (A[len_A-1] + tmp) // 2
                tmp = (A[len_A-1] + tmp) % 2
                len_A -= 1
            if len_B > 0:
                carry += (B[len_B-1] + tmp) // 2
                tmp = (B[len_B-1] + tmp) % 2
                len_B -= 1

            ret.insert(0, tmp)
            tmp = 0

        if carry > 0:
            ret.insert(0, 1)

        return ''.join(map(str, ret))

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (("100", "11"), "111"),
            (("11", "11"), "110"),
            (("110", "11"), "1001")
        ]

    def test_addBinary(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.addBinary(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

