class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for i in hash_map:
            if hash_map[i] == 1:
                return i
        return -1
        
        
        # num = 0
        # for i in range(len(nums)):
        #     cnt = 0
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             cnt += 1
        #     if cnt == 1:
        #         num = nums[i]
        # return num


        