class Solution:
    def nthUglyNumber(self, n):
        """
        Three pointers method.
        """
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i = j = k = 0
        while n > 1:
            num_i, num_j, num_k = res[i] * 2, res[j] * 3, res[k] * 5
            minNum = min(num_i, num_j, num_k)
            res.append(minNum)
            if num_i == minNum:
                i += 1
            if num_j == minNum:
                j += 1
            if num_k == minNum:
                k += 1
            n -= 1
        return res[-1]