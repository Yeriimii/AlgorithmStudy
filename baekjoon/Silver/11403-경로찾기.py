import sys

sys.setrecursionlimit(10**6)

def DFS(node):
    for k in range(n):
        if board[node][k] == 1 and ch[node][k] == 0:
            board[start][k] = 1
            ch[node][k] = 1
            DFS(k)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        start = i
        ch = [[0] * n for _ in range(n)]
        DFS(i)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
