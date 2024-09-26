def dfs(x: int, y: int, dist: int):
    global answer

    board[x][y] = 'T'
    if x == 0 and y == c - 1 and dist == k:
        answer += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'T':
                board[nx][ny] = 'T'
                dfs(nx, ny, dist + 1)
                board[nx][ny] = '.'


if __name__ == '__main__':
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    r, c, k = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    answer = 0
    dfs(r - 1, 0, 1)
    print(answer)
