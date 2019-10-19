#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def solve(self, board):
        def values(row, col):
            all_numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            square_top = (row // 3) * 3
            square_left = (col // 3) * 3
            for i in range(9):
                all_numbers.discard(board[row][i])
                all_numbers.discard(board[i][col])
                all_numbers.discard(board[square_top + i // 3][square_left + i % 3])

            return all_numbers

        def sudoku(pairs):
            if len(pairs) == 0:
                return True

            row, col = pairs[0]
            for value in values(row, col):
                board[row][col] = value
                if sudoku(pairs[1:]):
                    return True

            board[row][col] = '.'
            return False

        pairs = [(row, col) for row in range(9) for col in range(9) if board[row][col] == '.']
        sudoku(pairs)
        return board


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (
                [
                    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
                ], 
                []
            )
        ]

    def test_solve(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(s.solve(i), e)


if __name__ == '__main__':
    unittest.main(verbosity=2)

