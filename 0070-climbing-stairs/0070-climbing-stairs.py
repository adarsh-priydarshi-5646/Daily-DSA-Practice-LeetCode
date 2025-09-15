class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        def helper(steps):
            if steps == 0 or steps == 1:
                return 1
            if dp[steps] != 0:
                return dp[steps]
            
            dp[steps] = helper(steps - 1) + helper(steps - 2)
            return dp[steps]
        
        return helper(n)
        