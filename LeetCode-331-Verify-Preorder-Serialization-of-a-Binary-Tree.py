class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        seqs = preorder.split(',')
        if seqs[-1] != '#':
            return False
        res, isvalid = self.helper(seqs)
        return len(res) == 0 and isvalid

    def helper(self, seqs):
        if not seqs:
            return seqs, False
        if seqs[0] == '#':
            return seqs[1:], True
        # left tree
        afterleft, isvalid = self.helper(seqs[1:])
        # right tree
        afterright, isvalid = self.helper(afterleft)
        return afterright, isvalid

class Solution2:
    def isValidSerialization(self, preorder):
        seqs = preorder.split(',')
        if seqs[0] == '#' or seqs[-1] != '#':
            return False
        stack = [seqs[0]]
        for i in seqs:
            if not stack: return False
            if i == '#' and stack[-1] != '#':
                stack.append(i)
            if i == '#' and stack[-1] == '#':
                stack.pop()
        return True
        
            
