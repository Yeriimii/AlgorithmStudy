from collections import deque

def DFS(L, s):
    ch[s] = 1
    print(s, end=' ')
    if L == n:
        return
    else:
        for i in range(1, n+1):
            if board[s][i] == 1 and ch[i] == 0:
                DFS(L+1, i)

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    board = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        board[a][b] = 1
        board[b][a] = 1
    DFS(0, v)

    print()
    ch = [0] * (n + 1)
    Q = deque()
    Q.append(v)
    ch[v] = 1
    while Q:
        node = Q.popleft()
        print(node, end=' ')
        for i in range(1, n+1):
            if board[node][i] == 1 and ch[i] == 0:
                ch[i] = 1
                Q.append(i)
