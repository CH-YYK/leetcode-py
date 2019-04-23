import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = collections.Counter(s)
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1