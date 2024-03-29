# 서쪽 : (0.-1),남쪽 : (1,0), 동쪽 :(0,1), 북쪽 : (-1,0)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def back(x, y, direction):
    if direction == 0 or direction == 1:
        nx = x + dx[direction + 2]
        ny = y + dy[direction + 2]
    if direction == 2 or direction == 3:
        nx = x + dx[direction - 2]
        ny = y + dy[direction - 2]
    return nx, ny


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 청소여부 저장 0:청소X, 1: 청소 0
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1
count = 1
while True:
    unavail = 0
    for _ in range(4):
        nx = r + dx[(3 + d) % 4]
        ny = c + dy[(3 + d) % 4]
        # 청소가 가능한 지역
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            d = (3 + d) % 4
            visited[nx][ny] = 1
            r = nx
            c = ny
            count += 1
            unavail = 1
            break
        # 청소가 불가능한 지역
        else:
            d = (3 + d) % 4
    # 만약 4가지 방향을 다 보았는데도 청소가능한 지역이 없는경우
    if unavail == 0:
        a, b = back(r, c, d)
        if graph[a][b] == 1:
            break
        else:
            r, c = a, b

print(count)
