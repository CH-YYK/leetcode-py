# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and t2:
            return t2
        elif t1 and not t2:
            return t1
        elif not t1 and not t2:
            return
        self.dfsMerge(t1, t2)
        return t1

    def dfsMerge(self, t1, t2):
        t1.val += t2.val
        if not t1.left and not t1.right and not t2.left and not t2.right:
            return
        if t2.left:
            if t1.left:
                self.dfsMerge(t1.left, t2.left)
            else:
                t1.left = t2.left
        if t2.right:
            if t1.right:
                self.dfsMerge(t1.rigth, t2.right)
            else:
                t1.right = t2.right

    def mergeTrees2(self, t1, t2):
        if not t1 and t2:
            return t2
        elif t1 and not t2:
            return t1
        elif not t1 and not t2:
            return

        stack = [(t1, t2)]
        while stack:
            node1, node2 = stack.pop()
            node1.val += node2.val
            if not t1.left and not t1.right and not t2.left and not t2.right:
                continue
            if node2.left:
                if node1.left:
                    stack.append((node1.left, node2.left))
                else:
                    node1.left = node2.left
            if node2.right:
                if node1.right:
                    stack.append((node1.right, node2.right))
                else:
                    node1.right = node2.right
        return t1
