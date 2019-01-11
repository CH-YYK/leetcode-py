"""
This will resemble how stack works in python
"""


class Stack:
    class StackNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    top = None

    def pop(self):
        item = self.top.val
        self.top = self.top.next
        return item

    def push(self, item):
        t = self.StackNode(item)
        t.next = self.top
        self.top = t

    def peek(self):
        return self.top.val

    def isEmpty(self):
        return self.top is None