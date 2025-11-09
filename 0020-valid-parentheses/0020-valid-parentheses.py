class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) != 0:
                    topCh = stack[-1]
                    if char == ')' and topCh == '(':
                        stack.pop()
                    elif char == '}' and topCh == '{':
                        stack.pop()
                    elif char == ']' and topCh == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False








        #     elif char == ')':
        #         if len(stack) == 0 or stack[-1] != '(':
        #             return False
        #         else:
        #             stack.pop()
        #     elif char == '}':
        #         if len(stack) == 0 or stack[-1] != '{':
        #             return False
        #         else:
        #             stack.pop()
        #     elif char == ']':
        #         if len(stack) == 0 or stack[-1] != '[':
        #             return False
        #         else:
        #             stack.pop()

        # if len(stack) == 0:
        #     return True
        # else:
        #     return False



        