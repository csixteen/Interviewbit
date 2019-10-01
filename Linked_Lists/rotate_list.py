#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def rotateRight(A, B):
        new_tail= old_tail= A
        while B > 0:
            old_tail = old_tail.next
            if not old_tail:
                old_tail = A
            B -= 1

        while old_tail.next:
            old_tail = old_tail.next
            new_tail = new_tail.next

        old_tail.next = A
        new_head = new_tail.next
        new_tail.next = None

        return new_head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_rotateRight(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.rotateRight(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

