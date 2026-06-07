import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = {"+": lambda x, y: x + y,
              "-": lambda x, y: y - x,
              "/": lambda x, y: math.trunc(y / x),
              "*": lambda x, y: x * y,}
        for t in tokens:
            if t in op:
                val = op[t](stack.pop(), stack.pop())
                stack.append(val)
            else:
                stack.append(int(t))
        return stack.pop()