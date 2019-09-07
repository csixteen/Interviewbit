#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def is_prime(N):
        if N == 1:
            return False
        if N == 2:
            return True
        if N % 2 == 0:
            return False
        if N < 9:
            return True

        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                return False

        return True

    @staticmethod
    def generate_primes(U):
        pL, pS = [2, 3, 5, 7, 11, 13], {2, 3, 5, 7, 11, 13}
        for i in range(17, U+1, 2):
            if Solution.is_prime(i):
                pL.append(i)
                pS.add(i)

        return pL, pS

    @staticmethod
    def primesum(A):
        primesList, primesSet = Solution.generate_primes(A)
        print(primesList, primesSet)
        for i in primesList:
            if A - i in primesSet:
                return i, A - i


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (4, (2, 2)),
            (18, (5, 13)),
            (184, (3, 181))
        ]

    def test_primesum(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.primesum(i), e)


if __name__ == '__main__':
    unittest.main()

