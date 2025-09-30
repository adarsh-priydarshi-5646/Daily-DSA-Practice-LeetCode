class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Initialize min_price as infinity (bahut bada number) & max_profit as 0
        min_price = float('inf')  # ab tak ka sabse chhota price
        max_profit = 0            # ab tak ka max profit

        # Step 2: Loop through each price
        for price in prices:
            # Agar current price ab tak ka minimum hai, toh update karo
            if price < min_price:
                min_price = price
            # warna calculate karo profit agar hum aaj sell karte
            else:
                profit = price - min_price
                # agar naya profit zyada hai, toh max_profit update karo
                if profit > max_profit:
                    max_profit = profit

        # Step 3: Return the maximum profit found
        return max_profit
        