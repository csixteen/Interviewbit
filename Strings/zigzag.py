#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    @staticmethod
    def convert(A, B):
        res = [[] for _ in range(B)]
        i = 0
        inc = 1
        for c in A:
            res[i].append(c)
            i += inc
            if i <= 0:
                i = 0
                inc = 1
            elif i >= B - 1:
                i = B - 1
                inc = -1

        return ''.join([''.join(x) for x in res])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR'),
            (('PAYPALISHIRING', 2), 'PYAIHRNAPLSIIG'),
            (('kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS', 1),
                'kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS'),
            (('ABCD', 2), 'ACBD')
        ]

    def test_convert(self):
        for i, e in self.test_cases:
            self.assertEqual(Solution.convert(*i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

