from collections import deque


def find_coordinate(_favorites: list):
    q = deque()
    lst = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                q.append((i, j))
                f_cnt = 0
                e_cnt = 0
                while q:
                    _r, _c = q.popleft()
                    for _k in range(4):
                        nr = _r + dx[_k]
                        nc = _c + dy[_k]
                        if 0 <= nr < n and 0 <= nc < n:
                            if board[nr][nc] in _favorites:
                                f_cnt += 1
                            if board[nr][nc] == 0:
                                e_cnt += 1
                lst.append((f_cnt, e_cnt, (i, j)))
    return sorted(lst, key=lambda x: (x[0], x[1]), reverse=True)[0][2]


def calc_score():
    score = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            q.append((i, j))
            cnt = 0
            while q:
                _r, _c = q.popleft()
                for k in range(4):
                    nr = _r + dx[k]
                    nc = _c + dy[k]
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] in favorite_friends[board[i][j]]:
                        cnt += 1
            if cnt > 0:
                score += 10 ** (cnt - 1)
    return score


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    favorite_friends = dict()
    for _ in range(n ** 2):
        s, a, b, c, d = map(int, input().split())
        friends = [a, b, c, d]
        favorite_friends[s] = friends
        r, c = find_coordinate(friends)
        board[r][c] = s
    print(calc_score())
