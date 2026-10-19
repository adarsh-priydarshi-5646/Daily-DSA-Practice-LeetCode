class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        lo = min(bloomDay)
        hi = max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            bouq = 0
            flow = 0
            for d in bloomDay:
                if d <= mid:
                    flow += 1
                    if flow == k:
                        bouq += 1
                        flow = 0
                else:
                    flow = 0
            if bouq >= m:
                hi = mid
            else:
                lo = mid + 1
        return lo