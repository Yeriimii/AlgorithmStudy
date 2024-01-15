from collections import deque

N = int(input())
for _ in range(N):
    strings = deque(input())
    stack = list()
    cnt = 0
    while strings:
        x = strings.popleft()
        if x == '(':
            cnt += 1
            stack.append(x)
        else:
            cnt -= 1
            if stack:
                stack.pop()
            else:
                break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
