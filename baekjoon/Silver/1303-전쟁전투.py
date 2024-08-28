from collections import deque


def bfs(r: int, c: int, find_color: str):
    visited[r][c] = True
    count = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    q.append((r, c))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == find_color:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1

    return count


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [input() for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    my_power = 0
    enemy_power = 0

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and board[i][j] == 'W':
                white_count = bfs(i, j, 'W')
                my_power += white_count ** 2
            elif not visited[i][j] and board[i][j] == 'B':
                blue_count = bfs(i, j, 'B')
                enemy_power += blue_count ** 2

    print(my_power, enemy_power, end=' ')
