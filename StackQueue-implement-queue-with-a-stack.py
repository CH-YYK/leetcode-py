class Queue(object):
    def __init__(self):
        """
        implement queue with two stacks
        """
        self.stackEnque = []
        self.stackDeque = []

    def enqueue(self, val):
        self.stackEnque.append(val)

    def dequeue(self):
        if self.stackDeque:
            return self.stackDeque.pop()
        while self.stackEnque:
            self.stackDeque.append(self.stackEnque.pop())
        return self.stackDeque.pop()

    def display(self):
        print(self.stackDeque[::-1]+self.stackEnque)


class Queue2(object):
    def __init__(self):
        """
        implement queue with one stack
        """
        self.stack = []

    def enqueue(self, val):
        self.stack.append(val)

    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()
        currValue = self.stack.pop()
        res = self.dequeue()
        self.stack.append(currValue)
        return res

    def display(self):
        print(self.stack)


if __name__ == '__main__':
    queue = Queue2()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)