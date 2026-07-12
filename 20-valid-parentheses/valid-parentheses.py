class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ['(', '{', '[']:
                stack.append(x)
            elif x in [')', '}', ']']:
                if not stack:
                    return False
                elif x == ')' and stack[-1] == '(':
                    stack.pop()
                elif x == '}' and stack[-1] == '{':
                    stack.pop()
                elif x == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False