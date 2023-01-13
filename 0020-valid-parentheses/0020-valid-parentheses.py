class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 !=0:
            return False

        for char in s:
            try:
                if char == '(' or char == "{" or char == "[":
                    stack.append(char)
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            except:
                return False
        if len(stack) !=0:
            return False
        else:
            return True
        