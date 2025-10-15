class Solution:
    def helper(self,i,j,m,n,memo):
        if i >= m or j >= n:
            return 0

        if i == m-1 and j == n-1:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        
        down = self.helper(i+1,j,m,n,memo)
        right = self.helper(i,j+1,m,n,memo)
        
        memo[(i, j)] = down + right
        return memo[(i, j)]

    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.helper(0,0,m,n,memo)


        