while True:
    stack = []

    string = input()
    if string == ".":
        break

    for idx, x in enumerate(string):
        if x == "(" or x == "[":
            stack.append(x)
        elif x == ")":
            if len(stack) > 0:
                recent = stack.pop()
                if recent != "(":
                    print("no")
                    break
            else:
                print("no")
                break
        elif x == "]":
            if len(stack) > 0:
                recent = stack.pop()
                if recent != "[":
                    print("no")
                    break
            else:
                print("no")
                break

        if idx == len(string) - 1:
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
