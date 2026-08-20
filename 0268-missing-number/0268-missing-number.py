class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * (n + 1)
        for i in nums:
            arr[i] = 1
        for i in range(n + 1):
            if arr[i] == 0:
                return i





        #brute
        # for i in range(n+1):
        #     flag = 0
        #     for j in range(n):
        #         if i == nums[j]:
        #             flag = 1
        #             break
        #     if flag == 0:
        #         return i

        