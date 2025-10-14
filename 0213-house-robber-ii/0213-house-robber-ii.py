class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(nums, index, n, memo):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            
            case1 = nums[index] + helper(nums, index + 2, n, memo)
            case2 = helper(nums, index + 1, n, memo)
            
            memo[index] = max(case1, case2)
            return memo[index]
        
        def rober(nums, n):
            if n == 1:
                return nums[0]
            rob1 = helper(nums, 0, n - 1, {})
            rob2 = helper(nums, 1, n, {})
            return max(rob1,rob2)
        
        return rober(nums, n)