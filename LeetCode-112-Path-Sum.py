class Solution:
    def hasPathSum(self, root, number):
        if not root:
            return False
        return self.dfs_hasPathSum(root, number)

    def dfs_hasPathSum(self, root, number):
        if root:
            if number-root.val == 0 and not root.left and not root.right:
                return True
            hasLeft = self.dfs_hasPathSum(root.left, number-root.val) if root.left else False
            hasRight = self.dfs_hasPathSum(root.right, number-root.val) if root.right else False
            return hasLeft or hasRight

    def hasPathSum2(self, root, number):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, curr = stack.pop()
            if not node.left and not node.right:
                if curr == number:
                    return True
            if node.right:
                stack.append((node.right, curr+node.right.val))
            if node.left:
                stack.append((node.left, curr + node.left.val))
        return False

    def hasPathSum3(self, root, number):
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            node, curr = queue.pop(0)
            if not node.left and not node.right:
                if curr == number:
                    return True
            if node.left:
                queue.append((node.left, curr + node.left.val))
            if node.right:
                queue.append((node.right, curr + node.right.val))
        return False