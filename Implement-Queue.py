"""
This will resemble how queue works in python
"""


class Queue:
    class QueueNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    first = None
    last = None

    def add(self, item):
        t = self.QueueNode(item)
        if self.last:
            self.last.next = t
        self.last = t
        if not self.first:
            self.first = self.last

    def remove(self):
        data = self.first.val
        self.first = self.first.next
        if not self.first:
            self.last = None
        return data

    def peek(self):
        return self.first.data

    def isEmpty(self):
        return self.first is None

