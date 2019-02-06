class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import heapq
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1

        heap = [(-j, i) for i, j in hashmap.items()]
        heapq.heapify(heap)
        res = []
        while len(res) < k and heap:
            res.append(heapq.heappop(heap)[1])
        return res