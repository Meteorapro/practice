def check_brackets(s):
    stack = []
    output = []
    for char in s:
        if char == "(":
            stack.append(char)
            output.append(char)
        elif char == ")":
            if not stack or {'(': ')'}[stack.pop()] != char:
                output.append('x' if stack else '?')
            else:
                output.append(char)
        else:
            output.append(char)

    # 标记未匹配的左括号
    while stack:
        output.append('x')

    return ''.join(output)

print(check_brackets(input()))