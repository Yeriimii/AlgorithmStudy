n = int(input())
board = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
board.insert(0, [0] * (n + 2))
board.insert(n + 1, [0] * (n + 2))
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] > board[i][j - 1] and board[i][j] > board[i][j + 1] and \
                board[i][j] > board[i - 1][j] and board[i][j] > board[i + 1][j]:
            cnt += 1
print(cnt)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
