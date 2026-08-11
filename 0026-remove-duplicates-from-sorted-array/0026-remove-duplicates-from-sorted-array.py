class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])
        index = 0
        for i in sorted(s):
            nums[index] = i
            index += 1
        return index
