import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "/": lambda x, y: math.trunc(x / y),
              "*": lambda x, y: x * y,}
        for t in tokens:
            if t in op:
                r_operand = stack.pop()
                l_operand = stack.pop()
                val = op[t](l_operand, r_operand)
                stack.append(val)
            else:
                stack.append(int(t))
        return stack.pop()