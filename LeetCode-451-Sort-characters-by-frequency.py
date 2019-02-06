class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(N) + O(logN) + O(N) = O(N+logN)
        import heapq
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        l = [(-j, i) for i, j in hashmap.items()]
        heapq.heapify(l)

        res = ''
        while l:
            freq, char = heapq.heappop(l)
            res += char * -freq
        return res

if __name__ == '__main__':
    s = 'tree'
    print(Solution().frequencySort(s))
