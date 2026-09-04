class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i + 1

        # s = set()
        # for i in nums:
        #     s.add(i)
        # index = 0
        # for i in sorted(s):
        #     nums[index] = i
        #     index += 1
        # return index
       

        