s = input()
stack = list()
for x in s:
    if x.isalpha():
        print(x, end='')
    elif x == '(':
        stack.append(x)
    elif x == '*' or x == '/':
        while stack:
            o = stack.pop()
            if o == '(':
                stack.append(o)
                break
            elif o == '*' or o == '/':
                print(o, end='')
                break
            else:
                stack.append(o)
                break
        stack.append(x)
    elif x == '+' or x == '-':
        while stack:
            o = stack.pop()
            if o == '(':
                stack.append(o)
                break
            else:
                print(o, end='')
        stack.append(x)
    elif x == ')':
        while stack:
            o = stack.pop()
            if o == '(':
                break
            else:
                print(o, end='')
if len(stack) != 0:
    while stack:
        print(stack.pop(), end='')
