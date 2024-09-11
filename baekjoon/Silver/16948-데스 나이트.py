from collections import deque


def bfs():
    global answer
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    cnt = 0
    q.append((r1, c1, cnt))
    visited[r1][c1] = True
    while q:
        r, c, cur_cnt = q.popleft()
        if r == r2 and c == c2:
            answer = min(answer, cur_cnt)
            return
        for i in range(6):
            nr = r + moves[i][0]
            nc = c + moves[i][1]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, cur_cnt + 1))


if __name__ == '__main__':
    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())
    moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    answer = 2e9
    bfs()

    if r1 == r2 and c1 == c2:
        print(0)
    elif answer != 2e9:
        print(answer)
    else:
        print(-1)
