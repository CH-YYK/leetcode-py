class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s)
        
    def helper(self, s):
        res = ""
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                res += s[i]
                i += 1
                continue
            j = i
            while s[j].isdigit():
                j += 1
            num = int(s[i:j])
            i = j
            
            stack = [i]
            l = i+1
            while stack:
                if s[l] == '[': stack.append(l)
                elif s[l] == ']': stack.pop()
                l += 1
            res += num * self.helper(s[i+1:l-1])     
            i = l
        return res

class Solution2:
    def decodeString(self, s):
        stack = []
        curString = ""
        curNum = ""
        for i in s:
            if i == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = ""
            elif i == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + int(num) * curString
            elif i.isdigit():
                curNum += i
            else:
                curString += i
        return curString

if __name__ == "__main__":
    s = "10[bc]"
    print(Solution2().decodeString(s))
        
