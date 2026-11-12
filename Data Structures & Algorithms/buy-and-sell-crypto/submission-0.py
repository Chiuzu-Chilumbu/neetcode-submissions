class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # declare variables 
        max_profit = 0
        smallest_price = float('inf')

        # traverse prices 
        for price in prices:
            # obtain smallest price 
            smallest_price = min(price, smallest_price)

            # calculate profict
            current_profit = price - smallest_price

            # update max proft 
            max_profit = max(current_profit, max_profit)

        return max_profit