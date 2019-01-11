"""
one robot sitted at up-left corner of a grid, implement an algorithms to return
all paths that robot could reach the right-bottom corner
"""


class Solution:
    def robotInGrid(self, matrix):
        m, n = len(matrix), len(matrix[0])
        C = [[None for j in range(n)] for i in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    C[row][col] = 1
                elif matrix[row][col] == 0:
                    C[row][col] = 0
                else:
                    C[row][col] = C[row][col-1] + C[row-1][col]
        return C[-1][-1]

if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 1]
    ]
    print(Solution().robotInGrid(matrix))

