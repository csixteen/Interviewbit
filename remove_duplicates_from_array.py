#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def removeDuplicates(A):
        if len(A) < 2:
            return len(A)

        curr, fut = 1, 1
        while fut < len(A):
            if A[fut] == A[curr-1]:
                fut += 1
            else:
                A[curr] = A[fut]
                curr += 1
                fut += 1

        A = A[:curr]
        return len(A)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 1, 2], 2),
            ([1, 2, 3, 4, 5], 5),
            ([1, 1, 1, 1, 1], 1)
        ]

    def test_removeDuplicates(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.removeDuplicates(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

