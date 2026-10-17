class Solution:
    def calTotalHour(self, arr, hourly):
        totalHour = 0
        for x in arr:
            totalHour += math.ceil(x / hourly)
        return totalHour
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            totalHour = self.calTotalHour(piles, mid)
            if totalHour <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        