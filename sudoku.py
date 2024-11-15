from typing import List

class Input:
    @staticmethod
    def takeinput():
        board = []
        print("Please enter 9 rows of 9 numbers (use '.' for empty cells):")
        for _ in range(9):
            board.append(input().split())
        return board

#class Check: