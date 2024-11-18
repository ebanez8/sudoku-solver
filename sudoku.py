from typing import List

class Input:
    @staticmethod
    def takeinput():
        board = []
        print("Please enter 9 rows of 9 numbers (use '.' for empty cells):")
        for _ in range(9):
            board.append(input().split())
        return board

class Check:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        for i in range(9):
            rows = [x for x in board[i] if x != "."]
            if len(rows) != len(set(rows)):
                return False
            column = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(column) != len(set(column)):
                return False