import sys

if __name__ == '__main__':
    n = int(input())
    T = list()
    P = list()
    dy = [0] * (n+2)
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        T.append(a)
        P.append(b)
    T.insert(0, 0)
    P.insert(0, 0)
    res = 0
    for i in range(1, n+2):
        dy[i] = max(dy[i], dy[i-1])
        if i == n+1:
            break
        if i + T[i] <= n+1:
            dy[i+T[i]] = max(dy[i]+P[i], dy[i+T[i]])

    print(dy[n+1])
