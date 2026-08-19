class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        j = 0 
        
        # Iterate through the array with pointer i
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap elements
                nums[j], nums[i] = nums[i], nums[j]
                # Move the non-zero position pointer forward
                j += 1
        return nums


        #brute
        # temp = []
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         temp.append(nums[i])
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        # for i in range(len(temp), len(nums)):
        #     nums[i] = 0
        # return nums
        