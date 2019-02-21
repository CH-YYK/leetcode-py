class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        if A[0] * A[-1] > 0:
            return [i ** 2 for i in A] if A[0] >= 0 else [i ** 2 for i in A[::-1]]

        # find separator between positive and negative, O(N)
        i = 0
        while i < len(A) - 1 and A[i] * A[i+1] > 0:
            i += 1
        A = [i ** 2 for i in A]

        # merge to sorted array O(N)
        right, left, res = i, i+1, []
        while left < len(A) and right >= 0:
            if A[right] < A[left]:
                res.append(A[right])
                right -= 1
            else:
                res.append(A[left])
                left += 1

        while left < len(A):
            res.append(A[left])
            left += 1

        while right >= 0:
            res.append(A[right])
            right -= 1
        return res


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(A))