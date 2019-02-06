class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.K = k
        self.nums = sorted(nums, reverse=True)
        self.subset = self.nums[:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.subset) < self.K:
            self.subset.append(val)
            self.subset.sort(reverse=True)
        elif val > self.subset[-1]:
            self.subset[-1] = val
            self.subset.sort(reverse=True)
        return self.subset[-1]


import heapq
class KthLargest2(object):  # Heap
    def __init__(self, k, nums):
        self.K = k
        self.subset = nums
        heapq.heapify(self.subset)
        while len(self.subset) > self.K:
            heapq.heappop(self.subset)

    def add(self, val):
        if len(self.subset) < self.K:
            heapq.heappush(self.subset, val)
        elif val > self.subset[0]:
            heapq.heapreplace(self.subset, val)
        return self.subset[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)