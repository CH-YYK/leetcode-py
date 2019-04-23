class Solution(object):
    def findKthLargest(self, nums, k): ## min Heap
        """
        O(N) + O((N-K)*logK)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return heapq.heappop(nums)

class Solution2:
    def findKthLargest2(self, nums, k):  ## quick select
        return self.findKthSmallest(nums, len(nums) - k + 1)

    def findKthSmallest(self, nums, k):
        if nums:
            pivot = self.partition(nums, 0, len(nums) - 1)
            if k > pivot + 1:
                return self.findKthSmallest(nums[pivot+1:], k-pivot-1)
            elif k < pivot + 1:
                return self.findKthSmallest(nums[:pivot], k)
            else:
                return nums[k]

    def partition(self, nums, left, right):
        i = left
        pivot = right
        for j in range(left, right):
            if nums[j] < nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i


