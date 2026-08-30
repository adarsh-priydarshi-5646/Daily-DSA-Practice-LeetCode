class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        posIndex = 0
        negIndex = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[posIndex] = nums[i]
                posIndex += 2
            else:
                ans[negIndex] = nums[i]
                negIndex += 2
        return ans
        

                