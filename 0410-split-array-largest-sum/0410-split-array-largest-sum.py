class Solution:
    def isValid(self, nums, mid, k):
        count = 1
        total = 0
        for num in nums:
            if total + num > mid:
                count += 1
                total = num
            else:
                total += num
        return count <= k
        
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.isValid(nums, mid, k):
                right = mid - 1
            else:
                left = mid + 1
        return left



        