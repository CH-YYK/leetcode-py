class Solution:
    def mergeSort(self, array):
        self.divideArray(array, 0, len(array)-1)
        return array

    def mergeArrays(self, array, l, m, r):
        # merge two sorted array l:m and m+1:r
        i, j = l, m + 1
        res = []
        while i <= m and j <= r:
            if array[i] < array[j]:
                res.append(array[i])
                i += 1
            else:
                res.append(array[j])
                j += 1
        res += array[i:m+1] if i <= m else array[j:r+1]
        array[l:r+1] = res

    def divideArray(self, array, l, r):
        if l < r:
            m = (l+r) // 2
            self.divideArray(array, l, m)
            self.divideArray(array, m+1, r)
            self.mergeArrays(array, l, m, r)


class Solution2:
    def mergeSort(self, array):
        self.mergesort(array, 0, len(array) - 1)
        return array

    def mergesort(self, array, l, r):
        if l < r:
            m = (l+r) // 2
            self.mergesort(array, l, m)
            self.mergesort(array, m+1, r)
            self.merge(array, l, m, r)

    def merge(self, array, l, m, r):
        res = array[l:r+1]
        left, right = 0, m+1-l
        curr = l
        while left <= m-l and right <= r-l:
            print(left, right, res)
            if res[left] < res[right]:
                array[curr] = res[left]
                left += 1
            else:
                array[curr] = res[right]
                right += 1
            curr += 1
        while left <= m-l:
            array[curr] = res[left]
            curr += 1
            left += 1
        while right <= r-l:
            array[curr] = res[right]
            curr += 1
            right += 1


if __name__ == '__main__':
    array = [38, 27, 43, 3, 9, 82, 10]
    print(Solution2().mergeSort(array))

