import sys

class Solution:
    def mincost(self, price, ticket, n, k):
        self.price = price
        self.ticket = ticket
        self.k = k
        return self.dfs(n+1)
    
    def dfs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return min(ticket)
        currmin = sys.maxsize
        for i in range(len(self.price)):
            if n < self.ticket[i]:
                continue
            currmin = min(currmin, self.price[i] + self.dfs(n-self.ticket[i]))
        return currmin

price = [5, 6, 13]
ticket = [1, 2, 3]

if __name__ == "__main__":
    print(Solution().mincost(price, ticket, 2, 5))