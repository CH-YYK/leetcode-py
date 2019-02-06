class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s += ' '
        stack = []
        i = j = 0
        while i < len(s):
            if s[i] == ' ':
                wd = s[j:i]
                stack.append(wd)
                i += 1
                j = i
            else:
                i += 1
        newS = ''
        while stack:
            wd = stack.pop()
            if wd:
                newS += wd + ' '
        return newS[:-1]


if __name__ == '__main__':
    s = ' '
    print(Solution().reverseWords(s))


