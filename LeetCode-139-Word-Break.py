class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        self.wordDict = wordDict
        return self.recur(s)

    def recur(self, string):
        if not string:
            return True
        cond = False
        for i in range(len(string)):
            if string[:i+1] in self.wordDict:
                cond = cond or self.recur(string[i+1:])
            else:
                continue
        return cond

class Solution2:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        self.wordDict = wordDict
        self.memo = {}
        return self.recur(s, 0)
    
    def recur(self, string, l):
        if l == len(string):
            return True
        if l in self.memo:
            return self.memo[l]
        cond = False
        for k in range(l, len(string)):
            if string[l:k+1] in self.wordDict:
                cond = cond or self.recur(string, k+1)
        self.memo[l] = cond
        return self.memo[l]

