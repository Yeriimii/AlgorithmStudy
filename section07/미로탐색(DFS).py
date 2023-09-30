dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt

    if x == 6 and y == 6:  # 중단점
        cnt += 1
    else:
        for i in range(4):  # 4 방향 탐색
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:  # 방문하지 않은 곳이라면
                board[xx][yy] = 1  # 방문 체크 설정
                DFS(xx, yy)
                board[xx][yy] = 0  # 방문 체크 해제


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)
