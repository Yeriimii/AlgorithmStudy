def DFS(L, s):
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i)


if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * (n+1)
    DFS(0, 1)
