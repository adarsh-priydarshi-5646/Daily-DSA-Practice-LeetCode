class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_nums = nums
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        
        while left < right:
            summ = nums[left] + nums[right]
            if summ == target:
                idx1 = original_nums.index(nums[left])
                if nums[left] == nums[right]:
                    idx2 = original_nums.index(nums[right], idx1 + 1)
                else:
                    idx2 = original_nums.index(nums[right])
                return [idx1, idx2]
            elif summ < target:
                left += 1
            else:
                right -= 1         
        return []


        # hash_map = {}
        # for i in range(len(nums)):
        #     a = nums[i]
        #     more = target - a
        #     if more in hash_map:
        #         return [hash_map[more], i]
        #     hash_map[a] = i
        # return []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j

        