#!/usr/bin/env python3
# coding: utf-8
import unittest


class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        self.stack.append(x)
        if len(self.mins) == 0 or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        if len(self.stack) > 0:
            item = self.stack.pop()
            if len(self.mins) > 0 and item == self.mins[-1]:
                self.mins.pop()

            return item

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1

    def get_min(self):
        if len(self.mins) > 0:
            return self.mins[-1]
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = []

    def test_xpto(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.xpto(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

