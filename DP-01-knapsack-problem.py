"""
The classic knapsack problem with O(nW) runtime and O(nW) space
        or O(nW) runtime and O(W) space
"""

class Solution:
    def knapsack(self, values, weights, n, w):
        """
        values: values of items
        weights: weights of items
        n,W: "size of items" and "maximum size of weights"
        """
        
        # O(nW) in time, and O(nW) in space
        # Define the matrix for dp[i][j]:= max values formed by first i-1 items 
        # limited under weight of j.
        dp = [[0 for i in range(W+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for w in range(1, W+1):
                dp[i][w] = dp[i-1][w] # didn't include (i-1)th item
                if weights[i-1] <= W:
                    dp[i][w] = max(dp[i][w], # include (i-1)th item
                                    values[i-1] + dp[i-1][w-weights[i-1]])
        return dp[n][W]

class Solution2:
    def knapsack(self, values, weights, n, w):
        # O(nW) in time, O(W) space
        dp = [0 for i in range(W+1)]
        for i in range(0, n):
            for w in range(W, weights[i]-1, -1):
                dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
        return dp[W]

    
        