"""
Design a stack which, in addition to push and pop, has a function min
which returns minimum element? Push, pop and min should operate in O(1)
"""

import sys

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


class StackWithMin(Stack):
    stackMin = Stack()

    def push(self, value):
        if value < self.min():
            self.stackMin.push(value)
        super().push(value)

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.stackMin.pop()
        super().pop()

    def min(self):
        if self.stackMin.isEmpty():
            return sys.maxsize
        else:
            return self.stackMin.peek()
