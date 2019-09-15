#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def lengthLastWord(A):
        length = 0
        inWord = False
        for c in reversed(A):
            if c == ' ' and inWord:
                return length
            elif c != ' ':
                if not inWord:
                    inWord = True
                length += 1
        
        return length


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_lengthLastWord(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.lengthLastWord(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

