import sys
sys.setrecursionlimit(10**6)

def DFS(L, plus):
    global res, acsum
    if L == n:
        if res > acsum:
            res = acsum
    else:
        acsum += plus + P[L]
        DFS(L+1, plus + P[L])


if __name__ == '__main__':
    n = int(input())
    P = list(map(int, input().split()))
    P.sort()
    res = 2147000000
    acsum = 0
    DFS(0, 0)
    print(res)
