class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if maxi < s:
                maxi = s
            if s < 0:
                s = 0
        return maxi





        # m = float('-inf')
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     s = 0
        #     for j in range(i, len(nums)):
        #         s += nums[j]
        #         if s > m:
        #             m = s
        # return m


        