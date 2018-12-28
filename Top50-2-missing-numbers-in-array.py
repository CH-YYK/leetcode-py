"""
Given a ordered array which should be a list of successive numbers, find the missing numbers in the list
"""


class Solution:
    # case for only 1 missing number
    def MissingNumber_1(self, array):
        N = array[-1]
        return N*(N+1)/2 - sum(array)

    # case for two missing numbers
    def MissingNumber_2_avg(self, array):
        N = array[-1]
        total_diff = N*(N+1)/2 - sum(array)
        average = total_diff // 2

        smallersum, greatersum = 0, 0
        for num in array:
            if num <= average:
                smallersum += num
            else:
                greatersum += num

        # smaller missing number and greater missing number
        smaller = average * (average+1)/2 - smallersum
        greater = (N-average) * (N+average+1) / 2 - greatersum
        return int(smaller), int(greater)

    def MissingNumber_2_xor(self, array):
        N = array[-1]


if __name__ == '__main__':
    print(Solution().MissingNumber_2_avg([1, 2, 5]))

