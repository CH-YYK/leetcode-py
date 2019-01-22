class Solution:
    def isSubtree(self, s, t):
        if not s:
            return False
        if self.dfsIsSame(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def dfsIsSame(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if not s.val == t.val:
            return False
        return self.dfsIsSame(s.left, t.left) and self.dfsIsSame(s.right, t.right)

    def isSubtree2(self, s, t):
        preorder_s = self.dfsPreorder(s, '')
        preorder_t = self.dfsPreorder(t, '')

        postorder_s = self.dfsPostOrder(s, '')
        postorder_t = self.dfsPostOrder(t, '')
        return preorder_t in preorder_s and postorder_t in postorder_s

    def dfsPreorder(self, node, string):
        if not node:
            return string+"#"
        string += str(node.val)
        string = self.dfsPreorder(node.left, string)
        string = self.dfsPreorder(node.right, string)
        return string

    def dfsPostOrder(self, node, string):
        if not node:
            return string+"#"
        string = self.dfsPostOrder(node.left, string)
        string = self.dfsPostOrder(node.right, string)
        string += str(node.val)
        return string

