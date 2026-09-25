class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # newArr = []
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] not in newArr:
        #         cnt = 0
        #         for j in range(n):
        #             if nums[j] == nums[i]:
        #                 cnt += 1 
        #         if cnt > n // 3:
        #             newArr.append(nums[i])  
        # return newArr

        hash_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1
        newArr = []
        for i in hash_map:
            if hash_map[i] > n // 3:
                newArr.append(i)
        return newArr