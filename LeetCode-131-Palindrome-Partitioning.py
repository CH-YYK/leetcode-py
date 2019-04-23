class Solution:
    def partition(self, s: str) -> 'List[List[str]]':
        return self.dfs(s, len(s) - 1)
    
    def dfs(self, s, i):
        if i < 0:
            return [[]]
        if i == 0:
            return [[s[i]]]
        res = []
        for l in range(1, i+1+1):
            if self.is_palindrom(s[i-l+1: i+1]):
                tmp = self.dfs(s, i-l)
                for j in tmp:
                    j.append(s[i - l + 1:i+1])
                res += tmp
        if not res:
            return [[]]
        return res

    def is_palindrom(self, s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    ans = Solution().dfs('efe', 2)
    print(ans)