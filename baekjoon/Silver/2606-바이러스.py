from collections import deque


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    network = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1)
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        network[a][b] = 1
        network[b][a] = 1
    Q = deque()
    Q.append(1)
    ch[1] = 1
    while Q:
        cur = Q.popleft()
        for i in range(1, n+1):
            if network[cur][i] == 1 and ch[i] == 0:
                ch[i] = 1
                Q.append(i)
                cnt += 1
    print(cnt)
