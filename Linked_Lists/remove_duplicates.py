#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def deleteDuplicates(A):
        if not A:
            return A

        i, j = A, A.next
        while j:
            while j and j.val == i.val:
                j = j.next
            i.next = j
            i = i.next

        return A


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_deleteDuplicates(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.deleteDuplicates(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

