class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if profit < 0:
                buy = prices[i]
            max_profit = max(max_profit, profit)
        
        return max_profit