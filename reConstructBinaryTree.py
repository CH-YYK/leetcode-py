"""
You are given a pre-order traversal and an in-order traversal for a binary tree. Build a function to reconstruct it.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre_, in_):
        # no branches
        if len(pre_) == 0 and len(in_) == 0:
            return None

        # define root Node
        rootNode = TreeNode(pre_[0])
        if len(pre_) == 0:
            return rootNode

        # find index of root value in in-order sequence to split pre_ and in_
        rootIndex_in = 0
        for i in range(len(in_)):
            if in_[i] == rootNode.val:
                rootIndex_in = i

        # split pre_ and in_
        pre_start, pre_end = 1, rootIndex_in+1
        in_start, in_end = 0, rootIndex_in

        if rootIndex_in > 0:    # left node exist
            rootNode.left = self.reConstructBinaryTree(pre_[pre_start: pre_end], in_[in_start:in_end])
        if rootIndex_in < len(in_):     # right node exist
            rootNode.right = self.reConstructBinaryTree(pre_[pre_end:], in_[in_end+1:])
        return rootNode

if __name__ == '__main__':
    pre_ = [1, 2, 4, 7, 3, 5, 6, 8]
    in_ = [4, 7, 2, 1, 5, 3, 8, 6]
    print(Solution().reConstructBinaryTree(pre_, in_))