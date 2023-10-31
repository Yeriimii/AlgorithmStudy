from collections import deque


if __name__ == '__main__':
    T = int(input())
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    for _ in range(T):
        l = int(input())
        board = [[0] * l for _ in range(l)]
        dis = [[0] * l for _ in range(l)]
        Q = deque()
        sa, sb = map(int, input().split())
        da, db = map(int, input().split())
        Q.append((sa, sb))
        while Q:
            x, y = Q.popleft()
            if x == da and y == db:
                print(dis[x][y])
                break
            for i in range(8):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < l and 0 <= yy < l and (dis[xx][yy] == 0 or dis[xx][yy] > dis[x][y] + 1):
                    dis[xx][yy] = dis[x][y] + 1
                    Q.append((xx, yy))
