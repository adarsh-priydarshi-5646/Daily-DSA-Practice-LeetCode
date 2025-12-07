class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        final = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[final] = nums[i]
                final += 1
        return final