class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, index, memo):
            if index >= len(nums):  
                return 0
            if index in memo:
                return memo[index]

            case1 = nums[index] + helper(nums, index + 2, memo)
            case2 = helper(nums, index + 1, memo)
            
            memo[index] = max(case1, case2)
            return memo[index]
        
        return helper(nums, 0, {})
        
        