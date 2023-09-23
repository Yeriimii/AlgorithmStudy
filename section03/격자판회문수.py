board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:  # 행에서 회문 검사 tmp.reverse()
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-(k+1)][j]:  # 열에서 회문 검사
                break
        else:
            cnt += 1
print(cnt)
