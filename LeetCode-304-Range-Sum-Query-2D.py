class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row > 0 and col > 0:
                    matrix[row][col] += matrix[row - 1][col] + matrix[row][col - 1]
                    matrix[row][col] -= matrix[row - 1][col - 1]
                elif row == 0 and col > 0:
                    matrix[row][col] += matrix[row][col - 1]
                elif col == 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = self.matrix[row2][col2]
        area1 = self.matrix[row1 - 1][col2] if row1 > 0 else 0
        area2 = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        common = self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return total - (area1 + area2 - common)
