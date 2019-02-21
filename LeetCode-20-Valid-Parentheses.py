class Solution:
    def isValid(self, s: 'str') -> 'bool':
        leftStack = []
        hashmap = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in ['{', '[', '(']:
                leftStack.append(i)
            else:
                if not leftStack:
                    return False
                left = leftStack.pop()
                if i != hashmap[left]:
                    return False
        return not leftStack





