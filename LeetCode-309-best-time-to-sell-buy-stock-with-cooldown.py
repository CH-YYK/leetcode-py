
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = [0] * (len(prices)+2)
        sell = [0] * (len(prices)+2)
        buy[1] = -prices[0]
        for i in range(2, len(sell)):
            price = prices[i-2]
            buy[i] = max(sell[i-2]-price, buy[i-1])
            sell[i] = max(sell[i-1], buy[i-1]+price)
        return sell

    def maxProfit_modified(self, prices):
        if len(prices) < 2:
            return 0
        presell = sell = 0
        buy = -prices[0]
        for price in prices:
            prebuy = buy
            buy = max(presell - price, prebuy)
            presell = sell
            sell = max(presell, prebuy + price)
        return sell
