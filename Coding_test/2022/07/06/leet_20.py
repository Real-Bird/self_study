def isValid(s):
    stack = []
    table = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    for i in s:
        if i not in table:
            stack.append(i)
        elif not stack or table[i] != stack.pop():
            return False
    return len(stack) == 0

print(isValid("()[]{}"))