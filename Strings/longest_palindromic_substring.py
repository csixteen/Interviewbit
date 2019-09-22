#!/usr/bin/env python3
# coding: utf-8
from collections import defaultdict
import unittest


class Solution:
    @staticmethod
    def longestPalindrome(S):
        def is_palindrome(y):
            return y == y[::-1]

        if len(S) < 2:
            return S

        # Build sorted lists of indices where all chars occur
        indices = defaultdict(list)
        for i, c in enumerate(S):
            indices[c].append(i)

        longest = S[0]
        k = 0
        while k < len(S):
            last_occur = len(indices[S[k]]) - 1
            proceed = True
            while last_occur >= 0 and proceed:
                last = indices[S[k]][last_occur]
                if last >= k and (last - k) + 1 > len(longest) and is_palindrome(S[k:last+1]):
                    longest = S[k:last+1]
                    proceed = False

                last_occur -= 1

            k += 1

        return longest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ('babad', 'bab'),
            #('cbbd', 'bb'),
            #('bbbbbb', 'bbbbbb'),
            #('abcdefedbbbb', 'defed'),
            #('aaaaaaabcdefaaa', 'aaaaaaa'),
            #('aaaabcdeeee', 'aaaa'),
            #('', ''),
            #('c', 'c'),
            #('abcdef', 'a'),
            #('ccc', 'ccc')
        ]

    def test_longestPalindrome(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.longestPalindrome(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

