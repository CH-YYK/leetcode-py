"""
    Find the size of the largest square of 1's from the Matrix.
"""


class Solution:
    def largestSquareOf_1(self, m):
        if len(m) == 0:
            return 0
        if len(m[0]) == 0:
            return 0

        C = [[j for j in i] for i in m]
        # update count matrix
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i == 0 or j == 0:
                    C[i][j] = m[i][j]
                elif m[i][j] == 0:
                    C[i][j] = 0
                else:
                    C[i][j] = min(C[i-1][j], C[i][j-1], C[i-1][j-1]) + 1

        # find the maximum value
        maximum = 0
        for i in C:
            maximum = max(maximum, max(i))
        return maximum

if __name__ == '__main__':
    m = [
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1]
    ]
    print(Solution().largestSquareOf_1(m))