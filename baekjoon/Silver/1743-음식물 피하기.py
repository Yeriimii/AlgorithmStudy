from collections import deque

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [[False for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    answer = 0

    for _ in range(k):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = True

    q = deque()

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] is True:
                visited[i][j] = True
                q.append((i, j))
                cnt = 1
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr = r + dx[k]
                        nc = c + dy[k]
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] is True:
                            visited[nr][nc] = True
                            cnt += 1
                            q.append((nr, nc))
                answer = max(answer, cnt)
    print(answer)
