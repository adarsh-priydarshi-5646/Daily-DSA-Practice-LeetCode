class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_nums = {} 
        for num in nums:
            if num in hash_nums:
                hash_nums[num] += 1
            else:
                hash_nums[num] = 1
        for num in nums:
            if hash_nums[num] == 1:
                return num    
        return -1

        # result = 0
        # for num in nums:
        #     result ^= num  # This cancels out all duplicate pairs
        # return result

        # for i in range(len(nums)):
        #     num = nums[i]
        #     cnt = 0
        #     for j in range(len(nums)):
        #         if nums[j] == num:
        #             cnt += 1
        #     if cnt == 1:
        #         return num
        