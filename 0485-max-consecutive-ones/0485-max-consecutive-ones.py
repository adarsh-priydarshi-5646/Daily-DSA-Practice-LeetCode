class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                if cnt > maxi:
                    maxi = cnt
            else:
                cnt = 0
        return maxi
       