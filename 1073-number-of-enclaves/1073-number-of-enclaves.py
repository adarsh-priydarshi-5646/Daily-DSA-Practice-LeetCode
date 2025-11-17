from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            if grid[i][0] == 1:
                q.append((i, 0))
            if grid[i][n-1] == 1:
                q.append((i, n-1))

        for j in range(n):
            if grid[0][j] == 1:
                q.append((0, j))
            if grid[m-1][j] == 1:
                q.append((m-1, j))

        while q:
            x, y = q.popleft()
            if grid[x][y] == 0:
                continue

            grid[x][y] = 0

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    q.append((nx, ny))


        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1

        return ans
