#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def reverseBetween(A, B, C):
        if not A.next:
            return A

        x = C - B
        head1 = ListNode(None)
        node1 = head1
        while A and B > 1:
            node1.next, node1, A = A, A, A.next
            B -= 1

        prev = None
        curr = A
        while curr and x >= 0:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
            x -= 1

        node1.next = prev

        tmp = head1.next
        while tmp.next:
            tmp = tmp.next

        tmp.next = curr

        return head1.next

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_reverseBetween(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.reverseBetween(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

