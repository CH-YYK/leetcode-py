class Solution:
    def solveNQueens(self, n: int) -> 'List[List[str]]':
        self.col = [False] * (2*n - 1)
        self.diagup = [False] * (2 * n - 1)
        self.diagdown = [False] * (2 * n - 1)
        self.count = []
        self.n = n

        # create a board
        self.board = [["." for i in range(n)] for j in range(n)]
        self.placeQueen(0, n)
        return self.count

    def updateBoard(self, x, y, place):
        self.col[x] = place
        self.diagup[x+y] = place
        self.diagdown[x-y+self.n-1] = place
        self.board[y][x] = 'Q' if place else '.'

    def isavailable(self, x, y, n):
        return self.col[x] or self.diagup[x+y] or self.diagdown[x-y+n-1]

    def placeQueen(self, y, n):
        if y >= n:
            self.count.append(["".join(i) for i in self.board])
            return 
        for x in range(0, n):
            if self.isavailable(x, y, n):
                continue
            self.updateBoard(x, y, True)
            self.placeQueen(y+1, n)
            self.updateBoard(x, y, False)

if __name__ == "__main__":
    print(Solution().solveNQueens(4))