class Solution:
    def findSubstringInWraproundString(self, p: 'str') -> 'int':
        if not p:
            return 0
        alphaHash = {chr(i): i - 97 for i in range(97, 123)}
        start = end = 0
        index = alphaHash.get(p[0])
        num = 0
        hash = set()
        for end in range(1, len(p)):
            print('start')
            currIndex = alphaHash.get(p[end])
            if currIndex == (index + 1) % 26:
                index = currIndex
            else:
                substr = p[start:end]
                num += self.numSubstr(substr) if substr in hash else 0
                start = end
                hash.add(substr)
        substr = p[start:end + 1]
        num += self.numSubstr(substr) if substr in hash else 0
        hash.add(substr)
        return num

    def numSubstr(self, subStr):
        return (len(subStr) + 1) * len(subStr) // 2