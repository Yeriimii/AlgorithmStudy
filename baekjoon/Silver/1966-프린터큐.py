from collections import deque

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    if n == 1:
        Q = deque()
        Q.append((0, int(input())))
    else:
        Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
        Q = deque(Q)

    cnt = 0
    while True:
        cur = Q.popleft()
        if any(cur[1] < x[1] for x in Q):
            Q.append(cur)
        else:
            cnt += 1
            if cur[0] == m:
                print(cnt)
                break
