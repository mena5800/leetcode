class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def getstack(str_):
            stack1 = []
            for char in str_:
                if char == "#":
                    if len(stack1) ==0:
                        pass
                    else:
                        stack1.pop()
                else:
                    stack1.append(char)
            return stack1

        stack1 = getstack(s)
        stack2 = getstack(t)

        if "".join(stack1) == "".join(stack2):
            return True
        else:
            return False
