n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
res = ''
num = 1

for x in arr:
    while num <= x:
        stack.append(num)
        res += '+'
        num += 1
    if stack[-1] == x:
        stack.pop()
        res += '-'
    else:
        print('NO')
        exit(0)

for x in res:
    print(x)
