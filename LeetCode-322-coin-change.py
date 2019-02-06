class Solution(object):
    def coinChange(self, coins, amount):  # recursive solution
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.helper(coins, amount)

    def helper(self, coins, amount):
        if amount == 0:
            return 0
        res = []
        for coin in coins:
            if amount >= coin:
                tmp = self.helper(coins, amount-coin)
                if tmp != -1:
                    res.append(tmp)
        return min(res) + 1 if res else -1

    def coinChange2(self, coins, amount):  # recursive solution with memo
        memo = [None] * amount
        return self.helper2(coins, amount, memo)

    def helper2(self, coins, amount, memo):
        if amount == 0:
            return 0
        if memo[amount-1] is not None:
            return memo[amount-1]

        res = []
        for coin in coins:
            if amount >= coin:
                tmp = self.helper2(coins, amount - coin, memo)
                if tmp != -1:
                    res.append(tmp)
        memo[amount-1] = min(res)+1 if res else -1
        return memo[amount-1]

    def coinChange3(self, coins, amount):  # dynamic programming
        memo = [-1] * (amount + 1)
        memo[0] = 0
        for i in range(len(memo)):
            res = []
            for coin in coins:
                if i >= coin and memo[i-coin] != -1:
                    res.append(memo[i-coin])
            memo[i] = min(res) + 1 if res else -1
        return memo[amount]
