from collections import deque

MAX = 100000
n, m = map(int, input().split())
ch = [0 for _ in range(MAX+1)]
dis = [0 for _ in range(MAX+1)]
ch[n] = 1
Q = deque()
Q.append([n, str(n)])
res = 2147000000
while Q:
    now, string = Q.popleft()
    if now == m:
        if res > dis[now]:
            res = dis[now]
            print(res)
            print(string)
            break
    if dis[now] > res:
        continue
    for next in (now*2, now-1, now+1):  # 이 순서대로 하지않으면 오답 -> (간선의 가중치 0)
        # 이유: https://www.acmicpc.net/board/view/38887#comment-69010
        if 0 <= next <= MAX and ch[next] == 0:
            ch[next] = 1
            dis[next] = dis[now] + 1
            Q.append([next, string + ' ' + str(next)])
