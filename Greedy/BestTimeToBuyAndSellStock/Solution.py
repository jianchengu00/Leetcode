import sys


class Solution:
    def max_profit(self, prices: list) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            # always pick the smallest buy price
            if prices[i] < min_price:
                min_price = prices[i]
            # if price is larger than current min price, then try to sell it and check how much profit
            # update max_profit only when we can find a bigger profit with the current smallest buy price
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
