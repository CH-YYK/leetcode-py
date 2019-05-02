class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        memo = {}
        seen = set()
        return self.dfs(pattern, string, memo, seen)

    def dfs(self, pattern, string, memo, seen):
        if len(pattern) == 0 and len(string) == 0:
            return True
        if len(pattern) == 0 or len(string) == 0:
            return False
        if pattern[0] in memo:
            p = memo[pattern[0]]
            return p == string[:len(p)] and self.dfs(pattern[1:], string[len(p):], memo, seen)
        
        for i in range(1, len(string) - len(pattern) + 2):
            if string[:i] in seen:
                continue
            memo[pattern[0]] = string[:i]
            seen.add(string[:i])
            if self.dfs(pattern[1:], string[i:], memo, seen):
                return True
            del memo[pattern[0]]
            seen.remove(string[:i])
        return False

class Solution2:
     """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        memo = {}
        seen = set()
        return self.dfs(pattern, string, 0, 0, memo, seen)

    def dfs(self, pattern, string, i, j, memo, seen):
        if i == len(pattern) and j == len(string):
            return True
        if len(pattern) == i or len(string) == j:
            return False
        
        if pattern[i] in memo:
            p = memo[pattern[i]]
            return p == string[j:j+len(p)] and self.dfs(pattern, string, i+1, j+len(p), memo, seen)
        
        for k in range(1, len(string) - j - len(pattern) + i + 2):
            if string[j:j+k] in seen:
                continue
            memo[pattern[i]] = string[j:j+k]
            seen.add(string[j:j+k])
            if self.dfs(pattern, string, i+1, j+k, memo, seen):
                return True
            del memo[pattern[i]]
            seen.remove(string[j:j+k])
        return False


if __name__ == "__main__":
    print(Solution2().wordPatternMatch('abab', 'redblueredblue'))
    print(Solution2().wordPatternMatch('aaaa', 'asdasdasdasd'))
    print(Solution2().wordPatternMatch('aabb', 'xyzabcxzyabc'))