class Solution:
    def findTarget(self, root, k):
        if not root:
            return
        self.ind = False
        res = set()
        self.dfsFindTarget(root, res, k)
        return self.ind

    def dfsFindTarget(self, root, res, k):
        if not root:
            return
        self.dfsFindTarget(root.left, res, k)
        if k - root.val in res:
            self.ind = True
        res.add(root.val)
        self.dfsFindTarget(root.right, res, k)

    def findTarget3(self, root, k):
        res = set()
        def dfs(root, t):
            if not root:
                return False
            if t-root.val in res:
                return True
            res.add(root.val)
            return dfs(root.left, t) or dfs(root.right, t)
        return dfs(root, k)


    def findTarget2(self, root, k):
        if not root:
            return
        leftStack, rightStack = [], []
        node1 = node2 = root
        while node1:
            leftStack.append(node1.left)
            node1 = node1.left
        while node2:
            rightStack.append(node2.right)
            node2 = node2.right

        def findNextLeft():
            leftNode = leftStack.pop()
            if leftNode.right:
                leftNode = leftNode.right
                while leftNode:
                    leftStack.append(leftNode)
                    leftNode = leftNode.left

        def findNextRight():
            rightNode = rightStack.pop()
            if rightNode.left:
                rightNode = rightNode.left
                while rightNode:
                    rightStack.append(rightNode)
                    rightNode = rightNode.left

        while leftStack[-1].val != rightStack[-1].val:
            tmpSum = leftStack[-1].val + rightStack[-1].val
            if tmpSum == k:
                return True
            elif tmpSum < k:
                findNextLeft()
            else:
                findNextRight()
        return False