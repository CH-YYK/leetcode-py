class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        for i in range(len(T)):
            res.append(0)
            if not stack:
                stack.append(i)
                continue
            while stack and T[i] > T[stack[-1]]:
                tmp = stack.pop()
                res[tmp] = i-tmp
            stack.append(i)
        return res

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T))