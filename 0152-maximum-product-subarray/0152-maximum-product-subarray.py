class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        # 1. Forward Pass (Left to Right)
        current_product = 1
        for i in range(len(nums)):
            current_product *= nums[i]
            
            if current_product > max_product:
                max_product = current_product
            if current_product == 0:
                current_product = 1
                
        # 2. Backward Pass (Right to Left)
        current_product = 1
        for i in range(len(nums) - 1, -1, -1):
            current_product *= nums[i]
            
            if current_product > max_product:
                max_product = current_product
            if current_product == 0:
                current_product = 1
                
        return max_product

