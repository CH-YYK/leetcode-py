class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if (numerator // abs(numerator)) * (denominator // abs(denominator)) < 0:
            sign = '-'
        else:
            sign = ''
        numerator = abs(numerator)
        denominator = abs(denominator)


        history = {}
        ans = str(numerator // denominator)
        ans += '.'
        numerator = numerator % denominator * 10

        if numerator == 0:
            return sign + ans[:-1]

        i = len(ans)
        while numerator not in history:
            history[numerator] = i
            ans += str(numerator // denominator)
            if numerator % denominator == 0:
                return sign + ans
            numerator = numerator % denominator * 10
            i += 1
        left = history[numerator]
        return sign + ans[:left] + '(' + ans[left:] + ')'

if __name__ == "__main__":
    print(Solution().fractionToDecimal(4, 2))
        