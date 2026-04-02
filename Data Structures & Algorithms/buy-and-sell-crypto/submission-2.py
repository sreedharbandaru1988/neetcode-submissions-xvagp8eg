class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(1, len(prices)):
            if prices[R] <= prices[L]:
                L = R
                R += 1
            elif prices[R] > prices[L]:
                profit = max(profit, prices[R]-prices[L])
                R += 1
        return profit

        