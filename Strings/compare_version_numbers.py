#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def compareVersion(A, B):
        listA = list(map(int, A.split('.')))
        listB = list(map(int, B.split('.')))
        lenA = len(listA)
        lenB = len(listB)

        while lenA < lenB:
            listA.append(0)
            lenA += 1

        while lenB < lenA:
            listB.append(0)
            lenB += 1

        if listA < listB:
            return -1
        if listB < listA:
            return 1
        return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_compareVersion(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.compareVersion(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

