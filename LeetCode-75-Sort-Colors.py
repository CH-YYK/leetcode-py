class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        self.divideList(nums, 0, len(nums)-1)

    def mergeList(self, array, l, m, r):
        if l <= m and m+1 <= r:
            if array[l] <= array[m+1]:
                self.mergeList(array, l+1, m, r)
            else:
                tmp = array[m+1]
                for i in range(m+1, l, -1):
                    array[i] = array[i-1]
                array[l] = tmp
                self.mergeList(array, l+1, m+1, r)

    def divideList(self, array, l, r):
        if l < r:
            m = (l+r) // 2
            self.divideList(array, l, m)
            self.divideList(array, m+1, r)
            self.mergeList(array, l, m, r)

if __name__ == '__main__':
    nums = [1,3,4,2]
    Solution().sortColors(nums)
    print(nums)