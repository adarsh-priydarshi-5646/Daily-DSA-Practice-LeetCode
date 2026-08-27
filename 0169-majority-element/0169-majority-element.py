class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #better
        ele = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                ele = nums[i]
                count += 1
            elif nums[i] == ele:
                count += 1
            else:
                count -= 1
        return ele
        




        #better
        # hash_map = {}
        # for i in range(len(nums)):
        #     if nums[i] not in hash_map:
        #         hash_map[nums[i]] = 1
        #     else:
        #         hash_map[nums[i]] += 1
        # for num in hash_map:
        #     if hash_map[num] > len(nums)//2:
        #         return num

        #brute force
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        #     if count > len(nums)//2:
        #         return nums[i]
        