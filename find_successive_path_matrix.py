class Solution:
    def all_paths(self, matrix):
        if len(matrix) == 0:
            return None
        if len(matrix[0]) == 0:
            return None

        paths = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                paths.append(self.find_path(matrix, i, j, rows, cols, []))
        return max(paths, key=len)

    def find_path(self, matrix, i, j, rows, cols, paths):
        tmp = matrix[i][j]
        matrix[i][j] = 0

        all_sets = []
        if j + 1 < cols and matrix[i][j + 1] > tmp:
            all_sets.append(self.find_path(matrix, i, j + 1, rows, cols, paths+[tmp]))
        if j - 1 >= 0 and matrix[i][j - 1] > tmp:
            all_sets.append(self.find_path(matrix, i, j - 1, rows, cols, paths+[tmp]))
        if i + 1 < rows and matrix[i + 1][j] > tmp:
            all_sets.append(self.find_path(matrix, i + 1, j, rows, cols, paths+[tmp]))
        if i - 1 >= 0 and matrix[i - 1][j] > tmp:
            all_sets.append(self.find_path(matrix, i - 1, j, rows, cols, paths+[tmp]))

        matrix[i][j] = tmp
        if len(all_sets) == 0:
            return paths + [tmp]
        else:
            return max(all_sets, key=len)


if __name__ == '__main__':
    m = [
        [4, 1, 3],
        [4, 7, 6],
        [8, 9, 10]
    ]
    print(Solution().all_paths(m))