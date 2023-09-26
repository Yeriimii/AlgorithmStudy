n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = -2147000000
for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    tmp = max(sum1, sum2)
    if tmp > res:
        res = tmp
sum3 = 0
sum4 = 0
for i in range(n):
    sum3 += a[i][i]
    sum4 += a[i][n-i-1]
tmp = max(sum3, sum4)
if tmp > res:
    res = tmp
print(res)
