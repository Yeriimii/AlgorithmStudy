def dfs(k, n):
    if apartment[k][n] > 0:
        return apartment[k][n]
    else:
        res = 0
        for i in range(1, n + 1):
            apartment[k - 1][i] = dfs(k - 1, i)
            res += apartment[k - 1][i]
        return res


apartment = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    apartment[0][i] = i

T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    print(dfs(K, N))
