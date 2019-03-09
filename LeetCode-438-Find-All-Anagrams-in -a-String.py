class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        l = r = 0
        hashmap = {}
        res = []
        for i in p:
            hashmap[i] = hashmap.get(i,0) + 1
        matchsize = len(hashmap)
        while r < len(s):
            if s[r] in hashmap:
                hashmap[s[r]] -= 1
                if hashmap[s[r]] == 0:
                    matchsize -= 1
            r += 1
            while matchsize == 0:
                if r - l == len(p):
                    res.append(l)
                if s[l] in hashmap:
                    hashmap[s[l]] += 1
                    if hashmap[s[l]] > 0:
                        matchsize += 1
                l += 1
        return res

if __name__ == "__main__":
    print(Solution().findAnagrams('cbaebabacd', 'abc'))