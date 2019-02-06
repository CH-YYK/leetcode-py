class Solution:
    def quickSort(self, array):
        self.sorting(array, 0, len(array) - 1)
        return array

    def sorting(self, array, left, right):
        index = self.partition(array, left, right)
        if left < index - 1:
            self.sorting(array, left, index-1)
        if index < right:
            self.sorting(array, index, right)

    def partition(self, array, left, right):
        pivot = array[(left+right) // 2]
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return left


class Solution2:
    def quickSort(self, array):
        self.sorting(array, 0, len(array) - 1)
        return array

    def sorting(self, array, left, right):
        if left < right:
            pivot = self.partition(array, left, right)
            self.sorting(array, left, pivot-1)
            self.sorting(array, pivot+1, right)

    def partition(self, array, left, right):
        pivot = right
        i = left
        for j in range(left, right):
            if array[j] < array[pivot]:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[right] = array[right], array[i]
        return i


if __name__ == '__main__':
    array = [4, 3, 5, 2, 1, 7, 9 ,4 , 2]
    print(Solution().quickSort(array))