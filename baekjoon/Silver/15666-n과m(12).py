def DFS(L, s):
    if L == m:
        for z in range(L):
            print(res[z], end=' ')
        print()
    else:
        for i in range(s, len(num_list)):
            res[L] = num_list[i]
            DFS(L+1, i)


if __name__ == '__main__':
    n, m = map(int, input().split())
    num_list = sorted(list(set(map(int, input().split()))))
    res = [0] * (n+1)
    DFS(0, 0)
