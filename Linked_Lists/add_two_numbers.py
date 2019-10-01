#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def addTwoNumbers(A, B):
        head = ListNode(None)
        curr = head
        carry = 0
        tmp = 0
        while A or B:
            tmp = carry
            carry = 0
            if A:
                tmp += A.val
                A = A.next
            if B:
                tmp += B.val
                B = B.next
            if tmp >= 10:
                tmp = tmp % 10
                carry += 1
            curr.next = ListNode(tmp)
            curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)

        return head.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_addTwoNumbers(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.addTwoNumbers(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

