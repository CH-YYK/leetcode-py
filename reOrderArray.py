# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        even = []
        odd = []
        for num in array:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return odd + even

    def reOrderArray_free(self, array):
        end = len(array) - 1
        i = 0
        while i < end:
            if array[i] % 2 != 0:
                i += 1
            else:
                array[end], array[i] = array[i], array[end]
                end -= 1
        return array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print(Solution().reOrderArray(array))
    print(Solution().reOrderArray_free(array))