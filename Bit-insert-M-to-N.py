def printBinary(num):
    print("{0:b}".format(num))


class Solution:
    def insertMtoN(self, M, N, i):
        mask_M = ((M & M) << i)
        mask_N = (N & N)
        mask = mask_M ^ mask_N
        return (N & mask) | (M << i)

if __name__ == '__main__':
    N = 2 ** 10
    M = 19
    printBinary(N)
    printBinary(M)
    ans = Solution().insertMtoN(M, N, i=2)
    print("{0:b}".format(ans))