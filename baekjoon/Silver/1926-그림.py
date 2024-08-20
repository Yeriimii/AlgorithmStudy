import sys
sys.setrecursionlimit(10 ** 9)


def dfs(x: int, y: int):
    global image_size

    for _i in range(4):
        nx = x + dx[_i]
        ny = y + dy[_i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            image_size += 1
            dfs(nx, ny)


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n, m = map(int, sys.stdin.readline().strip().split())
    graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    image_cnt = 0
    max_size = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = 0
                image_cnt += 1
                image_size = 1
                dfs(i, j)
                max_size = max(max_size, image_size)

    print(image_cnt)
    print(max_size)
