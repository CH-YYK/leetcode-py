# To do next time

class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        self.all = []
        self.dfs(0, 0, n, '')
        return self.all

    def dfs(self, i, j, n, comb):
        if i == n:
            self.all.append(comb + ')'* (n-j))
            return
        for k in range(i, n):
            if k <= n-2:
                self.dfs(k+2, j, n, '(' * (k-i) + comb + '((')
            self.dfs(k+1, j + 1, n, '(' * (k-i) + comb + '()')
        
if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))