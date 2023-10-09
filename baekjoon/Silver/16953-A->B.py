def DFS(L, num):
    global res

    if num > b:
        return
    if num == b:
        if res > L:
            res = L
    else:
        DFS(L+1, num*2)
        DFS(L+1, num*10 + 1)


if __name__ == '__main__':
    a, b = map(int, input().split())
    res = 2147000000
    DFS(0, a)
    if res < 2147000000:
        print(res+1)
    else:
        print(-1)
