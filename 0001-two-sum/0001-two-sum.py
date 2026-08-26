class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            a = nums[i]
            more = target - a
            if more in hash_map:
                return [hash_map[more], i]
            hash_map[a] = i
        return []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j

        