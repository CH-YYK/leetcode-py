class MinStack:
    """
    use two stacks
        stack1: keep track of values pushed to it
        stack2: keep track of min values currently
    
    when:
        push(x): stack1: receive x:
                 stack2: test if x is currently minimum:
                    True: receive x
        pop() : stack1: drop x
                stack2: test if x is currently minumum:
                    True: drop x
        min() : return top value of stack2
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)
        
    def pop(self) -> None:
        mins = self.stack.pop()
        if mins == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()