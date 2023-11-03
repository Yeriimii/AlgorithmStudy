n = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
dy = [0 for _ in range(n + 1)]
dy[1] = P[1]
res = 0
for i in range(2, n + 1):
    if i % 2 == 0:
        for j in range(i-1, i // 2 - 1, -1):
            dy[i] = max(dy[i], P[i], dy[j] + dy[i-j])
            if res < dy[i]:
                res = dy[i]
    else:
        for j in range(i-1, i // 2, -1):
            dy[i] = max(dy[i], P[i], dy[j] + dy[i-j])
            if res < dy[i]:
                res = dy[i]
if n > 1:
    print(res)
else:
    print(max(dy))
