class MinStack:
    minVal = []
    stack = []
    def __init__(self):
        self.minVal = []
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minVal)==0 or self.minVal[-1] >= val :
            self.minVal.append(val)
    def pop(self) -> None:
        val = self.stack.pop()
        if(self.getMin()==val):
            self.minVal.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minVal[-1]

