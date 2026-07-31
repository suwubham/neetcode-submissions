class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy_day, buy_price in enumerate(prices):
            for sell_day, sell_price in enumerate(prices):
                if buy_day < sell_day:
                    current_profit = sell_price - buy_price
                    if current_profit > max_profit:
                        max_profit = current_profit
        return max_profit

