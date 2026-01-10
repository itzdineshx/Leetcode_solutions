class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0  # Initialize max profit

        for price in prices:
            # Update the minimum price -> current price is lower
            if price < min_price:
                min_price = price

            # Calculate profit if selling on this day and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit