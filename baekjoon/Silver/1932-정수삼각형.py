n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * (i+1) for i in range(n)]
dy[0][0] = tree[0][0]
for i in range(1, n):
    dy[i][0] = dy[i-1][0] + tree[i][0]
    dy[i][-1] = dy[i-1][-1] + tree[i][-1]
for i in range(2, n):
    for j in range(1, i):
        dy[i][j] = max(dy[i-1][j-1], dy[i-1][j]) + tree[i][j]
print(max(dy[-1]))
