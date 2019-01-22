class Solution:
    def diameterOfBinaryTree(self, root):
        self.Max = 0
        self.dfsDepth(root, 0)
        return self.Max

    def dfsDepth(self, root, depth):
        if not root:
            return depth
        leftHeight = self.dfsDepth(root.left, depth + 1) if root.left else 0
        rightHeight = self.dfsDepth(root.right, depth + 1) if root.right else 0

        self.Max = max(self.Max, leftHeight + rightHeight)

        return max(leftHeight, rightHeight) + 1

    def diameterOfBinaryTree2(self, root):
        if not root:
            return 0
        stack = [(root, 0)]
        Depth = {None: -1}
        diameter = 0
        while stack:
            node, reached = stack.pop()
            if not node:
                continue
            if not reached:
                stack.extend([(node, 1), (node.left, 0), (node.right, 0)])
            else:
                leftHeight = Depth[node.left] + 1
                rightHeight = Depth[node.right] + 1
                diameter = max(leftHeight + rightHeight, diameter)
                Depth[node] = max(leftHeight, rightHeight)
        return diameter