# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        Recursive
        build tree according to the in-Order traversal
        """
        if not nums:
            return None
        midpoint = len(nums) // 2
        root = TreeNode(nums[midpoint])
        root.left = self.sortedArrayToBST(nums[:midpoint])
        root.right = self.sortedArrayToBST(nums[(midpoint + 1):])
        return root

    def sortedArrayToBST2(self, nums):
        """
        Iterative method
        """
        if not nums:
            return []
        root = TreeNode(nums[len(nums) // 2])
        stack = [(root, nums[:len(nums) // 2], nums[len(nums) // 2+1:])]
        while stack:
            node, leftNums, rightNums = stack.pop()
            if not leftNums:
                node.left = None
            else:
                leftIndex = len(leftNums) // 2
                node.left = TreeNode(leftNums[leftIndex])
                stack.append((node.left, leftNums[:leftIndex], leftNums[leftIndex+1:]))

            if not rightNums:
                node.right = None
            else:
                rightIndex = len(rightNums) // 2
                node.right = TreeNode(rightNums[rightIndex])
                stack.append((node.right, rightNums[:rightIndex], rightNums[rightIndex+1:]))
        return root

    def sortedArrayToBST3(self, nums):
        if not nums:
            return []
        rootIndex = len(nums) // 2
        root = TreeNode(nums[rootIndex])
        queue = [(root, nums[:rootIndex], nums[rootIndex+1:])]
        while queue:
            node, leftNums, rightNums = queue.pop(0)
            if not leftNums:
                node.left = None
            else:
                leftIndex = len(leftNums) // 2
                node.left = TreeNode(leftNums[leftIndex])
                queue.append((node.left, leftNums[:leftIndex], leftNums[leftIndex + 1:]))

            if not rightNums:
                node.right = None
            else:
                rightIndex = len(rightNums) // 2
                node.right = TreeNode(rightNums[rightIndex])
                queue.append((node.right, rightNums[:rightIndex], rightNums[rightIndex + 1:]))
        return root


if __name__ == '__main__':
    array = [-10,-3,0,5,9]
    solution = Solution()
    ans = solution.sortedArrayToBST2(array)
