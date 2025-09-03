from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        # Trackers
        column = [0] * n              # Column occupied ya nahi
        leftDig = [0] * (2 * n - 1)   # Left diagonal (n-1 + col - row)
        rightDig = [0] * (2 * n - 1)  # Right diagonal (row + col)

        def backtrack(row):
            # Base case -> agar saare rows fill ho gaye
            if row == n:
                solution = []
                for r in board:
                    line = ""
                    for c in r:
                        line += c
                    solution.append(line)
                result.append(solution)
                return

            for col in range(n):
                if column[col] == 0 and leftDig[n - 1 + col - row] == 0 and rightDig[row + col] == 0:
                    board[row][col] = "Q"
                    column[col] = 1
                    leftDig[n - 1 + col - row] = 1
                    rightDig[row + col] = 1
                    backtrack(row + 1)
                    # Backtrack
                    board[row][col] = "."
                    column[col] = 0
                    leftDig[n - 1 + col - row] = 0
                    rightDig[row + col] = 0

        backtrack(0)
        return result
