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

        for j in range(3):
            for l in range(3):
                subgrid = [
                    board[j * 3 + m][l * 3 + n]
                    for m in range(3)
                    for n in range(3)
                    if board[j * 3 + m][l * 3 + n] != "."
                ]
                if len(subgrid) != len(set(subgrid)):
                    return False

        return True

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False

            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False

            return True

        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):
                            if isValid(board, row, col, num):
                                board[row][col] = num
                                if backtrack():
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        backtrack()

# Main execution
input_handler = Input()
board = input_handler.takeinput()

check = Check()
if not check.isValidSudoku(board):
    print("The input Sudoku board is invalid!")
else:
    solver = Solution()
    solver.solveSudoku(board)
    print("Solved Sudoku board:")
    for row in board:
        print(" ".join(row))
