class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_cost = float('-inf')
        profit = 0
        prev_profit = 0
        for price in prices:
            if prev_profit > price + cur_cost:
                profit += prev_profit
                prev_profit = 0
                cur_cost = -price
                continue
            cur_cost = max(-price, cur_cost)
            prev_profit = max(prev_profit, price + cur_cost)
            # elif cur_cost < -price:
            #     cur_cost = -price
            # elif prev_profit < price + cur_cost:
            #     prev_profit = price + cur_cost
        profit += prev_profit
        return profit