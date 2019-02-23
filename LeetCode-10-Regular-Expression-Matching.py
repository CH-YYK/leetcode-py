class Solution:

    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if not s or not p:
            if not s and not p:
                return True
            if len(p) == 2 and p[1] == '*':
                return True
            else:
                return False
                
        if len(p) > 1 and p[1] == '*':
            if p[0] != s[0] and p[0] != '.':
                return self.isMatch(s, p[2:])
            return self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:]) or self.isMatch(s, p[2:])
        
        if p[0] == '.' or p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        else:
            return False