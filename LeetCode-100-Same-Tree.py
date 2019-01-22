class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        method1: in-order traversal
        """
        traversal1 = []
        traversal2 = []
        self.inOrderTraversal(p, traversal1)
        self.inOrderTraversal(q, traversal2)
        print(traversal1)
        print(traversal2)
        return traversal1 == traversal2

    def inOrderTraversal(self, node, traversal):
        if node is not None:
            if node.left or node.right:
                node.left = node.left if node.left else TreeNode(None)
                node.right = node.right if node.right else TreeNode(None)

            self.inOrderTraversal(node.left, traversal)
            traversal.append(node.val)
            self.inOrderTraversal(node.right, traversal)

    def isSameTree2(self, p, q):
        """
        method2: recursive
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree2(p.right, q.right)
        else:
            return p == q

    def isSameTree3(self, p, q):
        """
        method3: stack (DFS)
        """
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 is None and node2 is None:
                continue
            elif (node1 and node2) and (node1.val == node2.val):
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                return False
        return True

    def isSameTree4(self, p, q):
        """
        method4: queue (BFS)
        """
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif node1 and node2 and (node1.val == node2.val):
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            else:
                return False
        return True


if __name__ == '__main__':
    p = TreeNode(1)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)

    print(Solution().isSameTree(p, q))