import sys

def DFS(L, sub):
    global cnt

    if sub < 0:
        return

    if sub == 0:
        cnt += 1
    else:
        for i in range(1, 4):
            DFS(L+1, sub-i)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        cnt = 0
        n = int(sys.stdin.readline())
        DFS(0, n)
        print(cnt)
