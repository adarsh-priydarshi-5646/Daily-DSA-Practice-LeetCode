class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]  

        def is_safe(row, col):
            # Check same column me koi queen hai ya nahi
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            # Check left diagonal (↖ direction)
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            
            # Check right diagonal (↗ direction)
            i = row - 1 
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            
            # Agar koi attack position nahi mila, then safe hai
            return True

        def backtrack(row):
            # Base case: agar last row tak queens place kar di
            if row == n:
                # Board ko valid solution ke form me string list banakar result me store karo
                solution = ["".join(r) for r in board]
                result.append(solution)
                return
            
            for col in range(n):
                if is_safe(row, col):  # Agar (row, col) safe hai
                    board[row][col] = "Q"   # Queen place karo
                    backtrack(row + 1)      # Next row solve karo
                    board[row][col] = "."   # Backtrack: Queen hata do

        backtrack(0)
        return result
            