class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import sys
        res = [1]
        idx = [0] * len(primes)

        for i in range(1, n):
            minValue = sys.maxsize
            for j in range(len(primes)):
                minValue = min(minValue, primes[j] * res[idx[j]])
            res.append(minValue)
            for j in range(len(primes)):
                while primes[j] * res[idx[j]] <= minValue:
                    idx[j] += 1
        return res[-1]

    def nthSuperUglyNumber2(self, n, primes):
        import sys
        res = []
        idx = [0] * len(primes)
        val = primes
        nextValue = 1
        for i in range(n):
            res.append(nextValue)
            nextValue = sys.maxsize
            for j in range(len(primes)):
                if val[j] == res[i]:
                    idx[j] += 1
                    val[j] = res[idx[j]] * primes[j]
                nextValue = min(nextValue, val[j])
        return res[-1]

    def nthSuperUglyNumber3(self, n, primes):
        import heapq
        res = [1]
        valIdx = [(val, idx, 0) for idx, val in enumerate(primes)]
        heapq.heapify(valIdx)
        for i in range(n-1):
            while valIdx[0][0] == res[i]:
                val, idx, resIdx = valIdx[0]
                heapq.heapreplace(valIdx, (primes[idx] * res[resIdx+1], idx, resIdx+1))
            res.append(valIdx[0][0])
        return res[n-1]

