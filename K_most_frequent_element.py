"""
    Find the K most frequent element in array.
"""


class Solution:
    def FreqK(self, num_list, k):
        freq_hash = {}
        bucket = {}

        # update frequency hashmap
        for i, num in enumerate(num_list):
            if num in freq_hash:
                freq_hash[num] += 1
            else:
                freq_hash[num] = 1
            bucket[i+1] = []

        # update element hashmap
        for num in freq_hash:
            freq = freq_hash[num]
            bucket[freq].append(num)

        lis = []
        for i in range(len(bucket), 0, -1):
            if bucket[i]:
                lis += bucket[i]
            if len(lis) == k:
                return lis

if __name__ == '__main__':
    num_list = [1, 6, 2, 1, 6, 1, 6]
    k = 2
    print(Solution().FreqK(num_list, 2))