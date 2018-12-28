# -*- coding:utf-8 -*-

"""
    Find the frequency of k in data. and
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 1 and data[0] == k:
            return 1
        i, j = 0, len(data)-1
        while i < j:
            if data[i] < k:
                i += 1
            if data[j] > k:
                j -= 1
            if data[i]== k and data[j] == k:
                return j-i+1
        return 0