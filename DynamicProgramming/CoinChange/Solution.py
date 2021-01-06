import sys


class Solution:
    def coin_change(self, coins: list, amount: int) -> int:
        least_coins = [None for _ in range(amount + 1)]
        return self.opt(least_coins, amount, coins)

    def opt(self, least_coins: list, curr_val: int, coins: list):
        # base cases
        if curr_val < 0:
            return -1
        if curr_val == 0:
            return 0
        if least_coins[curr_val] is not None:
            return least_coins[curr_val]
        # optimal recursive relation
        lowest = sys.maxsize
        for c in coins:
            # optimal coins for value after subtracting
            num = self.opt(least_coins, curr_val - c, coins)
            # watch out for case where none of the values are possible to make
            if 0 <= num < lowest:
                # add the current used coin to the most optimal coins for value after subtracting
                lowest = num + 1
        # if no coin changes are possible, then set -1 for the current amount
        if lowest == sys.maxsize:
            least_coins[curr_val] = -1
        else:
            least_coins[curr_val] = lowest

        return least_coins[curr_val]
