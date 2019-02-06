class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    matrix[row][col] = int(matrix[row][col])
                else:
                    tmp = min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1])
                    matrix[row][col] = tmp + 1 if matrix[row][col] == '1' else 0
        side = max([max(i) for i in matrix])
        return side ** 2