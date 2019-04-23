class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        self.record = [[-1] * n for i in range(m)]
        max_num = 0
        for i in range(m):
            for j in range(n):
                tmp = self.dfs(matrix, i, j)
                max_num = max(tmp, max_num)
        return max_num + 1
        
    def dfs(self, matrix, i, j):
        if self.record[i][j] >= 0:
            return self.record[i][j]

        res = []
        if i > 0 and matrix[i][j] > matrix[i-1][j]:
            res.append(self.dfs(matrix, i-1, j))
        if i < len(matrix)-1 and matrix[i][j] > matrix[i+1][j]:
            res.append(self.dfs(matrix, i+1, j))
        if j > 0 and matrix[i][j] > matrix[i][j-1]:
            res.append(self.dfs(matrix, i, j-1))
        if j < len(matrix[0]) - 1 and matrix[i][j] > matrix[i][j+1]:
            res.append(self.dfs(matrix, i, j+1))
        if not res:
            self.record[i][j] = 0
            return 0
        else:
            self.record[i][j] = max(res) + 1
            return self.record[i][j] 