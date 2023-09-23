n = int(input())
a = list(map(int, input().split()))
chk = [1] * n
res = [0] * n
for i, x in enumerate(a, 1):
    sum = 0
    for j in range(n):
        if sum == x:
            if chk[j] == 1:
                chk[j] = 0
                res[j] = i
            else:
                p = chk.index(1, j)
                chk[p] = 0
                res[p] = i
            break
        else:
            sum += chk[j]
for _ in res:
    print(_, end=' ')

n = int(input())
a = list(map(int, input().split()))
seq = [0] * n
for i in range(n):
    for j in range(n):
        # 빈 공간 찾아서 넣기
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:  # 빈 자리를 발견하면
            a[i] -= 1
for x in seq:
    print(x, end=' ')
