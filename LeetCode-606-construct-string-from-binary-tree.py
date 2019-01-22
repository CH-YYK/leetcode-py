class Solution:
    def tree2str(self, t):
        if not t:
            return ""
        string = self.preOder(t, "")
        return string[1:-1]

    def preOder(self, t, string):
        if not t.left and not t.right:
            return string + "({})".format(t.val)
        string += "("+str(t.val)
        string = self.preOder(t.left, string) if t.left else string + "()"
        string = self.preOder(t.right, string) if t.right else string
        string += ")"
        return string
