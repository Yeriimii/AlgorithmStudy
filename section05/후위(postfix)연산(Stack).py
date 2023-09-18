if __name__ == '__main__':
    t = input()
    stack = list()
    for x in t:
        if x.isdecimal():
            stack.append(int(x))
        elif x == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
        elif x == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif x == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
        elif x == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
    else:
        print(stack.pop())
