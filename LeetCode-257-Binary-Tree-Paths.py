class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfsPathFinding(root, str(root.val), res)
        return res

    def dfsPathFinding(self, root, path, total):
        if not root.left and not root.right:
            total.append(path)
        else:
            if root.left:
                self.dfsPathFinding(root.left, path+"->"+str(root.left.val), total)
            if root.right:
                self.dfsPathFinding(root.right, path+"->"+str(root.right.val), total)

    def binaryTreePaths2(self, root):
        if not root:
            return []
        stack = [(root, str(root.val))]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            else:
                if node.right:
                    stack.append((node.right, path + "->" + str(node.right.val)))
                if node.left:
                    stack.append((node.left, path + "->" + str(node.left.val)))
        return res

    def binaryTreePaths3(self, root):
        if not root:
            return []
        queue = [(root, str(root.val))]
        res = []
        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:
                res.append(path)
            else:
                if node.left:
                    queue.append((node.left, path+'->'+str(node.left.val)))
                if node.right:
                    queue.append((node.right, path+'->'+str(node.right.val)))
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    solution = Solution()
    print(solution.binaryTreePaths3(root))