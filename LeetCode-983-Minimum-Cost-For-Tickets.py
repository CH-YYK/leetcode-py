class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> int:
        self.memo = {}
        return self.helper(days, 0, 0, costs)
    
    def helper(self, days, ind, maxday, costs):
        if ind == len(days):
            return 0

        if days[ind] <= maxday:
            return self.helper(days, ind+1, maxday, costs)
        else:
            maxday = days[ind] - 1
            res = []
            ds = [1, 7, 30]
            for i in range(len(ds)):
                if maxday + ds[i] >= days[ind]:
                    res.append(costs[i] + self.helper(days, ind+1, maxday+ds[i], costs))
            return min(res)
        
        