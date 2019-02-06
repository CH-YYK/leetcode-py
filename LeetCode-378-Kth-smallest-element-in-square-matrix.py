class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ## max heap O(N^2log(K))
        import heapq
        heap = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])
                else:
                    if matrix[i][j] < -heap[0]:
                        heapq.heapreplace(heap, -matrix[i][j])
        return -heap[0]

    def kthSmallest2(self, matrix, k):
        """
        max heap
        """
        import heapq
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        res = 0
        heapq.heapify(heap)
        for _ in range(k):
            res, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return res
