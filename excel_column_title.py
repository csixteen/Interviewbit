#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def convertToTitle(A):
        ret = []
        while A > 0:
            val = A % 26
            if val == 0:
                val = 26

            A = (A - val) // 26
            ret.append(chr(val + 64))

        return ''.join(reversed(ret))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (1, "A"),
            (2, "B"),
            (27, "AA"),
            (28, "AB"),
            (52, "AZ"),
            (53, "BA")
        ]

    def test_convertToTitle(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.convertToTitle(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

