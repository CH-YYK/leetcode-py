class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        """
        recursive solution O(2^N), O(1)
        either include ith string or skip ith string
        """
        return self.helper(strs, m, n, 0)

    def helper(self, strs, m, n, i):
        if i == len(strs) or (m <= 0 and n <= 0):
            return 0
        n1, m0 = self.computeOneZero(strs[i])
        
        if m - m0 >= 0 and n-n1 >=0:
            return max(self.helper(strs, m-m0, n-n1, i+1) + 1, 
                    self.helper(strs, m, n, i+1))
        else:
            return self.helper(strs, m, n, i+1)
    
    def computeOneZero(self, string):
        ones = sum([int(i) for i in string])
        return ones, len(string) - ones


class Solution2:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        """
        recursive solution with memoization (top-down) O(m*n*N)
        """
        memo = {}
        return self.helper(strs, m, n, 0, memo)

    def helper(self, strs, m, n, i, memo):
        if i == len(strs) or (m <= 0 and n <= 0):
            return 0
        if (m,n,i) in memo:
            return memo[(m, n, i)]
        n1, m0 = self.computeOneZero(strs[i])
        if m - m0 >= 0 and n-n1 >=0:
            memo[(m,n,i)] = max(self.helper(strs, m-m0, n-n1, i+1, memo) + 1, 
                    self.helper(strs, m, n, i+1, memo))
        else:
            memo[(m, n, i)] = self.helper(strs, m, n, i+1, memo)
        return memo[(m, n, i)]
    
    def computeOneZero(self, string):
        ones = sum([int(i) for i in string])
        return ones, len(string) - ones


class Solution3: 
    def findMaxForm(self, strs, m, n):
        """
        bottom-up solution with O(mnN) in time and O(mn) in space
        ---> note: could be solved top-down in O(mnN) in time but in O(mnN) space
        """
        memo = [[0 for i in range(n+1)] for j in range(m+1)]
        for string in strs[:1]:
            n1, m0 = self.computeOneZero(string)
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i - m0 >= 0 and j - n1 >= 0:
                        memo[i][j] = max(memo[i][j], memo[i-m0][j-n1] + 1)
        return memo
                    
    def computeOneZero(self, string):
        ones = sum([int(i) for i in string])
        return ones, len(string) - ones



if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    # strs = ["10", "0", "1"]
    print(Solution3().findMaxForm(strs, 5, 3))