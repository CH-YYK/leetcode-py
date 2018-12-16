# by default fib(n) = fib(n-1) + fib(n-2) + fib(n-3) + ... + fib(n-n)
# and fib(n-1) = fib(n-2) + fib(n-3) + ... + fib(n-n)
# fib(n) = 2*fib(n-1)
class Solution:
    def jumpFloorII(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return 2*self.jumpFloorII(number-1)