n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = n // 2
e = n // 2 + 1
for i in range(n):
    for j in range(s, e):
        res += a[i][j]
    if n // 2 > i:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
