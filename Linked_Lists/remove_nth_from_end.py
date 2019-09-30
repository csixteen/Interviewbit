#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def removeNthFromEnd(A, B):
        fast = A
        while fast and B > 0:
            fast = fast.next
            B -= 1

        if not fast:
            tmp = A
            if A:
                A = A.next
            tmp = None
            return A

        slow = A
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next
        prev = None

        return A


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_removeNthFromEnd(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.removeNthFromEnd(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

