# given a-> '1' b -> '2' ---- z -> '26'
# create a function that return number of strings that a data could be matched


class Solution:
    def number_ways(self, data):
        return self.recur_match(data, len(data))

    def recur_match(self, data, k):
        if k == 0:
            return 1
        s = len(data) - k
        if data[s] == '0':
            return 0
        result = self.recur_match(data, k-1)
        if k >= 2 and int(data[s:s+2]) <= 26:
            result += self.recur_match(data, k-2)
        return result

# dynamic programming and memorization
class Solution_dp:
    def number_ways_dp(self, data):
        memo = [None] * len(data)
        return self.recur_match_dp(data, len(data), memo)


    def recur_match_dp(self, data, k, memo):
        if k == 0:
            return 1
        s = len(data) - k
        if data[s] == '0':
            return 0
        if memo[k-1]:
            return memo[k-1]
        result = self.recur_match_dp(data, k-1, memo)
        if k >= 2 and int(data[s:s+2]) <= 26:
            result += self.recur_match_dp(data, k-2, memo)
        memo[k-1] = result
        return result


if __name__ == '__main__':
    print(Solution().number_ways('121'))
    print(Solution_dp().number_ways_dp('121'))