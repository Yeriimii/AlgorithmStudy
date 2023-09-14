def DFS(L, sum: int):
    global res

    if L > res:  # cut edge
        return

    if sum > m:  # cut
        return

    if sum == m:
        if res > L:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+k[i])


if __name__ == '__main__':
    n = int(input())
    k = list(map(int, input().split()))
    k.sort(reverse=True)
    m = int(input())
    res = 2147000000
    DFS(0, 0)
    print(res)
