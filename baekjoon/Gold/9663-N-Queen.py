def check(prev_L):
    for i in range(prev_L):
        if (board[prev_L] == board[i]) or (prev_L - i == abs(board[prev_L] - board[i])):  # 좌우, 대각선 검사
            return False
    return True


def DFS(L):
    global res

    if L == n:
        res += 1
    else:
        for i in range(n):
            if visit[i] == False:
                board[L] = i  # (L, i)에 퀸 위치

                if check(L):  # 좌우 대각선에 퀸이 있는지 검사
                    visit[i] = True  # 없으면 i 열에 퀸 위치
                    DFS(L+1)  # 다음 행으로 이동
                    visit[i] = False  # 백트래킹


if __name__ == '__main__':
    n = int(input())
    board = [0] * n
    visit = [False] * n
    res = 0
    DFS(0)
    print(res)

