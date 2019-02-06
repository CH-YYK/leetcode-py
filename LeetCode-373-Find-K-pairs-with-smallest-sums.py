class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = []
        res = []
        if not nums1 or not nums2:
            return res
        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))

        # min(K, M*N)
        for j in range(min(k, len(nums1) * len(nums2))):
            sums, x, y = heapq.heappop(heap)
            res.append([nums1[x], nums2[y]])
            if y == len(nums2) - 1:
                continue
            heapq.heappush(heap, (nums1[x]+nums2[y+1], x, y+1))
        return res