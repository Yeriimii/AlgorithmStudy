from collections import deque

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()  # 하나 추출
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)  # 맨 뒤로 이동
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
