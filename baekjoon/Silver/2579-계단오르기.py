def DFS(L):
    if dy[L] > 0:
        return dy[L]

    if L == 0 or L == 1:
        return dy[L]

    if L == 2:
        dy[L] = dy[1] + s[L]
        return dy[L]

    dy[L] = max(DFS(L-2), s[L-1]+DFS(L-3)) + s[L]
    return dy[L]


if __name__ == '__main__':
    n = int(input())
    s = [int(input()) for _ in range(n)]
    s.insert(0, 0)
    dy = [0] * (n+1)
    dy[1] = s[1]
    print(DFS(n))
