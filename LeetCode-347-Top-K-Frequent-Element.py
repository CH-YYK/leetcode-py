import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 1) + 1

        heap = [(j, i) for i, j in hashmap.items()]
        heapq.heapify(heap)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res