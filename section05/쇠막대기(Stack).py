cnt = 0
stack = list()
m = input()
for i, x in enumerate(m):
    if x == '(':
        stack.append(x)
    else:
        stack.pop()

        # counting
        if m[i-1] == '(':  # 레이저 인식 -> 지금까지 모든 쇠막대기 잘려자감 -> 쇠막대기 개수만큼 +
            cnt += len(stack)
        else:  # 쇠막대기 끝 지점 -> 부러져 나감 -> +1
            cnt += 1

print(cnt)
