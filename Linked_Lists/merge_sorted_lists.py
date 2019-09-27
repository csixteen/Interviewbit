#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def mergeTwoLists(A, B):
        C, head = None,  None
        while not (A is None and B is None):
            choose_A = (B is None) or \
                (A is not None and B is not None and A.val < B.val)
            if choose_A:
                tmp = A.val
                A = A.next
            else:
                tmp = B.val
                B = B.next

            if head is None:
                C = ListNode(tmp)
                head = C
            else:
                C.next = ListNode(tmp)
                C = C.next
        return head

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_mergeTwoLists(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.mergeTwoLists(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

