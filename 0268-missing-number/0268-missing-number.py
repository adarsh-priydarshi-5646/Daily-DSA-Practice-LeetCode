class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # ss = n*(n+1)//2
        # s = 0
        # for i in range(n):
        #     s += nums[i]
        # return ss - s

        n = len(nums)
        for i in range(n+1):
            flag = 0
            for j in range(n):
                if i == nums[j]:
                    flag = 1
                    break
            if flag == 0:
                return i


        