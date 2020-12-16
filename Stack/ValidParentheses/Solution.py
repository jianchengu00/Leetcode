class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) > 0:
                    if ch == ')' and stack.pop() != '(':
                        return False
                    elif ch == '}' and stack.pop() != '{':
                        return False
                    elif ch == ']' and stack.pop() != '[':
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        return False
