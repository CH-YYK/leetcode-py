"""
You are given an array and 2 integers, partition the array into three parts
according to the integers
"""


class Solution:
    def threeWayPartition(self, array, a, b):
        start = 0
        i = 0
        end = len(array) - 1
        while i < len(array):
            if array[i] < a:
                array[start], array[i] = array[i], array[start]
                start += 1
                i += 1
            elif array[i] > b:
                array[i], array[end] = array[end], array[i]
                end -= 1
            else:
                i += 1
        return array


if __name__ == '__main__':
    array = [1, 4, 3, 2, 5, 9, 0, 3]
    print(Solution().threeWayPartition(array, 4, 7))
