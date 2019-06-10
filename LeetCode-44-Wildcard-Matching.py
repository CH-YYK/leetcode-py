class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, 0, 0)

    def helper(self, s, p, i, j):
        if i == len(s):
            if j == len(p):
                return True
            elif p[j] == '*':
                return self.helper(s, p, i, j+1)
            else:
                return False

        if j == len(p):
            return False
        
        if p[j] == '?' or s[i] == p[j]:
            return self.helper(s, p, i+1, j+1)
        elif p[j] == '*':
            return self.helper(s, p, i+1, j) or self.helper(s, p, i+1, j+1) or self.helper(s, p, i, j+1)
        else:
            return False

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = [[-1 for i in range(len(p)+1)] for _ in range(len(s)+1)]
        return self.helper(s, p, 0, 0) == 1

    def helper(self, s, p, i, j):
        if self.memo[i][j] > 0:
            return self.memo[i][j]

        if i == len(s):
            if j == len(p):
                return 1
            elif p[j] == '*':
                self.memo[i][j] = self.helper(s, p, i, j+1)
            else:
                self.memo[i][j] = 0
            return self.memo[i][j]
        
        if j == len(p):
            return 0

        if p[j] == '?' or s[i] == p[j]:
            self.memo[i][j] = self.helper(s, p, i+1, j+1)
        elif p[j] == '*':
            self.memo[i][j] = (self.helper(s, p, i+1, j) | self.helper(s, p, i+1, j+1)) | self.helper(s, p, i, j+1)
        else:
            self.memo[i][j] = 0
        return self.memo[i][j]

class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for i in range(len(p)+1)] for _ in range(len(s) + 1)]
        dp[0][0] = 1
        for i in range(0, len(s)+1):
            for j in range(1, len(p)+1):
                if i == 0:
                    dp[i][j] = 1 and dp[i][j-1] if p[j-1] == '*' else 0
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j-1] | dp[i-1][j] | dp[i][j-1]  # 1 char | >1 chars | 0 char
        return dp[len(s)][len(p)] == 1

class Solution4:
    def isMatch(self, s, p):
        """
        greedy algorithms: 
            suppose p is composed by segments of substrings where '?' represent any charaters
            substrings are separated by '*'
            
            For each substring:
                try to pair the substring with the s
                if not match: 
                    shift one step right from '*'
                if match:
                    navigate to the next substring.
            if all substrings matched s --> return True.
        """
        p_cur = 0
        s_cur = 0
        star = -1
        match = 0
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur += 1
            elif star != -1:
                p_cur = star + 1
                match = match + 1
                s_cur = match
            else:
                return False
        while p_cur < len(p) and p[p_cur] == '*':
            p_cur += 1
        if p_cur == len(p):
            return True
        else:
            return False

if __name__ == "__main__":
    s = "aa"
    p = "a*"
    ans = Solution3().isMatch(s, p)
    print(ans)
