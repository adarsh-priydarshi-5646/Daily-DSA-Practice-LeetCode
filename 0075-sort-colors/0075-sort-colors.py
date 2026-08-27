class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1 
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

        #brute
        # cnt0 = 0
        # cnt1 = 0
        # cnt2 = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         cnt0 += 1
        #     if nums[i] == 1:
        #         cnt1 += 1
        #     if nums[i] == 2:
        #         cnt2 += 1
        # for i in range(cnt0):
        #     nums[i] = 0
        # for i in range(cnt0,cnt0+cnt1):
        #     nums[i] = 1
        # for i in range(cnt0+cnt1, len(nums)):
        #     nums[i] = 2
        # return nums