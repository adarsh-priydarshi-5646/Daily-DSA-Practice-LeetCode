class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(".")
            board.append(row)

        def is_safe(row, col):
            # Check same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            # Base case
            if row == n:
                solution = []
                for r in board:
                    solution.append("".join(r))
                result.append(solution)
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."  # Backtrack

        backtrack(0)
        return result
