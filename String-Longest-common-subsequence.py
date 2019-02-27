class Solution:
    def longestCommonSubsequence(self, str1, str2):
        return self.dfs(str1, str2)
    
    def dfs(self, str1, str2):
        if not str1 or not str2:
            return ""
        if str1[0] == str2[0]:
            return str1[0] + self.dfs(str1[1:], str2[1:]) 
        else:
            return max(self.dfs(str1, str2[1:]), self.dfs(str1[1:], str2))

class Solution2:
    def longestCommonSubsequence(self, str1, str2):
        return self.dfs(str1, str2, 0, 0)

    def dfs(self, str1, str2, i, j):
        if i >= len(str1) or j >= len(str2):
            return ""
        if str1[i] == str2[j]:
            return str1[i] + self.dfs(str1, str2, i+1, j+1)
        else:
            return max(self.dfs(str1, str2, i+1, j), self.dfs(str1, str2, i, j+1))

if __name__ == "__main__":
    ans = Solution2().longestCommonSubsequence("hello world", "hello you")
    print(ans)