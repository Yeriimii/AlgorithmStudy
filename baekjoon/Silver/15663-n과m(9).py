def DFS(L):
    if L == m:
        tmp = ''
        for j in range(L):
            tmp += str(res[j]) + ' '
        if tmp not in prev_res:
            print(tmp, end='')
            prev_res.add(tmp)
            print()
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = num[i]
                DFS(L+1)
                ch[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    prev_res = set()
    res = [0] * (n+1)
    ch = [0] * (n+1)
    DFS(0)
