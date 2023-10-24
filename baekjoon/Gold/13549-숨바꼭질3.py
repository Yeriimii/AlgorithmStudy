from collections import deque

MAX = 100000
n, m = map(int, input().split())
ch = [0 for _ in range(MAX+1)]
dis = [0 for _ in range(MAX+1)]
ch[n] = 1
Q = deque()
Q.append(n)
res = 2147000000
while Q:
    now = Q.popleft()
    if now == m:
        if res > dis[now]:
            res = dis[now]
    if dis[now] > res:
        continue
    for next in (now*2, now-1, now+1):  # 이 순서대로 하지않으면 오답 -> (간선의 가중치 0)
        # 이유: https://www.acmicpc.net/board/view/38887#comment-69010
        if 0 <= next <= MAX and ch[next] == 0:
            ch[next] = 1
            if next != now*2:
                dis[next] = dis[now] + 1
            else:
                dis[next] = dis[now]
            Q.append(next)
print(res)

from collections import deque

n, k = map(int, input().split())
visit = [0] * 100001
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
        Q.append((multi, cur[1]))
    if 0 <= left and visit[left] == 0:
        Q.append((left, cur[1]+1))
    if right <= 100000 and visit[right] == 0:
        Q.append((right, cur[1]+1))
print(res)
