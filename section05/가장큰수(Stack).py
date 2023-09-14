num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    # x가 앞에 있는 원소보다 크면 앞에 있는 원소 제거
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1  # 제거할 자리수 감소 카운트
    stack.append(x)

if m != 0:  # 마지막까지 제거해야할 자리수가 남을 때 슬라이싱으로 처리
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)
