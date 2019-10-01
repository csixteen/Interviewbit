#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def swapPairs2(A):
        if not A.next:
            return A

        head = A.next
        prev = ListNode(None)
        left = A
        while left:
            tmp = left
            right = left.next
            if right:
                prev.next = right
                left.next = right.next
                right.next = left

            left = tmp
            tmp = None
            prev = left
            left = left.next

        return head

    @staticmethod
    def swapPairs(A):
        head = A.next if A and A.next else A
        while A and A.next:
            C = A.next.next
            D = C.next if C and C.next else C
            A.next.next, A.next, A = A, D, C

        return head
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_swapPairs(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.swapPairs(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

