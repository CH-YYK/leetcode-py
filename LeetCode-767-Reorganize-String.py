class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import heapq
        hashmap = {}
        for i in S:
            hashmap[i] = hashmap.get(i, 0) + 1
        heap = [(-j, i) for i, j in hashmap.items()]
        heapq.heapify(heap)
        res = ""
        while heap:
            firstNum, firstChar = heapq.heappop(heap)
            if len(res) == 0 or firstChar != res[-1]:
                res += firstChar
                firstNum += 1
            elif heap:
                secondNum, secondChar = heapq.heappop(heap)
                res += secondChar
                secondNum += 1
                if secondNum < 0:
                    heapq.heappush(heap, (secondNum, secondChar))
            else:
                return ""
            if firstNum < 0:
                heapq.heappush(heap, (firstNum, firstChar))
        return res

    def reorganizeString2(self, S):
        hashmap = {}
        for i in S:
            hashmap[i] = hashmap.get(i, 0) + 1
        val, count = max(hashmap.items(), key=lambda x: x[1])
        if count > (len(S) + 1) / 2:
            return ""
        del hashmap[val]
        base = [val for _ in range(count)]
        l = len(base)
        i = 0
        for val, cnt in hashmap.items():
            while cnt:
                base[i] += val
                cnt -= 1
                i = (i+1) % l
        return "".join(base)


if __name__ == '__main__':
    S = "aab"
    print(Solution().reorganizeString2(S))