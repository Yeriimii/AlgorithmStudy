from collections import deque

n, k = map(int, input().split())
visit = [0] * 100000
Q = deque()
Q.append((n, 0))
res = 2147000000
while Q:
    cur = Q.popleft()
    visit[cur[0]] = 1
    if cur[0] == k:
        if cur[1] < res:
            res = cur[1]
    if cur[1] > res:
        continue
    left = cur[0] - 1
    right = cur[0] + 1
    multi = cur[0] * 2
    if multi <= 100000 and visit[multi] == 0:
        Q.append((multi, cur[1]+1))
    if 0 <= left and visit[left] == 0:
        Q.append((left, cur[1]+1))
    if right <= 100000 and visit[right] == 0:
        Q.append((right, cur[1]+1))
print(res)
