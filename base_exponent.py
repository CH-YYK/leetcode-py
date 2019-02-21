# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        ans = 1
        for _ in range(abs(exponent)):
            ans = base * ans
        if exponent >= 0:
            return ans
        else:
            return 1/ans