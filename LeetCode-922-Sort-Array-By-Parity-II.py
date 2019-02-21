class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        A.sort()
        i, j = 0, 1
        while i <= len(A) - 2:
            if A[i] % 2 == 0:
                i += 2
            else:
                while A[j] % 2 != 0:
                    j += 2
                A[i], A[j] = A[j], A[i]
                i += 2

        return A
