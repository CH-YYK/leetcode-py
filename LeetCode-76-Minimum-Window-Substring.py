class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        This function only work when there's no duplicated characters in t
        """
        cache = {c : -1 for c in t}
        k = len(cache)

        l = 0
        res = ""
        for r in range(len(s)):
            if s[r] in cache:
                if cache[s[r]] == -1:
                    k -= 1
                cache[s[r]] = r
                l = min(val for val in cache.values() if val >= 0)
                if k == 0 and not res:
                    res = s[l : r+1]
                elif res and r - l + 1 < len(res):
                    res = s[l : r+1]
        return res

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        """
        beats 14% in python.
        """
        cache = {}
        for c in t:
            cache[c] = cache.get(c, 0) + 1
        K = len(t)
        
        record = {c:[] for c in cache}

        l = 0
        lft, rht = 0, len(s) - 1
        for r in range(len(s)):
            if s[r] in cache:
                if len(record[s[r]]) < cache[s[r]]:
                    record[s[r]].append(r)
                    K -= 1
                else:
                    record[s[r]].pop(0)
                    record[s[r]].append(r)
                
                
                l = min(lis[0] for lis in record.values() if lis)

                if K == 0 and r - l < rht - lft:
                    lft, rht = l, r
        return s[lft: rht+1] if K == 0 else ""


if __name__ == "__main__":
    print(Solution().minWindow())
                    
