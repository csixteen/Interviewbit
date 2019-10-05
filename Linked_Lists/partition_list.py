#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def partition(A, B):
        head1 = ListNode(None)  # handle for nodes < B
        head2 = ListNode(None)  # handle for nodes >= B
        node1, node2 = head1, head2
        while A:
            if A.val < B:
                node1.next, node1, A = A, A, A.next
            else:
                node2.next, node2, A = A, A, A.next

        node1.next = head2.next  # Links the two lists
        node2.next = None

        return head1.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_partition(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.partition(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

