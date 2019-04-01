class Solution:
    def simplifyPath(self, path: str) -> str:
        # split path to folders
        stack1 = []
        i = 0
        j = 0
        while i <= j and j < len(path):
            if path[j] == '/':
                if j - i > 0:
                    stack1.append(path[i:j])
                j += 1
                i = j
            else:
                j += 1
        if j - i > 0:
            stack1.append(path[i:j])
        stack2 = []
        for i in stack1:
            if i == '.':
                continue
            elif i == '..':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        return '/' + '/'.join(stack2)

class Solution:
    def simplifyPath(self, path):
        stack1 = [i for i in path.split('/') if len(i) > 0]
        stack2 = []
        for i in stack1:
            if i == '.':
                continue
            elif i == '..':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        return '/' + '/'.join(stack2)
if __name__ == "__main__":
    print(Solution().simplifyPath("/a//b////c/d//././/.."))