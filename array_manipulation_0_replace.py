"""
you are given an array containing zeros, the task is write a function that
move all zeros to the end and return the same array
"""


class Solution:
    def moveZerosEnd(self, array):
        j = 0
        for i in range(len(array)):
            if array[i] == 0:
                j = self.find_non_zero(max(i, j), array)
                if j < len(array):
                    array[i], array[j] = array[j], array[i]
            else:
                continue
        return array

    def find_non_zero(self, i, array):
        while i < len(array) and array[i] == 0:
            i += 1
        return i

    def moveZerosEnd_unorder(self, array):
        i = 0
        j = len(array) - 1
        while i < j:
            if array[j] == 0:
                j -= 1
            elif array[i] == 0:
                array[i], array[j] = array[j], array[i]
                j -= 1
                i += 1
            else:
                i += 1
        return array

if __name__ == '__main__':
    array = [0, 1, 2, 0, 3, 0]
    ans = Solution().moveZerosEnd_unorder(array)
    assert id(array) == id(ans)
    print(ans)
