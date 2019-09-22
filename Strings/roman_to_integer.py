#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def romanToInt(N):
        vals = {
            "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
            "XL": 40, "L": 50, "XC": 90, "C": 100,
            "CD": 400, "D": 500, "CM": 900, "M": 1000
        }

        total = 0
        i = 0
        while i < len(N):
            if i < len(N) - 1 and N[i:i+2] in vals:
                total += vals[N[i:i+2]]
                i += 2
            else:
                total += vals[N[i]]
                i += 1

        return total


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("I", 1),
            ("III", 3),
            ("IV", 4),
            ("XIV", 14),
            ("XI", 11),
            ("MMM", 3000),
            ("MMMCM", 3900),
            ("MMMCMXLIX", 3949)
        ]

    def test_romanToInt(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.romanToInt(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

