"""
You are given a array, build a function to reverse the order by array manipulation
without creating a new one
"""


class Solution:
    def reverseOrder(self, array):
        i = 0
        j = len(array) - 1
        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        return array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    ans = Solution().reverseOrder(array)
    print(ans)