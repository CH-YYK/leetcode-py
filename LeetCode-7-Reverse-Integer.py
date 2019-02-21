class Solution:
    def reverse(self, x: 'int') -> 'int':
        Sum = 0
        ind = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            print(Sum)
            Sum = Sum * 10 + ind * (x % 10)
            x //= 10
        return Sum if -2**31 <= Sum <= 2**31-1 else 0

if __name__ == '__main__':
    print(Solution().reverse(-321))