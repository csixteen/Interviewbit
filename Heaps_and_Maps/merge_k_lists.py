#!/usr/bin/env python3
# coding: utf-8
import unittest


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def mergeTwoLists(self, l1=None, l2=None):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtyle: ListNode
        """
        l3, ret = None, None
        while not (l1 is None and l2 is None):
            choose_l1 = (l2 is None) or \
                (l1 is not None and l2 is not None and l1.val < l2.val)
            if choose_l1:
                tmp = l1.val
                l1 = l1.next
            else:
                tmp = l2.val
                l2 = l2.next

            if ret is None:
                l3 = ListNode(tmp)
                ret = l3
            else:
                l3.next = ListNode(tmp)
                l3 = l3.next
        return ret

    def mergeKLists(self, lists):
        if len(lists) <= 2:
            return self.mergeTwoLists(*lists)

        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]
        left = self.mergeKLists(left)
        right = self.mergeKLists(right)

        return self.mergeTwoLists(left, right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_mergeKLists(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.mergeKLists(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

