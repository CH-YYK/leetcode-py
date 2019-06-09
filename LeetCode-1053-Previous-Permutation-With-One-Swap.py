class Solution:
    def prevPermOpt1(self, A: 'List[int]') -> 'List[int]':
        n = len(A)

        i = n-1
        while i > 0 and A[i-1] <= A[i]:
            i -= 1
        
        if i == 0:
            return A 
        
        j = i-1
        
        k = n-1
        while k > i and A[k] > A[j] or A[k] == A[k-1]:
            k -= 1
        A[k], A[j] = A[j], A[k]
        return A