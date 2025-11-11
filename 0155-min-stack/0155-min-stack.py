class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        return self.min_stack.append(val)
        

    def pop(self) -> None:
        if len(self.min_stack) == 0:
            return None
        else:
            return self.min_stack.pop()
        

    def top(self) -> int:
        if len(self.min_stack) == 0:
            return None
        else:
            return self.min_stack[-1]
        

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None
        else:
            return min(self.min_stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()