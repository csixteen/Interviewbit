#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def detectCycle2(A):
        while A and not hasattr(A, 'visited'):
            A.visited = True
            A = A.next

        if not A:
            return None
        return A

    @staticmethod
    def detectCycle(A):
        if not A:
            return None

        slow = fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow != fast:
            return None

        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_detectCycle(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.detectCycle(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

