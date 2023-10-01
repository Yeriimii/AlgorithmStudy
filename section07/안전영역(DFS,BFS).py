import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y, h):
    ch[x][y] = 1

    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for rain in range(100):  # 0 부터 돌아야 문제가 없다.
        cnt = 0
        ch = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > rain:
                    cnt += 1
                    DFS(i, j, rain)
        res = max(res, cnt)
        if cnt == 0:  # 안전영역이 0 개면 -> rain for loop 중단 (섬 높이보다 비가 많이 내림)
            break
    print(res)

