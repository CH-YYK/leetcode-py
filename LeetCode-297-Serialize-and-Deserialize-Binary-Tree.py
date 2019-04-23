# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    self.root = 1
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if not curr:
                res.append('null')
                continue
            res.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        j = len(res) - 1
        while res and res[j] == 'null':
            res.pop()
            j -= 1
        return '['+ ','.join(res) + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        nodes = [int(i) if i != 'null' else i for i in data[1:-1].split(',')]

        i, n = 0, len(nodes)

        root = TreeNode(nodes[i])
        queue = [root]

        while queue:
            curr = queue.pop(0)
            if not curr:
                continue
            if i + 1 < n:
                i += 1
                curr.left = TreeNode(nodes[i])
            if i + 1 < n:
                i += 1
                curr.right = TreeNode(nodes[i])
            queue.append(curr.left)
            queue.append(curr.right)
        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))