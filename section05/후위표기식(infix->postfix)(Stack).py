if __name__ == '__main__':
    a = input()
    stack = []  # 연산자
    res = ''  # 출력
    for x in a:
        if x.isdecimal():
            res += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()  # '(' 없앤다.
    while stack:
        res += stack.pop()
    print(res)
