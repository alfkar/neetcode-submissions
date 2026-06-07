class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack)==0:
                return False
            elif pairs.get(stack.pop())!=bracket:
                return False
        if len(stack)==0:
            return True
        else:
            return False
