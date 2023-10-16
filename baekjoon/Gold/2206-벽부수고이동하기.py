from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
res = 2147000000
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
Q = deque()
Q.append((0, 0, 0, 1))
visit[0][0][0] = 1
visit[0][0][1] = 1
last_x = 0
last_y = 0
while Q:
    cur = Q.popleft()
    last_x = cur[0]
    last_y = cur[1]
    has_break = cur[2]
    dist = cur[3]
    if last_x == n-1 and last_y == m-1:
        if res > dist:
            res = dist
        break
    for i in range(4):
        xx = last_x + dx[i]
        yy = last_y + dy[i]
        if 0 <= xx < n and 0 <= yy < m and visit[xx][yy][has_break] == 0:  # 벽 부순 이력 상태를 갖고, 방문한 적이 없는 경우만
            if board[xx][yy] == 0:  # 지나갈 수 있을 경우
                visit[xx][yy][has_break] = 1  # 방문 체크
                Q.append((xx, yy, has_break, dist + 1))  # 현재 상태(벽을 부쉈는지 상태)를 다음 탐색에 넘김
            else:  # 벽을 만난 경우
                if not has_break:  # 벽을 한 번도 부순적이 없을 때만
                    visit[xx][yy][has_break] = 1  # 방문 체크
                    Q.append((xx, yy, 1, dist + 1))  # 다음 탐색부터는 '벽을 부순 이력이 있는 상태'를 넘김

if res < 2147000000:
    print(res)
else:
    print(-1)
