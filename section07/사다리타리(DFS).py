def DFS(L, col):
    global res

    if board[L][col] == 0:
        return
    ch[L][col] = 1
    left = col - 1
    right = col + 1
    if L == 9:
        if board[L][col] == 2:
            res = 1
        return
    else:
        if 0 <= left < 10 and board[L][left] == 1 and ch[L][left] == 0:
            DFS(L, left)
        elif 0 <= right < 10 and board[L][right] == 1 and ch[L][right] == 0:
            DFS(L, right)
        else:
            DFS(L+1, col)


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(10)]
    res = 0
    for i in range(10):
        ch = [[0]*10 for _ in range(10)]
        DFS(0, i)
        if res == 1:
            print(i)
            break

'''
최적화 풀이 : 도착지점이 2인 열에서 역으로 출발
'''
def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


if __name__ == '__main__':

    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)
