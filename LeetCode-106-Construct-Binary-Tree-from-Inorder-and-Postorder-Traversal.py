# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        inorder_right = inorder[inorder.index(root.val)+1:]
        inorder_left = inorder[:inorder.index(root.val)]

        root.right = self.buildTree(inorder_right, postorder)
        root.left = self.buildTree(inorder_left, postorder)
        return root

class Solution2:
    def buildTree(self, inorder, postorder):
        return self.recurhelper(inorder, postorder, 0, len(inorder)-1)
    
    def recurhelper(self, inorder, postorder, i, j):
        if i == j:
            return None
        root = TreeNode(postorder.pop())
        pivot = inorder.index(root.val)

        root.right = self.recurhelper(inorder, postorder, pivot+1, j)
        root.left = self.recurhelper(inorder, postorder, i, pivot-1)
        return root

if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    ans = Solution2().buildTree(inorder, postorder)