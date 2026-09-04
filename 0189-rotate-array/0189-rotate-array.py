from typing import List

class Solution: 
    def reverse(self, nums: List[int], start:int, end:int) -> None: 
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start] 
            start += 1 
            end -= 1 
    def rotate(self, nums: List[int], k: int) -> None: 
        """ 
        Do not return anything, modify nums in-place instead. 
        """
        n = len(nums)
        if n == 0 or k == 0: 
            return nums 
        k = k % n 
        # Step 1: reverse first k elements 
        self.reverse(nums, 0, n-k-1) 
        # Step 2: reverse remaining n-k elements 
        self.reverse(nums, n-k, n - 1) 
        # Step 3: reverse entire array 
        self.reverse(nums, 0, n-1) 
        return nums

        #brute force
        # n = len(nums)
        # k = k % n
        # temp = []
        # for i in range(n - k, n):
        #     temp.append(nums[i])  
        # j = n - 1
        # for i in range(n - k - 1, -1, -1):
        #     nums[j] = nums[i]
        #     j -= 1
        # for i in range(k):
        #     nums[i] = temp[i]
        # return nums

