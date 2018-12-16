# 1 step or 2 steps a time, how many ways to access nth step
# n = 0 -> 0, n = 1 -> 1, n = 2 -> 2, let fib(n) define the # of ways to access nth step
# n = 3, first to 1, left fib(2), first to 2, left fib(1) --> fib(3) = fib(1) + fib(2)
# fib(n) = fib(n-1) + fib(n-2)

class Solution:
    def jumpFloor(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            result = [0, 1, 2] + [0 for i in range(number-2)]
            for i in range(3, number+1):
                result[i] = result[i-1] + result[i-2]
            return result[number]