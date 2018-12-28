"""
You are given am integer as an upper bound, N, the task is to build a function that return
all primes under N
"""


class Solution:
    def primesUnderN(self, N):
        primes_list = [True] * (N+1)
        for i in range(2, N+1):
            if primes_list[i]:
                for k in range(2*i, N+1, i):
                    if primes_list[k]:
                        primes_list[k] = False
        return [index+2 for index, number in enumerate(primes_list[2:]) if number]


if __name__ == '__main__':
    solution = Solution()
    print(solution.primesUnderN(100))