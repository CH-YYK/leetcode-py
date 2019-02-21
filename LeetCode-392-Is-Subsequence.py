class Solution:
    def isSubsequence(self, s, t):
        # recursive solution, O(2^(N_t))
        if s and not t:
            return False
        if not s:
            return True
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])

    def isSubsequence2(self, s: 'str', t: 'str') -> 'bool':
        # recursive with memoization
        memo = {}
        return self.helper(s, t, memo)

    def helper(self, s, t, memo):
        if s and not t:
            return False
        if not s:
            return True

        if (s, t) in memo:
            return memo[(s, t)]

        if s[0] == t[0]:
            memo[(s, t)] = self.helper(s[1:], t[1:], memo)
            return memo[(s, t)]
        else:
            memo[(s, t)] = self.helper(s, t[1:], memo)
            return memo[(s, t)]

    def isSubsequence3(self, s, t):
        # recursive with index
        return self.helper_index(s, t, 0, 0)

    def helper_index(self, s, t, index_s, index_t):
        if index_t == len(t) and index_s < len(s):
            return False
        if index_s == len(s):
            return True

        if s[index_s] == t[index_t]:
            return self.helper_index(s, t, index_s + 1, index_t + 1)
        else:
            return self.helper_index(s, t, index_s, index_t + 1)

    def isSubsequence4(self, s, t):
        # recursive with index and memoization
        memo = {}
        return self.helper_index_memo(s, t, 0, 0, memo)

    def helper_index_memo(self, s, t, index_s, index_t, memo):
        if index_t == len(t) and index_s < len(s):
            return False
        if index_s == len(s):
            return True

        if (index_s, index_t) in memo:
            return memo[(index_s, index_t)]

        if s[index_s] == t[index_t]:
            memo[(index_s, index_t)] = self.helper_index_memo(s, t, index_s+1, index_t+1, memo)
            return memo[(index_s, index_t)]
        else:
            memo[(index_s, index_t)] = self.helper_index_memo(s, t, index_s, index_t + 1, memo)
            return memo[(index_s, index_t)]

    def isSubsequence5(self, s, t):
        i_s = 0
        i_t = 0
        while i_t < len(t) and i_s < len(s):
            if s[i_s] == t[i_t]:
                i_s += 1
                i_t += 1
            else:
                i_t += 1
        return True if i_s == len(s) else False

    def isSubsequence6(self, s, t):
        i_s = 0
        for i_t in range(len(t)):
            if i_s == len(s):
                return True
            if s[i_s] == t[i_t]:
                i_s += 1
        return i_s == len(s)
