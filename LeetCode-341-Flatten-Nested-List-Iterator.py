class Solution:
    def flattenNestedList(self, nestedList):
        self.res = []
        self.dfs(nestedList)
        return self.res

    def dfs(self, nestedList):
        if type(nestedList) == int:
            self.res.append(nestedList)
            return
        for i in nestedList:
            self.dfs(i)

class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()
            
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            curr = self.stack.pop()
            if curr.isInteger():
                self.stack.append(curr)
                break
            else:
                currList = curr.getList()
                if not currList:
                    continue
                for i in currList[::-1]:
                    self.stack.append(i)
        return len(self.stack) > 0

if __name__ == "__main__":
    nestedList = [[1,1],2,[1,1]]
    print(Solution().flattenNestedList(nestedList))
