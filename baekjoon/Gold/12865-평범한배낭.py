n, k = map(int, input().split())
dy = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j >= w:
            dy[i][j] = max(dy[i-1][j-w] + v, dy[i-1][j-0])
        elif j < w:
            dy[i][j] = dy[i-1][j]

print(dy[-1][-1])
