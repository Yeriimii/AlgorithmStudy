def DFS(L, s):
    if dy[L][s] > 0:
        return dy[L][s]

    if L == 1:
        res = 0
        for j in range(s):
            res += 1
        dy[L][s] = res
        return dy[L][s]
    else:
        for k in range(s-1, L-2, -1):
            dy[L][s] += DFS(L-1, k)
        return dy[L][s]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        dy = [[0] * (b+1) for _ in range(a+1)]
        dy[a][a] = 1
        DFS(a, b)
        print(dy[a][b])
