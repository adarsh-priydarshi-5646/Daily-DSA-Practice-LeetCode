class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(row, col, index):
            # Base case: all letters matched
            if index == len(word):
                return True
            
            # Boundary and validity check
            if (row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]):
                return False
            
            # Mark current cell as visited
            temp = board[row][col]   # store original letter
            board[row][col] = '#'    # mark visited
            
            # Explore all 4 directions
            found = (
                dfs(row + 1, col, index + 1) or  # Down
                dfs(row - 1, col, index + 1) or  # Up
                dfs(row, col + 1, index + 1) or  # Right
                dfs(row, col - 1, index + 1)     # Left
            )
            
            # Backtrack: restore original letter
            board[row][col] = temp 
            return found
        
        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # match first letter
                    if dfs(i, j, 0):        # start DFS from here
                        return True
        
        return False  # word not found

        