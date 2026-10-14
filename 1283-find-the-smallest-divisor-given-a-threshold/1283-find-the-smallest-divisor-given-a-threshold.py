class Solution:
    def sumByD(self, nums ,div):
        summ = 0
        for num in nums:
            summ += math.ceil(num / div)
        return summ
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if self.sumByD(nums, mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans