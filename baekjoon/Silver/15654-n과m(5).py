def DFS(L, s):
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
    else:
        for i in range(s, n):
            res[L] = num[i]
            DFS(L+1, i)


if __name__ == '__main__':
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    res = [0] * n
    DFS(0, 0)
