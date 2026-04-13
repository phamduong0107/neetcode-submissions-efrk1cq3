class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        max_profits = 0
        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            else:
                profit = prices[i] - min_prices
                if profit > max_profits:
                    max_profits = profit
        return max_profits