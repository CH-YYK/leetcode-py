class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        s = []
        base = 0
        for i in S:
            if i != '(' and not s:
                base += 1
            else:
                if i == '(':
                    s.append('(')
                else:
                    s.pop()
        return len(s) + base
