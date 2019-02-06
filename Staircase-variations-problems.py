"""
Given a set of ways of jumping stairs, writing a function 'num_ways' which take the positive integer N and returns the
number of ways that you can go from the bottom to the top.
"""

class Solution:
    def num_ways(self, N, X):
        return self.helper(N, X)

    def helper(self, N, X):
        if N < 0:
            return 0
        if N == 0 or N == 1:
            return 1
        return sum([self.helper(N-step, X) for step in X])

    def num_ways_bottom_up(self, N, X):
        if N == 0 or N == 1:
            return 1
        num = [0] * (N + 1)
        num[0] = 1; num[1] = 1
        for i in range(2, len(num)):
            for j in X:
                if i - j >=0:
                    num[i] += num[i-j]
                else:
                    break
        return num[N]


if __name__ == '__main__':
    X = [1, 2]
    N = 4
    solution = Solution()
    print(solution.num_ways_bottom_up(N, X))