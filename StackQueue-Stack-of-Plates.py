"""
build a list of stacks where each of which has capacity
"""


class Stack:
    def __init__(self, capacity):
        self.top = None
        self.volumne = 0
        self.capacity = capacity

    class StackNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def pop(self):
        item = self.top.val
        self.top = self.top.next
        self.volumne -= 1
        return item

    def push(self, item):
        t = self.StackNode(item)
        t.next = self.top
        self.top = t
        self.volumne += 1

    def peek(self):
        return self.top.val

    def isEmpty(self):
        return self.top is None

    def isFull(self):
        return self.volumne == self.capacity


class SetOfStacks:
    def __init__(self, capacity):
        self.stacksSet = []
        self.capacity = capacity

    def push(self, value):
        LastStack = self.getLastStack()
        if not (LastStack is None and LastStack.isFull()):
            LastStack.push(value)
        else:
            self.stacksSet.append(Stack(capacity=10))
            self.stacksSet[-1].push(value)

    def pop(self):
        LastStack = self.getLastStack()
        if LastStack is None:
            raise AttributeError("LastStack is Empty")
        value = LastStack.pop()
        if LastStack is None:
            self.stacksSet.pop()
        return value

    def getLastStack(self):
        if len(self.stacksSet) == 0:
            return None
        else:
            return self.stacksSet[-1]

    def isEmpty(self):
        return len(self.stacksSet) == 0