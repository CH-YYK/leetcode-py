# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, target):
        self.numSums = 0
        self.dfs(root, target)
        return self.numSums

    def dfs(self, root, target):
        if not root:
            return
        self.findSums(root, target)
        self.dfs(root.left, target)
        self.dfs(root.right, target)

    def findSums(self, root, target):
        if not root:
            return
        if target == root.val:
            self.numSums += 1
        self.findSums(root.left, target - root.val)
        self.findSums(root.right, target - root.val)

    def pathSum2(self, root, target):
        self.numSums = 0
        cache = {0: 1}  # currentPathSum = 0
        self.dfs2(root, target, root.val, cache)
        return self.numSums

    def dfs2(self, root, target, currPathSum, cache):
        if not root:
            return
        currPathSum += root.val     # currPathSum update by the node value
        oldPathSum = currPathSum - target
        self.numSums += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        self.dfs2(root.left, target, currPathSum, cache)
        self.dfs2(root.right, target, currPathSum, cache)
        cache[currPathSum] -= 1     # the currPathSum in this branch should be removed

    def pathSum3(self, root, target):
        if not root:
            return 0
        result = 0
        stack = [(root, 0)]
        cache = {0: 1}
        while stack:
            node, currPathSum = stack.pop()
            currPathSum += node.val
            cache[currPathSum] = cache.get(currPathSum, 0) + 1
            if currPathSum - target in cache:
                print(node.val)
                result += cache[currPathSum - target]
            if node.left:
                stack.append((node.left, currPathSum))
            if node.right:
                stack.append((node.right, currPathSum))
            if not node.left and not node.right:
                cache[currPathSum] -= 1
        return result