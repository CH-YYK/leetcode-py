class Solution:
    def minCostClimbingStairs(self, cost):   ## recursive
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        return self.recur(cost, len(cost)-1)

    def recur(self, cost, index):
        if index < 0:
            return 0
        return max(self.recur(cost, index-1), self.recur(cost, index-2)) + cost[index]

    def minCostClimbingStairs2(self, cost):   ## recursive with memo
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        memo = [-1] * len(cost)
        return self.recur(cost, len(cost) - 1, memo)

    def recur(self, cost, index, memo):
        if index < 0:
            return 0
        if memo[index] >= 0:
            return memo[index]
        memo[index] = min(self.recur(cost, index - 1, memo) + cost[index],
                          self.recur(cost, index - 2, memo) + cost[index])
        return memo[index]