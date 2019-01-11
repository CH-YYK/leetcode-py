"""
You are given a matrix, implement an algorithms that return the longest consecutive increasing sequence
"""


class Solution:
    def longestUpPath(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        rows, cols = len(matrix), len(matrix[0])
        paths = []
        for i in range(rows):
            for j in range(cols):
                paths.append(self.dfs(matrix, i, j, [], rows, cols))
        return max(paths, key=len)

    def dfs(self, matrix, i, j, path, rows, cols):
        tmp = matrix[i][j]
        matrix[i][j] = 0
        all_sets = []
        if j+1 < cols and matrix[i][j+1] > tmp:
            all_sets.append(self.dfs(matrix, i, j+1, path+[tmp], rows, cols))
        if j-1 >= 0 and matrix[i][j-1] > tmp:
            all_sets.append(self.dfs(matrix, i, j-1, path+[tmp], rows, cols))
        if i-1 >= 0 and matrix[i-1][j] > tmp:
            all_sets.append(self.dfs(matrix, i-1, j, path+[tmp], rows, cols))
        if i+1 < rows and matrix[i+1][j] > tmp:
            all_sets.append(self.dfs(matrix, i+1, j, path+[tmp], rows, cols))

        matrix[i][j] = tmp
        if len(all_sets) == 0:
            return path + [tmp]
        else:
            all_sets.sort(key=lambda x:x[-1], reverse=True)
            return max(all_sets, key=len)

if __name__ == '__main__':
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 2, 1]
    ]
    print(Solution().longestUpPath(matrix))
