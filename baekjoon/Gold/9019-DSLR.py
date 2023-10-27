import sys
from collections import deque


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        dis = [0 for _ in range(10001)]
        Q = deque()
        Q.append([A, ''])
        res = 2147000000
        while Q:
            now = Q.popleft()

            # 탐색 중단점
            if now[0] == B:
                if res > dis[now[0]]:
                    res = dis[now[0]]
                    print(now[1])
                    break

            # operator D
            o1 = (now[0] * 2) % 10000

            # operator S
            o2 = ((now[0] + 10000) - 1) % 10000

            if len(str(now[0])) == 4:
                zero = ''
            elif len(str(now[0])) == 1:
                zero = '0' * 3
            else:
                zero = '0' * (4 // len(str(now[0])))

            tmp = zero + str(now[0])
            # operator L
            o3 = int(tmp[1:4] + tmp[0])
            # operator R
            o4 = int(tmp[3] + tmp[:3])

            for next in (o1, o2, o3, o4):
                if dis[next] == 0:
                    dis[next] = dis[now[0]] + 1
                    if next == o1:
                        Q.append([o1, now[1] + 'D'])
                    elif next == o2:
                        Q.append([o2, now[1] + 'S'])
                    elif next == o3:
                        Q.append([o3, now[1] + 'L'])
                    elif next == o4:
                        Q.append([o4, now[1] + 'R'])
