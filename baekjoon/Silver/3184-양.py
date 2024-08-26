from collections import deque


def bfs(y: int, x: int):
    q = deque()
    q.append((y, x))

    while q:
        _r, _c = q.popleft()
        for _i in range(4):
            nx = _c + dx[_i]
            ny = _r + dy[_i]
            if 0 <= nx < c and 0 <= ny < r and board[ny][nx] != "#" and not visited[ny][nx]:
                visited[ny][nx] = True
                if board[ny][nx] == "o":
                    o_xy.append((ny, nx))
                elif board[ny][nx] == "v":
                    v_xy.append((ny, nx))
                q.append((ny, nx))

    return o_xy, v_xy


if __name__ == '__main__':
    r, c = map(int, input().split())
    board = [input() for _ in range(r)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = [[False for _ in range(c)] for _ in range(r)]

    total_o_cnt = 0
    total_v_cnt = 0

    for i in range(r):
        for j in range(c):
            if board[i][j] != "#" and not visited[i][j]:
                visited[i][j] = True
                o_xy = []
                v_xy = []

                if board[i][j] == "o":
                    o_xy.append((i, j))
                elif board[i][j] == "v":
                    v_xy.append((i, j))

                o_xy, v_xy = bfs(i, j)

                if len(o_xy) > len(v_xy):
                    total_o_cnt += len(o_xy)
                    for (k, l) in v_xy:
                        board[k][l].replace("v", ".")
                else:
                    total_v_cnt += len(v_xy)
                    for (k, l) in o_xy:
                        board[k][l].replace("o", ".")

    print(total_o_cnt, total_v_cnt, end=' ')
