class Solution:
    def binarySearch(self, array, target):
        """
        Iterative solution
        """
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left+right) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def binarySearch2(self, array, target):
        # recursive solution
        return self.binarySearch_recur(array, 0, len(array)-1, target)

    def binarySearch_recur(self, array, left, right, target):
        if left > right:
            return -1
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return self.binarySearch_recur(array, mid+1, right, target)
        else:
            return self.binarySearch_recur(array, left, mid, target)


if __name__ == '__main__':
    array = [1, 2, 3, 5, 6]
    print(Solution().binarySearch2(array, 5))