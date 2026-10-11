class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        ans = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= ans:
                left = mid + 1
            else:
                ans = nums[mid]
                right = mid - 1
        return ans




