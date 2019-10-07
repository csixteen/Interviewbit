#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def mergeTwoLists2(A, B):
        dummy = ListNode(None)
        curr = dummy
        while A and B:
            if A.val < B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next
            curr = curr.next

        if A:
            curr.next = A
        elif B:
            curr.next = B

        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_mergeTwoLists(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.mergeTwoLists(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

