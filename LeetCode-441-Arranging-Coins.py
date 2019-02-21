class Solution:
    def arrangeCoins(self, n: 'int') -> 'int':
        # Iterative method O(N)
        i = 1
        while i*(i+1)// 2 <= n:
            i += 1
        return i-1

    def arrangeCoins2(self, n):
        # binary search
        l, r = 1, n+1
        while l < r:
            m = (l + r) // 2
            if m * (m + 1) // 2 == n:
                return m
            elif m * (m + 1) // 2 < n:
                l = m + 1
            else:
                r = m
        return l-1

    def arrangeCoins3(self, n):
        # mathematical way
        return int(((8 * n + 1) ** (1/2) - 1) / 2)