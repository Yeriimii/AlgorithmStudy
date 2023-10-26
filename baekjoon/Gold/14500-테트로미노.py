def DFS(x, y, dsum, cnt):
    global res
    if cnt == 4:
        res = max(res, dsum)
        return
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
                visited[xx][yy] = True
                DFS(xx, yy, dsum+board[xx][yy], cnt+1)
                visited[xx][yy] = False


def DFS2(x, y):
    global res
    for i in range(4):
        tmp = board[x][y]
        for j in range(3):
            k = (i+j) % 4
            xx = x + dx[k]
            yy = y + dy[k]
            if not (0 <= xx < n and 0 <= yy < m):
                tmp = 0
                break
            tmp += board[xx][yy]
        res = max(res, tmp)


if __name__ == '__main__':
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    res = 0
    visited[0][0] = True
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            DFS(i, j, board[i][j], 1)
            visited[i][j] = False

            DFS2(i, j)
    print(res)
