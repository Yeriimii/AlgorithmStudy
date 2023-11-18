from collections import deque

n, m = map(int, input().split())
A = list()
B = list()
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n * 2):
    if i < n:
        A.append(' '.join(input()).split())
    else:
        B.append(' '.join(input()).split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
for i in range(n):
    for j in range(m):
        if (not visited[i][j]) and (A[i][j] != B[i][j]):
            prev_color = A[i][j]
            apply_color = B[i][j]
            A[i][j] = apply_color
            visited[i][j] = True
            Q.append((i, j))
            while Q:
                x, y = Q.popleft()
                for k in range(4):
                    xx = dx[k] + x
                    yy = dy[k] + y
                    if 0 <= xx < n and 0 <= yy < m and (not visited[xx][yy]) and (A[xx][yy] == prev_color):
                        A[xx][yy] = apply_color
                        visited[xx][yy] = True
                        Q.append((xx, yy))

cnt = 0
for i in range(n):
    for j in range(m):
        if A[i][j] == B[i][j]:
            cnt += 1

if cnt == n * m:
    print("YES")
else:
    print("NO")
