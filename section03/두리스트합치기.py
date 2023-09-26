n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
res = list()
p1 = 0
p2 = 0
while p1 < n or p2 < m:
    if a[p1] <= b[p2]:
        res.append(a[p1])
        p1 += 1
    else:
        res.append(b[p2])
        p2 += 1
if p1 < n:
    res += a[p1:]
elif p2 < m:
    res += b[p2:]
for x in res:
    print(x, end=' ')

