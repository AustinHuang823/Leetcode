
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float("inf")
        for n in prices:
            low = min(n, low)
            profit = max(n - low, profit)
        return profit