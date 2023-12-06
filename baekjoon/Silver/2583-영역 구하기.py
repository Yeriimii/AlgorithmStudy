from collections import deque


def bfs(i, j):
    Q = deque()
    Q.append((i, j))
    cnt = 1
    while Q:
        y, x = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                Q.append((ny, nx))
                cnt += 1
    return cnt


if __name__ == '__main__':
    # n = x, m = y
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                graph[i][j] = 1

    result = []
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 0:
                graph[i][j] = 1
                res = bfs(i, j)
                result.append(res)

    print(len(result))
    print(*sorted(result))
