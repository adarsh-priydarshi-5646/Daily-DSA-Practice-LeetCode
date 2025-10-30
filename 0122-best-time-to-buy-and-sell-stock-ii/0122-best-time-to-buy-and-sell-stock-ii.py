class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            # Agar kal ka price zyada hai aaj se, toh profit add karo
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit
        
        