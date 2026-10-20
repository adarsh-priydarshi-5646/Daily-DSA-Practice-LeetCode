class Solution:
    def findDays(self, weights, capacity):
        days = 1
        load = 0
        for weight in weights:
            if weight + load <= capacity:
                load += weight
            else:
                days += 1
                load = weight
        return days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        while lo <= hi:
            mid = (lo + hi) // 2
            numberOfdays = self.findDays(weights, mid)
            if numberOfdays <= days:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

        