class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        temp = []
        for i in range(n - k, n):
            temp.append(nums[i])  
        j = n - 1
        for i in range(n - k - 1, -1, -1):
            nums[j] = nums[i]
            j -= 1
        for i in range(k):
            nums[i] = temp[i]
        
        return nums
