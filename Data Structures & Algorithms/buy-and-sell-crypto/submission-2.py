class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        profit = 0
        min_price = prices[0]

        while j < len(prices):
            min_price = min(min_price, prices[j])
            if min_price <= prices[j]:
                curr_profit = prices[j] - min_price
                if profit < curr_profit:
                    profit = max(profit, curr_profit)
            j+= 1


        return profit


