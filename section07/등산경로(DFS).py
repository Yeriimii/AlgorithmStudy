dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt

    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1  # 방문 체크 설정
                DFS(xx, yy)
                ch[xx][yy] = 0  # 방문 체크 해제


if __name__ == '__main__':
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))  # 첫 행 읽기
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]  # 시작점 좌표
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]  # 끝점 좌표
                ex = i
                ey = j
            board[i][j] = tmp[j]  # board 입력
    ch[sx][sy] = 1  # 시작점 체크
    cnt = 0
    DFS(sx, sy)
    print(cnt)
