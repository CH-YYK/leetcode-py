class Solution:
    def isSymmetric(self, root):
        return root is None or self.recurSymmetrix(root.left, root.right)

    def recurSymmetrix(self, left, right):
        if not left or not right:
            return left == right
        if left and right:
            return left.val == right.val
        return self.recurSymmetrix(left.left, right.right) and self.recurSymmetrix(left.right, right.left)

    def isSymmetric2(self, root):
        if not root:
            return True
        stack = []
        if root.left:
            if not root.right: return False
            stack.append(root.left)
            stack.append(root.right)
        elif root.right:
            return False

        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left.val == right.val:
                return False
            if left.left:
                if not right.right: return False
                stack.append(left.left)
                stack.append(right.right)
            elif right.right: return False
            if left.right:
                if not right.left: return False
                stack.append(left.right)
                stack.append(right.left)
            elif right.left: return False
        return True

    def isSymmetric3(self, root):
        if not root:
            return True
        queue = []
        if root.left:
            if not root.right: return False
            queue.append(root.left)
            queue.append(root.right)
        elif root.right: return False

        while queue:
            left = queue.pop(0)
            right = queue.pop(0)

            if not left.val == right.val: return False

            if left.left:
                if not right.right: return False
                queue.append(left.left)
                queue.append(right.right)
            elif right.right: return False

            if left.right:
                if not right.left: return False
                queue.append(left.right)
                queue.append(right.left)
            elif right.left: return False
        return True






