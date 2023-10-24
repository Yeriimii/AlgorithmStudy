import sys
from collections import deque

MAX = 100000
N, K = map(int, sys.stdin.readline().split())
Q = deque()
Q.append(N)
dis = [0] * (MAX + 1)  # 최대 크기
cnt, res = 0, 0
while Q:
    now = Q.popleft()
    if now == K:  # 둘이 만났을 때
        res = dis[now]  # 결과
        cnt += 1  # 방문 횟수 +1
        continue

    for next in [now - 1, now + 1, now * 2]:
        # 범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
        if 0 <= next <= MAX and (dis[next] == 0 or dis[next] == dis[now] + 1):
            dis[next] = dis[now] + 1
            Q.append(next)
print(res)
print(cnt)
