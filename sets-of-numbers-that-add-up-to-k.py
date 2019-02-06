class Solution:
    def setofnumbers(self, array, K):
        return self.recur(array, K, len(array)-1)

    def recur(self, array, K, index):
        if K == 0:
            return 1
        if K < 0:
            return 0
        if index < 0:
            return 0
        if K < array[index]:
            return self.recur(array, K, index-1)
        else:
            return self.recur(array, K-array[index], index-1) + self.recur(array, K, index-1)