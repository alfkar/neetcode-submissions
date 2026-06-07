class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def generateValid(nLeft: int, nRight: int):
            print("Stack: ", stack)
            if(n == nLeft == nRight):
                result.append("".join(stack))
                return
            if(nLeft < n):
                stack.append('(')
                generateValid(nLeft+1, nRight)
                stack.pop()
            if(nRight < nLeft):
                stack.append(')')
                generateValid(nLeft, nRight+1)
                stack.pop()
        generateValid(0,0)
        return result